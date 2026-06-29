# PROJECT STATUS — AI Kids Studio

_Living document. **Not canon.** Update freely; do not freeze._
_Last updated: 2026-06-29_

> First file any agent should read after README.md.
> Tells you where the studio is **right now** and what the next move is.

---

## Current Production Stage

- **Current Episode:** EP-001 (Pilot)
- **Current Focus:** Complete the Animatic Review checklist (human scratch voice outstanding)
- **Next Milestone:** Animatic Review PASS → Children Test #001

> Infrastructure is intentionally settled. From here the work is creative:
> draw frames, record voice, watch with children, write OBS. Do not keep
> reorganizing structure — when tempted to add a gate or a doc, prefer a
> checklist item inside what already exists.

---

## Current Quality Gate

```text
Gate:    Animatic Review (EP-001)
Status:  IN REVIEW
Owner:   Creative Director
```

A gate answers one question: can we go to the next stage? Right now — no. So the gate is
simply **not yet passed**. (One gate, with a checklist — we do not split it into picture/
sound/export gates; DEC-000 asks us to avoid proliferating gates.)

### Animatic Review checklist
```text
☑ Picture           — readable; schematic, fine for first review
☑ Timing            — canonical STORY-001 timings
☑ Interaction pauses — present and marked (panels 6, 8, 14)
☑ Ambience balanced — ambience + simple music bed
☐ Human scratch voice present
☐ Final playback reviewed

PASS only after every box is checked.
```

**Studio rule:** _An animatic must contain a human scratch voice before Children Test._
(Any person may record it — founder, another person, a future actor, any studio member.
The pipeline does not depend on a specific individual. No TTS.)

⚠️ Do NOT start Children Test from the current voiceless mp4 — the voice box is unchecked.

### Previous gates
```text
Storyboard Creative Review (EP-001): PASSED WITH MINOR COMMENTS · Creative Director, 2026-06-29
```

Picture/timing comments accepted (not blocking, recorded for the build):
1. Frames readable but very schematic — fine for first internal review.
2. Without voice a 2–3 y/o does not get the full experience.
3. Ambience/music better than silence, but voice is critical here.
4. Do not change STORY-001 over the first-30s question — Children Test will measure it.

---

## Open production sub-task (checks the outstanding box)

- **Record a human scratch voice** against `episodes/EP-001/animatic/VO-cue-sheet.md`
  (plain human read, not acted; no TTS). Production then lays it into the mp4 and reviews
  final playback — completing the last two checklist boxes.

---

## Active EP-001 Artifacts

- **Story (canon, frozen):** `STORY/STORY-001_Where_Did_The_Ball_Hide.md` — «Куда спрятался мячик?»
- **Storyboard v1 (passed w/ comments):** `episodes/EP-001/storyboard/STORY-001-ball-storyboard-v1.md`
- **Storyboard Player (interactive, internal review tool):** `episodes/EP-001/storyboard/player/STORY-001-ball-storyboard-player-v1.html`
- **Animatic v1 (real frames) — in review; voice box outstanding:** `episodes/EP-001/animatic/`
  - `render_frames.py`, `synth_audio.py`, `build_animatic.sh` → rebuild `STORY-001-ball-animatic-v1.mp4` (~4:55, voiceless)
  - `VO-cue-sheet.md` — RU lines + timecodes for human scratch voice
  - `README.md` — what it is, how to rebuild, gate, timings
  - the `.mp4` is a build output (regenerate via `build_animatic.sh`), not a git binary
- **Off-canon / non-active:** `episodes/EP-001/storyboard/STORY-LEAF-storyboard-v1.svg`

---

## Notes carried forward (verify before Animatic Review PASS)

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
✅ Storyboard Player      — HTML (internal review tool), under storyboard/player/
🟡 Animatic v1 (real frames) — IN REVIEW; human scratch voice + final playback outstanding
⬜ Children Test          — not started
⬜ OBS                    — not started
⬜ Final                  — not started
```

---

## Pipeline position

```text
Story ✅ → Storyboard ✅ → Animatic Review (in review) → Children Test → OBS → Production
```

---

## Housekeeping notes (non-blocking)

- `README.md` (root) is **stale**: it lists the next step as `ART-001.001 — Eye Research`.
- `tmp_test_commit.md` at repo root appears to be a leftover test artifact and can be removed if approved.
