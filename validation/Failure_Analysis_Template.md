# Failure Analysis Template

Complete after every validation run. Karen's standard: know where the workflow fails and why, on a hundred companies, not just that one example works. Validation only. Never use in scoring.

## Run details
Workflow version, AI and model version, run date, dataset name and size, Scoring As Of Date, reference file used (if any).

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
Classify every difference once: model or execution error, reference file error, rubric ambiguity, data ambiguity, missing data handled correctly but different from the reference.
| Cause | Count | Example (account, criterion) | Fix and where it goes (rubric, prompt, data, reference file) |
|---|---:|---|---|

## Tier errors
List every account whose tier differs from the reference, with the criteria that caused it and whether the review rule would have caught it.

## What the review rule missed and over caught
Accounts that were wrong but marked `Acceptable`, and accounts sent to review that the key says were fine.

## Open items for TargetOrate
