# Independent source and semantic fidelity review

4 November 2026. All reads/checks and review writes ran on iska-linux-vscode. Production, existing artifacts, environments, credentials, models and Mac files were not modified by this reviewer. This is a transformation-fidelity review, not whole-book proof verification, browser/visual approval or Lean formalization.

## Verdict

ACCEPT the full-PDF candidate outputs/book-integration-20261104/v4 and corrected native-MathML candidate native-v2 within the stated route. The first native-v1 candidate had a material insertion-order bug; it was caught before promotion, retained, and corrected in v2. Root must still inspect visuals/browser and decide promotion.

## Full-PDF source preservation

Independently reconstructed v4/main.tex from source-expansion-before-diagram-replacement.tex. It is byte-exact after only19 documented diagram-environment substitutions, replacement of now-unused TikZ package imports by existing graphicx/xcolor, and removal of the unused TikZ library declaration. No other prose, formula, caption, label or source ordering changed in the compiled expansion. All recorded source and static-figure hashes still match current inputs.

All45 pre-existing book/chapters source files are byte-identical to public origin/main. The main-file delta from the saved pre-integration source consists only of date3→4November, the explicitly authorized private→public reader-guide sentence, and the new PartVI plus three chapter inputs. Both original source volumes are outside these transformations and retain their existing integrity scope.

All19 diagram environments match the accepted source-SHA manifest and accepted SVG byte hashes in exact order. Eighteen compiled diagram PDFs are byte-identical to their preserved cache PDFs; each cache TeX document has the matching diagram as its exact sole document body. One source-matched accepted SVG is converted with already installed librsvg/cairo. No diagram contains a lost TeX label/input. The standalone5pt border is explicitly trimmed on insertion, retaining vector assets rather than inventing a package shim. This is reuse of previously accepted diagram geometry, not fresh TikZ compilation or an independent pixel-level proof of the conversion.

The actual PDF TOC identifies the new part as VI. Existing source/math/prose retention is verified by exact data comparison, not inferred from page count. The full candidate is233pages/40chapters according to its build record; clean PDF logs and visual layout remain root's separate checks.

## Native MathML and bounded renderer syntax

Only the three new reviewed chapters are fed through the existing Pandoc3.10 binary. Reviewed every unified-diff normalization: five old-style rm math words become mathrm; nine hbox text strings become text; fourteen generalized-atop condition stacks become substack; four notag tokens are removed from the rendering copy only. These are renderer syntax/layout changes on the closed supplied expressions, preserving all mathematical operands, predicates and prose. Original production TeX inputs remain the actual canonical mathematical source; this is not a claimed general TeX equivalence transformer.

Independent AST inspection finds no RawBlock/RawInline fallback. All860 source Math nodes match the MathML TeX-annotation multiset exactly, and no rendered node text outside annotations contains an unparsed backslash command. The annotations are provenance/accessibility content, not a raw-TeX display fallback. The converter's recorded warnings are zero. This does not certify Pandoc as a proof kernel; it verifies the documented input transformations and completeness checks for this exact supplement.

All33 explicit labels survive. Equation numbers, six theorem/proof environments and reference-link text were independently checked against the complete PDF aux. They match chapters38–40's actual numbering. The new PartVI and three TOC links are additive; all13 canonical iframe tools are retained without duplication. Every old MathML/table/iframe subtree remains byte-identical under XML serialization; removing the new content/TOC insertions and reversing exactly the two authorized old-prose edits recovers the complete baseline HTML string.

## Found and corrected before acceptance

native-v1 used a DOTALL pattern starting at the first unnumbered h2 and ending at Bibliography. It matched Reader's guide at byte2440 through the later Bibliography, so it inserted the new chapters before the guide despite subtree-preservation checks passing. I reported this to root/engineer; v1 remains unpromoted and preserved.

native-v2 now enumerates individual headings, selects the unique heading whose stripped text is exactly Bibliography, requires that position to follow the old final numbered chapter, and asserts the final parsed chapter sequence1..40. Independent checking confirms the corrected order. This is the accepted native candidate; v1's passing preservation receipt is not publication approval.

## Evidence and limits

Independent checker: planning/book-integration-20261104/review/check_fidelity.py.
Report: outputs/checks/2026-11-04-weighted-moment/book-review/fidelity-v1.json.
It verifies exact PDF transformation, all19 diagram/cache relations, all45 old source files, current source/static-figure hashes, reversibility to baseline, ordered chapter sequence,860 MathML/AST annotations, renderer-only normalization counts and actual PDF label/reference numbers.

No dependency installation, alternate Lean toolchain, admission/custom axiom or mathematical completion claim follows. The existing broader book and arithmetic obligations remain open. These candidates integrate the newly reviewed prose/finite certificates; they do not turn the full book into a Lean-checked proof of GRH. This review does not replace root's browser, PDF-image, mobile or accessibility inspection.
