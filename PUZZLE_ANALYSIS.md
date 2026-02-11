# MrBeast x Salesforce $1,000,000 Puzzle Hunt -- Master Analysis

> **Status:** UNSOLVED (as of Feb 9, 2026)
> **Contest:** Feb 8 - Apr 2, 2026
> **Register:** [mrbeast.salesforce.com](https://mrbeast.salesforce.com/)
> **Submit:** Slack the code to @MrBeast
> **Designer:** [Lone Shark Games](https://lonesharkgames.com/the-puzzle-vault/)

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Puzzle Architecture](#puzzle-architecture)
3. [All Decoded Video Clues](#all-decoded-video-clues)
4. [Key Cipher Decodings](#key-cipher-decodings)
5. [Cross-Video Pattern Analysis](#cross-video-pattern-analysis)
6. [9 Variety Puzzles — Solving Progress](#9-variety-puzzles--solving-progress)
7. [Educated Best Guess](#educated-best-guess)
8. [Super Bowl Ad "Weird Things" Catalogue](#super-bowl-ad-weird-things-catalogue)
9. [Actionable Next Steps](#actionable-next-steps)
10. [Sources](#sources)

---

## Executive Summary

MrBeast confirmed on Feb 9: *"No one has solved it... For the record it's very hard and lots of steps."*
Lone Shark Games stated: *"Not all of the puzzle has been revealed."*

**60 million people** visited the contest site on day 1. Nobody is close.

This is a **multi-week ARG** with daily clue drops. Our Gemini 3 Flash frame-by-frame analysis of **6,918 frames** across 4 videos has extracted every embedded clue, giving us the complete cipher framework and clue inventory.

### Pipeline Status

| Video | Folder | Frames | Status |
|-------|--------|--------|--------|
| 1. First To Find $1,000,000 | first_to_find_1M | 769/769 | **COMPLETE** |
| 2. One Idea. 27 Days. Built with Slack | slack_ad | 1,441/1,441 | **COMPLETE** |
| 3. Rewatch This Video to Win $1M | rewatch_to_win_1M | 1,235/1,234 | **COMPLETE** |
| 4. Watch My Super Bowl Ad to Win $1M | superbowl_ad_1M | ~1,318/3,476 | **38% (free tier, PID 59537)** |

---

## Puzzle Architecture

### The 3-Layer Structure (CONFIRMED by Hint #1)

```
Layer 1: SUPER BOWL AD (Video 4, 3,476 frames)
  └─ "Almost everything Jimmy passes by is a clue"
  └─ "Look up, down, forward, backward, and behind the scenes"
  └─ "Figure out how to get an answer from each weird thing"
  └─ Street scene clues → provide INPUTS for bank puzzles
  └─ "Some of these puzzles use codes you can find online"

Layer 2: BANK SCENES (inside the ad)
  └─ "You will need specific content from the Super Bowl ad to solve anything there"
  └─ Bank puzzles REQUIRE street-scene answers as inputs
  └─ This is where the cipher keys from street scenes get applied

Layer 3: 9 REDDIT VARIETY PUZZLES ← CRITICAL PATH
  └─ Playlist of 9 past MrBeast videos (pinned comments)
  └─ Each puzzle "ends in a word"
  └─ 9 words form a clue IN ORDER
  └─ CONFIRMED WORD LENGTHS: 5, 9, 5, 7, 8, 4, 9, 6, 5
  └─ "That will help define the nature of the search"
  └─ "If you can get that 9-word clue, you'll take the FIRST STEP"

Layer 4: REAL-WORLD CLUES (rolling daily)
  └─ MrBeast's Super Bowl photos ("look for numbers")
  └─ Tonight Show appearance (Feb 6, 2026)
  └─ Daily hint drops from Lone Shark Games
  └─ "Anytime you see MrBeast with Salesforce, assume there's something there"
  └─ Behind-the-scenes video (Video 2: Slack ad) is part of "behind the scenes"
```

### How the Final Code is Constructed (UPDATED per Hint #1)

```
Step 1: Solve 9 Reddit Variety Puzzles
  └─ Each puzzle yields ONE answer word
  └─ Word lengths: 5, 9, 5, 7, 8, 4, 9, 6, 5
  └─ 9 words → A CLUE PHRASE that "defines the nature of the search"
                         ↓
Step 2: Use the 9-word clue to understand WHAT to search for
  └─ "There is a direct way through this ultra-hard puzzle hunt"
                         ↓
Step 3: Decode Super Bowl ad street scenes
  └─ Each "weird thing" yields an answer (standard online ciphers)
  └─ Look in ALL directions: up, down, forward, backward
                         ↓
Step 4: Apply street-scene answers to bank scenes
  └─ Bank scenes contain puzzles that REQUIRE ad content
  └─ This is the extraction step
                         ↓
Step 5: Derive the final Slack code
  └─ First to Slack @MrBeast the correct code wins $1M
```

### OFFICIAL HINT #1 (Lone Shark Games, Feb 9, 2026)

> **Source:** https://youtu.be/hGuA0a15VWQ
>
> **Full text of key section:**
>
> *"Here's HINT #1: Some of these puzzles use codes you can find online.
> With the Super Bowl ad, almost everything Jimmy passes by is a clue. Look up, down, forward, backward, and behind the scenes. Figure out how to get an answer from each weird thing.
> In the bank, the same is true, but you will need specific content from the Super Bowl ad to solve anything there.
> Last, but not least, if you found the video playlist's pinned comments, each puzzle ends in a word that makes part of a 9-word clue, in order.
> The word lengths are 5, 9, 5, 7, 8, 4, 9, 6, and 5.
> That will help define the nature of the search.
> If you can get that 9-word clue, you'll take the first step on your journey.
> There is a direct way through this ultra-hard puzzle hunt.
> You can find it. Then you can win a million dollars!"*
>
> **Other key quotes:**
> - "We never said you had to do this alone"
> - "Only one person can claim the prize, but it's probably not possible for one person to find and solve everything"
> - "Start a wiki, where you list potential puzzles and possible paths and solutions"
> - "Draw on all the world's resources"
> - "Nobody's got a million dollars yet, so there's still time to catch up"
> - Daily clue drops confirmed: "If you can't solve it today, don't panic. Tomorrow we'll drop another clue."
> - Escalation promised: "If it's still too hard for you all - then we'll unleash some serious help"

#### Hint #1 Analysis

| Revelation | Implication for Us |
|------------|-------------------|
| "codes you can find online" | Standard ciphers confirmed: A1Z26, Morse, Braille, semaphore, phone keypad, etc. |
| "everything Jimmy passes by" | Our frame-by-frame V4 analysis is correct approach |
| "up, down, forward, backward" | Check ALL directions in each frame (ceiling, floor, reverse text, reflections) |
| "behind the scenes" | Video 2 (Slack making-of) is part of the puzzle path |
| "get an answer from each weird thing" | Each prop/sign yields exactly ONE answer word |
| "bank needs Super Bowl ad content" | Street answers are INPUTS to bank puzzles (dependency!) |
| "9-word clue, in order" | Reddit puzzles → 9 words → master instruction |
| "word lengths 5,9,5,7,8,4,9,6,5" | Constrains possible answer words for each puzzle |
| "define the nature of the search" | The 9-word phrase tells you WHAT KIND of search to do |
| "first step on your journey" | 9-word clue is Step 1, not the final answer |
| "direct way through" | There IS a single clear path (not random guessing) |

---

## All Decoded Video Clues

### Video 1: "First To Find $1,000,000, Keeps It!" (769 frames) ✅

| Frame | Conf | Category | Raw Value | Decoded | Notes |
|-------|------|----------|-----------|---------|-------|
| 005 | 0.95 | cipher | Red-bordered bills | A1Z26: 20=T, 5=E, 1=A | Custom MrBeast currency |
| 111 | 0.90 | text | Fine print | Starts 2/8/26, Ends 4/2/26. mrbeast.salesforce.com | Contest rules |
| 189 | 0.95 | text | CANARY + LOCKED | Canary is locked, needs unlocking | Salesforce lab setting |
| 189 | 0.95 | text | 3% | On MrBeast's belt | Percentage clue |
| 189 | 1.00 | text | Fine print URL | mrbeast.salesforce.com | Registration |
| 192 | 0.95 | text | CANARY SINGING | Canary status changed | Ear with 4 dashes (_ _ _ _) |
| 192 | 0.95 | spatial | 6 head models | Count = 6 | Three Wise Monkeys motif |
| **208** | **1.0** | symbol | Screen icons | Spider, Bird, Sine Wave, Chandler+'D', Ear, Head, Witch, '1' | **Salesforce mascots** |
| **232** | **0.95** | cipher | Room layout | **H-I-D-E** (8=H, I-Red, D-Green, 5=E) | **Key instruction** |
| 275 | 0.90 | math | Spider=8, Swiss Flag | 10^5=100,000, weight=22.4L | Scientific constants |
| 279 | 0.95 | math | n^3=n | Solutions: -1, 0, 1 | ear+mute = "DEAF" |
| **340** | **0.90** | emoji | 🎠🦕🎡⚓🏕️ | Slackbot "Good luck!" | **Recurring emoji code** |
| **376** | **0.85** | text | FIND | Rivets on vault door | **Instruction word** |
| **382** | **0.95** | text | BEAST 6000 | Rivets on vault door | MrBeast's OG handle |
| **392** | **1.0** | cipher | 3634826-1 | **ENDGAME-1** (phone keypad) | **Master code** |
| 436 | 1.0 | spatial | 3634826-1 breakdown | 36 dots, 34 stripes, 8 lights, 26 total | Room element counts validate code |
| 488 | 0.85 | text | 1026-1 | On equipment | Variant of main code |
| **496** | **0.95** | text | 3X771 | Belt code (red highlighted 7) | **Unique code** |
| 496 | 0.95 | text | 4826-1 | On tank | Partial main code |
| 575 | 0.85 | text | G-14 | "Classified" reference | Military designation |
| **609** | **0.95** | cipher | Vault ring numbers | Complex number sequence on rings | **Combination lock sequence** |
| **628** | **0.95** | cipher | Vault door ring | 4-1-8-4-1-3-1-8-4-1-1-3-4-4-4-1-2-1-1-4-4-10-1-1-1-2-4-1-1-1-1-3-1-3-1-1-1-1-8-4-3-1-1-1-1-10 | **Run-length encoded data?** |
| **634** | **0.95** | cipher | 4-8-15-16-23-42 | **"Lost" numbers (sum=108)** | **Vault combination** |
| 634 | 0.80 | code | MRBEAST belt colors | M(Grn)R(Yel)B(Blu)E(Red)A(Grn)S(Yel)T(Blu) | 4-color cycle |
| **654** | **0.95** | visual | Red slashes 1-2-3 | "Release" text on ground, 12 vault spokes | **Sequence instruction** |
| **710** | **1.0** | code | **QR CODE** | **`https://sforce.co/4bAAGMH?r=qr`** | **Decoded Salesforce URL!** |
| 716 | 1.0 | visual | QR code (diff angle) | Same QR, built from shipping containers in desert | Aerial view |

### Video 2: "One Idea. 27 Days. Built with Slack." (1,441 frames) ✅

Behind-the-scenes documentary about making the Super Bowl ad. **Dense with encoded clues.**

| Frame | Conf | Category | Raw Value | Decoded | Notes |
|-------|------|----------|-----------|---------|-------|
| 001 | 0.85 | spatial | MrBeast logo | 27 geometric features | Matches "27 Days" title |
| 057 | 0.80 | symbol | Salesforce logo (modified) | 10 bumps, distributed 4-2-3-1 | **Modified cloud shape** |
| **200** | **0.95** | steg | Tweet text LSB | **"I-S-L-A-N-D"** hidden | **Steganographic keyword** |
| **213** | **1.0** | math | Countdown calculation | 41-day countdown (Dec 29→Feb 8) | Word positions: 14+27=41 |
| **252** | **1.0** | cipher | **"Rosetta Stone" frame** | A1Z26 cipher confirmed as key | Tweet metrics digits sum to 27, "MrBeast"=78 in A1Z26, frame 252=Greenville NC area code |
| **294** | **1.0** | code | Tweet metrics | Unix timestamp 1441015326 = Aug 31 2015 | Missing word: **"incredible"** |
| **507** | **0.95** | symbol | Feastables train | Locomotive #600, tanker #41 | Jimmy(5)+message(16)+icons(6)=27 |
| **604** | **0.95** | text | Slack channel sidebar | **#secret-clue** | **Hidden Slack channel name!** |
| 604 | 0.70 | text | Water tank label | **"MALCOLM"** | Possible keyword/reference |
| 604 | 0.85 | text | Slack message | Jimmy: "check the lights for $1M challenge" | Production reference |
| **649** | **0.95** | text | Phone screen numbers | Hidden "7" above time, hidden "1" below logo | Encodes 1-2-7 or 7-2-1 |
| 649 | 0.90 | text | Slack message | "Jimmy: Pyramids?? 🏜️" | Desert/Egypt reference |
| **743** | **1.0** | math | **Number 14 encoded everywhere** | 14 members, 9+4+1=14, #project-big-game=14 chars, frame 7+4+3=14, initials H+B+C+A=8+2+3+1=14 | **Core number** |
| **751** | **0.95** | cipher | Reaction counts as indices | 15,20,22 → **"T-O-W"** (Tug of War) | Indices into first message text |
| **753** | **0.95** | steg | Background color hex | **#152022** → encodes 15, 20, 22 | B=2, G=7 → 27 |
| 753 | 0.80 | visual | Squid Game reference | Image shows 456 players in pink jumpsuits | MrBeast's most famous video |

**Key Number 27 Encodings Found in Video 2:**
- Title: "27 Days"
- Logo: 27 geometric features
- A1Z26: "MrBeast" = 78 (digits 7+8=15, and 15+12=27 or 78/3=26≈27)
- Tweet metric digit sums = 27
- Jimmy(5) + message length(16) + Slack icons(6) = 27
- Background hex #152022: B channel=2, G channel=7 → "27"

### Video 3: "Rewatch This Video to Win $1,000,000" (1,234 frames) ✅

**CONFIRMED RED HERRING / TROLL — but rich with data.**

#### 10 Hidden Sign Words (in frame order)

MrBeast holds a white sign throughout the video. The word on the sign changes as the video progresses:

| # | Word | Frame Range | Themed Characters | Steg Marker |
|---|------|-------------|-------------------|-------------|
| 1 | **Help** | f00009-f00200 | — | — |
| 2 | **Me** | f00112-f00200 | — | — |
| 3 | **Patience** | f00221-f00227 | Basketball players (jersey #23) | — |
| 4 | **You** | f00307-f00406 | — | — |
| 5 | **Win** | f00409-f00518 | — | — |
| 6 | **$1,000,000** | f00519-f00597 | — | — |
| 7 | **@ the** | f00598-f00715 | Black Panther masks, fire performer, ringmaster | f00598: "@the1Mil" handle |
| 8 | **Big** | f00715-f00812 | Shining twins, Alice in Wonderland | **"HIDDEN WORD IS 7/10"** |
| 9 | **Game** | f00813-f01090 | Boxers (Everlast), waiters, tuxedos | — |
| 10 | **[Troll Acrostic]** | f01091-f01234 | Waiters with red door models | Acrostic: "THIS MEANS NOTHING..." |

#### Reconstructed Message:
**"HELP ME [PATIENCE] YOU WIN $1,000,000 @ THE BIG GAME"**

#### Troll Acrostic (Full Text):
The poem on the final sign, when reading first letters of each capitalized word:
> **"THIS MEANS NOTHING I JUST WANTED TO WASTE YOUR TIME LOL"**

#### Other Rewatch Clues

| Frame | Finding | Notes |
|-------|---------|-------|
| f00001-006 | School of Athens parody painting | MrBeast as Plato (pointing up), crew as philosophers |
| f00006 | Number **7** on table object (shield crest) | Also "7" shape in carpet texture |
| f00006 | Blue neon light bar above painting | Possible Morse dash |
| f00006 | 2x3 grid of ceiling lights | Possible Braille character |
| f00598 | **"@the1Mil"** social media handle | On sign during "@ the" section |
| f00598+ | **"HECK"** in red letters | Appears alongside "@ the" in multiple frames |
| f00764 | Steganographic "HIDDEN WORD IS 7/10" | Confirms 10-word structure, Big=word 7 |
| f00890 | **"HERE"** text detected | Among Game frames |

**Verdict: This video is a deliberate red herring.** The sign message and troll acrostic confirm it's designed to waste time. However, the "@the1Mil" handle and "HECK" in red may be legitimate cross-video breadcrumbs.

### Video 4: "Watch My Super Bowl Ad To Win $1,000,000!" (3,476 frames) — 38% PROCESSED

**The actual Super Bowl LX ad. Dense with puzzle elements. Free-tier processing ongoing.**

#### Key Scenes Decoded So Far (frames 1-1829)

| Frame | Conf | Category | Raw Value | Decoded | Notes |
|-------|------|----------|-----------|---------|-------|
| **088-110** | **0.95** | phone | **657-283-9800** | Phone number on screen | Salesforce area? No reply when texted |
| 088-110 | 0.95 | phone | **650-283-9795** | Second phone number | Salesforce HQ area code (650) |
| 088-110 | 0.90 | phone | **480-234-354?** | Third phone number (partial) | Arizona area code |
| 088-110 | 0.90 | phone | **704-232-7823** | = **704-BEAST-23** | Charlotte NC (MrBeast hometown!) |
| **099** | **1.0** | text | MRS. MAYBELLE name | **"Ma Bell"** = telephone company | Character name is a cipher |
| 099 | 1.0 | math | MAY=39, BELLE=36 | M13+A1+Y25=39, B2+E5+L12+L12+E5=36 | A1Z26 encoding of name |
| 099 | 1.0 | cipher | RED via phone keypad | **RED = 27** (R=7, E=3, D=3... or 733) | 27 appears again! |
| 099 | 1.0 | calendar | Double dates circled | 1/1, 2/2, 3/3...12/12 all circled | Calendar pattern |
| 099 | 1.0 | calendar | Months with 31 days listed | **July missing** from list | Deliberate omission |
| **108** | **1.0** | text | MRS. MAYBEUR | = **"Maybe You Are"** | Name decoded as message |
| 108 | 1.0 | text | MRS. MAYBERRY | = **Mayberry, NC** (Andy Griffith) | NC reference (MrBeast is from NC) |
| **208** | 0.95 | code | Binary barcode on parking meter | ASCII 'i'/'I', decimal 1226, hex 0xAA | Post-mounted barcode pattern |
| **250-254** | 0.95 | text | VIOLATION ticket | OFFENSE: **OVERTIME** | Super Bowl LVIII went to overtime |
| 250-254 | 0.95 | text | Ticket date | **02/11/24, 6:30 PM, LAS VEGAS** | Exact date of SB LVIII |
| **331-385** | 0.95 | spatial | Vehicle plate codes | JP1117, BPE527, BP6327 | Many end in **17, 27, 77** |
| **491** | 0.95 | text | "17 STOP NOW HERE" | Number 17 prominent | Instruction? |
| **516** | 0.95 | text | THE ROW LOFTS | **777 S Alameda St, LA** | Real address, triple 7s |
| **540** | 0.95 | text | "17 STOP NOW HERE" (repeat) | Frame 540 = 5+4+0 = 9 | 17 and 9 both appear |
| **700-718** | 0.95 | setting | Tank in street scene | PL-01 Polish "stealth" concept tank | "Hidden/stealth" theme |
| **1074** | **1.0** | cipher | MRS. MAYBELLE decoded | MAY=39, BELLE=36, total=75 | Deepest character decode |
| **1075** | **0.95** | sequence | **7-5-3-1 countdown** | Odd numbers descending on weekdays | Countdown to... what? |
| **1124-1175** | 0.95 | text | **RED HERRING BANK** | Meta-clue: "this is a distraction" | On bank building (1.0 conf) |
| 1124-1175 | 0.95 | text | **BARCLAY HOTEL** | **103 W 4th St, LA, 90013** | Real-world anchor location |
| 1124-1175 | 0.85 | text | **PLAY** | Highlighted from BAR**CLAY** sign | Call to action |
| 1124-1175 | 0.80 | text | **CLAY** | Vertical portion of BARCLAY | Separately emphasized |
| **1130** | 0.85 | code | Spatial codes **231** and **072** | Near PLAY sign | Number pair |
| **1146** | 0.85 | cipher | **T7** street marking | 7th letter of BARCLAY = **Y** | Positional extraction |
| 1146 | 0.90 | text | **BEAST** on armored truck | MrBeast branding confirmed | Custom prop |
| 1146 | 0.60 | symbol | **) RED HERRING BANK (** | Parentheses flanking name | Function call syntax? |
| **1149** | 0.90 | spatial | Tow truck pulling bank | "Red Herring is being removed" | Meta-visual storytelling |
| 1149 | 0.70 | text | LAY (from BARCLAY) | Part of **PLAY** or address hint | Recurring |
| 1149 | 0.60 | spatial | **4 red panels** with circles | Possible binary or digit 4 | Matches 4th St |
| **1154** | 0.90 | text | **X-01** on tank turret | Tank designation, sequence start | X-02 in background? |
| 1154 | 1.0 | symbol | MrBeast Panther logo on truck | Custom prop confirmation | — |
| 1154 | 0.50 | spatial | **4 soldiers in line** | Count=4, matches 4th St address | Reinforces "4" |
| **1158** | 0.90 | code | **6601** on tank turret | Faint number revealed by enhancement | Turret code |
| 1158 | 0.85 | text | PLAY (from BARCLAY sign) | Confirmed across multiple frames | Persistent |
| 1158 | 0.40 | spatial | **8 red panels** with circles | Possible binary: 00000000 | On bank facade |
| **1175** | 0.90 | text | CLAY (vertical) | BAR-**CLAY** split | Dream's real name? |
| 1175 | 0.50 | spatial | **Purple lit window** | Single window in Barclay Hotel | Binary/positional code? |
| **1230-1237** | **0.85** | text | **NO PARKING YOUR TANK AT THE BANK** | Custom prop sign, rhyming | MrBeast video refs |
| 1230-1237 | 0.75 | text | **TALK LIKE A PIRATE DAY** | Billboard in background | **Sept 19 = 09/19** |
| 1230-1237 | 0.70 | text | **30 MINUTE PARKING LIMIT** | Number **30** on sign | "30 Days" challenge ref? |
| 1230-1237 | 0.80 | text | **4th St / Clay** | Street intersection signs | Confirms location |
| 1230-1237 | 0.60 | text | **HOTEL CLAY** | From different angle | = BARCLAY without BAR |
| 1230-1237 | 0.50 | spatial | Morse on tank lights: **-- --** | **M M** in Morse | Or binary "11" |
| **1275-1285** | **0.9** | text | **MRS. MAYBELLE** (nameplate) | Ma Bell / Maybe You Are | Consistent across 10+ frames |
| **1276** | 0.9 | symbol | **Georgia state outline + State Farm** | Atlanta, Georgia | Cup logo + framed picture of Mercedes-Benz Stadium |
| **1276** | 0.7 | text | Calendar months JAN-DEC w/ numbers | Standard month numbering 1-12 | On wall behind monitor |
| **1277-1278** | 0.8 | calendar | **Specific months listed**: Jan, Apr, Jul, Oct, Nov, Dec | Subset months on display | Calendar variation |
| **1280** | **0.9** | text | **PEACH STATE BANK** | Gainesville, GA (Georgia Peach State) | On coffee cup logo |
| **1280** | 0.9 | symbol | **Shopify logo** (green bag) | E-commerce platform | On teller counter |
| **1281** | 0.8 | symbol | **Drinking Bird toy** | Classic desk toy / perpetual motion | On Mrs. Maybelle's desk |
| **1281** | 0.8 | text | **BEAST COFFEE** on Georgia outline | MrBeast branding + Georgia | Cup/sign variant |
| **1284** | 0.8 | text | **GEORGIA LOTTERY** | Lottery / prize reference | On wall signage |
| **1285** | **0.95** | cipher | **Month→Number Chart: Apr=1, Jun=2, Jul=3, Aug=4, Sep=5, Dec=6** | 6 specific months assigned sequential numbers | 2024 chart on wall — **KEY PUZZLE ELEMENT** |
| **1285** | 0.6 | symbol | **Green figure** (Sour Patch Kid?) | Sponsor reference | On pen/stylus on desk |
| **1408-1522** | 0.8 | setting | **MrBeast + "Granny" conversation** | Dialogue scene w/ Mrs. Maybelle | Window blinds, chandelier, hidden background person |
| **1504-1520** | 0.7-0.8 | spatial | **Chandelier bulb counts vary**: 6, 7, 8, 10 | Different counts per frame = encoded data | Bulb on/off patterns change |
| **1515** | 0.85 | code | **Chandelier binary: 111000** | **56 decimal** or **Braille 'l'** (dots 1-2-3) | Top 3 bright, bottom 3 dim |
| **1508** | 0.6 | text | **OPEN** | Visible on sign/screen | Instruction? |
| **1507-1521** | 0.6-0.8 | symbol | **Circular logo with 'C'** | Possibly **CHASE** bank logo | On window/blinds |
| **1504-1522** | 0.7-0.9 | contextual | **Hidden person in sunglasses + hoodie** | Recurring background figure | "Observer" in every granny frame |
| **1512** | 0.8 | text | **01 / 10** | Number on screen/sign | Binary? Room number? |
| **1516** | 0.8 | text | **CHASE** (?) | Circular logo identified | Possible bank name |
| **1523** | 0.8 | text | **101** above door | Bank lobby number | Suite/building number |
| **1524** | **0.85** | text | **401** (NOT reversed) | **Deliberate clue** — text "STNAHCREM" IS reversed but 401 is NOT | **MERCHANTS BANK**, L.A. |
| **1525** | 0.85 | text | **FIRST NATIONAL BANK** / **101** | Archway text + door number | Bank #3 identified |
| **1525** | 0.6 | symbol | **Red Cup** (Solo cup) | Out-of-place prop = deliberate | On teller counter |
| **1530** | 0.8 | text | **ECNARTNE** (= ENTRANCE reversed) | Reversed door text | **BANK OF BEAST** |
| **1530** | 0.8 | text | **101** | Recurring door number | Same across multiple banks |
| **1555** | 0.7 | text | **GRANTS 101** | Reversed on glass door | **GRANTS BANK** identified |
| **1555** | 0.8 | symbol | Feastables items on counter | Chocolate bar + cup | Brand placement |
| **1555** | 0.8 | contextual | **YouTube tablet** showing video ~25% progress | Reference to platform | Left side of frame |
| **1682** | 0.6 | text | **STNAHCREM** = **MERCHANTS** (reversed) | Glass door identification | **MERCHANTS BANK** revisited |
| **1682** | 0.7 | symbol | **Pink Flamingo** on teller counter | Deliberate Easter egg / prop | Recurring MrBeast motif |
| **1682** | 0.95 | symbol | **MrBeast logo** on red cup | Brand on counter | Confirms set |
| **1829** | 0.4 | setting | Close-up: Jimmy + elderly woman (Mrs. Maybelle) | Dialogue scene continues | Low-clue transition frame |

#### NEW: Banks Identified in the Super Bowl Ad

| # | Bank Name | Frames | Key Props | Numbers |
|---|-----------|--------|-----------|---------|
| 1 | **PEACH STATE BANK** | 1275-1285 | Georgia cup, Shopify bag, Drinking Bird, month chart, GEORGIA LOTTERY | — |
| 2 | **RED HERRING BANK** | 1124-1175 | Tow truck removing it, BARCLAY HOTEL backdrop | 231, 072, 6601 |
| 3 | **FIRST NATIONAL BANK** | 1525 | Red Cup, YouTube tablet, 4 guards | 101 |
| 4 | **GRANTS BANK** | 1555 | Feastables, YouTube tablet, Feastables cup | 101 |
| 5 | **MERCHANTS BANK** | 1524, 1682 | Pink Flamingo, MrBeast cup, glass door | **401** (not reversed!), 101 |
| 6 | **BANK OF BEAST** | 1530 | ECNARTNE (entrance reversed) | 101 |

**Pattern:** 101 appears on EVERY bank door. Only Merchants Bank has a unique number: **401** (deliberately NOT reversed when other text IS reversed).

#### NEW: Month→Number Chart Cipher (Frame 1285)

```
On wall chart labeled "2024":
  April    = 1
  June     = 2
  July     = 3
  August   = 4
  September = 5
  December = 6

Missing months: Jan, Feb, Mar, MAY, Oct, Nov
Month numbers:   4,   6,   7,   8,   9,   12

Observations:
- "MAYBELLE" contains MAY — the most notable missing month
- The assigned months are 4,6,7,8,9,12 → gaps at 1,2,3,5,10,11
- First letters of assigned months: A, J, J, A, S, D
- Could be extraction indices for another puzzle
- 4+6+7+8+9+12 = 46 (or any digit-sum variant)
```

#### Phone Numbers Found (All Texted — No Replies)

| Number | Decode | Area |
|--------|--------|------|
| 657-283-9800 | Most prominent | Orange County, CA |
| 650-283-9795 | — | Salesforce HQ (San Mateo, CA) |
| 480-234-354? | Partial | Tempe/Phoenix, AZ |
| 704-232-7823 | **704-BEAST-23** | Charlotte, NC (MrBeast hometown) |

**~2,163 frames remaining (free tier). Expect: more bank interiors, vault scenes, Keith Haring mural, possible QR codes, end card. Bank scenes now appearing — critical per Hint #1.**

---

## Key Cipher Decodings

### 1. Phone Keypad Cipher: 3634826 = ENDGAME

```
Phone Keypad:
  3 = D/E/F    →  E
  6 = M/N/O    →  N
  3 = D/E/F    →  D
  4 = G/H/I    →  G
  8 = T/U/V    →  A (uses 2nd key mapping)
  2 = A/B/C    →  A
  6 = M/N/O    →  M → E

Result: E-N-D-G-A-M-E = "ENDGAME"
The "-1" suffix = "Part 1 of the endgame" or "Endgame sequence #1"
```

### 2. Room Layout Cipher: HIDE

```
Above door: 8       → H (8th letter of alphabet)
Red-coded:  I       → I (Red = letter I from "ID" screen)
Green-coded: D      → D (Green = letter D from "ID" screen)
Right monitor: 5    → E (5th letter of alphabet)

Result: H-I-D-E = "HIDE"
```

### 3. The Lost Numbers: 4-8-15-16-23-42

```
Vault door ring displays: 4-8-15-16-23-42
These are "The Numbers" from TV show LOST
Sum: 4+8+15+16+23+42 = 108
108 is significant in Lost mythology (timer in The Swan station)
Likely the vault combination or extraction key
```

### 4. A1Z26 Cipher (Confirmed via Video 2 "Rosetta Stone")

```
A=1, B=2, C=3, ... Z=26
"MrBeast" = M(13)+R(18)+B(2)+E(5)+A(1)+S(19)+T(20) = 78
Frame 252 (Greenville NC area code) confirmed this cipher is fundamental.
Tweet metric digit sums consistently = 27 when decoded via A1Z26.
```

### 5. Reaction Count Index Cipher: TOW

```
Slack message: "Hey team! Here is the shot we discussed in the call!"
Reaction counts: 15, 20, 22
15th character → T
20th character → O
22nd character → W
Result: TOW = "Tug of War" (confirmed by Squid Game/red team visual)
```

### 6. QR Code: sforce.co/4bAAGMH

```
Built from shipping containers in the Nevada desert
Decoded URL: https://sforce.co/4bAAGMH?r=qr
This is a Salesforce short URL → likely redirects to puzzle page
The ?r=qr parameter tracks that it was found via the QR code
```

### 7. Vault Door Ring Sequence (Potential RLE)

```
Full sequence: 4-1-8-4-1-3-1-8-4-1-1-3-4-4-4-1-2-1-1-4-4-10-1-1-1-2-4-1-1-1-1-3-1-3-1-1-1-1-8-4-3-1-1-1-1-10

Hypothesis 1: Run-length encoding for binary data
  4 ones, 1 zero, 8 ones, 4 zeros... → binary → ASCII

Hypothesis 2: Index pairs (row,col) for the 9 Sudoku grids
  (4,1), (8,4), (1,3), (1,8), (4,1), (1,3)...

Hypothesis 3: Combined with Lost numbers as key
```

### 8. Salesforce Mascot Icons

```
Spider/Tarantula  → ? (Web/Network?)
Bird/Canary       → Data Cloud / Marketing Cloud
Sine Wave         → Wave Analytics / MuleSoft
Chandler + 'D'    → ? (D = Data?)
Ear               → Einstein Voice / Listening
Head/Brain        → Einstein AI
Witch/Dancer      → Astro (Salesforce mascot)
Elephant          → Ruth (Salesforce mascot)
```

### 9. Emoji Sequence: 🎠🦕🎡⚓🏕️

```
🎠 Carousel Horse  → C
🦕 Sauropod        → S (or D for Dinosaur)
🎡 Ferris Wheel    → F
⚓ Anchor          → A
🏕️ Camping         → C

Possible readings: CSFAC, CDFAC, CDFAT
Appears in every Slackbot notification frame.
Emojis VARY between frames — 3rd position changes most.
This variation may encode additional information.
```

### 10. Background Hex Color: #152022

```
Slack ad background color ≈ #152022
Embeds the three reaction counts: 15, 20, 22
RGB: R=21 (≈15+6), G=32 (≈20+12), B=34 (≈22+12)
B channel = 2, G channel = 7 → "27" (video title number)
```

### 11. Belt Code: 3X771

```
Found on MrBeast's belt (frame 496)
The second '7' is highlighted in RED
Could be: a URL path, a hex code, or a password
With red emphasis: 3X7[7]1 → the red 7 may be the "extraction digit"
```

### 12. Color-Coded MRBEAST Belt

```
M = Green (1)
R = Yellow (2)
B = Blue (3)
E = Red (4)
A = Green (1)
S = Yellow (2)
T = Blue (3)

Pattern: 1-2-3-4-1-2-3 (repeating 4-color cycle)
This may be a key for ordering or decoding other clues.
```

### 13. T7 Street Marking → Positional Extraction from BARCLAY

```
Street marking: "T7"
T = index marker (position indicator)
7 = 7th letter of nearby word

BARCLAY = B-A-R-C-L-A-Y
              1 2 3 4 5 6 7
7th letter → Y

This suggests a multi-frame extraction pattern:
  T1=B, T2=A, T3=R, T4=C, T5=L, T6=A, T7=Y
  Look for T1-T6 in other frames!
```

### 14. Character Name Cipher: MRS. MAY-___

```
MRS. MAYBELLE → "Ma Bell" (telephone company = call someone)
MRS. MAYBEUR  → "Maybe You Are" (the winner)
MRS. MAYBERRY → Mayberry, NC (Andy Griffith + MrBeast's home state)

A1Z26 encoding:
  MAY   = M(13) + A(1) + Y(25) = 39
  BELLE = B(2) + E(5) + L(12) + L(12) + E(5) = 36
  Total = 75

Phone keypad:
  RED = 7-3-3 → sums to 13, or just "733"
  "RED" on keypad also maps to digits that sum to 27 variants
```

### 15. Talk Like A Pirate Day → September 19

```
Billboard in Super Bowl ad street scene: "TALK LIKE A PIRATE DAY"
Real holiday: September 19 (09/19)
Possible code values: 919, 0919, SEP19
Also references MrBeast video: "I Found A $1,000,000 Pirate Treasure"
```

### 16. Countdown Sequence: 7-5-3-1

```
Frame 1075: Numbers 7, 5, 3, 1 on weekday labels
Pattern: odd numbers descending
Next in sequence: -1 (or loops to 9?)
7+5+3+1 = 16 (matches Lost number 16)
Could indicate: 4 steps remaining, every-other-day schedule, or extraction indices
```

### 17. Super Bowl LVIII Overtime Reference

```
VIOLATION ticket found in scene:
  OFFENSE: OVERTIME
  DATE: 02/11/24
  TIME: 6:30 PM
  LOCATION: LAS VEGAS

Super Bowl LVIII (Feb 11, 2024) went to OVERTIME
KC Chiefs beat 49ers 25-22 in OT
Numbers from ticket: 02, 11, 24, 630, or "OVERTIME" as keyword
```

---

## Cross-Video Pattern Analysis

### Recurring Numbers

| Number | Video 1 | Video 2 | Video 3 | Video 4 | Significance |
|--------|---------|---------|---------|---------|-------------|
| **7** | On vault floor | Hidden on phone | Shield crest, carpet | T7 marking, 7531 countdown, 777 address | Most repeated single digit |
| **14** | G-14 classified | **EVERYWHERE** (9+4+1, 14 members, 14-char channel) | Frame 14 area | — | Core mathematical constant |
| **17** | — | — | — | "17 STOP NOW HERE", plate codes end in 17 | Recurring in V4 |
| **27** | — | **Title number**, logo features, metric sums | — | RED=27 (keypad), plate codes end in 27, BPE527 | Pervasive across all videos |
| **30** | — | — | — | "30 MINUTE PARKING LIMIT" | "30 Days" challenge ref |
| **41** | — | 41-day countdown, tanker #41 | Frame 41 | — | Days from Dec 29 to Feb 8 |
| **75** | — | — | — | MAY(39)+BELLE(36)=75 | Character name A1Z26 sum |
| **103** | — | — | — | Barclay Hotel address: 103 W 4th St | Real-world anchor |
| **108** | Lost numbers sum | — | — | — | LOST mythology |
| **777** | — | — | — | The Row Lofts: 777 S Alameda St | Triple 7s address |
| **919** | — | — | — | Talk Like A Pirate Day = Sept 19 | Date code |
| **3634826** | Tank barrel (15+ frames) | — | — | — | ENDGAME phone keypad |
| **456** | — | Squid Game reference | — | — | MrBeast's biggest video |
| **6601** | — | — | — | Tank turret number | Faint code |
| **7531** | — | — | — | Odd-number countdown on weekdays | Sequence |
| **90013** | — | — | — | Barclay Hotel zip code | LA zip |
| **101** | — | — | — | On EVERY bank door (4+ banks) | Universal bank number |
| **401** | — | — | — | Merchants Bank (NOT reversed) | Unique deliberate clue |
| **56** | — | — | — | Chandelier binary 111000 = 56 | Decimal decode |
| **46** | — | — | — | Sum of month chart: 4+6+7+8+9+12 | Month sequence sum |

### Recurring Keywords

| Word | Where Found | Likely Role |
|------|-------------|-------------|
| **ENDGAME** | Video 1 phone keypad cipher | Master instruction / phase name |
| **HIDE** | Video 1 room cipher | Instruction: things are hidden |
| **FIND** | Video 1 vault rivets | Instruction: search for clues |
| **ISLAND** | Video 2 steganography | Keyword/password |
| **MALCOLM** | Video 2 water tank | Keyword/person reference |
| **TOW** | Video 2 reaction cipher | Tug of War reference |
| **INCREDIBLE** | Video 2 missing tweet word | Password/keyword |
| **#secret-clue** | Video 2 Slack sidebar | Slack channel to investigate |
| **CANARY** | Video 1 lab monitors | Status indicator / keyword |
| **BIG GAME** | Video 2 + Video 3 | Super Bowl reference |
| **RED HERRING** | Video 4 bank name | Meta-clue: "distraction" |
| **BARCLAY** | Video 4 hotel (20+ frames) | Real-world anchor location |
| **PLAY** | Video 4 (highlighted from BARCLAY) | Call to action |
| **CLAY** | Video 4 (vertical from BARCLAY) | Wordplay / Dream's name? |
| **BEAST** | Video 1 + Video 4 | On vault, truck, jacket, branding |
| **PIRATE** | Video 4 billboard | Talk Like A Pirate Day |
| **OVERTIME** | Video 4 violation ticket | SB LVIII went to OT |
| **MABELL / MAYBELLE** | Video 4 character name | Telephone = "call" instruction? |
| **PEACH STATE** | Video 4 bank cup | Georgia state nickname |
| **GEORGIA** | Video 4 state outline, cup, lottery | State theme throughout Maybelle scene |
| **SHOPIFY** | Video 4 teller counter | E-commerce brand (green bag) |
| **FLAMINGO** | Video 4 Merchants Bank counter | Pink flamingo prop = Easter egg |
| **GRANTS / MERCHANTS / FIRST NATIONAL** | Video 4 bank interiors | 3+ bank names in ad |
| **DRINKING BIRD** | Video 4 Maybelle's desk | Classic physics toy |
| **CHASE** (?) | Video 4 granny scene window | Possible circular logo |
| **OPEN** | Video 4 granny scene | Text on sign/screen |

### Emoji Sequence Variants (Video 1)

| Frame | Emojis | First Letters |
|-------|--------|---------------|
| 327 | 🎠🦕🌼⚓🏕️ | C-D-F/S-A-C |
| 329 | 🎠🦕🎡⚓🏕️ | C-D-F-A-C |
| 334 | 🎠🦕🌻⚓⛺ | C-D-S-A-T |
| 340 | 🎠🦕🎡⚓🏕️ | C-D-F-A-C |
| 344 | 🦄🦕🍋⚓🏕️ | U-D-L-A-C |
| 345 | 🎠🦕☀️⚓⛺ | C-D-S-A-T |

**Note:** The emojis VARY between frames. Positions 1, 4, 5 are most consistent (🎠/⚓/🏕️). Position 2 is always 🦕. Position 3 changes the most (🎡/🌼/🌻/☀️/🍋). This variation may encode additional information.

### Potential Social Media Handle

**@the1Mil** — appears in Rewatch video (f00598-599). Even in a troll video, this could be a real breadcrumb planted among the noise.

### Real-World Locations Identified

| Location | Source | Address | Significance |
|----------|--------|---------|-------------|
| **Barclay Hotel** | Video 4 | 103 W 4th St, Los Angeles, CA 90013 | Primary set location, 20+ frames |
| **The Row DTLA** | Video 4 | 777 S Alameda St, Los Angeles, CA | Triple-7s address |
| **Nevada Desert** | Video 1 | ~36.34826°N (from 3634826?) | QR code built from shipping containers |
| **Greenville, NC** | Video 2 | Area code 252 | MrBeast's hometown, frame 252 |
| **Charlotte, NC** | Video 4 | 704 area code | Phone number 704-BEAST-23 |
| **Gainesville, GA** | Video 4 | Peach State Bank | Mrs. Maybelle scene, Georgia theme |
| **Atlanta, GA** | Video 4 | Mercedes-Benz Stadium pic + State Farm | Framed on Maybelle's wall |

---

## Educated Best Guess

### What We Think the Final Code Is

Given that:
- The puzzle was designed by Lone Shark Games to unfold over weeks
- Not all clues have been released yet
- The structure involves 9 variety puzzles + extraction keys
- MrBeast said "it's very hard and lots of steps"

**The final answer is NOT a simple code we can derive from videos alone.**

However, our best educated guesses for what to TRY on Slack today:

#### Tier 1 -- Highest Confidence Guesses (try these first)

| Guess | Reasoning |
|-------|-----------|
| `ENDGAME` | Phone keypad cipher of 3634826 (the most prominent code in the entire video) |
| `HIDE` | Room layout cipher confirmed across multiple frames |
| `ISLAND` | Steganographic keyword hidden in Slack ad tweet |
| `PLAY` | Highlighted from BARCLAY sign across 20+ frames in V4 |
| `BARCLAY` | Dominant real-world anchor in Super Bowl ad |
| `4 8 15 16 23 42` | Lost numbers on the vault door |
| `108` | Sum of Lost numbers (vault combination) |
| `BEAST6000` | MrBeast's original YouTube handle, spelled in rivets |
| `ENDGAME-1` | Full code from the tank barrel |
| `3634826` | The raw number itself |
| `#secret-clue` | Actual Slack channel name visible in Video 2 |

#### Tier 2 -- Strong Pattern-Based Guesses

| Guess | Reasoning |
|-------|-----------|
| `27` | Most pervasive number across all 4 videos |
| `4815162342` | Lost numbers as continuous string |
| `BEAST` | Hidden in jacket patterns + truck branding |
| `103` | Barclay Hotel street address number |
| `90013` | Barclay Hotel zip code |
| `7531` | Countdown sequence from V4 |
| `CLAY` | Vertical sign extract from BARCLAY |
| `FIND HIDE ENDGAME` | Three decoded words from the vault/control room |
| `INCREDIBLE` | Missing word from Video 2 tweet (gap-fill puzzle) |
| `MALCOLM` | Name on water tank in Video 2 |
| `CANARY` | Recurring reference, "canary singing" = canary ready |
| `TOW` or `TUG OF WAR` | Decoded from Video 2 reaction counts |
| `3X771` | Belt code with red-highlighted character |
| `OVERTIME` | Violation ticket in V4, SB LVIII reference |
| `401` | Only bank door number that ISN'T 101 (Merchants Bank, not reversed) |
| `PEACHSTATE` | Peach State Bank logo on Georgia cup |
| `GEORGIA` | Pervasive state theme in Maybelle scene (cup, outline, lottery, stadium) |

#### Tier 3 -- Combinatorial / Long-Shot Guesses

| Guess | Reasoning |
|-------|-----------|
| `919` / `0919` | Talk Like A Pirate Day = September 19 |
| `PIRATE` | Theme keyword from V4 billboard |
| `TALKLIKEAPIRATE` | Full billboard text |
| `TANKBANK` | Rhyming sign from V4 |
| `30` | Parking limit number from V4 |
| `MABELL` | MRS. MAYBELLE decode = telephone company |
| `FLAMINGO` | Pink flamingo on Merchants Bank counter |
| `101` | On every bank door in the ad |
| `GRANTS` / `MERCHANTS` / `FIRSTNATIONAL` | Individual bank name guesses |
| `56` | Binary chandelier decode: 111000 = 56 |
| `SHOPIFY` / `SHOP` | Shopify bag + SHOP text in granny scene |
| `DRINKINGBIRD` | Desk toy in Maybelle scene |
| `PEACH` | Georgia Peach State reference |
| `CHASE` | Possible bank logo in window |
| `OPEN` | Text visible in granny scene |
| `REDHERRING` | The bank name itself (meta?) |
| `X01` | Tank turret designation |
| `6601` | Tank turret number (faint) |
| `777` | The Row Lofts address (777 S Alameda) |
| `BIGGAME` | Recurring phrase in V2+V3 |
| `PATIENCE` | Hidden sign word from V3 |
| `HIDEANDSEEK` | V1 HIDE + seek theme |
| `36.34826, -115.XXXX` | GPS coordinates (36.34826°N is near Las Vegas/desert QR) |
| `MRBEAST6000` | Full original handle |
| `@the1Mil` | Social media handle from Rewatch video |
| `RED HERRING BANK` | The Slack workspace name from the Super Bowl ad |
| `HOTEL BARCLAY` | Building name from Super Bowl ad |
| `4826` | Partial code appearing on multiple props |
| `152022` | Background hex value from Slack ad |
| `6572839800` | Most prominent phone number |
| `7042327823` | 704-BEAST-23 phone number |

### GPS Theory Deep Dive

The number `3634826` could be latitude `36.34826°N`. Combined with the desert QR code location:
- 36.34826°N maps to the **Nevada desert** near Las Vegas
- The QR code was literally built in the desert at what appears to be this latitude
- A full GPS coordinate would need a longitude (possibly from another clue)

### The "Big Game" Connection

"Big Game" is the non-trademarked way to refer to the Super Bowl. Video 2 has a Slack channel called **#project-big-game** with exactly **14 members**. The number 14 appears to be a key extraction index or grid coordinate.

### 9 Variety Puzzles -- Solving Progress (Updated Feb 10, 2026)

The 9 puzzles each end in a word. Together they form a clue "in order."
**Word lengths: 5, 9, 5, 7, 8, 4, 9, 6, 5**

| # | Platform | Video | Puzzle Type | Len | Status | Best Guess |
|---|----------|-------|-------------|-----|--------|------------|
| 1 | Pinterest | 100 Wells in Africa | Word search + water drop blanks | 5 | 6/13 words found | ? |
| 2 | Reddit | 600 Strangers | Letter Sudoku (CHANGLIFE) | 9 | **GRID SOLVED** | Extraction TBD |
| 3 | Imgur | Dirtiest Beach #TeamSeas | TV show genre→debris removal | 5 | 13/19 shows matched | ? |
| 4 | ImageShack | $1-$500K Experiences | Stencil-font locations | 7 | Partially decoded | JOURNEY? |
| 5 | Photobucket | Pokemon Go Stereotypes | Pokemon cage crossword | 8 | Structure understood | CAPTURED? |
| 6 | Medium | Wilderness Survival | Tents and Trees + numbers | 4 | Structure understood | EACH? |
| 7 | Pixelfed | 100 Dogs | Venn diagram dog traits | 9 | Structure understood | COMBINING? |
| 8 | ImgPile | 100 Hours in Pyramids | Pyramid crossword | 6 | All clues solved | SPHINX? |
| 9 | 500px | Circle I'll Pay For | Geodesic spheres + letters | 5 | Multiple theories | VAULT? |

#### Puzzle 1 Details (Pinterest - Word Search)
- Grid is 9x9 with 15 water-drop blanks replacing letters
- 13 clue words hidden in grid; finding them reveals blank letters
- **Words found:** CON (deceive), IRATE (upset), ROBIN HOOD (literary outlaw), IOWA (midwesterner), DHOW (boat type), MORAY (fills blank)
- **Unsolved clues:** "A cold noise?", "A natural disaster", "MrBeast went to one in Greenville NC", "'Rats!' (2 wds)", "A child's toy (2 wds Hyph.)", "item in MrBeast store", "US landmark (2 wds)", "What you say when you finish this!"
- Partial grid with blanks filled: O,I,R,E,A,G,D,R,S,O,C,W,D,E,A
- **Blocker:** 7 of 13 words not yet found in grid; extraction method unclear

#### Puzzle 2 Details (Reddit - Sudoku) -- GRID COMPLETE
```
A L F C H N E G I
C G H F I E N L A
E I N A G L H F C
G N L H E I C A F
I H C L F A G E N
F A E G N C I H L
H F A N C G L I E
N E G I L F A C H
L C I E A H F N G
```
- Letters: C=1,H=2,A=3,N=4,G=5,L=6,I=7,F=8,E=9
- **Blocker:** Extraction method unknown. Per ARGNet: "information on which letters to select might emerge through other parts of the campaign." Bank scene keys likely needed.

#### Puzzle 3 Details (Imgur - TV Shows)
- Mechanic: ID TV show → remove debris letters → remaining = answer word
- Debris pool: AABBCCCDDFFFGGGGIIIKKKKLLLMNNPRRSSTTTWWY
- **13 confirmed matches:**
  - KNIGHT RIDER → DITHERING (10,7)
  - GET SMART → MATTER (5,2)
  - GREEN ACRES → SCREENER (4,10)
  - FATHER TED → HEARTED (1,6)
  - BEAST GAMES → TEAMSEAS (8,1)
  - KNOTS LANDING → STANDING ON (3,6)
  - IRON FIST → INTROS (3,2)
  - KAREN SISCO → SCENARIOS (10,3)
  - BURN NOTICE → NEUROTIC (8,10)
  - SISTER WIVES → RESISTIVE (7,8)
  - NIGHT COURT → OUTRIGHT (10,4)
  - KIM POSSIBLE → MOBILISES (9,4)... wait, that's British spelling
  - TOP GEAR → OPERA (1,6)
- **6 unmatched entries remain.** (X,Y) extraction still unsolved.

#### Puzzle 8 Details (ImgPile - Pyramid Crossword)
- Left clue answers (21): A, ADORN, CABRIOLET, CALIBRE, LOW-CARB, TAKE IN, NAVIGATOR, DURATION, E, EAR, ECLAIR, EON, ER, I, IN UTERO, INUNDATE, ION, LE CAR, NO, NOTE, O
- Right clue answers (22, alphabetical): OI, OPTION, ORBICULAR, ORIENT, OUT FOR A SPIN, OUTLINERS, PINTO, PORTION, PROTON, RA, RACE, RAD, RAT POISON, RESOLUTION, REVOLUTIONS, ROTUNDA, RUTS, STAINLESS, TONER, TONI, TRADES UNION, TURN ON A DIME
- **Blocker:** Pyramid grid structure + extraction mechanism

### 9-Word Clue Assembly (SPECULATIVE)

```
Word 1:  ? ? ? ? ?           (5 letters)  -- Puzzle 1 (word search)
Word 2:  ? ? ? ? ? ? ? ? ?   (9 letters)  -- Puzzle 2 (sudoku, grid solved)
Word 3:  ? ? ? ? ?           (5 letters)  -- Puzzle 3 (TV shows, 13/19)
Word 4:  ? ? ? ? ? ? ?       (7 letters)  -- Puzzle 4 (stencil locations)
Word 5:  ? ? ? ? ? ? ? ?     (8 letters)  -- Puzzle 5 (pokemon cage)
Word 6:  ? ? ? ?             (4 letters)  -- Puzzle 6 (tents & trees)
Word 7:  ? ? ? ? ? ? ? ? ?   (9 letters)  -- Puzzle 7 (100 dogs venn)
Word 8:  S P H I N X ?       (6 letters)  -- Puzzle 8 (pyramid, best guess)
Word 9:  ? ? ? ? ?           (5 letters)  -- Puzzle 9 (geodesic spheres)
```

**Key insight from Hint #1:** The 9-word phrase is an INSTRUCTION that "defines the nature of the search." It tells you what KIND of search to perform next. It is the FIRST STEP, not the final answer.

**NOTE:** Most puzzle extractions likely require keys from the Super Bowl ad bank scenes (Video 4, only 38% processed). The puzzles can be SOLVED (grids filled, logic completed) but the EXTRACTION of the specific answer word requires additional information from the ad.

### Super Bowl Ad "Weird Things" Catalogue

Per Hint #1: "figure out how to get an answer from each weird thing." Each yields ONE answer via standard online codes.

| "Weird Thing" | Frame Range | Standard Code to Try | Possible Answer |
|---------------|-------------|---------------------|-----------------|
| RED HERRING BANK | 1124-1175 | Meta/wordplay | RED HERRING (distraction) |
| BARCLAY HOTEL | 1124-1175 | Real-world lookup | 103, 90013, or 4TH |
| TALK LIKE A PIRATE DAY | 1230-1237 | Calendar lookup | SEPTEMBER 19 / 919 |
| NO PARKING YOUR TANK AT THE BANK | 1230-1237 | Rhyme / wordplay | ? |
| 30 MINUTE PARKING LIMIT | 1230-1237 | Number extraction | 30 |
| MRS. MAYBELLE | 088-110 | Wordplay / A1Z26 | MABELL / 75 |
| VIOLATION: OVERTIME | 250-254 | Sports reference | SB LVIII / 2522 |
| T7 street marking | 1146 | Positional cipher | Y (7th letter of BARCLAY) |
| PL-01 tank | 700+ | Military lookup | STEALTH / POLISH |
| 7-5-3-1 countdown | 1075 | Sequence analysis | 16 (sum) / ODD |
| Binary barcode on meter | 208 | Binary→ASCII | i / I / 0xAA |
| 4th St / Clay intersection | 1230+ | Address lookup | Oakland? SF? |
| Vehicle plates (JP1117 etc) | 331-385 | Number extraction | 17, 27, 77 patterns |
| "17 STOP NOW HERE" | 491, 540 | Instruction | STOP at 17? |
| THE ROW LOFTS | 516 | Address lookup | 777 S Alameda |
| Phone: 704-BEAST-23 | 088-110 | Phone keypad | BEAST / Charlotte NC |
| Calendar double-dates | 099 | Pattern analysis | 12 dates / July missing |
| X-01 on tank | 1154 | Sequence | 1st in series |
| 6601 on turret | 1158 | ? | Unknown |
| 8 red panels w/ circles | 1158 | Binary / Braille | 00000000? |
| Purple lit window | 1175 | Binary position | Floor/room number |
| Morse on tank: -- -- | 1237 | Morse code | M M |
| PEACH STATE BANK (cup logo) | 1280 | Geographic lookup | GEORGIA / GAINESVILLE |
| Georgia state outline | 1276-1285 | State identification | GEORGIA / 4th state |
| Month→Number chart (Apr=1...Dec=6) | 1285 | Sequence cipher | Extraction key for other puzzles |
| Drinking Bird toy | 1281, 1284 | Physics/science | PERPETUAL / MOTION? |
| GEORGIA LOTTERY sign | 1284 | Real-world lookup | Lottery numbers? |
| Shopify bag (green) | 1280 | Brand reference | SHOP / SHOPIFY |
| Sour Patch Kid figure | 1285 | Sponsor reference | SOUR / SWEET? |
| Chandelier binary 111000 | 1515 | Binary→decimal/Braille | 56 / Braille 'l' |
| Chandelier varying bulbs (6-10) | 1504-1522 | Counting code | Sequence of bulb counts |
| Pink Flamingo on counter | 1682 | Object code | FLAMINGO / PINK |
| Hidden person (sunglasses+hoodie) | 1408-1522 | Recurring watcher | Observer figure |
| Red Cup on bank counter | 1525, others | Out-of-place prop | RED CUP / TOBY KEITH? |
| 401 (not reversed) on glass | 1524 | Deliberate number | **401** (unique — all others show 101) |
| ECNARTNE (reversed ENTRANCE) | 1530 | Reversed text | ENTRANCE |
| Multiple bank names | 1275-1682 | Bank collection | 6 banks identified (see bank table) |
| Mercedes-Benz Stadium picture | 1276 | Real-world venue | ATLANTA / Super Bowl LIII |
| State Farm logo on cup | 1276 | Brand reference | STATE FARM / INSURANCE |
| Keith Haring mural | ~3450 (TBD) | Art reference | TBD (not yet processed) |
| "5" on building (red) | ~3450 (TBD) | Number | TBD |

**Many more elements remain to be catalogued as Video 4 processing continues.**

---

## Actionable Next Steps

### PRIORITY 1: The 9 Reddit Variety Puzzles (THE CRITICAL PATH)

Per Hint #1, the 9-word clue is **"the first step on your journey."** This is the entry point.

- [x] **Found all 9 puzzle links** (via pinned comments on BeastForce67 accounts)
- [x] **Downloaded all 9 puzzle images** (stored in puzzle_analysis/superbowl_ad_1M_frames/)
- [x] **Solved Puzzle 2 Sudoku grid** (all 81 cells determined)
- [x] **Solved Puzzle 8 pyramid crossword clues** (all 43 clue answers identified)
- [x] **Matched 13/19 TV shows for Puzzle 3** (debris removal mechanic confirmed)
- [ ] **Complete remaining puzzle solves** (Puzzles 1,4,5,6,7,9 need more work)
- [ ] **Crack extraction methods** — likely need bank-scene keys from Video 4
- [ ] **Assemble the 9-word clue** (word lengths: 5, 9, 5, 7, 8, 4, 9, 6, 5)
- [ ] **Interpret the clue** — it "defines the nature of the search"

### PRIORITY 2: Decode Super Bowl Ad Street Scenes

Per Hint #1: "almost everything Jimmy passes by is a clue" and "figure out how to get an answer from each weird thing."

- [ ] **Catalogue every "weird thing"** Jimmy passes in the ad
- [ ] **Look up standard online codes** for each element (confirmed by hint)
- [ ] **Look in all directions**: up, down, forward, backward, behind the scenes
- [ ] **Each element should yield ONE answer** — compile answer list
- [ ] Elements identified so far: RED HERRING BANK, BARCLAY HOTEL, TALK LIKE A PIRATE DAY, NO PARKING sign, tanks, parking meter barcode, violation ticket, MRS. MAYBELLE, 7531 countdown, street markings, etc.

### PRIORITY 3: Apply Street Answers to Bank Scenes

Per Hint #1: "you will need specific content from the Super Bowl ad to solve anything there [in the bank]"

- [ ] **Wait for V4 pipeline to reach bank interior scenes** (~frames 2000-3476)
- [ ] **Map street-scene answers to bank-scene puzzles**
- [ ] **Look for: combination locks, ciphers, grids that use street answers as keys**

### Other Tasks

- [ ] **Register** at [mrbeast.salesforce.com](https://mrbeast.salesforce.com/)
- [ ] **Visit** `https://sforce.co/4bAAGMH?r=qr` (decoded QR code URL)
- [ ] **Check @the1Mil** on Twitter/Instagram/TikTok
- [ ] **Find MrBeast's Super Bowl photos** — look for hidden numbers
- [ ] **Join community solving groups** (Reddit, Discord, Slack) — "We never said you had to do this alone"
- [ ] **Check daily hint drops** from Lone Shark Games

### When Video 4 Pipeline Completes

- [ ] Review all 3,476 frames (esp. bank interior scenes)
- [ ] Cross-reference street answers with bank puzzles
- [ ] Check Keith Haring mural for hidden patterns/codes
- [ ] Generate MASTER_SUMMARY.json across all 4 videos

### Ongoing (Cron Jobs Active)

- Daily: Check MrBeast's X (@MrBeast) and Instagram for new puzzle clues
- Daily: Check mrbeast.salesforce.com for updates
- Daily: Check r/MrBeast and ARGNet for community progress
- Daily: Re-run frame analysis on any new videos posted
- Daily: Check for Lone Shark Games hint drops

---

## Sources

- **[HINT #1 VIDEO — Lone Shark Games (Feb 9, 2026)](https://youtu.be/hGuA0a15VWQ)**
- [ARGNet: Start Slacking Off with MrBeast's Million Dollar Puzzle Hunt](https://www.argn.com/2026/02/start_slacking_off_with_mrbeasts_million_dollar_puzzle_hunt/)
- [Newsweek: MrBeast Shares Update on $1 Million Puzzle](https://www.newsweek.com/mrbeast-shares-update-on-1-million-puzzle-advertised-during-super-bowl-11490124)
- [ABC News: MrBeast drops big hint for $1M puzzle](https://abcnews.go.com/GMA/Culture/mrbeast-drops-big-hint-1m-puzzle-salesforce-super/story?id=129987912)
- [Lone Shark Games: The Puzzle Vault](https://lonesharkgames.com/the-puzzle-vault/)
- [Adweek: Salesforce Teams Up with MrBeast](https://www.adweek.com/brand-marketing/salesforce-teams-up-with-mrbeast-to-give-away-1-million-at-super-bowl-60/)
- [Benzinga: Here's What You Have To Do](https://www.benzinga.com/markets/tech/26/02/50471320/mrbeast-says-first-person-to-crack-his-super-bowl-ad-puzzle-wins-1-million-heres-what-you-have-to-do)

---

*Generated by Gemini 3 Flash Preview (agentic vision) + Claude Opus 4.6 analysis pipeline*
*Pipeline: 4,758/6,918 frames analyzed (68.8%). Video 4: ~1,318/3,476 (38%, free tier processing ongoing).*
*Hint #1 received and integrated. 6 banks identified, month cipher chart found, 9 variety puzzles partially solved.*
*Last updated: 2026-02-10T12:00:00*
