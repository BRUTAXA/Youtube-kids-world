# PROJECT STATUS — AI Kids Studio

_Living document. **Not canon.** Update freely; do not freeze._
_Last updated: 2026-06-29_

> First file any agent should read after README.md.
> Tells you where the studio is **right now** and what the next move is.

---

## Current Production Stage

- **Current Episode:** EP-001 (Pilot)
- **Current Focus:** Build **Animatic v1 (real frames)** — the first child-facing viewing artifact
- **Next Milestone:** Animatic v1 (real frames) → Animatic Review → Children Test #001

---

## Current Quality Gate

```text
Gate:    (none open)
Reason:  Real-frame Animatic v1 does not exist yet. The HTML below is an
         internal review tool, not a child-facing artifact, so it opens no gate.
Next:    Animatic Review — only after a real-frame Animatic v1 is committed.
Owner:   Creative Director (gates are never opened by Production)
```

### Previous gate — Storyboard Creative Review (EP-001)

```text
Gate:    Creative Review (Storyboard EP-001)
Status:  PASSED WITH MINOR COMMENTS
Owner:   Creative Director
Decided: Creative Director, 2026-06-29
```

---

## Terminology correction (Creative Director, 2026-06-29)

The committed HTML file is an **Interactive Storyboard / Storyboard Player**, not an
animatic. It renders schematic SVG frames live in the browser — excellent for internal
ritm/timing review, wrong for Children Test. Pipeline updated accordingly:

```text
Storyboard
   ↓
Interactive Storyboard (HTML)   ← internal review tool (DONE)
   ↓
Animatic v1 (real frames)       ← the child-facing artifact (NEXT)
   ↓
Children Test
```

The file is intentionally cheap and is a rational tool for a small studio — it is kept,
just correctly named. The child watches the **next** stage, not this one.

---

## Active EP-001 Artifacts

- **Story (canon, frozen):** `STORY/STORY-001_Where_Did_The_Ball_Hide.md` — «Куда спрятался мячик?»
- **Storyboard v1 (passed w/ comments):** `episodes/EP-001/storyboard/STORY-001-ball-storyboard-v1.md`
- **Interactive Storyboard (internal tool, NOT the animatic):** `episodes/EP-001/animatic/STORY-001-ball-animatic-v1.html`
  - ⚠️ to be renamed to a `*-storyboard-player-*` path when the real Animatic v1 is built, to avoid confusion.
- **Animatic v1 (real frames):** NOT BUILT YET — current focus.
- **Off-canon / non-active:** `episodes/EP-001/storyboard/STORY-LEAF-storyboard-v1.svg`

---

## Notes carried forward (verify on the real Animatic v1)

1. **Scene 4 (Max searches alone, 0:55–1:15):** keep visually varied; trim toward ~15s if it drags. Do not cut the beat.
2. **Three to-camera interaction pauses (panels 6, 8, 14):** keep eye-line soft, not demanding.
3. **First-30-seconds risk is a STORY-001 question, NOT an artifact fix.** Opening ritual length and the
   late hook come from frozen STORY-001 timecodes. Do not "speed up" by editing artifacts — that would
   rewrite canon through the back door. Let **Children Test** measure first-30s attention; only OBS evidence
   may justify changing STORY-001.

---

## Progress

```text
Foundation / Canon (frozen)
✅ AKS-000  Project Philosophy
✅ AKS-001  Child Psychology / Knowledge Base
✅ AKS-002  World Bible: Luma
✅ AKS-003  Character Bible (Max, Eva)
✅ AKS-004  Visual Language
✅ DEC-000  Architecture Freeze
✅ STORY-001 Reference Story / Pilot — «Куда спрятался мячик?» (frozen)

EP-001 Production
✅ Storyboard             — v1 canon-aligned, PASSED WITH MINOR COMMENTS
✅ Interactive Storyboard — HTML player (internal review tool)
🟡 Animatic v1 (real frames) — NOT STARTED (current focus)
⬜ Children Test          — not started
⬜ OBS                    — not started
⬜ Final                  — not started
```

---

## Pipeline position

```text
Story ✅ → Storyboard ✅ → Interactive Storyboard ✅ → Animatic v1 (real frames) 🟡 → [Animatic Review] → Children Test → OBS → Production
```

---

## Housekeeping notes (non-blocking)

- `README.md` is **stale**: it lists the next step as `ART-001.001 — Eye Research`.
- `tmp_test_commit.md` at repo root appears to be a leftover test artifact and can be removed if approved.

---

## Roles (by function, not by tool)

- **Creator & Producer / Studio Founder** — direction, final authority.
- **Creative Director** — owns Quality Gates; only role that marks a gate Passed.
- **Production Director** — produces artifacts, moves the pipeline, sets gates to Waiting/Blocked, commits work. Never marks a gate Passed; never edits frozen canon.
- **Children Test / OBS** — validates the experience; the only thing that can justify reopening frozen canon.
