# Campaign Rules

> **Single source of truth** for campaign-specific gameplay rules. When these rules change, only this file needs editing — all operational principles and their dependencies are documented in `../CampaignMaster.md`.

These are the campaign-specific rules for The Whisper Below. They supplement — but do not override — official Aeon's End rules.

---

## Core Principles

1. **Official rules take precedence.** Campaign rules only add narrative objectives, bonuses, rewards, and consequences.

> The following operational principles are defined in `../CampaignMaster.md` and are not duplicated here:
> - Victories and defeats both matter (Campaign Master's Campaign Philosophy)
> - The world is persistent / ignored threats worsen (Campaign Master's Campaign Philosophy)
> - Progression is light / max 2 permanent perks (Campaign Master's Prohibited Behaviour)
> - Most battles above ground (Campaign Master's Mission Setting Rule)

## Mission Structure

Every main mission includes:

1. Mission title
2. Story introduction
3. Mission objective
4. Assigned Nemesis
5. Four nominated mages (players choose three)
6. Exact market or thematic market instructions
7. Optional bonus objective
8. Any special campaign rule
9. Victory consequences
10. Defeat consequences
11. Required post-game report

## Mage Selection

- The Campaign Master nominates four mages per mission
- Players choose three from the four nominated
- The Campaign Master normally chooses the Nemesis

## Player Choices

Player agency focuses on:

- Which mission to pursue
- Which location to save
- Which reward to claim
- Which ally to trust
- Which upgrade to purchase
- Which risk to accept

## Defeat Consequences

A defeat should not end the campaign. Instead it may:

- Damage Gravehold
- Advance the enemy threat
- Remove an opportunity
- Injure or exhaust a mage narratively
- Alter a future mission
- Allow a Nemesis or lieutenant to escape
- Change the state of a location
- Create a recovery mission

## Campaign Rules That Modify Gameplay

Any campaign rule that modifies normal gameplay must be clearly stated in `../Game/CurrentMission.md`. Examples include:

- Narrative objectives
- Optional bonus objectives
- Persistent rewards
- Limited pre-game modifiers
- Rare mage perks
- Campaign-wide resources
- Branching consequences

---

*This file may be extended as the campaign evolves.*

## Mage Pool & Geographic Availability

Mages are not always available. After each mission, the Campaign Master determines which mages are in which districts and which mages can physically reach the next mission location.

### Districts

Gravehold is divided into districts. Mages in each district can reach mission locations as follows:

| District | Mission Locations Reachable |
|----------|---------------------------|
| **Upper Ward / Spire** | Anywhere (central, well-connected) |
| **East Gate** | Outer Settlements, Old Foundry, Ash-Fields |
| **Lower Markets** | Outer Settlements, Old Foundry, Warrens |
| **Warrens** | Warrens, Lower Markets, Deep Warrens |
| **Healer's Ward** | Nowhere — mages here are recovering |
| **Outer Settlements** | Ash-Fields, East Gate |

### Mage Pool Rules

1. After each mission, mages are reassigned to districts based on the narrative.
2. Mages who participated in the last mission are in the district where that mission took place.
3. Recovering mages are in the Healer's Ward and unavailable for 1-2 missions.
4. Unused mages remain in their previous district or are moved by the narrative.
5. New mages arriving at Gravehold start in the Upper Ward.
6. The Campaign Master nominates 4-6 mages per mission from those who can physically reach the location. Players choose 3.

---

## Side Missions

Side missions are narrative interludes that do not involve playing a full game of Aeon's End. They represent moments of exploration, diplomacy, investigation, resource management, or personal stakes.

### Structure

1. **Cost**: Side missions cost Council Favour (typically 1-2) to undertake, representing the political capital and resources needed.
2. **Timing**: Side missions are offered alongside main missions and can be undertaken in addition to a main mission — they don't compete for the mages' time, only the Council's resources.
3. **Resolution**: Side missions are resolved through narrative choices (from the players) rather than gameplay. The Campaign Master describes the situation; the players decide what to do; the Campaign Master narrates the outcome.
4. **Rewards**: Side missions may yield:
   - Companions (drakes, spirits, constructs)
   - Allies (NPCs who help narratively or mechanically)
   - Relic unlocks
   - Intelligence about nemeses or locations
   - Council Favour (net gain or loss)
   - Story flags that unlock future options
5. **No Aeon's End Gameplay**: Side missions never require setting up a market, nemesis, or playing a round of Aeon's End.

### Side Mission: The Ember in the Dark (Example)

The first side mission in the campaign:
- **Cost**: 1 Council Favour
- **Premise**: A dying drake found in the Warrens
- **Resolution**: Spend the favour to save it; players choose which mage it imprints on
- **Reward**: A drake companion with narrative perks (breach-energy sensing, secret passage discovery, future combat potential)

---

## Council Favour

Council Favour is the campaign's primary meta-currency. It represents the trust, goodwill, and political capital the mages have earned with Gravehold's ruling council.

### Earning Council Favour

| Source | Amount |
|--------|--------|
| Mission victory | +1 |
| Bonus objective completed | +1 |
| Major heroic deed (Campaign Master discretion) | +1 |
| Saving a district from destruction | +1 |
| Discovering critical intelligence | +1 |

### Spending Council Favour

| Cost | Option |
|------|--------|
| 1 | **Side Mission** — undertake a narrative interlude |
| 2 | **Mage Training** — a mage of your choice gains +1 XP |
| 2 | **Gravehold Repairs** — restore 10 to any one Gravehold attribute |
| 3 | **Relic Research** — unlock a relic for use in future missions |
| 3 | **Call Reinforcements** — summon a specific mage from outside the current pool |
| 4 | **District Fortification** — a chosen district gains a permanent defensive trait |

### Rules

1. Council Favour is never lost on a defeat — only the opportunity to spend it is delayed.
2. The Council remembers past deeds. Favour is a reflection of trust, not a spendable token that expires.
3. Spending favour does not reduce the Council's trust — it represents calling in favours and requisitioning resources.
4. The Campaign Master may offer new spending options as the narrative evolves.

---

## Companions

Companions are creatures or constructs that accompany the mages but do not participate directly in Aeon's End gameplay (unless a future campaign rule specifies otherwise).

### Rules

1. Companions are acquired through side missions, story events, or relic research.
2. Each companion is bonded to one mage (chosen by the players when the companion is acquired).
3. Companions provide narrative perks:
   - **Breach-energy sensing**: The companion can detect disturbances, hidden nemeses, or secret passages
   - **Scouting**: The companion can explore ahead, revealing mission options or intelligence
   - **Future combat potential**: As the companion grows, it may eventually participate in battles
4. Companions appear in the bonded mage's story entries and may influence narrative choices.
5. Companions can be lost if the bonded mage dies or if a narrative event separates them.

---

## Market Restrictions

To prevent the campaign from becoming stale or dominated by a handful of overpowered cards, the following restrictions apply to the market:

### Temporary Ban (Cooldown)

After a card appears in the market and is purchased by at least one mage, it enters a **1-mission cooldown**. It cannot appear in the market for the next mission. After the cooldown, it may be included again.

The Campaign Master tracks which cards are on cooldown in each mission's market section.

### Permanent Ban

If a card proves consistently dominant across multiple missions (e.g., Scrying Bolt appearing in every mage's deck and trivialising encounters), the Campaign Master may place it on a **permanent ban** list for the remainder of the campaign. This is a last resort and should be discussed with the players before being enacted.

### Current Cooldown List

*To be populated after Mission 3 — the first mission where this rule is in effect. Cards from Mission 2 are grandfathered.*

### Current Permanent Ban List

*None.*

---

## Mage Rotation

To ensure all mages get playtime and prevent over-reliance on a few favourites:

1. **Back-to-back restriction**: A mage who participated in the previous mission may still be nominated, but the Campaign Master will prioritise mages who have not played recently when building the mage pool.
2. **Benched mage priority**: Mages who have not yet played in any mission receive priority for nomination. The campaign currently has 18 unplayed mages — they should be featured before the existing active mages are recycled.
3. **Two-mission cooldown (optional)**: If a mage has played in 2 consecutive missions, the Campaign Master may enforce a 1-mission cooldown before they can be nominated again. This is not automatic — it is a tool the Campaign Master can use to maintain variety.
4. **Exceptions**: A mage may bypass rotation rules if the narrative demands it (e.g., a mage's personal story arc requires their presence, or a mage is the only one who can reach a specific location).

### Current Play Count

| Mage | Missions Played |
|------|-----------------|
| Kadir | 1 |
| Adelheim | 1 |
| Xaxos (AE) | 1 |
| Brama | 1 |
| Jian | 1 |
| Lash | 1 |
| *All others* | 0 |
