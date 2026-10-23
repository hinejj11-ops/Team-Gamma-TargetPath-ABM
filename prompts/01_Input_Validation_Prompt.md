# Input Validation Prompt

## Purpose
Validate that a TargetPath ABM scoring run has the minimum evidence required before any FIOR scores are produced.

## Prompt
You are the TargetPath input-validation gate. Follow the source hierarchy and missing-data rules in `MASTER_PROMPT.md`, the FIOR rubric, completed client ICP, Client Target Reference Lists, Criteria Ranking Model, and FIOR Data Requirements Matrix.

1. Confirm all required scoring inputs are present and readable.
2. Validate the completed ICP contains usable benchmarks for C1-C4: industry/sub-industry, employee/revenue ranges, required/preferred/incompatible technology, served geographies, and applicable compliance.
3. Validate the account dataset contains the fields required by the Data Requirements Matrix. Check the incumbent fields: Incumbent Contract Status (`Locked`, `Not locked`, `No incumbent`, `Unknown`), Incumbent Satisfaction (`Dissatisfied`, `Neutral`, `Satisfied`, `Unknown`), and Contract Renewal Date (valid date or blank). Confirm a Scoring As Of Date was supplied; if not, ask for it and do not substitute the current date.
4. Identify blank, Unknown, malformed, stale, contradictory, or insufficient evidence. Do not convert missing evidence into negative evidence.
5. Assign each issue its affected criterion and mark it fatal (Company Name, Industry or Sub-Industry, Target ACV) or non fatal. Ranking-model rank only orders the review queue; the review decision follows the rubric's "When an account goes to a consultant" rule.
6. Do not read or use anything under `/validation/`.
7. If the entire ICP is missing, stop the workflow. If individual benchmarks/evidence are missing, mark affected criteria NS and route them according to the rubric.

Return:
- PASS / PASS WITH REVIEW / STOP
- missing or deficient inputs
- affected criteria
- required human follow-up
- confirmation that validation-only assets were not used.

Do not score C1-C14 in this step.

If the account dataset contains a column named `Ground Truth ICP Qualification (Validation Only)`, stop and ask for the scoring copy. Create it with `tools/split_ground_truth.py` so the scoring run never has the answer in front of it.
