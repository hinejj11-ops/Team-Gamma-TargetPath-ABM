# MVP v1.1 Blind Scoring Run Provenance

**Status:** Provisional. No consultant approval was obtained. This records the provenance of a blind first run of the 20 account Iteration 7 dataset, as required by step 4 of `validation/MVP_v1_1_Integration_Test_Plan.md`.

## Run provenance

| Item | Value |
|---|---|
| Run date | 2026-10-12 |
| Scoring As Of Date | 2026-10-11 (the date the test plan specifies for the Iteration 7 fixtures) |
| Repository | `hinejj11-ops/Team-Gamma-TargetPath-ABM` |
| Branch and commit | `1.1-integration` at `5933b44235a47ed9506160613b5f32802cb46c3d` (merge of PR #19) |
| AI model (configured identifier) | `claude-sonnet-5-5` |
| Model version caveat | The session configuration names this model, but the model that served each turn can differ and can change mid session. The exact serving model was not verifiable from inside the session. Treat the identifier as configured, not confirmed. |
| Interface | Claude Code on the Claude Agent SDK, in a cloud container |
| Code execution | Python 3.13.16 for roll up math, gate logic and cross checks |
| Run operator | Jonas (Team Gamma), executed by the AI at his request |
| Human approval | None. Every result is labeled PROVISIONAL. |

## Input hashes (SHA 256)

Files read and used during the run:

| File | SHA 256 |
|---|---|
| `data/20_Company_Dataset_Iteration7.csv` | `5887851af6c516ec4bd726747cbe7002c0cd9871f0fd2b9f9dd61a931c8ee4c4` |
| `MASTER_PROMPT.md` | `32d1a9cd81c40e5f9a53a98614d8952ed815dd51dc439b4264f276683bcdb92b` |
| `FIOR_Scoring_Rubric_10_2_2026.md` | `af82af8b371d2052a00ff7903a3a49cb7cb6f736ea0c8c0bac9a5a9e07d9d14e` |
| `Client_Target_Reference_Lists.md` | `956fa59d8a1b2681b3ff77b8c15d84f1cc882c86b7ca1c244490ef9bc5dd2dee` |
| `examples/TargetOrate_Completed_ICP_Example.md` | `70d4f6dd88f049a06cc862590272d32b5341c04469363e6e7d3704f9988dbcef` |
| `data/Criteria_Ranking_Model.csv` | `a55ce7be787cd4569b9487fda96ef6583eb6316f394dff04acb10dddb26f2aee` |
| `data/FIOR_Data_Requirements_Matrix.csv` | `78ddc8fd6eeb5da20b637bbe116aace7ff55ceecfa013c201d1f0fb1074cd8fa` |
| `prompts/01_Input_Validation_Prompt.md` | `9cf37ab8c9180c4263f1545d451c916f487f8262de184cd6579425a6d56c4f18` |
| `prompts/06_Criterion_Self_Review_Prompt.md` | `c6aadaa6282280b0e370c112d0e093ebb03d698c9cfadeffd843062373eec5d2` |

`tools/split_ground_truth.py` was read but not executed, because the dataset has no ground truth column.

Also read: `README.md`, `workflow/TargetPath_Workflow_Instructions.md`, `validation/MVP_v1_1_Integration_Test_Plan.md`, `templates/ABM_Portfolio_Output_Template.csv`, and `data/Incumbent_Vendor_Events_Reference.csv` (empty, no vendor events populated).

Present at this commit but not read during the run: `prompts/02` to `05` and `07`, `workflow/Competitive_Lock_Gate_Open_Items.md`, `workflow/Vendor_Event_Intelligence.md`, `workflow/Human_Approval_Instructions.md`, `workflow/Quality_Control_Checklist.md`, all templates other than the portfolio output template, and the contents of `validation/` other than the test plan. Scoring followed `MASTER_PROMPT.md` and the rubric, which the README names as authoritative over the prompt modules.

## Blind run controls

- No file under `validation/` was opened for scoring or comparison.
- The dataset contains no `Ground Truth` column, so no split was needed.
- The `ICP Qualified` label was not used as evidence for C1 to C4.
- No answer key was compared against the results.
