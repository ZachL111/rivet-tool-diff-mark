# Rivet Tool Diff Mark Walkthrough

The fixture is intentionally compact, so the review starts with the cases that pull farthest apart.

| Case | Focus | Score | Lane |
| --- | --- | ---: | --- |
| baseline | file span | 176 | ship |
| stress | terminal width | 207 | ship |
| edge | argument risk | 159 | ship |
| recovery | report density | 172 | ship |
| stale | file span | 191 | ship |

Start with `stress` and `edge`. They create the widest contrast in this repository's fixture set, which makes them better review anchors than the middle cases.

`stress` is the optimistic case; use it to make sure the scoring path still rewards strong signal.
