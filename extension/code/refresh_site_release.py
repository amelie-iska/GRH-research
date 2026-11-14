#!/usr/bin/env python3
"""Refresh public evidence and text from source-checked release records.

Run after both manuscripts and the selected Lean/crypto checks are final, then
package_release.py, then release_freshness.py --site --archives. No network or
deployment mutation occurs. Existing laboratory code and numerical data remain
outside this metadata refresh.
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import shutil

from release_freshness import (ROOT, PDFS, check_release, digest,
                              excluded_credential_path, site_copy_map)


def replace_once(text: str, pattern: str, replacement: str, name: str) -> str:
    updated, count = re.subn(pattern, lambda _: replacement, text, flags=re.S)
    if count != 1:
        raise ValueError(f"Expected exactly one {name} text region, found {count}")
    return updated


def refresh(root: Path = ROOT) -> dict:
    report = check_release(root)
    if report["status"] != "passed":
        raise ValueError("Release sources are not ready: " + json.dumps(report["failures"][:12]))
    summary = report["summary"]
    count = summary["local_finite_declarations"]
    claims = summary["written_claims"]
    pages = summary["pdfs"]["main"]["pages"]
    fluid_pages = summary["pdfs"]["fluid-extension"]["pages"]
    site = root / "extension/site"
    copies = site_copy_map(root)
    for job, record_name, site_pdf, site_record in PDFS:
        copies["extension/manuscript/" + record_name] = "verification/" + site_record
        copies["extension/manuscript/" + job + ".pdf"] = "downloads/" + site_pdf
    for path in sorted((root / "extension/lean/final-verification").rglob("*")):
        if path.is_file() and not excluded_credential_path(path.relative_to(root)):
            relative = path.relative_to(root / "extension/lean/final-verification").as_posix()
            copies[path.relative_to(root).as_posix()] = "verification/lean-current/" + relative
    for original, target in copies.items():
        destination = site / target
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(root / original, destination)

    readme_path = site / "README.md"
    readme = readme_path.read_text()
    readme = re.sub(r"Compiled monograph: \d+ pages", f"Compiled monograph: {pages} pages", readme)
    readme = re.sub(r"Standalone fluid supplement: \d+ pages",
                    f"Standalone fluid supplement: {fluid_pages} pages", readme)
    section = f"""## Current proof and source evidence

The [claim register](verification/claim-register.md) inventories
**{claims['claim_environments']} named environments**, including
{claims['by_status']['local_argument_present']} local arguments,
{claims['by_status']['conditional_local_argument']} conditional arguments,
{claims['by_status']['external_cited']} cited external results, and
{claims['by_status']['proposed_open_problem']} open problem. It records
**{claims['attached_proof_environments']} attached written proofs**. Presence of
a written argument does not certify its correctness. The selected external
statements in prose retain their distinct source and proof-scope classifications.

The [current selected Lean record](verification/lean-current/verification.json)
contains **{count} kernel-checked declarations in {summary['local_modules']} modules**.
The [formal type map](verification/formal-type-map.md) maps
**{claims['verified_declarations_mapped_to_precise_components']} declarations** to
precise components of **{claims['environments_with_partial_formal_components']}
manuscript environments**. No complete composite manuscript environment is
marked fully formalized. The source hashes, exact printed types, actual axiom
dependencies and module logs accompany the record and the recursive Lean archive.

The selected checks use Lean 4.24.0 and the pinned mathlib revision. Their
foundational dependencies are limited to `propext`, `Classical.choice` and
`Quot.sound`. They trust cached compiled imports; they do not independently
rebuild every dependency or formalize the entire monograph. The four-module,
82-declaration manifests retained elsewhere are historical evidence.

The library-backed cryptographic implementation has
**{summary['crypto_tests']} passing test methods** in its
[current regression record](verification/crypto/verification.json). Those tests
exercise the implemented interfaces and malformed-input rejection. They do not
prove computational security or certify a deployment.

The [release summary](verification/release-summary.json) binds these displayed
counts and the two PDF records to their source hashes. The separate upstream
Navier–Stokes check remains **incomplete**, as recorded in the
[current build status](verification/final-pass/upstream-build-current.json).
Local finite-interface certificates do not establish that continuum theorem.

The [review ledger](verification/review-ledger.md) retains historical audits at
their original scope. Fluid sources have separate
[microscopic](verification/navier-stokes/microscopic-source-review.md),
[Farhat](verification/navier-stokes/farhat-review.md), and
[quantum-algorithm](verification/navier-stokes/quantum-algorithms-review.md)
records. They distinguish full-text reading, selected passages, image inspection
and inaccessible originals. The prior 249-segment video transcript review lacks
a retained executor-local transcript export and content hash. The nine current
Farhat decks contain 627 PDF pages including overlays; they are replacements
for unavailable historical filenames, not a claim of identical editions.

"""
    readme = replace_once(readme,
        r"## Current proof and source evidence\n.*?(?=## Numerical verification and browser inspection)",
        section, "README proof evidence")
    readme = readme.replace(
        "The research repository and the managed website checkout have separate commit\nand deployment records.",
        "The Pages release combines this companion with the inherited project material;\npublication and machine synchronization are recorded separately from local validation.")
    readme = readme.replace(
        "Separate rendered-page reviews cover the\n[main manuscript's inspected pages](verification/main-fluid-pdf-visual-qa.json)\nand the [fluid supplement](verification/fluid-pdf-visual-qa.json).",
        "Earlier rendered-page reviews are retained as historical records for the\n[main manuscript](verification/main-fluid-pdf-visual-qa.json) and\n[fluid supplement](verification/fluid-pdf-visual-qa.json); their hashes identify\nthe editions they inspected. Current build freshness is checked independently.")
    readme = readme.replace(
        "[build-attempt record](verification/navier-stokes/release-build-verification.json)",
        "[current build-attempt record](verification/final-pass/upstream-build-current.json)")
    readme_path.write_text(readme)

    index_path = site / "index.html"
    index = index_path.read_text()
    index = re.sub(r"\d+-PAGE RESEARCH MONOGRAPH", f"{pages}-PAGE RESEARCH MONOGRAPH", index)
    index = re.sub(r"<h3>\d+ selected formal declarations</h3>",
                   f"<h3>{count} selected formal declarations</h3>", index)
    proof = (f'<p id="proofStatus">The selected formal development has {count} declarations '
             f'in {summary["local_modules"]} modules, checked with Lean 4.24.0 and pinned Mathlib. '
             'It covers finite algebra, quantum characters, typed diagrams, fluid interfaces, '
             'reduction contracts and transport bounds. The complete monograph and external '
             'continuum theorems remain outside this selected formal scope.</p>')
    index = replace_once(index, r'<p id="proofStatus">.*?</p>', proof, "proof status")
    details = ('<p id="proofDetails">The <a href="verification/lean-current/verification.json">'
               'current source-hashed Lean record</a> contains exact types, axiom reports and '
               'per-module logs. The <a href="verification/claim-register.md">written-claim '
               'register</a> maps selected formal components to manuscript statements. The '
               '<a href="verification/release-summary.json">release summary</a> records PDF '
               'and implementation evidence. Numerical residuals are separate from Lean proof '
               'certificates; the <a href="verification/final-pass/upstream-build-current.json">'
               'independent upstream Navier–Stokes build</a> remains incomplete.</p>')
    index = replace_once(index, r'<p id="proofDetails">.*?</p>', details, "proof details")
    index_path.write_text(index)

    anchors = ["extension/manuscript/build-verification.json",
               "extension/manuscript/fluid-build-verification.json",
               "extension/lean/final-verification/verification.json",
               "extension/review/claim-register.json", "extension/review/formal-type-map.json",
               "extension/crypto/verification.json",
               "extension/review/final-pass/upstream-build-current.json",
               "extension/code/release_freshness.py", "extension/code/refresh_site_release.py"]
    record = {"schema_version": 1, "summary": summary,
              "source_sha256": {name: digest(root / name) for name in anchors},
              "copied_files": [{"source": original, "target": target,
                                "sha256": digest(root / original)} for original, target in sorted(copies.items())],
              "scope": "Public metadata generated from source-current local records. This does not attest deployment, upstream continuum proof verification, whole-manuscript formalization or cryptographic security."}
    (site / "verification/release-summary.json").write_text(json.dumps(record, indent=2) + "\n")
    return record


def main() -> int:
    try:
        result = refresh()
    except (ValueError, OSError) as error:
        print(str(error))
        return 1
    print(json.dumps({"status": "refreshed", "copied_files": len(result["copied_files"]),
                      "summary": result["summary"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
