#!/usr/bin/env python3
"""Check inherited arithmetic/analytic proofs with existing pinned Lean tools.

No downloads or source changes. Every public theorem/lemma in the supported
source syntax receives an exact type and axiom report, including declarations
missing from older embedded print commands.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import tempfile
import time

from verify_all import COMPILER_PIN, MATHLIB_PIN, digest, evaluate_lean_output, stripped_code

REPO = Path(__file__).resolve().parents[2]
DECLARATION = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)*(?:(private)\s+)?(?:noncomputable\s+)?"
    r"(?:theorem|lemma)\s+([A-Za-z_][A-Za-z0-9_']*)\b")


def declaration_inventory(source: str) -> list[str]:
    """Resolve this corpus's namespace/section syntax; ignore comments and strings."""
    scopes: list[tuple[str, str]] = []
    result = []
    for line in stripped_code(source).splitlines():
        opening = re.match(r"^\s*(?:noncomputable\s+)?(namespace|section)(?:\s+(\S+))?\s*$", line)
        if opening:
            kind, name = opening.groups()
            if kind == "namespace" and not name:
                raise ValueError("An unnamed namespace cannot be inventoried")
            scopes.append((kind, name or ""))
            continue
        closing = re.match(r"^\s*end(?:\s+(\S+))?\s*$", line)
        if closing:
            if not scopes:
                raise ValueError("Unmatched scope closure in source inventory")
            _, name = scopes.pop()
            if closing.group(1) and closing.group(1) != name:
                raise ValueError("Named scope closure does not match its opening")
            continue
        declaration = DECLARATION.match(line)
        if declaration and not declaration.group(1):
            namespace = ".".join(name for kind, name in scopes if kind == "namespace")
            result.append((namespace + "." if namespace else "") + declaration.group(2))
    if scopes or not result or len(result) != len(set(result)):
        raise ValueError("Incomplete, empty or duplicate declaration inventory")
    return result


def default_toolchain() -> Path | None:
    if os.environ.get("GRH_LEAN_TOOLCHAIN"):
        return Path(os.environ["GRH_LEAN_TOOLCHAIN"])
    suffix = {("Linux", "x86_64"): "linux", ("Linux", "aarch64"): "linux_aarch64",
              ("Darwin", "arm64"): "darwin_aarch64", ("Darwin", "x86_64"): "darwin"}.get(
                  (platform.system(), platform.machine().lower()))
    if suffix:
        candidate = REPO / ".tools" / ("lean-4.24.0-" + suffix)
        if (candidate / "bin/lean").is_file():
            return candidate
    # An elan shim can download a compiler on invocation; require an explicit
    # existing toolchain instead of silently invoking a global shim.
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", choices=["all", "arithmetic", "analytic"], default="all")
    parser.add_argument("--toolchain", type=Path, default=default_toolchain())
    parser.add_argument("--mathlib", type=Path,
                        default=Path(os.environ.get("GRH_MATHLIB", REPO / ".tools/mathlib4-v4.24.0")))
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    if args.toolchain is None:
        parser.error("Supply --toolchain or GRH_LEAN_TOOLCHAIN for an existing Lean 4.24.0 installation")
    args.toolchain = args.toolchain.resolve()
    args.mathlib = args.mathlib.resolve()
    lean, lake = args.toolchain / "bin/lean", args.toolchain / "bin/lake"
    output = args.output_dir or REPO / "extension/lean/inherited-verification" / args.package
    output.mkdir(parents=True, exist_ok=True)
    version = subprocess.check_output([str(lean), "--version"], text=True).strip()
    if "version 4.24.0," not in version or COMPILER_PIN not in version:
        raise SystemExit("Unexpected Lean compiler version/revision")
    sources = []
    if args.package in {"all", "arithmetic"}:
        sources += sorted((REPO / "lean").glob("*.lean"))
    if args.package in {"all", "analytic"}:
        sources += sorted((REPO / "lean-analytic").glob("*.lean"))
    for package in (["lean", "lean-analytic"] if args.package == "all" else
                    ["lean" if args.package == "arithmetic" else "lean-analytic"]):
        if not any(source.parent.name == package for source in sources):
            raise SystemExit("No proof sources found for requested package " + package)
    includes_analytic = args.package != "arithmetic"
    provenance = {"checker": Path(__file__), "evidence_policy": Path(__file__).with_name("verify_all.py"),
                  "lean_binary": lean}
    if includes_analytic:
        revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=args.mathlib, text=True).strip()
        dirty = subprocess.check_output(["git", "status", "--porcelain", "--untracked-files=no"],
                                        cwd=args.mathlib, text=True).strip()
        expected_manifest = REPO / "lean-analytic/mathlib-manifest.json"
        actual_manifest = args.mathlib / "lake-manifest.json"
        if revision != MATHLIB_PIN or dirty or expected_manifest.read_bytes() != actual_manifest.read_bytes():
            raise SystemExit("A clean pinned mathlib checkout and matching dependency manifest are required")
        provenance.update({"lake_binary": lake, "mathlib_manifest": actual_manifest,
                           "repository_mathlib_manifest": expected_manifest})
    hashes = {name: digest(path) for name, path in provenance.items()}

    def check(source_path: Path) -> dict:
        source_bytes = source_path.read_bytes()
        source = source_bytes.decode()
        source_hash = hashlib.sha256(source_bytes).hexdigest()
        names = declaration_inventory(source)
        code = stripped_code(source)
        if re.search(r"\b(?:sorry|admit|sorryAx|axiom|unsafe|native_decide)\b", code):
            raise ValueError("Unproved or unsafe source token: " + source_path.name)
        commands = "\n".join(f"#check {name}\n#print axioms {name}" for name in names)
        started = time.monotonic()
        with tempfile.TemporaryDirectory(prefix="grh-inherited-proof-") as temporary:
            audit = Path(temporary) / "Audit.lean"
            audit.write_text(source + "\n" + commands + "\n")
            command = [str(lean), "-DwarningAsError=true", str(audit)]
            if source_path.parent.name == "lean-analytic":
                command = [str(lake), "env", *command]
                cwd = args.mathlib
            else:
                cwd = Path(temporary)
            process = subprocess.run(command, cwd=cwd, text=True, capture_output=True, timeout=300)
        log = process.stdout + process.stderr
        stable = source_hash == digest(source_path)
        evidence = evaluate_lean_output(names, log, process.returncode, stable)
        missing_dependencies = re.findall(r"of module ([A-Za-z0-9_.]+) does not exist", log)
        if evidence["status"] == "failed" and missing_dependencies:
            evidence["status"] = "blocked_missing_dependency"
        evidence["missing_compiled_dependencies"] = sorted(set(missing_dependencies))
        log_path = output / (source_path.parent.name + "-" + source_path.stem + ".log")
        log_path.write_text(log)
        return {"source": str(source_path.relative_to(REPO)), "source_sha256": source_hash,
                "declaration_count": len(names), "declarations": names,
                "source_unchanged_during_check": stable, "exit_code": process.returncode,
                "elapsed_seconds": time.monotonic() - started,
                "log": log_path.name, "log_sha256": digest(log_path), **evidence}

    with ThreadPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(check, sources))
    names = [name for result in results for name in result["declarations"]]
    stable_provenance = all(digest(path) == hashes[name] for name, path in provenance.items())
    success = (all(result["status"] == "verified" for result in results)
               and stable_provenance and len(names) == len(set(names)))
    verified = [result for result in results if result["status"] == "verified"]
    blocked = [result for result in results if result["status"] == "blocked_missing_dependency"]
    status = ("verified" if success else "incomplete" if blocked
              and len(verified) + len(blocked) == len(results) and stable_provenance else "failed")
    report = {"schema_version": 1, "checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "status": status, "package": args.package,
              "module_count": len(results), "declaration_count": len(names),
              "verified_module_count": len(verified),
              "verified_declaration_count": sum(result["declaration_count"] for result in verified),
              "blocked_module_count": len(blocked),
              "lean_version": version, "mathlib_commit": MATHLIB_PIN if includes_analytic else None,
              "provenance_sha256": hashes, "configuration_unchanged_during_check": stable_provenance,
              "warnings_treated_as_errors": True, "modules": results,
              "scope": "Fresh elaboration of the listed inherited public theorem/lemma declarations, with exact types and foundational axiom reports. Private helper proofs are elaborated but not separately inventoried. Cached compiled imports and the pinned tools are trusted. No complete manuscript, arithmetic identification, GRH, continuum Navier-Stokes or Yang-Mills proof is asserted."}
    (output / "verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({key: report[key] for key in ["status", "package", "module_count", "declaration_count",
                                                 "verified_declaration_count", "blocked_module_count"]}, indent=2))
    for result in results:
        if result["status"] != "verified":
            print("FAILED", result["source"], "exit", result["exit_code"], "log", result["log"])
    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
