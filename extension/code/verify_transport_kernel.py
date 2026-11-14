#!/usr/bin/env python3
"""Check the transport module with the project's exact Lean/mathlib pins.

No downloads or environment changes are performed. Pass existing absolute
installation paths. The record identifies the exact checked source and
prints every theorem's type and actual axiom dependencies.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toolchain", required=True, type=Path)
    parser.add_argument("--mathlib", required=True, type=Path)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[2]
    source = repo / "extension/lean/TransportContracts.lean"
    output = args.output_dir or repo / "extension/review/final-pass"
    lean, lake = args.toolchain / "bin/lean", args.toolchain / "bin/lake"
    compiler = subprocess.check_output([str(lean), "--version"], text=True).strip()
    if "version 4.24.0," not in compiler:
        raise RuntimeError("This module is pinned to Lean 4.24.0")
    mathlib_commit = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=args.mathlib, text=True).strip()
    expected_mathlib = "f897ebcf72cd16f89ab4577d0c826cd14afaafc7"
    if mathlib_commit != expected_mathlib:
        raise RuntimeError("The mathlib checkout differs from the pinned commit")
    text = source.read_text()
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    if re.search(r"\b(sorry|admit|sorryAx)\b|^\s*(axiom|constant)\s", text, re.M):
        raise RuntimeError("Unexpected proof placeholder or assumed declaration")
    names = re.findall(r"^theorem\s+(\w+)", text, re.M)
    qualified = ["TransportContracts." + n for n in names]
    commands = "\n".join(f"#check {n}\n#print axioms {n}" for n in qualified)
    with tempfile.TemporaryDirectory(prefix="transport-kernel-") as tmp:
        audit = Path(tmp) / "Audit.lean"
        audit.write_text(text + "\n" + commands + "\n")
        run = subprocess.run([str(lake), "env", str(lean), str(audit)],
                             cwd=args.mathlib, text=True, capture_output=True)
    log = run.stdout + run.stderr
    if source_hash != hashlib.sha256(source.read_bytes()).hexdigest():
        raise RuntimeError("Source changed while the kernel was checking it")
    axiom_entries = re.findall(r"'([^']+)' depends on axioms: \[([^]]*)\]", log)
    axioms = {name: [x.strip() for x in value.split(",") if x.strip()]
              for name, value in axiom_entries}
    allowed = {"propext", "Classical.choice", "Quot.sound"}
    unexpected = {name: sorted(set(values) - allowed)
                  for name, values in axioms.items() if set(values) - allowed}
    success = run.returncode == 0 and set(axioms) == set(qualified) and not unexpected
    output.mkdir(parents=True, exist_ok=True)
    (output / "transport-kernel.log").write_text(log)
    record = {
        "status": "passed" if success else "failed",
        "exit_code": run.returncode,
        "compiler": compiler,
        "mathlib_commit": mathlib_commit,
        "source": str(source.relative_to(repo)),
        "source_sha256": source_hash,
        "declarations": qualified,
        "axioms_by_declaration": axioms,
        "unexpected_axioms": unexpected,
        "log_sha256": hashlib.sha256(log.encode()).hexdigest(),
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Fresh kernel elaboration and axiom inventory for exactly the listed finite declarations.",
    }
    (output / "transport-kernel-verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps(record, indent=2))
    if not success:
        print(log)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
