#!/usr/bin/env python3
"""
MrBeast $1M Puzzle Solver — Agentic Vision Pipeline
====================================================
Uses Gemini 3 Flash's Agentic Vision (code execution + thinking)
to analyze every video frame for hidden clues, puzzles, and patterns.

Persona: World's best enigmatologist, cruciverbalist, solutionist,
         and puzzle solver.

Features:
  - Resumable: skips already-analyzed frames
  - Rate-limited with exponential backoff
  - Concurrent processing with configurable workers
  - Per-frame JSON results + master summary
  - Agentic vision: model can zoom, crop, enhance, annotate

Setup:
  1. pip install google-genai
  2. export GEMINI_API_KEY="your-api-key-here"
  3. Place video frame JPGs in subfolders (see VIDEO_FOLDERS below)
  4. python puzzle_solver.py
"""

import os
import sys
import json
import time
import glob
import base64
import logging
import argparse
import hashlib
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock, Semaphore

from google import genai
from google.genai import types

# ─── Configuration ────────────────────────────────────────────────────────────

API_KEY = os.environ.get("GEMINI_API_KEY", "")
if not API_KEY:
    print("ERROR: Set the GEMINI_API_KEY environment variable.")
    print("  export GEMINI_API_KEY='your-api-key-here'")
    sys.exit(1)

MODEL = "gemini-3-flash-preview"

# Rate limiting (adjust based on your API tier)
MAX_WORKERS = 5          # concurrent threads
RPM_LIMIT = 28           # requests per minute (stay under 30 free tier)
REQUESTS_PER_SECOND = RPM_LIMIT / 60.0
MIN_REQUEST_INTERVAL = 1.0 / REQUESTS_PER_SECOND

# Retry settings
MAX_RETRIES = 5
BASE_RETRY_DELAY = 2.0   # seconds

BASE_DIR = Path(__file__).parent.parent  # assumes pipeline/ is inside the project root
RESULTS_DIR = BASE_DIR / "puzzle_analysis"

# ─── The Puzzle Solver System Prompt ──────────────────────────────────────────

SYSTEM_PROMPT = """You are the world's foremost enigmatologist, cruciverbalist, solutionist, and puzzle solver — a composite mind combining the brilliance of Will Shortz, Marcel Danesi, and Alan Turing. You have been hired to analyze video frames from MrBeast challenge videos where $1,000,000 is hidden behind puzzles, riddles, hidden clues, and encoded messages.

YOUR MISSION: Analyze this single video frame with EXTREME forensic attention. You are looking for ANYTHING that could be a clue to winning $1,000,000.

ANALYSIS PROTOCOL — Examine each of these dimensions:

1. **TEXT & TYPOGRAPHY**: Every visible word, number, letter, symbol. Look for:
   - Obvious text (signs, screens, captions, overlays)
   - Subtle/hidden text (watermarks, small print, reversed text, text in reflections)
   - Unusual fonts, letter spacing, capitalization patterns (acrostics, ciphers)
   - Numbers that could be coordinates, dates, codes, URLs, phone numbers
   - Text partially obscured or split across elements

2. **VISUAL CODES & SYMBOLS**:
   - QR codes, barcodes, Data Matrix codes (even partial or distorted)
   - Morse code patterns (flashing lights, dot/dash arrangements)
   - Semaphore, Braille, sign language, nautical flags
   - Mathematical symbols or equations
   - Chemical formulas or scientific notation
   - Musical notation

3. **SPATIAL & GEOMETRIC CLUES**:
   - Unusual arrangements of objects that could form letters/numbers
   - Color patterns that seem deliberate (RGB values, hex codes)
   - Grid patterns, mazes, connect-the-dots possibilities
   - Compass directions, arrows, pointers
   - Map-like features, coordinate grids

4. **STEGANOGRAPHIC INDICATORS**:
   - Areas of unusual pixel density or color banding
   - Regions that look artificially smooth or noisy
   - Color channels that seem to carry different information
   - Suspicious patterns in shadows or highlights

5. **CONTEXTUAL PUZZLE ELEMENTS**:
   - Objects that seem deliberately placed or out of context
   - Things that break the "fourth wall" or address the viewer
   - References to other MrBeast videos, internet culture, or puzzle traditions
   - Countdown elements, sequence indicators (suggesting multi-frame clues)
   - Props or background items that encode information

6. **TEMPORAL MARKERS**:
   - Frame counters, timecodes, or sequence numbers visible
   - Elements that suggest "look at frame X" or "combine with another frame"
   - Transition artifacts that might hide single-frame messages

USE YOUR CODE EXECUTION to:
- Zoom into suspicious regions and examine them in detail
- Enhance contrast/brightness of dark or subtle areas
- Isolate color channels to look for hidden data
- Apply edge detection or other filters to reveal hidden patterns
- Decode any QR codes or barcodes found
- Analyze pixel patterns for steganographic content
- Convert any found codes (binary, hex, base64, morse) to plaintext

OUTPUT FORMAT (respond in valid JSON):
{
  "frame_id": "<filename>",
  "confidence_score": <0.0 to 1.0 — how likely this frame contains a meaningful clue>,
  "primary_content": "<brief description of what's visually dominant in the frame>",
  "clues_found": [
    {
      "type": "<text|code|symbol|spatial|steganographic|contextual|temporal>",
      "description": "<what you found>",
      "raw_value": "<exact text/code/number if applicable>",
      "decoded_value": "<decoded meaning if you could decode it>",
      "location": "<where in the frame: top-left, center, bottom-right, etc.>",
      "confidence": <0.0 to 1.0>
    }
  ],
  "code_execution_findings": "<summary of what your code analysis revealed>",
  "cross_frame_notes": "<anything suggesting this connects to other frames>",
  "puzzle_theory": "<your expert hypothesis about what this clue means or how it fits>"
}

If the frame appears to be a normal video frame with no puzzle elements, still note any text, numbers, or notable visual elements — seemingly mundane details can be part of a larger pattern across frames.

BE THOROUGH. BE RELENTLESS. $1,000,000 is at stake."""

# ─── Logging Setup ────────────────────────────────────────────────────────────

def setup_logging(results_dir):
    """Configure logging to both file and console."""
    log_file = results_dir / "pipeline.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger("puzzle_solver")


# ─── Rate Limiter ─────────────────────────────────────────────────────────────

class RateLimiter:
    """Thread-safe token bucket rate limiter."""

    def __init__(self, rpm_limit):
        self.min_interval = 60.0 / rpm_limit
        self.lock = Lock()
        self.last_request_time = 0

    def acquire(self):
        """Block until we can make a request within rate limits."""
        with self.lock:
            now = time.time()
            elapsed = now - self.last_request_time
            if elapsed < self.min_interval:
                sleep_time = self.min_interval - elapsed
                time.sleep(sleep_time)
            self.last_request_time = time.time()


# ─── Core Analysis Function ──────────────────────────────────────────────────

def analyze_frame(client, frame_path, rate_limiter, logger, video_name):
    """
    Analyze a single frame using Gemini 3 Flash Agentic Vision.
    Returns the analysis result dict or None on failure.
    """
    frame_name = os.path.basename(frame_path)

    for attempt in range(MAX_RETRIES):
        try:
            rate_limiter.acquire()

            # Read image bytes
            with open(frame_path, "rb") as f:
                image_bytes = f.read()

            image_part = types.Part.from_bytes(
                data=image_bytes,
                mime_type="image/jpeg"
            )

            prompt = f"""Video: "{video_name}"
Frame: {frame_name}

Analyze this video frame following your complete analysis protocol.
Use code execution to zoom in, enhance, and decode anything suspicious.
Respond with the JSON analysis object ONLY."""

            response = client.models.generate_content(
                model=MODEL,
                contents=[image_part, prompt],
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    tools=[types.Tool(code_execution=types.ToolCodeExecution)],
                    thinking_config=types.ThinkingConfig(thinking_level="HIGH"),
                    temperature=0.1,  # low temp for analytical precision
                ),
            )

            # Extract the text response
            response_text = ""
            code_outputs = []

            for part in response.candidates[0].content.parts:
                if hasattr(part, 'text') and part.text:
                    response_text += part.text
                if hasattr(part, 'executable_code') and part.executable_code:
                    code_outputs.append({
                        "code": part.executable_code.code,
                    })
                if hasattr(part, 'code_execution_result') and part.code_execution_result:
                    code_outputs.append({
                        "output": part.code_execution_result.output,
                    })

            # Try to parse JSON from response
            result = None
            # Try to find JSON in the response
            try:
                # Look for JSON block in markdown
                if "```json" in response_text:
                    json_str = response_text.split("```json")[1].split("```")[0].strip()
                elif "```" in response_text:
                    json_str = response_text.split("```")[1].split("```")[0].strip()
                else:
                    json_str = response_text.strip()
                result = json.loads(json_str)
            except (json.JSONDecodeError, IndexError):
                # If JSON parsing fails, wrap the raw response
                result = {
                    "frame_id": frame_name,
                    "raw_response": response_text,
                    "parse_error": True,
                    "confidence_score": 0.0,
                    "clues_found": []
                }

            # Attach code execution outputs if any
            if code_outputs:
                result["_code_execution_log"] = code_outputs

            # Attach metadata
            result["_metadata"] = {
                "video": video_name,
                "frame_file": frame_name,
                "model": MODEL,
                "timestamp": datetime.now().isoformat(),
                "attempt": attempt + 1
            }

            logger.info(
                f"✓ {frame_name} | confidence={result.get('confidence_score', '?')} | "
                f"clues={len(result.get('clues_found', []))} | "
                f"code_exec={'yes' if code_outputs else 'no'}"
            )
            return result

        except Exception as e:
            error_str = str(e)

            # Check for rate limit errors
            if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                delay = BASE_RETRY_DELAY * (2 ** attempt) + (attempt * 5)
                logger.warning(
                    f"⏳ Rate limited on {frame_name}, retry {attempt+1}/{MAX_RETRIES} "
                    f"in {delay:.0f}s"
                )
                time.sleep(delay)
                continue

            # Other retryable errors
            if attempt < MAX_RETRIES - 1:
                delay = BASE_RETRY_DELAY * (2 ** attempt)
                logger.warning(
                    f"⚠ Error on {frame_name}: {error_str[:100]}... "
                    f"retry {attempt+1}/{MAX_RETRIES} in {delay:.0f}s"
                )
                time.sleep(delay)
                continue

            logger.error(f"✗ FAILED {frame_name} after {MAX_RETRIES} attempts: {error_str[:200]}")
            return {
                "frame_id": frame_name,
                "error": error_str[:500],
                "confidence_score": 0.0,
                "clues_found": [],
                "_metadata": {
                    "video": video_name,
                    "frame_file": frame_name,
                    "model": MODEL,
                    "timestamp": datetime.now().isoformat(),
                    "failed": True
                }
            }

    return None


# ─── Video Processing ─────────────────────────────────────────────────────────

def process_video_folder(client, folder_path, video_name, rate_limiter, logger,
                         results_subdir, max_frames=None, workers=MAX_WORKERS):
    """Process all frames in a video folder."""

    os.makedirs(results_subdir, exist_ok=True)

    # Get all frame files, sorted
    frames = sorted(glob.glob(os.path.join(folder_path, "*.jpg")))

    if max_frames:
        frames = frames[:max_frames]

    # Check which frames are already analyzed (resume support)
    already_done = set()
    for f in glob.glob(os.path.join(results_subdir, "*.json")):
        fname = os.path.basename(f).replace(".json", ".jpg")
        already_done.add(fname)

    remaining = [f for f in frames if os.path.basename(f) not in already_done]

    logger.info(
        f"\n{'='*60}\n"
        f"📹 {video_name}\n"
        f"   Total frames: {len(frames)}\n"
        f"   Already analyzed: {len(already_done)}\n"
        f"   Remaining: {len(remaining)}\n"
        f"{'='*60}"
    )

    if not remaining:
        logger.info(f"   ✓ All frames already analyzed!")
        return len(frames), 0

    completed = 0
    failed = 0
    high_confidence = []

    with ThreadPoolExecutor(max_workers=workers) as executor:
        future_to_frame = {
            executor.submit(
                analyze_frame, client, frame, rate_limiter, logger, video_name
            ): frame
            for frame in remaining
        }

        for future in as_completed(future_to_frame):
            frame_path = future_to_frame[future]
            frame_name = os.path.basename(frame_path)

            try:
                result = future.result()

                if result:
                    # Save individual result
                    result_file = os.path.join(
                        results_subdir,
                        frame_name.replace(".jpg", ".json")
                    )
                    with open(result_file, "w") as f:
                        json.dump(result, f, indent=2)

                    completed += 1

                    # Track high-confidence finds
                    score = result.get("confidence_score", 0)
                    if isinstance(score, (int, float)) and score >= 0.5:
                        high_confidence.append({
                            "frame": frame_name,
                            "score": score,
                            "clues": result.get("clues_found", []),
                            "theory": result.get("puzzle_theory", "")
                        })
                        logger.info(
                            f"🔥 HIGH CONFIDENCE ({score}) in {frame_name}: "
                            f"{result.get('puzzle_theory', 'n/a')[:100]}"
                        )
                else:
                    failed += 1

            except Exception as e:
                failed += 1
                logger.error(f"✗ Exception processing {frame_name}: {e}")

            # Progress update every 25 frames
            total_done = completed + failed
            if total_done % 25 == 0:
                pct = (total_done / len(remaining)) * 100
                logger.info(
                    f"   📊 Progress: {total_done}/{len(remaining)} "
                    f"({pct:.1f}%) | ✓{completed} ✗{failed}"
                )

    # Save high-confidence summary for this video
    if high_confidence:
        summary_file = os.path.join(results_subdir, "_HIGH_CONFIDENCE_CLUES.json")
        high_confidence.sort(key=lambda x: x.get("score", 0), reverse=True)
        with open(summary_file, "w") as f:
            json.dump(high_confidence, f, indent=2)
        logger.info(
            f"🏆 {len(high_confidence)} high-confidence clues saved to "
            f"_HIGH_CONFIDENCE_CLUES.json"
        )

    return completed, failed


# ─── Master Summary Generator ────────────────────────────────────────────────

def generate_master_summary(results_dir, logger):
    """Aggregate all findings into a master summary."""

    logger.info("\n" + "="*60 + "\n🧩 Generating Master Summary\n" + "="*60)

    all_clues = []
    total_frames = 0
    total_high_conf = 0
    video_summaries = {}

    for video_dir in sorted(results_dir.iterdir()):
        if not video_dir.is_dir() or video_dir.name.startswith("_"):
            continue

        video_name = video_dir.name
        video_clues = []
        frame_count = 0

        for json_file in sorted(video_dir.glob("*.json")):
            if json_file.name.startswith("_"):
                continue

            try:
                with open(json_file) as f:
                    result = json.load(f)

                frame_count += 1
                score = result.get("confidence_score", 0)
                clues = result.get("clues_found", [])

                if isinstance(score, (int, float)) and score >= 0.3:
                    for clue in clues:
                        clue["_source_frame"] = result.get("frame_id", json_file.stem)
                        clue["_source_video"] = video_name
                        clue["_frame_confidence"] = score
                        video_clues.append(clue)
                        all_clues.append(clue)

                if isinstance(score, (int, float)) and score >= 0.5:
                    total_high_conf += 1

            except (json.JSONDecodeError, KeyError) as e:
                logger.warning(f"   Skip malformed: {json_file.name}: {e}")

        total_frames += frame_count
        video_summaries[video_name] = {
            "frames_analyzed": frame_count,
            "clues_found": len(video_clues),
            "top_clues": sorted(
                video_clues,
                key=lambda x: x.get("confidence", 0),
                reverse=True
            )[:20]  # top 20 per video
        }

        logger.info(
            f"   📹 {video_name}: {frame_count} frames, "
            f"{len(video_clues)} clues"
        )

    # Sort all clues by confidence
    all_clues.sort(key=lambda x: x.get("confidence", 0), reverse=True)

    master = {
        "generated_at": datetime.now().isoformat(),
        "model": MODEL,
        "total_frames_analyzed": total_frames,
        "total_high_confidence_frames": total_high_conf,
        "total_clues_extracted": len(all_clues),
        "video_summaries": video_summaries,
        "top_50_clues": all_clues[:50],
        "all_clues_by_type": {}
    }

    # Group clues by type
    for clue in all_clues:
        ctype = clue.get("type", "unknown")
        if ctype not in master["all_clues_by_type"]:
            master["all_clues_by_type"][ctype] = []
        master["all_clues_by_type"][ctype].append(clue)

    summary_path = results_dir / "MASTER_SUMMARY.json"
    with open(summary_path, "w") as f:
        json.dump(master, f, indent=2)

    logger.info(
        f"\n{'='*60}\n"
        f"🏆 MASTER SUMMARY\n"
        f"   Total frames analyzed: {total_frames}\n"
        f"   High-confidence frames: {total_high_conf}\n"
        f"   Total clues extracted: {len(all_clues)}\n"
        f"   Saved to: {summary_path}\n"
        f"{'='*60}"
    )

    return master


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="MrBeast $1M Puzzle Solver — Gemini Agentic Vision Pipeline"
    )
    parser.add_argument(
        "--max-frames", type=int, default=None,
        help="Max frames per video (for testing). Omit to process ALL frames."
    )
    parser.add_argument(
        "--workers", type=int, default=MAX_WORKERS,
        help=f"Concurrent worker threads (default: {MAX_WORKERS})"
    )
    parser.add_argument(
        "--rpm", type=int, default=RPM_LIMIT,
        help=f"Requests per minute limit (default: {RPM_LIMIT})"
    )
    parser.add_argument(
        "--video", type=str, default=None,
        help="Process only this video folder name (e.g., 'superbowl_ad_1M_frames')"
    )
    parser.add_argument(
        "--summary-only", action="store_true",
        help="Skip analysis, just regenerate the master summary from existing results"
    )
    args = parser.parse_args()

    # Setup
    os.makedirs(RESULTS_DIR, exist_ok=True)
    logger = setup_logging(RESULTS_DIR)

    logger.info(
        f"\n{'#'*60}\n"
        f"# MrBeast $1M Puzzle Solver\n"
        f"# Model: {MODEL} (Agentic Vision + Code Execution)\n"
        f"# Workers: {args.workers} | RPM: {args.rpm}\n"
        f"# Max frames/video: {args.max_frames or 'ALL'}\n"
        f"# Started: {datetime.now().isoformat()}\n"
        f"{'#'*60}"
    )

    if args.summary_only:
        generate_master_summary(RESULTS_DIR, logger)
        return

    # Initialize client
    client = genai.Client(api_key=API_KEY)
    rate_limiter = RateLimiter(args.rpm)

    # Define video folders and their display names
    # Place your extracted frames in these folders relative to the project root:
    #   <project_root>/first_to_find_1M_frames/*.jpg
    #   <project_root>/slack_ad_frames/*.jpg
    #   etc.
    videos = [
        {
            "folder": "first_to_find_1M_frames",
            "name": "First To Find $1,000,000, Keeps It!"
        },
        {
            "folder": "slack_ad_frames",
            "name": "One Idea. 27 Days. Built with Slack."
        },
        {
            "folder": "rewatch_to_win_1M_frames",
            "name": "Rewatch This Video to Win $1,000,000"
        },
        {
            "folder": "superbowl_ad_1M_frames",
            "name": "Watch My Super Bowl Ad To Win $1,000,000!"
        },
    ]

    # Filter to specific video if requested
    if args.video:
        videos = [v for v in videos if v["folder"] == args.video]
        if not videos:
            logger.error(f"Video folder '{args.video}' not found!")
            return

    total_completed = 0
    total_failed = 0
    start_time = time.time()

    for video in videos:
        folder_path = BASE_DIR / video["folder"]
        results_subdir = RESULTS_DIR / video["folder"]

        if not folder_path.exists():
            logger.warning(f"Skipping {video['folder']} — folder not found")
            continue

        completed, failed = process_video_folder(
            client=client,
            folder_path=str(folder_path),
            video_name=video["name"],
            rate_limiter=rate_limiter,
            logger=logger,
            results_subdir=str(results_subdir),
            max_frames=args.max_frames,
            workers=args.workers
        )
        total_completed += completed
        total_failed += failed

    elapsed = time.time() - start_time
    elapsed_min = elapsed / 60

    logger.info(
        f"\n{'='*60}\n"
        f"📊 PIPELINE COMPLETE\n"
        f"   Frames analyzed: {total_completed}\n"
        f"   Failed: {total_failed}\n"
        f"   Time: {elapsed_min:.1f} minutes\n"
        f"   Avg: {elapsed/max(total_completed,1):.1f}s per frame\n"
        f"{'='*60}"
    )

    # Generate master summary
    generate_master_summary(RESULTS_DIR, logger)

    logger.info("\n🎯 Pipeline finished! Check puzzle_analysis/MASTER_SUMMARY.json for results.\n")


if __name__ == "__main__":
    main()
