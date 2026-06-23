# AKS-002C — Additional Ideas Before AKS-003

Status: Review notes for Claude
Version: 0.1

This document captures additional ideas that appeared after closing AKS-002, before starting AKS-003 Character Bible.

## 1. Context

AKS-002 World Bible is considered ready to close. The world of Luma is defined enough for the project to move forward:

- The world is Earth.
- The main city is Luma.
- Luma is an emotional home, not a talking magical character.
- The project uses an ensemble of six children: Leo, Mia, Max, Zoe, Nico, Eva.
- Rituals and world constants replace the need for one single main hero.

## 2. Additional ideas to review

### 2.1 Relationship graph between heroes

The strongest new idea is that stories are born not only from characters, but from relationships between them.

Possible relationship types:

- best friend
- often plays with
- learns from
- inspires
- helps
- sometimes argues with
- feels shy around
- looks up to

Example:

```text
Leo
├── best friend → Mia
├── inspires → Nico
└── learns from → Zoe

Mia
├── helps → Max
└── likes drawing with → Eva
```

This should not be a technical graph database yet. It should be a simple human-readable relationship map in AKS-003.

### 2.2 Add more fields to character cards

Claude proposed a strong minimal character card. ChatGPT suggests adding a few warm, story-generating fields:

- Favorite object
- Favorite place
- Favorite game
- Dream / wish
- What the character does when sad
- What the character does when happy
- Best friend / closest friend

These fields can make AI-generated stories more consistent and emotionally alive.

### 2.3 Recurring animals of Luma

Luma should have recurring animals that make the world feel alive.

Examples:

- ducks in the park
- a squirrel in the trees
- a calm orange cat
- a friendly dog that belongs to the postman
- birds near the playground

These animals should not replace the child characters, but they can become recurring emotional anchors.

### 2.4 Officially close AKS-002

Recommendation: stop expanding AKS-002 unless a serious contradiction appears.

Further world details should move into Production-level documents:

- Locations
- Rituals
- Visual style
- Design system
- Episodes

### 2.5 Move to AKS-003

The next foundation document should be:

**AKS-003 — Character Bible**

Its goal is to define the six main children clearly enough that both humans and AI systems can write consistent stories with them.

## 3. Questions for Claude

1. Should AKS-003 include a simple relationship map between the six children from the start?
2. Which relationship types are useful for ages 2–4, and which are too complex?
3. Are the extra character card fields useful, or do they risk overcomplicating the character bible?
4. Should recurring animals be included in AKS-003, AKS-002, or a separate Production document?
5. If Pixar were creating a 2–4 educational ensemble, what would still be missing before writing the first episode?

## 4. Proposed decision

Close AKS-002 and begin AKS-003.

AKS-003 should contain:

- one card per main child;
- one main trait per child;
- one color per child;
- one area of questions per child;
- strengths and difficulties;
- simple relationship map;
- recurring phrases and rituals;
- minimal but useful emotional details.
