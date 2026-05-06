# rivet-tool-diff-mark

`rivet-tool-diff-mark` is a compact Python repository for cli tools, centered on this goal: Package a Python local lab for diff analysis with fixture event logs, golden state snapshots, and documented operating limits.

## Reason For The Project

The project exists to keep a narrow engineering decision visible and testable. For this repo, that decision is how file span and argument risk should influence a review result.

## Rivet Tool Diff Mark Review Notes

`stress` and `edge` are the cases worth reading first. They show the optimistic and cautious ends of the fixture.

## What It Does

- `fixtures/domain_review.csv` adds cases for file span and terminal width.
- `metadata/domain-review.json` records the same cases in structured form.
- `config/review-profile.json` captures the read order and the two review questions.
- `examples/rivet-tool-diff-walkthrough.md` walks through the case spread.
- The Python code includes a review path for `terminal width` and `argument risk`.
- `docs/field-notes.md` explains the strongest and weakest cases.

## How It Is Put Together

The repository has two validation layers: the original compact policy fixture and the domain review fixture. They are separate so one can change without hiding failures in the other.

The Python code keeps the review rule close to the tests.

## Run It

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

## Check It

The same command runs the local verification path. The highest-scoring domain case is `stress` at 207, which lands in `ship`. The most cautious case is `edge` at 159, which lands in `ship`.

## Boundaries

No external service is required. A deeper version would add more negative cases and a clearer boundary around invalid input.
