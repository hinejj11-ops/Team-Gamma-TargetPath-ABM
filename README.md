# TargetPath AI ABM Workflow Toolkit — MVP v1.1
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
10. When testing a workflow change, use `prompts/05_Validation_Adjudication_Prompt.md`; never open test scenario files before the run is locked.

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
| Test scenarios & example results | 20-company sample: `data/20_Company_Dataset_Iteration7.csv`; 100-company synthetic set: `data/100_Company_Dataset_Synthetic_Test.csv` (see `data/100_Company_Dataset_Synthetic_Test_README.md`), with results in `100_Company_Run_Report.md` and provenance in `100_Company_v1.1_Run_Record.md`; Competitive Lock Gate tests: `data/20_Company_Dataset_Iteration7.csv`, `validation/Expected_FIOR_Results_ITERATION7_GATE_DRAFT.csv`, `validation/Competitive_Lock_Gate_Test_Scenarios.md` |
| Validation prompts | `prompts/05_Validation_Adjudication_Prompt.md`; `validation/Run_Record_Template.md`; `validation/Failure_Analysis_Template.md` |

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

There is no answer key for this toolkit. Scoring is a judgment against the rubric and the client ICP, so results are reported from running the process, with a record of how each run was produced. A consultant reviews the output.

Files under `/validation/` are test scenarios, templates, and run documentation. They are not scoring evidence and must not be used to score accounts. Do not open the test scenario files before a test run is locked, so the run stays independent.

- `validation/Competitive_Lock_Gate_Test_Scenarios.md` and `validation/Expected_FIOR_Results_ITERATION7_GATE_DRAFT.csv` are example scenarios for the Competitive Lock Gate. Team Gamma wrote them, not TargetOrate, so they check that the gate follows its rules. They are not an independent measure of accuracy. They pair with `data/20_Company_Dataset_Iteration7.csv`, which adds the Incumbent Contract Status column.
- `validation/Run_Record_Template.md` records how a run was produced (model, inputs, hashes, as-of date, approvals). Complete one per run and do not edit it afterward.
- `validation/Failure_Analysis_Template.md` and `validation/Repeatability_Protocol.md` support review of a run and repeat runs.
- `validation/MVP_v1_Acceptance_Test.md`, `validation/MVP_v1_1_Integration_Test_Plan.md`, and `validation/MVP_v1_1_Gate_Regression_Report.md` document testing of the toolkit itself.

If a dataset carries a ground truth column, split it out with `tools/split_ground_truth.py` and score only the `_scoring` copy.

When reporting a run, state the workflow version, the model, the as-of date, the dataset, and the number of accounts routed to consultant review. Report any self review corrections separately from first pass results.

## Production Use

The included ICP, company datasets, example scenarios, and run reports are synthetic capstone assets. In production:

1. replace the example ICP with the client's completed ICP;
2. replace the synthetic account dataset with current client/account data;
3. keep dated evidence current;
4. preserve consultant approval for flagged cases;
5. keep test scenario files out of scoring runs;
6. change scoring methodology only through a separately tested and documented iteration; and
7. populate Incumbent Satisfaction (the target account's satisfaction with its current vendor) from TargetOrate's intent data and sales conversations, and state a Scoring As Of Date for every run. The Competitive Lock Gate open items for TargetOrate are in `workflow/Competitive_Lock_Gate_Open_Items.md`.

## MVP Acceptance Test

The toolkit qualifies as minimum viable when a new consultant can, using this README and the linked artifacts only:

- prepare and validate inputs;
- execute a blind FIOR scoring run;
- identify and handle exceptions;
- route mandatory-review items to human approval;
- publish the standard portfolio and account-summary outputs; and
- validate a test run without leaking test scenario files into scoring.

The cold-start MVP acceptance test is documented in `validation/MVP_v1_Acceptance_Test.md`. All 13 functional acceptance conditions passed; two minor documentation/version-control issues identified by the test are corrected in the MVP v1.0 cleanup.

**MVP v1.0 status: Accepted (Iteration 6 toolkit; the Iteration 7 additions have not been re-tested cold).** Future scoring-rule changes should be treated as post-MVP enhancements and tested as separate iterations.

## MVP v1.1 integration status
The v1.1 additions are proposed changes undergoing a new 20-account and edge-case acceptance test. Existing MVP v1.0 acceptance metrics do not establish v1.1 scoring correctness. Vendor-event evidence schema and controls are documented in `workflow/Vendor_Event_Intelligence.md`; no events are prepopulated or assumed verified. Run the 20-account test and retain approvals before proceeding to a 100-account run.
