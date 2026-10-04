# TargetPath AI Account Scoring Workflow (Week 5/6 MVP)
**Team Gamma | Auburn University Harbert College of Business (MBA Capstone, Fall 2026)**

## Overview
This repository is an **LLM-native, one-click account scoring system** built for TargetOrate. The repository packages enterprise instructions, the **10-2-2026 FIOR Rubric**, and the **Criteria Ranking Model** so any LLM can autonomously execute the entire scoring workflow in a single conversational prompt.

## Repository Structure
- `/docs/FIOR_Scoring_Rubric_10_02_2026.md`: The official 14-criterion anchored scoring rules.
- `/data/Criteria_Ranking_Model.csv`: The 1–20 data-importance hierarchy governing missing data handling.
- `/data/CloudBridge_20_Company_Dataset_Week5_MVP.csv`: The 20-company test dataset.
- `MASTER_PROMPT.md`: The master prompt and system instructions for the LLM.

## How to Run the System (One-Click LLM Execution)
1. Load this repository into your enterprise LLM (e.g., ChatGPT Enterprise or Claude Enterprise).
2. Upload your company dataset CSV into the chat.
3. Paste the following prompt:
   > *"Execute the scoring workflow outlined in `MASTER_PROMPT.md` for the attached company dataset."*
