#!/usr/bin/env python3
"""Negative controls for release consistency; fixtures are not proof evidence."""
from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest
import zipfile

from release_freshness import (PDFS, check_release, compact_source_files, digest,
                               lean_archive_files, manuscript_inputs, site_copy_map)


class ReleaseFreshnessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="grh-release-gate-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name, content in {
            ".gitignore": "keys.txt\n.private-credentials/\n",
            "extension/manuscript/main.tex": "synthetic main fixture",
            "extension/manuscript/fluid-extension.tex": "synthetic fluid fixture",
            "extension/manuscript/lean-listings-unicode.tex": "synthetic listing fixture",
            "extension/manuscript/build_pdf.py": "synthetic build driver fixture",
            "extension/manuscript/chapters/claim.tex": "synthetic claim fixture",
            "extension/manuscript/main.pdf": "synthetic PDF bytes, not a real PDF",
            "extension/manuscript/fluid-extension.pdf": "synthetic fluid PDF bytes",
            "extension/lean/Example.lean": "synthetic Lean fixture, not compiled",
            "extension/lean/verify_all.py": "synthetic verifier fixture",
            "extension/lean/lakefile.toml": "synthetic lake fixture",
            "extension/lean/final-verification/Example.log": "synthetic compiler log",
            "extension/crypto/example.py": "synthetic crypto source",
            "extension/crypto/verification.log": "synthetic test log",
            "extension/review/claim-register.md": "synthetic claim inventory",
            "extension/review/formal-type-map.md": "synthetic type map",
            "extension/review/final-pass/upstream-build-current.md": "upstream incomplete",
            "extension/site/fluid-core.js": "synthetic fluid kernel",
            "extension/site/data/fluids-reference.json": "synthetic numerical reference",
            "extension/site/verify-fluids.cjs": "synthetic JavaScript checker",
            "extension/code/verify_fluid_interfaces.py": "synthetic Python fluid checker",
            "extension/code/verify_examples.py": "synthetic examples checker",
            "extension/code/verify_invariants.py": "synthetic invariants checker",
        }.items():
            self.write(name, content)
        for job, record_name, _, _ in PDFS:
            source = self.root / "extension/manuscript"
            self.record("extension/manuscript/" + record_name, {
                "builder_sha256": self.hash("extension/manuscript/build_pdf.py"),
                "sources_unchanged_during_build": True,
                "source_sha256": {str(p.relative_to(source)) if p.is_relative_to(source)
                                  else "../lean/" + p.name: digest(p)
                                  for p in manuscript_inputs(self.root, job)},
                "pdf_sha256": digest(source / (job + ".pdf")), "pages": 1,
                "pdf_bytes": (source / (job + ".pdf")).stat().st_size,
                "warning_counts": {k: 0 for k in ("overfull_boxes", "missing_characters",
                    "undefined_citation_reports", "undefined_reference_reports",
                    "undefined_summary_reports", "bibtex_warnings")}})
        self.record("extension/review/claim-register.json", {
            "source_files": [{"path": "extension/manuscript/chapters/claim.tex",
                              "sha256": self.hash("extension/manuscript/chapters/claim.tex")}],
            "counts": {"authoritative_verified_declarations": 1}})
        self.record("extension/lean/final-verification/verification.json", {
            "status": "verified", "declaration_count": 1,
            "checker_sha256": self.hash("extension/lean/verify_all.py"),
            "lakefile_sha256": self.hash("extension/lean/lakefile.toml"),
            "modules": [{"module": "Example", "source": "extension/lean/Example.lean",
                "source_sha256": self.hash("extension/lean/Example.lean"),
                "log": "Example.log", "log_sha256": self.hash("extension/lean/final-verification/Example.log"),
                "status": "verified", "exit_code": 0, "warning_count": 0,
                "source_unchanged_during_check": True, "declaration_count": 1,
                "declarations": ["example"], "axioms_per_declaration": {"example": []},
                "unexpected_axioms": {}}]})
        self.record("extension/review/formal-type-map.json", {
            "declaration_count": 1, "lean_source_audit": {"verified_modules": [{
                "source_file": "extension/lean/Example.lean",
                "source_sha256": self.hash("extension/lean/Example.lean"),
                "verification_log": "extension/lean/final-verification/Example.log",
                "verification_log_sha256": self.hash("extension/lean/final-verification/Example.log")}]}})
        self.record("extension/crypto/verification.json", {
            "status": "passed", "tests_run": 1, "failures": 0, "errors": 0, "skipped": 0,
            "source_sha256": {"example.py": self.hash("extension/crypto/example.py")},
            "log_sha256": self.hash("extension/crypto/verification.log")})
        self.record("extension/review/final-pass/upstream-build-current.json",
                    {"status": "upstream_fixture_incomplete"})
        self.record("extension/verification/fluids-node.json", {
            "status": "passed", "hashes": {
                "core": self.hash("extension/site/fluid-core.js"),
                "reference": self.hash("extension/site/data/fluids-reference.json"),
                "verification_script": self.hash("extension/site/verify-fluids.cjs")}})
        for name, script in (("fluids-python.json", "verify_fluid_interfaces.py"),
                             ("examples.json", "verify_examples.py"),
                             ("invariants.json", "verify_invariants.py")):
            self.record("extension/verification/" + name,
                        {"status": "passed", "script_sha256": self.hash("extension/code/" + script)})

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def record(self, name, value):
        self.write(name, json.dumps(value))

    def hash(self, name):
        return digest(self.root / name)

    def reject(self, code, **kwargs):
        result = check_release(self.root, **kwargs)
        self.assertEqual(result["status"], "failed")
        self.assertIn(code, {entry["check"] for entry in result["failures"]})

    def add_archives(self):
        downloads = self.root / "extension/site/downloads"
        downloads.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(downloads / "lean4.zip", "w") as archive:
            for path in lean_archive_files(self.root):
                archive.write(path, path.relative_to(self.root / "extension/lean").as_posix())
        with zipfile.ZipFile(downloads / "source.zip", "w") as archive:
            entries = []
            for path in compact_source_files(self.root):
                name = path.relative_to(self.root).as_posix()
                archive.write(path, name)
                entries.append({"path": name, "sha256": self.hash(name)})
            archive.writestr("ARCHIVE-MANIFEST.json", json.dumps({"files": entries}))
            archive.writestr("SOURCE-README.md", "Synthetic archive fixture")

    def test_consistent_fixture_and_honest_upstream_gap_pass(self):
        result = check_release(self.root)
        self.assertEqual(result["failures"], [])
        self.assertEqual(result["status"], "passed")
        self.assertFalse(result["summary"]["upstream_final_kernel_verified"])

    def test_changed_pdf_source_rejected(self):
        self.write("extension/manuscript/main.tex", "changed after recorded build")
        self.reject("pdf_source_hash")

    def test_unrecorded_new_chapter_rejected(self):
        self.write("extension/manuscript/chapters/new.tex", "not in either PDF record")
        self.reject("pdf_source_inventory")

    def test_changed_pdf_bytes_rejected(self):
        self.write("extension/manuscript/main.pdf", "changed PDF artifact")
        self.reject("pdf_artifact_hash")

    def test_changed_written_claim_rejected(self):
        self.write("extension/manuscript/chapters/claim.tex", "changed argument")
        self.reject("claim_source_hash")

    def test_changed_formal_log_rejected(self):
        self.write("extension/lean/final-verification/Example.log", "changed compiler log")
        self.reject("formal_log_hash")

    def test_unapproved_axiom_rejected(self):
        path = "extension/lean/final-verification/verification.json"
        record = json.loads((self.root / path).read_text())
        record["modules"][0]["axioms_per_declaration"]["example"] = ["sorryAx"]
        self.record(path, record)
        self.reject("formal_axiom_boundary")

    def test_changed_crypto_source_rejected(self):
        self.write("extension/crypto/example.py", "changed implementation")
        self.reject("crypto_source_hash")

    def test_changed_fluid_reference_rejected(self):
        self.write("extension/site/data/fluids-reference.json", "stale fluid data")
        self.reject("fluid_node_input_hash")

    def test_stale_public_evidence_copy_rejected(self):
        for original, target in site_copy_map(self.root).items():
            self.write("extension/site/" + target, (self.root / original).read_text())
        for job, record, site_pdf, site_record in PDFS:
            self.write("extension/site/downloads/" + site_pdf,
                       (self.root / "extension/manuscript" / (job + ".pdf")).read_text())
            self.write("extension/site/verification/" + site_record,
                       (self.root / "extension/manuscript" / record).read_text())
        for path in (self.root / "extension/lean/final-verification").rglob("*"):
            if path.is_file():
                self.write("extension/site/verification/lean-current/" + path.name, path.read_text())
        summary = check_release(self.root)["summary"]
        self.record("extension/site/verification/release-summary.json",
                    {"summary": summary, "source_sha256": {}})
        self.assertEqual(check_release(self.root, site=True)["status"], "passed")
        self.write("extension/site/verification/claim-register.json", "stale public copy")
        self.reject("site_evidence_copy", site=True)

    def test_recursive_archive_contains_logs_and_rejects_missing_log(self):
        self.add_archives()
        self.assertEqual(check_release(self.root, archives=True)["status"], "passed")
        archive_path = self.root / "extension/site/downloads/lean4.zip"
        with zipfile.ZipFile(archive_path) as archive:
            entries = {name: archive.read(name) for name in archive.namelist()}
        entries.pop("final-verification/Example.log")
        with zipfile.ZipFile(archive_path, "w") as archive:
            for name, content in entries.items():
                archive.writestr(name, content)
        self.reject("lean_archive_inventory", archives=True)

    def test_added_source_missing_from_archive_rejected(self):
        self.add_archives()
        self.write("extension/code/new_component.py", "added after source packaging")
        self.reject("source_archive_inventory", archives=True)

    def test_tex_build_leftovers_do_not_change_archive_or_clean_inventory(self):
        # Reproduce the release defect: local TeX outputs existed while a clean
        # checkout had no such files. Keep bibliography source and audit logs.
        self.write("extension/manuscript/references.bib", "synthetic bibliography")
        self.write("extension/manuscript/build-review.log", "retained audit evidence")
        # Keep the synthetic PDF records consistent with their added source;
        # the archive check must be the only variable exercised below.
        for _, record_name, _, _ in PDFS:
            path = "extension/manuscript/" + record_name
            record = json.loads((self.root / path).read_text())
            record["source_sha256"]["references.bib"] = self.hash(
                "extension/manuscript/references.bib")
            self.record(path, record)
        baseline = {p.relative_to(self.root).as_posix()
                    for p in compact_source_files(self.root)}
        leftovers = [
            "main.bbl", "main.out", "main.toc", "main.aux", "main.blg",
            "main.bcf", "main.fls", "main.fdb_latexmk", "main.run.xml",
            "main.synctex.gz", "main.lof", "main.lot", "main.dvi",
            "slides.nav", "slides.snm", "slides.vrb", "slides.xdv",
            "chapters/claim.aux", "fluid-extension.synctex",
        ]
        for name in leftovers:
            self.write("extension/manuscript/" + name, "synthetic TeX intermediate")
        self.assertEqual(baseline, {p.relative_to(self.root).as_posix()
                                  for p in compact_source_files(self.root)})
        self.add_archives()
        with zipfile.ZipFile(self.root / "extension/site/downloads/source.zip") as archive:
            names = set(archive.namelist())
            self.assertTrue(baseline <= names)
            self.assertIn("extension/manuscript/references.bib", names)
            self.assertIn("extension/manuscript/build-review.log", names)
            self.assertFalse(any("extension/manuscript/" + name in names
                                 for name in leftovers))
        self.assertEqual(check_release(self.root, archives=True)["status"], "passed")
        for name in leftovers:
            (self.root / "extension/manuscript" / name).unlink()
        self.assertEqual(check_release(self.root, archives=True)["status"], "passed")

    def test_source_omitted_from_both_manifest_and_zip_rejected(self):
        self.add_archives()
        archive_path = self.root / "extension/site/downloads/source.zip"
        with zipfile.ZipFile(archive_path) as archive:
            entries = {name: archive.read(name) for name in archive.namelist()}
        omitted = "extension/manuscript/main.tex"
        entries.pop(omitted)
        manifest = json.loads(entries["ARCHIVE-MANIFEST.json"])
        manifest["files"] = [entry for entry in manifest["files"] if entry["path"] != omitted]
        entries["ARCHIVE-MANIFEST.json"] = json.dumps(manifest).encode()
        with zipfile.ZipFile(archive_path, "w") as archive:
            for name, content in entries.items():
                archive.writestr(name, content)
        self.reject("source_archive_inventory", archives=True)

    def test_credentials_excluded_and_ignore_rules_included(self):
        for path in ("keys.txt", "extension/keys.txt", "extension/lean/KEYS.TXT",
                     "extension/.private-credentials/example.txt",
                     "extension/lean/.private-credentials/example.txt"):
            self.write(path, "synthetic forbidden-path fixture, not a credential")
        self.add_archives()
        self.assertEqual(check_release(self.root, archives=True)["status"], "passed")
        for name in ("lean4.zip", "source.zip"):
            with zipfile.ZipFile(self.root / "extension/site/downloads" / name) as archive:
                self.assertFalse(any(Path(path).name.casefold() == "keys.txt" or
                                     ".private-credentials" in path.casefold().split("/")
                                     for path in archive.namelist()))
                if name == "source.zip":
                    self.assertIn(".gitignore", archive.namelist())

    def test_pages_builder_rejects_credential_paths_before_copying(self):
        from build_github_pages import build
        self.write("extension/site/index.html", "<title>Synthetic site</title>")
        self.write("extension/site/keys.txt", "synthetic forbidden-path fixture")
        output = self.root / "pages-output"
        with self.assertRaisesRegex(ValueError, "Credential paths are not published"):
            build(self.root / "extension/site", output, "/GRH-research/")
        self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
