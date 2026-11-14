# Review of the principal upstream mathematical source files

Review date: 13 November 2026. Reviewer task: `orders_volume_two`.

## Snapshot and actual coverage

The primary source is [amelie-iska/GRH-research at the frozen commit](https://github.com/amelie-iska/GRH-research/tree/dbd954eede479a5129831e4e7c30537389ae973d), commit `dbd954eede479a5129831e4e7c30537389ae973d`. The four files below were read in their entirety as source text, in bounded output chunks. Gaps caused by initially truncated tool output were reread before recording complete coverage.

| File relative to upstream repository | Lines | Whitespace words | Bytes |
|---|---:|---:|---:|
| `book/main.tex` | 67 | 466 | 5,119 |
| `book/chapters/reviewed-mathematics.tex` | 1,453 | 23,652 | 181,791 |
| `papers/core.tex` | 1,072 | 6,123 | 50,292 |
| `papers/details.tex` | 1,621 | 9,893 | 77,885 |
| **Total** | **4,213** | **40,134** | **315,087** |

These counts measure actual source files. They include LaTeX commands and repeated arguments between the summary and expanded sections; they are not counts of unique mathematical prose. Complete text review is not a blanket assertion that every proof is correct or that every cited theorem was independently proved. Several central constructions and diagnostic counterexamples were checked logically, as described below. External deep theorems retain their external status.

Exact SHA-256 identifiers:

```text
book/main.tex
f9ffbeb5e9e204ee980042e2d753999e618aa3aed67cc7f3f0b79855b4b53561

book/chapters/reviewed-mathematics.tex
886dd136c7dbc4e6715fc326b6dc5cb59776bed19fb680bd67930862e75b27a9

papers/core.tex
767e7373b9e49887df50059ab38d6b3df3f65236b21d6475e960d0c67a1bd868

papers/details.tex
de0089049bb53bcc426ac80189dc7afd9644ba54de975af6a2054b63a28b0127
```

The root synthesis chapter was also read completely: `extension/manuscript/chapters/synthesis.tex`, 423 lines, 2,896 whitespace words, 21,218 bytes, SHA-256 `a625d875fbb00dd94850bfe7046d49c4415f7e1953da8decceb36f1101a5f412` at review. Later changes, if any, require a fresh hash.

## Scope exclusions that remain material

`book/main.tex` includes nineteen chapter files. This review covers its entry-point text and the one requested generated mathematics chapter; it does not claim that all nineteen chapters were read by this reviewer. Other team reviews have separate ledgers.

Each of `papers/core.tex` and `papers/details.tex` includes two additional files at its end: the corresponding `short-row-pair-*` and `mobius-split-*` sources. The content of those four transitive inputs is outside this review. Reading an input directive is not reading the input file.

The 409 distinct external URLs in the larger inventory were not all opened and reviewed. The linked mathematics submodule's 174,524-file tree is an inventory, not content coverage. Neither the complete oeuvre of the classical book authors nor all linked modern author manuscripts has been independently proof-audited. No contrary coverage statement should be inferred from this report.

## Overall mathematical assessment

The fully read files do **not** present their conditional interfaces as a completed proof of GRH. They explicitly separate valid finite calculations, counterexamples to earlier intermediate claims, arithmetic input supplied from outside a construction, and remaining analytic obligations. The corrected conditional closure statements are mathematically informative precisely because their difficult approximation and positivity assumptions remain visible.

The upstream source supplies a substantial algebraic and diagnostic research program. Its most useful contributions to the new monograph are explicit order examples, projective resolutions, distinctions between module categories, determinant multiplicity obstructions, and counterexamples to invalid operator or arithmetic transfers. It does not supply a Yang–Mills mass-gap proof, a quantum ECC speedup, or a lattice-cryptographic security reduction. The new monograph's synthesis likewise explicitly declines those conclusions.

## Orders, resolutions, and representation-theoretic interfaces

The generated chapter distinguishes the arrow-adic order parameter from path degree, and keeps formal, Laurent, and operator-norm completions separate. Its locally gentle closed examples have infinite projective resolutions along forbidden words. The endpoint dependence of Ext and the failure of simples to be perfect are retained; these are not treated as incidental exceptions.

The adjacent-generator staircase resolution is supplied with explicit syzygies and signs. The accompanying calculation for `(x², xy, y²)` has the expected three generators and two adjacent relations. Tensoring an auxiliary resolution with an order is discussed through a mapping-cone argument rather than assumed automatically exact in every setting.

The corrected DG model uses `d ε = ξη`. The source recognizes that `d ε = 1` would contract every module and cannot describe a nontrivial ground-field object. This distinction is essential when a relation is replaced by a differential.

The determinant semi-invariant construction retains its change-of-basis weight. Vanishing Hom in the square presentation controls the stated first Ext calculation, but not all higher Ext; the source gives the missing higher orthogonality its own status. On the reduced continuous nilpotent representation variety, ordinary invariants are constant by degeneration to zero arrows, while semi-invariants may vary. This is a coherent distinction, not a contradiction.

Schur constructions preserve the stated monomial zero relations for nonempty partitions, but the source explicitly identifies failures of additivity and preservation of a fixed central parameter. A Schur-character identity or a positive Cauchy kernel therefore cannot alone establish an exact functor with the desired arithmetic scalar action.

The nodal lattice classification and almost-split sequences are stated in their exact lattice setting. The Chebyshev quotient meshes are intrinsic to the specified quotient; the text does not automatically identify them with an ambient Auslander–Reiten component or an extension-closed subcategory. The classification of finite polynomial strings likewise does not exhaust completed lattices.

The source correctly restricts the surface/Fukaya comparison. Closed permitted and forbidden cycles obstruct the direct use of smooth/proper hypotheses. Passing to a smooth quotient gives a different category, and inflation need not be derived fully faithful. These category boundaries should remain visible in any reuse.

## Operator completions and arithmetic attachment

The original CK1 relations combined with forbidden products force collapse in the specified setting. The constrained Fock construction instead uses different initial projections; it is not presented as a harmless relabeling of the collapsed algebra. The terminal-sector compact ideal, permitted-circle quotient, and integer boundary map are described separately.

The graph presentation and the diagonal-fiber pullback are different completions. In particular, raw diagonal residue extraction need not be a ring map. The source repairs this with a specified fiber condition and separately checks a faithful polynomial embedding. It explains why this embedding cannot automatically extend to every formal series: a formally invertible element may map to a singular operator.

A degree operator with compact resolvent produces explicit zeta-type traces after the requisite external character input. This is not an identification of arithmetic zeros with that operator's eigenvalues. A positive degree operator's Fredholm-class calculation also does not supply the missing spectral determinant identity.

The Abel rank-one construction analytically encodes the desired scalar arithmetic function in a Fredholm determinant on its stated half-plane. Its estimates concern trace-norm holomorphy. Because the arithmetic coefficients have already been inserted, the encoding is not an independent derivation of arithmetic from the order. The fixed-range positive-metric obstruction is a useful warning against interpreting this encoding as a self-adjoint realization.

The rational-twist example has the correct logical scope: the same complex dessin can correspond to distinct arithmetic local factors when rational descent differs. It does not refute a theory with specified descent data. The source also distinguishes the weight-one elliptic center from the Dirichlet center.

The local Gauss/Jacobi calculations and the cellular two-dimensional carrier form a concrete benchmark. The rational chain lift cancels auxiliary determinants to recover the intended local polynomial. The source does not infer from this a canonical integral Tate module, an order-linear Frobenius, or a global positive spectral limit.

The projective determinant calculation exposes ordinary determinant multiplicities. A later branch coefficient functor removes one particular multiplicity by choosing a branch/vertex and changing the target. The resulting loss of symmetry is part of the theorem's scope. Tame descent can preserve a hereditary endomorphism order while its column comparison has determinant equal to the ramification parameter and is not an integral isomorphism.

The full-deck finite-free fixed-center coefficient-kernel obstruction is stated for that class. It must not be expanded to rule out all infinite-dimensional, semilinear, or twisted determinant constructions. The finite-cover pushdown examples likewise distinguish exactness from fullness, density, and control of derived Hom.

## Analytic closure and diagnostic examples in the papers

The corrected closure theorem uses zero confinement of fixed self-adjoint finite models, a nonvanishing normalization, and local uniform convergence to the actual completed arithmetic function. Rouché/Hurwitz then has the intended force. The arithmetic approximation hypothesis is indispensable. A normal-family route additionally needs local boundedness and agreement on a genuine overlap; these conditions cannot be replaced by formal analogy.

Several simple obstructions were checked directly at the algebraic level:

- For a hyperbolic integral determinant-one matrix, an alleged integer expanding norm `n > 1` forces the trace-square relation `t² = n + 2 + 1/n`, which cannot be integral.
- Integral generation by cyclic inductions fails in the stated Klein-four example by degree parity. Rational Artin induction and induction from elementary/hyperelementary subgroups have different conclusions.
- Taking the Hermitian part or a Hermitian dilation changes determinant information and can discard complex phase. It does not preserve the original arithmetic determinant merely by producing self-adjoint matrices.
- A positive definite generalized pencil has real generalized eigenvalues; the indefinite case needs a different conclusion, and the source supplies a counterexample.
- Strong operator convergence is weaker than trace-norm convergence. The rank-one projection example `P_n → 0` strongly while `det(I-P_n)=0` demonstrates the determinant obstruction.
- Holomorphy of a matrix family that is Hermitian in one fixed positive metric throughout a complex open set forces constancy. This does not exclude Hermitian values only on the real axis or a fixed spectral operator with a complex resolvent parameter.

The finite Euler-product obstruction is a valid application of zero-free locally uniform limits. The replacement Dirichlet partial sums have a controlled fixed-character Abel error on `Re s > 0`, but their finite zero sets are not constrained to the critical line. The explicit off-line zero certificate for the stated five-term approximant is consequently a counterexample to that approximant's proposed finite spectral model, not to GRH. Its detailed rational estimates are supplied in prose; this review does not label the entire certificate Lean-verified.

The Jensen-polynomial discussion separates coefficient convergence from universal Newton/Hankel positivity. The latter is where the RH difficulty remains. Positivity of an unrelated moment kernel cannot establish it; the displayed mixture example has a negative required minor. Similarly, holomorphic continuation of the prime-linear function into the critical half-plane is tied to a zero-free conclusion and cannot be assumed as an innocuous regularization.

The later Euler-correction, frozen-count, low-energy, central-contour, and reflected-block sections contain useful exact exponent bookkeeping. Their scalar identities, moment estimates, height conditions, common-density estimates, and remaining row bounds are not all independently established. The source labels these interfaces accordingly. The shifted angular Hecke factor is considered under explicitly external analytic theory; it is not silently equated with a proof of GRH or a refutation of another claimed region.

The finite-field correlation discussion requires nonzero residual unit data where indicated; zero extension has its own behavior at the all-zero input. The periodic Poisson estimate uses annular support, the normalized Fourier transform, and summable decay in four dimensions. The support hypothesis is essential because an origin contribution can survive without it. These are substantive hypotheses, not cosmetic conventions.

## Specific editorial and integration findings

1. **Earlier multiplicity sentence needs local scope.** At generated chapter line 1158, the statement that no multiplicity-removing functor is supplied is too broad if read as a claim about the entire later document. The section beginning at line 1220 supplies an actual branch coefficient functor under changed requirements. Suggested qualification: no such repair is supplied by the naive tensor insertion currently under discussion; the later functor changes the determinant target and sacrifices specified symmetry. No upstream text was silently edited in this review.

2. **Historical formal declaration counts are not a fresh build.** The generated chapter includes successive accounts of earlier formal layers and their literal limitations. These counts should not be combined or described as a newly compiled complete proof suite without a manifest and successful build for that exact snapshot. The new extension's separate 25-declaration build has its own authentic log, dependency report, and hash.

3. **Generated source requires provenance-aware maintenance.** The reviewed mathematics file is generated. A future correction should be made in the maintained source that produces it and then regenerated, so a generated-file edit is not lost.

4. **Three-term exactness means middle exactness in the synthesis example.** The displayed rank-one consecutive maps on real two-dimensional spaces satisfy `im A = ker B`. A truncation with zero terms at both ends is not exact at both endpoints. The synthesis treats them as consecutive differentials and computes the middle Hodge operator; subsequent summaries should preserve the word “middle.”

## Direct check of the new synthesis chapter

For `Λ = R[X]/(X²-uX)`, with `x = X` and `y = u-x`, the basis `(1,x)` gives the stated matrices of multiplication. Their products are zero. Comparing coefficients establishes `ann(x)=Ry` and `ann(y)=Rx`, hence the alternating free resolution. Tensoring with `Λ/(x)` changes the maps to alternation between zero and multiplication by `u`; when `u` is a non-zero-divisor, the positive odd Tor groups are `R/uR` and the positive even groups vanish. The generic and special fibers have the described split/idempotent and dual-number forms.

For the real specialization `u=t`, the maps have rank one, are exact in the middle, and direct multiplication gives `AAᵀ+BᵀB=(1+t²)I`. Scaling both differentials by a nonzero scalar preserves their images and kernels and scales this Hodge operator by the scalar's square. Thus each finite member is positive while a family can have least eigenvalues tending to zero.

The quantitative transport lemma correctly assumes a lower norm bound for an isomorphism. Passing to the inverse image of the kernel and taking infima transports the distance estimate. Pointwise invertibility without a uniform smallest-singular-value bound is insufficient. These calculations supply a concrete bridge between algebraic exactness, integral degeneration, and metric control without claiming a quantum physical gap or a cryptographic algorithm.

The synthesis conclusion explicitly disclaims a proof of GRH, a Yang–Mills mass gap, a generally faster ECC algorithm, and a new lattice-security reduction. No unsupported overall conclusion of those forms was found in the reviewed files.

## Disposition

The four requested upstream files and the entire synthesis chapter have completed text review. The selected elementary inferences above are checked; advanced external inputs, unreviewed transitive files, and the remaining analytic interfaces retain their explicit status. No manuscript edits were made during this audit. The separate source-concordance chapter summarizes coverage and provenance, and the book review ledgers record the all-page OCR reading and selective visual/proof audit of the two classical volumes.
