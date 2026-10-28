# Run Record Template

Complete one record per run of the prompt chain, before any comparison to a reference file is read. Save it with the run output and do not edit it afterward. For repeatability runs, use one record per run. Pairs with `validation/Failure_Analysis_Template.md`, which is completed after comparison and refers back to this record for its run details.

## Run provenance

| Item | Value |
|---|---|
| Run ID (for example, Run 1 of 3) | |
| Run date | |
| Scoring As Of Date | |
| Scoring dataset and number of accounts | |
| Repository | |
| Branch and commit | |
| Workflow version (for example, MVP v1.1) | |
| Rubric and prompt revision (file names and dates or versions) | |
| Competitive Lock Gate applied (Yes or No) | |
| AI model (configured identifier) | |
| Model version caveat | State whether the serving model could be confirmed. If not, say the identifier is configured, not confirmed. |
| Interface and tools | |
| Code execution used (language and version, or None) | |
| Run operator | |
| Fresh chat with no memory of earlier runs (Yes or No) | |
| Approval status | Provisional (no consultant approval), or Approved by (name and date) |

## Input hashes (SHA 256)

Hash every file the run read and used, and hash the exact files given to the AI, not copies. Record the command used so others can repeat it: `sha256sum <file>` on Mac or Linux, or `Get-FileHash <file> -Algorithm SHA256` in Windows PowerShell.

| File | SHA 256 |
|---|---|
| Scoring dataset | |
| `MASTER_PROMPT.md` | |
| FIOR scoring rubric | |
| `Client_Target_Reference_Lists.md` | |
| Completed client ICP | |
| `data/Criteria_Ranking_Model.csv` | |
| `data/FIOR_Data_Requirements_Matrix.csv` | |
| Prompt files used (one row each) | |

List files that were present at this commit but not read, and note any file that was read but not executed.

## Blind run controls

Confirm each item, or mark it as not met with a reason.

- [ ] No file under `validation/` was opened for scoring.
- [ ] The scoring dataset has no ground truth column.
- [ ] The `ICP Qualified` label was not used as evidence for C1 to C4.
- [ ] No reference file or test scenario was compared before all outputs were locked.
- [ ] No human input was accepted during the run.

## Output files

| Output | Saved file name | Locked before comparison (Yes or No) |
|---|---|---|
| C1 to C14 scores, dimensions, totals, tiers, review statuses | | |
| Self review log (corrections reported separately from first pass) | | |
| Portfolio output | | |

## Deviations and notes

List anything that departed from the protocol, such as a skipped prompt, a rerun, an interrupted session, or a model change mid session.
