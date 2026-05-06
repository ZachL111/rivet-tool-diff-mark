# Review Journal

The repository goal stays the same: package a Python local lab for diff analysis with fixture event logs, golden state snapshots, and documented operating limits. This note explains the added review angle.

The local checks classify each case as `ship`, `watch`, or `hold`. That gives the project a small review vocabulary that matches its cli tools focus without claiming live deployment or external usage.

## Cases

- `baseline`: `file span`, score 176, lane `ship`
- `stress`: `terminal width`, score 207, lane `ship`
- `edge`: `argument risk`, score 159, lane `ship`
- `recovery`: `report density`, score 172, lane `ship`
- `stale`: `file span`, score 191, lane `ship`

## Note

The repository should be understandable without pretending it is larger than it is.
