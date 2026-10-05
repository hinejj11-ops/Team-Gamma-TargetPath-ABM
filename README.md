# TargetPath AI ABM Workflow Toolkit — MVP
**Team Gamma | Auburn University Harbert College of Business (MBA Capstone, Fall 2026)**

## Purpose

This repository is a **tested and documented AI ABM workflow toolkit** for TargetOrate. It operationalizes the FIOR account-scoring methodology as a reusable, human-in-the-loop workflow rather than a single prompt.

The MVP contains all 11 requested toolkit components: modular prompts, review prompts, multi-step prompt chains, quality-control checklists, workflow instructions, human approval instructions, input templates, exception-handling prompts, output templates, test scenarios and expected results, and validation prompts.

## Start Here

A new TargetOrate consultant should execute the toolkit in this order:

1. Complete `templates/Client_ICP_Input_Template.md` and populate account data using `templates/Account_Data_Input_Template.csv`.
2. Read `workflow/TargetPath_Workflow_Instructions.md`.
3. Run `prompts/01_Input_Validation_Prompt.md`.
4. If the input gate permits scoring, run `prompts/02_FIOR_Scoring_Prompt.md` with `MASTER_PROMPT.md` and the scoring artifacts.
5. Route exceptions through `prompts/04_Exception_Handling_Prompt.md`.
6. Route mandatory-review cases through `prompts/03_Consultant_Review_Prompt.md` and `workflow/Human_Approval_Instructions.md`.
7. Complete `workflow/Quality_Control_Checklist.md`.
8. Publish results using the output templates.
9. When testing a workflow change, use `prompts/05_Validation_Adjudication_Prompt.md`; never expose validation assets before the blind run is locked.

## 11-Component Toolkit Map

| TargetOrate requirement | MVP artifact |
|---|---|
| Modular prompts | `prompts/01_Input_Validation_Prompt.md`, `prompts/02_FIOR_Scoring_Prompt.md` |
| Review prompts | `prompts/03_Consultant_Review_Prompt.md` |
| Multi-step prompt chains | `MASTER_PROMPT.md`; `workflow/TargetPath_Workflow_Instructions.md` |
| Quality-control checklists | `workflow/Quality_Control_Checklist.md` |
| Workflow instructions | `workflow/TargetPath_Workflow_Instructions.md` |
| Human approval instructions | `workflow/Human_Approval_Instructions.md` |
| Input templates | `templates/Client_ICP_Input_Template.md`; `templates/Account_Data_Input_Template.csv` |
| Exception-handling prompts | `prompts/04_Exception_Handling_Prompt.md` |
| Output templates | `templates/ABM_Portfolio_Output_Template.csv`; `templates/Account_Summary_Card_Template.md` |
| Test scenarios & expected results | `data/20_Company_Dataset_Week6_Validation.csv`; `validation/Expected_FIOR_Results_VALIDATION_ONLY.csv` |
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

The AI produces recommendations, evidence trails, confidence, data-gap flags, and review triggers. It does not self-approve mandatory-review cases. Consultants use the review and human-approval artifacts to approve, override with evidence, request data, or escalate methodology ambiguity.

## Validation Boundary

Everything under `/validation/` is quarantined during normal scoring and blind test execution. Validation assets may be opened only after the independent run has been completed and locked.

The synthetic 20-company validation set and original expected-results key preserve the reproducible blind benchmark. `validation/Adjudication_Log.md` documents the subsequent human examination of residual disagreements without rewriting historical test results.

Iteration 6 baseline:
- Raw criterion agreement: **255/280 (91.1%)**
- Residual disagreements: **25**
- Human adjudication: **18 validation-key errors, 3 model/execution errors, 4 unresolved rubric/data ambiguities**
- Adjudicated agreement crediting confirmed key errors: **273/280 (97.5%)**
- Accuracy on determinable cases excluding the four unresolved ambiguities: **273/276 (98.9%)**

Raw and adjudicated metrics must be reported separately.

## Production Use

The included ICP, company dataset, expected results, and adjudication log are synthetic capstone assets. In production:

1. replace the example ICP with the client's completed ICP;
2. replace the synthetic account dataset with current client/account data;
3. keep dated evidence current;
4. preserve consultant approval for flagged cases;
5. keep validation assets quarantined; and
6. change scoring methodology only through a separately tested and documented iteration.

## MVP Acceptance Test

The toolkit qualifies as minimum viable when a new consultant can, using this README and the linked artifacts only:

- prepare and validate inputs;
- execute a blind FIOR scoring run;
- identify and handle exceptions;
- route mandatory-review items to human approval;
- publish the standard portfolio and account-summary outputs; and
- validate a test run without leaking expected results into scoring.

The next project step is an end-to-end usability test against these acceptance conditions, not additional score tuning.
