#!/usr/bin/env python3
"""Freshly elaborate all six finite-interface modules with exact pinned tools.

This driver makes no downloads or source changes. It captures actual theorem
types and axiom dependencies, verifies source stability during checking, and
rejects a mismatch between Lake's default targets and the audited modules.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile
import time
import tomllib

MATHLIB_PIN = "f897ebcf72cd16f89ab4577d0c826cd14afaafc7"
COMPILER_PIN = "797c613eb9b6d4ec95db23e3e00af9ac6657f24b"
FOUNDATIONS = {"propext", "Classical.choice", "Quot.sound"}
MODULES = {
    "BridgeTheorems": ("ResearchBridge", 25),
    "QuantumInterfaces": ("ResearchQuantum", 7),
    "DiagramGrammar": ("DiagramGrammar", 16),
    "FluidInterfaces": ("FluidInterfaces", 34),
    "ReductionContracts": ("ReductionContracts", 16),
    "TransportContracts": ("TransportContracts", 17),
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stripped_code(source: str) -> str:
    """Blank comments and strings while retaining line boundaries for inventory."""
    out, i, depth, string = [], 0, 0, False
    while i < len(source):
        if depth:
            if source.startswith("/-", i):
                depth += 1; out.extend("  "); i += 2
            elif source.startswith("-/", i):
                depth -= 1; out.extend("  "); i += 2
            else:
                out.append("\n" if source[i] == "\n" else " "); i += 1
        elif string:
            if source[i] == "\\":
                out.extend("  "); i += 2
            elif source[i] == '"':
                string = False; out.append(" "); i += 1
            else:
                out.append("\n" if source[i] == "\n" else " "); i += 1
        elif source.startswith("/-", i):
            depth = 1; out.extend("  "); i += 2
        elif source.startswith("--", i):
            end = source.find("\n", i)
            if end == -1: end = len(source)
            out.extend(" " * (end - i)); i = end
        elif source[i] == '"':
            string = True; out.append(" "); i += 1
        else:
            out.append(source[i]); i += 1
    if depth or string:
        raise ValueError("unterminated comment or string in inventory input")
    return "".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toolchain", type=Path, required=True)
    parser.add_argument("--mathlib", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    output_dir = args.output_dir or root / "final-verification"
    output_dir.mkdir(parents=True, exist_ok=True)
    lean, lake = args.toolchain / "bin/lean", args.toolchain / "bin/lake"
    version = subprocess.check_output([str(lean), "--version"], text=True).strip()
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=args.mathlib, text=True).strip()
    dirty = subprocess.check_output(["git", "status", "--porcelain", "--untracked-files=no"],
                                    cwd=args.mathlib, text=True).strip()
    if "version 4.24.0," not in version or COMPILER_PIN not in version:
        raise SystemExit("unexpected Lean compiler version/revision")
    if revision != MATHLIB_PIN or dirty:
        raise SystemExit("mathlib must match the pinned revision with clean tracked files")
    config = tomllib.loads((root / "lakefile.toml").read_text())
    if set(config["defaultTargets"]) != set(MODULES) or {
            lib["name"] for lib in config["lean_lib"]} != set(MODULES):
        raise SystemExit("Lake libraries/default targets differ from the checked inventory")
    if config["require"][0]["rev"] != MATHLIB_PIN:
        raise SystemExit("Lake's mathlib pin differs from the audit pin")

    def check(module: str) -> dict:
        namespace, expected_count = MODULES[module]
        source_path = root / (module + ".lean")
        source = source_path.read_text()
        source_hash = digest(source_path)
        code = stripped_code(source)
        names = [namespace + "." + name for name in re.findall(r"^theorem\s+(\w+)", code, re.M)]
        forbidden = re.findall(r"\b(?:sorry|admit|sorryAx|axiom|unsafe|native_decide)\b", code)
        if len(names) != expected_count or forbidden:
            raise ValueError(f"declaration or trust-boundary mismatch in {module}")
        commands = "\n".join(f"#check {name}\n#print axioms {name}" for name in names)
        started = time.monotonic()
        with tempfile.TemporaryDirectory(prefix="grh-proof-check-") as tmp:
            audit = Path(tmp) / "Audit.lean"
            audit.write_text(source + "\n" + commands + "\n")
            process = subprocess.run([str(lake), "env", str(lean), str(audit)],
                                     cwd=args.mathlib, text=True, capture_output=True, timeout=180)
        log = process.stdout + process.stderr
        axioms = {name: sorted(x.strip() for x in values.split(",") if x.strip())
                  for name, values in re.findall(r"'([^']+)' depends on axioms: \[([^]]*)\]", log)}
        for name in re.findall(r"'([^']+)' does not depend on any axioms", log):
            axioms[name] = []
        unexpected = {name: sorted(set(values) - FOUNDATIONS)
                      for name, values in axioms.items() if set(values) - FOUNDATIONS}
        stable = source_hash == digest(source_path)
        success = process.returncode == 0 and set(axioms) == set(names) and not unexpected and stable
        log_path = output_dir / (module + ".log")
        log_path.write_text(log)
        return {
            "module": module, "source": f"extension/lean/{module}.lean",
            "source_sha256": source_hash, "status": "verified" if success else "failed",
            "exit_code": process.returncode, "elapsed_seconds": time.monotonic() - started,
            "warning_count": len(re.findall(r"\bwarning:", log)),
            "declaration_count": len(names), "declarations": names,
            "axioms_per_declaration": axioms, "unexpected_axioms": unexpected,
            "source_unchanged_during_check": stable,
            "log": log_path.name, "log_sha256": digest(log_path),
        }

    with ThreadPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(check, MODULES))
    success = all(item["status"] == "verified" for item in results)
    report = {
        "schema_version": 1, "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "verified" if success else "failed", "module_count": len(results),
        "declaration_count": sum(item["declaration_count"] for item in results),
        "lean_version": version, "lean_binary_sha256": digest(lean),
        "mathlib_commit": revision, "mathlib_tracked_files_clean": not dirty,
        "checker_sha256": digest(Path(__file__)),
        "lakefile_sha256": digest(root / "lakefile.toml"),
        "command": "python extension/lean/verify_all.py --toolchain <pinned-toolchain> --mathlib <pinned-mathlib>",
        "modules": results,
        "scope": "Fresh elaboration, printed types and actual foundational axiom dependencies for exactly the listed finite-interface declarations. Cached compiled imports and the named Lean/mathlib toolchain are trusted. No claim of complete monograph, continuum Navier-Stokes, GRH, Yang-Mills or cryptographic implementation verification.",
        "upstream_continuum_build_performed": False,
    }
    (output_dir / "verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({key: report[key] for key in ["status", "module_count", "declaration_count"]}, indent=2))
    for item in results:
        print(item["module"], item["status"], "warnings:", item["warning_count"])
    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
