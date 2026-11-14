# Volume I: review record and mathematical integration

Review date: 13 November 2026.

## Identity and scope

The supplied file is **Klaus W. Roggenkamp and Verena Huber-Dyson, _Lattices over Orders I_, Lecture Notes in Mathematics 115, Springer, 1970**. Both authors are printed on the title page, which was inspected as an image. The scan contains 309 PDF pages: nineteen pages of preliminary material followed by 290 numbered pages. For the numbered body, PDF page = printed page + 19. The publisher's permanent bibliographic record is <https://doi.org/10.1007/BFb0068796>.

All 309 PDF pages were OCR processed, and all of the resulting text was read for content, argument structure, definitions, theorem identifiers, and relevance. The per-page extraction and review record is `coverage.json`; aggregate counts and the attachment's SHA-256 are in `summary.json`. The extraction script is `ocr_all.py`.

**This is an all-page OCR-assisted content review, not a certification of every proof in the book.** The scan's mathematical notation is imperfectly recognized: subscripts, superscripts, hats, opposite-ring markers, noncontainment signs, and long commutative diagrams are frequently damaged. Text review cannot establish the validity of a formula whose symbols have been lost. Selected key pages were inspected as images; the exact visual checks are listed below. The manuscript consequently supplies independent elementary proofs in current notation, and cites advanced source results as external theorems. It does not assert that all source proofs have been formalized, checked line by line, or independently reconstructed.

The user's request for the authors' entire research corpus is larger than this review. The bibliography itself identifies sixteen Roggenkamp items, several described in 1970 as unpublished, forthcoming, or lecture notes. This review verifies two directly relevant published 1969 papers, in addition to the supplied book and modern primary mathematical expositions. It does not label all of either author's output as reviewed.

## All-page coverage by section

| PDF pages | Printed range | Content and review finding |
|---|---|---|
| 1–6 | preliminary | Title, copyright, preface, contents. Attribution to both authors checked visually on PDF 1. The text is an exposition of integral representation and order theory; it is not a cryptographic or quantum-field-theory monograph. |
| 7–19 | vii–xix | Introduction and historical guide. Distinguishes rational representations from lattices, localization and completion, ideal classes, direct decompositions, and finiteness/cancellation questions. Historical statements about the frontier are dated 1970 and must not be repeated as current research status. |
| 20–83 | 1–64 | Chapter I, rings and modules. Projectivity, tensor products, finiteness, radicals, integrality, localization, Dedekind domains, lattice patching, and completions provide the elementary base used by the new chapters. |
| 84–142 | 65–123 | Chapter II, homological algebra. Categories, complexes, homology, resolutions, Ext and Tor, homological dimension, and the extension interpretation of Ext. Important for keeping the algebraic meaning of a complex separate from analytic ellipticity. |
| 143–196 | 124–177 | Chapter III, Morita equivalence and separability. Evaluation maps, generators, matrix-style equivalences, trace and discriminant, derivations, separable algebras, splitting fields, reduced trace/norm, and projective covers. Opposite-ring conventions require care when converting the book's right-written maps into standard composition notation. |
| 197–261 | 178–242 | Chapter IV, maximal orders. Lattices and multiplier orders, completions, Morita properties, maximality, ideals, complete division-algebra structure, and Hasse's local classification. The directly reused elementary arguments were independently reproved. The large local-division-algebra proofs remain external. |
| 262–290 | 243–271 | Chapter V, Higman ideals and extensions. Trace duals, different and inverse different, projective homomorphisms, extension annihilators, conductors, and finite group-ring averaging. The new chapter proves the averaging lift explicitly and states its precise splitting hypothesis. |
| 291–307 | 272–288 | Bibliography. Identified author-related sources and original sources for structural results. Entries marked forthcoming in the original are not treated as complete modern bibliographic evidence. |
| 308–309 | 289–290 | Index. Cross-checked chapter-section vocabulary and identified useful entry points; the index is not evidence of a proof. |

## Exact source anchors

Book references below use chapter.section.result; the printed body page can be recovered by subtracting 19 from its PDF page. These are locations, not claims that their full proofs received independent formal verification.

| Source anchor | PDF location | Role in the new paper |
|---|---:|---|
| I.2.9; I.2.12 | Chapter I | Projectivity and duality background. The paper's finite projective double-dual step is explained directly. |
| I.7.2; I.7.3 | Chapter I | Finitely generated torsion-free modules over Dedekind domains are projective and decompose into fractional ideals; retained as established structural background. |
| I.8.6–I.8.8 | Chapter I | Intersection of local lattices and patching. The paper proves its own local membership test and embedded-equality criterion. |
| II.3.6–II.3.10 | Chapter II | Lifting chain maps, independence of resolutions, and exact homology/Ext constructions. No assertion about analytic spectra follows from these algebraic facts alone. |
| II.5.9 | Chapter II | Extension classes and Ext. Used to explain the meaning of an annihilating integer after a direct pullback splitting proof. |
| III.1.5; III.1.10; III.2.1 | Chapter III | Dual-basis criterion, generators, and Morita equivalence. The matrix case is fully proved in the manuscript. General Morita results are source theorems. |
| III.3.2; III.3.7 | Chapter III | Discriminant change of basis and dual bases. The paper supplies its own determinant and trace-dual arguments. |
| III.6.11–III.6.19 | 182–187 | Reduced characteristic polynomial, reduced norm and trace, and separability. The paper explicitly distinguishes ordinary trace from reduced trace. |
| IV.1.1; IV.1.3 | 197–198 | Definitions of orders and lattices; left/right multiplier orders. PDF 197 checked visually. |
| IV.1.4 | 198–200 | Integrality and traces for orders, used as background in the finite overorder certificate. |
| IV.1.12 | 203 | Existence of a stable lattice in a finite-dimensional module. The paper proves this by a finite set of generators. |
| IV.1.14; IV.1.15 | 204 | Linearity over an overorder and integral endomorphism orders. Both statements and the denominator cancellation mechanism checked visually. |
| IV.3.1 | 209–210 | Detection of generator conditions after passage to completions. **Use the correction in Volume II**, not the erroneous torsion decomposition argument. |
| IV.4.6 | 220 | Existence of maximal overorders. The new finite-certificate proposition proves a restricted case with an explicit integral nondegenerate trace. |
| IV.4.8 | 221 | Maximality detected locally and after completion. Statement and proof structure checked visually. |
| IV.4.19 | 225 | Hereditary property of maximal orders. Retained as an external structural theorem. |
| IV.5.5 | 232–233 | Maximality and faithful progenerators; Morita invariance in the appropriate setting. Statement and its precise footnote checked visually on PDF 232. |
| IV.5.7–IV.5.8 | 234 | Local lattice classification for maximal orders and conjugacy. These do not erase global ideal-class data. |
| IV.6.13–IV.6.17 | 251–259 | Hasse's structure and splitting results over the complete local field in the section's hypotheses. OCR notation is too damaged to claim independent verification of these calculations. |
| V.1.1–V.1.3 | 262–263 | Different, inverse different, and localization. PDF 262 checked visually. |
| V.3.5–V.3.10 | 274–277 | Nonzero Higman ideal, localization of extension obstructions, and the finite group-ring formula. V.3.10 inspected visually on PDF 276. |
| V.4.3; V.4.7; V.4.12 | 279, 281, 282–284 | Conductors and projective homomorphisms. Useful source structure, with hypotheses retained. |
| V.5.3–V.5.5 | 287–290 | Special classes of lattices and annihilator formulas. The dependence of V.5.3 on Volume II is explicit in the original and is not hidden in the new exposition. |

## Corrections from Volume II

Volume II PDF page 392 contains the original author's corrections to Volume I. The page was read as OCR and inspected as an image. Two corrections materially affect synthesis across the books.

1. The statement on preliminary page xviii needs a restriction excluding simple components that are full matrix rings over totally definite quaternion algebras. This is exactly the kind of exceptional case that matters when connecting orders to supersingular elliptic curves. An unrestricted cancellation claim must not be carried into the quaternion discussion.
2. The proof at chapter-page IV.13 uses a torsion/torsion-free decomposition that need not be a decomposition of modules over the order. The correction explicitly replaces the faulty step with a faithful-flatness and evaluation-map argument after completion. The manuscript does not reproduce the faulty proof. Its explicit matrix Morita equivalence is proved independently.

The corrections also amend notation and remove an excessive faithfulness assertion at chapter-page III.13. These corrections are a further reason to distinguish content review from validation of every historical proof.

## Selected author research checked

### K. W. Roggenkamp, “On the Irreducible Lattices of Orders” (1969)

Canadian Journal of Mathematics 21, 970–976. DOI: <https://doi.org/10.4153/CJM-1969-106-x>. Primary publisher PDF: <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/25660C441608D384D2564A931E2D692D/S0008414X00042346a.pdf/on_the_irreducible_lattices_of_orders.pdf>.

The paper is directly relevant to the interaction of irreducible lattices, maximal overorders, commuting endomorphisms, and genera. Its Proposition 1 gives the overorder-linearity mechanism used in the new arithmetic chapter. The manuscript provides an independent denominator-cancellation proof, and does not elevate genus-level information to a global classification theorem without hypotheses.

### K. W. Roggenkamp, “A Remark on Separable Orders” (1969)

Canadian Mathematical Bulletin 12(4), 453–455. DOI: <https://doi.org/10.4153/CMB-1969-055-4>. Primary publisher PDF: <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/54C0AFAE48BBD8E21854E750B6EF49BE/S000843950005387Xa.pdf/a-remark-on-separable-orders.pdf>.

The distinction between maximality and separability over the integral base is central. The paper's arithmetic characterization involves unramified conditions; it does not say that every maximal order is separable over its base ring. The new chapter uses this as a precise limitation on transferring generic-fiber properties to integral orders.

## Modern bridge sources

John Voight's open chapter “Supersingular elliptic curves,” in _Quaternion Algebras_ (2021), is the main source for the maximal quaternion-order classification and the Deuring correspondence: <https://doi.org/10.1007/978-3-030-56694-4_42>. Theorem 42.1.9 and section 42.3 are the relevant anchors. Right-module Hom conventions in the new text are stated explicitly rather than silently importing a left-ideal convention.

Andrew Sutherland's original MIT 18.783 lecture notes (2023), lectures 7, 12, 13, 17 and 18, supply elliptic-curve trace/norm, ordinary-versus-supersingular, complex multiplication, ideal actions, and isogeny context. Their URLs and exact titles appear in `sources.bib`. The chosen passages were reviewed for the claims used; this record does not claim a complete review of every lecture.

John Tate's 1966 original paper “Endomorphisms of Abelian Varieties over Finite Fields” supplies the deep Tate-module theorem. The new manuscript proves elementary faithfulness on prime-to-characteristic torsion and explicitly distinguishes it from Tate's surjectivity/image theorem. Primary author-paper copy: <https://pazuki.perso.math.cnrs.fr/index_fichiers/Tate66.pdf>.

## Original mathematical deliverable

`manuscript/chapters/orders.tex` contains two original chapters, “Orders as integral arithmetic structures” and “Elliptic curves through their endomorphism lattices.” They include independent proofs of common-denominator commensurability, existence of stable integral models, endomorphism and multiplier orders, local membership and equality, overorder linearity, matrix Morita equivalence, trace duality, discriminant scaling, metric distortion of minima, quaternion norm multiplicativity, a finite overorder bound, an integral averaging lift, holomorphic homomorphisms of complex tori, the elementary CM dichotomy, quadratic conductor classification, the ideal-class torsor, a Frobenius-order discriminant consequence, torsion-action faithfulness, right-ideal endomorphisms, conditional degree multiplicativity, a matrix centralizer, and a Gaussian-order trace-dual calculation.

These are original explanatory proofs of established mathematics, not claims of new research theorems. The Frobenius, dual-isogeny, and geometric classification inputs are identified as external or conditional. The new exposition distinguishes arithmetic module lattices, Euclidean lattices with positive forms, and spacetime lattices in gauge theory. It identifies precisely why an algebraic equivalence need not preserve metric distortion, cryptographic distributions, reversible circuit costs, or a field-theoretic mass gap.

## Publication handling

The public project may include this review, the original manuscript, bibliographic metadata, and the coverage counts. The supplied scan, extracted full text, and page-image crops are research intermediates and should not be republished with the original codebase. `coverage.json` contains page-level metadata, not the book's text. The source scan's checksum permits identification without redistributing the source.
