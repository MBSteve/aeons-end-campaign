# Changelog

All notable changes to the Aeon's End campaign repository.

---

## [CampaignJournal → Story.md + Chapters/] — 2026-07-13

### Changed
- **`CampaignJournal.md`** split into **`Story.md`** (chapter summaries) + **`Chapters/`** (full narrative)
- Prologue content moved to `Chapters/Prologue.md` (4 sections)
- Chapter 1 content moved to `Chapters/Chapter 01 - The Whisper Below.md` (summary + 4 sections)
- `Story.md` created with 1-paragraph summaries per chapter
- `CampaignJournal.md` deleted

### Updated References
- `.github/copilot-instructions.md` — points to Story.md + Chapters/
- `_CM_Rules/CampaignMaster.md` — all references updated
- `Game/CurrentMission.md` — story link updated
- `Game/viewer.html` — sidebar now lists Story.md + chapter files
- `README.md` — quick-start and file table updated
- `AeonsEndCampaignBootstrap.md` — structure diagram and references updated

---

## [Initialization] — 2026-07-10

### Created
- Repository structure initialized from `AeonsEndCampaignBootstrap.md`
- All directories created: `World/`, `Heroes/`, `Rules/`, `Sessions/`, `ImagePrompts/`, `Maps/`, `Images/`
- `README.md` — project overview and usage instructions
- `CampaignMaster.md` — complete operating instructions for the Campaign Master
- `CampaignState.yaml` — initial campaign state (The Whisper Below, Chapter 1, status: initialized)
- `CampaignJournal.md` — prologue and opening narrative for The Whisper Below
- `CurrentMission.md` — placeholder awaiting content verification
- `CHANGELOG.md` — this file
- `World/Gravehold.md` — Gravehold lore and state reference
- `World/Locations.md` — locations index
- `World/NPCs.md` — NPC index
- `World/Relics.md` — relics index
- `World/Allies.md` — allies index
- `World/Nemeses.md` — Nemesis dossier
- `Heroes/Roster.md` — mage roster (empty, awaiting content verification)
- `Heroes/RetiredHeroes.md` — retired heroes archive
- `Rules/CampaignRules.md` — campaign-specific rules
- `Rules/ProgressionRules.md` — mage and team progression rules
- `Rules/DifficultyRules.md` — difficulty management rules
- `Rules/ContentOwnership.md` — verified owned content
- `Sessions/SessionTemplate.md` — reusable post-game report template
- `ImagePrompts/ImagePromptTemplate.md` — reusable image prompt template
- `Maps/README.md` — maps directory reference
- `Images/README.md` — images directory reference

### Pending
- Verification of the four small expansion names
- OR complete list of available mages, Nemeses, and market cards
- Generation of first playable mission (Chapter 1, Mission 1)

## [Content Verification] — 2026-07-10

### Verified
- Four small expansions confirmed: **The Depths**, **The Nameless**, **Outer Dark**, **The Void**
- `CampaignState.yaml` updated with verified expansion names
- `Rules/ContentOwnership.md` updated to reflect fully verified collection

### Pending
- Generation of first playable mission (Chapter 1, Mission 1)

## [Content Listing] — 2026-07-10

### Added
- Full mage roster (20 mages) added to `Heroes/Roster.md` and `CampaignState.yaml`
  - 16 verified (Base Game + War Eternal), 4 needing verification (small expansions)
- Full nemesis roster (12 nemeses) added to `World/Nemeses.md` and `CampaignState.yaml`
  - 8 verified (Base Game + War Eternal), 4 needing verification (small expansions)
- `Rules/ContentOwnership.md` updated with complete mage and nemesis tables

### Awaiting Player Verification
- Small expansion mages: Nym (The Depths), Reeve (The Nameless), Mazra (Outer Dark), Soskel (The Void)
- Small expansion nemeses: The Wailing (The Depths), The Nameless (The Nameless), Thrice-Dead Prophet (Outer Dark), unknown nemesis (The Void)
- Market cards from all products still need to be listed

## [Content Verification — Player Corrected] — 2026-07-10

### Corrected by Player
- **War Eternal mages**: Malastar → Mazahaedron, added Mist (WE) & Ulgimor, removed Razra
- **Small expansion mages**: Malastar is from The Nameless; Z'hana is from The Depths; Reeve is from The Depths; Outer Dark has Indira & Remnant; The Void has Sparrow & Xaxos (V)
- **Duplicate mages noted**: Mist (AE + WE) and Xaxos (AE + Void) are distinct playable versions
- **Nemeses corrected**: Horde-Crone (The Depths), Blight Lord & Wayward One (The Nameless), Wraithmonger (Outer Dark), Knight Of Shackles & Maiden Of Thorns (The Void), Umbra Titan (War Eternal)

### Updated
- All files synced: `ContentOwnership.md`, `Heroes/Roster.md`, `World/Nemeses.md`, `CampaignState.yaml`, `CurrentMission.md`
- Final count: **24 mages, 15 nemeses** — all verified
- Campaign ready for first mission generation

## [Mission 1 Generated] — 2026-07-10

### Mission 1: What the Dark Attracts
- **Nemesis**: Rageborne (Base Game, Tier 1)
- **Location**: East Gate / Ash-Fields (above ground)
- **Nominated mages**: Adelheim, Brama, Kadir, Xaxos (AE)
- **Bonus objective**: Hold the Gate (no mage exhausted at victory)
- **Market**: Standard 9-card Base Game market (4 gems, 2 relics, 3 spells)
- **Setting**: Rageborne drawn to Gravehold by the psychic disturbance below; mages intercept at the outer wall

### Updated
- `CurrentMission.md` — full mission brief
- `CampaignState.yaml` — mission added to active, story threads updated
- `CampaignJournal.md` — narrative setup for Mission 1
- `Rules/CampaignRules.md` — added Core Principle #5 (most battles above ground)
- `CampaignMaster.md` — added Mission Setting Rule

### Pending
- Players to choose 3 of 4 nominated mages and play Mission 1
- Post-game report to be submitted

## [Wiki Correction] — 2026-07-10

### Fixed
- **Rageborne tier**: 1 → 2 (wiki corrected)
- **All nemesis tiers** updated from wiki data (15 nemeses, all verified)
- **Rageborne journal entry**: removed fictional "husks" — Rageborne has no minions, it's pure direct damage
- **Kadir pronouns**: corrected to she/her in CampaignJournal.md
- **ContentOwnership.md**: nemesis tables now show Tier instead of Verified column

### Wiki Data Saved
- Full mage list (52 entries) and nemesis list (47 entries) extracted from fandom wiki
- Campaign Master memory updated with correct tiers, Rageborne mechanics, and owned content

## [Image Prompts — Mission 1 Mages & Nemesis] — 2026-07-10

### Created
- `ImagePrompts/Adelheim.md` — veteran economy mage, amethyst crystal, composed and weathered
- `ImagePrompts/Brama.md` — healer mage, golden light, warm and weary but unbroken
- `ImagePrompts/Kadir.md` — flex mage, emerald crystal, watchful and guarded
- `ImagePrompts/Xaxos_AE.md` — spell-focused mage, contained fire, intense and restless
- `ImagePrompts/Rageborne.md` — Tier 2 nemesis, pure destruction, advancing across ash-fields at dawn

### Pending
- All 5 prompts ready for image generation via `scripts/generate_images.py`

## [Session Learnings] — 2026-07-10

### Added to CampaignMaster.md
- **Wiki Reference section** — URLs for mage and nemesis tables, rules for wiki use
- Future Campaign Masters will know to verify mechanics on wiki before inventing

### Key Lessons
1. Never invent nemesis mechanics (Rageborne has no minions — verified on wiki)
2. Always check mage gender (Kadir is female — corrected)
3. All 15 nemesis tiers were initially wrong — wiki is source of truth for tiers
4. Duplicate mages (Mist AE+WE, Xaxos AE+Void) must be labelled with source
5. Player corrections to ContentOwnership.md are authoritative — sync all files immediately
6. Image prompts: 3:4 portrait for mages, 16:9 for nemeses; ground in wiki facts
7. Fandom wiki is ad-heavy but browser + Playwright table extraction works; API and raw pages blocked

## [Story Consolidation] — 2026-07-12

### Changed
- **`CampaignJournal.md`** is now the single canonical story file. All narrative prose lives here.
- **`CurrentMission.md`** is now mechanics-only — objectives, setup, market, consequences. Points to journal with `> **Story**: See CampaignJournal.md → ...`
- Story prose removed from `CurrentMission.md` and consolidated into `CampaignJournal.md`
- **`CampaignMaster.md`** updated with new "Story vs Mechanics: File Separation" section
- **`README.md`** updated to reflect the new pattern and file authority order

### Rule
- When generating a new mission: write full narrative in CampaignJournal.md, write only mechanics in CurrentMission.md
- Never duplicate story prose between the two files

## [Mission 1 Completed — Victory] — 2026-07-12

### Session S01: What the Dark Attracts
- **Outcome**: Victory
- **Mages**: Kadir, Adelheim, Xaxos (AE). Brama was nominated but diverted to a medical crisis in the Lower Markets.
- **Gravehold remaining**: 10 life
- **Kadir exhausted**: Yes — dealt the killing blow while exhausted. Earned title "The Unbroken" and +1 bonus XP.
- **Xaxos highlight**: 16 damage in a single turn
- **Bonus objective**: Failed (Kadir exhausted)
- **Rageborne**: Defeated. Killed by Kadir.

### Updated
- `CampaignState.yaml` — Mission 1 moved to completed, XP awarded, Council Favour +1, Rageborne moved to defeated, story threads updated
- `Heroes/Roster.md` — Adelheim, Kadir, Xaxos (AE) activated with full records. Kadir titled "The Unbroken".
- `World/Nemeses.md` — Rageborne entry added to Defeated Nemeses
- `CampaignJournal.md` — Full battle narrative, aftermath, Council debrief, and Mission 2 branching choice
- `CurrentMission.md` — Mission 2: Choose Your Path (two branching options)
- Session file renamed to `S01 - What the Dark Attracts.md`

### Player Feedback Incorporated
- Post-mission epilogue/debrief written in CampaignJournal.md
- Mission 2 offers a branching choice with timeframes and consequences
- Brama's absence explained narratively (medical crisis in Lower Markets)
- Spell usage woven into battle narrative (Xaxos's 16-damage barrage, Kadir's recycling, Adelheim's interrupted Amplify Vision)

### Mission 2: Choose Your Path
- **Option A**: The Vanished Swarm — Carapace Queen (Tier 3) at Outer Settlements. Defensive/protective tone.
- **Option B**: The Whisper's Echo — Umbra Titan (Tier 3) at Old Foundry. Investigative/ominous tone.
- Unchosen option escalates with permanent consequences.

## [Mission 2 Expanded — Mage Pool, Side Missions, Council Favour] — 2026-07-12

### Added
- **Mage Pool & Geographic Availability** system: mages are now assigned to specific districts after each mission. Only mages who can physically reach a mission location are available. Recovering mages are in the Healer's Ward and unavailable.
  - District table added to `CampaignRules.md`: Upper Ward/Spire (central), East Gate, Lower Markets, Warrens, Healer's Ward, Outer Settlements
  - All 24 available mages assigned to districts in `CampaignState.yaml`
  - Kadir moved to Healer's Ward (recovering, 1 mission)
  - Mage pools for Mission 2 expanded from 4 to 6 mages per option (with district annotations)
- **Council Favour system** formalized:
  - Earning table: mission victory (+1), bonus objective (+1), heroic deeds, district saves, intelligence
  - Spending table: Side Mission (1), Mage Training (2), Gravehold Repairs (2), Relic Research (3), Call Reinforcements (3), District Fortification (4)
  - Rules: favour never lost on defeat; represents trust and political capital
- **Side Missions** system: narrative interludes that cost Council Favour, resolved through player choice (not Aeon's End gameplay). Rewards include companions, allies, relics, intelligence.
- **First side mission: The Ember in the Dark** — a dying drake (lesser dragon) found in the Warrens. Costs 1 Council Favour to save. Reward: drake companion with breach-energy sensing, secret passage discovery, future combat potential.
- **Companions** system: creatures/constructs bonded to one mage. Provide narrative perks. Tracked in `CampaignState.yaml` under new `companions:` section.

### Updated
- `CampaignJournal.md` — Mission 2 section rewritten as "The City Divided" with full mage pool table, Council Favour explanation, side mission narrative (The Ember in the Dark), and expanded threat options with district-annotated mage pools
- `CurrentMission.md` — renamed to "The City Divided", added side mission option, expanded mage pools from 4 to 6 per option, added side mission reporting to post-game report
- `CampaignState.yaml` — added `district` to all mages, Kadir status changed to `recovering`, added `companions:` section with drake_ember entry, added side mission tracking to active mission, added `recovery_missions_left` to Kadir
- `CampaignRules.md` — added four new sections: Mage Pool & Geographic Availability, Side Missions, Council Favour, Companions
- `CHANGELOG.md` — this entry

### Player Choice Required
- Choose Option A (Carapace Queen at Outer Settlements) or Option B (Umbra Titan at Old Foundry)
- Decide whether to spend 1 Council Favour on the side mission (The Ember in the Dark)
- If side mission taken: choose which mage the drake imprints on
