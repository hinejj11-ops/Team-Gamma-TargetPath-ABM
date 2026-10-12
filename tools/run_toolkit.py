#!/usr/bin/env python3
"""One-command packaging around the unchanged v1.1 provisional scorer.

This is deterministic automation, NOT an LLM second independent scoring pass.
Outputs remain provisional pending human review.
"""
import argparse
import csv
import datetime
import hashlib
import json
import pathlib
import subprocess
import sys
import tempfile
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
AS_OF = "2026-10-11"
CRITERIA = [f"C{i}" for i in range(1, 15)]


def read_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def write_csv(path, rows, fields=None):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError("Cannot write empty output")
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields or list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def validate(rows):
    if not rows:
        raise ValueError("Empty input dataset")
    names = [r.get("Company Name", "").strip() for r in rows]
    if any(not n for n in names) or len(set(names)) != len(names):
        raise ValueError("Company Name must be present and unique")
    for row in rows:
        for key in ("Industry", "Sub-Industry", "Target ACV ($)"):
            if not row.get(key, "").strip():
                raise ValueError(f"{row['Company Name']}: missing fatal field {key}")
        for key in ("Employee Count", "Annual Revenue ($M)", "Target ACV ($)"):
            try:
                float(row[key])
            except (ValueError, KeyError):
                raise ValueError(f"{row['Company Name']}: invalid numeric {key}") from None
    return list(rows[0])


def expand_to_100(rows):
    if len(rows) != 20:
        raise ValueError("Synthetic 100-company stress fixture requires 20 seed accounts")
    result = []
    for replicate in range(5):
        for row in rows:
            item = dict(row)
            item["Company Name"] = f"{row['Company Name']} [SYNTHETIC COPY {replicate + 1}]"
            if "index" in item:
                item["index"] = str(len(result) + 1)
            result.append(item)
    return result


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", default=str(ROOT / "data/20_Company_Dataset_Iteration7.csv"))
    p.add_argument("--out-dir", default="run_output")
    p.add_argument("--mode", choices=["20", "100"], default="20")
    p.add_argument("--as-of", default=AS_OF)
    args = p.parse_args()
    if args.as_of != AS_OF:
        p.error("The existing scorer fixes the scoring date to 2026-10-11. Other dates require scorer updates.")
    source = pathlib.Path(args.input)
    rows = read_csv(source)
    validate(rows)
    if args.mode == "100":
        rows = expand_to_100(rows)
    elif len(rows) != 20:
        p.error("Current underlying scorer supports 20-row fixtures only")
    out = pathlib.Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    scored, evidence = [], []
    with tempfile.TemporaryDirectory() as tmp:
        temp = pathlib.Path(tmp)
        for offset in range(0, len(rows), 20):
            batch = rows[offset:offset + 20]
            if len(batch) != 20:
                raise ValueError("Scorer batch must contain exactly 20 accounts")
            input_path = temp / f"batch_{offset}.csv"
            write_csv(input_path, batch)
            dest = temp / f"results_{offset}"
            subprocess.run([sys.executable, str(ROOT / "tools/score_v1_1.py"),
                            "--input", str(input_path), "--out-dir", str(dest)], check=True)
            scored.extend(read_csv(dest / "portfolio_PROVISIONAL.csv"))
            evidence.extend(read_csv(dest / "criterion_evidence.csv"))
    assert len(scored) == len(rows)
    assert len(evidence) == 14 * len(rows)
    assert {r["Company Name"] for r in scored} == {r["Company Name"] for r in rows}
    write_csv(out / "portfolio_PROVISIONAL.csv", scored)
    write_csv(out / "criterion_evidence.csv", evidence)
    review = []
    for r in scored:
        review.append({"Company Name": r["Company Name"], "Composite": r["Composite"],
                       "Score Implied Tier": r["Score Implied Tier"],
                       "Proposed Tier": r["Final Tier"],
                       "Review Status": r["Review Status"],
                       "Review Reasons": r["Review Reasons"],
                       "Consultant Decision": "PENDING",
                       "Consultant Rationale": "", "Reviewer": "", "Review Date": ""})
    write_csv(out / "consultant_review_queue.csv", review)
    cards = out / "account_cards"
    cards.mkdir(exist_ok=True)
    for i, r in enumerate(scored, 1):
        lines = [f"# {r['Company Name']}", "",
                 f"- Composite: {r['Composite']}",
                 f"- Score-implied tier: {r['Score Implied Tier']}",
                 f"- Proposed post-gate tier: {r['Final Tier']}",
                 f"- Approval: PROVISIONAL",
                 f"- Review reasons: {r['Review Reasons'] or 'Routine consultant approval'}", "",
                 "## Criterion evidence"]
        for e in (x for x in evidence if x["Company"] == r["Company Name"]):
            lines.append(f"- {e['Criterion']}: {e['Score']} — {e['Evidence']} ({e['Rule']})")
        (cards / f"account_{i:03d}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    audit = {"run_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
             "scoring_as_of": args.as_of, "mode": args.mode, "account_count": len(rows),
             "criterion_count": len(evidence), "input_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
             "scorer": "tools/score_v1_1.py (unchanged)",
             "independent_ai_self_review": "NOT EXECUTED",
             "human_approvals": "PENDING",
             "status": "PROVISIONAL",
             "fixture_note": "100-mode is five labeled copies of the 20 synthetic seed accounts; scale stress test only" if args.mode == "100" else "Synthetic 20-company fixture"}
    (out / "run_manifest.json").write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    qc = ["# Quality control", "", f"- [x] {len(rows)} unique accounts",
          f"- [x] {len(evidence)} criterion evidence rows",
          "- [x] All results marked PROVISIONAL",
          "- [x] Consultant review queue generated",
          "- [x] Account summary cards generated",
          "- [ ] Independent AI criterion self-review (not automated)",
          "- [ ] Consultant review and final approval (not automated)",
          "- [ ] TargetOrate production signoff (not granted)"]
    (out / "QUALITY_CONTROL.md").write_text("\n".join(qc) + "\n", encoding="utf-8")
    package = out / "targetpath_provisional_toolkit.zip"
    with zipfile.ZipFile(package, "w", zipfile.ZIP_DEFLATED) as archive:
        for file in out.rglob("*"):
            if file.is_file() and file != package:
                archive.write(file, file.relative_to(out))
    print(f"PASS: {len(rows)} accounts, {len(evidence)} criteria; packaged {package}; approvals PENDING")


if __name__ == "__main__":
    main()
