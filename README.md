# Team-Gamma-TargetPath-ABM
TargetPath AI Account Scoring Workflow
**Team Gamma | Auburn University Harbert College of Business (MBA Capstone, Fall 2026)**

## Overview
This repository contains Team Gamma's automated, platform-agnostic account-scoring engine built for TargetOrate. The workflow implements a strict **Human + AI Governance Model**:
1. **AI Classification Layer:** The LLM ingests account firmographics, research behavior, and intent surges, classifying each criterion against fixed rubric bands (JSON output).
2. **Deterministic Scoring Engine:** All mathematical calculations (dimension averages, weighted roll-up, 0–100 composite scores, and ABM tier assignments) are executed deterministically in Python to eliminate run-to-run drift.

## Repository Structure
- `/data`: Contains input test data (`CloudBridge_20_Company_Dataset_Week5_MVP.csv`) and output scored reports.
- `/scripts`: Contains the core Python execution engine (`fior_scoring_engine.py`).
- `/docs`: Contains official process maps, prompt templates, and executive summary cards.

## How to Run the Scoring Engine Locally
1. Ensure Python 3.8+ and pandas are installed (`pip install pandas numpy`).
2. Navigate to the repository root and run:
   ```bash
   python scripts/fior_scoring_engine.py
