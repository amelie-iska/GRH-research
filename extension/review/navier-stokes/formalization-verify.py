#!/usr/bin/env python3
"""Recheck FluidInterfaces using the exact pinned Lean/mathlib toolchain.

The toolchain and mathlib must already be installed. No downloads, trusted
axioms, source edits, or replacement of existing theorem files are performed.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import subprocess
import time
from pathlib import Path

PIN = "f897ebcf72cd16f89ab4577d0c826cd14afaafc7"
TRUSTED = {"propext", "Classical.choice", "Quot.sound"}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    repo = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mathlib", type=Path,
                        default=repo.parent / ".tooling/mathlib4-v4.24.0")
    parser.add_argument("--toolchain", type=Path,
                        default=repo.parent / ".tooling/lean-4.24.0-linux")
    args = parser.parse_args()
    mathlib = args.mathlib.resolve()
    toolchain = args.toolchain.resolve()
    version = subprocess.check_output([str(toolchain / "bin/lean"), "--version"], text=True).strip()
    pin = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=mathlib, text=True).strip()
    if pin != PIN or "version 4.24.0" not in version:
        raise SystemExit(f"Toolchain mismatch: {version}; mathlib {pin}")
    folder = repo / "extension/lean"
    source = folder / "FluidInterfaces.lean"
    text = source.read_text()
    names = ["FluidInterfaces." + name for name in re.findall(r"^theorem (\w+)", text, re.M)]
    printed = re.findall(r"^#print axioms (\S+)", text, re.M)
    checked = re.findall(r"^#check (\S+)", text, re.M)
    if len(set(names)) != len(names) or set(names) != set(printed) or set(names) != set(checked):
        raise SystemExit("Theorem, type, and axiom inventories disagree")
    if re.search(r"\b(sorry|admit|sorryAx)\b|^\s*axiom\s", text, re.M):
        raise SystemExit("Unproved declaration or placeholder detected")
    command = [str(toolchain / "bin/lake"), "env", str(toolchain / "bin/lean"), str(source)]
    before = digest(source)
    start = time.monotonic()
    result = subprocess.run(command, cwd=mathlib, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)
    elapsed = time.monotonic() - start
    log = folder / "fluid-verification.log"
    log.write_text(result.stdout)
    axiom_rows = re.findall(r"^'([^']+)' depends on axioms: \[([^\]]*)\]$", result.stdout, re.M)
    axiom_map = {name: [x.strip() for x in values.split(",") if x.strip()]
                 for name, values in axiom_rows}
    for name in re.findall(r"^'([^']+)' does not depend on any axioms$", result.stdout, re.M):
        axiom_map[name] = []
    axiom_lines = [line for line in result.stdout.splitlines()
                   if "depends on axioms:" in line or "does not depend on any axioms" in line]
    axiom_log = folder / "fluid-axioms.log"
    axiom_log.write_text("\n".join(axiom_lines) + "\n")
    warnings = len(re.findall(r"\bwarning:", result.stdout))
    foreign_axioms = sorted(set().union(*(set(v) for v in axiom_map.values())) - TRUSTED)
    ok = (result.returncode == 0 and warnings == 0 and digest(source) == before
          and set(axiom_map) == set(names) and not foreign_axioms)
    report = {
        "source_file": source.name,
        "source_sha256": before,
        "status": "verified" if ok else "failed",
        "checked_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "lean_version": version,
        "mathlib_commit": pin,
        "command": command,
        "working_directory": str(mathlib),
        "exit_code": result.returncode,
        "elapsed_seconds": elapsed,
        "warning_count": warnings,
        "theorem_count": len(names),
        "theorems": names,
        "axioms_per_theorem": axiom_map,
        "unexpected_axioms": foreign_axioms,
        "verification_log_sha256": digest(log),
        "axiom_log_sha256": digest(axiom_log),
        "source_unchanged_during_check": digest(source) == before,
        "scope": (
            "Finite real matrix energy and actual coordinate time derivatives; orthogonal "
            "reduction and approximation; boundary-flux continuity; exact linear Schur and "
            "discrete memory elimination; strict-lower/diagonal block nilpotence; exact "
            "quadratic-order and renormalization matrix identities. The new module does "
            "not import, recheck, extend, or replace the released continuum Navier-Stokes "
            "formalization. It proves no CFD continuum convergence, mesh-uniform "
            "regularity, hydrodynamic limit, quantum advantage, or complete surface "
            "algebra reconstruction. The matrix determinant is not itself a formal "
            "proof of a covering-space degree."
        ),
    }
    (folder / "fluid-verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({key: report[key] for key in ["status", "source_sha256", "theorem_count",
                                                "exit_code", "warning_count", "elapsed_seconds"]}, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
