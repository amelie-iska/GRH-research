# Bounded public SVG reproduction

The optional Linux wrapper supports a cache-independent diagram route:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/build_remote_book_candidate.py --svg-only --output outputs/book-integration-20261104/NEW-PUBLIC-RUN
```

The destination must not exist. The same flag is available on the retained proposed wrapper and directly on `build_isolated.py --consume-book`. No helper installs packages, fetches Git history, authenticates, promotes generated artifacts or changes source data/caches. Without the flag, the earlier preserved-PDF-cache-with-public-SVG-fallback behavior remains available and is explicitly identified in new build records.

This is tested on the existing iska-linux-vscode environment. Required tools are Python3, pdflatex/Poppler, native librsvg/Cairo/GObject, and the existing Pandoc3.10 binary at the renderer's recorded path. Exact paths/versions/hashes are in public-svg-toolchain.json. This records the environment used; it is not an automatic installer or a general cross-platform setup guarantee.

## Inputs and failure gates

public-input-manifest.json lists 113 exact current source/helper/figure/native-asset paths and SHA256 hashes. It also identifies the pinned local Git baseline object `38816daa63af5cb7986c0694e34b4948a3a4ea39:web/book/main.html` with SHA256 `bce3d2b6c7feda66ff03a5a7531300d07b4b054beb915461547ed68566c84545`. A complete clone retaining that history is required; a shallow/source archive without the object fails rather than fetching. Current local-index tracking labels in that snapshot do not determine public-origin availability; the release inventory independently compares exact origin blobs.

For every source diagram, the builder verifies the source environment hash, accepted manifest index/order, SVG byte hash and length. In --svg-only mode it never opens or stats the preserved standalone-PDF cache. Every diagram is converted from its accepted public SVG through the already installed stable C APIs. The same documented standalone5pt border is trimmed; no TikZ package shim or alternate mathematical source is introduced. The complete original expanded source and the bounded package/diagram substitutions remain recorded. Figure bytes are copied unchanged. The native renderer still processes only the reviewed three new chapters, with the same MathML/numbering/source-preservation gates.

## Executed evidence and precise equivalences

- `outputs/book-integration-20261104/public-svg-reproduction-v1/candidate-record.json`: fresh wrapper success, 233 pages/40 chapters, 19 public-SVG conversions, zero recorded diagram-cache reads, 860 new MathML nodes, zero conversion warnings.
- `public-svg-reproduction-v1/comparison.json`: expanded main.tex, main.toc and main.aux are byte-identical to accepted v4. Native HTML and responsive runtime are byte-identical to native-v3. Every source and static figure still matches the recorded hash.
- `public-svg-cache-audit-v1/cache-audit.json`: a complete additional wrapper run under strace open/stat/readlink tracing observed zero accesses under outputs/html-diagrams. This concerns the diagram-PDF cache only; general runtime/TeX/system caches are not claimed absent.
- `public-svg-reproduction-v1/diagram-comparison.json`: all19 standalone PDF page dimensions match accepted v4 exactly. Paired scale-to900 PNGs are retained for every diagram. Root visually reviewed the two largest mean raster-difference pairs (indices13/14) and confirmed the same labels, formulas and arrows, minor border/spacing raster shifts, and no overlap/clipping. The route is accepted within this bounded source-matched-vector scope.

## PDF bytes and searchability limitation

SVGs may represent font glyphs as paths. Converting the accepted SVGs back to PDF retains the vector appearance but can remove the original cached PDF's searchable diagram text. Accordingly the cache-free PDF is not byte-identical to v4, and its extracted full-PDF text is not byte-identical. The comparison report records both hashes rather than presenting equality. Original TeX remains the mathematical source. Source/TOC/aux/native HTML equivalences above do not imply a bit-for-bit PDF reproduction or fresh independent proof verification.

The accepted/published v4 PDF remains the canonical artifact. This public-route test does not replace it. All previous v4/native-v3 and reproduction-v1/v2 records/snapshots remain unchanged; new CLI/helper versions and this new build are separately recorded. No new theorem, Lean coverage or GRH result follows from successful reproduction.
