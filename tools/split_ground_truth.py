#!/usr/bin/env python3
"""Split the validation-only ground truth column out of an account dataset.

Usage: python3 tools/split_ground_truth.py INPUT.csv
Writes INPUT_scoring.csv (no ground truth column, safe to give the scoring run)
and INPUT_ground_truth.csv (company name and ground truth only, for validation/).
"""
import csv, sys, pathlib

GT = "Ground Truth ICP Qualification (Validation Only)"
src = pathlib.Path(sys.argv[1])
rows = list(csv.DictReader(src.open(encoding="utf-8-sig")))
cols = list(rows[0].keys())
if GT not in cols:
    sys.exit("No ground truth column found; nothing to split.")
keep = [c for c in cols if c != GT]
with src.with_name(src.stem + "_scoring.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=keep); w.writeheader()
    for r in rows: w.writerow({c: r[c] for c in keep})
with src.with_name(src.stem + "_ground_truth.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["Company Name", GT])
    for r in rows: w.writerow([r["Company Name"], r[GT]])
print(f"Wrote scoring copy ({len(keep)} columns) and ground truth file ({len(rows)} rows).")
