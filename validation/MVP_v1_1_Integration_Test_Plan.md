# TargetPath MVP v1.1 Integration — Acceptance Gates

**Status:** Integration candidate; not production approved.

## Sequence
1. Confirm all v1.0 baseline assets and the original Week 6 dataset are unchanged.
2. Fix a `Scoring As Of Date` (for the included Iteration 7 fixtures use 2026-10-11).
3. Input validate the scoring-only `data/20_Company_Dataset_Iteration7.csv` without opening `/validation/` or any ground-truth column.
4. Run first-pass C1–C14 on all 20 records, lock output and provenance (model identifier, exact version, run date, rubric/prompt revision, dataset hash, as-of date).
5. Perform a **second independent pass** over all 280 criteria; log each discrepancy and recompute dimensions, totals, score-implied and post-gate tiers.
6. Run 22 independent gate scenarios including boundaries, contract status, satisfaction, unknown status, and past renewal date.
7. Run tier-impact missing-data bounds plus uncapped mandatory exceptions, sampling routine acceptable accounts. In blind evaluation do not pretend human approval occurred: return PROVISIONAL.
8. Lock all predictions before reading any test scenario file. Compare against test scenario files only after independent execution and log all deviations. There is no answer key; report the results from the run itself.
9. Return CloudBridge before/after and portfolio tier distribution; ensure the gate never increases underlying FIOR scores.
10. Only after the 20-company run and human signoff proceed to generate a **separate 100-company fixture** covering every gate branch. Execute three independent repeatability runs and record metrics.

## Release gates
- 20/20 records accounted for; 14 criteria per record audited and provenance captured.
- 22/22 competitive-lock scenarios pass, with unknown-status review safeguarded.
- No unauthorized changed rubric weights or excluded /validation/ evidence leakage.
- No mandatory exception deferred solely because of a 25% routine-review target.
- Every tier remains provisional until consultant approval.
- No claim that the 100-company test has run before fixtures and evidence exist.

## Known open issues
Exact satisfaction-band boundaries, undated dissatisfied accounts, stale renewal dates, and vendor-event applicability still require client confirmation. The sample dataset does not contain populated verified vendor events. Run them as explicit synthetic cases before enabling live C8 uplifts.
