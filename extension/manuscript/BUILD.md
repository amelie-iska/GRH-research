# Rebuilding the monograph

Run from this directory:

```sh
python3 build_pdf.py
python3 build_pdf.py --main fluid-extension --min-pages 1
```

The build requires a conventional TeX installation with `pdftex`, `bibtex`,
`kpsewhich`, LaTeX's base formats and macros, Latin Modern fonts, the AMS
packages, `mathtools`, `geometry`, `microtype`, `graphicx`, `booktabs`,
`longtable`, `array`, `enumitem`, `xcolor`, `fancyhdr`, `listings`, `natbib`,
`url`, and `hyperref`. Python uses only its standard library. The included
figure PDFs are inputs; figure generation is separate.

If the machine has its TeX macros installed but no generated `pdflatex.fmt`,
the helper generates an isolated format in `.texbuild`. It does not modify
the global TeX installation, shell settings, or another process. Shell escape
is disabled for manuscript compilation.

If only `listings` is absent, an optional project-local bootstrap is available:

```sh
python3 build_pdf.py --fetch-listings
```

It downloads the official [CTAN listings archive](https://mirrors.ctan.org/macros/latex/contrib/listings.zip)
with normal TLS verification, checks SHA-256
`aed069ff5c67e5458efa0f2f03f45987876db0cf9d1628111da5795bda0154ce`, and
generates the package under `.texbuild/vendor`. That archive contains
listings 1.11b, dated 2025-11-14. If CTAN replaces the archive, the checksum
gate deliberately rejects it; review a replacement before updating the pin.
No network operation is performed when `listings.sty` is already available.

The helper runs the first LaTeX pass, BibTeX, and the required reference passes.
It writes the authentic final TeX log to `build-verified.log` and records PDF
page count, PDF hash, input hashes, engine version, and warnings in
`build-verification.json`. It rejects undefined references/citations,
missing-character reports, overfull boxes, and fewer than 100 pages. Ordinary
underfull-box warnings and bibliographic metadata warnings are separately
inspectable; the machine gates do not replace visual review. The standalone
fluid supplement uses the same chapters and has its own PDF, log and
`fluid-build-verification.json`; its page count is not padded to a target.

The authoritative selected formal proofs remain in
`../lean/BridgeTheorems.lean`, `../lean/QuantumInterfaces.lean`, and
`../lean/DiagramGrammar.lean`, and `../lean/FluidInterfaces.lean`.
`lean-listings-unicode.tex` only maps their
Unicode characters to corresponding printed glyphs. The proof source is
neither transliterated nor edited for the PDF.
