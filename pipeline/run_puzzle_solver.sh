#!/bin/bash
# ═══════════════════════════════════════════════════════════
# MrBeast $1M Puzzle Solver — Quick Start
# ═══════════════════════════════════════════════════════════
#
# SETUP (one time):
#   pip install google-genai
#   export GEMINI_API_KEY="your-api-key-here"
#
# USAGE:
#   ./run_puzzle_solver.sh              # Run everything
#   ./run_puzzle_solver.sh test         # Test on 3 frames first
#   ./run_puzzle_solver.sh summary      # Regenerate summary only
#   ./run_puzzle_solver.sh <folder>     # Run one video only
#
# The script is RESUMABLE — rerun it and it picks up where
# it left off (skips already-analyzed frames).
# ═══════════════════════════════════════════════════════════

set -e
cd "$(dirname "$0")"

# Check for API key
if [ -z "$GEMINI_API_KEY" ]; then
    echo "ERROR: Set the GEMINI_API_KEY environment variable first."
    echo "  export GEMINI_API_KEY='your-api-key-here'"
    exit 1
fi

# Check dependencies
if ! python3 -c "from google import genai" 2>/dev/null; then
    echo "Installing google-genai..."
    pip install google-genai
fi

MODE="${1:-full}"

case "$MODE" in
    test)
        echo "🧪 TEST MODE: Analyzing 3 frames from each video..."
        python3 puzzle_solver.py --max-frames 3 --workers 1 --rpm 10
        ;;
    summary)
        echo "📊 Regenerating master summary from existing results..."
        python3 puzzle_solver.py --summary-only
        ;;
    first_to_find_1M_frames|slack_ad_frames|rewatch_to_win_1M_frames|superbowl_ad_1M_frames)
        echo "📹 Running single video: $MODE"
        python3 puzzle_solver.py --video "$MODE" --workers 5 --rpm 28
        ;;
    full)
        echo "🚀 FULL RUN: Analyzing all frames..."
        echo "   This will take a while. The script is resumable — Ctrl+C safely."
        echo ""
        python3 puzzle_solver.py --workers 5 --rpm 28
        ;;
    *)
        echo "Usage: $0 [test|summary|full|<folder_name>]"
        exit 1
        ;;
esac

echo ""
echo "✅ Done! Results are in: puzzle_analysis/"
echo "   📄 MASTER_SUMMARY.json — all findings aggregated"
echo "   📁 <video>/              — per-frame JSON results"
echo "   🔥 _HIGH_CONFIDENCE_CLUES.json — best leads per video"
