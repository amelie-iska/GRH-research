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
import zipfile

ROOT = Path(__file__).resolve().parents[2]
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
PDFS = (("main", "build-verification.json", "paper.pdf", "pdf-build.json"),
        ("fluid-extension", "fluid-build-verification.json", "fluid-extension.pdf",
         "fluid-build-verification.json"))
SITE_COPIES = {
    "extension/review/claim-register.json": "verification/claim-register.json",
    "extension/review/claim-register.md": "verification/claim-register.md",
    "extension/review/formal-type-map.json": "verification/formal-type-map.json",
    "extension/review/formal-type-map.md": "verification/formal-type-map.md",
    "extension/crypto/verification.json": "verification/crypto/verification.json",
    "extension/crypto/verification.log": "verification/crypto/verification.log",
    "extension/review/final-pass/upstream-build-current.json": "verification/final-pass/upstream-build-current.json",
    "extension/review/final-pass/upstream-build-current.md": "verification/final-pass/upstream-build-current.md",
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

    def match(path: Path, expected: str | None, code: str) -> None:
        actual = file_hash(path)
        require(bool(expected) and actual == expected, code,
                str(path.relative_to(root)) if path.is_relative_to(root) else str(path))

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
            "scope": "Offline freshness and consistency of selected source, PDF, Lean, crypto and publication records. No new proof, independent upstream verification, certificate authenticity, browser interaction or deployment success is asserted."}


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
