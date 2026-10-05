# MVP v1.0 Acceptance Test

**Status:** PASS WITH MINOR CORRECTIONS  
**Test basis:** Default `main` branch after Iterations 1-6 and toolkit packaging were merged.  
**Test method:** Cold-start operator examination using the README and packaged toolkit artifacts, with `/validation/` quarantined until the operational workflow was examined.

## Acceptance Results

| Acceptance condition | Result |
|---|---|
| Prepare inputs from reusable templates | PASS |
| Validate ICP and account inputs | PASS |
| Execute the FIOR scoring chain | PASS |
| Handle missing, negative, contradictory, and stale evidence | PASS |
| Route exceptions without unsupported assumptions | PASS |
| Route mandatory-review cases to human review | PASS |
| Record human approval/override decisions | PASS |
| Produce standardized portfolio output | PASS |
| Produce Account Summary Cards | PASS |
| Apply pre-release quality control | PASS |
| Quarantine validation assets during blind execution | PASS |
| Conduct post-run validation and adjudication | PASS |
| Discover and operate the workflow from the README | PASS |

**Functional acceptance:** 13/13 conditions passed.

## Minor corrections discovered

1. `MASTER_PROMPT.md` referenced `FIOR_Scoring_Rubric_10_02_2026.md`, while the actual rubric is `FIOR_Scoring_Rubric_10_2_2026.md`. Corrected in the MVP cleanup PR.
2. The validation documentation described the expected-results key as the original historical key even though the working CSV had already incorporated adjudicated corrections. MVP cleanup separates the historical Iteration 6 key from the adjudicated working key and documents their distinct purposes.

## MVP decision

The toolkit meets the minimum viable product definition for the capstone: a new operator can discover the workflow, prepare inputs, run the governed AI scoring process, route exceptions and human approvals, produce standard outputs, and perform blind validation using documented artifacts.

## Scope boundary

This acceptance test establishes workflow usability and packaging completeness. It does not certify the four unresolved rubric/data ambiguities in the Iteration 6 adjudication log, and it does not convert synthetic capstone assets into production client data.
