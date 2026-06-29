# PROJECT STATUS — AI Kids Studio

_Living document. **Not canon.** Update freely; do not freeze._
_Last updated: 2026-06-29_

> First file any agent should read after README.md.
> Tells you where the studio is **right now** and what the next move is.

---

## Current Production Stage

- **Current Episode:** EP-001 (Pilot)
- **Current Focus:** Resolve EP-001 story/storyboard conflict (see Blocker)
- **Next Milestone:** Re-review storyboard → Animatic v1 → Children Test #001

---

## Current Quality Gate

```
Gate:    Creative Review (Storyboard EP-001)
Status:  BLOCKED
Owner:   Creative Director
```

Production cannot move this gate. Only the Creative Director can open it.
It is currently blocked for two independent reasons (see Blocker + Review notes).

---

## 🔴 Active Blocker — EP-001 story/storyboard mismatch

The approved, **frozen** canon story for EP-001 is:

- `STORY/STORY-001_Where_Did_The_Ball_Hide.md` — **«Куда спрятался мячик?»**
  (Max loses his ball; Eva arrives; the "В домик" tidying game; ball found; they run out. ~4–5 min.)
  Status in file: **APPROVED v1.0 / frozen until OBS evidence.**

But the storyboard in production is:

- `episodes/EP-001/storyboard/STORY-LEAF-storyboard-v1.svg` — **«Большой лист»**
  (Max and Eva shelter from rain under one big leaf. 9 panels, ~62s.)

These are **two different stories.** The storyboard does not adapt STORY-001.

**This is a Creative Director decision and must not be resolved by Production:**

- **Option A —** Storyboard is wrong → rebuild a storyboard that adapts the
  frozen STORY-001 (the ball). Leaf storyboard is shelved/archived.
- **Option B —** The pilot story changed to «Большой лист» → this requires a
  **DEC** + Creative Review to unfreeze/replace STORY-001. Canon and README
  must then be updated to match. (Production will not touch frozen canon
  without this.)

Until A or B is decided, EP-001 cannot advance to Animatic.

---

## Storyboard Creative Review notes (separate from canon conflict)

Even setting the canon mismatch aside, the «Большой лист» storyboard review
returned **REQUIRES STORYBOARD REVISION** (Production Director assessment):

1. Eva continuity (panels 3–6): Eva is present in 1/3/4, absent in 5, then
   "runs in" at 6 — she appears to teleport. Staging must be made consistent.
2. Panel 8 (emotional peak, "переглянулись") is shot too wide; the smiles do
   not read for ages 2–4. Needs a close-up.
3. Panels 1–2 are front-loaded; first raindrop should arrive ~0:10–0:12, not 0:16.

(These are moot under Option A, which replaces the storyboard entirely.)

---

## Progress

```
Foundation / Canon (frozen)
✅ AKS-000  Project Philosophy
✅ AKS-001  Child Psychology / Knowledge Base
✅ AKS-002  World Bible: Luma
✅ AKS-003  Character Bible (Max, Eva)
✅ AKS-004  Visual Language
✅ DEC-000  Architecture Freeze
✅ STORY-001 Reference Story / Pilot — «Куда спрятался мячик?» (frozen)

EP-001 Production
🟡 Storyboard       — exists, but OFF-CANON + REQUIRES REVISION (blocked)
⬜ Animatic         — blocked by storyboard gate
⬜ Children Test    — not started
⬜ OBS              — not started
⬜ Final            — not started
```

---

## Pipeline position

```
Story ✅ → Storyboard 🔴(blocked) → [Creative Review] → Animatic → Children Test → OBS → Production
```

---

## Housekeeping notes (non-blocking)

- `README.md` is **stale**: it lists the next step as `ART-001.001 — Eye Research`
  and says storyboard comes later, but a storyboard already exists. README needs
  updating once the EP-001 story conflict is resolved.
- `tmp_test_commit.md` at repo root appears to be a leftover test artifact and
  can likely be removed (awaiting confirmation — Production will not delete
  unprompted).

---

## Roles (by function, not by tool)

- **Creator & Producer / Studio Founder** — direction, final authority.
- **Creative Director** — owns Quality Gates; only role that marks a gate Passed.
- **Production Director** — produces artifacts, moves the pipeline, sets gates to
  Waiting/Blocked, commits work. Never marks a gate Passed; never edits frozen canon.
- **Children Test / OBS** — validates the experience; the only thing that can
  justify reopening frozen canon.
