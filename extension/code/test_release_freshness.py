#!/usr/bin/env python3
"""Negative controls for release consistency; fixtures are not proof evidence."""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
import tempfile
import unittest
import zipfile

from check_weighted_gain_witness import replay_weighted_gain_witness
from release_freshness import (PDFS, QUANTUM_SOURCES, WEIGHTED_CASES, WEIGHTED_SOURCES,
                               check_release, compact_source_files, digest, lean_archive_files,
                               manuscript_inputs, site_copy_map)


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
            "extension/review/quantum-tropical-substrates-20261113.md": "synthetic source-review fixture",
            "extension/manuscript/quantum-tropical-substrates.bib": "synthetic bibliography fixture",
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
            "lean_version": "synthetic Lean version", "mathlib_commit": "synthetic mathlib revision",
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
        self.add_inherited_records()
        self.add_gain_records()

    def add_inherited_records(self):
        self.write("extension/lean/verify_inherited.py", "synthetic inherited verifier fixture")
        self.write("lean-analytic/mathlib-manifest.json", "{}")
        modules = []
        for package, theorem in (("lean", "Inherited.arithmetic"), ("lean-analytic", "Inherited.analytic")):
            source = package + "/Example.lean"
            log = package + "-Example.log"
            self.write(source, "synthetic inherited source; never compiled")
            self.write("extension/lean/inherited-verification/all/" + log, "synthetic inherited log")
            modules.append({"source": source, "source_sha256": self.hash(source),
                "log": log, "log_sha256": self.hash("extension/lean/inherited-verification/all/" + log),
                "status": "verified", "exit_code": 0, "warning_count": 0,
                "source_unchanged_during_check": True, "missing_compiled_dependencies": [],
                "declaration_count": 1, "declarations": [theorem],
                "axioms_per_declaration": {theorem: []}, "unexpected_axioms": {},
                "kernel_printed_types": {theorem: theorem + " : True"},
                "printed_types_cover_every_declaration": True})
        manifest_hash = self.hash("lean-analytic/mathlib-manifest.json")
        self.record("extension/lean/inherited-verification/all/verification.json", {
            "status": "verified", "package": "all", "module_count": 2, "verified_module_count": 2,
            "declaration_count": 2, "verified_declaration_count": 2, "blocked_module_count": 0,
            "configuration_unchanged_during_check": True, "warnings_treated_as_errors": True,
            "lean_version": "synthetic Lean version", "mathlib_commit": "synthetic mathlib revision",
            "provenance_sha256": {"checker": self.hash("extension/lean/verify_inherited.py"),
                "evidence_policy": self.hash("extension/lean/verify_all.py"),
                "repository_mathlib_manifest": manifest_hash, "mathlib_manifest": manifest_hash},
            "modules": modules})

    @staticmethod
    def rational(value):
        value = Fraction(value)
        return {"numerator": str(value.numerator), "denominator": str(value.denominator)}

    def gain_pair(self, directory, witness_name, replay_name, rate):
        # A genuine one-dimensional exact witness, used only as a gate fixture.
        gain, rate = Fraction(1, 2), Fraction(rate)
        witness = {"schema_version": 1, "kind": "weighted-gain",
            "gain": [[self.rational(gain)]], "weights": [self.rational(1)],
            "rate": self.rational(rate), "row_lhs": [self.rational(gain)],
            "row_rhs": [self.rational(rate)], "row_slack": [self.rational(rate - gain)],
            "row_bounds": [self.rational(gain)], "weighted_bound": self.rational(gain),
            "bound_holds": gain <= rate, "certifies_contraction": gain <= rate < 1}
        self.record(directory + "/" + witness_name, witness)
        self.record(directory + "/" + replay_name, replay_weighted_gain_witness(witness))

    def add_gain_records(self):
        for source in sorted(WEIGHTED_SOURCES | QUANTUM_SOURCES):
            self.write(source, "synthetic source-binding fixture")
        self.write("extension/code/check_weighted_gain_witness.py",
                   Path(__file__).with_name("check_weighted_gain_witness.py").read_text())
        weighted_root = "extension/review/final-pass/weighted-gain"
        weighted_hashes = {name: self.hash(name) for name in WEIGHTED_SOURCES}
        self.record(weighted_root + "/verification.json", {
            "status": "passed", "test_methods_run": 1, "failures": 0, "errors": 0, "skipped": 0,
            "sources_unchanged_during_tests": True, "source_sha256": weighted_hashes,
            "randomized_exact_cases_checked": 1, "scalar_rejection_cases": 1,
            "derived_field_mutation_cases": 1, "standalone_cli_cases_checked": 1})
        examples = []
        for name, (exit_code, status, contraction) in WEIGHTED_CASES.items():
            rate = Fraction(1, 2) if contraction else 2 if exit_code == 0 else Fraction(2, 5)
            witness, replay = "witness-" + name + ".json", "replay-" + name + ".json"
            self.gain_pair(weighted_root, witness, replay, rate)
            examples.append({"name": name, "witness": witness, "replay": replay,
                "witness_sha256": self.hash(weighted_root + "/" + witness),
                "replay_sha256": self.hash(weighted_root + "/" + replay),
                "exit_code": exit_code, "status": status, "certifies_contraction": contraction})
        self.record(weighted_root + "/manifest.json", {
            "status": "passed", "examples": examples, "source_sha256": weighted_hashes,
            "ordinary_regression_equal_to_ae44abb_except_source_hash": True,
            "artifact_sha256": {prefix + name + ".json": self.hash(weighted_root + "/" + prefix + name + ".json")
                                for name in WEIGHTED_CASES for prefix in ("witness-", "replay-")}})
        quantum_root = "extension/review/final-pass/quantum-gain-control"
        for name, rate in (("accepted", Fraction(1, 2)), ("rejected", Fraction(2, 5))):
            self.gain_pair(quantum_root, "gain-" + name + ".json", "gain-" + name + "-replay.json", rate)
        self.record(quantum_root + "/trajectories.json", {"steps_per_trajectory": 1,
            "trajectories": {mode: [{"step": n, "bloch_states": [[0, 0, 0], [0, 0, 0]]}
                                     for n in range(2)] for mode in ("ideal", "bounded_readout_error")}})
        self.record(quantum_root + "/path-comparison.json", {"horizons": [{"horizon": 1}]})
        artifacts = [p.name for p in (self.root / quantum_root).glob("*.json")]
        self.record(quantum_root + "/verification.json", {
            "status": "passed", "sources_unchanged_during_checks": True,
            "source_sha256": {name: self.hash(name) for name in QUANTUM_SOURCES},
            "artifact_sha256": {name: self.hash(quantum_root + "/" + name) for name in artifacts},
            "channel_checks": {"retentions": [0], "controls": [0], "state_fixtures": 1},
            "trajectories": {"steps_per_trajectory": 1, "states_per_trajectory": 2},
            "independent_gain_replays": [
                {"name": "accepted", "proposed_rate": self.rational(Fraction(1, 2)),
                 "exit_code": 0, "status": "certified", "certifies_contraction": True},
                {"name": "rejected", "proposed_rate": self.rational(Fraction(2, 5)),
                 "exit_code": 2, "status": "rejected", "certifies_contraction": False}],
            "counts": {"channel_parameter_cases": 1, "choi_principal_minors": 15,
                "coherent_matrix_bloch_comparisons": 1, "fixed_control_distance_equalities": 1,
                "controller_pair_block_bounds": 2, "trajectory_state_budget_checks": 8,
                "residual_one_step_block_checks": 4, "path_horizons": 1,
                "invalid_domain_rejections": 1, "independent_gain_replays": 2}})

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
        self.assertEqual(result["summary"]["inherited_declarations"], 2)
        self.assertEqual(result["summary"]["all_local_declarations"], 3)
        self.assertEqual(result["summary"]["weighted_gain_test_methods"], 1)
        self.assertEqual(result["summary"]["quantum_control_checks"]["independent_gain_replays"], 2)

    def refresh_artifact_hash(self, directory, record_name, artifact):
        path = directory + "/" + record_name
        record = json.loads((self.root / path).read_text())
        record["artifact_sha256"][artifact] = self.hash(directory + "/" + artifact)
        self.record(path, record)

    def test_changed_gain_producer_rejected(self):
        self.write("extension/code/verify_toric_transport.py", "changed after recorded gain tests")
        self.reject("weighted_source_hash")

    def test_changed_weighted_witness_rejected(self):
        self.write("extension/review/final-pass/weighted-gain/witness-accepted.json", "stale witness")
        self.reject("weighted_artifact_hash")

    def test_changed_weighted_replay_rejected(self):
        self.write("extension/review/final-pass/weighted-gain/replay-accepted.json", "{}")
        self.reject("weighted_artifact_hash")

    def test_overclaimed_noncontracting_replay_rejected_after_rehash(self):
        directory = "extension/review/final-pass/weighted-gain"
        name = "replay-noncontracting.json"
        record = json.loads((self.root / directory / name).read_text())
        record["certifies_contraction"] = True
        self.record(directory + "/" + name, record)
        self.refresh_artifact_hash(directory, "manifest.json", name)
        self.reject("gain_replay_matches_record")

    def test_inconsistent_witness_rejected_by_live_integer_replay_after_rehash(self):
        directory = "extension/review/final-pass/weighted-gain"
        name = "witness-accepted.json"
        record = json.loads((self.root / directory / name).read_text())
        record["row_lhs"][0] = self.rational(7)
        self.record(directory + "/" + name, record)
        self.refresh_artifact_hash(directory, "manifest.json", name)
        self.reject("gain_replay_matches_record")

    def test_changed_quantum_producer_rejected(self):
        self.write("extension/code/quantum_gain_control.py", "changed after recorded exact checks")
        self.reject("quantum_source_hash")

    def test_changed_quantum_output_rejected(self):
        self.write("extension/review/final-pass/quantum-gain-control/path-comparison.json", "{}")
        self.reject("quantum_artifact_hash")

    def test_inconsistent_quantum_counter_rejected(self):
        path = "extension/review/final-pass/quantum-gain-control/verification.json"
        record = json.loads((self.root / path).read_text())
        record["counts"]["choi_principal_minors"] += 1
        self.record(path, record)
        self.reject("quantum_counter_consistency")

    def test_overclaimed_quantum_replay_metadata_rejected(self):
        path = "extension/review/final-pass/quantum-gain-control/verification.json"
        record = json.loads((self.root / path).read_text())
        record["independent_gain_replays"][1]["certifies_contraction"] = True
        self.record(path, record)
        self.reject("quantum_replay_metadata")

    def test_missing_quantum_source_inventory_rejected(self):
        path = "extension/review/final-pass/quantum-gain-control/verification.json"
        record = json.loads((self.root / path).read_text())
        del record["source_sha256"]["extension/code/verify_quantum_gain_control.py"]
        self.record(path, record)
        self.reject("quantum_source_inventory")

    def test_changed_inherited_source_rejected(self):
        self.write("lean-analytic/Example.lean", "changed after recorded inherited check")
        self.reject("inherited_source_hash")

    def test_missing_inherited_module_rejected(self):
        path = "extension/lean/inherited-verification/all/verification.json"
        record = json.loads((self.root / path).read_text())
        record["modules"].pop()
        for name in ("module_count", "verified_module_count", "declaration_count", "verified_declaration_count"):
            record[name] = 1
        self.record(path, record)
        self.reject("inherited_source_inventory")

    def test_unapproved_inherited_axiom_rejected(self):
        path = "extension/lean/inherited-verification/all/verification.json"
        record = json.loads((self.root / path).read_text())
        record["modules"][0]["axioms_per_declaration"]["Inherited.arithmetic"] = ["sorryAx"]
        self.record(path, record)
        self.reject("inherited_type_axiom_boundary")

    def test_missing_inherited_printed_type_rejected(self):
        path = "extension/lean/inherited-verification/all/verification.json"
        record = json.loads((self.root / path).read_text())
        record["modules"][0]["kernel_printed_types"] = {}
        self.record(path, record)
        self.reject("inherited_type_axiom_boundary")

    def test_changed_inherited_policy_rejected(self):
        self.write("extension/lean/verify_all.py", "changed shared evidence policy")
        self.reject("inherited_provenance_hash")

    def test_changed_inherited_log_rejected(self):
        self.write("extension/lean/inherited-verification/all/lean-Example.log", "changed inherited log")
        self.reject("inherited_log_hash")

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

    def add_site_copies(self):
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

    def test_stale_public_evidence_copy_rejected(self):
        self.add_site_copies()
        self.assertEqual(check_release(self.root, site=True)["status"], "passed")
        self.write("extension/site/verification/claim-register.json", "stale public copy")
        self.reject("site_evidence_copy", site=True)

    def test_recursive_final_pass_mirrors_required_and_credentials_excluded(self):
        required = {}
        for name in ("weighted-gain", "quantum-gain-control", "release-gate-continuation"):
            source = "extension/review/final-pass/" + name
            nested = source + "/nested/trace.log"
            self.write(nested, "synthetic nested audit evidence")
            self.write(source + "/KEYS.TXT", "synthetic forbidden-path fixture, not a credential")
            self.write(source + "/.private-credentials/example.txt", "synthetic forbidden-path fixture")
            required[nested] = "verification/final-pass/" + name + "/nested/trace.log"
        for name in ("weighted-gain", "quantum-gain-control"):
            required["extension/review/final-pass/" + name + "/verification.json"] = (
                "verification/final-pass/" + name + "/verification.json")
        copies = site_copy_map(self.root)
        for source, target in required.items():
            self.assertEqual(copies.get(source), target)
        self.assertFalse(any(Path(name).name.casefold() == "keys.txt" or
                             ".private-credentials" in Path(name).parts for name in copies))
        self.add_site_copies()
        self.assertEqual(check_release(self.root, site=True)["status"], "passed")
        for source, target in required.items():
            with self.subTest(missing_public_mirror=target):
                public = self.root / "extension/site" / target
                public.unlink()
                self.reject("site_evidence_copy", site=True)
                self.write("extension/site/" + target, (self.root / source).read_text())

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
