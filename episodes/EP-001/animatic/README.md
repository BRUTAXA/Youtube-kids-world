# EP-001 — Animatic v1 (real frames)

**Source canon:** `STORY/STORY-001_Where_Did_The_Ball_Hide.md` (approved, frozen).
**Adapts** the canon storyboard `episodes/EP-001/storyboard/STORY-001-ball-storyboard-v1.md`. Does not change canon.

**What this is:** a rough *viewing* animatic — real still frames cut at the canonical
STORY-001 timings (~4:55), with room ambience + a simple warm music bed and held pause
beats. Movement is intentionally minimal (stills + cuts).

**Voice:** the voice track is intentionally **empty**. Scratch voice must be a *human*
reading (not acted, not perfect) — recorded by the studio against `VO-cue-sheet.md`.
No TTS is used.

**Frames** are rough blocking in the studio silhouette style. They are **not** final
character design — see `AKS-003` Character Bible for canon character art.

## Rebuild
```bash
bash build_animatic.sh   # needs python3 (Pillow, numpy) + ffmpeg
# -> STORY-001-ball-animatic-v1.mp4  (1280x720, ~4:55)
```
The `.mp4` is a build output and is not stored in git; regenerate it from these sources.

## Quality Gate
```
Gate:   Animatic Review (EP-001)
Status: WAITING FOR REVIEW
Owner:  Creative Director
```
Production does not open this gate.

## Review focus (carried from Storyboard Creative Review)
- Scene 4 (Max searches alone): keep visually varied; trim toward ~15s if it drags.
- Three to-camera pauses (panels 6, 8, 14): keep eye-line soft, not demanding.
- First-30s attention is a STORY-001 question for **Children Test**, not an artifact edit.

## Panel timings (canonical)
1:0:00 · 2:0:18 · 3:0:35 · 4:0:55 · 5:1:15 · 6:1:35 · 7:1:50 · 8:2:05 · 9:2:18 · 10:2:32 · 11:2:42 · 12:2:50 · 13:3:10 · 14:3:25 · 15:3:40 · 16:3:55 · 17:4:15 · 18:4:35 · 19:4:40 — end 4:55
