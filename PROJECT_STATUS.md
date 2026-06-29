# PROJECT STATUS — AI Kids Studio

_Living document. **Not canon.** Update freely; do not freeze._
_Last updated: 2026-06-29_

> First file any agent should read after README.md.
> Tells you where the studio is **right now** and what the next move is.

---

## Current Production Stage

- **Current Episode:** EP-001 (Pilot)
- **Current Focus:** Record human scratch voice → lay into mp4 → Animatic Review (final)
- **Next Milestone:** Animatic Review (final) → Children Test #001

---

## Current Quality Gate

```text
Gate:    Animatic Review (final) — EP-001  [picture + voice together]
Status:  BLOCKED
Blocker: Human scratch voice not yet recorded/laid into the mp4.
Owner:   Creative Director
```

⚠️ **Do NOT start Children Test from the current voiceless mp4.** The picture/timing pass
below is NOT a green light for testing with children. A child aged 2–3 cannot get the full
experience without a human voice. Children Test waits for Animatic Review (final).

### Picture/timing gate — Animatic Review (v1, picture only)
```text
Gate:    Animatic Review (EP-001) — picture & timing only
Status:  PASSED WITH COMMENTS
Owner:   Creative Director
Decided: Creative Director, 2026-06-29
```

Comments (accepted, not blocking the picture pass):
1. Frames are readable but very schematic — fine for a first internal review.
2. Without voice, a 2–3 y/o does not get the full experience.
3. Ambience/music is better than silence, but **voice is critical** here.
4. Do not change STORY-001 over the first-30s question — Children Test will measure it.

### Previous gate — Storyboard Creative Review (EP-001)
```text
Status: PASSED WITH MINOR COMMENTS  ·  Creative Director, 2026-06-29
```

---

## Open production sub-task (unblocks the final gate)

- **Record human scratch voice** against `episodes/EP-001/animatic/VO-cue-sheet.md`
  (plain human read, not acted; no TTS). Then Production lays it into the mp4 and sets
  **Animatic Review (final)** to WAITING for the Creative Director.

---

## Active EP-001 Artifacts

- **Story (canon, frozen):** `STORY/STORY-001_Where_Did_The_Ball_Hide.md` — «Куда спрятался мячик?»
- **Storyboard v1 (passed w/ comments):** `episodes/EP-001/storyboard/STORY-001-ball-storyboard-v1.md`
- **Interactive Storyboard (internal tool, NOT the animatic):** `episodes/EP-001/animatic/STORY-001-ball-animatic-v1.html`
  - ⚠️ to be renamed to a `*-storyboard-player-*` path to avoid confusion.
- **Animatic v1 (real frames) — picture PASSED w/ comments; voice pending:** `episodes/EP-001/animatic/`
  - `render_frames.py`, `synth_audio.py`, `build_animatic.sh` → rebuild `STORY-001-ball-animatic-v1.mp4` (~4:55, voiceless)
  - `VO-cue-sheet.md` — RU lines + timecodes for human scratch voice
  - `README.md` — what it is, how to rebuild, gate, timings
  - the `.mp4` is a build output (regenerate via `build_animatic.sh`), not a git binary
- **Off-canon / non-active:** `episodes/EP-001/storyboard/STORY-LEAF-storyboard-v1.svg`

---

## Notes carried forward (verify on Animatic Review final)

1. **Scene 4 (Max searches alone):** keep visually varied; trim toward ~15s if it drags. Do not cut the beat.
2. **Three to-camera pauses (panels 6, 8, 14):** keep eye-line soft, not demanding.
3. **First-30-seconds risk is a STORY-001 question, NOT an artifact fix.** Children Test measures it;
   only OBS evidence may justify changing frozen STORY-001.

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
🟡 Animatic v1 (real frames) — picture/timing PASSED WITH COMMENTS; human voice PENDING
⬜ Animatic Review (final)   — BLOCKED until voice is laid in
⬜ Children Test          — not started
⬜ OBS                    — not started
⬜ Final                  — not started
```

---

## Pipeline position

```text
Story ✅ → Storyboard ✅ → Interactive Storyboard ✅ → Animatic v1 picture 🟡 → (human voice) → Animatic Review (final) → Children Test → OBS → Production
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
