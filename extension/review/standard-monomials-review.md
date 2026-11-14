# Standard monomial theory: source and proof review

## Scope and output

The new manuscript source is extension/manuscript/chapters/standard-monomials.tex. It contains three connected chapters:

1. Exterior algebra, tableaux, and Schur constructions.
2. Standard monomials on spaces of complexes.
3. Associated graded rings, semigroups, and toric limits.

The source contains approximately 8,000 whitespace-delimited source words, 17 proof environments, and three explicitly external general theorems. These counts describe the new contribution, not the complete monograph. Neither this source review nor the manuscript claims a full proof audit of the author's whole oeuvre, all external URLs in the upstream repository, or complete Lean formalization of standard monomial theory.

## Primary sources actually inspected

| Source | Reading coverage | Primary location |
|---|---|---|
| Akin, Buchsbaum, Weyman, *Schur Functors and Schur Complexes*, 1982 | Section II.2, printed pages 223–234, read in full, including shuffle presentation, tableau order, spanning, triangular independence, and universal freeness. Introduction and bibliographic page also inspected. Not a claim to have read all 72 pages. | https://jerzyweyman.webflow.io/research/schur |
| De Concini, Eisenbud, Procesi, *Hodge Algebras*, Astérisque 91, 1982 | Sections 1–3, 11–12, and 16 read. Critical mixed-minor standardness on printed page 71 and rank-quotient conclusions on printed page 73 visually checked against rendered pages. | https://smf.emath.fr/system/files/filepdf/AST_1982__91__1_0.pdf |
| Carroll, Weyman, *Semi-Invariants for Gentle String Algebras*, arXiv:1106.0774v1, 2011 | Sections 3–5 read completely by this contributor, including coordinate filtration and product argument. The parent contributor read Sections 1–2 and 6–9; collectively the paper's sections were covered. | https://arxiv.org/abs/1106.0774v1 |
| Gonciulea, Lakshmibai, *Schubert Varieties, Toric Varieties and Ladder Determinantal Varieties*, 1997 | Introduction and Sections 6 and 10 read, including the distinction between the lattice binomial algebra, Stanley–Reisner degeneration, and toric degeneration. Dense OCR formulas in the general Jacobian computation were read for argument structure, not independently formula-certified. | https://www.numdam.org/item/AIF_1997__47_4_1013_0/ |
| De Concini, Strickland, *On the Variety of Complexes*, 1981 | Foundational attribution retained through existing bibliography and the precise primary reworking in DEP Section 16 and CW Section 4. The complete original DS article was not newly retrieved and read in this stage. | https://doi.org/10.1016/S0001-8708(81)80004-7 |

The current ABW author-hosted download was obtained through the author's page. The older indexed WordPress PDF link returned HTTP 404; no source-content claim is based on that failed link. The current direct PDF URL is:

https://cdn.prod.website-files.com/69c19dc391eb37d617c813ce/69cc3be3405f5e9e171b7db4_JW%231_Schur.pdf

Downloaded papers and full extracted text remain in the research staging directory outside the project repository. They are not included as a bulk copyrighted-text distribution.

## Conventions fixed explicitly

- The complex is descending: D_i maps V_i to V_(i−1). Its point action is g_(i−1) D_i g_i^−1. The action on functions is contragredient.
- The arrow coordinate representation is V_i tensor V_(i−1)^*. At a vertex, the positive weight block comes from the outgoing arrow and the reversed negative block from the incoming arrow.
- The Schur formula has one factor for every vertex, including both endpoints. The allowed partition lengths are bounded by the corresponding ranks, and the rank admissibility inequalities ensure room for both signed blocks.
- Schur modules use row partitions, column exterior powers, column-strict and row-weak tableaux. ABW's transposed tableau convention is stated.
- The mixed-minor rule uses the complement of the row-index set of the higher arrow and compares the column-index set of the lower arrow with the terminal entries of that complement. It is DEP's stated transpose convention.
- Rank at most r is imposed by the (r+1)-minors. Exact rank r, rather than rank strictly below r, labels the orbit.
- Every admissible rank vector defines an irreducible orbit closure. Coordinatewise maximality is the condition for being a component of the whole complex variety.
- Representation splitting is stated only in characteristic zero. The integral standard bases do not imply modular semisimplicity.

## Source issues not propagated

The 2011 CW preprint has several apparent typographical slips in the relevant sections. Definition 3.2 prints a strict rank inequality for the exact-rank stratum; its proposition and proof require equality. A sentence in Proposition 3.3 refers to r-by-r minors where the rank bound requires (r+1)-minors. Proposition 5.2 phrases irreducibility as equivalent to maximality, while its proof and the normal-form argument distinguish all irreducible rank closures from maximal component closures. The displayed Schur product must be reindexed to include all vertices. Our statements are checked against the independently proved normal form and the one-arrow and (1,2,1) examples.

The parent contributor separately verified the monomial correction in CW Example 8.20: the relation involving Y1Y2 uses B1, not the printed B2. That correction belongs to the gentle-invariants chapter and its review. It is not used as an assumption in the elementary standard monomial proofs here.

## Fully proved statements in the new chapters

The following are proved directly, with no appeal to a general standard monomial theorem for their independence or spanning claims:

1. The ordered exterior basis over a commutative ring.
2. Cauchy–Binet from exterior functoriality.
3. Exterior coproduct well-definedness, naturality, coassociativity, and the binomial multiplication identity.
4. Contraction square zero and the contracting homotopy when a covector evaluates to one.
5. The one-row, one-column, and (2,1) Schur cases, including the integral short exact sequence and basis.
6. The characteristic-zero Young-idempotent tensor-complex construction and acyclicity for positive tensor degree.
7. The rank-one Segre kernel, straightening algorithm, standard basis, and degree count.
8. The two-row Plucker shuffle identity.
9. The two-row Plucker quadratic presentation and standard basis, with termination and leading-monomial independence.
10. The (1,2,1) complex's ring, basis, singular locus, dimensions, and Hilbert series.
11. Its bihomogeneous Schur representation, checked using the two-dimensional dual identity and a dimension-matched surjection.
12. General exact-rank orbit classification, rank-closure containment, component criterion, and stratum dimension.
13. A flat monomial degeneration for a quadratic degree-one straightening algebra, with an explicit positive weight construction.
14. The diagonal SAGBI basis for two-row minors.
15. The diagonal semigroup's prefix inequalities, integer matching construction, tableau bijection, and saturation.
16. Normality for the two explicit semigroups, proved via Laurent polynomial and valuation intersections.
17. Two distinct free flat families for the cone over Gr(2,4), with reducible monomial and normal integral toric special fibers.

The general integral Schur basis theorem, the general complex standard basis/normality theorem, and the general coordinate Schur filtration are external theorems. Their hypotheses and roles are stated. The integral two-row and rank-one examples, the elementary degeneration families, and their normality are proved independently.

## Key distinctions preserved

A Schur filtration is a filtration by representation modules. Splitting it as a representation does not identify the original multiplication with the top graded product. A Stanley–Reisner limit sets incomparable or nonstandard products to zero and can have zero divisors. A diagonal initial subalgebra is an affine semigroup ring and remains a domain. The manuscript supplies explicit examples starting from the same Grassmannian to demonstrate this difference.

The Gelfand–Tsetlin description is proved for the stated two-row semigroup, including its endpoint conditions. No claim is made that every general complex coordinate ring has the same two-row toric degeneration. The invariant-theory interface states the scalar-character test and leaves the additional tensor-product and semi-invariant arguments to the gentle-algebra chapter.

The chapter does not infer an ECC algorithm, cryptographic security reduction, analytic index theorem, or Yang–Mills mass gap from a standard basis or a flat degeneration. These require the independent hypotheses and proofs stated elsewhere in the monograph.

## Verification boundary

All TeX is ASCII, uses the existing theorem environments and packages, and introduces no new global macro. Environment opening/closing counts were checked; there are 17 proofs and 20 theorem/proposition/lemma statements, the difference being the three explicitly external results. The original Lean modules are not changed by this chapter. The general SMT statements are not claimed to be Lean-verified.

An independent contributor checked the central formulas and the termination/weight arguments before the final document build. Typesetting and page-level visual QA are recorded by the final build contributor rather than claimed here before compilation.
