# Pipeline — Agentic Vision Video Analyzer

The automated analysis pipeline that powers this project. Feeds every video frame to **Gemini 3 Flash Preview** with agentic vision (code execution + thinking), then aggregates findings into structured JSON.

## Quick Start

```bash
# 1. Install the dependency
pip install google-genai

# 2. Set your Gemini API key
export GEMINI_API_KEY="your-api-key-here"

# 3. Extract frames from your videos (1 frame per second)
ffmpeg -i video.mp4 -vf "fps=1" video_frames/frame_%05d.jpg

# 4. Run the pipeline
cd pipeline
./run_puzzle_solver.sh
```

## Frame Extraction

Use ffmpeg to extract frames at 1fps from each video:

```bash
ffmpeg -i "First To Find.mp4" -vf "fps=1" first_to_find_1M_frames/f%05d.jpg
ffmpeg -i "Slack Ad.mp4" -vf "fps=1" slack_ad_frames/f%05d.jpg
ffmpeg -i "Rewatch.mp4" -vf "fps=1" rewatch_to_win_1M_frames/f%05d.jpg
ffmpeg -i "Super Bowl Ad.mp4" -vf "fps=1" superbowl_ad_1M_frames/f%05d.jpg
```

Place each set of frames in its corresponding folder at the project root.

## Usage

```bash
./run_puzzle_solver.sh              # Analyze all frames from all videos
./run_puzzle_solver.sh test         # Test on 3 frames per video
./run_puzzle_solver.sh summary      # Regenerate master summary only
./run_puzzle_solver.sh <folder>     # Analyze one video only
```

The pipeline is **resumable** — rerun it and it picks up where it left off (skips already-analyzed frames). Safe to Ctrl+C at any time.

## Configuration

Edit the top of `puzzle_solver.py` to tune:

| Setting | Default | Description |
|---------|---------|-------------|
| `MAX_WORKERS` | 5 | Concurrent API threads |
| `RPM_LIMIT` | 28 | Requests per minute (free tier: stay under 30) |
| `MAX_RETRIES` | 5 | Retries per frame on failure |
| `MODEL` | `gemini-3-flash-preview` | Gemini model to use |

## Output

Results go to `puzzle_analysis/` at the project root:

```
puzzle_analysis/
  MASTER_SUMMARY.json              # Aggregated findings across all videos
  first_to_find_1M_frames/
    frame_00001.json               # Per-frame analysis
    _HIGH_CONFIDENCE_CLUES.json    # Top clues for this video
  slack_ad_frames/
    ...
```

Each frame JSON contains:
- `confidence_score` — how likely the frame contains a clue (0.0–1.0)
- `clues_found[]` — every detected clue with type, raw value, decoded value, and location
- `code_execution_findings` — what the model's code execution revealed
- `puzzle_theory` — the model's hypothesis about what it means
- `_code_execution_log` — full code execution traces

## Monitoring Scripts

**`monitor_puzzle.sh`** — Checks X/Twitter, Reddit, ARGNet, and YouTube for new puzzle developments. Run via cron for daily monitoring.

**`rerun_solver_new_videos.sh`** — Automatically downloads and analyzes new MrBeast videos containing puzzle keywords. Requires `yt-dlp` and `ffmpeg`.

## Requirements

- Python 3.10+
- `google-genai` Python package
- A [Google AI Studio](https://aistudio.google.com/) API key with Gemini 3 Flash access
- `ffmpeg` for frame extraction
- `yt-dlp` (optional, for auto-downloading new videos)
