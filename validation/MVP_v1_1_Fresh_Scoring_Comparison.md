# MVP v1.1 — Fresh Scoring Candidate and Diagnostic Comparison

**Run date:** 2026-10-12  
**Scoring as-of date:** 2026-10-11  
**Branch:** `mvp-v1.1-integration`  
**Candidate output:** `validation/MVP_v1_1_Fresh_Scoring_Candidate.csv` (committed before key comparison)  
**Comparison key:** `validation/Expected_FIOR_Results_ITERATION7_GATE_DRAFT.csv`

## Status: NOT ACCEPTED

The 20 accounts and 280 C1–C14 cells were processed using a **simplified, rule-based candidate implementation**. It is not a certified implementation of every rubric detail and must not be represented as an independent fully compliant AI self-review. Fifteen candidate criteria were NS. No human approvals have occurred.

After the candidate output was committed, the composite scores and post-gate tiers were compared with the existing draft expected-results fixture.

- Exact composite matches: **6 / 20**.
- Matching post-gate tiers: **15 / 20**.
- Different final tiers: **5 / 20**.

| Company | Candidate score | Draft key score | Candidate final tier | Draft key final tier |
| --- | ---: | ---: | --- | --- |
| Pioneer Digital Services | 81 | 78 | Tier 1 | Tier 2 |
| Stratagem Software | 59 | 66 | Tier 3 | Tier 2 |
| Pinnacle Enterprise Tech | 57 | 64 | Tier 3 | Tier 2 |
| Quantum Integration Group | 33 | 40 | Nurture / Disqualify | Tier 3 |
| Helix Cloud Solutions | 40 | 39 | Tier 3 | Nurture / Disqualify |

CloudBridge candidate score **84** versus draft **85**; both yield post-gate **Tier 3**. The candidate's simplified treatment of technology, C11, C12, missing evidence and other score bands is a known potential source of error. **Do not change the rubric or adjudicate the key merely to match this candidate.**

## Required remediation before acceptance

1. Independently re-derive **every one of the 280 criterion decisions** from the complete rubric, ICP, and structured evidence, preserving an evidence/band/confidence trail for each. Start with the five tier-changing accounts and the largest score gaps, but finish all 20.
2. Implement all required score bands, including 10/8/6/4/2 and supported odd-band scores, C3 preferred vs required tech, C4 applicability, C5 signal-type distinctness, C6 multiple triggers, C11 top-quartile reference test, C12 actual win-rate/competitive/budget evidence, and C13 role verification.
3. Rerun self-review independently from the first-pass candidate, lock all 280 rederived decisions, record corrections/escalations, and recompute tiers and missing-data bounds.
4. Complete human correction and approval exercise. Mark all outputs PROVISIONAL until a real consultant signs off.
5. Document exact execution environment, model identifier/version if an LLM is used, commit hashes, and reproducible scoring script or prompt transcript. A new deterministic test should not be mislabeled as a blind AI model test.

## Gate regression retained

The earlier **20/20 post-gate and 22/22 edge-case** results test the gate against the carried-forward score fixture, not the candidate scoring implementation. They remain separate from full end-to-end acceptance.
