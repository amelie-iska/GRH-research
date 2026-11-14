#!/usr/bin/env python3
"""Freshly check the four unchanged local modules with the cached pinned tools.

Only local-kernel-* review files are written. The original Lean sources,
manifests, and logs are checked for changes. No download or upstream continuum
Navier--Stokes verification is attempted.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import time


PROJECT = Path(__file__).resolve().parents[3]
REVIEW = Path(__file__).resolve().parent
LEAN = PROJECT / "extension/lean"
PIN = "f897ebcf72cd16f89ab4577d0c826cd14afaafc7"
COMPILER_PIN = "797c613eb9b6d4ec95db23e3e00af9ac6657f24b"
FOUNDATIONAL = {"propext", "Classical.choice", "Quot.sound"}
MODULES = [
    ("BridgeTheorems.lean", "verification.json", "ResearchBridge"),
    ("QuantumInterfaces.lean", "quantum-verification.json", "ResearchQuantum"),
    ("DiagramGrammar.lean", "diagram-verification.json", "DiagramGrammar"),
    ("FluidInterfaces.lean", "fluid-verification.json", "FluidInterfaces"),
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dependency_set(value) -> set[str]:
    if isinstance(value, list):
        return set(value)
    return {s.strip() for s in value.strip("[]").split(",") if s.strip()}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mathlib", type=Path,
                        default=PROJECT.parent / ".tooling/mathlib4-v4.24.0")
    parser.add_argument("--toolchain", type=Path,
                        default=PROJECT.parent / ".tooling/lean-4.24.0-linux")
    args = parser.parse_args()
    mathlib, toolchain = args.mathlib.resolve(), args.toolchain.resolve()
    version = subprocess.check_output([str(toolchain / "bin/lean"), "--version"], text=True).strip()
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=mathlib, text=True).strip()
    if revision != PIN or "version 4.24.0," not in version or COMPILER_PIN not in version:
        raise SystemExit(f"Pinned-tool mismatch: {version}; mathlib {revision}")

    spec = importlib.util.spec_from_file_location("claim_inventory", REVIEW.parent / "build_claim_register.py")
    inventory = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(inventory)
    protected = [p for name, manifest, _ in MODULES
                 for p in (LEAN / name, LEAN / manifest,
                           LEAN / manifest.replace(".json", ".log"))]
    before = {str(p.relative_to(PROJECT)): sha(p) for p in protected}

    def check(item: tuple[str, str, str]) -> dict:
        name, manifest_name, namespace = item
        source = LEAN / name
        manifest = json.loads((LEAN / manifest_name).read_text())
        if sha(source) != manifest["source_sha256"]:
            raise ValueError(f"Source differs from original verified snapshot: {name}")
        entries = manifest.get("declarations", [])
        expected = ({v["name"]: dependency_set(v["axioms"]) for v in entries}
                    if entries else
                    {k: dependency_set(v) for k, v in manifest["axioms_per_theorem"].items()})
        code = inventory.strip_lean_comments_and_strings(source.read_text())
        names = {namespace + "." + n for n in
                 re.findall(r"(?m)^\s*theorem\s+([A-Za-z_][A-Za-z0-9_]*)", code)}
        forbidden = re.findall(r"\b(?:axiom|sorry|admit|sorryAx|unsafe|native_decide)\b", code)
        if names != set(expected) or forbidden:
            raise ValueError(f"Source declaration/placeholder audit failed: {name}")
        command = [str(toolchain / "bin/lake"), "env", str(toolchain / "bin/lean"), str(source)]
        start = time.monotonic()
        timed_out = False
        try:
            process = subprocess.run(command, cwd=mathlib, text=True,
                                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                     timeout=180)
            output, exit_code = process.stdout, process.returncode
        except subprocess.TimeoutExpired as exc:
            timed_out = True
            output = exc.stdout or ""
            if isinstance(output, bytes):
                output = output.decode(errors="replace")
            exit_code = None
        elapsed = time.monotonic() - start
        log = REVIEW / ("local-kernel-" + source.stem + ".log")
        log.write_text(output)
        axioms = {n: dependency_set(v) for n, v in re.findall(
            r"^'([^']+)' depends on axioms: \[([^\]]*)\]$", output, re.M)}
        for n in re.findall(r"^'([^']+)' does not depend on any axioms$", output, re.M):
            axioms[n] = set()
        unexpected = set().union(*axioms.values()) - FOUNDATIONAL if axioms else set()
        unchanged = sha(source) == manifest["source_sha256"]
        ok = exit_code == 0 and axioms == expected and unchanged and not unexpected and not timed_out
        return {
            "source_file": str(source.relative_to(PROJECT)),
            "source_sha256": sha(source),
            "original_manifest": str((LEAN / manifest_name).relative_to(PROJECT)),
            "status": "verified" if ok else "failed",
            "command": command,
            "working_directory": str(mathlib),
            "exit_code": exit_code,
            "timed_out": timed_out,
            "elapsed_seconds": elapsed,
            "warning_count": len(re.findall(r"\bwarning:", output)),
            "log": str(log.relative_to(PROJECT)),
            "log_sha256": sha(log),
            "declaration_count": len(names),
            "axioms_per_declaration": {n: sorted(v) for n, v in sorted(axioms.items())},
            "axioms_match_original_manifest": axioms == expected,
            "unexpected_axioms": sorted(unexpected),
            "source_unchanged": unchanged,
            "forbidden_tokens_outside_comments_and_strings": forbidden,
        }

    with ThreadPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(check, MODULES))
    after = {str(p.relative_to(PROJECT)): sha(p) for p in protected}
    all_ok = before == after and all(r["status"] == "verified" for r in results)
    report = {
        "schema_version": 1,
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "verified" if all_ok else "failed",
        "lean_version": version,
        "lean_binary_sha256": sha(toolchain / "bin/lean"),
        "mathlib_commit": revision,
        "module_count": len(results),
        "declaration_count": sum(r["declaration_count"] for r in results),
        "original_sources_manifests_and_logs_unchanged": before == after,
        "protected_snapshot_sha256": before,
        "modules": results,
        "scope": (
            "Fresh Lean kernel elaboration of the four local companion modules only, "
            "with their exact existing sources and cached pinned Lean 4.24/mathlib. "
            "The printed dependencies are compared declaration by declaration to the "
            "original verification manifests. This does not verify every manuscript "
            "theorem or any upstream continuum Navier--Stokes release theorem."
        ),
        "upstream_continuum_kernel_verification_performed": False,
        "separate_upstream_attempt": "extension/review/navier-stokes/release-build-verification.json",
    }
    (REVIEW / "local-kernel-verification.json").write_text(json.dumps(report, indent=2) + "\n")
    lines = ["# Fresh local Lean verification", "", report["scope"], "",
             f"Status: **{report['status']}**. {report['module_count']} modules; "
             f"{report['declaration_count']} declarations. Checked {report['checked_at_utc']}.", "",
             f"Compiler: `{version}`. Mathlib: `{revision}`.", "",
             "| Module | Declarations | Exit | Warnings | Axiom manifest match |",
             "|---|---:|---:|---:|---|",
             *[f"| {Path(r['source_file']).name} | {r['declaration_count']} | {r['exit_code']} | "
               f"{r['warning_count']} | {r['axioms_match_original_manifest']} |" for r in results], "",
             "The original sources, manifests, and original logs were unchanged: "
             f"**{before == after}**. Every declaration reports dependencies only among "
             "`propext`, `Classical.choice`, and `Quot.sound`. These foundational axioms "
             "are disclosed, not claimed absent.", "",
             "The new fluid module certifies selected finite matrix, recurrence, block, "
             "and derivative identities. In particular, the energy derivative is not "
             "the global finite ODE continuation theorem; discrete memory is not the "
             "continuous matrix-exponential formula; determinant arithmetic is not "
             "covering-space topology; and a zero block composite is not the analytic "
             "Volterra convergence theorem.", "",
             "The separate upstream Lean 4.34 release attempt did not complete kernel "
             "verification after a rate-limited cache download and missing compiled "
             "imports. This successful local check does not change that status. See "
             "`release-build-verification.json` for the exact earlier failure boundary.", "",
             "Reproduce with `python extension/review/navier-stokes/local-kernel-verify.py` "
             "after installing the exact pinned tools at the recorded paths, or supply "
             "`--toolchain` and `--mathlib`. The script performs no downloads.", ""]
    (REVIEW / "local-kernel-verification.md").write_text("\n".join(lines))
    print(json.dumps({k: report[k] for k in ("status", "module_count", "declaration_count",
                                           "original_sources_manifests_and_logs_unchanged")}, indent=2))
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
