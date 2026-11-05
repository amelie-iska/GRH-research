# Representative PDF visual review

PASS for12NEW representative physical pages across all four fresh67/183/25/74-page editions. Pages were located with existing pdftotext; pdftoppm rendered original source PDFs at1600pixels maximum dimension, and each PNG was inspected through SSH/base64/functions image. No recompilation, source edit, product change, cleanup or promotion occurred. All source PDFs and existing build receipts remain exact.

| Edition | Physical pages visually inspected |
|---|---|
| concise-v1 | 59, 60 |
| extended-v1 | 170, 171, 175, 176 |
| notes-concise-v1 | 24, 25 |
| notes-extended-v1 | 67, 68, 72, 73 |

The selected theorem/control pages were inspected in every edition; the Stieltjes and operator-budget pages were additionally inspected in both extended editions. Concise editions intentionally omit the detailed PIT subsection. No clipping, equation-number collision, table overlap, missing visible math glyph or unreadable scope/reference text was found. The theorem continuation in concise pages59–60 is normal. Tables and their negative values remain distinguishable; the full smooth-step fraction and weak scaled inequalities are visible.

All recorded pdftotext word-coordinate boxes lie within their physical pages. Minimum selected-page word margins are above69points horizontally and above38points at the bottom (including footers). This coordinate check supplements visual inspection and is not a claim that extracted text perfectly encodes every math glyph.

The original bbox XML parser stopped on pdftotext math-font control text U+0001 and delimiter codes U+0012/U+0013 inside word bodies. The v1 script, first two renders and failure record were preserved. The v2 reader parses every strict coordinate tag without interpreting those text bodies; no word boxes are excluded. Actual indicator and delimiter glyphs render correctly in the inspected PNGs. No PDF repair or recompile was needed.

This is a representative layout review, not an inspection of every page or a new mathematical/numerical proof. Root’s book visual/native QA and the existing exact-source/log checks are separate evidence.

## concise-v1 physical page59

Theorem39.1 and equations44–53 are legible; sum conditions, tall brackets and right equation numbers have clear separation. The theorem continues onto page60 without clipping.

PNG SHA256 `baa40dfaa2bbab78aa6a44e4edaf1ae0244f2590bfb2c18047bfaa2b4874afba`.

## concise-v1 physical page60

Critical bound54, indicator glyph, full smooth-step construction and both control tables are legible. The negative raw value−256 is distinguishable from its preceding column; all table rows and scope text fit.

PNG SHA256 `27cf64b3e223c26bfa5a0f1728cf0448753c2745abbc790c0c82b7cf1c799c18`.

## extended-v1 physical page170

TheoremS69.1 and all displayed correction bounds fit with readable subscripts and separated numbers81–85. The parameter table at the foot stays above the footer.

PNG SHA256 `d77f6ac244fb80f45814d1f317c4fc1b4397bf8fdb7638e31f5c27b47d9b1d5e`.

## extended-v1 physical page171

Smooth-step fraction and raw control table are clear. SectionS70 heading, common-divisor proof and bottom invariance formula88 fit without clipping or overlap.

PNG SHA256 `352ead259559a2f3677da4664cea8d771a2a1cdc1051cb37f2b107953580d34a`.

## extended-v1 physical page175

Capacity contradiction, finite-control scope and PIT heading are readable. The exact Stieltjes formula105 includes the visible negative lower-boundary term and does not overlap its explanatory paragraph.

PNG SHA256 `c3d5fdb062963114bf46da1259b0b106c77473fa96a3c4cb4e1659e4cfd5f14c`.

## extended-v1 physical page176

The widest variation budget106, positive input107, Bop109 and primary citation/fixed-field display all fit. Fraction bars, roots, subscripts and equation labels are readable with no collision.

PNG SHA256 `02677e86aa3e04b50f66f703a664f1a9bab7969c17b3fcfb3d783405ead1f4bc`.

## notes-concise-v1 physical page24

Theorem18, correction constants, complete critical bound47 and restricted indicator identity fit clearly. No missing glyph or collision is visible.

PNG SHA256 `8c17127038c207fe1ac30b03b2d23a2550e02f9e00eaf8794ff2fd1d726f78e3`.

## notes-concise-v1 physical page25

Both parameter and raw tables, the smooth-step fraction, noncritical-capacity qualifier and summary-link text are readable. The inherited closing reference is separate; the end-of-document whitespace is normal.

PNG SHA256 `ef8e7c3075d3dd7e6ef522261a7cafb8a6e1cc406a2ded15cde0cf3f4541f781`.

## notes-extended-v1 physical page67

Theorem19 and bounds74–78 are clear. Parameter table rows remain legible above the footer; no clipping or overlap is visible.

PNG SHA256 `b74dd4c1be4535f69d4d3ddcddf1c56b586f541305271b65a95a1f91190ab01d`.

## notes-extended-v1 physical page68

Profile construction and raw table fit clearly. Section41 and its first proof subsection have adequate spacing; the bottom invariance formula81 is fully visible.

PNG SHA256 `a5c30364e2126e4bea0b08f8d0e0106329b67e20241d5a9a5dcd06cee5721a9d`.

## notes-extended-v1 physical page72

Capacity proof, finite scope and PIT section41.8 are readable. The exact lower-boundary term in formula98 and its explanatory text are fully visible.

PNG SHA256 `e9bb17fec58e2f7bb7b541576b6823a1e690f52544fa5b480288cce4dc9247cd`.

## notes-extended-v1 physical page73

Variation formula99, positive operator100, Bop102 and fixed-field citation/display fit within the page with legible indices, roots, fractions and equation numbers.

PNG SHA256 `dc8324004c1df6b3349d58497b57dccecb6086353687a2cdc7b5ac182904620b`.
