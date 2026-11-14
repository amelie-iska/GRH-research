#!/usr/bin/env python3
"""Test evidence and formalization-scope gates in isolated temporary copies.

Checks use explicit conditional failures, so Python optimization cannot remove
them. This verifies the evidence gate's behavior; it does not invoke Lean or
replace the separately recorded kernel elaboration.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile


REPO = Path(__file__).resolve().parents[2]
GENERATOR = REPO / "extension/review/build_claim_register.py"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=REPO / "extension/lean/claim-register-gate-checks.json")
    args = parser.parse_args()
    generator_hash = digest(GENERATOR)
    spec = importlib.util.spec_from_file_location("claim_gate_review", GENERATOR)
    require(spec is not None and spec.loader is not None, "Cannot load the claim generator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    checks = []

    def expect_rejection(name, function, expected):
        try:
            function()
        except ValueError as error:
            require(expected in str(error),
                    f"{name}: rejected for an unexpected reason: {error}")
            checks.append({"name": name, "status": "passed",
                           "observed_rejection": str(error)})
        else:
            raise RuntimeError(f"{name}: invalid evidence was accepted")

    with tempfile.TemporaryDirectory(prefix="grh-claim-gate-") as directory:
        temporary = Path(directory)
        lean = temporary / "extension/lean"
        lean.mkdir(parents=True)
        for name in ["BridgeTheorems.lean", "QuantumInterfaces.lean", "DiagramGrammar.lean",
                     "FluidInterfaces.lean", "ReductionContracts.lean", "TransportContracts.lean",
                     "lakefile.toml", "lean-toolchain", "verify_all.py", "new-declarations.json"]:
            shutil.copy2(REPO / "extension/lean" / name, lean / name)
        shutil.copytree(REPO / "extension/lean/final-verification", lean / "final-verification")
        module.PROJECT, module.LEAN = temporary, lean
        _, signatures = module.lean_audit()
        require(len(signatures) == 115, "The accepted inventory must contain exactly 115 declarations")
        checks.append({"name": "current_115_declaration_manifest_accepted", "status": "passed"})

        source = lean / "TransportContracts.lean"
        original_source = source.read_bytes()
        source.write_bytes(original_source + b"\n-- stale source probe\n")
        expect_rejection("stale_source_rejected", module.lean_audit,
                         "Source/declaration/printed-type mismatch")
        source.write_bytes(original_source)

        checker = lean / "verify_all.py"
        original_checker = checker.read_bytes()
        checker.write_bytes(original_checker + b"\n# stale checker probe\n")
        expect_rejection("stale_checker_rejected", module.lean_audit,
                         "checker/toolchain/configuration provenance mismatch")
        checker.write_bytes(original_checker)

        log_path = lean / "final-verification/TransportContracts.log"
        original_log = log_path.read_text()
        log_path.write_text(original_log + "\nchanged log probe\n")
        expect_rejection("changed_log_bytes_rejected", module.lean_audit,
                         "verification log/manifest mismatch")
        log_path.write_text(original_log)

        changed = re.sub(
            r"(?m)^TransportContracts\.nonnormal_shear_gain_squared[^\n]*\n(?: [^\n]*\n)*",
            "", original_log)
        require(changed != original_log, "The printed-type removal probe did not alter its fixture")
        manifest_path = lean / "final-verification/verification.json"
        original_manifest = manifest_path.read_bytes()
        manifest = json.loads(original_manifest)
        log_path.write_text(changed)
        for entry in manifest["modules"]:
            if entry["module"] == "TransportContracts":
                entry["log_sha256"] = digest(log_path)
        manifest_path.write_text(json.dumps(manifest))
        expect_rejection("missing_exact_printed_type_rejected_even_with_updated_log_hash",
                         module.lean_audit, "Source/declaration/printed-type mismatch")
        log_path.write_text(original_log)
        manifest_path.write_bytes(original_manifest)

        map_path = lean / "new-declarations.json"
        declarations = json.loads(map_path.read_text())
        declarations["declarations"][0]["whole_manuscript_formalization_claim"] = True
        map_path.write_text(json.dumps(declarations))
        expect_rejection("whole_statement_overclaim_rejected",
                         lambda: module.merge_new_component_mappings(signatures),
                         "Stale or overclaimed")

    require(digest(GENERATOR) == generator_hash, "Claim generator changed while the gate checks ran")
    report = {
        "schema_version": 1,
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed",
        "python_optimization": sys.flags.optimize,
        "explicit_checks_active_under_optimization": True,
        "generator_sha256": generator_hash,
        "gate_checker_sha256": digest(Path(__file__)),
        "lean_manifest_sha256": digest(REPO / "extension/lean/final-verification/verification.json"),
        "checks": checks,
        "scope": "Temporary isolated copies only. These targeted rejection checks validate evidence binding and formalization-scope gates; they do not prove mathematical theorems or replace the recorded Lean run.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
