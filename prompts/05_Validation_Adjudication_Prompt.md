# Validation and Review Prompt

## Purpose
Test the workflow without leaking test scenario or expected-outcome files into the scoring run, then review any differences. There is no answer key. Results come from running the process, and differences are reviewed by a consultant.

## Prompt
Phase 1 — Independent run:
1. Execute input validation and FIOR scoring without reading any file under `/validation/` or any validation-only field.
2. Run the self review (`prompts/06_Criterion_Self_Review_Prompt.md`). Accept no human input; the human input step is not exercised in a blind run and results are provisional.
3. Lock and retain the complete C1-C14 results, dimensions, totals, tiers, and review statuses, plus the self review log. Report self review corrections separately from first pass results, and label which workflow version produced the run.

Phase 2 — Comparison:
4. Only after Phase 1 is complete, and only if a prior run or test scenario file is being compared, read that file. Treat it as a reference point, not as the correct answer.
5. Calculate exact criterion agreement, dimension/total differences, tier agreement, and review-status agreement.
6. List every disagreement.

Phase 3 — Consultant review:
7. For each difference, evaluate the frozen source hierarchy rather than assuming the reference file is correct.
8. Classify it as MODEL/EXECUTION ERROR, REFERENCE FILE ERROR, RUBRIC AMBIGUITY, or DATA AMBIGUITY.
9. Record the governing evidence and recommended disposition.
10. Do not modify the scoring rules or the reference file during the same test.
11. Report raw agreement and reviewed outcomes separately; state the denominator and the treatment of ambiguous cases. Do not describe agreement with a reference file as accuracy.

Return a validation report and a review ledger suitable for audit.
