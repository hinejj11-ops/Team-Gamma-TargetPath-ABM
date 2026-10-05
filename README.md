# TargetPath AI Account Scoring Workflow (Week 5/6 MVP)
**Team Gamma | Auburn University Harbert College of Business (MBA Capstone, Fall 2026)**

## Overview

This repository is an **LLM-native operational account-scoring workflow** developed for TargetOrate. It packages the FIOR scoring methodology, client-input structure, missing-data governance, and portfolio-ranking logic needed to evaluate target accounts consistently.

The workflow is intentionally separated into two layers:

- **Stable scoring logic:** FIOR rubric, ranking model, and TargetOrate reference definitions.
- **Client-specific inputs:** a completed Ideal Customer Profile (ICP) and account dataset.

The repository includes a **synthetic completed ICP example** so the capstone workflow can be executed end-to-end. In production, TargetOrate should replace that example with the relevant client's completed ICP.

## Repository Structure

- `FIOR_Scoring_Rubric_10_02_2026.md` — official 14-criterion anchored FIOR scoring rules.
- `MASTER_PROMPT.md` — master execution instructions, source hierarchy, validation, scoring, and output requirements.
- `Client_Target_Reference_Lists.md` — TargetOrate-level product, expansion, strategic-value, win-rate, and baseline reference parameters.
- `data/Criteria_Ranking_Model.csv` — 1–20 data-importance hierarchy used for data-gap severity and review priority.
- `examples/TargetOrate_Completed_ICP_Example.xlsx` — completed **synthetic** ICP demonstrating the required client input.
- `20_Company_Dataset_Week5_MVP.csv` — synthetic 20-company test dataset.

## Source-of-Truth Hierarchy

When information overlaps, use:

**FIOR Rubric → Completed Client ICP → Client Target Reference Lists → Account Dataset → No Unsupported Assumptions**

The rubric governs *how* to score. The ICP defines *what a good-fit client account looks like*. The reference lists provide TargetOrate-specific product and benchmark context. The account dataset supplies evidence about each candidate.

## How to Run the System

1. Load this repository into the enterprise LLM.
2. Upload the candidate account dataset.
3. Ensure a completed client ICP is available. For the capstone test, use `examples/TargetOrate_Completed_ICP_Example.xlsx`.
4. Run:

> *"Using the instructions in MASTER_PROMPT.md, the FIOR rubric, the completed ICP, the client reference lists, and the ranking model in this repository, evaluate all accounts in the attached dataset and output the final scored ABM portfolio table."*

## Input Validation

Before scoring, the workflow validates that the ICP contains the client-specific benchmarks needed for FIOR Fit Criteria 1–4, including:

- target industries and sub-industries;
- employee and revenue ranges;
- required/preferred/incompatible technology definitions;
- served geographies; and
- compliance requirements.

If a required ICP benchmark is missing, the workflow does **not** reverse-engineer the answer from the account dataset. The affected criterion is returned as `NS` and routed for consultant review. If the ICP itself is missing, the workflow stops before producing final portfolio scores and tiers.

## Missing-Data Principle

A blank field is **not** a negative signal. The FIOR rubric's missing-data rule is authoritative: missing evidence is returned as `NS` where required. The Criteria Ranking Model determines the severity and review priority of the gap; it does not authorize the model to invent or automatically penalize missing facts.

## Capstone Example vs. Production Use

The included ICP and 20-company dataset are synthetic operational test inputs. They are designed to validate consistency, differentiation, auditability, and human-in-the-loop review.

For production use, TargetOrate should:

1. replace the example ICP with the client's completed ICP;
2. replace the synthetic account dataset with current client/account data;
3. maintain dated intent, trigger, relationship, and role-verification evidence;
4. validate client-specific ICP definitions before scoring; and
5. retain consultant review for rubric-defined anomalies and strategic outliers.

The FIOR rubric should remain stable unless TargetOrate intentionally changes its scoring methodology.
