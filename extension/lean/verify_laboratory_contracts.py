#!/usr/bin/env python3
"""Compile actual fixed-template lab exports and reject false specializations.

The supplied directory must contain the eleven named exports produced by the
project's certificate bridge. This is a developer verification command, not a
sandbox for arbitrary Lean input. It uses existing pinned tools and fresh local
imports, performs no downloads, and creates no project .olean files.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

from verify_all import COMPILER_PIN, MATHLIB_PIN, digest, stripped_code


GENERATED = (
    "hodge-zero.lean", "hodge-third.lean", "hodge-one.lean",
    "cover-zero.lean", "cover-three.lean", "gain-0.lean", "gain-1.lean", "gain-2.lean",
    "cosmology-budget-passes.lean", "cosmology-budget-fails.lean", "cosmology-capped-one.lean",
)
IMPORTS = ("BridgeTheorems", "FluidInterfaces", "WeightedGainContracts",
           "LaboratoryContracts", "CosmologyCalibration")
PRELUDE = """import BridgeTheorems
import FluidInterfaces
import WeightedGainContracts
import LaboratoryContracts
import CosmologyCalibration
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FinCases
open Matrix
open scoped BigOperators
"""
NEGATIVE = {
    "hodge-outside-domain": """example :
    ResearchBridge.hodgeMatrix 2 0 0 1 = !![(2 : ℝ)^2, 0; 0, 1] ∧
    (∀ a b : ℝ, (2 : ℝ)^2 * (a^2+b^2) ≤ ResearchBridge.hodgeEnergy 2 0 0 1 a b) ∧
    (0 < (2 : ℝ)^2 ↔ (2 : ℝ) ≠ 0) :=
  LaboratoryContracts.hodge_family_certificate 2 (by norm_num) (by norm_num)
""",
    "hodge-zero-positive": "example : (0 : ℝ) < 0 ^ 2 := by norm_num\n",
    "cover-wrong-degree": """example :
    Matrix.det (FluidInterfaces.renormalizationMatrix ^ 3) = 2745 := by
  rw [FluidInterfaces.renormalization_power_determinant]
  norm_num
""",
    "gain-false-feasibility": """def G : Matrix (Fin 2) (Fin 2) ℚ := !![1/4, 3/2; 3/32, 1/4]
def w : Fin 2 → ℚ := ![4,1]
example : (G *ᵥ w) 0 ≤ (3/5 : ℚ) * w 0 := by
  norm_num [G, w, Matrix.mulVec, dotProduct, Fin.sum_univ_two]
""",
    "moment-false-budget": """example :
    (288 : ℝ) * 2027025 ≤ (1/20 : ℝ) * 2 ^ (2 * 8) := by norm_num
""",
    "rank-false-zero": """example : CosmologyCalibration.rankFraction 4095 0 = 0 := by
  norm_num [CosmologyCalibration.rankFraction]
""",
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toolchain", type=Path, required=True)
    parser.add_argument("--mathlib", type=Path, required=True)
    parser.add_argument("--generated-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    repo = root.parent.parent
    output = args.output_dir or root / "laboratory-verification"
    output.mkdir(parents=True, exist_ok=True)
    generated_output = output / "generated"
    generated_output.mkdir(exist_ok=True)
    lean = args.toolchain.resolve() / "bin/lean"
    lake = args.toolchain.resolve() / "bin/lake"
    mathlib = args.mathlib.resolve()
    version = subprocess.check_output([str(lean), "--version"], text=True).strip()
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=mathlib, text=True).strip()
    dirty = subprocess.check_output(["git", "status", "--porcelain", "--untracked-files=no"],
                                    cwd=mathlib, text=True).strip()
    if "version 4.24.0," not in version or COMPILER_PIN not in version:
        raise SystemExit("wrong compiler version or revision")
    if revision != MATHLIB_PIN or dirty:
        raise SystemExit("mathlib must have the clean tracked pinned source")
    manifest_path = root / "final-verification/verification.json"
    manifest = json.loads(manifest_path.read_text())
    checked = {m["module"]: m for m in manifest["modules"]}
    if manifest["status"] != "verified":
        raise SystemExit("current aggregate proof manifest is not verified")
    for module in IMPORTS:
        if checked[module]["source_sha256"] != digest(root / (module + ".lean")):
            raise SystemExit("a required theorem module differs from its verified source")
    bound_paths = {
        "checker": Path(__file__), "proof_checker": root / "verify_all.py",
        "proof_manifest": manifest_path, "lean_binary": lean, "lake_binary": lake,
        "mathlib_manifest": mathlib / "lake-manifest.json",
        "generator": repo / "extension/site/certificate-bridge.js",
        **{module: root / (module + ".lean") for module in IMPORTS},
    }
    initial_hashes = {name: digest(path) for name, path in bound_paths.items()}
    cases = []
    for name in GENERATED:
        original = args.generated_dir / name
        source = original.read_text()
        code = stripped_code(source)
        if re.search(r"\b(?:sorry|admit|axiom|unsafe|native_decide)\b|#(?:eval|run)", code):
            raise SystemExit(f"unexpected trust-boundary token in generated file: {name}")
        snapshot = generated_output / name
        snapshot.write_bytes(original.read_bytes())
        cases.append((name.removesuffix(".lean"), snapshot, True))

    build_records, results = [], []
    with tempfile.TemporaryDirectory(prefix="grh-lab-contracts-") as tmp:
        cache = Path(tmp)
        env = os.environ.copy()
        env["LEAN_PATH"] = str(cache)
        for module in IMPORTS:
            target = cache / (module + ".olean")
            process = subprocess.run(
                [str(lake), "env", str(lean), "-DwarningAsError=true", "--root=" + str(root),
                 "-o", str(target), str(root / (module + ".lean"))],
                cwd=mathlib, env=env, text=True, capture_output=True, timeout=180)
            log = process.stdout + process.stderr
            log_path = output / (module + ".import-build.log")
            log_path.write_text(log)
            passed = (process.returncode == 0 and target.is_file()
                      and not re.search(r"\bwarning:", log) and "sorryAx" not in log)
            build_records.append({"module": module, "exit_code": process.returncode,
                                  "passed": passed, "log": log_path.name,
                                  "log_sha256": digest(log_path),
                                  "olean_sha256": digest(target) if target.is_file() else None})
            if not passed:
                raise SystemExit(f"fresh local import failed: {module}")
        for name, body in NEGATIVE.items():
            path = cache / (name + ".lean")
            path.write_text(PRELUDE + body)
            cases.append((name, path, False))

        def compile_case(case: tuple[str, Path, bool]) -> dict:
            name, path, expected_success = case
            source_hash = digest(path)
            process = subprocess.run([str(lake), "env", str(lean), "-DwarningAsError=true", str(path)],
                                     cwd=mathlib, env=env, text=True, capture_output=True, timeout=180)
            log = process.stdout + process.stderr
            log_path = output / (name + ".log")
            log_path.write_text(log)
            warnings = len(re.findall(r"\bwarning:", log))
            if expected_success:
                passed = process.returncode == 0 and warnings == 0 and "sorryAx" not in log
            else:
                # The negative control must fail on the false mathematical
                # goal, not merely due to a missing import or a syntax error.
                passed = (process.returncode != 0 and "unsolved goals" in log and "⊢ False" in log
                          and "unknownIdentifier" not in log and "object file" not in log)
            stable = source_hash == digest(path)
            return {"case": name, "expected_success": expected_success,
                    "exit_code": process.returncode, "passed": passed and stable,
                    "warning_count": warnings, "source_sha256": source_hash,
                    "source_unchanged_during_check": stable,
                    "log": log_path.name, "log_sha256": digest(log_path)}

        with ThreadPoolExecutor(max_workers=2) as executor:
            results = list(executor.map(compile_case, cases))
    stable = all(digest(path) == initial_hashes[name] for name, path in bound_paths.items())
    passed = stable and all(item["passed"] for item in results)
    report = {
        "schema_version": 1, "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed" if passed else "failed", "lean_version": version,
        "mathlib_commit": revision, "source_sha256": initial_hashes,
        "bound_sources_unchanged_during_check": stable,
        "generated_specializations": len(GENERATED), "negative_controls": len(NEGATIVE),
        "checks": len(results), "fresh_local_imports": build_records, "results": results,
        "scope": "Actual fixed-template browser exports compiled under the pinned Lean kernel; six false domain/arithmetic specializations rejected. The registered generic declarations have separate complete type and foundational-axiom evidence. This does not prove JavaScript execution, the Gaussian model, calibration exchangeability, or a pseudorandom generator.",
        "additional_registered_theorem_declarations": 0,
    }
    (output / "verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ("status", "generated_specializations", "negative_controls", "checks")}))
    for result in results:
        if not result["passed"]:
            print("FAILED", result["case"], "see", output / result["log"])
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
