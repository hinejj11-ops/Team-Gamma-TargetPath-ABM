# Synthetic 100-company test dataset

File: `data/100_Company_Dataset_Synthetic_Test.csv`

- Rows 1–20: **unchanged** from HockeyBear01/ABM-Project `data/20_Company_Dataset_Iteration7.csv` (source blob SHA `c49c86aa9b72f9450535097b31a4e0ad53c895f7`).
- Rows 21–100: **80 invented test accounts**, derived from seed-row structures but with distinct fictional names and varied employee counts, revenues, ACVs, dates, contract status, satisfaction, evidence availability and review cases.
- Exactly **100 companies, 54 columns**. Existing 20 account values preserved exactly.
- **Synthetic fixtures only**. No claims about actual businesses, real vendors, or verified market signals. Do not use for prospecting or business decisions.
- **No expected scoring answers** are provided. This is an input fixture for blind scoring and workflow stress testing, not an independent ground-truth validation set.
- Run with a stated scoring-as-of date; the dates in this file were intentionally varied relative to October 11, 2026, including stale evidence, renewals at 12/24-month boundaries, missing renewal dates, and dates already past.
- Includes deliberate **fatal/missing field** scenarios (blank Industry, Target ACV, employee count, geography, etc.). An end-to-end system should hold or route these cases as required by the rubric; do not silently repair them.
- The 80 synthetic records intentionally reuse some seed-derived narratives and tech stacks. They are **not 80 independently researched companies**. Use them for load, routing, exception and regression testing, not as evidence of scoring accuracy or independence.

## Coverage in the 80 new rows
Each of the 16 deterministic scenario positions occurs five times. Positions exercise missing industry, ACV, employee count, geography, referenceability; unhappy churn; dissatisfied and satisfied incumbents; locks beyond 24 months; undated locks; exact 12- and 24-month renewal boundaries; past renewals; unknown lock status; and satisfaction-based cap changes. Other varied fields exercise stale/missing intent signals, technology evidence, compliance, budget and contacts.

This file is on a **separate data branch**; the restored `main` branch and teammate scoring implementation are unchanged. Do not merge or run against the MVP until TargetOrate adjudication is complete.
