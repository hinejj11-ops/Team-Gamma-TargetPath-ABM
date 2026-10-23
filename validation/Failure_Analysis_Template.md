# Failure Analysis Template

Complete after every validation run. Karen's standard: know where the workflow fails and why, on a hundred companies, not just that one example works. Validation only. Never use in scoring.

## Run details
Workflow version, AI and model version, run date, dataset name and size, Scoring As Of Date, key used.

## Summary
| Measure | Value |
|---|---|
| Accounts scored | |
| Criteria compared | accounts times 14 |
| Raw criterion agreement | |
| Tier agreement | |
| Review rate against the 25 percent ceiling | |
| Accounts held (fatal missing field) | |

## Failures by criterion
| Criterion | Disagreements | Share of all disagreements |
|---|---:|---:|

## Failures by cause
Classify every disagreement once: model or execution error, validation key error, rubric ambiguity, data ambiguity, missing data handled correctly but different from key.
| Cause | Count | Example (account, criterion) | Fix and where it goes (rubric, prompt, data, key) |
|---|---:|---|---|

## Tier errors
List every account whose tier differs from the key, with the criteria that caused it and whether the review rule would have caught it.

## What the review rule missed and over caught
Accounts that were wrong but marked `Acceptable`, and accounts sent to review that the key says were fine.

## Open items for TargetOrate
