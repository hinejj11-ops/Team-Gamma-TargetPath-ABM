# TargetPath AI Account Scoring Workflow (Week 5 MVP)
**Team Gamma | Auburn University Harbert College of Business (MBA Capstone, Fall 2026)**

## Overview
This repository contains Team Gamma's automated, platform-agnostic account-scoring engine built for TargetOrate. Following our Week 5 MVP platform review, our architecture enforces a strict **Human + AI Governance Model**:
1. **AI Classification Layer (JSON):** The LLM is strictly restricted to classifying account data (firmographics, research behavior, intent surges) against fixed rubric bands (10/7/4/1), returning structured JSON with direct evidence citations.
2. **Agent Self-Check Loop:** Before scoring, the agent validates data completeness, criteria count, and rubric band formatting internally.
3. **Deterministic Python Engine:** All mathematical calculations—including dimension averages, weighted roll-ups (\(35\%\) Fit, \(25\%\) Intent, \(30\%\) Opportunity, \(10\%\) Relationship), $0–100$ composite scores, and ABM tier allocations—are executed deterministically in Python code to completely eliminate run-to-run drift and ranking instability.

## Repository Structure
- `/data`: Contains the updated Week 5 MVP test dataset (`CloudBridge_20_Company_Dataset_Week5_MVP.csv`, featuring negative disqualified cases and differentiated sub-industries) and the deterministically scored output report (`CloudBridge_20_Company_Scored_Week5_MVP.csv`).
- `/scripts`: Contains the core Python deterministic execution engine (`fior_scoring_engine.py`).
- `/docs`: Contains official process maps, prompt templates, and the updated workflow architecture draft (`FIOR_Account_Scoring_Workflow_MVP.md`).

## How to Run the Scoring Engine Locally
1. Ensure Python 3.8+ and pandas are installed:
   ```bash
   python -m pip install pandas numpy
