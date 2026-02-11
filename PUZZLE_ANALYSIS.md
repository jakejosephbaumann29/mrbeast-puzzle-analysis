# MrBeast x Salesforce $1,000,000 Puzzle Hunt

> **Status:** Unsolved | **Contest:** Feb 8 -- Apr 2, 2026 | **Designer:** [Lone Shark Games](https://lonesharkgames.com/the-puzzle-vault/)
>
> **Register:** [mrbeast.salesforce.com](https://mrbeast.salesforce.com/) | **Submit:** Slack the code to @MrBeast

---

## Table of Contents

1. [Overview](#overview)
2. [Methodology](#methodology)
3. [Puzzle Architecture](#puzzle-architecture)
4. [9 Variety Puzzles (Step 1)](#9-variety-puzzles)
5. [Video-by-Video Clue Inventory](#video-by-video-clue-inventory)
6. [Decoded Ciphers](#decoded-ciphers)
7. [Cross-Video Patterns](#cross-video-patterns)
8. [Super Bowl Ad "Weird Things"](#super-bowl-ad-weird-things)
9. [Behind the Scenes Gallery Clues](#behind-the-scenes-gallery-clues)
10. [Current Best Guesses](#current-best-guesses)
11. [Next Steps](#next-steps)
12. [Contributing](#contributing)
13. [Sources](#sources)

---

## Overview

On Feb 9, 2026, MrBeast confirmed: *"No one has solved it... For the record it's very hard and lots of steps."* Lone Shark Games added: *"Not all of the puzzle has been revealed."*

60 million people visited the contest site on day one. Nobody is close.

This repository is a comprehensive, machine-assisted analysis of every clue we've found so far. The goal is to enable community collaboration -- the puzzle designers explicitly encouraged it: *"We never said you had to do this alone."*

---

## Methodology

### What We Did

We built an automated pipeline that extracts and analyzes every frame from all four official puzzle videos -- 6,918 frames total. Each frame is examined for text, symbols, spatial patterns, ciphers, and steganographic data. We then cross-referenced all findings against each other and against the official Hint #1 to build a unified clue inventory.

### How We Did It

| Component | Detail |
|-----------|--------|
| **Frame extraction** | ffmpeg at 1fps from each of 4 YouTube videos |
| **Vision analysis** | [Gemini 3 Flash Preview](https://ai.google.dev/) with agentic vision (code execution + thinking) |
| **Analysis model** | Claude Opus 4.6 for cross-referencing, cipher decoding, and pattern recognition |
| **Pipeline** | Custom Python script processing frames in parallel with rate limiting |
| **Output** | One JSON file per frame containing: clues found, confidence scores, code execution logs, cross-frame notes, and puzzle theories |

Each frame analysis includes:
- Region-of-interest cropping and enhancement (contrast, sharpening, edge detection)
- QR code / barcode detection
- OCR on all visible text (including reversed, rotated, and partially obscured text)
- Color channel separation to find steganographic data
- Cross-referencing against known cipher systems (A1Z26, Morse, Braille, phone keypad, semaphore)

### Why This Approach

Lone Shark Games confirmed in Hint #1 that *"almost everything Jimmy passes by is a clue"* and to *"look up, down, forward, backward, and behind the scenes."* A human watching the video at normal speed would miss the vast majority of embedded clues. Frame-by-frame machine analysis ensures nothing is overlooked.

### Pipeline Status

| Video | Frames | Status |
|-------|--------|--------|
| 1. First To Find $1,000,000 | 769 / 769 | Complete |
| 2. One Idea. 27 Days. Built with Slack | 1,441 / 1,441 | Complete |
| 3. Rewatch This Video to Win $1M | 1,235 / 1,234 | Complete |
| 4. Watch My Super Bowl Ad to Win $1M | ~1,318 / 3,476 | 38% (in progress) |

---

## Puzzle Architecture

### The Multi-Stage Structure (Confirmed by Hints #1 and #2)

The puzzle is not a single riddle. It's a staged vault with **at least 3 stages** ("like rooms in the vault") and a dependency chain within each stage.

**Stage 1** has 3 hubs:

```
Hub 1: VIDEO PLAYLIST (9 Variety Puzzles)
  Each puzzle yields one word -> 9 words form an instruction
  Word lengths: 5, 9, 5, 7, 8, 4, 9, 6, 5
  "That will help define the nature of the search"

Hub 2: THE COMMERCIAL (Super Bowl Ad -- Street Scenes)
  "Almost everything Jimmy passes by is a clue"
  Each "weird thing" yields one answer via standard online codes
  Look up, down, forward, backward, and behind the scenes

Hub 3: THE BANK (Super Bowl Ad -- Bank Scenes)
  Bank puzzles REQUIRE content from the other hubs to solve
  KEY: Each Salesforce computer lab screen (V1) maps 1:1 to one bank clue
  Each screen is used only once
```

**Stage 2**: Unlocked by the crossword puzzle (see [Stage 2 Crossword](#stage-2-crossword)). Clues fill in as Stage 1 progress is made.

**Stage 3+**: Unknown. *"There are at least two more stages, and we can't say much about them yet."*

### How the Solution Path Works

```
STAGE 1:
  Step 1: Solve 9 variety puzzles -> 9-word instruction phrase
                      |
  Step 2: Use instruction to understand WHAT to search for
                      |
  Step 3: Decode each "weird thing" in the Super Bowl ad street scenes
                      |
  Step 4: Match Salesforce lab screens (V1 frame 208) to bank clues (1:1)
                      |
  Step 5: Apply street-scene + lab-screen answers to solve bank puzzles
                      |
STAGE 2:
  Step 6: Crossword puzzle unlocks (clues fill in as you progress)
                      |
STAGE 3+:
  Step 7+: Unknown ("more on that another day")
                      |
  FINAL: Derive the Slack code -> Message @MrBeast -> Win $1M
```

### Salesforce Lab Screen -> Bank Clue Mapping (NEW from Hint #2)

From Hint #2: *"We tied each screen in the Salesforce computer lab to one clue in the bank video. Each is used only once."*

The 8 screens from Video 1 (frame 208):

| Screen | Icon | Mapped Bank Clue |
|--------|------|-----------------|
| 1 | Spider/Tarantula | ? |
| 2 | Bird/Canary | ? |
| 3 | Sine Wave | ? |
| 4 | Chandler + 'D' | ? |
| 5 | Ear | ? |
| 6 | Head/Brain | ? |
| 7 | Witch/Dancer | ? |
| 8 | '1' / Elephant | ? |

**Which screen goes with which bank clue is up to us to figure out.**

### Official Hint #1 (Lone Shark Games, Feb 9, 2026)

> **Source:** https://youtu.be/hGuA0a15VWQ
>
> *"Here's HINT #1: Some of these puzzles use codes you can find online. With the Super Bowl ad, almost everything Jimmy passes by is a clue. Look up, down, forward, backward, and behind the scenes. Figure out how to get an answer from each weird thing. In the bank, the same is true, but you will need specific content from the Super Bowl ad to solve anything there. Last, but not least, if you found the video playlist's pinned comments, each puzzle ends in a word that makes part of a 9-word clue, in order. The word lengths are 5, 9, 5, 7, 8, 4, 9, 6, and 5. That will help define the nature of the search. If you can get that 9-word clue, you'll take the first step on your journey. There is a direct way through this ultra-hard puzzle hunt. You can find it. Then you can win a million dollars!"*

**Other key quotes:**
- *"We never said you had to do this alone"*
- *"Only one person can claim the prize, but it's probably not possible for one person to find and solve everything"*
- *"Start a wiki, where you list potential puzzles and possible paths and solutions"*
- *"If you can't solve it today, don't panic. Tomorrow we'll drop another clue."*

| What Hint #1 Tells Us | Implication |
|------------------------|------------|
| "codes you can find online" | Standard ciphers: A1Z26, Morse, Braille, semaphore, phone keypad |
| "everything Jimmy passes by" | Frame-by-frame analysis is the correct approach |
| "up, down, forward, backward" | Check ceilings, floors, reversed text, reflections |
| "behind the scenes" | Video 2 (the Slack making-of) is part of the puzzle |
| "answer from each weird thing" | Each prop/sign yields exactly one answer |
| "bank needs Super Bowl ad content" | Street answers are inputs to bank puzzles (dependency) |
| "9-word clue, in order" | Variety puzzles produce a master instruction |
| "define the nature of the search" | The phrase tells you what kind of search to do |
| "first step on your journey" | The 9-word clue is Step 1, not the final answer |
| "direct way through" | There is one clear path, not random guessing |

### Official Hint #2 (Lone Shark Games, Feb 10, 2026)

> **Source:** [mrbeast.salesforce.com](https://mrbeast.salesforce.com/)
>
> *"You guys are making tremendous progress!"*
>
> *"Many of you have already figured out - this hunt has 3 main hubs in this first stage (yes there's stages - like rooms in the vault, but more on that another day)."*
>
> *"Hub 1 is the video playlist. Hub 2 is the commercial that aired on Sunday. Hub 3 is the bank."*
>
> *"There are at least two more stages, and we can't say much about them yet."*
>
> **On the bank:** *"We tied each screen in the Salesforce computer lab to one clue in the bank video. Which screen goes with which clue ... that's up to you to figure out. Each is used only once, so once you tie a screen to a bank video clue, you won't use it for any other clue."*
>
> **On Stage 2:** *"In one of the Behind the Scenes videos, you might have seen puzzlemaster Mike drop a crossword puzzle. That crossword might also be a key to STAGE 2. It doesn't have any clues... yet. The more progress you make, the more the clues will fill in. You'll need those for the endgame."*

| What Hint #2 Tells Us | Implication |
|------------------------|------------|
| "3 main hubs in this first stage" | Variety puzzles, commercial, and bank are all Stage 1 |
| "yes there's stages" | Multi-stage structure confirmed (at least 3 stages) |
| "lab screen -> bank clue, 1:1" | The 8 Salesforce mascot screens from V1 are extraction keys for bank puzzles |
| "each used only once" | One-to-one matching, no reuse -- process of elimination helps |
| "crossword ... key to STAGE 2" | The BTS crossword is the gateway to Stage 2 |
| "doesn't have any clues... yet" | Crossword clues unlock dynamically as Stage 1 is solved |
| "you'll need those for the endgame" | The crossword is required for the final solution |

### Stage 2 Crossword

Puzzlemaster Mike's crossword was shown in the Behind the Scenes video and is available at [mrbeast.salesforce.com/behindthescenes](https://mrbeast.salesforce.com/behindthescenes). The crossword image is included in this repo as `puzzle_analysis/superbowl_ad_1M_frames/crossword_stage2.webp`.

**Title:** "I MADE A PUZZLE FOR JIMMY"

**Key facts:**
- Standard crossword grid (~15x15) with Lone Shark Games branding
- The clue list is **intentionally incomplete** -- clues fill in as the community solves Stage 1
- Per Hint #2: *"You'll need those for the endgame"*
- The crossword was a "gift to Jimmy" from puzzlemaster Mike

**Strategy:** This crossword cannot be fully solved until Stage 1 progress unlocks its clues. Focus on Stage 1 first.

---

## 9 Variety Puzzles

Per Hint #1, these are **Step 1 of the entire puzzle**. Each puzzle produces one word. The 9 words form a clue phrase that *"defines the nature of the search."*

**Required word lengths: 5, 9, 5, 7, 8, 4, 9, 6, 5**

The puzzles were posted as pinned comments on a playlist of 9 MrBeast videos, by the account "BeastForce67" across 9 different image hosting platforms. All 9 puzzle images are included in this repository under `puzzle_analysis/superbowl_ad_1M_frames/`.

| # | Platform | MrBeast Video | Puzzle Type | Letters | Status | Notes |
|---|----------|---------------|-------------|---------|--------|-------|
| 1 | Pinterest | 100 Wells in Africa | Word search + water drop blanks | 5 | Partial (6/13 words) | 7 clue words remain unfound |
| 2 | Reddit | 600 Strangers | Letter Sudoku (CHANGLIFE) | 9 | **Grid solved** | Extraction method unknown |
| 3 | Imgur | Dirtiest Beach #TeamSeas | TV show genre + debris removal | 5 | Partial (13/19 shows) | 6 entries unmatched |
| 4 | ImageShack | $1-$500K Experiences | Stencil-font locations | 7 | Structure decoded | |
| 5 | Photobucket | Pokemon Go Stereotypes | Pokemon cage crossword | 8 | Structure understood | |
| 6 | Medium | Wilderness Survival | Tents and Trees + number grid | 4 | Structure understood | |
| 7 | Pixelfed | 100 Dogs | Venn diagram dog traits | 9 | Structure understood | |
| 8 | ImgPile | 100 Hours in Pyramids | Pyramid crossword | 6 | **All 43 clues solved** | Grid placement needed |
| 9 | 500px | Circle I'll Pay For | Geodesic spheres + letters | 5 | Multiple theories | |

### Puzzle 2: Letter Sudoku (SOLVED GRID)

The grid uses the letters C-H-A-N-G-L-I-F-E instead of digits 1-9:

```
A L F | C H N | E G I
C G H | F I E | N L A
E I N | A G L | H F C
------+-------+------
G N L | H E I | C A F
I H C | L F A | G E N
F A E | G N C | I H L
------+-------+------
H F A | N C G | L I E
N E G | I L F | A C H
L C I | E A H | F N G
```

Letter-to-number mapping: C=1, H=2, A=3, N=4, G=5, L=6, I=7, F=8, E=9

**Blocker:** The grid is complete, but the extraction method (which cells to read to get the 9-letter answer word) is unknown. Per ARGNet, *"information on which letters to select might emerge through other parts of the campaign."* Bank scene keys are likely needed.

### Puzzle 3: TV Show Debris Removal

Mechanic: identify the TV show from each clue, then remove "debris" letters from the title. The remaining letters form anagram material or a direct answer.

Debris pool: `AABBCCCDDFFFGGGGIIIKKKKLLLMNNPRRSSTTTWWY`

**13 confirmed matches:**

| TV Show | Debris Removed | Result | Grid Position |
|---------|---------------|--------|---------------|
| KNIGHT RIDER | debris letters | DITHERING | (10,7) |
| GET SMART | debris letters | MATTER | (5,2) |
| GREEN ACRES | debris letters | SCREENER | (4,10) |
| FATHER TED | debris letters | HEARTED | (1,6) |
| BEAST GAMES | debris letters | TEAMSEAS | (8,1) |
| KNOTS LANDING | debris letters | STANDING ON | (3,6) |
| IRON FIST | debris letters | INTROS | (3,2) |
| KAREN SISCO | debris letters | SCENARIOS | (10,3) |
| BURN NOTICE | debris letters | NEUROTIC | (8,10) |
| SISTER WIVES | debris letters | RESISTIVE | (7,8) |
| NIGHT COURT | debris letters | OUTRIGHT | (10,4) |
| KIM POSSIBLE | debris letters | MOBILISES | (9,4) |
| TOP GEAR | debris letters | OPERA | (1,6) |

6 entries remain unmatched. The (X,Y) grid extraction method is still unsolved.

### Puzzle 8: Pyramid Crossword (ALL CLUES SOLVED)

All 43 clue answers identified. Left-side answers (21): A, ADORN, CABRIOLET, CALIBRE, LOW-CARB, TAKE IN, NAVIGATOR, DURATION, E, EAR, ECLAIR, EON, ER, I, IN UTERO, INUNDATE, ION, LE CAR, NO, NOTE, O. Right-side answers (22): OI, OPTION, ORBICULAR, ORIENT, OUT FOR A SPIN, OUTLINERS, PINTO, PORTION, PROTON, RA, RACE, RAD, RAT POISON, RESOLUTION, REVOLUTIONS, ROTUNDA, RUTS, STAINLESS, TONER, TONI, TRADES UNION, TURN ON A DIME.

**Blocker:** Grid placement and extraction mechanism still needed.

### Puzzle 1: Word Search (Partial)

9x9 grid with 15 water-drop blanks. 13 hidden words reveal the blank letters.

**Found:** CON, IRATE, ROBIN HOOD, IOWA, DHOW, MORAY

**Unsolved clues:** "A cold noise?", "A natural disaster", "MrBeast went to one in Greenville NC", "'Rats!' (2 wds)", "A child's toy (2 wds Hyph.)", "item in MrBeast store", "US landmark (2 wds)", "What you say when you finish this!"

### 9-Word Clue Assembly (Speculative)

```
Word 1:  _ _ _ _ _           (5)  -- Puzzle 1 (word search)
Word 2:  _ _ _ _ _ _ _ _ _   (9)  -- Puzzle 2 (sudoku -- grid solved)
Word 3:  _ _ _ _ _           (5)  -- Puzzle 3 (TV shows -- 13/19 matched)
Word 4:  _ _ _ _ _ _ _       (7)  -- Puzzle 4 (stencil locations)
Word 5:  _ _ _ _ _ _ _ _     (8)  -- Puzzle 5 (pokemon cages)
Word 6:  _ _ _ _             (4)  -- Puzzle 6 (tents & trees)
Word 7:  _ _ _ _ _ _ _ _ _   (9)  -- Puzzle 7 (100 dogs venn)
Word 8:  _ _ _ _ _ _         (6)  -- Puzzle 8 (pyramid -- all clues solved)
Word 9:  _ _ _ _ _           (5)  -- Puzzle 9 (geodesic spheres)
```

**Key insight:** This phrase is an INSTRUCTION. It tells you what kind of search to perform. It is Step 1, not the final answer. Most extractions likely require keys from the Super Bowl ad bank scenes (Video 4, only 38% processed).

---

## Video-by-Video Clue Inventory

Every clue below was extracted by the Gemini 3 Flash pipeline. Confidence scores (0.0--1.0) reflect the model's certainty. Bold rows indicate high-confidence, high-importance findings.

### Video 1: "First To Find $1,000,000, Keeps It!" (769 frames)

| Frame | Conf | Type | Raw Value | Decoded | Notes |
|-------|------|------|-----------|---------|-------|
| 005 | 0.95 | cipher | Red-bordered bills | A1Z26: 20=T, 5=E, 1=A | Custom MrBeast currency |
| 111 | 0.90 | text | Fine print | Starts 2/8/26, Ends 4/2/26 | Contest dates + registration URL |
| 189 | 0.95 | text | CANARY + LOCKED | Canary status indicator | Salesforce lab setting |
| 189 | 0.95 | text | 3% | On MrBeast's belt | Percentage clue |
| 192 | 0.95 | text | CANARY SINGING | Status changed | Ear with 4 dashes (_ _ _ _) |
| 192 | 0.95 | spatial | 6 head models | Count = 6 | Three Wise Monkeys motif |
| **208** | **1.0** | **symbol** | **Screen icons** | **Spider, Bird, Sine Wave, Chandler+'D', Ear, Head, Witch, '1'** | **Salesforce mascots** |
| **232** | **0.95** | **cipher** | **Room layout** | **H-I-D-E** | **Key instruction word** |
| 275 | 0.90 | math | Spider=8, Swiss Flag | 10^5=100,000, weight=22.4L | Scientific constants |
| 279 | 0.95 | math | n^3=n | Solutions: -1, 0, 1 | ear+mute = "DEAF" |
| **340** | **0.90** | **emoji** | **Slackbot emojis** | **Recurring 5-emoji code** | **Varies between frames** |
| **376** | **0.85** | **text** | **FIND** | **Rivets on vault door** | **Instruction word** |
| **382** | **0.95** | **text** | **BEAST 6000** | **Original YouTube handle** | **Spelled in rivets** |
| **392** | **1.0** | **cipher** | **3634826-1** | **ENDGAME-1 (phone keypad)** | **Most prominent code in all videos** |
| 436 | 1.0 | spatial | 3634826-1 breakdown | 36 dots, 34 stripes, 8 lights, 26 total | Room elements validate the code |
| 488 | 0.85 | text | 1026-1 | On equipment | Variant of main code |
| **496** | **0.95** | **text** | **3X771** | **Belt code (red-highlighted 7)** | **Unique code** |
| 496 | 0.95 | text | 4826-1 | On tank | Partial main code |
| 575 | 0.85 | text | G-14 | "Classified" reference | Military designation |
| **609** | **0.95** | **cipher** | **Vault ring numbers** | **Complex sequence on rings** | **Combination lock** |
| **628** | **0.95** | **cipher** | **Vault door ring** | **46-element number sequence** | **Possible run-length encoding** |
| **634** | **0.95** | **cipher** | **4-8-15-16-23-42** | **"Lost" numbers (sum=108)** | **Vault combination** |
| 634 | 0.80 | code | MRBEAST belt colors | M(Grn)R(Yel)B(Blu)E(Red)A(Grn)S(Yel)T(Blu) | 4-color repeating cycle |
| **654** | **0.95** | **visual** | **Red slashes 1-2-3** | **"Release" text, 12 vault spokes** | **Sequence instruction** |
| **710** | **1.0** | **code** | **QR CODE** | **`https://sforce.co/4bAAGMH?r=qr`** | **Decoded Salesforce URL** |
| 716 | 1.0 | visual | QR code (diff angle) | Same URL | Built from shipping containers in desert |

### Video 2: "One Idea. 27 Days. Built with Slack." (1,441 frames)

Behind-the-scenes documentary about making the Super Bowl ad. Dense with encoded clues.

| Frame | Conf | Type | Raw Value | Decoded | Notes |
|-------|------|------|-----------|---------|-------|
| 001 | 0.85 | spatial | MrBeast logo | 27 geometric features | Matches "27 Days" title |
| 057 | 0.80 | symbol | Salesforce logo (modified) | 10 bumps, distributed 4-2-3-1 | Modified cloud shape |
| **200** | **0.95** | **steg** | **Tweet text LSB** | **"I-S-L-A-N-D"** | **Steganographic keyword** |
| **213** | **1.0** | **math** | **Countdown calculation** | **41-day countdown (Dec 29 to Feb 8)** | **14+27=41** |
| **252** | **1.0** | **cipher** | **"Rosetta Stone" frame** | **A1Z26 confirmed as key cipher** | **Tweet digits sum to 27; "MrBeast"=78 in A1Z26** |
| **294** | **1.0** | **code** | **Tweet metrics** | **Unix timestamp 1441015326 = Aug 31, 2015** | **Missing word: "incredible"** |
| **507** | **0.95** | **symbol** | **Feastables train** | **Locomotive #600, tanker #41** | **Jimmy(5)+message(16)+icons(6)=27** |
| **604** | **0.95** | **text** | **Slack sidebar** | **#secret-clue** | **Hidden Slack channel name** |
| 604 | 0.70 | text | Water tank label | "MALCOLM" | Keyword / person reference |
| 604 | 0.85 | text | Slack message | Jimmy: "check the lights for $1M challenge" | Production reference |
| **649** | **0.95** | **text** | **Phone screen numbers** | **Hidden "7" above time, hidden "1" below logo** | **Encodes 1-2-7 or 7-2-1** |
| 649 | 0.90 | text | Slack message | "Jimmy: Pyramids??" | Desert/Egypt reference |
| **743** | **1.0** | **math** | **Number 14 encoded everywhere** | **14 members, 9+4+1=14, #project-big-game=14 chars** | **Core number** |
| **751** | **0.95** | **cipher** | **Reaction counts as indices** | **15,20,22 -> T-O-W** | **Tug of War reference** |
| **753** | **0.95** | **steg** | **Background hex #152022** | **Encodes 15, 20, 22** | **B=2, G=7 -> "27"** |
| 753 | 0.80 | visual | Squid Game reference | 456 players in pink | MrBeast's biggest video |

**Number 27 encodings found in Video 2:** title ("27 Days"), logo (27 geometric features), A1Z26 ("MrBeast"=78, digits sum toward 27), tweet metric digit sums, Jimmy(5)+message(16)+icons(6)=27, background hex B=2/G=7.

### Video 3: "Rewatch This Video to Win $1,000,000" (1,234 frames)

**Verdict: Confirmed red herring / troll.** Still contains a few potentially real breadcrumbs.

MrBeast holds a white sign that changes words throughout the video:

| # | Word | Frame Range | Notable Detail |
|---|------|-------------|----------------|
| 1 | Help | f00009-f00200 | -- |
| 2 | Me | f00112-f00200 | -- |
| 3 | Patience | f00221-f00227 | Basketball players (jersey #23) |
| 4 | You | f00307-f00406 | -- |
| 5 | Win | f00409-f00518 | -- |
| 6 | $1,000,000 | f00519-f00597 | -- |
| 7 | @ the | f00598-f00715 | "@the1Mil" handle visible |
| 8 | Big | f00715-f00812 | Steganographic: "HIDDEN WORD IS 7/10" |
| 9 | Game | f00813-f01090 | -- |
| 10 | [Acrostic] | f01091-f01234 | First letters spell: "THIS MEANS NOTHING I JUST WANTED TO WASTE YOUR TIME LOL" |

**Reconstructed message:** "HELP ME [PATIENCE] YOU WIN $1,000,000 @ THE BIG GAME"

**Possible real breadcrumbs despite troll status:** "@the1Mil" social media handle (f00598), "HECK" in red letters, "HERE" text (f00890).

### Video 4: "Watch My Super Bowl Ad To Win $1,000,000!" (3,476 frames -- 38% processed)

The actual Super Bowl LX ad. This is the densest video for puzzle content. Analysis covers frames 1--1829 so far.

| Frame | Conf | Type | Raw Value | Decoded | Notes |
|-------|------|------|-----------|---------|-------|
| **088-110** | **0.95** | **phone** | **657-283-9800** | **Primary phone number** | **No reply when texted** |
| 088-110 | 0.95 | phone | 650-283-9795 | Second number | Salesforce HQ area code |
| 088-110 | 0.90 | phone | 480-234-354? | Partial | Arizona area code |
| 088-110 | 0.90 | phone | 704-232-7823 | **704-BEAST-23** | Charlotte, NC (MrBeast hometown) |
| **099** | **1.0** | **text** | **MRS. MAYBELLE** | **"Ma Bell" = telephone company** | **Character name is a cipher** |
| 099 | 1.0 | math | MAY=39, BELLE=36 | A1Z26 sum = 75 | Name encodes numbers |
| 099 | 1.0 | calendar | Double dates circled | 1/1, 2/2, 3/3...12/12 | Calendar pattern |
| 099 | 1.0 | calendar | Months with 31 days | **July missing** from list | Deliberate omission |
| **108** | **1.0** | **text** | **MRS. MAYBEUR** | **"Maybe You Are" (the winner)** | **Phonetic decode** |
| 108 | 1.0 | text | MRS. MAYBERRY | Mayberry, NC (Andy Griffith) | NC reference |
| 208 | 0.95 | code | Binary barcode on parking meter | ASCII 'i'/'I', decimal 1226, hex 0xAA | Post-mounted pattern |
| **250-254** | **0.95** | **text** | **VIOLATION: OVERTIME** | **SB LVIII went to OT** | **02/11/24, 6:30 PM, Las Vegas** |
| 331-385 | 0.95 | spatial | Vehicle plates | JP1117, BPE527, BP6327 | Patterns: 17, 27, 77 |
| 491 | 0.95 | text | "17 STOP NOW HERE" | Number 17 prominent | Instruction? |
| 516 | 0.95 | text | THE ROW LOFTS | 777 S Alameda St, LA | Triple 7s address |
| 700-718 | 0.95 | setting | PL-01 tank | Polish "stealth" concept tank | Hidden/stealth theme |
| **1075** | **0.95** | **sequence** | **7-5-3-1** | **Odd numbers descending** | **Sum = 16 (Lost number)** |
| **1124-1175** | **1.0** | **text** | **RED HERRING BANK** | **Meta-clue: distraction** | **Being towed away in scene** |
| **1124-1175** | **0.95** | **text** | **BARCLAY HOTEL** | **103 W 4th St, LA 90013** | **Primary real-world anchor (20+ frames)** |
| 1124-1175 | 0.85 | text | PLAY | Highlighted from BARCLAY | Call to action |
| **1146** | **0.85** | **cipher** | **T7 street marking** | **7th letter of BARCLAY = Y** | **Positional extraction pattern** |
| 1146 | 0.90 | text | BEAST on armored truck | MrBeast branding | Custom prop |
| 1154 | 0.90 | text | X-01 on tank turret | Tank designation | Sequence start |
| 1158 | 0.90 | code | 6601 on tank turret | Faint, revealed by enhancement | Unknown significance |
| 1230-1237 | 0.85 | text | NO PARKING YOUR TANK AT THE BANK | Custom rhyming sign | Deliberate prop |
| **1230-1237** | **0.75** | **text** | **TALK LIKE A PIRATE DAY** | **September 19 (09/19)** | **Billboard in background** |
| 1230-1237 | 0.70 | text | 30 MINUTE PARKING LIMIT | Number 30 | "30 Days" challenge ref? |
| 1230-1237 | 0.80 | text | 4th St / Clay | Street intersection | Confirms location |
| 1230-1237 | 0.50 | spatial | Morse on tank: -- -- | M M | Or binary "11" |
| **1275-1285** | **0.9** | **text** | **MRS. MAYBELLE** (nameplate) | **Consistent across 10+ frames** | **Bank teller scene** |
| **1276** | **0.9** | **symbol** | **Georgia state outline + State Farm** | **Atlanta, GA** | **Cup + Mercedes-Benz Stadium picture** |
| **1280** | **0.9** | **text** | **PEACH STATE BANK** | **Georgia Peach State** | **Coffee cup logo** |
| 1280 | 0.9 | symbol | Shopify logo (green bag) | E-commerce brand | On teller counter |
| 1281 | 0.8 | symbol | Drinking Bird toy | Classic desk toy | On Mrs. Maybelle's desk |
| 1284 | 0.8 | text | GEORGIA LOTTERY | Prize reference | Wall signage |
| **1285** | **0.95** | **cipher** | **Month-to-Number Chart** | **Apr=1, Jun=2, Jul=3, Aug=4, Sep=5, Dec=6** | **Key puzzle element on wall** |
| 1408-1522 | 0.8 | setting | MrBeast + Mrs. Maybelle | Dialogue scene | Hidden background observer in every frame |
| **1515** | **0.85** | **code** | **Chandelier binary: 111000** | **56 decimal / Braille 'l'** | **Top 3 bright, bottom 3 dim** |
| 1504-1520 | 0.7 | spatial | Chandelier bulb counts vary | 6, 7, 8, 10 per frame | On/off patterns change |
| **1524** | **0.85** | **text** | **401 (NOT reversed)** | **All other text IS reversed** | **MERCHANTS BANK -- deliberate clue** |
| 1525 | 0.85 | text | FIRST NATIONAL BANK / 101 | Archway text + door number | Bank #3 |
| 1530 | 0.8 | text | ECNARTNE = ENTRANCE reversed | Reversed door text | BANK OF BEAST |
| 1555 | 0.7 | text | GRANTS 101 | Reversed on glass door | GRANTS BANK |
| 1682 | 0.7 | symbol | Pink Flamingo | Deliberate Easter egg | Merchants Bank counter |

#### Banks Identified in the Super Bowl Ad

| # | Bank Name | Frames | Key Props | Door Number |
|---|-----------|--------|-----------|-------------|
| 1 | Peach State Bank | 1275-1285 | Georgia cup, Shopify bag, Drinking Bird, month chart, Georgia Lottery | -- |
| 2 | Red Herring Bank | 1124-1175 | Being towed away, Barclay Hotel backdrop | -- |
| 3 | First National Bank | 1525 | Red Cup, YouTube tablet, 4 guards | 101 |
| 4 | Grants Bank | 1555 | Feastables, YouTube tablet | 101 |
| 5 | Merchants Bank | 1524, 1682 | Pink Flamingo, MrBeast cup, glass door | **401** (not reversed) |
| 6 | Bank of Beast | 1530 | ECNARTNE (reversed ENTRANCE) | 101 |

**Pattern:** 101 appears on every bank door except Merchants Bank, which shows **401** -- deliberately NOT reversed when all surrounding text IS reversed.

#### Month-to-Number Cipher (Frame 1285)

```
On wall chart labeled "2024":
  April     = 1
  June      = 2
  July      = 3
  August    = 4
  September = 5
  December  = 6

Missing months: Jan, Feb, Mar, MAY, Oct, Nov
Month numbers used: 4, 6, 7, 8, 9, 12
Notable: "MAYBELLE" contains MAY -- the most prominent missing month
First letters of assigned months: A, J, J, A, S, D
Sum: 4+6+7+8+9+12 = 46
```

#### Phone Numbers (All Texted -- No Replies)

| Number | Decode | Area |
|--------|--------|------|
| 657-283-9800 | Most prominent | Orange County, CA |
| 650-283-9795 | -- | Salesforce HQ (San Mateo, CA) |
| 480-234-354? | Partial | Tempe/Phoenix, AZ |
| 704-232-7823 | 704-BEAST-23 | Charlotte, NC (MrBeast hometown) |

**~2,163 frames remain unprocessed.** Expect: more bank interiors, vault scenes, Keith Haring mural, possible QR codes, end card.

---

## Decoded Ciphers

### 1. Phone Keypad: 3634826 = ENDGAME

```
3=E, 6=N, 3=D, 4=G, 8=A, 2=A, 6=M -> E-N-D-G-A-M-E
The "-1" suffix: "Endgame Part 1" or sequence indicator
```

Found on the tank barrel in 15+ frames (Video 1). The most repeated code in the entire video set.

### 2. Room Layout: HIDE

```
Above door: 8 -> H | Red-coded: I -> I | Green-coded: D -> D | Monitor: 5 -> E
Result: H-I-D-E
```

### 3. The Lost Numbers: 4-8-15-16-23-42

```
Vault door ring: 4-8-15-16-23-42
From TV show LOST. Sum = 108 (The Swan station timer).
Likely vault combination or extraction key.
```

### 4. A1Z26 (Confirmed as Core Cipher)

```
A=1, B=2, C=3 ... Z=26
"MrBeast" = M(13)+R(18)+B(2)+E(5)+A(1)+S(19)+T(20) = 78
Confirmed via Video 2 "Rosetta Stone" frame (252 = Greenville NC area code).
```

### 5. Reaction Count Indexing: TOW

```
Slack message: "Hey team! Here is the shot we discussed in the call!"
Reaction counts: 15, 20, 22
Characters at those positions: T, O, W -> "Tug of War"
```

### 6. QR Code: Salesforce URL

```
Built from shipping containers in the Nevada desert.
URL: https://sforce.co/4bAAGMH?r=qr
The ?r=qr parameter tracks discovery via the QR code.
```

### 7. Vault Door Ring Sequence

```
4-1-8-4-1-3-1-8-4-1-1-3-4-4-4-1-2-1-1-4-4-10-1-1-1-2-4-1-1-1-1-3-1-3-1-1-1-1-8-4-3-1-1-1-1-10

Hypothesis 1: Run-length encoding for binary -> ASCII
Hypothesis 2: Index pairs (row,col) for Sudoku grids
Hypothesis 3: Combined with Lost numbers as decryption key
```

### 8. Salesforce Mascot Icons

```
Spider/Tarantula -> Web/Network?     Ear          -> Einstein Voice
Bird/Canary      -> Data Cloud       Head/Brain   -> Einstein AI
Sine Wave        -> Wave Analytics   Witch/Dancer -> Astro
Chandler + 'D'   -> Data?            Elephant     -> Ruth
```

### 9. Emoji Sequence (Varies Between Frames)

```
Base pattern: Carousel(C) Sauropod(D) FerrisWheel(F) Anchor(A) Camping(C)
Position 3 changes most: Ferris Wheel / Sunflower / Blossom / Sun / Lemon
Position 2 always: Sauropod
This variation may encode additional information.
```

### 10. Background Hex: #152022

```
Slack ad background color encodes reaction counts: 15, 20, 22
B channel = 2, G channel = 7 -> "27"
```

### 11. Belt Code: 3X771

```
On MrBeast's belt (frame 496). The second '7' is highlighted in RED.
The red-highlighted digit may be the extraction target.
```

### 12. Color-Coded MRBEAST Belt

```
M=Green(1) R=Yellow(2) B=Blue(3) E=Red(4) A=Green(1) S=Yellow(2) T=Blue(3)
Pattern: 1-2-3-4-1-2-3 (repeating 4-color cycle)
```

### 13. T7 Street Marking: Positional Extraction

```
T7 -> 7th letter of BARCLAY = Y
This implies T1=B, T2=A, T3=R, T4=C, T5=L, T6=A, T7=Y
Look for T1-T6 markings in other frames.
```

### 14. Character Name: MRS. MAY-___

```
MAYBELLE -> "Ma Bell" (telephone company = call someone)
MAYBEUR  -> "Maybe You Are" (the winner)
MAYBERRY -> Mayberry, NC (Andy Griffith + MrBeast's home state)

A1Z26: MAY = M(13)+A(1)+Y(25) = 39, BELLE = B(2)+E(5)+L(12)+L(12)+E(5) = 36
Total = 75

Phone keypad: RED = 7-3-3 (sums to 13, or "733")
```

### 15. Talk Like A Pirate Day = September 19

```
Billboard in street scene. Real holiday: 09/19.
Also references MrBeast video: "I Found A $1,000,000 Pirate Treasure"
```

### 16. Countdown: 7-5-3-1

```
Odd numbers descending. Sum = 16 (a Lost number).
Could indicate: 4 steps remaining, or extraction indices.
```

### 17. Violation Ticket: OVERTIME

```
OFFENSE: OVERTIME | DATE: 02/11/24 | TIME: 6:30 PM | LOCATION: LAS VEGAS
Super Bowl LVIII went to overtime. KC Chiefs 25-22 over 49ers.
```

---

## Cross-Video Patterns

### Recurring Numbers

| Number | V1 | V2 | V3 | V4 | Significance |
|--------|----|----|----|----|-------------|
| **7** | Vault floor | Hidden on phone | Shield crest | T7, 7531, 777 address | Most repeated digit |
| **14** | G-14 | Everywhere (members, digits, channel) | Frame 14 | -- | Core constant |
| **17** | -- | -- | -- | "17 STOP NOW HERE", plate codes | Recurring in V4 |
| **27** | -- | Title, logo, metric sums | -- | RED=27, plate codes, BPE527 | Pervasive |
| **41** | -- | Countdown, tanker #41 | -- | -- | Dec 29 to Feb 8 |
| **101** | -- | -- | -- | Every bank door | Universal bank number |
| **108** | Lost numbers sum | -- | -- | -- | LOST mythology |
| **401** | -- | -- | -- | Merchants Bank only | Unique deliberate clue |
| **777** | -- | -- | -- | The Row Lofts address | Triple 7s |
| **3634826** | Tank barrel (15+ frames) | -- | -- | -- | ENDGAME |

### Recurring Keywords

| Word | Source | Role |
|------|--------|------|
| **ENDGAME** | V1 phone keypad | Master instruction / phase name |
| **HIDE** | V1 room cipher | Instruction |
| **FIND** | V1 vault rivets | Instruction |
| **ISLAND** | V2 steganography | Keyword / password |
| **MALCOLM** | V2 water tank | Keyword / person |
| **TOW** | V2 reaction cipher | Tug of War |
| **INCREDIBLE** | V2 missing tweet word | Password / keyword |
| **#secret-clue** | V2 Slack sidebar | Channel name |
| **RED HERRING** | V4 bank name | Meta-clue |
| **BARCLAY** | V4 hotel (20+ frames) | Real-world anchor |
| **PLAY** | V4 (from BARCLAY) | Call to action |
| **BEAST** | V1 + V4 | Vault, truck, jacket |
| **OVERTIME** | V4 violation ticket | SB LVIII reference |
| **MAYBELLE** | V4 character name | Ma Bell / Maybe You Are |
| **PEACH STATE** | V4 bank cup | Georgia |
| **GEORGIA** | V4 cup, outline, lottery | State theme |

### Emoji Sequence Variants

| Frame | Emojis | First Letters |
|-------|--------|---------------|
| 327 | Carousel Sauropod Blossom Anchor Camping | C-D-F/S-A-C |
| 329 | Carousel Sauropod FerrisWheel Anchor Camping | C-D-F-A-C |
| 334 | Carousel Sauropod Sunflower Anchor Tent | C-D-S-A-T |
| 340 | Carousel Sauropod FerrisWheel Anchor Camping | C-D-F-A-C |
| 344 | Unicorn Sauropod Lemon Anchor Camping | U-D-L-A-C |
| 345 | Carousel Sauropod Sun Anchor Tent | C-D-S-A-T |

Position 2 is always Sauropod. Position 3 varies most. This variation may encode data.

### Real-World Locations

| Location | Source | Address | Significance |
|----------|--------|---------|-------------|
| Barclay Hotel | V4 | 103 W 4th St, Los Angeles, CA 90013 | Primary set (20+ frames) |
| The Row DTLA | V4 | 777 S Alameda St, Los Angeles | Triple-7s address |
| Nevada Desert | V1 | ~36.34826 N (from 3634826?) | QR code site |
| Greenville, NC | V2 | Area code 252 | MrBeast's hometown |
| Charlotte, NC | V4 | Area code 704 | 704-BEAST-23 |
| Gainesville, GA | V4 | Peach State Bank | Mrs. Maybelle scene |
| Atlanta, GA | V4 | Mercedes-Benz Stadium | Framed on Maybelle's wall |

---

## Super Bowl Ad "Weird Things"

Per Hint #1: *"Figure out how to get an answer from each weird thing."* Each element yields one answer via standard online codes.

| Element | Frames | Code Type | Possible Answer |
|---------|--------|-----------|-----------------|
| RED HERRING BANK | 1124-1175 | Meta / wordplay | RED HERRING |
| BARCLAY HOTEL | 1124-1175 | Real-world lookup | 103 / 90013 / 4TH |
| TALK LIKE A PIRATE DAY | 1230-1237 | Calendar | SEPTEMBER 19 / 919 |
| NO PARKING YOUR TANK AT THE BANK | 1230-1237 | Rhyme / wordplay | ? |
| 30 MINUTE PARKING LIMIT | 1230-1237 | Number extraction | 30 |
| MRS. MAYBELLE | 088-110 | Wordplay / A1Z26 | MABELL / 75 |
| VIOLATION: OVERTIME | 250-254 | Sports reference | SB LVIII |
| T7 street marking | 1146 | Positional cipher | Y (7th of BARCLAY) |
| PL-01 tank | 700+ | Military lookup | STEALTH / POLISH |
| 7-5-3-1 countdown | 1075 | Sequence | 16 / ODD |
| Binary barcode on meter | 208 | Binary to ASCII | i / I / 0xAA |
| 4th St / Clay intersection | 1230+ | Address lookup | ? |
| Vehicle plates (JP1117 etc) | 331-385 | Number extraction | 17, 27, 77 |
| "17 STOP NOW HERE" | 491, 540 | Instruction | STOP at 17? |
| THE ROW LOFTS | 516 | Address lookup | 777 S Alameda |
| 704-BEAST-23 | 088-110 | Phone keypad | BEAST / Charlotte |
| Calendar double-dates | 099 | Pattern | 12 dates / July missing |
| X-01 on tank | 1154 | Sequence | 1st in series |
| 6601 on turret | 1158 | Unknown | Unknown |
| 8 red panels | 1158 | Binary / Braille | 00000000? |
| Purple lit window | 1175 | Binary position | ? |
| Morse on tank: -- -- | 1237 | Morse code | M M |
| PEACH STATE BANK (cup) | 1280 | Geographic | GEORGIA |
| Georgia state outline | 1276-1285 | State ID | GEORGIA / 4th state |
| Month-Number chart | 1285 | Cipher | Extraction key |
| Drinking Bird toy | 1281 | Physics | PERPETUAL / MOTION? |
| GEORGIA LOTTERY | 1284 | Lookup | Lottery numbers? |
| Shopify bag | 1280 | Brand | SHOP / SHOPIFY |
| Chandelier binary 111000 | 1515 | Binary / Braille | 56 / Braille 'l' |
| Chandelier bulb counts | 1504-1522 | Counting | Encoded sequence |
| Pink Flamingo | 1682 | Object code | FLAMINGO / PINK |
| Red Cup (out of place) | 1525+ | Deliberate prop | RED CUP |
| 401 (not reversed) | 1524 | Number | **Unique to Merchants Bank** |
| ECNARTNE (reversed) | 1530 | Reversed text | ENTRANCE |
| Mercedes-Benz Stadium pic | 1276 | Venue | ATLANTA |
| Keith Haring mural | ~3450 | Art reference | TBD (not yet processed) |

**More elements will be catalogued as Video 4 processing continues.**

---

## Behind the Scenes Gallery Clues

The [Behind the Scenes page](https://mrbeast.salesforce.com/behindthescenes) contains 9 production photos. Per Hint #1: *"look behind the scenes"* -- these images may contain intentional clues.

### Golden Desert Vault Expense List

A clipboard reads:

```
FEBRUARY 2026
OPERATING CAPITAL EXPENSES
OF GOLDEN DESERT VAULT

One Million Dollars in Large Bills
MrBeast-Branded Sand Hydrofoil
Proton Cannon Usable for Missile Defense
Lion (2)
Ramjet Engine Upgrades
Lamborghini Countach Moved to Garage
Vault Code Generator (Unbreakable)

[MrBeast signature]
```

First-letter acrostic: **O-M-P-L-R-L-V** (no obvious word -- may use a different extraction). The items themselves are absurd/fictional, suggesting the real content is encoded.

### Vault Set Clapperboard

```
A021 | MIKE
SALESFORCE: INSIDE THE BEAST
J. WOLINER
M. CORDERO
1.20.26
```

Production title "INSIDE THE BEAST" and shot date January 20, 2026. Puzzlemaster Mike (Lone Shark Games) is the subject.

### Lobby Scene Props

A group photo in a hotel/office lobby contains:

- **4 world time zone clocks:** Tokyo, London, Chicago, New York
- **Rubik's cube** held by one person
- **Large jar of coins** held by another
- **"FEASTABLES" sweatshirt** (MrBeast's chocolate brand)
- **Magazine/book** being read by a third person
- **Papers and succulent** on coffee table

The 4 time zones may encode: time differences, specific times shown, or city initials (T-L-C-N).

### Belt Construction

A prop maker is shown assembling MrBeast's belt (the one with code 3X771 and color-coded MRBEAST letters). Blue and yellow tape are used for the colored X markings.

---

## Current Best Guesses

The puzzle was designed by Lone Shark Games to unfold over weeks. Not all clues have been released. The 9 variety puzzles require extraction keys we don't have yet. **The final answer is not something we can derive from current data alone.**

That said, here are the strongest candidates to try:

### Tier 1: Highest Confidence

| Guess | Reasoning |
|-------|-----------|
| `ENDGAME` | Phone keypad cipher of 3634826 (most prominent code across all videos) |
| `HIDE` | Room layout cipher, confirmed across multiple frames |
| `ISLAND` | Steganographic keyword hidden in V2 tweet |
| `PLAY` | Highlighted from BARCLAY across 20+ frames |
| `4 8 15 16 23 42` | Lost numbers on vault door |
| `108` | Sum of Lost numbers |
| `ENDGAME-1` | Full code from tank barrel |
| `#secret-clue` | Slack channel name visible in V2 |

### Tier 2: Strong Pattern-Based

| Guess | Reasoning |
|-------|-----------|
| `27` | Most pervasive number across all 4 videos |
| `BARCLAY` | Dominant real-world anchor in the ad |
| `BEAST` | On vault, truck, jacket, belt |
| `INCREDIBLE` | Missing word from V2 tweet |
| `401` | Only bank number that isn't 101 |
| `OVERTIME` | Violation ticket, SB LVIII reference |
| `GEORGIA` | Pervasive state theme in Maybelle scene |

### Tier 3: Combinatorial

`919`, `PIRATE`, `MABELL`, `FLAMINGO`, `101`, `56`, `CLAY`, `MALCOLM`, `CANARY`, `3X771`, `777`, `@the1Mil`, `704-BEAST-23`, `REDHERRING`, `MRBEAST6000`, `36.34826`

### GPS Theory

The number 3634826 could be latitude 36.34826 N, which maps to the Nevada desert near Las Vegas -- where the QR code was physically built from shipping containers. A full GPS coordinate would need a longitude from another clue.

---

## Next Steps

### Priority 1: Complete the 9 Variety Puzzles (Stage 1, Hub 1)

- [x] Found all 9 puzzle links via BeastForce67 pinned comments
- [x] Downloaded all 9 puzzle images
- [x] Solved Puzzle 2 Sudoku grid (all 81 cells)
- [x] Solved all 43 clues for Puzzle 8 pyramid crossword
- [x] Matched 13/19 TV shows for Puzzle 3
- [ ] Complete remaining puzzle solves (1, 4, 5, 6, 7, 9)
- [ ] Crack extraction methods (likely need bank-scene keys from Video 4)
- [ ] Assemble the 9-word clue
- [ ] Interpret the instruction it gives

### Priority 2: Map Lab Screens to Bank Clues (Stage 1, Hub 3)

Per Hint #2, the 8 Salesforce computer lab screens (V1 frame 208) map 1:1 to bank clues. This is the key to unlocking the bank puzzles.

- [ ] Identify all distinct bank puzzles in Video 4
- [ ] Match each lab screen icon to its corresponding bank clue
- [ ] Use process of elimination (each screen used exactly once)

### Priority 3: Decode Street Scene Elements (Stage 1, Hub 2)

- [ ] Catalogue every "weird thing" Jimmy passes in the ad
- [ ] Apply standard online codes to each element
- [ ] Check all directions: up, down, forward, backward, behind the scenes
- [ ] Compile one answer per element

### Priority 4: Stage 2 Crossword

- [ ] Monitor crossword clue drops as Stage 1 progress unlocks them
- [ ] Begin filling in the crossword as clues appear
- [ ] Cross-reference crossword answers with Stage 1 findings

### Other

- [ ] Finish Video 4 pipeline (~2,163 frames remaining)
- [ ] Analyze BTS gallery images for additional hidden clues
- [ ] Register at [mrbeast.salesforce.com](https://mrbeast.salesforce.com/)
- [ ] Visit `https://sforce.co/4bAAGMH?r=qr` (decoded QR code)
- [ ] Monitor daily hint drops from Lone Shark Games
- [ ] Join community solving groups (Reddit, Discord, Slack)

---

## Contributing

This puzzle was explicitly designed for collaboration:

> *"We never said you had to do this alone. Only one person can claim the prize, but it's probably not possible for one person to find and solve everything."*
> -- Lone Shark Games, Hint #1

**How to help:**
- Solve the remaining variety puzzles (especially 1, 4, 5, 6, 7, 9)
- Identify the extraction methods that convert solved grids into answer words
- Decode "weird things" from the Super Bowl ad using standard cipher lookups
- Cross-reference findings with community progress on Reddit and ARGNet
- Watch for daily hint drops from Lone Shark Games

All puzzle images are in `puzzle_analysis/superbowl_ad_1M_frames/`. Open an issue or PR with any findings.

---

## Sources

- **[Hint #1 -- Lone Shark Games (Feb 9, 2026)](https://youtu.be/hGuA0a15VWQ)**
- **[Hint #2 -- mrbeast.salesforce.com (Feb 10, 2026)](https://mrbeast.salesforce.com/)**
- **[Behind the Scenes -- mrbeast.salesforce.com](https://mrbeast.salesforce.com/behindthescenes)**
- [ARGNet: Start Slacking Off with MrBeast's Million Dollar Puzzle Hunt](https://www.argn.com/2026/02/start_slacking_off_with_mrbeasts_million_dollar_puzzle_hunt/)
- [Newsweek: MrBeast Shares Update on $1 Million Puzzle](https://www.newsweek.com/mrbeast-shares-update-on-1-million-puzzle-advertised-during-super-bowl-11490124)
- [ABC News: MrBeast drops big hint for $1M puzzle](https://abcnews.go.com/GMA/Culture/mrbeast-drops-big-hint-1m-puzzle-salesforce-super/story?id=129987912)
- [Lone Shark Games: The Puzzle Vault](https://lonesharkgames.com/the-puzzle-vault/)
- [Adweek: Salesforce Teams Up with MrBeast](https://www.adweek.com/brand-marketing/salesforce-teams-up-with-mrbeast-to-give-away-1-million-at-super-bowl-60/)
- [Benzinga: Here's What You Have To Do](https://www.benzinga.com/markets/tech/26/02/50471320/mrbeast-says-first-person-to-crack-his-super-bowl-ad-puzzle-wins-1-million-heres-what-you-have-to-do)

---

*Generated by [Gemini 3 Flash Preview](https://ai.google.dev/) (agentic vision) + [Claude Opus 4.6](https://claude.ai/) analysis pipeline. 4,758 of 6,918 frames analyzed (68.8%). Video 4 processing ongoing. Last updated: 2026-02-11.*
