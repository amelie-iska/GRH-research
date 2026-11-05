# Bounded Linux book integration without installing tooling

This optional route was executed entirely on iska-linux-vscode. It builds reviewable candidates and never publishes or promotes production files. No package installation, authentication, GPU/model job or existing-cache migration is part of the workflow.

## Executed results

- `outputs/book-integration-20261104/v4/main.pdf`:233pages,40chapters,19source-matched diagrams; clean3pass pdflatex log.
- `outputs/book-integration-20261104/native-v3/book/main.html`: chapters1–40 in order,860new nativeMathML expressions with zero conversion warnings/raw-TeX AST nodes/fallbacks,33explicit labels and35resolved references. Six new theorem environments and six proofs retain full-book numbering.
- All5356old MathML,384old table and13unique iframe subtrees remain unchanged; the new total is6216MathML and385tables. New chapters are inserted before Bibliography with proper TOC entries and PartVI heading. Only the old guide's public-source sentence and title date are intentionally corrected.
- `reproduction-v2/candidate-record.json` records the fresh rebuild including the responsive runtime. Its HTML/runtime are byte-identical to native-v3; extracted PDF layout text is byte-identical to v4 (`reproduction-comparison.json`).
- `v4/preservation-audit.json` reverses the diagram/package substitutions to the exact actual expanded book source and verifies old source retention. Independent review: `review/SEMANTIC_FIDELITY_REVIEW.md`.

- `outputs/checks/2026-11-04-weighted-moment/native-browser-v9/browser.json`: final Firefox QA passes at 320/390/768/1440 px and reflow back to 390 px. Math stays at 18 px and wide formulas scroll in focusable HTML containers; no page overflow or scaling. All old MathML/table/iframe browser DOM hashes match the pinned baseline.
- Native-v3 adds only reversible supplement CSS and `reviewed-math-scroll.js` to the accepted native-v2 content. The unchanged independent checker passes native-v3 in `native-browser-v7/fidelity.json`. All prior failed/accepted candidates remain preserved.
- Root inspected and accepted desktop/mobile/light/scrolled/stable-night screenshots and selected PDF pages. Final night base-color contrast is 14.5379:1 after the actual shared-theme transition settles. Three malformed old TeX4ht `munder` nodes remain byte-identical to the old baseline; they are inherited diagnostics, with none in the 860 new expressions.

Root owns promotion and publication. These remain candidates until that step. Exact bounded copy targets and hashes are in `outputs/checks/2026-11-04-weighted-moment/native-browser-v9/promotion-plan.json`; diagnosis, limitations and handoff are in [MOBILE_QA.md](MOBILE_QA.md). No public deployment or new Lean verification is implied by this worker's completion.

## Reproduction

The reviewed proposed wrapper is `proposed-build-remote-book-candidate.py`, intended for the optional production destination `scripts/build_remote_book_candidate.py` after root review. It uses only the existing Python runtime, pdflatex/Poppler, librsvg/cairo and the already installed Pandoc3.10 at `/home/iska/miniconda3/envs/tokengt/bin/pandoc`. Tool hashes/versions are pinned in `existing-tools.json`.

From the repository root, before or after production HTML promotion:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 planning/book-integration-20261104/proposed-build-remote-book-candidate.py --output outputs/book-integration-20261104/NEW-RUN
```

The output must not exist. The wrapper reconstructs the37chapter HTML baseline from the local immutable Git object `38816daa63af5cb7986c0694e34b4948a3a4ea39:web/book/main.html` and checks SHA256 `bce3d2b6c7feda66ff03a5a7531300d07b4b054beb915461547ed68566c84545`. It does not fetch or authenticate. It then runs the two helper scripts into fresh PDF/native subdirectories, copies the additive reviewed-math-scroll.js runtime, verifies matching book-source hashes and writes a candidate record. Missing baseline objects/tooling cause a failure rather than a download.

This is a bounded Nov4 integration of the three named chapters after a pinned37chapter baseline. Extending the chapter set or changing accepted diagram sources requires an explicit renderer/baseline update and review; it is not a general substitute for a maintained make4ht pipeline.

## Public reproduction without local diagram-PDF caches

The bounded `--svg-only` route is verified in `outputs/book-integration-20261104/public-svg-reproduction-v1`. It renders all 19 accepted, source-hash-matched public SVGs with the existing librsvg/Cairo C APIs and reads no standalone-PDF diagram cache. It rebuilds 233 pages/40 chapters with a clean final log, byte-identical expanded source/TOC/aux to accepted v4, and byte-identical native HTML/runtime to native-v3. A complete second wrapper run under `strace` recorded zero accesses to `outputs/html-diagrams` (`public-svg-cache-audit-v1/cache-audit.json`). No cache was moved, deleted or altered.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/build_remote_book_candidate.py --svg-only --output outputs/book-integration-20261104/NEW-PUBLIC-RUN
```

Use a fresh output directory and the recorded existing toolchain. This route needs no private diagram cache, but it still needs the published chapter/figure/SVG inputs and pinned baseline Git object. [Public input manifest](public-input-manifest.json), [tool versions and hashes](public-svg-toolchain.json) and [scope/limitations](PUBLIC_REPRODUCTION.md) define the tested inputs and environment. Local-index untracked status in the manifest is historical context, not a claim an asset is absent from public origin.

SVG glyphs can be paths: cache-free diagram PDF bytes and PDF text searchability differ from the cached-PDF edition. Do not claim PDF byte/text identity or replace the accepted/published v4 artifact with this diagnostic rebuild. All 19 standalone page dimensions match; root reviewed the largest raster-difference pairs (indices 13/14), confirming the same labels/formulas/arrows with minor raster/border/spacing shifts and no overlap/clipping. This is a bounded public reproduction route, not fresh TikZ compilation or a new mathematical/formal verification.

## Fidelity mechanisms

`build_isolated.py --consume-book` follows every actual book input in order. Each of the19TikZ source environments must match the existing diagram manifest and accepted SVG hash. Eighteen existing standalone PDFs are reused; the remaining accepted vector SVG is rendered by the existing librsvg/cairo C APIs through stdlib ctypes. The added standalone5pt borders are trimmed. Only the now-unused TikZ package/library imports are replaced, with already installed xcolor loaded explicitly; no package shim stands in for a diagram or theorem. All other actual source is retained exactly. Figure assets are copied, never modified.

`render_native.py` processes only the three new shared chapters through existing Pandoc. Renderer-only equivalent syntax normalizations are recorded:5old-style font commands,9hbox word boxes,14atop groups and4notag directives. Original TeX is retained separately; all860MathML annotations match the parsed math AST. PDF aux labels supply section/theorem/equation numbers and link targets. Missing labels, duplicate IDs, wrong chapter order, conversion warnings, raw-TeX nodes, source changes or changed old subtrees fail closed.

The initial native-v1 broad Bibliography regex bug was found by independent review and corrected before promotion. Native-v1 and the earlier unit/optional-Python-bridge build failures remain preserved. The exact heading selector and complete1–40order assertion now prevent that error.

No new analytic/category/whole-book Lean theorem or GRH proof follows from a successful PDF/HTML build. Actual mathematical scopes and external dependencies remain in the reviewed source chapters and claim ledger.
