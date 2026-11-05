# Public focused article build

The production helper builds both focused editions from the actual canonical paper sources, without overwriting production PDFs or installing dependencies.

From any working directory, use the absolute helper and fresh output paths:

~~~sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 nice -n15 python3 /PATH/TO/GRH-research/scripts/build_remote_articles.py --edition concise --output /PATH/TO/NEW-CONCISE
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 nice -n15 python3 /PATH/TO/GRH-research/scripts/build_remote_articles.py --edition extended --output /PATH/TO/NEW-EXTENDED
~~~

The extended build defaults to the final package in book/figures/article-grids. Its two accepted PDF vectors, render TeX and original TikZ-cd blocks are preserved byte-identically. The manifest contains repository-relative paths; preview paths point to the accepted vector PDFs themselves, so no JPEG render tree is required. The acceptance record binds the new path-only manifest to root's original semantic and visual acceptance and to the frozen file hashes. The builder verifies that acceptance, exact current diagram source hashes and PDF hashes before use. Arbitrary alternative grid directories still require explicit independent review and visual approval.

The two grids retain exactly15nodes/18arrows and9nodes/12arrows respectively, including all hooks, signs and label sides. Original canonical TikZ source remains untouched. Matching existing diagrams use the accepted source-SHA manifest and existing vector SVGs; previously compiled caches are optional. Installed pdflatex/Poppler and librsvg/Cairo provide the bounded rendering route. Missing tools or source mismatches fail rather than trigger installation or a generic drawing shim.

Every build expands the current actual inputs, writes the original expansion, records input SHA256 values, uses absolute compile and figure paths, and runs three pdflatex passes in an unused output directory. It checks unique labels, resolved references, no overfull boxes and all four newly integrated proof headings. The accepted focused editions contain49and129pages. Both editions were reproduced from cwd /tmp using the packaged default, with canonical source hashes unchanged and PDF text byte-identical to the accepted candidates. Fresh PDF metadata/IDs mean file-byte identity is not promised.

The exact-source logs retain the existing amsmath atop warning in concise and atop/over warnings in extended, plus seven underfull hboxes per edition. These warnings are disclosed rather than hidden by altering source mathematics. Independent source/rendering checks do not establish new analytic theorems, Lean declarations, whole-article formalization or GRH.

The final package is the reproducible diagram input. Historical staging paths in older handoffs identify the preserved original review process; they are not needed by these default commands.
