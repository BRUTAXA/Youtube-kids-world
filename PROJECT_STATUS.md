# PROJECT STATUS — AI Kids Studio

_Living document. **Not canon.** Update freely; do not freeze._
_Last updated: 2026-06-29_

> First file any agent should read after README.md.
> Tells you where the studio is **right now** and what the next move is.

---

## Current Production Stage

- **Current Episode:** EP-001 (Pilot)
- **Current Focus:** Animatic Review (EP-001)
- **Next Milestone:** Animatic Review → Children Test #001

---

## Current Quality Gate

```text
Gate:    Animatic Review (EP-001)
Status:  WAITING FOR REVIEW
Owner:   Creative Director
```

Animatic v1 is committed and ready. Production cannot open this gate.
Only the Creative Director marks it Passed.

### Previous gate — Storyboard Creative Review (EP-001)

```text
Gate:    Creative Review (Storyboard EP-001)
Status:  PASSED WITH MINOR COMMENTS
Owner:   Creative Director
Decided: Creative Director, 2026-06-29
```

---

## Active EP-001 Artifacts

- **Story (canon, frozen):** `STORY/STORY-001_Where_Did_The_Ball_Hide.md` — «Куда спрятался мячик?»
- **Storyboard v1 (passed w/ comments):** `episodes/EP-001/storyboard/STORY-001-ball-storyboard-v1.md`
- **Animatic v1 (waiting review):** `episodes/EP-001/animatic/STORY-001-ball-animatic-v1.html`
- **Off-canon / non-active:** `episodes/EP-001/storyboard/STORY-LEAF-storyboard-v1.svg`

---

## Animatic Notes (verify during Animatic Review)

1. **Scene 4 (Max searches alone, 0:55–1:15):** emotionally needed but risks sagging for
   ages 2–3. Built with two visible search spots; trim toward ~15s if it drags. Do not cut the beat.
2. **Three to-camera interaction pauses (panels 6, 8, 14):** marked in the animatic; keep the
   eye-line soft, not demanding. Confirm live.
3. **First-30-seconds risk is a STORY-001 question, NOT a storyboard/animatic fix.** Opening
   ritual length (0:00–0:18) and late hook (ball loss at 0:35) come from frozen STORY-001 timecodes.
   Do not "speed up" by editing the artifacts — that would rewrite canon through the back door.
   Decision: keep canon timing; let **Children Test** measure first-30s attention. Only OBS evidence
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
✅ Storyboard       — v1 canon-aligned, PASSED WITH MINOR COMMENTS
🟡 Animatic         — v1 committed, AWAITING ANIMATIC REVIEW
⬜ Children Test    — not started
⬜ OBS              — not started
⬜ Final            — not started
```

---

## Pipeline position

```text
Story ✅ → Storyboard ✅ → Animatic ✅(v1, waiting review) → [Animatic Review] → Children Test → OBS → Production
```

---

## Housekeeping notes (non-blocking)

- `README.md` is **stale**: it lists the next step as `ART-001.001 — Eye Research`.
  Update it after the Animatic Review result is known, so README does not jump ahead of the gate.
- `tmp_test_commit.md` at repo root appears to be a leftover test artifact and can be removed if approved.

---

## Roles (by function, not by tool)

- **Creator & Producer / Studio Founder** — direction, final authority.
- **Creative Director** — owns Quality Gates; only role that marks a gate Passed.
- **Production Director** — produces artifacts, moves the pipeline, sets gates to Waiting/Blocked, commits work. Never marks a gate Passed; never edits frozen canon.
- **Children Test / OBS** — validates the experience; the only thing that can justify reopening frozen canon.
