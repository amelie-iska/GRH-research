#!/usr/bin/env python3
"""Compile this monograph using a project-local format when necessary.

No global TeX configuration is changed. The optional listings bootstrap uses
the official CTAN archive and verifies the exact archive reviewed for this build.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import zipfile


ROOT = Path(__file__).resolve().parent
BUILD = ROOT / ".texbuild"
LISTINGS_URL = "https://mirrors.ctan.org/macros/latex/contrib/listings.zip"
LISTINGS_SHA256 = "aed069ff5c67e5458efa0f2f03f45987876db0cf9d1628111da5795bda0154ce"


def run(command: list[str], stage: str, *, cwd: Path = ROOT,
        env: dict[str, str] | None = None) -> str:
    result = subprocess.run(command, cwd=cwd, env=env, text=True,
                            errors="replace", stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, check=False)
    (BUILD / f"{stage}.stdout").write_text(result.stdout)
    print(f"{stage}: exit {result.returncode}", flush=True)
    if result.returncode:
        print(result.stdout[-8000:], file=sys.stderr)
        raise SystemExit(result.returncode)
    return result.stdout


def locate(name: str, env: dict[str, str]) -> str:
    result = subprocess.run(["kpsewhich", name], env=env,
                            text=True, capture_output=True, check=False)
    return result.stdout.strip()


def prepare_local_tex_runtime(env: dict[str, str]) -> dict:
    """Use installed TeX trees even when their runtime ls-R links are absent.

    Some bundled environments provide the complete read-only TeX installation
    without the generated /var/lib/texmf databases or font map. Repair search
    behavior for this child process only; never run a system-wide mktexlsr or
    updmap. Ordinary complete TeX installations retain their normal settings.
    """
    evidence: dict = {"filesystem_search_fallback": False, "local_font_map": None}
    if not locate("pdflatex.ini", env):
        trees = subprocess.check_output(["kpsewhich", "-var-value=TEXMF"],
                                        env=env, text=True).strip()
        # Kpathsea's !! prefix forces database-only lookup. Removing it permits
        # lookup in the existing tree when a generated database is unavailable.
        if "!!" in trees:
            env["TEXMF"] = trees.replace("!!", "")
            evidence["filesystem_search_fallback"] = True
        if not locate("pdflatex.ini", env):
            raise SystemExit("pdflatex.ini is absent from the installed TeX trees. "
                             "Install the LaTeX base macros before building.")
    if not locate("pdftex.map", env):
        components = ["cm.map", "cmextra.map", "symbols.map", "euler.map", "lm.map"]
        paths = [Path(locate(name, env)) for name in components]
        if not all(path.is_file() for path in paths):
            missing = [name for name, path in zip(components, paths) if not path.is_file()]
            raise SystemExit("Cannot construct the local font map; missing " + ", ".join(missing))
        font_dir = BUILD / "fonts"
        font_dir.mkdir(parents=True, exist_ok=True)
        font_map = font_dir / "pdftex.map"
        font_map.write_text("\n".join(path.read_text() for path in paths) + "\n")
        env["TEXFONTMAPS"] = str(font_dir) + "//:" + env.get("TEXFONTMAPS", "")
        evidence["local_font_map"] = {
            "path": str(font_map.relative_to(ROOT)),
            "sha256": hashlib.sha256(font_map.read_bytes()).hexdigest(),
            "components": {name: hashlib.sha256(path.read_bytes()).hexdigest()
                           for name, path in zip(components, paths)},
        }
    return evidence


def source_inventory(job: str) -> dict[str, str]:
    inputs = [ROOT / (job + ".tex"), ROOT / "lean-listings-unicode.tex"]
    inputs.extend(sorted(ROOT.glob("*.bib")))
    inputs.extend(sorted((ROOT.parent / "lean").glob("*.lean")))
    inputs.extend(sorted((ROOT / "chapters").glob("*.tex")))
    inputs.extend(sorted((ROOT / "figures").glob("*.pdf")))
    return {os.path.relpath(path, ROOT): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in inputs}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch-listings", action="store_true",
                        help="fetch the hash-verified official listings archive if absent")
    parser.add_argument("--min-pages", type=int, default=100)
    parser.add_argument("--main", default="main",
                        help="TeX entry-point basename (main or fluid-extension)")
    args = parser.parse_args()
    if args.main not in {"main", "fluid-extension"}:
        raise SystemExit("Unknown manuscript entry point")
    job = args.main
    source_hashes = source_inventory(job)
    builder_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    for executable in ("pdftex", "bibtex", "kpsewhich"):
        if not shutil.which(executable):
            raise SystemExit(f"Required TeX executable is absent: {executable}")
    BUILD.mkdir(exist_ok=True)
    env = os.environ.copy()
    vendor = BUILD / "vendor" / "listings"
    env["TEXINPUTS"] = str(vendor) + "//:" + env.get("TEXINPUTS", "")
    runtime_evidence = prepare_local_tex_runtime(env)

    fmt = BUILD / "pdflatex.fmt"
    if not fmt.exists():
        run(["pdftex", "-ini", "-etex", "-interaction=nonstopmode",
             "-halt-on-error", "-jobname=pdflatex", "-progname=pdflatex",
             "pdflatex.ini"], "format-generation", cwd=BUILD, env=env)

    if not locate("listings.sty", env):
        if not args.fetch_listings:
            raise SystemExit("listings.sty is absent. Install the normal TeX listings "
                             "package, or rerun with --fetch-listings for a project-local copy.")
        if not shutil.which("curl"):
            raise SystemExit("curl is needed for the optional verified-TLS download.")
        vendor.parent.mkdir(parents=True, exist_ok=True)
        archive = vendor.parent / "listings.zip"
        run(["curl", "--fail", "--location", "--max-time", "60",
             LISTINGS_URL, "--output", str(archive)], "listings-download", env=env)
        actual = hashlib.sha256(archive.read_bytes()).hexdigest()
        if actual != LISTINGS_SHA256:
            raise SystemExit("The CTAN listings archive changed; refusing an unreviewed "
                             f"replacement. Expected {LISTINGS_SHA256}; obtained {actual}.")
        with zipfile.ZipFile(archive) as bundle:
            for member in bundle.infolist():
                target = (vendor.parent / member.filename).resolve()
                if not target.is_relative_to(vendor.parent.resolve()):
                    raise SystemExit("Unexpected archive member outside the local vendor directory.")
            bundle.extractall(vendor.parent)
        run(["pdftex", "-fmt=" + str(fmt.with_suffix("")), "-progname=pdflatex",
             "-interaction=nonstopmode", "-halt-on-error", "listings.ins"],
            "listings-generation", cwd=vendor, env=env)

    command = ["pdftex", "-fmt=" + str(fmt.with_suffix("")),
               "-progname=pdflatex", "-no-shell-escape",
               "-interaction=nonstopmode", "-halt-on-error", job + ".tex"]
    run(command, "latex-pass-1", env=env)
    run(["bibtex", job], "bibliography", env=env)
    run(command, "latex-pass-2", env=env)
    run(command, "latex-pass-3", env=env)
    log = (ROOT / (job + ".log")).read_text(errors="replace")
    if "Rerun to get cross-references right" in log or "Rerun to get outlines right" in log:
        run(command, "latex-pass-4", env=env)
        log = (ROOT / (job + ".log")).read_text(errors="replace")
    evidence_prefix = "build" if job == "main" else "fluid-build"
    (ROOT / (evidence_prefix + "-verified.log")).write_text(log)
    biblog = (ROOT / (job + ".blg")).read_text(errors="replace")
    page_match = re.search(r"Output written on " + re.escape(job) + r"\.pdf \((\d+) pages?", log)
    pages = int(page_match.group(1)) if page_match else None
    pdf = ROOT / (job + ".pdf")
    if source_inventory(job) != source_hashes:
        raise SystemExit("Manuscript inputs changed during compilation; refusing a mixed-source manifest.")
    if hashlib.sha256(Path(__file__).read_bytes()).hexdigest() != builder_hash:
        raise SystemExit("The build driver changed during compilation; rerun against stable inputs.")
    warning_counts = {
        "overfull_boxes": log.count("Overfull "),
        "missing_characters": log.count("Missing character:"),
        "undefined_citation_reports": len(re.findall(r"Citation .* undefined", log)),
        "undefined_reference_reports": len(re.findall(r"Reference .* undefined", log)),
        "undefined_summary_reports": log.count("There were undefined"),
        "bibtex_warnings": biblog.count("Warning--"),
    }
    version = subprocess.run(["pdftex", "--version"], text=True,
                             capture_output=True, check=True).stdout.splitlines()[0]
    manifest = {
        "status": "compiled; visual QA is recorded separately",
        "engine": version,
        "pages": pages,
        "pdf_bytes": pdf.stat().st_size,
        "pdf_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
        "warning_counts": warning_counts,
        "bibtex_warning_details": [line for line in biblog.splitlines() if "Warning--" in line],
        "source_sha256": source_hashes,
        "builder_sha256": builder_hash,
        "sources_unchanged_during_build": True,
        "local_format": ".texbuild/pdflatex.fmt",
        "shell_escape": False,
        "listings_path": locate("listings.sty", env),
        "runtime_preparation": runtime_evidence,
    }
    (ROOT / (evidence_prefix + "-verification.json")).write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({key: manifest[key] for key in
                      ("pages", "pdf_bytes", "pdf_sha256", "warning_counts")}, indent=2))
    blocking = sum(value for key, value in warning_counts.items() if key != "bibtex_warnings")
    if blocking or pages is None or pages < args.min_pages:
        raise SystemExit("The PDF was generated but did not pass the requested typesetting gates.")


if __name__ == "__main__":
    main()
