# OBS — Observation System

OBS stores real observations from tests and reviews.

OBS is not a decision. It is a fact record.

DEC uses OBS to update decisions.

---

## Core rule

Every OBS entry must separate:

```text
Expected:
Observed:
Difference:
Decision impact:
```

This prevents the team from seeing only what it hoped to see.

---

## Example

```text
OBS-001
Context: STORY-001 animatic test
Expected: viewer follows Max and reacts to “В домик!”
Observed: viewer follows only the ball and ignores Max
Difference: the ball effect may be too strong
Decision impact: reduce ball sound or movement in animatic v2
```

---

## OBS influences DEC

OBS can confirm or overturn a design decision.

If reality disagrees with the theory, reality wins.

> Reality over Architecture.
