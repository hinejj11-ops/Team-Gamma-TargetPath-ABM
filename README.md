# TargetPath AI ABM Workflow Toolkit — MVP v1.0
**Team Gamma | Auburn University Harbert College of Business (MBA Capstone, Fall 2026)**

## Purpose

This repository is a **tested and documented AI ABM workflow toolkit** for TargetOrate. It operationalizes the FIOR account-scoring methodology as a reusable, human-in-the-loop workflow rather than a single prompt.

The MVP contains all 11 requested toolkit components: modular prompts, review prompts, multi-step prompt chains, quality-control checklists, workflow instructions, human approval instructions, input templates, exception-handling prompts, output templates, test scenarios and expected results, and validation prompts.

## Start Here

A new TargetOrate consultant should execute the toolkit in this order:

1. Complete `templates/Client_ICP_Input_Template.md` and populate account data using `templates/Account_Data_Input_Template.csv`. If a dataset carries a ground truth column, run `tools/split_ground_truth.py` first and score only the `_scoring` copy.
2. Read `workflow/TargetPath_Workflow_Instructions.md`.
3. Run `prompts/01_Input_Validation_Prompt.md`.
4. If the input gate permits scoring, run `prompts/02_FIOR_Scoring_Prompt.md` with `MASTER_PROMPT.md` and the scoring artifacts.
5. Run `prompts/06_Criterion_Self_Review_Prompt.md` so the AI rechecks every criterion for every account before a human sees the results.
6. Route exceptions through `prompts/04_Exception_Handling_Prompt.md`.
7. Route mandatory-review cases through `prompts/03_Consultant_Review_Prompt.md` and `workflow/Human_Approval_Instructions.md`. At the human input checkpoint (`prompts/07_Human_Input_Correction_Prompt.md`), submit corrections, supplied data, and overrides using `templates/Human_Review_Input_Template.csv`.
8. Complete `workflow/Quality_Control_Checklist.md`.
9. Publish results using the output templates.
10. When testing a workflow change, use `prompts/05_Validation_Adjudication_Prompt.md`; never expose validation assets before the blind run is locked.

## 11-Component Toolkit Map

| TargetOrate requirement | MVP artifact |
|---|---|
| Modular prompts | `prompts/01_Input_Validation_Prompt.md`, `prompts/02_FIOR_Scoring_Prompt.md` |
| Review prompts | `prompts/03_Consultant_Review_Prompt.md`; `prompts/06_Criterion_Self_Review_Prompt.md` |
| Multi-step prompt chains | `MASTER_PROMPT.md`; `workflow/TargetPath_Workflow_Instructions.md` |
| Quality-control checklists | `workflow/Quality_Control_Checklist.md` |
| Workflow instructions | `workflow/TargetPath_Workflow_Instructions.md` |
| Human approval instructions | `workflow/Human_Approval_Instructions.md`; `prompts/07_Human_Input_Correction_Prompt.md` |
| Input templates | `templates/Client_ICP_Input_Template.md`; `templates/Account_Data_Input_Template.csv`; `templates/Human_Review_Input_Template.csv` |
| Exception-handling prompts | `prompts/04_Exception_Handling_Prompt.md` |
| Output templates | `templates/ABM_Portfolio_Output_Template.csv`; `templates/Account_Summary_Card_Template.md` |
| Test scenarios & expected results | `data/20_Company_Dataset_Week6_Validation.csv`; `validation/Expected_FIOR_Results_VALIDATION_ONLY.csv`; Iteration 7 gate tests: `data/20_Company_Dataset_Iteration7.csv`, `validation/Expected_FIOR_Results_ITERATION7_GATE_DRAFT.csv`, `validation/Competitive_Lock_Gate_Test_Scenarios.md` |
| Validation prompts | `prompts/05_Validation_Adjudication_Prompt.md`; `validation/Adjudication_Log.md` |

## Authoritative Scoring Artifacts

- `MASTER_PROMPT.md` — orchestration, source hierarchy, scoring chain, review/output requirements.
- `FIOR_Scoring_Rubric_10_2_2026.md` — anchored C1-C14 scoring rules and weights.
- `Client_Target_Reference_Lists.md` — TargetOrate product, expansion, strategic-value, and historical benchmark definitions.
- `data/Criteria_Ranking_Model.csv` — evidence-category importance and review priority.
- `data/FIOR_Data_Requirements_Matrix.csv` — criterion-to-field evidence contract.
- `examples/TargetOrate_Completed_ICP_Example.md` — synthetic completed ICP.

The reusable prompt modules do not supersede these files. If wording conflicts, use the source hierarchy in `MASTER_PROMPT.md`.

## Source-of-Truth Hierarchy

**FIOR Rubric → Completed Client ICP → Client Target Reference Lists → Account Dataset → No Unsupported Assumptions**

A blank or Unknown value is not automatically negative evidence. Structured V2 fields take precedence over legacy narrative fields when both address the same concept.

## Human-in-the-Loop Control

The AI produces recommendations, evidence trails, confidence, data-gap flags, and review triggers. It does not self-approve mandatory-review cases. Before any human sees the results, the AI rechecks every criterion for every account (self review). Consultants then use the review and human-approval artifacts, including the human input checkpoint, to approve, correct data, supply missing data, override with evidence, request data, or escalate methodology ambiguity. Every correction flows back through rescoring and recomputed totals and tiers.

## Validation Boundary

Everything under `/validation/` is quarantined during normal scoring and blind test execution. Validation assets may be opened only after the independent run has been completed and locked.

The synthetic 20-company validation set uses versioned validation keys so historical and current testing are not conflated:

- `validation/Expected_FIOR_Results_ITERATION6_ORIGINAL.csv` preserves the original Iteration 6 answer key used to reproduce the historical blind benchmark.
- `validation/Expected_FIOR_Results_ADJUDICATED_WORKING.csv` preserves the post-adjudication working key for future regression testing.
- `validation/Expected_FIOR_Results_VALIDATION_ONLY.csv` is retained for backward compatibility and currently mirrors the adjudicated working key.
- `validation/Adjudication_Log.md` documents why the historical and working keys differ.
- `validation/Expected_FIOR_Results_ITERATION7_GATE_DRAFT.csv` and `validation/Competitive_Lock_Gate_Test_Scenarios.md` test the Competitive Lock Gate. They were written by Team Gamma, not by TargetOrate, so they check that the gate follows its rules and are not an independent accuracy measure. They pair with `data/20_Company_Dataset_Iteration7.csv`, which adds the Incumbent Contract Status column and replaces the old `Locked` value in Incumbent Satisfaction with `Unknown`. The Week 6 dataset is kept unchanged for the Iteration 6 keys.

Do not compare a new run to one key while reporting metrics from the other.

After each run, complete `validation/Failure_Analysis_Template.md`. For consistency across runs, follow `validation/Repeatability_Protocol.md`. The ground truth column for the Iteration 7 dataset is held in `validation/20_Company_Dataset_Iteration7_Ground_Truth.csv`, not in the scoring file.

The Iteration 6 baseline below predates the self review step. Runs that include `prompts/06_Criterion_Self_Review_Prompt.md` must label their metrics with the workflow version and report self review corrections separately from first pass results.

Iteration 6 baseline:
- Raw criterion agreement: **255/280 (91.1%)**
- Residual disagreements: **25**
- Human adjudication: **18 validation-key errors, 3 model/execution errors, 4 unresolved rubric/data ambiguities**
- Rule conformance after author adjudication, crediting confirmed key errors: **273/280 (97.5%)**
- Rule conformance after author adjudication, excluding the four unresolved ambiguities: **273/276 (98.9%)**

These two figures are not accuracy against an independent answer. Team Gamma wrote both the validation key and the corrections, so they measure how closely the output follows the rubric as the team understands it. The 91.1% raw figure is the cleaner measure of agreement with the original key. Provenance of the run (which AI, version, and date) and the committed run output are not in this repository and must be added by the team that ran it.

Tie rule note: three Iteration 6 key totals end exactly in .5 (Apex 73.5, Summit 74.5, BlueMatrix 73.5) and the key rounded some of them down. Iteration 7 rounds .5 up. No tier changes. The Iteration 6 keys are left as they were.

Raw and adjudicated metrics must be reported separately.

## Production Use

The included ICP, company dataset, expected results, and adjudication log are synthetic capstone assets. In production:

1. replace the example ICP with the client's completed ICP;
2. replace the synthetic account dataset with current client/account data;
3. keep dated evidence current;
4. preserve consultant approval for flagged cases;
5. keep validation assets quarantined;
6. change scoring methodology only through a separately tested and documented iteration; and
7. populate Incumbent Satisfaction (the target account's satisfaction with its current vendor) from TargetOrate's intent data and sales conversations, and state a Scoring As Of Date for every run. The Competitive Lock Gate open items for TargetOrate are in `workflow/Competitive_Lock_Gate_Open_Items.md`.

## MVP Acceptance Test

The toolkit qualifies as minimum viable when a new consultant can, using this README and the linked artifacts only:

- prepare and validate inputs;
- execute a blind FIOR scoring run;
- identify and handle exceptions;
- route mandatory-review items to human approval;
- publish the standard portfolio and account-summary outputs; and
- validate a test run without leaking expected results into scoring.

The cold-start MVP acceptance test is documented in `validation/MVP_v1_Acceptance_Test.md`. All 13 functional acceptance conditions passed; two minor documentation/version-control issues identified by the test are corrected in the MVP v1.0 cleanup.

**MVP v1.0 status: Accepted (Iteration 6 toolkit; the Iteration 7 additions have not been re-tested cold).** Future scoring-rule changes should be treated as post-MVP enhancements and tested as separate iterations.
