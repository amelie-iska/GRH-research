#!/usr/bin/env python3
"""Read-only provenance/source audit; optional exact-toolchain upstream build.

The source scan is evidence about text, not a theorem checker. Build status is
recorded separately. No upstream source, manifest, or toolchain file is edited.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import subprocess

EXPECTED_REVISION = "f9e8bc5b38b6e212696e8a30e3e91517af887bbd"
EXPECTED_TREE = "a503f07635f200c0f2f9c5361df1fa07f95c4741"
EXPECTED_TOOLCHAIN = "leanprover/lean4:v4.34.0-rc2"
EXPECTED_COMPILER = "6a10ac8c22beadecabdbb0919c2b50214762f91d"
EXPECTED_MATHLIB = "85e3a25e006c35636f0e53b0e9296caca2685bc0"
TARGET = "NavierStokes.ComparatorSolution"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def code_only(text: str) -> str:
    """Blank nested Lean block comments, line comments, and string literals.

    Retain line positions. This is intentionally a lexical screen rather than
    a Lean parser; final assurance comes from elaboration and kernel checking.
    """
    out = list(text)
    i, depth = 0, 0
    while i < len(text):
        if depth:
            if text.startswith("/-", i):
                out[i:i+2] = "  "; depth += 1; i += 2
            elif text.startswith("-/", i):
                out[i:i+2] = "  "; depth -= 1; i += 2
            else:
                if text[i] != "\n": out[i] = " "
                i += 1
        elif text.startswith("/-", i):
            out[i:i+2] = "  "; depth = 1; i += 2
        elif text.startswith("--", i):
            while i < len(text) and text[i] != "\n":
                out[i] = " "; i += 1
        elif text[i] == '"':
            out[i] = " "; i += 1
            while i < len(text):
                if text[i] == "\\":
                    out[i] = " "; i += 1
                    if i < len(text):
                        if text[i] != "\n": out[i] = " "
                        i += 1
                elif text[i] == '"':
                    out[i] = " "; i += 1; break
                else:
                    if text[i] != "\n": out[i] = " "
                    i += 1
        else:
            i += 1
    if depth:
        raise ValueError("Unclosed block comment in source scan")
    return "".join(out)


def imports(text: str) -> list[str]:
    result = []
    for match in re.finditer(r"^\s*(?:(?:public|private|meta)\s+)*import\s+([^\n]+)", text, re.M):
        result.extend(re.findall(r"[A-Za-z_][A-Za-z_0-9'.]*(?:\.[A-Za-z_0-9']+)*", match.group(1)))
    return result


def run_logged(argv: list[str], cwd: Path, env: dict[str, str], log: Path, timeout: int) -> dict:
    started = dt.datetime.now(dt.timezone.utc)
    with log.open("w") as handle:
        process = subprocess.Popen(argv, cwd=cwd, env=env, stdout=handle,
                                   stderr=subprocess.STDOUT, start_new_session=True)
        try:
            exit_code = process.wait(timeout=timeout)
            status = "completed"
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            process.wait()
            status, exit_code = "timeout", None
    return {"command": argv, "status": status, "exit_code": exit_code,
            "started_utc": started.isoformat(),
            "ended_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "log": str(log), "log_sha256": digest(log)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--upstream", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--toolchain", type=Path,
                        help="Exact extracted Lean distribution; no version substitution")
    parser.add_argument("--cache", action="store_true",
                        help="Request pinned mathlib cache before build; stop on failure")
    parser.add_argument("--build", action="store_true",
                        help="Actually compile final solution target (potentially expensive)")
    parser.add_argument("--comparator", action="store_true",
                        help="After successful build, run upstream Comparator configuration")
    parser.add_argument("--timeout", type=int, default=3600,
                        help="Seconds allowed per requested cache/build/Comparator process")
    args = parser.parse_args()
    root, output = args.upstream.resolve(), args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    revision = git(root, "rev-parse", "HEAD")
    tree = git(root, "rev-parse", "HEAD^{tree}")
    toolchain = (root / "lean-toolchain").read_text().strip()
    tracked = git(root, "ls-files").splitlines()
    status = git(root, "status", "--porcelain", "--untracked-files=no")
    if (revision, tree, toolchain) != (EXPECTED_REVISION, EXPECTED_TREE, EXPECTED_TOOLCHAIN):
        raise SystemExit("Revision/tree/toolchain mismatch: refusing to label this pinned verification")
    if status:
        raise SystemExit("Tracked upstream changes: refusing to verify an altered proof")
    modules = {str(Path(p).with_suffix("")).replace(os.sep, "."): root / p
               for p in tracked if p.endswith(".lean")}
    cleaned = {name: code_only(path.read_text()) for name, path in modules.items()}
    graph = {name: imports(text) for name, text in cleaned.items()}
    pending, visited, external = [TARGET], set(), set()
    while pending:
        name = pending.pop()
        if name in visited: continue
        if name not in modules:
            external.add(name); continue
        visited.add(name)
        pending.extend(graph[name])
    findings = {token: [] for token in
                ["sorry", "admit", "sorryAx", "axiom", "unsafe", "native_decide", "implemented_by"]}
    for name in sorted(visited):
        for token in findings:
            for match in re.finditer(r"(?<![\w'])" + re.escape(token) + r"(?![\w'])", cleaned[name]):
                findings[token].append({"module": name,
                                        "line": cleaned[name].count("\n", 0, match.start()) + 1})
    manifest = json.loads((root / "lake-manifest.json").read_text())
    records = []
    for package in manifest["packages"]:
        entry = {key: package.get(key) for key in ["name", "url", "rev", "inputRev"]}
        package_path = root / ".lake/packages" / package["name"]
        if (package_path / ".git").exists():
            entry["local_head"] = git(package_path, "rev-parse", "HEAD")
            entry["matches_manifest"] = entry["local_head"] == entry["rev"]
        records.append(entry)
    report = {
        "audit_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "revision": revision, "tree": tree, "tracked_tree_clean": not status,
        "toolchain": toolchain, "tracked_files": len(tracked),
        "navier_stokes_tracked_files": sum(p.startswith("NavierStokes/") for p in tracked),
        "target": TARGET, "local_import_closure_modules": len(visited),
        "local_import_closure_bytes": sum(modules[n].stat().st_size for n in visited),
        "challenge_module_in_solution_closure": any(n.startswith("ComparatorChallenges.") for n in visited),
        "closure": [{"module": n, "sha256": digest(modules[n])} for n in sorted(visited)],
        "external_imports": sorted(external), "lexical_screen": findings,
        "lexical_screen_limits": "Comment/string-aware text screen, not Lean parsing or kernel verification.",
        "dependencies": records,
        "metadata": {p: digest(root / p) for p in
                     ["lean-toolchain", "lake-manifest.json", "lakefile.toml", "formalization.yaml",
                      "ComparatorChallenges/NavierStokes.json"]},
        "build": {"status": "not_requested"},
        "comparator": {"status": "not_requested"}}
    env = os.environ.copy()
    if args.toolchain:
        env["PATH"] = str(args.toolchain.resolve() / "bin") + os.pathsep + env.get("PATH", "")
        version = subprocess.check_output(["lean", "--version"], env=env, text=True).strip()
        report["local_compiler_version"] = version
        if "version 4.34.0-rc2" not in version or EXPECTED_COMPILER not in version:
            raise SystemExit("Wrong local compiler; refusing substitution")
    if args.cache or args.build or args.comparator:
        if not args.toolchain:
            raise SystemExit("Explicit --toolchain required for execution")
        if not all(p.get("matches_manifest", True) for p in records):
            raise SystemExit("Downloaded dependency revision mismatch")
        if args.comparator and not args.build:
            raise SystemExit("--comparator requires --build in this verification run")
        proceed = True
        if args.cache:
            result = run_logged(["lake", "exe", "cache", "get"], root, env,
                                output.with_name("release-cache.log"), args.timeout)
            report["cache"] = result
            proceed = result["exit_code"] == 0
        if args.build and proceed:
            result = run_logged(["lake", "build", "+" + TARGET + ":olean"], root, env,
                                output.with_name("release-build.log"), args.timeout)
            report["build"] = result
            proceed = result["exit_code"] == 0
        elif args.build:
            report["build"] = {"status": "blocked_by_cache_failure"}
        if args.comparator and proceed:
            report["comparator"] = run_logged(
                ["lake", "exe", "comparator", "ComparatorChallenges/NavierStokes.json"],
                root, env, output.with_name("release-comparator.log"), args.timeout)
        elif args.comparator:
            report["comparator"] = {"status": "blocked_by_earlier_failure"}
    report["tracked_tree_clean_after"] = not git(root, "status", "--porcelain", "--untracked-files=no")
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"report": str(output), "local_import_closure_modules": len(visited),
                      "challenge_import": report["challenge_module_in_solution_closure"],
                      "lexical_counts": {k: len(v) for k, v in findings.items()},
                      "build": report["build"], "comparator": report["comparator"]}, indent=2))


if __name__ == "__main__":
    main()
