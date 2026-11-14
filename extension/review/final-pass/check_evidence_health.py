#!/usr/bin/env python3
"""Check the published evidence's current source/log bindings without rerunning proofs.

Deterministic and offline: identical repository bytes produce identical reports.
Passing means that the selected records are internally consistent with current
files. It is not a new Lean kernel run, authentication of the records, a complete
manuscript audit, or an upgrade of the blocked upstream verification status.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import tomllib

LOCAL = "extension/lean/final-verification/verification.json"
CRYPTO = "extension/crypto/verification.json"
UPSTREAM = "extension/review/final-pass/upstream-build-current.json"
HISTORICAL = "extension/review/navier-stokes/final-pass-upstream-recheck.json"
HERE = "extension/review/final-pass"
FOUNDATIONS = {"propext", "Classical.choice", "Quot.sound"}
ENDPOINTS = {
    "NavierStokes.Comparator.navier_stokes_breakdown_R3",
    "NavierStokes.Comparator.navier_stokes_breakdown_periodic",
}
SUCCESS = {"passed", "verified", "completed"}
BLOCKED_STATUS = "fresh_source_audit_passed; fresh_final_kernel_build_not_completed"
VERIFIED_STATUS = "fresh_source_audit_and_final_kernel_build_passed"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_axioms(log: str) -> dict[str, list[str]]:
    result = {}
    for name, values in re.findall(r"'([^']+)' depends on axioms: \[([^]]*)\]", log):
        value = sorted(x.strip() for x in values.split(",") if x.strip())
        if name in result and result[name] != value:
            raise ValueError(f"conflicting axiom output for {name}")
        result[name] = value
    for name in re.findall(r"'([^']+)' does not depend on any axioms", log):
        if name in result and result[name]:
            raise ValueError(f"conflicting axiom output for {name}")
        result[name] = []
    return result


def audit(root: Path, overrides: dict[str, bytes] | None = None) -> dict:
    overrides = overrides or {}
    inputs, failures = {}, []
    checks = 0
    summary = {"local_finite_declarations": 0, "crypto_tests": 0,
               "upstream_final_kernel_verified": False}

    def check(condition: bool, code: str, detail: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            failures.append({"code": code, "detail": detail})

    def read(name: str) -> bytes:
        p = PurePosixPath(name)
        if p.is_absolute() or ".." in p.parts:
            raise ValueError(f"evidence path must stay relative to repository: {name}")
        name = str(p)
        target = (root / name).resolve()
        if not target.is_relative_to(root.resolve()):
            raise ValueError(f"evidence symlink leaves repository: {name}")
        data = overrides[name] if name in overrides else target.read_bytes()
        inputs[name] = sha(data)
        return data

    def obj(name: str) -> dict:
        value = json.loads(read(name))
        if not isinstance(value, dict):
            raise ValueError(f"expected JSON object in {name}")
        return value

    def bind(name: str, expected: str, code: str) -> bytes:
        data = read(name)
        check(isinstance(expected, str) and sha(data) == expected, code, name)
        return data

    try:
        local = obj(LOCAL)
        config = tomllib.loads(read("extension/lean/lakefile.toml").decode())
        toolchain = read("extension/lean/lean-toolchain").decode().strip().rsplit(":v", 1)[-1]
        bind("extension/lean/verify_all.py", local["checker_sha256"], "local.checker_hash")
        bind("extension/lean/lakefile.toml", local["lakefile_sha256"], "local.lakefile_hash")
        mathlib = next(x["rev"] for x in config["require"] if x["name"] == "mathlib")
        check(local["mathlib_commit"] == mathlib, "local.mathlib_pin", "manifest versus Lake pin")
        check(f"version {toolchain}," in local["lean_version"], "local.lean_pin", "compiler versus toolchain")
        check(local["status"] == "verified" and local["mathlib_tracked_files_clean"] is True,
              "local.status", "successful local elaboration with clean pinned mathlib required")
        check(local.get("upstream_continuum_build_performed") is False,
              "local.scope", "finite modules must not certify the upstream continuum theorem")
        modules = local["modules"]
        names = [m["module"] for m in modules]
        targets = set(config["defaultTargets"])
        check(len(names) == len(set(names)) == local["module_count"] and set(names) == targets,
              "local.module_inventory", "unique exact Lake default-target coverage required")
        declarations = []
        for m in modules:
            check(m["source"] == f"extension/lean/{m['module']}.lean",
                  "local.source_path", m["module"])
            bind(m["source"], m["source_sha256"], "local.source_hash")
            log = bind(str(PurePosixPath(LOCAL).parent / m["log"]), m["log_sha256"],
                       "local.log_hash").decode()
            check(m["status"] == "verified" and m["exit_code"] == 0
                  and m["source_unchanged_during_check"] is True,
                  "local.module_status", m["module"])
            actual = parse_axioms(log)
            recorded = m["axioms_per_declaration"]
            declared = m["declarations"]
            check(len(declared) == len(set(declared)) == m["declaration_count"],
                  "local.declaration_count", m["module"])
            check(set(actual) == set(recorded) == set(declared) and actual == recorded,
                  "local.axiom_log", m["module"])
            check(not m["unexpected_axioms"] and all(set(a) <= FOUNDATIONS for a in recorded.values()),
                  "local.axiom_boundary", m["module"])
            declarations.extend(declared)
        check(len(declarations) == len(set(declarations)) == local["declaration_count"],
              "local.total_declarations", "exact unique declaration count")
        summary["local_finite_declarations"] = len(declarations)

        crypto = obj(CRYPTO)
        check(crypto["status"] == "passed" and crypto["tests_run"] > 0
              and crypto["failures"] == crypto["errors"] == crypto["skipped"] == 0,
              "crypto.status", "all reported functional checks must have run and passed")
        for name, digest in crypto["source_sha256"].items():
            bind("extension/crypto/" + name, digest, "crypto.source_hash")
        bind("extension/crypto/verification.log", crypto["log_sha256"], "crypto.log_hash")
        summary["crypto_tests"] = crypto["tests_run"]

        upstream = obj(UPSTREAM)
        evidence = upstream["evidence"]
        source = json.loads(bind(HERE + "/" + evidence["source_audit_file"],
                                 evidence["source_audit_sha256"], "upstream.source_audit_hash"))
        cache_log = bind(HERE + "/" + evidence["cache_log_file"],
                         evidence["cache_log_sha256"], "upstream.cache_log_hash")
        check(sha(cache_log) == upstream["cache_attempt"]["log_sha256"],
              "upstream.cache_log_reference", "cache attempt and evidence must bind the same log")
        check(source["revision"] == upstream["upstream"]["revision"]
              and source["tree"] == upstream["upstream"]["tree"],
              "upstream.source_identity", "source audit and build record identities")
        check(set(upstream["theorems"]) == ENDPOINTS, "upstream.endpoints", "both exact Clay adapters")
        check(source["tracked_tree_clean_after"] is True
              and source["challenge_module_in_solution_closure"] is False
              and all(d["matches_manifest"] is True and d["rev"] == d["local_head"]
                      for d in source["dependencies"]),
              "upstream.source_provenance", "clean pinned solution closure without challenge imports")
        status = upstream["status"]
        build = upstream["full_target_build"]
        kernel_claimed = status in SUCCESS or status == VERIFIED_STATUS or build["status"] in SUCCESS
        if kernel_claimed:
            check(build["status"] in SUCCESS and build.get("exit_code") == 0
                  and build.get("target") == "NavierStokes.ComparatorSolution",
                  "upstream.success_without_endpoint", "successful exact endpoint build required")
            if all(key in build for key in ["log", "log_sha256", "axioms_per_declaration"]):
                log = bind(HERE + "/" + build["log"], build["log_sha256"], "upstream.endpoint_log_hash")
                axioms = parse_axioms(log.decode())
                check(ENDPOINTS <= set(axioms)
                      and {n: axioms.get(n) for n in ENDPOINTS} == build["axioms_per_declaration"]
                      and all(set(axioms.get(n, [])) <= FOUNDATIONS for n in ENDPOINTS),
                      "upstream.endpoint_axioms", "both actual endpoint axiom outputs required")
            else:
                check(False, "upstream.endpoint_evidence_missing", "build log, digest and endpoint axiom map required")
            check(status == VERIFIED_STATUS, "upstream.success_status", "explicit final-kernel status required")
            summary["upstream_final_kernel_verified"] = not any(
                f["code"].startswith("upstream.") for f in failures)
        else:
            check(status == BLOCKED_STATUS and build["status"] == "not_run_after_incomplete_cache",
                  "upstream.blocked_status", "explicit incomplete-build status required")
            check(upstream["cache_observations"]["source_cache_complete"] is False
                  and upstream["cache_attempt"]["exit_code"] != 0,
                  "upstream.blocker", "incomplete cache and unsuccessful process are recorded")
        check(upstream["independent_comparator"]["status"] == "not_run",
              "upstream.comparator_boundary", "this checker has no independent Comparator certificate schema")

        historical = obj(HISTORICAL)
        check(historical.get("terminal") is True and historical["status"] != "running",
              "history.terminal", "a start-only historical record cannot remain an active success signal")
        check(historical.get("superseded_by") == UPSTREAM
              and historical.get("superseding_evidence_sha256") == inputs[UPSTREAM],
              "history.superseding_hash", "historical record must bind the explicit newer outcome")
        check(historical["source_revision"] == upstream["upstream"]["revision"],
              "history.revision", "same upstream source revision")
        if not summary["upstream_final_kernel_verified"]:
            check(historical.get("fresh_final_kernel_verified") is False,
                  "history.no_false_success", "blocked upstream status cannot be promoted by older evidence")
        read(HERE + "/check_evidence_health.py")
    except (OSError, ValueError, KeyError, TypeError, StopIteration) as error:
        check(False, "evidence.unreadable_or_malformed", str(error))
    return {"schema_version": 1, "status": "passed" if not failures else "failed",
            "checks_run": checks, "summary": summary, "failures": failures,
            "input_sha256": dict(sorted(inputs.items())),
            "scope": "Offline integrity and consistency check of selected current evidence. No Lean rerun, cryptographic security proof, record authenticity guarantee, or continuum proof verification is performed."}


def negative_controls(root: Path) -> list[dict]:
    local = json.loads((root / LOCAL).read_text())
    upstream = json.loads((root / UPSTREAM).read_text())
    historical = json.loads((root / HISTORICAL).read_text())
    cases = []

    def changed(name: str, value: dict) -> bytes:
        return json.dumps(value).encode()

    first = local["modules"][0]
    src, log = first["source"], str(PurePosixPath(LOCAL).parent / first["log"])
    cases += [("changed_Lean_source", {src: (root / src).read_bytes() + b"\n-- changed\n"}, "local.source_hash"),
              ("changed_Lean_log", {log: (root / log).read_bytes() + b"\nchanged\n"}, "local.log_hash")]
    broken = json.loads(json.dumps(local)); broken["mathlib_commit"] = "0" * 40
    cases.append(("wrong_mathlib_pin", {LOCAL: changed(LOCAL, broken)}, "local.mathlib_pin"))
    broken = json.loads(json.dumps(local))
    broken["modules"][0]["axioms_per_declaration"][first["declarations"][0]] = ["sorryAx"]
    cases.append(("unapproved_local_axiom", {LOCAL: changed(LOCAL, broken)}, "local.axiom_boundary"))
    broken = dict(historical); broken["status"] = "running"; broken["terminal"] = False
    cases.append(("stale_running_record", {HISTORICAL: changed(HISTORICAL, broken)}, "history.terminal"))
    broken = json.loads(json.dumps(upstream)); broken["status"] = "verified"
    cases.append(("source_audit_mislabeled_kernel_success", {UPSTREAM: changed(UPSTREAM, broken)},
                  "upstream.success_without_endpoint"))
    broken = json.loads(json.dumps(upstream)); broken["status"] = VERIFIED_STATUS
    broken["full_target_build"].update(status="verified", exit_code=0)
    cases.append(("missing_endpoint_log_and_axioms", {UPSTREAM: changed(UPSTREAM, broken)},
                  "upstream.endpoint_evidence_missing"))
    name = "extension/crypto/research_crypto.py"
    cases.append(("changed_crypto_source", {name: (root / name).read_bytes() + b"\n# changed\n"}, "crypto.source_hash"))
    results = []
    for name, override, code in cases:
        result = audit(root, override)
        rejected = result["status"] == "failed" and any(f["code"] == code for f in result["failures"])
        results.append({"case": name, "rejected_for_expected_reason": rejected, "expected_failure": code})
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--self-test", action="store_true", help="run in-memory tamper controls; never edit inputs")
    args = parser.parse_args()
    root = args.root.resolve()
    report = audit(root)
    if args.self_test and report["status"] == "passed":
        report["negative_controls"] = negative_controls(root)
        if not all(x["rejected_for_expected_reason"] for x in report["negative_controls"]):
            report["status"] = "failed"
    if args.output_dir:
        output = args.output_dir if args.output_dir.is_absolute() else root / args.output_dir
        output.mkdir(parents=True, exist_ok=True)
        (output / "evidence-health.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ["status", "checks_run", "summary", "failures"]}, indent=2))
    if "negative_controls" in report:
        print(f"Negative controls: {sum(x['rejected_for_expected_reason'] for x in report['negative_controls'])}/{len(report['negative_controls'])} rejected as expected")
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
