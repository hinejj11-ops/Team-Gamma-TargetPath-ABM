# Reproducible v1.1 scoring execution

**Status: SCRIPT COMMITTED, EXECUTION NOT YET VERIFIED.** The runner is provisional and is not an approved AI-scoring implementation.

## Run

From the repository root, with Python 3.10+:

```bash
python tools/score_v1_1.py --input data/20_Company_Dataset_Iteration7.csv --out-dir validation/local_run
```

Expected artifacts:
- `validation/local_run/portfolio_PROVISIONAL.csv` — 20 account totals, C1–C14 scores, gate outcomes, NS bounds and review flags.
- `validation/local_run/criterion_evidence.csv` — 280 criterion decisions, cited source fields, rule explanations and confidence.

**Never substitute the historical expected key as scoring input.** Keep generated output frozen before opening any reference results. Check output counts, then independently re-derive all 280 decisions, review any rubric ambiguities and correct defects. Human approval is required before release.

## Known limitations requiring QA

1. C12's client historical win-rate baseline is conditional on budget confirmation; confirm whether its scoring interpretation agrees with the approved rubric.
2. C5 distinct signal types are identified by their structured descriptions; verify that this matches the intended four signal categories, especially repeated descriptions.
3. C3 incomplete coverage may require NS rather than a numeric low band where required-category absence has not been explicitly verified.
4. C1 adjacent categories and C2 boundary logic need targeted unit tests.
5. C14 past event/meeting and champion precedence need review.
6. The script currently fixes the Scoring As Of Date at **2026-10-11**, intentionally matching the regression fixtures; make this configurable for production.
7. The runner is deterministic, not an LLM blind scoring or independent AI self-review. A human must resolve scoring and validation-key conflicts.

Do not merge PR #19 or expand to 100 accounts based solely on the existence of this script.
