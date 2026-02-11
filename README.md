# MrBeast x Salesforce $1,000,000 Puzzle Hunt

**Status:** Unsolved | **Contest:** Feb 8 -- Apr 2, 2026 | **Prize:** $1,000,000

A community-driven, machine-assisted analysis of MrBeast's million-dollar puzzle hunt, designed by [Lone Shark Games](https://lonesharkgames.com/the-puzzle-vault/).

## What is This?

MrBeast and Salesforce launched a $1M puzzle hunt during Super Bowl LX. The puzzle is a multi-stage ARG ("like rooms in the vault") with daily clue drops, embedded ciphers across 4 YouTube videos, 9 variety puzzles, a crossword that unlocks Stage 2, and a final Slack code that wins the prize.

We built an automated pipeline using **Gemini 3 Flash Preview** (agentic vision) and **Claude Opus 4.6** to analyze every frame of all 4 videos -- **6,918 frames total** -- extracting text, symbols, ciphers, and steganographic data that humans would miss at normal viewing speed.

**60 million people** visited the contest site on day one. As of Feb 11, 2026, nobody has solved it.

## Key Findings

- **At least 3 stages** confirmed ("like rooms in the vault") -- Hint #2
- **17 distinct ciphers decoded** (phone keypad, A1Z26, room layout, Lost numbers, steganography, etc.)
- **8 Salesforce lab screens map 1:1 to bank clues** -- the key to Hub 3 (Hint #2)
- **6 banks identified** in the Super Bowl ad with puzzle-relevant props
- **9 variety puzzles located** across 9 image hosting platforms (2 grids fully solved)
- **30+ "weird things"** catalogued from the ad street scenes (each yields one answer via standard codes)
- **Stage 2 crossword** identified -- clues fill in as Stage 1 is solved

## Read the Full Analysis

**[PUZZLE_ANALYSIS.md](PUZZLE_ANALYSIS.md)** -- The complete clue inventory, cipher decodings, cross-video patterns, and solving progress.

## Puzzle Images

All 9 variety puzzle images + the Stage 2 crossword are in [`puzzle_analysis/superbowl_ad_1M_frames/`](puzzle_analysis/superbowl_ad_1M_frames/).

The variety puzzles were posted by "BeastForce67" as pinned comments across Pinterest, Reddit, Imgur, ImageShack, Photobucket, Medium, Pixelfed, ImgPile, and 500px.

## How to Help

Lone Shark Games said it explicitly: *"We never said you had to do this alone."*

The biggest open problems right now:

1. **Solve the remaining variety puzzles** (1, 4, 5, 6, 7, 9) -- see puzzle images in this repo
2. **Map the 8 Salesforce lab screens to their corresponding bank clues** (1:1 mapping, each used once)
3. **Crack the extraction methods** that convert solved grids into answer words
4. **Decode "weird things"** from the Super Bowl ad using standard cipher lookups
5. **Monitor the Stage 2 crossword** for new clues as Stage 1 progress is made

Open an issue or PR with any findings.

## Links

- **Register:** [mrbeast.salesforce.com](https://mrbeast.salesforce.com/)
- **Behind the Scenes:** [mrbeast.salesforce.com/behindthescenes](https://mrbeast.salesforce.com/behindthescenes)
- **Hint #1:** [Lone Shark Games (Feb 9)](https://youtu.be/hGuA0a15VWQ)
- **Hint #2:** [mrbeast.salesforce.com (Feb 10)](https://mrbeast.salesforce.com/)
- **Puzzle Designer:** [Lone Shark Games - The Puzzle Vault](https://lonesharkgames.com/the-puzzle-vault/)
- **Community:** [r/MrBeast](https://reddit.com/r/MrBeast) | [ARGNet](https://www.argn.com/2026/02/start_slacking_off_with_mrbeasts_million_dollar_puzzle_hunt/)

---

*Analysis pipeline: [Gemini 3 Flash Preview](https://ai.google.dev/) (agentic vision) + [Claude Opus 4.6](https://claude.ai/). 4,758 of 6,918 frames analyzed. Last updated: 2026-02-11.*
