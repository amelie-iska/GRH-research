#!/usr/bin/env python3
"""Prove that assertion-based evidence generators refuse optimized Python.

Each subprocess runs an isolated copy of one verifier. Refusal must happen at
import time, with the documented diagnostic, before an evidence file is made.
This driver uses explicit conditions rather than assert, so it also works when
the parent interpreter is optimized. It tests runtime behavior, not arithmetic.
"""
from __future__ import annotations

import argparse
import ast
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile


REFUSAL = "Verification requires assertions; run without -O or PYTHONOPTIMIZE"
MODES = (
    ("flag_O", ["-O"], None, False),
    ("flag_OO", ["-OO"], None, False),
    ("env_1", [], "1", False),
    ("env_2", [], "2", False),
    ("optimized_import", ["-O"], None, True),
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_checks(source_dir: Path) -> dict:
    targets = sorted(path for path in source_dir.glob("verify_*.py")
                     if any(isinstance(node, ast.Assert)
                            for node in ast.walk(ast.parse(path.read_text()))))
    if not targets:
        raise RuntimeError("No assertion-based verifiers were found; refusing an empty check")
    before = {path.name: sha(path) for path in targets}
    checks = []
    with tempfile.TemporaryDirectory(prefix="grh-verifier-runtime-") as directory:
        root = Path(directory)
        for target in targets:
            for label, flags, optimization, import_only in MODES:
                isolated = root / target.stem / label
                script = isolated / "extension/code" / target.name
                script.parent.mkdir(parents=True)
                shutil.copyfile(target, script)
                environment = os.environ.copy()
                environment.pop("PYTHONOPTIMIZE", None)
                environment["PYTHONDONTWRITEBYTECODE"] = "1"
                if optimization is not None:
                    environment["PYTHONOPTIMIZE"] = optimization
                arguments = (["-c", "import runpy, sys; runpy.run_path(sys.argv[1], "
                               "run_name='verification_import_probe')", str(script)]
                              if import_only else [str(script)])
                run = subprocess.run([sys.executable, *flags, *arguments],
                                     cwd=isolated, env=environment, capture_output=True,
                                     text=True, timeout=20)
                files = sorted(str(path.relative_to(isolated)) for path in isolated.rglob("*")
                               if path.is_file())
                output = run.stdout + run.stderr
                passed = (run.returncode != 0 and REFUSAL in output
                          and files == ["extension/code/" + target.name]
                          and sha(script) == before[target.name])
                checks.append({"script": "extension/code/" + target.name, "mode": label,
                               "exit_code": run.returncode, "refusal_observed": REFUSAL in output,
                               "created_evidence_files": [name for name in files
                                                          if name != "extension/code/" + target.name],
                               "passed": passed})
    after = {path.name: sha(path) for path in targets}
    if after != before:
        raise RuntimeError("Verifier sources changed during the subprocess checks")
    return {"status": "passed" if all(row["passed"] for row in checks) else "failed",
            "checked_at_utc": datetime.now(timezone.utc).isoformat(),
            "python": platform.python_version(), "verifiers": len(targets),
            "checks_run": len(checks), "checks": checks,
            "source_sha256": {"extension/code/" + name: digest for name, digest in before.items()},
            "checker_sha256": sha(Path(__file__)),
            "scope": "Fail-closed subprocess behavior for assertion-dependent evidence generators; "
                     "ordinary mathematical checks are recorded separately."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parents[1]
                        / "verification/verification-runtime.json")
    args = parser.parse_args()
    report = run_checks(Path(__file__).resolve().parent)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({key: report[key] for key in ["status", "verifiers", "checks_run"]}))
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
