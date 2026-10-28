# Iteration 7 / MVP v1.1 Deterministic Gate Regression

> Historical record. It was run against reference files that have since been removed (the 20 company answer key and Week 6 dataset). Terms such as "working key" and "regression key" refer to those files. The gate scenarios and Iteration 7 draft outcomes remain in `validation/`.

**Date:** 2026-10-12
**Scoring as-of date:** 2026-10-11 (fixture provenance)
**Inputs:** `data/20_Company_Dataset_Iteration7.csv`; versioned existing working FIOR score fixture and Iteration 7 draft gate outcomes
**Method:** Independent JavaScript recomputation of gate bands, satisfaction shifts, post-gate tier, and mandatory gate review flags. Expected gate outcomes were consulted **for regression comparison**, not for an independent blind 14-criterion model test.

## Results

- Dataset rows checked: **20/20**
- Post-gate tier matching draft regression key: **20/20**
- Competitive lock edge cases matching updated v1.1 policy: **22/22**
- Changed portfolio tiers: **1** (CloudBridge Solutions: Tier 1 → Tier 3)
- Unknown incumbent contract status requires consultant review: **Pioneer Digital Services**
- Differences in the carried-forward composite score between v1.0 working key and v1.1 gate fixture: **0** (none)

## Deviations

- No 20-company gate-tier mismatches.
- No edge-scenario tier/review mismatches.

## What this does *not* certify

This is a **deterministic gate regression**, not a fresh blinded AI rerun of all **280 C1–C14 judgments**; it uses carried-forward criterion totals from the existing fixture. It does not demonstrate that the criterion self-review prompt is operationally reliable across independent model executions; no consultant has approved final tiers; no verified vendor event is populated in the empty reference file. Therefore, **full v1.1 acceptance remains pending** the 20-account blind end-to-end test and human signoff described in `validation/MVP_v1_1_Integration_Test_Plan.md`. The 100-company test is a subsequent stage.
