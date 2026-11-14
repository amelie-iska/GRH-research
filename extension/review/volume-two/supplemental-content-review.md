# Volume II: supplemental all-page content review

Date: 13 November 2026. Reviewers: the arithmetic/order-theory workstream and the Volume II/complexes workstream.

This record supplements the primary Volume II review. It records actual reading of the OCR text of the scanned pages, including exercises and bibliographical material. It does **not** certify all source proofs, reconstruct every damaged formula, or claim complete formalization. Long diagrams and arithmetic subscripts are often corrupted by OCR. The supplied scan and full OCR text remain private research intermediates.

## Completed ranges in this supplement

| PDF pages | Section | Content reviewed and implications |
|---|---|---|
| 2 | Copyright/imprint | Publisher and date metadata; reinforces that the scan and OCR should not be republished with original research artifacts. |
| 31–33 | VI, end of §4 | Jordan–Zassenhaus finiteness for global fields and the finite-residue local case. A finite quotient is used to control integral models with fixed rational span. Finiteness is distinct from an effective complexity bound. |
| 34–42 | VI §5 | Irreducible lattices, maximal overorders, commuting endomorphism orders, Morita parametrizations by ideal classes, and local finiteness in the split case. VI.5.7–VI.5.10 connect the maximality of endomorphism orders to extension of lattice actions. VI.5.13 needs the split-algebra hypothesis; the exercises explicitly warn that removing it changes the conclusion. |
| 43–48 | VI §6 | Archimedean completions, real quaternion algebras, ramification, global splitting and norm theorems, and the definite-quaternion exception. VI.6.8–VI.6.10 are explicitly quoted external theorems in the original. The exceptional case is relevant to supersingular elliptic curves, whose geometric endomorphism algebras are definite rational quaternion algebras. |
| 49–64 | VI §7 | Eichler’s condition, the precise epimorphism/kernel comparison theorem VI.7.2, approximation, polynomial construction, reductions to maximal orders and central simple algebras, and the final automorphism argument. The geometry-of-numbers exercises explain one use of arithmetic lattice norms. The proof is not a complexity analysis or a cryptographic reduction. |
| 65–74 | VI §8 | Normal one-sided ideals, left/right orders, proper products, inversion, factorization into maximal normal ideals, and reduced ideal norms. Norm multiplicativity is attached to composable ideal products. VI.8.12 and VI.8.14 use the exclusion of the totally definite quaternion case to classify ideals by norm data. Their unrestricted use in a supersingular quaternion setting would be invalid. |
| 296–308 | X §1 | Constructions of indecomposable lattices through endomorphism rings without nontrivial idempotents; Dade's obstruction with at least four simple components (X.1.7); the three independence patterns of X.1.8; generator-number obstructions and the long case analysis beginning at X.1.12. Finite representation type concerns indecomposables of all ranks, a different assertion from Jordan–Zassenhaus finiteness for a fixed rational representation. The eighteen-case proof and corrupted inequalities are content reviewed, not independently certified. |
| 312–319 | X §2 | Reduction to extensions with a characteristic Bass-order submodule, quotient module, and vanishing Hom group. The proposed classification program computes overorders, indecomposables, Ext groups and automorphism actions before reducing extension matrices. X.2.8 and X.2.12 distinguish Gorenstein and non-Gorenstein cases. Bounds on primitive orthogonal components must not be paraphrased as bounds on all idempotents of a ring. |
| 320–325 | X §3 | One division-component case: three-dimensional residue algebras, field and nilpotent alternatives, explicit Ext groups as bimodules, and maps induced by homomorphisms of overorders. Left and right scalar actions and their possible twists are part of the data. |
| 326–336 | X §4 | Two division-component case, decomposable and indecomposable multiplier orders, chains of overorders, Ext generators and Hom-induced actions. The printed label X.4.9 occurs both for a theorem at PDF 331 and a lemma at PDF 332; a citation should include the printed/PDF page to distinguish them. |
| 337–341 | X §5 | Three division-component case, Bass and maximal factors, intersections of ideals, Ext bases, and transfer maps. The distinction between zero and nonzero induced actions is necessary for the subsequent matrix problem. |
| 342–350 | X §6 | Heller–Reiner's extension-matrix criterion X.6.1: characteristic submodule, vanishing Hom from quotient to submodule, decomposition of the two ends, and the action of their automorphism groups. The source then lists the separate one-, two-, and three-component matrix problems. These are concrete orbit problems on Ext classes; they are not automatically the Buchsbaum–Eisenbud varieties of complexes. |
| 351–361 | X §7 | Restricted elementary row and column operations; the rank/surjectivity constraint X.7.1 via Nakayama; reductions and bounded sizes of indecomposable matrices for a cubic finite-field extension; the final use of finiteness of the residue field to obtain finitely many equivalence classes. The intermediate pure-cubic claim at PDF 356 is overstrong; the correction below isolates the weaker relation actually needed. |
| 362–368 | X §8 | Parallel reductions over a truncated nilpotent algebra. Commutation of the residue-field action with the nilpotent generator is explicitly used; this is not unrestricted Gaussian elimination over an arbitrary noncommutative order. The displayed catalogue X.8.1 is OCR damaged and has not been independently reconstructed entry by entry. |
| 369–379 | X §9 | Coupled matrix blocks over two truncated algebras, constraints from the underlying exact sequence (X.9.1), and Hom-induced transformations between blocks (X.9.2–X.9.4). The conclusion is a bound on indecomposable block degrees under these specified operations. Long displayed matrix calculations are content-triaged; OCR alone is insufficient to certify every transformation. |
| 380–383 | X §§10–11 | Final two-component decompositions. Minimization of certain nonzero entries and the permitted transfer maps isolate a finite list of block factors. The source's short proofs depend on the complete earlier matrix-action descriptions. |
| 384–386 | X §12, opening | Three-component reductions and the remaining possible indecomposable blocks. The end of §12 and the bibliography/errata at PDF 387–392 were covered in the primary review. |

The rows above were read by the arithmetic/order-theory reviewer: **133 distinct additional PDF pages**. The following rows were read in full as OCR text by the Volume II/complexes reviewer and reported to this shared ledger: **101 further distinct PDF pages**.

| PDF pages | Content reviewed and implications |
|---|---|
| 182–198 | Clean orders, local genus and Cartan equivalences, Hattori rank/trace criteria, and projective group-ring results of Swan. The hypotheses defining the appropriate “nice” orders must remain attached to the statements. Local equivalence of invariants does not by itself give a global isomorphism of arbitrary lattices. |
| 203–256 | Hereditary local order types and counts of maximal overorders; Frobenius induction–restriction; Artin cyclic induction with its integer multiplier; Brauer induction and the Berman–Witt distinction; character duality for finite torsion modules through Hom over the base ring into its quotient field modulo that ring. Artin's cyclic theorem must not be changed into an assertion of integral generation by cyclic induction. |
| 260–264 | Finite-sum constructions of covers and hypercharacteristic modules, with the specified maps and module classes. These are homological algebra statements and do not assert efficient cryptographic reconstruction. |
| 267–291 | Bass orders, Morita invariance, local division/matrix/product alternatives, and the two-generator characterization. The finite-residue-field assumption is introduced explicitly at PDF 282 for the later classification. Final computational matrices at PDF 289–291 are badly corrupted by OCR and were content-triaged, not formula- or proof-certified. |

## Assumption and transcription notes

- The first volume's errata in Volume II PDF 392 have already been visually checked by this workstream and recorded in the Volume I review. The cancellation exception for definite quaternion components is substantive.
- Page 38's OCR presents a descending-chain stabilization argument using the word “noetherian.” Noetherianity alone controls ascending chains. In the displayed setting the relevant intermediate lattices are bounded between two full lattices over a complete discrete valuation ring, so the quotient has finite length; this is the appropriate reason for stabilization. The new paper's elementary overorder certificate uses an explicit finite trace-dual quotient instead of relying on that shorthand.
- The discussion of places in VI §6 should be read with the full global-field set of places and the base-domain convention made explicit. An arbitrary localization of a ring of integers does not retain every finite place as a prime ideal of that localization. The new manuscript does not identify those sets without qualification.
- “Totally definite quaternion algebra” is used in the standard number-field sense requiring a totally real center and ramification at every real place. The characteristic-positive remark is not an invitation to interpret “every infinite place” as a vacuous defining condition.

### A visually confirmed overstatement in X §7

At **PDF 356, printed page 351, chapter-page X 65**, the scan claims that when the characteristic of a finite field is not 3, a cubic extension can be presented by a primitive element whose cube lies in the base field. This assertion is false without further hypotheses. For example, over the field with two elements every polynomial of the form X³ − a has a root in the base field: 0 for a = 0 and 1 for a = 1. Consequently no such polynomial can be the degree-three minimal polynomial of an element generating the field with eight elements.

The weaker relation used in the subsequent matrix reductions is valid: one can choose a primitive element α satisfying

\[
\alpha^3=a\alpha+b,\qquad a,b\in k,\quad b\ne0.
\]

Here is a direct repair when the characteristic is not 3. Start with any β in the cubic finite-field extension S but outside k. Since [S:k] = 3 is prime, β generates S. Put

\[
\alpha=\beta-\operatorname{Tr}_{S/k}(\beta)/3.
\]

The subtracted element belongs to k, so α still lies outside k and generates S. Its trace is zero. Its degree-three monic minimal polynomial therefore has zero coefficient of X², giving the displayed relation. Its constant term is nonzero because α is nonzero. The useful inverse formula then follows directly:

\[
\alpha^{-1}=b^{-1}\alpha^2-a b^{-1}.
\]

Thus the later claim that the inverse is a quadratic expression in α is justified without the overstrong pure-cubic presentation. In characteristic 3 the source uses an Artin–Schreier presentation, a separate case. This observation repairs the isolated assertion identified above; it does **not** certify the complete surrounding matrix classification proof. The new manuscript does not rely on a pure-cubic presentation of an arbitrary finite-field extension.

The page was rendered from the supplied scan and inspected visually to separate this issue from an OCR transcription error. The rendered scan is a private intermediate and is not included in the public project.

## Mathematical connections retained after review

The book supplies precise constructions through endomorphism orders, ideal classes, localization, projective modules, and extension classes. These support the arithmetic and homological connections made in the new manuscript. They do not identify all uses of the word “lattice,” provide a reduction of module equivalence to shortest-vector problems, or establish a quantum speedup for nonabelian ideal-class problems.

The final matrix chapters are particularly useful for teaching the distinction between a presentation and an invariant. The same Ext class can have many matrices; the permitted changes of basis are determined by endomorphism and Hom rings, rather than arbitrary independent row and column operations. This is a concrete bridge to moduli and complexes, provided the objects, morphisms, equivalence relation and base ring are specified separately.

In the finite-type proofs, a bound on the dimensions of indecomposable blocks combines with a finite residue field to give finitely many possible representatives. This logical use of finiteness does not prove that constructing representatives is efficient. Similarly, a finite collection of local possibilities is not automatically a classification of all global lattices without the gluing and ideal-class information in the preceding chapters.

## Review ledger status

The completed reading ranges partition all 392 PDF pages as follows:

| Reading pass | Exact PDF pages | Distinct pages |
|---|---|---:|
| Primary Volume II content review | 1, 3–30, 75–181, 199–202, 257–259, 265–266, 292–295, 309–311, 387–392 | 158 |
| Supplemental arithmetic/order-theory reviewer | 2, 31–74, 296–308, 312–386 | 133 |
| Supplemental Volume II/complexes reviewer | 182–198, 203–256, 260–264, 267–291 | 101 |
| Union, with no omissions or overlap | 1–392 | **392** |

The page-set union and pairwise disjointness were checked programmatically. The accompanying `content-reading-coverage.json` records the exact reading pass for each PDF page. The primary reviewer's separate OCR coverage record is not altered by this supplement.

**Accurate completion statement:** every page's available OCR text in both supplied volumes has been read and its subject matter reviewed across the team; key statements and selected problematic pages were checked against the scans. The dense displayed matrices and damaged formulas marked above were not all reconstructed, and neither historical book has been fully proof-audited or formalized in Lean.
