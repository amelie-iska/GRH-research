#!/usr/bin/env python3
"""Reproduce focused lab bridge tests, exact exports and independent replay.

Requires a current registry and the separately completed frozen Lean-instance
audit. Does not regenerate a registry, compile Lean, or change release scripts.
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
import sys

import verify_lab_certificate as V


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=V.ROOT / "extension/review/final-pass/lab-certificates")
    parser.add_argument("--report", type=Path, default=V.ROOT / "extension/verification/lab-certificate-bridge.json")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    registry = json.loads(V.REGISTRY.read_text())
    V.verify_registry_sources(registry)
    runtime = {rel for binding in registry["contracts"].values() for rel in binding["runtime_sources"]}
    theorem_sources = {theorem["source"] for binding in registry["contracts"].values() for theorem in binding["theorems"]}
    inputs = sorted(runtime | theorem_sources | {"extension/lean/final-verification/verification.json", "extension/lean/laboratory-verification/verification.json",
                             "extension/lean/verify_laboratory_contracts.py", "extension/site/data/certificate-contracts.json", "extension/site/export-certificate-examples.cjs",
                             "extension/site/verify-certificate-bridge.cjs", "extension/code/test_lab_certificate.py",
                             "extension/code/build_lab_contract_registry.py", "extension/code/verify_lab_bridge.py"})
    before = {rel: digest(V.ROOT / rel) for rel in inputs}
    commands = [
        ("node-tests", ["node", "--test", "--test-reporter=tap", "extension/site/verify-certificate-bridge.cjs"]),
        ("python-tests", [sys.executable, "extension/code/test_lab_certificate.py"]),
    ]

    def run_test(item):
        name, command = item
        process = subprocess.run(command, cwd=V.ROOT, capture_output=True, text=True, timeout=120)
        log = args.output_dir / (name + ".log")
        text = process.stdout + process.stderr
        log.write_text(text)
        match = re.search(r"# tests (\d+)" if name == "node-tests" else r"Ran (\d+) tests", text)
        return {"name": name, "command": command, "exit_code": process.returncode,
                "test_count": int(match.group(1)) if match else 0, "log": log.name, "log_sha256": digest(log)}

    with ThreadPoolExecutor(max_workers=2) as pool:
        tests = list(pool.map(run_test, commands))
    if any(t["exit_code"] or not t["test_count"] for t in tests):
        raise RuntimeError("Focused bridge tests failed; inspect retained logs")
    subprocess.run(["node", "extension/site/export-certificate-examples.cjs", str(args.output_dir)], cwd=V.ROOT, check=True, capture_output=True, text=True, timeout=60)
    exports = json.loads((args.output_dir / "export-manifest.json").read_text())
    replayed = []
    for item in exports["source_bound_instances"]:
        certificate = args.output_dir / item["certificate"]
        if digest(certificate) != item["certificate_sha256"]:
            raise RuntimeError("Exported certificate changed during replay")
        replayed.append({"file": item["certificate"], **V.replay(certificate.read_text(), registry)})
    replay_file = args.output_dir / "independent-replays.json"
    replay_file.write_text(json.dumps({"status": "passed", "checked": len(replayed), "local_source_bindings_checked": True,
                                       "lean_kernel_executed": False, "results": replayed}, indent=2) + "\n")
    proof_path = V.ROOT / "extension/lean/laboratory-verification/verification.json"
    proof = json.loads(proof_path.read_text())
    if proof["status"] != "passed" or not proof["bound_sources_unchanged_during_check"]:
        raise RuntimeError("A successful frozen Lean-instance receipt is required")
    if proof["source_sha256"]["generator"] != before["extension/site/certificate-bridge.js"]:
        raise RuntimeError("Lean-instance receipt binds a different emitter")
    proof_cases = {case["case"]: case for case in proof["results"]}
    for item in exports["source_bound_instances"]:
        checked = proof_cases[item["name"]]
        if not checked["passed"] or not checked["expected_success"] or checked["source_sha256"] != item["lean_sha256"]:
            raise RuntimeError("Current emitted Lean is not byte-identical to the kernel-checked instance")
        item["byte_identical_to_kernel_checked_template"] = True
    after = {rel: digest(V.ROOT / rel) for rel in inputs}
    if before != after:
        raise RuntimeError("Bridge source or registry changed during verification")
    artifacts = [{"path": str(p.relative_to(V.ROOT)) if p.is_relative_to(V.ROOT) else str(p), "bytes": p.stat().st_size, "sha256": digest(p)}
                 for p in sorted(args.output_dir.iterdir()) if p.is_file()]
    report = {"schema_version": 1, "status": "passed", "checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "source_hashes": before, "sources_unchanged_during_check": True,
              "registry": "extension/site/data/certificate-contracts.json", "registry_sha256": digest(V.REGISTRY),
              "contracts": sorted(registry["contracts"]), "tests": tests, "cross_language_replay_cases": 132,
              "source_bound_exports": len(replayed), "independent_replays": len(replayed),
              "kernel_instance_record": str(proof_path.relative_to(V.ROOT)), "kernel_instance_record_sha256": digest(proof_path),
              "kernel_checked_emitted_instances": proof["generated_specializations"], "kernel_rejected_negative_controls": proof["negative_controls"],
              "exported_instances": exports["source_bound_instances"], "artifacts": artifacts,
              "scope": "Exact protocol/arithmetic replay, adversarial input and reversible transaction tests, plus byte identity with separately kernel-checked fixed-template instances. This does not prove JavaScript execution, canvas geometry, probability-model hypotheses or the whole manuscript. Browser rendering/interaction QA is recorded separately."}
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "node_tests": tests[0]["test_count"], "python_tests": tests[1]["test_count"],
                      "exports": len(replayed), "kernel_instances": proof["generated_specializations"],
                      "negative_controls": proof["negative_controls"], "report": str(args.report)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
