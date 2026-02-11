#!/bin/bash
# MrBeast $1M Puzzle Hunt - Daily Monitor
# Checks for new clues, community progress, and puzzle updates
# Run daily via cron: 0 8,12,18,22 * * * /path/to/monitor_puzzle.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$(dirname "$SCRIPT_DIR")"
LOG_DIR="$BASE_DIR/puzzle_monitor_logs"
mkdir -p "$LOG_DIR"
TIMESTAMP=$(date +%Y-%m-%d_%H%M)
LOG_FILE="$LOG_DIR/monitor_${TIMESTAMP}.log"

echo "=== MrBeast Puzzle Monitor - $(date) ===" | tee "$LOG_FILE"

# --- 1. Check MrBeast's X/Twitter for new puzzle posts ---
echo "" | tee -a "$LOG_FILE"
echo "--- Checking @MrBeast X posts ---" | tee -a "$LOG_FILE"
if command -v curl &>/dev/null; then
    # Use nitter or a public proxy to check recent posts
    curl -s "https://nitter.net/MrBeast/rss" 2>/dev/null | \
        grep -iE '(puzzle|clue|hint|vault|million|code|slack|salesforce)' | \
        head -10 >> "$LOG_FILE" 2>&1 || echo "  Could not fetch X posts (use browser)" | tee -a "$LOG_FILE"
fi

# --- 2. Check ARGNet for updates ---
echo "" | tee -a "$LOG_FILE"
echo "--- Checking ARGNet for puzzle updates ---" | tee -a "$LOG_FILE"
curl -s "https://www.argn.com/feed/" 2>/dev/null | \
    grep -i "mrbeast\|puzzle\|vault\|salesforce" | \
    head -5 >> "$LOG_FILE" 2>&1 || echo "  Could not fetch ARGNet" | tee -a "$LOG_FILE"

# --- 3. Check mrbeast.salesforce.com accessibility ---
echo "" | tee -a "$LOG_FILE"
echo "--- Checking mrbeast.salesforce.com ---" | tee -a "$LOG_FILE"
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "https://mrbeast.salesforce.com/" 2>/dev/null || echo "000")
echo "  HTTP Status: $HTTP_CODE" | tee -a "$LOG_FILE"

# --- 4. Check Reddit for puzzle discussion ---
echo "" | tee -a "$LOG_FILE"
echo "--- Checking Reddit r/MrBeast ---" | tee -a "$LOG_FILE"
curl -s "https://www.reddit.com/r/MrBeast/search.json?q=puzzle+OR+vault+OR+salesforce+OR+clue&sort=new&t=day&limit=5" \
    -H "User-Agent: PuzzleMonitor/1.0" 2>/dev/null | \
    python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    posts = data.get('data', {}).get('children', [])
    for p in posts[:5]:
        d = p['data']
        print(f\"  [{d.get('score',0)} pts] {d.get('title','?')[:80]}\")
except:
    print('  Could not parse Reddit data')
" 2>/dev/null >> "$LOG_FILE" || echo "  Could not fetch Reddit" | tee -a "$LOG_FILE"

# --- 5. Check for new MrBeast YouTube videos ---
echo "" | tee -a "$LOG_FILE"
echo "--- Checking for new MrBeast YouTube videos ---" | tee -a "$LOG_FILE"
if command -v yt-dlp &>/dev/null; then
    yt-dlp --flat-playlist --print "%(upload_date)s %(title)s" \
        "https://www.youtube.com/@MrBeast/videos" 2>/dev/null | \
        head -5 >> "$LOG_FILE" 2>&1 || echo "  Could not fetch YouTube" | tee -a "$LOG_FILE"
else
    echo "  yt-dlp not installed - install with: brew install yt-dlp" | tee -a "$LOG_FILE"
fi

# --- 6. Summary ---
echo "" | tee -a "$LOG_FILE"
echo "=== Monitor complete. Log saved to: $LOG_FILE ===" | tee -a "$LOG_FILE"
echo ""
echo "REMINDER: Check these manually too:"
echo "  - MrBeast Instagram: https://instagram.com/mrbeast"
echo "  - MrBeast X: https://x.com/MrBeast"
echo "  - Lone Shark Discord: Check https://lonesharkgames.com/the-puzzle-vault/"
echo "  - Reddit: https://reddit.com/r/MrBeast"
