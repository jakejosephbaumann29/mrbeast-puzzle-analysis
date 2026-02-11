#!/bin/bash
# Re-run puzzle solver on any new MrBeast videos
# Checks for new videos on the MrBeast channel and downloads + analyzes them
# Run daily via cron: 0 6 * * * /path/to/rerun_solver_new_videos.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$(dirname "$SCRIPT_DIR")"
LOG_DIR="$BASE_DIR/puzzle_monitor_logs"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/solver_rerun_$(date +%Y-%m-%d).log"

echo "=== Puzzle Solver Re-run Check - $(date) ===" | tee "$LOG_FILE"

# Check for API key
if [ -z "${GEMINI_API_KEY:-}" ]; then
    echo "ERROR: Set the GEMINI_API_KEY environment variable." | tee -a "$LOG_FILE"
    exit 1
fi

# Check if yt-dlp is available
if ! command -v yt-dlp &>/dev/null; then
    echo "ERROR: yt-dlp not installed. Install with: brew install yt-dlp" | tee -a "$LOG_FILE"
    exit 1
fi

# Check for new videos from MrBeast posted in the last 48 hours
echo "Checking for new MrBeast videos..." | tee -a "$LOG_FILE"
NEW_VIDEOS=$(yt-dlp --flat-playlist --print "%(id)s %(title)s" \
    --dateafter "$(date -v-2d +%Y%m%d)" \
    "https://www.youtube.com/@MrBeast/videos" 2>/dev/null || true)

if [ -z "$NEW_VIDEOS" ]; then
    echo "No new videos found in the last 48 hours." | tee -a "$LOG_FILE"
    exit 0
fi

echo "New videos found:" | tee -a "$LOG_FILE"
echo "$NEW_VIDEOS" | tee -a "$LOG_FILE"

# For each new video that contains puzzle-related keywords
echo "$NEW_VIDEOS" | while read -r VIDEO_ID VIDEO_TITLE; do
    if echo "$VIDEO_TITLE" | grep -qiE '(puzzle|vault|million|clue|salesforce|slack|find|win)'; then
        echo "" | tee -a "$LOG_FILE"
        echo ">>> Downloading puzzle-relevant video: $VIDEO_TITLE" | tee -a "$LOG_FILE"

        # Create safe folder name
        SAFE_NAME=$(echo "$VIDEO_TITLE" | tr -cd '[:alnum:] ' | tr ' ' '_' | head -c 50)
        VIDEO_DIR="$BASE_DIR/${SAFE_NAME}"
        FRAMES_DIR="$BASE_DIR/${SAFE_NAME}_frames"

        # Download video
        yt-dlp -o "$VIDEO_DIR.mp4" "https://youtube.com/watch?v=$VIDEO_ID" 2>>"$LOG_FILE" || continue

        # Extract frames at 1fps
        mkdir -p "$FRAMES_DIR"
        ffmpeg -i "$VIDEO_DIR.mp4" -vf "fps=1" "$FRAMES_DIR/${SAFE_NAME}_f%05d.jpg" 2>>"$LOG_FILE" || continue

        echo "Frames extracted to $FRAMES_DIR" | tee -a "$LOG_FILE"

        # Run puzzle solver on new frames
        echo "Running puzzle solver..." | tee -a "$LOG_FILE"
        cd "$SCRIPT_DIR"
        python3 puzzle_solver.py --workers 5 --rpm 28 2>>"$LOG_FILE" &
        echo "Solver started in background (PID: $!)" | tee -a "$LOG_FILE"
    fi
done

echo "" | tee -a "$LOG_FILE"
echo "=== Re-run check complete ===" | tee -a "$LOG_FILE"
