# Repeatability Protocol

Repeatability is a listed test in the kickoff deck. Run this on the 100 company dataset.

1. Fix the inputs: same scoring copy of the dataset (no ground truth column), same ICP, same As Of Date, same prompt versions.
2. Run the full chain three times, each in a fresh chat with no memory of earlier runs. Record AI, model version and date for each run.
3. Save each run's criterion scores in its own file. Do not edit them.
4. Compare run to run: share of criteria with identical scores, share of totals within 1 point, share of identical tiers, and share of identical review statuses.
5. List every criterion that varies by more than 2 points between runs. These point to rubric bands that need tighter wording.
6. Report the figures with the run details. Do not compare to the key until all three runs are locked.

Suggested target (a Team Gamma proposal for TargetOrate to confirm): at least 95 percent identical tiers across runs.
