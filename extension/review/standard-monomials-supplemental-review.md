# Supplementary primary-source review: ABW and DEP

## Coverage reached after the manuscript build

The team has now read **all extracted text from all 72 PDF pages** of Akin–Buchsbaum–Weyman (ABW), *Schur Functors and Schur Complexes*, and **all extracted text from all 88 PDF pages** of De Concini–Eisenbud–Procesi (DEP), *Hodge Algebras*. These totals include title material, references, and the DEP résumé; the blank DEP front-matter page was identified as blank. The text comprises 27,680 and 23,698 whitespace-delimited words, respectively.

This is **complete text-content reading with selected visual formula checks**, not complete independent proof certification. The readers followed the arguments and checked their hypotheses against the manuscript. Every displayed formula, tableau drawing, diagram, and cited external argument has not been independently reconstructed. In particular, a proof that refers to an earlier proposition or another paper was read as such; the reference was not silently counted as a fresh proof audit. OCR and text-extraction damage remains a limitation outside the selected page-image checks.

The earlier [SMT review](standard-monomials-review.md) accurately records the narrower coverage at the time the manuscript was drafted. This supplement extends that boundary. The frozen first-release 187-page PDF retains its conservative description of the earlier review stage. No mathematical manuscript change was required by this additional reading, and no new general SMT theorem has thereby become Lean-formalized.

The companion [machine-readable ledger](standard-monomials-supplemental-review.json) records exact files, hashes, section intervals, reviewer assignments, and page-image checks. Intervals below use **newline-numbered extracted-text lines**, as in `sed -n`; form-feed page separators do not introduce extra numbered lines. Consequently these counts differ from Python's broader Unicode `splitlines()` count.

## Primary editions and reading partitions

### Akin–Buchsbaum–Weyman

ABW, *Advances in Mathematics* **44** (1982), 207–278, [DOI 10.1016/0001-8708(82)90039-1](https://doi.org/10.1016/0001-8708(82)90039-1). The PDF was obtained from the [author's research page](https://jerzyweyman.webflow.io/research/schur), using its linked author-hosted copy. It contains 72 physical PDF pages, corresponding to printed pages 207–278.

| Portion | Printed pages, including shared boundary pages | Extracted-text lines | Reader and phase |
|---|---:|---:|---|
| Introduction | 207–210 | 1–180 | Volume II contributor, supplemental reading |
| I: Hopf, exterior, symmetric, divided-power, and bigraded constructions | 210–217 | 181–491 | Yang–Mills contributor, supplemental reading |
| II.1: Schur and skew-Schur definitions | 217–223 | 492–744 | Yang–Mills contributor, supplemental reading |
| II.2: universal freeness of Schur functors | 223–234 | 745–1233 | Volume II contributor, previously completed |
| II.3: universal freeness of coSchur functors | 234–236 | 1234–1349 | Yang–Mills contributor, supplemental reading |
| II.4: duality and restriction filtrations | 236–242 | 1350–1605 | Yang–Mills contributor, supplemental reading |
| III.1: symmetric Cauchy filtration | 242–246 | 1606–1819 | Volume II contributor, supplemental reading |
| III.2: exterior Cauchy filtration | 246–249 | 1820–1927 | Volume II contributor, supplemental reading |
| IV.1–2: Schensted process and Littlewood–Richardson rule | 249–260 | 1928–2435 | Volume II contributor, supplemental reading |
| V.1: Schur complexes and acyclicity | 260–267 | 2436–2737 | Volume II contributor, supplemental reading |
| V.2: general modules and generic resolutions | 267–275 | 2738–3116 | Volume II contributor, supplemental reading |
| Appendix and references | 276–278 | 3117–3219 | Volume II contributor, supplemental reading |

These intervals partition all 3,219 newline-delimited text lines. Selected additional visual checks covered physical PDF pages 7, 9, 10, 11, 30, and 61: printed pages 213, 215, 216, 217, 236, and 267.

### De Concini–Eisenbud–Procesi

DEP, *Astérisque* **91** (1982), [publisher-hosted PDF](https://smf.emath.fr/system/files/filepdf/AST_1982__91__1_0.pdf); [Numdam bibliographic record](https://www.numdam.org/item/AST_1982__91__1_0/). The PDF contains 88 physical pages, including the digitization cover, contents, blank front matter, and printed résumé on page 87.

| Portion | Printed pages | Extracted-text lines | Reader and phase |
|---|---:|---:|---|
| Cover, contents, introduction, preliminaries | front matter and 3–12 | 1–607 | Volume II contributor, supplemental reading |
| §§1–3: definitions, standard filtrations, simplification | 13–23 | 608–1241 | Volume II contributor, previously completed |
| §§4–10: discrete rings, dimension, depth, posets, Hilbert functions, constructions | 24–48 | 1242–2393 | Volume I contributor, supplemental reading |
| §§11–12: Grassmannians, determinantal and Pfaffian varieties | 49–53 | 2394–2646 | Volume II contributor, previously completed |
| §13: varieties of minimal degree | 54–59 | 2647–2949 | Volume II contributor, supplemental reading |
| §§14–15: low-dimensional square-free Hodge algebras | 60–68 | 2950–3432 | Volume II contributor, supplemental reading |
| §16: varieties of complexes | 69–73 | 3433–3668 | Volume II contributor, previously completed |
| §§17–18: flag varieties, dosets, and symmetric matrices | 74–83 | 3669–4126 | Volume II contributor, supplemental reading |
| References and résumé | 84–87 | 4127–4320 | Volume II contributor, supplemental reading |

These intervals partition all 4,320 newline-delimited text lines. Sections may share a PDF page with adjacent material. Additional visual checks covered physical PDF pages 31, 39, 45, 47, and 48: printed pages 30, 38, 44, 46, and 47. The earlier direct image checks of printed pages 71 and 73 remain part of the review record.

## Assumptions verified against the algebraic chapters

### Integral constructions and characteristic zero

ABW develops the relevant integral constructions for finite free modules. Its Hopf-duality arguments impose the stated connected grading and finite-free graded-piece conditions. The divided-power algebra is essential over general coefficient rings; replacing it by the symmetric algebra, or dividing by factorials without an invertibility assumption, would change the construction. Its bigraded interchange sign, checked visually on printed page 216, uses the first-first, first-second, and second-first degree pairings; the second-second pairing is absent. This is a source convention, not the usual total-degree sign inserted by guesswork.

ABW's partition convention is transposed relative to the row-partition convention of the new manuscript. A skew diagram is the difference of the two Young diagrams, not a left-justified diagram obtained by subtracting their row lengths. The duality in II.4.1 transposes both shapes and exchanges Schur with coSchur constructions. The integral coSchur straightening proof retains its repeated-entry rule to obtain a coefficient of absolute value one; this is why the argument does not require division in the base ring.

ABW II.4 and III construct **filtrations** over a general commutative ring. Their associated graded pieces are tensor products of appropriate Schur or coSchur modules. The exterior Cauchy formula requires the coSchur factor in this generality. A representation-theoretic direct-sum decomposition in characteristic zero must not be exported to a modular setting, nor does a module filtration identify multiplication with that of the associated graded algebra. The explicit Littlewood–Richardson direct-sum theorem IV.2.1 assumes a ground ring containing a characteristic-zero field. Its proof uses semisimplicity after reducing to that field. These distinctions agree with the frozen manuscript.

### Schur complexes and the meaning of acyclicity

ABW V defines the symmetric and exterior complexes of a map of finite free modules, including divided powers in the exterior-complex terms. The standard basis supplies universal freeness and base change. The direct-sum construction again supplies a filtration, not an integral canonical splitting.

For a split injection, V.1.15 has vanishing positive homology and identifies degree-zero homology with a Schur functor of the cokernel. The word *acyclic* in this resolution context must not be read as asserting that degree-zero homology vanishes. V.1.16 treats the removal of an isomorphism summand by homotopy equivalence. V.2.2 identifies degree-zero homology for a finite free presentation, and the remaining section constructs generic-map resolutions by a mapping cone and a grade argument. Reading that construction does not prove a general statement that arbitrary nonlinear termwise functors preserve exact sequences.

The image of printed page 267 resolves important OCR ambiguity in V.1.17. In its notation, the ranks satisfy `m ≥ n`, the partition bound is `λ₁ ≤ m−n+1`, and the hypothesis is

\[
\operatorname{grade} I_j(\phi)\geq (m-n+1)(n-j+1),\qquad 1\leq j\leq n.
\]

The statement uses non-strict inequalities. This is a sufficient determinantal-grade criterion in the source's acyclicity framework, not an unconditional assertion for every matrix. The frozen manuscript's elementary positive-degree characteristic-zero tensor-complex argument has its own stated assumptions and does not silently invoke this broader criterion.

### Degenerations, normality, and Cohen–Macaulayness

DEP distinguishes general Hodge algebras, ordinal Hodge algebras, square-free cases, and discrete cases. Varieties of complexes and some flag Schubert rings motivate the broader, nonordinal definition. A proof formulated for an ordinal poset cannot automatically be applied to every Hodge algebra.

The standard-filtration and simplification arguments deform to a monomial quotient. Such a quotient can have zero divisors. DEP's introduction expressly separates this situation from a normal domain and discusses additional conditions needed for stronger singularity conclusions. This supports the manuscript's separation of the Stanley–Reisner-type monomial degeneration from the independently proved, saturated-semigroup toric examples.

DEP §4 works with a domain as base in its discrete-ring discussion and uses polarization through a regular sequence. The dimension statements in §6 impose a universally catenary Noetherian base. Section 7 compares filtered Koszul homology by a subquotient construction; it does not identify the two homology modules. Its transfer gives a depth inequality, with the discrete algebra providing the lower bound, and a corresponding sufficient Gorenstein implication. Section 8's wonderful-poset result is an ordinal result with its combinatorial hypotheses.

The weighted constructions of §10 also carry real restrictions. Proposition 10.1 allows nonnegative generator degrees, requires the specified compatibility with the order, and restricts the number of factors in straightening terms. Its Rees/blowup application additionally uses its condition on multiplication by a poset ideal. None of these statements says that every filtration of every Hodge algebra has a Hodge associated graded ring.

The low-dimensional classification in §§14–15 retains the universally catenary base assumption; its more detailed two-dimensional results then work over a field and with the displayed special poset. Section 17 states its flag-variety construction over the integers or a field and cites the general standard-monomial theorem. Section 18 changes the combinatorial structure to a **doset** and has its own straightening axioms. Its Cohen–Macaulay conclusions use the corresponding subdivision and combinatorial results. These sections were read for their actual scope, not treated as new proofs of unrestricted normality or Cohen–Macaulayness.

## Local source cautions identified

The following affect how one should reuse the sources. None is repeated as a premise of the frozen manuscript.

1. **Anti-invariant tensors over rings with 2-torsion.** On printed page 213, ABW gives a characteristic-not-two qualification for identifying the exterior image with all anti-invariant tensors. For arbitrary commutative rings, that qualification alone is insufficient. Let `R = Z/6Z` and let `F = R e`. Then `3(e⊗e)` is nonzero and equals its negative, so the transposition acts on it by the sign character, but `Λ²F = 0`. Requiring multiplication by 2 to be injective on the coefficient ring resolves the repeated-index obstruction; invertibility of 2 is a stronger sufficient condition. The manuscript instead defines the exterior quotient by the alternating relations and proves its basis directly over every commutative ring.
2. **Divided-power scalar typing.** The printed axiom on ABW page 215 writes a product of two module elements where the scalar law is required. Its well-typed interpretation is `γ_p(a g) = a^p γ_p(g)` for `a∈R`, `g∈F`. No multiplication on the arbitrary input module should be inferred.
3. **Complement shapes in ABW II.4.2.** The displayed complementary partitions on printed page 236 need the relevant width bound, or explicit extended-shape/vanishing conventions, before being used as ordinary partitions. For example, an outer one-row shape of length `n+1` and empty inner shape can produce a negative proposed part. The manuscript does not use this unrestricted formula.
4. **DEP depth/cohomology indexing.** The superscript in printed Theorem 4.6 was checked against the page image. Its conversion to conventional reduced-cohomology/depth indexing needs a convention reconciliation before that formula is reused. This ledger records a caution, not a declared erratum or a repaired theorem. The manuscript does not rely on that displayed indexing.
5. **DEP Hilbert-series field scope.** Printed Proposition 9.2 does not visibly repeat an explicit field assumption beside its Gorenstein reciprocity formulation, although the surrounding discussion uses a rank-based Hilbert function. Its equivalence should not be exported to arbitrary base rings without further hypotheses. Proposition 9.3 explicitly assumes a field. The manuscript does not use the unsupported extension.

## Release and review boundary

The only release changes from this review are this note, its JSON ledger, and the two ABW/DEP rows in the central source-review README. The manuscript, compiled PDF, Lean sources, formal-verification manifests, and theorem inventory are unchanged. Downloaded third-party PDFs, extracted full texts, and rendered source images remain outside the release repository; only original review notes and source hashes are supplied.

This completes the **text-content reading of these two named primary works**. It does not complete review of all 409 outbound URL strings, the author's entire oeuvre, the full original De Concini–Strickland article, every linked repository file, or every proof in the books. It also does not establish an ECC speedup, a cryptographic security reduction, an analytic index theorem from first principles, or the Yang–Mills mass-gap conjecture.
