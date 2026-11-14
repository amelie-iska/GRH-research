#!/usr/bin/env python3
"""Package the authored companion; optionally archive the complete committed tree.

Run from any directory. Generated downloads are excluded from their own source
archive. The compact companion contains every new manuscript, proof, program,
review record and laboratory, while the complete archive additionally contains
the inherited repository and assembled legacy site. Git submodules remain
separate pinned dependencies in both forms.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[2]
STAMP = (2026, 11, 13, 0, 0, 0)
UPSTREAM = "dbd954eede479a5129831e4e7c30537389ae973d"


def digest(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def included(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    if any(part in {"__pycache__", ".texbuild", ".lake", "node_modules"}
           for part in rel.parts):
        return False
    if rel.parts[:3] in {("extension", "site", "legacy"),
                         ("extension", "site", "downloads")}:
        return False
    if path.suffix in {".pyc", ".olean", ".ilean", ".aux", ".blg", ".fls"}:
        return False
    if rel.as_posix() in {"extension/manuscript/main.log", "extension/manuscript/fluid-extension.log"}:
        return False  # Identical authentic output is in build-verified.log.
    return path.is_file()


def zip_bytes(archive: zipfile.ZipFile, name: str, data: bytes) -> None:
    info = zipfile.ZipInfo(name, STAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    archive.writestr(info, data, compresslevel=9)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--complete", action="store_true",
                        help="Also archive the complete clean committed tree")
    args = parser.parse_args()
    out = args.output.resolve()
    if out == ROOT or ROOT in out.parents:
        raise SystemExit("Keep release archives outside the source repository.")
    out.mkdir(parents=True, exist_ok=True)
    files = [ROOT / n for n in ("README.md", "README-UPSTREAM.md", ".gitmodules")]
    files += [p for p in (ROOT / "extension").rglob("*") if included(p)]
    files = sorted(set(p for p in files if p.is_file()))
    manifest = {
        "format": 1,
        "upstream_repository": "https://github.com/amelie-iska/GRH-research",
        "upstream_commit": UPSTREAM,
        "scope": "New companion, without the duplicated legacy tree or generated downloads",
        "submodules_recursively_vendored": False,
        "files": [{"path": str(p.relative_to(ROOT)), "bytes": p.stat().st_size,
                   "sha256": digest(p)} for p in files],
    }
    readme = """# Research companion source archive

Start with README.md. The compiled paper is extension/manuscript/main.pdf;
its complete LaTeX project is in the same directory. The Lean files, actual
verification logs, CPU/GPU programs and results, mathematical claim register,
source reviews, and new interactive laboratories are included.

This compact archive excludes the duplicated legacy site and its large data
sets. Obtain the separate Complete_Repository.zip, or clone the pinned original
repository and overlay this archive, then run:

    python3 extension/code/prepare_legacy.py

The original Git submodules are recorded in .gitmodules; their full contents
are separate dependencies. Uploaded book scans, full OCR transcriptions and
downloaded third-party papers are not redistributed.

To serve the new laboratories locally, run:

    python3 -m http.server 8000 --directory extension/site

The downloads directory is generated during publication and is excluded from
this archive to avoid recursion. The manuscript is available directly above.
ARCHIVE-MANIFEST.json records a SHA-256 hash for every included source file.
"""
    compact = out / "Research_Companion_Source.zip"
    with zipfile.ZipFile(compact, "w") as archive:
        for path in files:
            zip_bytes(archive, str(path.relative_to(ROOT)), path.read_bytes())
        zip_bytes(archive, "ARCHIVE-MANIFEST.json",
                  (json.dumps(manifest, indent=2) + "\n").encode())
        zip_bytes(archive, "SOURCE-README.md", readme.encode())
    pdf = out / "Orders_Complexes_Cryptography_YangMills.pdf"
    tex = out / "main.tex"
    shutil.copy2(ROOT / "extension/manuscript/main.pdf", pdf)
    shutil.copy2(ROOT / "extension/manuscript/main.tex", tex)
    fluid_pdf = out / "Fluid_Dynamics_Quantum_Information_and_Navier_Stokes.pdf"
    fluid_tex = out / "fluid-extension.tex"
    shutil.copy2(ROOT / "extension/manuscript/fluid-extension.pdf", fluid_pdf)
    shutil.copy2(ROOT / "extension/manuscript/fluid-extension.tex", fluid_tex)
    lean = out / "Lean4_Proofs_and_Verification.zip"
    with zipfile.ZipFile(lean, "w") as archive:
        for path in sorted((ROOT / "extension/lean").iterdir()):
            if path.is_file():
                zip_bytes(archive, path.name, path.read_bytes())
    artifacts = [pdf, tex, fluid_pdf, fluid_tex, compact, lean]
    if args.complete:
        dirty = subprocess.check_output(["git", "status", "--porcelain"], cwd=ROOT)
        if dirty.strip():
            raise SystemExit("Commit the reviewed tree before --complete.")
        complete = out / "Complete_Repository.zip"
        subprocess.run(["git", "archive", "--format=zip", "-9",
                        "--prefix=Orders-Complexes-Cryptography-YangMills/",
                        f"--output={complete}", "HEAD"], cwd=ROOT, check=True)
        artifacts.append(complete)
    report = {p.name: {"bytes": p.stat().st_size, "sha256": digest(p)}
              for p in artifacts}
    (out / "SHA256SUMS.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
