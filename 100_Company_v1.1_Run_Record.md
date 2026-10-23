# MVP v1.1 Blind Scoring Run Provenance: 100 Account Synthetic Dataset

**Status:** Provisional. No consultant approval was obtained. This records the provenance of a first run of the 100 account synthetic dataset. The run completed Steps 0 to 6 of `MASTER_PROMPT.md` and stopped at the human input checkpoint (Step 7).

## Run provenance

| Item | Value |
|---|---|
| Run date | 2026-10-22 |
| Scoring As Of Date | 2026-10-11 (chosen by the operator from two offered options; it is the date the dataset README says the fixture dates were built around) |
| Repository | `hinejj11-ops/Team-Gamma-TargetPath-ABM` |
| Branch and commit | `synthetic-100-company` at `c52b396bd3bfebc05ac2fad81edc0cf8714db69a` (shallow clone, one commit of history) |
| AI model (configured identifier) | `claude-sonnet-5-5` |
| Model version caveat | The session configuration names this model, but the model that served each turn can differ and can change mid session. The exact serving model was not verifiable from inside the session. Treat the identifier as configured, not confirmed. |
| Interface | Claude Code harness inside the Claude app, in a cloud container |
| Code execution | Python 3.13.16 for scoring, roll up math, gate logic and the independent self review |
| Run operator | Jonas (Team Gamma), executed by the AI at his request |
| Human approval | None. Every result is labeled PROVISIONAL. |

## Input hashes (SHA 256)

Files read and used during the run:

| File | SHA 256 |
|---|---|
| `data/100_Company_Dataset_Synthetic_Test.csv` | `76fae75824e73af66f40899c87272d32dbccf8b13bc57f99ec2b9bc4bec6e187` |
| `MASTER_PROMPT.md` | `32d1a9cd81c40e5f9a53a98614d8952ed815dd51dc439b4264f276683bcdb92b` |
| `FIOR_Scoring_Rubric_10_2_2026.md` | `af82af8b371d2052a00ff7903a3a49cb7cb6f736ea0c8c0bac9a5a9e07d9d14e` |
| `Client_Target_Reference_Lists.md` | `956fa59d8a1b2681b3ff77b8c15d84f1cc882c86b7ca1c244490ef9bc5dd2dee` |
| `examples/TargetOrate_Completed_ICP_Example.md` | `70d4f6dd88f049a06cc862590272d32b5341c04469363e6e7d3704f9988dbcef` |
| `data/Criteria_Ranking_Model.csv` | `a55ce7be787cd4569b9487fda96ef6583eb6316f394dff04acb10dddb26f2aee` |
| `data/FIOR_Data_Requirements_Matrix.csv` | `78ddc8fd6eeb5da20b637bbe116aace7ff55ceecfa013c201d1f0fb1074cd8fa` |
| `prompts/01_Input_Validation_Prompt.md` | `9cf37ab8c9180c4263f1545d451c916f487f8262de184cd6579425a6d56c4f18` |
| `prompts/02_FIOR_Scoring_Prompt.md` | `c5db5840bc1e2f690697933d8bac95dfcdb907fd5868207f7b86c644e0d0c906` |
| `prompts/06_Criterion_Self_Review_Prompt.md` | `c6aadaa6282280b0e370c112d0e093ebb03d698c9cfadeffd843062373eec5d2` |
| `prompts/07_Human_Input_Correction_Prompt.md` | `0fa35dd12c9801cbd3cb01ecb3f91a84286e7bf3cd142b8771ef55c579d8820a` |

Scoring programs written for this run (not part of the repository), final versions that produced the outputs:

| File | SHA 256 |
|---|---|
| `scripts/score_first_pass.py` | `bae76fba7fc16095e8e707355e28d428354b2c1032b7e92c40b882cbd4847a8e` |
| `scripts/self_review.py` | `01c8235e12bd6d2a665a2fa229e6ed553052594e61e2aef1a4ea436b0cfbb416` |
| `scripts/build_outputs.py` | `f48fc5eabb47e5e0f26f5b74f07592d3f988bf2fdf236c2405415e530a1bbecb` |

`tools/split_ground_truth.py` (`adfa38537d6ef114a3595d7b764612ad04d00f1017c24124dad615021198474c`) was read but not executed, because the dataset has no ground truth column.

Also read: `README.md` (`d64e9730162d4a92d0da8dcbe45192c6759863a418a7448b320404587c7be633`), `data/100_Company_Dataset_Synthetic_Test_README.md` (`2c3fc83d2f551d6e1bbfece46b0fc4be54e8cc30bdb2c9b9f794074331d249d4`), `workflow/TargetPath_Workflow_Instructions.md` (`f670b64cb05fa4fbc8ee5b1d2f64a555e235ca0a708f4051b3a95bcdbba8b7a7`), `workflow/Quality_Control_Checklist.md` (`7b072d096069395db79614a1e387124b2d3f7627b788e7ad08575d069af56775`), `templates/ABM_Portfolio_Output_Template.csv` (`4a20ca86fed38d13d1a499b5040d6cc1eef7f772c1bcf65a96511dea488b19b2`), and `templates/Account_Summary_Card_Template.md` (`b0ee58bbd79274e43af150c665f7bc224402d2292ae1dfac952a4621acfd9c4a`).

Present at this commit but not read during the run: `prompts/03`, `04` and `05`, `workflow/Competitive_Lock_Gate_Open_Items.md`, `workflow/Vendor_Event_Intelligence.md`, `workflow/Human_Approval_Instructions.md`, the Client ICP, Account Data and Human Review input templates, `data/Incumbent_Vendor_Events_Reference.csv` (so no vendor events were used for C8), both 20 account datasets, `examples/CloudBridge_Before_After.md`, and everything under `validation/`. Scoring followed `MASTER_PROMPT.md` and the rubric, which the README names as authoritative over the prompt modules.

## Blind run controls

- No file under `validation/` was opened for scoring or comparison.
- The dataset contains no `Ground Truth` column (54 columns, 100 rows), so no split was needed.
- The `ICP Qualified` label does not exist in this dataset and was not used as evidence for C1 to C4.
- No answer key exists for this dataset, and none was compared against the results.
- The dataset README advises against running this data against the MVP until TargetOrate adjudication is complete. The operator asked for the run, so it was executed and every result is labeled a provisional stress test of synthetic fixtures.

## Run outputs and counts

| Item | Value |
|---|---|
| Accounts in dataset | 100 |
| Held for a missing fatal field | 10 (5 blank Industry, 5 blank Target ACV) |
| Scored | 90 |
| Recommended tier after the gate | Tier 1: 5; Tier 2: 36; Tier 3: 30; Nurture: 10; Disqualified (Competitive Lock): 9 |
| Competitive Lock Gate | Applied to 55 scored accounts; 9 disqualified; 15 capped to Tier 3 |
| Review status | Review: 82; Acceptable: 8; Held: 10 |
| Review rate | 82 of 90 scored (91 percent), against a proposed 25 percent routine ceiling |
| Self review | 100 accounts, 1,400 criteria rechecked, 5 mismatches (all C9 at $250K), 0 corrections, 0 unresolved |
| Escalations | 9 accounts: 5 for the C9 edge conflict, 4 for C8 with No incumbent and Dissatisfied. No escalated reading changes a tier |
| Human input applied | None |

Deliverables: `Run_Report.md`, `ABM_Portfolio_Output.csv`, `Criterion_Audit_Trail.csv`.

## Known limitations of this record

- The self review was written by the same model as the first pass, so agreement shows internal consistency, not independent verification.
- A first version of the self review evidence check reported 38 false failures caused by a quote parsing bug on names containing an apostrophe. The checker was fixed and rerun. No score changed.
- The revenue per employee outlier fence was changed from 3 times to 1.5 times the interquartile range after the first run, because the first setting missed an obvious outlier (row 20). All outputs were regenerated from the final scripts.
- Twelve rubric interpretation calls are listed in section 6 of `Run_Report.md` for consultant confirmation.
