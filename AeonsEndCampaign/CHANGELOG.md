# Changelog

All notable changes to the Aeon's End campaign repository.

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
