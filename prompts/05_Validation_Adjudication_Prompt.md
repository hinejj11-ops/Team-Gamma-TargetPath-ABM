# Validation and Adjudication Prompt

## Purpose
Test the workflow without leaking expected results into the scoring run, then adjudicate disagreements.

## Prompt
Phase 1 — Blind run:
1. Execute input validation and FIOR scoring without reading any file under `/validation/` or any validation-only field.
2. Lock and retain the complete C1-C14 results, dimensions, totals, tiers, and review statuses.

Phase 2 — Comparison:
3. Only after Phase 1 is complete, read the designated expected-results file.
4. Calculate exact criterion agreement, dimension/total differences, tier agreement, and review-status agreement.
5. List every disagreement.

Phase 3 — Human adjudication:
6. For each disagreement, evaluate the frozen source hierarchy rather than assuming the expected key is correct.
7. Classify it as MODEL/EXECUTION ERROR, VALIDATION-KEY ERROR, RUBRIC AMBIGUITY, or DATA AMBIGUITY.
8. Record the governing evidence and recommended disposition.
9. Do not modify the scoring rules or expected-results key during the same blind test.
10. Report both raw agreement and adjudicated performance; clearly state the denominator and treatment of ambiguous cases.

Return a validation report and an adjudication ledger suitable for audit.