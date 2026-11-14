# Final document build continuation

Completed 13 November 2026, Pacific time. Both document entry points compile
successfully from the current, stable source inventory.

| Document | Physical pages | Bytes | SHA-256 |
|---|---:|---:|---|
| [Research monograph](../../manuscript/main.pdf) | 341 | 2,145,675 | `74910b1c9d54d2112386198e46e75df6a7f24b2ccc006806f3923c087369ea7b` |
| [Fluid supplement](../../manuscript/fluid-extension.pdf) | 90 | 851,343 | `170fe2fb31d43e7fef6c0d2a5b162d66cf33d9b7cba54de16ec11b7124c91721` |

Each final build reports zero overfull boxes, missing characters, undefined
citations, undefined references, undefined-reference summaries and BibTeX
warnings. The build manifests bind the exact PDF bytes, conservative source
inventory, build driver and locally generated font map. Both record that the
source inventory stayed unchanged throughout compilation.

## Runtime repair

The supplied TeX binaries and macro/font trees were already installed. The
generated `ls-R` database symlinks were broken, while Kpathsea's default `!!`
prefixes restricted lookup to those missing databases. Consequently the first
build could not locate the existing `pdflatex.ini`.

`build_pdf.py` now retries lookup through the same existing TeX trees with
database-only restrictions removed in the build subprocess's environment. If
the generated `pdftex.map` is absent, it constructs a project-local map from
the installed Computer Modern, AMS and Latin Modern maps. The component hashes
are recorded. No packages were downloaded, no global TeX configuration was
edited, and no system-wide database or font-map command was run.

The build driver additionally hashes all declared inputs before compilation and
rejects a source inventory or driver change before writing a successful final
manifest. This prevents concurrent edits from producing a mixed-source success
record. It retains the existing source inventory expected by the release gate.

## Document changes

- Updated two cryptography test-count references from 25 to 31 and described
  the six permanent boundary regressions already executed.
- Updated the TransportContracts opening scope count from eleven to seventeen,
  matching the current verified module.
- Reflowed long commit and Lean declaration names, displayed the six module
  counts in a compact table, and added a discretionary hyphen to a long word.
  These layout changes resolve the observed overfull boxes without changing
  the mathematical claims or hypotheses.

## Evidence and visual review

The authoritative per-document records are
[build-verification.json](../../manuscript/build-verification.json) and
[fluid-build-verification.json](../../manuscript/fluid-build-verification.json).
Final command output is preserved in `pdf-main-build-continuation.log` and
`pdf-fluid-build-continuation.log`; the full TeX logs are the existing
`build-verified.log` and `fluid-build-verified.log` beside the manuscripts.
The [continuation manifest](pdf-build-continuation-20261113.json) hashes those
records and the changed source files.

Poppler's font inventory reports **48 embedded fonts** in the monograph and
**28 embedded fonts** in the supplement; every listed font is embedded. Seven
representative physical pages were rendered at 100 dpi for the final visual
review: monograph pages 1, 110 and 292; supplement pages 1, 57, 61 and 66. The
root integration task records the visual inspection separately. Rendered
representative pages and clean TeX logs do not constitute a visual inspection
of every page or an independent mathematical proof audit.

## Rebuild

```sh
python extension/manuscript/build_pdf.py --main fluid-extension --min-pages 60
python extension/manuscript/build_pdf.py
```

The remaining release integration must regenerate the claim register after
the source changes, refresh the site copies and archives, and check the actual
deployed artifacts against these final hashes.

## Final count-consistency follow-up

Three remaining passages now distinguish the historical four-module/82-declaration
package from the current six-module/115-declaration package. Both documents were
rebuilt with stable inputs; page counts remain341 and90 and every typesetting
warning count remains zero. Seven earlier selected renders are pixel-identical;
four pages containing the corrected wording were additionally inspected.
The final visual record covers11 physical pages and is stored separately.
