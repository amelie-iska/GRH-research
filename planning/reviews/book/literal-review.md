# Independent literal AR and physics chapter review

2026-11-03. Read-only review; this report is the only shared file written by this reviewer. No source clones, manuscripts, environments, dependencies, caches, Git history or generated research data were modified.

## Exact coverage

Read all 817 lines of `book/chapters/ar-components.tex` and all 804 lines of `book/chapters/physics.tex` as present at review time, the source-integration report `planning/reviews/book/source-review.md`, the prior primary-source physics audit `/tmp/grh-book-physics-review.md`, and the corresponding new bibliography chunks where relevant. This is literal review of the corrected chapters, not a new end-to-end certification of every original source, every cited paper, or every hardware measurement. The source report preserves the distinction between prior collective full coverage and the fresh differential reading of the two supplied versions.

## One mathematical correction required

In the laboratory drive calculation, the displayed

H(t) = hbar omega0 Z/2 + hbar Omega cos(omega0 t + phi) X

with the resonant interaction frame R(t)=exp(+i omega0 t Z/2) gives

H_rot = hbar Omega (cos(phi) X + sin(phi) Y)/2.

Indeed R X R* = cos(omega0 t) X - sin(omega0 t) Y; averaging its product with cos(omega0 t+phi) gives the PLUS sign. The chapter's minus sign would instead match a drive cos(omega0 t-phi). The parent was notified; change one of these signs and name the frame. The phi=0 pulse examples are unaffected. A 2048-point in-memory quadrature at phi=.61 gives error 7.24e-16 against the plus formula and .810 against the minus formula, corroborating the exact trigonometric derivation.

## Organizational correction

`book/main.tex` emits a physics part title immediately before inputting `physics.tex`, which itself begins a different part title. Remove one to avoid consecutive part pages with no intervening content. The parent was notified. This is an integration issue, not a mathematical objection.

## Confirmed explicit constructions and category boundaries

- The theta face-unfolding is exact and faithful but not full. The three-to-six primitive-idempotent obstruction correctly refutes the asserted unital quotient. The two equal-dimension examples have varying Hom defects, so do not meet the bilinear K0 definition of Hom control.
- The circular-complex kernel incidence construction uses dim R_i=d_i-r_i. Its allowed maps form a vector bundle; feasibility supplies the intermediate subspaces, full-rank points have R_i=ker D_i, and properness comes from the Grassmannian factor. The statement is correctly assigned to its six-factor group.
- The finite-covering Hom decomposition is not conflated with Zwara's bilinear numerical condition. The S1+S2/P1 example has the displayed defects 2 and 1 at the same K0 class.
- The polynomial smooth-support node tube fixes quasi-length under tau. The completed-node lattice category has exactly the three displayed indecomposables and two almost-split rows; its stable category has two isolated ordinary vertices, with suspension/translation exchanging them.
- The signed HLS diamond is assigned to the actual continuous quotient-annihilator category. The finite matrix window and the source's global hook/cohook theorem have distinct roles. Infinite-pd E=M(ab) correctly blocks its promotion to an AR triangle ending in E in the bounded derived category.
- Ringel's tile is a scoped quilt comparison with infinite-word limits and a different source algebra. No unproved category identification or equality of quilt genus with Belyi genus is asserted.
- The free-generator A2 example refutes the blanket mesh-to-syzygy inference. The product theorem retains separate square-evaluation and short-projective-resolution conditions. Relative node R-determinants and the framed six-minor Pluecker presentation have their stated, different targets.
- Physics correctly distinguishes total positivity from Hermitian positivity, positive transfer from unitary logarithms, finite central quotients from faithful rotation-algebra representations, odometer towers from irrational-rotation limits, and actual CP pooling from an impossible d²-to-d isometry.
- The finite first law, regularized correlation metric, POVM requirement, noise/dilation statements, isotropic-exchange formula and hyperbolic CSS counts are internally consistent. Einstein limits, molecular assemblies, coherence improvements, thresholds and arithmetic identifications remain explicitly additional assumptions or proposed work.
- No complete GRH conclusion is asserted in either reviewed chapter. Learned channels, tube parameters, categorical tau, hardware clock phases and quantum spectra are not substituted for an independently proved arithmetic determinant comparison.

## Focused independent in-memory diagnostics

Used only the already approved isolated CPU environment. Checked the normalized transfer logarithm identity (error 3.14e-16), the stated positive-sign Fourier conjugation in dimensions 2 through 8, and 50 fixed-seed pooling-feature and isotropic-exchange identities (all errors below 1e-12). Seed 817. These are finite corroborations of the written universal algebra calculations, not proofs of AR factorization, global QFT or GRH.

## Validation boundary

This review did not rerun the full Lean suite, independently repeat the framework training, inspect a compiled integrated book PDF, or verify every experimental number against its primary dataset. Those tasks remain the parent's compilation/computation review stages. The RWA sign and duplicate part title should be fixed before the reviewed manuscript is accepted. No other blocking inconsistency was found in the literal explicit constructions within this review's scope.


## Integrated-book acceptance follow-up

The two issues above have been corrected in the integrated source: the RWA formula now has the plus sine with its stated resonant frame, and the extra consecutive physics part heading has been removed. The earlier “required before acceptance” wording is superseded by this follow-up.

Read all of the new `computations.tex` (149 lines), `frontier.tex` (43 lines), and `toricgt.tex` (378 lines), plus the generated training-results table. The hyperelliptic Belyi passport/genus/order-rank argument is consistent; the three periodic torus lifts have disjoint interiors and give the one-face theta rotation system. The exact Ising decimation and Boolean-Fourier star-to-triangle teachers are correct and clearly separated from learned outputs. The Gaussian principal-axis objective has its stated analytic optimum. The Segre normal-form proof, toric/tropical distinctions, Weyl cocycle gauge and factor-of-two correction are consistent. The Harper benchmark's rank-two argument yields the stated characteristic polynomial t²(t²−4(1+lambda²)) and ground energy −2 sqrt(1+lambda²). Its exact principal-minor acceptance/repair is not represented as a theorem about arithmetic L-functions.

Rendered the integrated 116-page PDF's physical pages 70, 73, 75, 78, 80, 88, 95, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 and 109 at a maximum dimension of 1800 pixels into `/tmp/grh-book-literal-visual/`. Visually inspected all nineteen on four contact sheets; additionally inspected full-size pages 73 (the signed HLS diamond), 75 (Ringel tile) and 101 (all training plots). No clipping, overlapping labels/arrows, missing symbols, broken equations or illegible figure labels were found on these selected pages. The log has no overfull boxes or unresolved references/citations. The book has a consistent chapter/section hierarchy; this was a selected-page review, not a claim to have inspected all 116 pages individually.

Reviewed PDF SHA256: `c9596bf341414f6f19a57261bc50243e128a50bc884f260b5060db01fd95845a`.

No further blocking issue was found in these newly reviewed literal sections or selected layouts. Complete book-wide Lean formalization, Sage execution, GPU execution, physical hardware realization and the arithmetic spectral bridge remain explicitly unestablished. This follow-up did not independently repeat all framework training, the full analytic suite, or all original-source primary literature. It supports acceptance of the stated finite/modelled results within these boundaries, not completion of GRH.
