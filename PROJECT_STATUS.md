# PROJECT STATUS — AI Kids Studio

_Living document. **Not canon.** Update freely; do not freeze._
_Last updated: 2026-06-29_

> First file any agent should read after README.md.
> Tells you where the studio is **right now** and what the next move is.

---

## Current Production Stage

- **Current Episode:** EP-001 (Pilot)
- **Current Focus:** Animatic Review (EP-001) + record human scratch voice
- **Next Milestone:** Animatic Review → Children Test #001

---

## Current Quality Gate

```text
Gate:    Animatic Review (EP-001)
Status:  WAITING FOR REVIEW
Owner:   Creative Director
```

Animatic v1 (real frames) is built and committed as reproducible sources. Production
cannot open this gate. Only the Creative Director marks it Passed.

### Open production sub-task (does not block review of picture/timing)
- **Human scratch voice** must be recorded against `episodes/EP-001/animatic/VO-cue-sheet.md`.
  The animatic's voice track is intentionally empty (no TTS). Picture, timing, ambience and
  pauses can be reviewed now; voice is layered in before Children Test.

### Previous gate — Storyboard Creative Review (EP-001)
```text
Status: PASSED WITH MINOR COMMENTS  ·  Creative Director, 2026-06-29
```

---

## Active EP-001 Artifacts

- **Story (canon, frozen):** `STORY/STORY-001_Where_Did_The_Ball_Hide.md` — «Куда спрятался мячик?»
- **Storyboard v1 (passed w/ comments):** `episodes/EP-001/storyboard/STORY-001-ball-storyboard-v1.md`
- **Interactive Storyboard (internal tool, NOT the animatic):** `episodes/EP-001/animatic/STORY-001-ball-animatic-v1.html`
  - ⚠️ to be renamed to a `*-storyboard-player-*` path to avoid confusion.
- **Animatic v1 (real frames) — WAITING REVIEW:** `episodes/EP-001/animatic/`
  - `render_frames.py`, `synth_audio.py`, `build_animatic.sh` — rebuild → `STORY-001-ball-animatic-v1.mp4` (~4:55)
  - `VO-cue-sheet.md` — RU lines + timecodes for human scratch voice
  - `README.md` — what it is, how to rebuild, gate, timings
  - the `.mp4` is a build output (regenerate via `build_animatic.sh`), not stored as a git binary
- **Off-canon / non-active:** `episodes/EP-001/storyboard/STORY-LEAF-storyboard-v1.svg`

---

## Notes carried forward (verify on Animatic Review)

1. **Scene 4 (Max searches alone):** keep visually varied; trim toward ~15s if it drags. Do not cut the beat.
2. **Three to-camera pauses (panels 6, 8, 14):** keep eye-line soft, not demanding.
3. **First-30-seconds risk is a STORY-001 question, NOT an artifact fix.** Let **Children Test** measure
   first-30s attention; only OBS evidence may justify changing frozen STORY-001.

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
🟡 Animatic v1 (real frames) — built; AWAITING ANIMATIC REVIEW; human VO pending
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

- `README.md` (root) is **stale**: it lists the next step as `ART-001.001 — Eye Research`.
- `tmp_test_commit.md` at repo root appears to be a leftover test artifact and can be removed if approved.

---

## Roles (by function, not by tool)

- **Creator & Producer / Studio Founder** — direction, final authority.
- **Creative Director** — owns Quality Gates; only role that marks a gate Passed.
- **Production Director** — produces artifacts, moves the pipeline, sets gates to Waiting/Blocked, commits work. Never marks a gate Passed; never edits frozen canon.
- **Children Test / OBS** — validates the experience; the only thing that can justify reopening frozen canon.
