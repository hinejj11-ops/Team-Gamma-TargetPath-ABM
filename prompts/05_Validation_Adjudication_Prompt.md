# Validation and Adjudication Prompt

## Purpose
Test the workflow without leaking expected results into the scoring run, then adjudicate disagreements.

## Prompt
Phase 1 — Blind run:
1. Execute input validation and FIOR scoring without reading any file under `/validation/` or any validation-only field.
2. Run the self review (`prompts/06_Criterion_Self_Review_Prompt.md`). Accept no human input; the human input step is not exercised in a blind run and results are provisional.
3. Lock and retain the complete C1-C14 results, dimensions, totals, tiers, and review statuses, plus the self review log. Report self review corrections separately from first pass results, and label which workflow version produced the run.

Phase 2 — Comparison:
4. Only after Phase 1 is complete, read the designated expected-results file.
5. Calculate exact criterion agreement, dimension/total differences, tier agreement, and review-status agreement.
6. List every disagreement.

Phase 3 — Human adjudication:
7. For each disagreement, evaluate the frozen source hierarchy rather than assuming the expected key is correct.
8. Classify it as MODEL/EXECUTION ERROR, VALIDATION-KEY ERROR, RUBRIC AMBIGUITY, or DATA AMBIGUITY.
9. Record the governing evidence and recommended disposition.
10. Do not modify the scoring rules or expected-results key during the same blind test.
11. Report both raw agreement and adjudicated performance; clearly state the denominator and treatment of ambiguous cases.

Return a validation report and an adjudication ledger suitable for audit.
