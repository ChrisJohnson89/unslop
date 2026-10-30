#!/usr/bin/env python3
"""Run retained scanner/preservation contracts and native skill integrity checks."""
from __future__ import annotations

import json
import subprocess
import sys
from _check_support import ROOT, load_contract_examples
from _assertions import check_assertion


def main() -> int:
    failures = []
    examples = 0
    predicates = 0
    for family in ("scanner-examples", "preservation-examples", "maintenance-examples"):
        rows = load_contract_examples(family)
        for row in rows:
            if family == "scanner-examples":
                command = [sys.executable, "scripts/banned_phrase_scan.py"]
            elif family == "preservation-examples":
                command = [sys.executable, "scripts/validate_preservation.py", *row["args"]]
            else:
                command = list(row["command"])
                if command[0] == "python3":
                    command[0] = sys.executable
            proc = subprocess.run(command, cwd=ROOT, input=row.get("stdin", ""),
                                  text=True, capture_output=True, timeout=30)
            assertions = [check_assertion(a, proc) for a in row["assertions"]]
            examples += 1
            predicates += len(assertions)
            if not all(ok for ok, _ in assertions):
                failures.append(row["id"])
                print(f"FAIL {row['id']}: {assertions}\n{proc.stderr}")
        print(f"Checked {family}: {len(rows)} examples", flush=True)
    print(f"Contract totals: {examples} examples, {predicates} assertions", flush=True)
    for command in (
        ["evals/check_pattern_coverage.py"],
        ["evals/check_pairs.py"],
        ["evals/check_silhouette.py", "--reference"],
        ["evals/check_silhouette.py", "--separation"],
        ["evals/check_skill_install.py"],
    ):
        proc = subprocess.run([sys.executable, *command], cwd=ROOT, timeout=60)
        if proc.returncode:
            failures.append(" ".join(command))
    scenarios = json.loads((ROOT / "evals/adversarial-evals.json").read_text())["evals"]
    print(f"Behavioral scenarios: {len(scenarios)} available; live model evaluation not run.")
    if failures:
        print("FAILED: " + ", ".join(failures), file=sys.stderr)
        return 1
    print("PASS: offline checks. This does not establish prose quality or AI authorship.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
