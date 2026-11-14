#!/usr/bin/env python3
"""Exercise the fresh-check acceptance policy with actual Lean compiler outputs."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

from verify_all import COMPILER_PIN, digest, evaluate_lean_output


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toolchain", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path,
                        default=Path(__file__).resolve().parent / "verifier-gate-verification")
    args = parser.parse_args()
    lean = args.toolchain.resolve() / "bin/lean"
    version = subprocess.check_output([str(lean), "--version"], text=True).strip()
    require("version 4.24.0," in version and COMPILER_PIN in version, "Unexpected compiler")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    names = ["VerificationFixture.checked"]
    policy = Path(__file__).with_name("verify_all.py")
    policy_hash = digest(policy)
    checks, invocations = [], []
    suffix = "\nend VerificationFixture\n#check VerificationFixture.checked\n#print axioms VerificationFixture.checked\n"

    def compile_fixture(label: str, body: str, strict: bool = False):
        with tempfile.TemporaryDirectory(prefix="grh-verifier-fixture-") as directory:
            source = Path(directory) / "Fixture.lean"
            source.write_text("import Lean\nnamespace VerificationFixture\n" + body + suffix)
            command = [str(lean)] + (["-DwarningAsError=true"] if strict else []) + [str(source)]
            process = subprocess.run(command, text=True, capture_output=True, timeout=60)
        log = process.stdout + process.stderr
        path = args.output_dir / (label + ".log")
        path.write_text(log)
        invocations.append({"fixture": label, "exit_code": process.returncode,
                            "warnings_as_errors": strict, "log": path.name,
                            "log_sha256": digest(path)})
        return log, process.returncode

    def expect(label, log, returncode, stable, expected):
        observed = evaluate_lean_output(names, log, returncode, stable)
        require(observed["status"] == expected, f"{label}: unexpected status {observed['status']}")
        checks.append({"name": label, "status": "passed", "observed": observed["status"]})

    good, good_exit = compile_fixture("proved", "theorem checked : True := True.intro")
    require(good_exit == 0, "Positive compiler fixture failed")
    expect("complete_kernel_evidence_accepted", good, good_exit, True, "verified")

    warning_body = 'run_cmd Lean.logWarning "intentional regression warning"\ntheorem checked : True := True.intro'
    warning, warning_exit = compile_fixture("warning", warning_body)
    require(warning_exit == 0 and "warning:" in warning,
            "Warning fixture must reproduce Lean's zero-exit warning behavior")
    expect("zero_exit_warning_rejected", warning, warning_exit, True, "failed")
    strict, strict_exit = compile_fixture("warning-strict", warning_body, strict=True)
    require(strict_exit != 0, "warningAsError did not reject the warning fixture")
    expect("compiler_warning_as_error_rejected", strict, strict_exit, True, "failed")

    admitted, admitted_exit = compile_fixture("admitted", "theorem checked : False := by sorry")
    require("sorryAx" in admitted, "The admission fixture did not expose its dependency")
    expect("admitted_dependency_rejected", admitted, admitted_exit, True, "failed")
    axiom, axiom_exit = compile_fixture("project-axiom", "axiom premise : False\ntheorem checked : False := premise")
    require(axiom_exit == 0 and "VerificationFixture.premise" in axiom,
            "The project-axiom fixture did not expose its dependency")
    expect("project_axiom_rejected", axiom, axiom_exit, True, "failed")

    without_type = re.sub(r"(?m)^VerificationFixture\.checked[^\n]*\n(?: [^\n]*\n)*", "", good)
    require(without_type != good, "Missing-type probe did not alter its fixture")
    expect("missing_type_rejected", without_type, good_exit, True, "failed")
    without_axioms = re.sub(r"(?m)^'VerificationFixture\.checked'.*\n", "", good)
    require(without_axioms != good, "Missing-axiom probe did not alter its fixture")
    expect("missing_axiom_report_rejected", without_axioms, good_exit, True, "failed")
    expect("changed_source_rejected", good, good_exit, False, "failed")
    expect("nonzero_process_exit_rejected", good, 1, True, "failed")
    require(digest(policy) == policy_hash, "Evidence policy changed during regression checks")
    report = {"schema_version": 1, "checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "status": "passed", "python_optimization": sys.flags.optimize,
              "explicit_checks_active_under_optimization": True, "lean_version": version,
              "lean_binary_sha256": digest(lean), "checker_sha256": digest(Path(__file__)),
              "evidence_policy_sha256": policy_hash, "checks": checks,
              "compiler_invocations": invocations,
              "scope": "Acceptance-policy regressions using five actual compiler invocations plus targeted omissions and failure states. Negative fixtures are temporary and are never project theorem sources. This record is not an additional mathematical theorem proof."}
    (args.output_dir / "verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "checks": len(checks),
                      "compiler_invocations": len(invocations), "python_optimization": sys.flags.optimize}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
