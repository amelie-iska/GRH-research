#!/usr/bin/env python3
"""Fail closed when selected release artifacts no longer match their sources.

This is a consistency gate for recorded evidence, not a new mathematical proof,
an authenticated attestation, or a replacement for the recorded compiler/tests.
It deliberately permits an honestly recorded incomplete upstream continuum
build. It does not permit stale local PDFs, theorem inventories, or test logs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[2]
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
PDFS = (("main", "build-verification.json", "paper.pdf", "pdf-build.json"),
        ("fluid-extension", "fluid-build-verification.json", "fluid-extension.pdf",
         "fluid-build-verification.json"))
# These are reproducible TeX working files, not manuscript source or evidence.
# Match full endings because pathlib's suffix alone loses .run.xml/.synctex.gz.
TEX_INTERMEDIATE_ENDINGS = (
    ".aux", ".bbl", ".bcf", ".blg", ".dvi", ".fdb_latexmk", ".fls",
    ".lof", ".lot", ".nav", ".out", ".run.xml", ".snm", ".synctex",
    ".synctex.gz", ".toc", ".vrb", ".xdv",
)
SITE_COPIES = {
    "extension/review/claim-register.json": "verification/claim-register.json",
    "extension/review/claim-register.md": "verification/claim-register.md",
    "extension/review/formal-type-map.json": "verification/formal-type-map.json",
    "extension/review/formal-type-map.md": "verification/formal-type-map.md",
    "extension/crypto/verification.json": "verification/crypto/verification.json",
    "extension/crypto/verification.log": "verification/crypto/verification.log",
    "extension/review/final-pass/upstream-build-current.json": "verification/final-pass/upstream-build-current.json",
    "extension/review/final-pass/upstream-build-current.md": "verification/final-pass/upstream-build-current.md",
    "extension/review/quantum-tropical-substrates-20261113.md": "verification/quantum-tropical-substrates-20261113.md",
    "extension/manuscript/quantum-tropical-substrates.bib": "verification/quantum-tropical-substrates.bib",
}
WEIGHTED_SOURCES = {
    "extension/code/verify_toric_transport.py", "extension/code/check_weighted_gain_witness.py",
    "extension/code/test_weighted_gain.py",
}
QUANTUM_SOURCES = {
    "extension/code/quantum_gain_control.py", "extension/code/verify_quantum_gain_control.py",
    "extension/code/verify_toric_transport.py", "extension/code/check_weighted_gain_witness.py",
}
WEIGHTED_CASES = {
    "accepted": (0, "certified", True), "noncontracting": (0, "certified", False),
    "rejected": (2, "rejected", False), "subnormal-exact-rejected": (2, "rejected", False),
}
QUANTUM_ARTIFACTS = {
    "trajectories.json", "path-comparison.json", "gain-accepted.json", "gain-accepted-replay.json",
    "gain-rejected.json", "gain-rejected-replay.json",
}
QUANTUM_COUNTERS = {
    "channel_parameter_cases", "choi_principal_minors", "coherent_matrix_bloch_comparisons",
    "fixed_control_distance_equalities", "controller_pair_block_bounds",
    "trajectory_state_budget_checks", "residual_one_step_block_checks", "path_horizons",
    "invalid_domain_rejections", "independent_gain_replays",
}


def digest(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def manuscript_inputs(root: Path, job: str) -> list[Path]:
    """Mirror build_pdf.py's deliberately conservative source inventory."""
    source = root / "extension/manuscript"
    result = [source / (job + ".tex"), source / "lean-listings-unicode.tex"]
    for directory, glob in ((source, "*.bib"), (root / "extension/lean", "*.lean"),
                            (source / "chapters", "*.tex"), (source / "figures", "*.pdf")):
        result.extend(sorted(directory.glob(glob)))
    return result


def excluded_credential_path(path: Path) -> bool:
    """Credential exclusions apply independently of Git tracking/ignore state."""
    return path.name.casefold() == "keys.txt" or any(
        part.casefold() == ".private-credentials" for part in path.parts)


def compact_source_files(root: Path) -> list[Path]:
    """The complete source inventory promised by the compact companion archive."""
    files = [root / name for name in ("README.md", "README-UPSTREAM.md", ".gitmodules", ".gitignore")]
    for path in (root / "extension").rglob("*"):
        rel = path.relative_to(root)
        if excluded_credential_path(rel) or any(
                part in {"__pycache__", ".texbuild", ".lake", "node_modules"} for part in rel.parts):
            continue
        if rel.parts[:3] in {("extension", "site", "legacy"), ("extension", "site", "downloads")}:
            continue
        if path.suffix in {".pyc", ".olean", ".ilean", ".aux", ".blg", ".fls"}:
            continue
        if (rel.parts[:2] == ("extension", "manuscript")
                and path.name.endswith(TEX_INTERMEDIATE_ENDINGS)):
            continue
        if rel.as_posix() in {"extension/manuscript/main.log", "extension/manuscript/fluid-extension.log"}:
            continue
        if path.is_file():
            files.append(path)
    selected = sorted(set(path for path in files if path.is_file()))
    if any(path.is_symlink() or not path.resolve().is_relative_to(root.resolve()) for path in selected):
        raise ValueError("Symlinks and paths escaping the repository are not archived")
    return selected


def lean_archive_files(root: Path) -> list[Path]:
    """Include nested verification records while excluding compiler caches."""
    source = root / "extension/lean"
    selected = sorted(p for p in source.rglob("*") if p.is_file()
                  and not excluded_credential_path(p.relative_to(source))
                  and not any(part in {".lake", "__pycache__", "node_modules"}
                              for part in p.relative_to(source).parts)
                  and p.suffix not in {".pyc", ".olean", ".ilean"})
    if any(path.is_symlink() or not path.resolve().is_relative_to(source.resolve()) for path in selected):
        raise ValueError("Symlinks and paths escaping the Lean source are not archived")
    return selected


def site_copy_map(root: Path) -> dict[str, str]:
    copies = dict(SITE_COPIES)
    # Canonical finite-computation and historical browser records already have
    # the same relative location in the site's verification directory.
    for path in (root / "extension/verification").glob("*"):
        if path.is_file() and not excluded_credential_path(path.relative_to(root)):
            copies[path.relative_to(root).as_posix()] = "verification/" + path.name
    for name in ("weighted-gain", "quantum-gain-control", "release-gate-continuation"):
        directory = root / "extension/review/final-pass" / name
        for path in sorted(directory.rglob("*")):
            if path.is_file() and not excluded_credential_path(path.relative_to(root)):
                copies[path.relative_to(root).as_posix()] = (
                    "verification/final-pass/" + name + "/" + path.relative_to(directory).as_posix())
    return copies


def check_release(root: Path = ROOT, *, site: bool = False,
                  archives: bool = False) -> dict:
    root = root.resolve()
    failures, inputs = [], {}
    checks = 0

    def require(ok: bool, code: str, path: str, detail: str = "") -> None:
        nonlocal checks
        checks += 1
        if not ok:
            failures.append({"check": code, "path": path, "detail": detail})

    def checked_path(path: Path) -> Path | None:
        resolved = path.resolve()
        if not resolved.is_relative_to(root):
            require(False, "path_outside_repository", str(path))
            return None
        return resolved

    def file_hash(path: Path) -> str | None:
        path = checked_path(path)
        if path is None:
            return None
        rel = path.relative_to(root).as_posix()
        require(path.is_file(), "required_file", rel)
        if not path.is_file():
            return None
        value = digest(path)
        inputs[rel] = value
        return value

    def match(path: Path, expected: str | None, code: str) -> bool:
        actual = file_hash(path)
        valid = bool(expected) and actual == expected
        require(valid, code,
                str(path.relative_to(root)) if path.is_relative_to(root) else str(path))
        return valid

    def read_json(path: Path) -> dict:
        if file_hash(path) is None:
            return {}
        try:
            result = json.loads(path.read_text())
            if not isinstance(result, dict):
                raise ValueError("record is not an object")
            return result
        except (ValueError, OSError) as error:
            require(False, "valid_json_object", str(path), str(error))
            return {}

    def bind_sources(record: dict, expected: set[str], label: str) -> bool:
        recorded = record.get("source_sha256", {})
        valid = isinstance(recorded, dict) and set(recorded) == expected
        require(valid, label + "_source_inventory", label)
        if not isinstance(recorded, dict):
            recorded = {}
        results = [match(root / name, recorded.get(name), label + "_source_hash")
                   for name in sorted(expected)]
        return valid and all(results)

    def bind_artifacts(directory: Path, recorded: object, expected: set[str], label: str) -> bool:
        valid = isinstance(recorded, dict) and set(recorded) == expected
        require(valid, label + "_artifact_inventory", directory.relative_to(root).as_posix())
        if not isinstance(recorded, dict):
            recorded = {}
        results = [match(directory / name, recorded.get(name), label + "_artifact_hash")
                   for name in sorted(expected)]
        return valid and all(results)

    def replay_gain(directory: Path, witness: str, replay: str,
                    outcome: tuple[int, str, bool], ready: bool) -> None:
        """Replay only the finite integer witness; expected rejections remain valid evidence."""
        expected_exit, expected_status, contraction = outcome
        recorded = read_json(directory / replay)
        require(recorded.get("status") == expected_status
                and recorded.get("bound_holds") is (expected_exit == 0)
                and recorded.get("certifies_contraction") is contraction,
                "gain_replay_record_status", replay)
        if not ready:
            return  # A source/artifact failure is already recorded; do not execute stale code.
        try:
            process = subprocess.run(
                [sys.executable, "-B", str(root / "extension/code/check_weighted_gain_witness.py"),
                 str(directory / witness)], cwd=root, text=True, capture_output=True, timeout=20)
            actual = json.loads(process.stdout)
            require(process.returncode == expected_exit and actual == recorded
                    and not process.stderr,
                    "gain_replay_matches_record", witness,
                    f"Expected exit {expected_exit}; observed {process.returncode}.")
        except (OSError, ValueError, subprocess.SubprocessError) as error:
            require(False, "gain_replay_matches_record", witness, str(error))

    source = root / "extension/manuscript"
    pdf_metadata = {}
    for job, record_name, site_pdf, site_record in PDFS:
        record = read_json(source / record_name)
        match(source / "build_pdf.py", record.get("builder_sha256"), "pdf_builder_hash")
        require(record.get("sources_unchanged_during_build") is True,
                "pdf_sources_unchanged_during_build", record_name)
        recorded = record.get("source_sha256", {})
        expected = {str(p.relative_to(source)) if p.is_relative_to(source)
                    else "../lean/" + p.name: p for p in manuscript_inputs(root, job)}
        require(set(recorded) == set(expected), "pdf_source_inventory", record_name,
                "Every current manuscript, bibliography, figure and selected Lean source must be recorded.")
        for name, path in expected.items():
            match(path, recorded.get(name), "pdf_source_hash")
        match(source / (job + ".pdf"), record.get("pdf_sha256"), "pdf_artifact_hash")
        counts = record.get("warning_counts", {})
        required_warning_keys = {"overfull_boxes", "missing_characters",
                                 "undefined_citation_reports", "undefined_reference_reports",
                                 "undefined_summary_reports", "bibtex_warnings"}
        require(required_warning_keys <= counts.keys() and
                all(counts.get(name) == 0 for name in required_warning_keys),
                "pdf_typesetting_gate", record_name)
        require(isinstance(record.get("pages"), int) and record["pages"] > 0,
                "pdf_page_count", record_name)
        pdf_metadata[job] = {key: record.get(key) for key in
                             ("pages", "pdf_sha256", "pdf_bytes")}
        if site:
            match(root / "extension/site/downloads" / site_pdf,
                  record.get("pdf_sha256"), "site_pdf_hash")
            match(root / "extension/site/verification" / site_record,
                  file_hash(source / record_name), "site_pdf_record")

    claim = read_json(root / "extension/review/claim-register.json")
    require(bool(claim.get("source_files")), "claim_source_inventory", "claim-register.json")
    for entry in claim.get("source_files", []):
        match(root / entry["path"], entry.get("sha256"), "claim_source_hash")

    lean_root = root / "extension/lean"
    formal = read_json(lean_root / "final-verification/verification.json")
    require(formal.get("status") == "verified" and bool(formal.get("modules")),
            "formal_record_status", "final-verification/verification.json")
    match(lean_root / "verify_all.py", formal.get("checker_sha256"), "formal_checker_hash")
    match(lean_root / "lakefile.toml", formal.get("lakefile_sha256"), "formal_configuration_hash")
    declaration_count = 0
    formal_names = []
    for entry in formal.get("modules", []):
        name = entry.get("module", "unknown")
        match(root / entry["source"], entry.get("source_sha256"), "formal_source_hash")
        match(lean_root / "final-verification" / entry["log"],
              entry.get("log_sha256"), "formal_log_hash")
        declarations = entry.get("declarations", [])
        axiom_map = entry.get("axioms_per_declaration", {})
        require(entry.get("status") == "verified" and entry.get("exit_code") == 0
                and entry.get("warning_count") == 0
                and entry.get("source_unchanged_during_check") is True,
                "formal_module_status", name)
        require(set(declarations) == set(axiom_map)
                and all(set(axioms) <= ALLOWED_AXIOMS for axioms in axiom_map.values())
                and not entry.get("unexpected_axioms"), "formal_axiom_boundary", name)
        require(len(declarations) == entry.get("declaration_count"), "formal_module_count", name)
        declaration_count += len(declarations)
        formal_names.extend(declarations)
        if site:
            match(root / "extension/site/verification/lean-current" / entry["log"],
                  entry.get("log_sha256"), "site_formal_log")
    require(declaration_count == formal.get("declaration_count")
            == claim.get("counts", {}).get("authoritative_verified_declarations"),
            "formal_claim_count", "claim-register.json")
    type_map = read_json(root / "extension/review/formal-type-map.json")
    require(type_map.get("declaration_count") == declaration_count,
            "formal_type_map_count", "formal-type-map.json")
    for entry in type_map.get("lean_source_audit", {}).get("verified_modules", []):
        match(root / entry["source_file"], entry.get("source_sha256"), "type_map_source_hash")
        match(root / entry["verification_log"], entry.get("verification_log_sha256"), "type_map_log_hash")
    if site:
        match(root / "extension/site/verification/lean-current/verification.json",
              file_hash(lean_root / "final-verification/verification.json"), "site_formal_record")

    # This binding requires a full clone. The compact companion ZIP deliberately
    # includes the extension and its evidence, not the inherited source packages.
    inherited_root = lean_root / "inherited-verification/all"
    inherited = read_json(inherited_root / "verification.json")
    require(inherited.get("status") == "verified" and inherited.get("package") == "all"
            and inherited.get("blocked_module_count") == 0
            and inherited.get("configuration_unchanged_during_check") is True
            and inherited.get("warnings_treated_as_errors") is True,
            "inherited_record_status", "inherited-verification/all/verification.json")
    provenance = inherited.get("provenance_sha256", {})
    for key, path in {"checker": lean_root / "verify_inherited.py",
                      "evidence_policy": lean_root / "verify_all.py",
                      "repository_mathlib_manifest": root / "lean-analytic/mathlib-manifest.json"}.items():
        match(path, provenance.get(key), "inherited_provenance_hash")
    require(inherited.get("lean_version") == formal.get("lean_version")
            and inherited.get("mathlib_commit") == formal.get("mathlib_commit")
            and bool(inherited.get("lean_version")) and bool(inherited.get("mathlib_commit"))
            and provenance.get("mathlib_manifest") == provenance.get("repository_mathlib_manifest"),
            "inherited_toolchain_consistency", "inherited-verification/all/verification.json")
    expected_sources = {p.relative_to(root).as_posix() for package in ("lean", "lean-analytic")
                        for p in (root / package).glob("*.lean")}
    modules = inherited.get("modules", [])
    require(bool(list((root / "lean").glob("*.lean")))
            and bool(list((root / "lean-analytic").glob("*.lean")))
            and {entry.get("source") for entry in modules} == expected_sources
            and len(modules) == len(expected_sources),
            "inherited_source_inventory", "inherited-verification/all/verification.json")
    inherited_names = []
    for entry in modules:
        name = entry.get("source", "unknown")
        match(root / name, entry.get("source_sha256"), "inherited_source_hash")
        match(inherited_root / entry["log"], entry.get("log_sha256"), "inherited_log_hash")
        names = entry.get("declarations", [])
        axioms = entry.get("axioms_per_declaration", {})
        printed = entry.get("kernel_printed_types", {})
        require(entry.get("status") == "verified" and entry.get("exit_code") == 0
                and entry.get("warning_count") == 0
                and entry.get("source_unchanged_during_check") is True
                and entry.get("missing_compiled_dependencies") == [],
                "inherited_module_status", name)
        require(bool(names) and len(names) == entry.get("declaration_count")
                and set(names) == set(axioms) == set(printed)
                and entry.get("printed_types_cover_every_declaration") is True
                and all(isinstance(value, str) and value.strip() for value in printed.values())
                and all(set(value) <= ALLOWED_AXIOMS for value in axioms.values())
                and not entry.get("unexpected_axioms"), "inherited_type_axiom_boundary", name)
        inherited_names.extend(names)
    inherited_count = len(inherited_names)
    require(len(set(inherited_names)) == inherited_count
            and set(inherited_names).isdisjoint(formal_names)
            and inherited_count == inherited.get("declaration_count")
            == inherited.get("verified_declaration_count")
            and len(modules) == inherited.get("module_count") == inherited.get("verified_module_count"),
            "inherited_count_consistency", "inherited-verification/all/verification.json")

    weighted_root = root / "extension/review/final-pass/weighted-gain"
    weighted = read_json(weighted_root / "verification.json")
    weighted_manifest = read_json(weighted_root / "manifest.json")
    require(weighted.get("status") == "passed"
            and type(weighted.get("test_methods_run")) is int and weighted["test_methods_run"] > 0
            and all(weighted.get(key) == 0 for key in ("failures", "errors", "skipped"))
            and weighted.get("sources_unchanged_during_tests") is True
            and all(type(weighted.get(key)) is int and weighted[key] > 0 for key in
                    ("randomized_exact_cases_checked", "scalar_rejection_cases",
                     "derived_field_mutation_cases", "standalone_cli_cases_checked")),
            "weighted_record_status", "weighted-gain/verification.json")
    weighted_sources_ok = bind_sources(weighted, WEIGHTED_SOURCES, "weighted")
    manifest_sources_ok = bind_sources(weighted_manifest, WEIGHTED_SOURCES, "weighted_manifest")
    weighted_examples = weighted_manifest.get("examples", [])
    require(weighted_manifest.get("status") == "passed"
            and isinstance(weighted_examples, list) and len(weighted_examples) == len(WEIGHTED_CASES)
            and {entry.get("name") for entry in weighted_examples} == set(WEIGHTED_CASES)
            and weighted_manifest.get("ordinary_regression_equal_to_ae44abb_except_source_hash") is True,
            "weighted_manifest_status", "weighted-gain/manifest.json")
    weighted_artifacts = {prefix + name + ".json" for name in WEIGHTED_CASES
                          for prefix in ("witness-", "replay-")}
    weighted_artifacts_ok = bind_artifacts(weighted_root, weighted_manifest.get("artifact_sha256"),
                                           weighted_artifacts, "weighted")
    for entry in weighted_examples:
        name = entry.get("name")
        if name not in WEIGHTED_CASES:
            continue
        exit_code, status, contraction = WEIGHTED_CASES[name]
        witness, replay = "witness-" + name + ".json", "replay-" + name + ".json"
        hashes = weighted_manifest.get("artifact_sha256", {})
        require(entry.get("witness") == witness and entry.get("replay") == replay
                and entry.get("witness_sha256") == hashes.get(witness)
                and entry.get("replay_sha256") == hashes.get(replay)
                and entry.get("exit_code") == exit_code and entry.get("status") == status
                and entry.get("certifies_contraction") is contraction,
                "weighted_example_metadata", str(name))
    for name, outcome in WEIGHTED_CASES.items():
        replay_gain(weighted_root, "witness-" + name + ".json", "replay-" + name + ".json", outcome,
                    weighted_sources_ok and manifest_sources_ok and weighted_artifacts_ok)

    quantum_root = root / "extension/review/final-pass/quantum-gain-control"
    quantum = read_json(quantum_root / "verification.json")
    require(quantum.get("status") == "passed" and quantum.get("sources_unchanged_during_checks") is True,
            "quantum_record_status", "quantum-gain-control/verification.json")
    quantum_sources_ok = bind_sources(quantum, QUANTUM_SOURCES, "quantum")
    quantum_artifacts_ok = bind_artifacts(quantum_root, quantum.get("artifact_sha256"),
                                          QUANTUM_ARTIFACTS, "quantum")
    quantum_counts = quantum.get("counts", {})
    require(isinstance(quantum_counts, dict) and set(quantum_counts) == QUANTUM_COUNTERS
            and all(type(value) is int and value > 0 for value in quantum_counts.values()),
            "quantum_counter_inventory", "quantum-gain-control/verification.json")
    channel = quantum.get("channel_checks", {})
    trajectory = read_json(quantum_root / "trajectories.json")
    paths = read_json(quantum_root / "path-comparison.json")
    parameter_cases = len(channel.get("retentions", [])) * len(channel.get("controls", []))
    state_fixtures = channel.get("state_fixtures", 0)
    steps = trajectory.get("steps_per_trajectory", -1)
    rows = trajectory.get("trajectories", {})
    valid_trajectories = (type(steps) is int and steps >= 1 and isinstance(rows, dict)
                          and set(rows) == {"ideal", "bounded_readout_error"}
                          and all(isinstance(values, list) and len(values) == steps + 1
                                  and [row.get("step") for row in values] == list(range(steps + 1))
                                  and all(len(row.get("bloch_states", [])) == 2 for row in values)
                                  for values in rows.values()))
    require(valid_trajectories and quantum.get("trajectories", {}).get("steps_per_trajectory") == steps
            and quantum.get("trajectories", {}).get("states_per_trajectory") == steps + 1,
            "quantum_trajectory_inventory", "quantum-gain-control/trajectories.json")
    require(parameter_cases > 0 and type(state_fixtures) is int and state_fixtures > 0
            and quantum_counts.get("channel_parameter_cases") == parameter_cases
            and quantum_counts.get("choi_principal_minors") == 15 * parameter_cases
            and quantum_counts.get("coherent_matrix_bloch_comparisons") == parameter_cases * state_fixtures
            and quantum_counts.get("fixed_control_distance_equalities") == parameter_cases * state_fixtures
            and quantum_counts.get("trajectory_state_budget_checks") == 4 * (steps + 1)
            and quantum_counts.get("residual_one_step_block_checks") == 4 * steps
            and quantum_counts.get("path_horizons") == len(paths.get("horizons", []))
            and quantum_counts.get("independent_gain_replays") == 2
            == len(quantum.get("independent_gain_replays", [])),
            "quantum_counter_consistency", "quantum-gain-control/verification.json")
    quantum_outcomes = {"accepted": (0, "certified", True), "rejected": (2, "rejected", False)}
    replay_metadata = quantum.get("independent_gain_replays", [])
    require(isinstance(replay_metadata, list) and len(replay_metadata) == 2
            and {entry.get("name") for entry in replay_metadata} == set(quantum_outcomes),
            "quantum_replay_inventory", "quantum-gain-control/verification.json")
    for entry in replay_metadata:
        name = entry.get("name")
        if name not in quantum_outcomes:
            continue
        exit_code, status, contraction = quantum_outcomes[name]
        witness = read_json(quantum_root / ("gain-" + name + ".json"))
        require(entry.get("exit_code") == exit_code and entry.get("status") == status
                and entry.get("certifies_contraction") is contraction
                and entry.get("proposed_rate") == witness.get("rate"),
                "quantum_replay_metadata", str(name))
    for name, outcome in quantum_outcomes.items():
        replay_gain(quantum_root, "gain-" + name + ".json", "gain-" + name + "-replay.json", outcome,
                    quantum_sources_ok and quantum_artifacts_ok)

    crypto_root = root / "extension/crypto"
    crypto = read_json(crypto_root / "verification.json")
    require(crypto.get("status") == "passed" and crypto.get("tests_run", 0) > 0
            and all(crypto.get(k) == 0 for k in ("failures", "errors", "skipped")),
            "crypto_record_status", "extension/crypto/verification.json")
    require(bool(crypto.get("source_sha256")), "crypto_source_inventory", "verification.json")
    for name, expected in crypto.get("source_sha256", {}).items():
        match(crypto_root / name, expected, "crypto_source_hash")
    match(crypto_root / "verification.log", crypto.get("log_sha256"), "crypto_log_hash")

    numerical_root = root / "extension/verification"
    fluid_node = read_json(numerical_root / "fluids-node.json")
    require(fluid_node.get("status") == "passed", "fluid_node_status", "fluids-node.json")
    for key, name in {"core": "extension/site/fluid-core.js",
                      "reference": "extension/site/data/fluids-reference.json",
                      "verification_script": "extension/site/verify-fluids.cjs"}.items():
        match(root / name, fluid_node.get("hashes", {}).get(key), "fluid_node_input_hash")
    for name, script in (("fluids-python.json", "verify_fluid_interfaces.py"),
                         ("examples.json", "verify_examples.py"),
                         ("invariants.json", "verify_invariants.py")):
        record = read_json(numerical_root / name)
        require(record.get("status") == "passed" or record.get("passed") is True,
                "numerical_record_status", name)
        match(root / "extension/code" / script, record.get("script_sha256"), "numerical_checker_hash")

    upstream = read_json(root / "extension/review/final-pass/upstream-build-current.json")
    summary = {"pdfs": pdf_metadata, "local_finite_declarations": declaration_count,
               "local_modules": len(formal.get("modules", [])),
               "inherited_declarations": inherited_count,
               "all_local_declarations": declaration_count + inherited_count,
               "weighted_gain_test_methods": weighted.get("test_methods_run"),
               "quantum_control_checks": quantum_counts,
               "written_claims": claim.get("counts", {}),
               "crypto_tests": crypto.get("tests_run"),
               "upstream_build_status": upstream.get("status"),
               "upstream_final_kernel_verified": upstream.get("fresh_final_kernel_verified", False)}
    if site:
        for original, copy in site_copy_map(root).items():
            match(root / "extension/site" / copy, file_hash(root / original), "site_evidence_copy")
        published = read_json(root / "extension/site/verification/release-summary.json")
        require(published.get("summary") == summary, "site_release_summary", "release-summary.json")
        for name, expected in published.get("source_sha256", {}).items():
            match(root / name, expected, "site_summary_source_hash")

    if archives:
        downloads = root / "extension/site/downloads"
        lean_zip = downloads / "lean4.zip"
        if file_hash(lean_zip):
            try:
                with zipfile.ZipFile(lean_zip) as archive:
                    expected = {p.relative_to(lean_root).as_posix(): p for p in lean_archive_files(root)}
                    require(set(archive.namelist()) == set(expected)
                            and len(archive.namelist()) == len(expected), "lean_archive_inventory", "lean4.zip")
                    for name, path in expected.items():
                        require(name in archive.namelist() and
                                hashlib.sha256(archive.read(name)).hexdigest() == digest(path),
                                "lean_archive_source_hash", name)
            except (OSError, KeyError, ValueError, zipfile.BadZipFile) as error:
                require(False, "lean_archive_readable", "lean4.zip", str(error))
        compact = downloads / "source.zip"
        if file_hash(compact):
            try:
                with zipfile.ZipFile(compact) as archive:
                    manifest = json.loads(archive.read("ARCHIVE-MANIFEST.json"))
                    expected = {p.relative_to(root).as_posix() for p in compact_source_files(root)}
                    recorded = [entry["path"] for entry in manifest["files"]]
                    require(set(recorded) == expected and len(recorded) == len(expected),
                            "source_archive_inventory", "source.zip")
                    allowed_members = expected | {"ARCHIVE-MANIFEST.json", "SOURCE-README.md"}
                    require(set(archive.namelist()) == allowed_members
                            and len(archive.namelist()) == len(allowed_members),
                            "source_archive_member_inventory", "source.zip")
                    for entry in manifest["files"]:
                        name = entry["path"]
                        match(root / name, entry.get("sha256"), "source_archive_current_hash")
                        require(hashlib.sha256(archive.read(name)).hexdigest() == entry.get("sha256"),
                                "source_archive_member_hash", name)
            except (OSError, KeyError, ValueError, zipfile.BadZipFile) as error:
                require(False, "source_archive_readable", "source.zip", str(error))
    return {"schema_version": 1, "status": "passed" if not failures else "failed",
            "checks_run": checks, "site_checked": site, "archives_checked": archives,
            "summary": summary, "failures": failures, "input_sha256": inputs,
            "scope": "Offline freshness and consistency of selected source, PDF, Lean, crypto and publication records, plus bounded independent integer replay of the supplied gain witnesses. Inherited source binding requires a full clone; the compact companion archive is an explicit extension subset. No new proof, independent upstream verification, certificate authenticity, browser interaction or deployment success is asserted."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--site", action="store_true")
    parser.add_argument("--archives", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    report = check_release(args.root, site=args.site, archives=args.archives)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ("status", "checks_run", "summary", "failures")}, indent=2))
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
