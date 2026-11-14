# Live verification workbench and finite-search calibration

Review date: **13 November 2026, America/Los_Angeles**.
Machine records use UTC timestamps.

## Mathematical and operational scope

The new chapter is `extension/manuscript/chapters/verification-workbench.tex`.
It adds exact contracts and a conditional measure-theoretic false-positive
argument to both manuscript editions. The generated registry identifies the
current page anchors, source/type hashes and compiler identity for the Hodge,
quadratic cover, weighted gain and cosmology contracts.

The browser does not run a Lean kernel. It performs exact finite arithmetic,
exports a source-bound record and imports a validated state transaction.
Generated Lean files use fixed templates and validated literals. Their actual
compiler checks are separate from arithmetic replay and from the aggregate
declaration count. Hashes identify content; they are not signatures.

## The finite null model

The noise model is defined by the stored 96×96 factor `L`:
`Y=L ξ` for ideal independent standard Gaussian coordinates `ξ`.
The 288 stored filters and factor entries are interpreted as exact binary64
constants. All variances `||Lᵀw_j||²` are reconstructed exactly and bounded by
`1000000000001/1000000000000`. This outward envelope is not an assertion that
every numerical filter has exactly unit variance.

`build_moment_contract.py` performs integer/dyadic construction;
`cosmology_certificate.py` independently uses full-column Fraction dot
products, importing neither the JavaScript producer nor the builder.
`verify_cosmology_moments.py` compares every returned field in 32 cross-language
cases, rejects 29 invalid-domain cases, checks nine binary64 conversions,
rejects three nonfinite coefficients and three model tamperings, and
independently reconstructs all 288 variances. Ordinary and optimized Python
records are separate. No validation depends on executable `assert` statements.

The moment model binds the dataset, factor and builder hashes. The browser
checks all three model asset hashes against its registry before enabling the
certificate panel. These checks establish the declared finite coefficient
model, not equality with an unrounded covariance kernel or a physical sky.

## Probability and rank boundaries

The Lean theorem uses a genuine probability measure, measurable scores,
integrable absolute even powers and true moment inequalities. For a fixed
positive threshold and finite family it proves

`P(∃j: Z_j ≥ t) ≤ min(1, Σ_j M_j / t^(2k))`

without requiring independence between the scores. The Gaussian moment formula
has a written integration-by-parts argument; formal construction of the
Gaussian product law and its moment identity remains an explicit obligation.

A scalar inequality is not relabelled as a probability theorem. The emitted
Lean instance applies the actual measure theorem with all its model
assumptions retained. The capped-bound case `alpha=1` uses the capped theorem
when the stronger uncapped budget premise is false.

The 4095 stored calibration maxima give a finite rank with floor `1/4096`.
Its arithmetic is checked separately. No exchangeability theorem, exact PRNG
law, observational-data claim or universal calibration guarantee is asserted.
A threshold selected after viewing the same sky does not automatically inherit
the fixed-threshold risk guarantee.

## Primary source and reproduction

The formal Markov step comes from the project's
[pinned mathlib source](https://github.com/leanprover-community/mathlib4/tree/f897ebcf72cd16f89ab4577d0c826cd14afaafc7/Mathlib/MeasureTheory),
in `Integral/Bochner/Basic.lean`:
`MeasureTheory.mul_meas_ge_le_integral_of_nonneg`.
The [current official API documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/Bochner/Basic.html)
was inspected as a navigation aid; it can change independently of the pinned
source. The manuscript's finite algebraic and probability arguments are
self-contained. Formal component correspondence is recorded explicitly in
the source/type map.

Canonical evidence:

- `extension/lean/final-verification/verification.json`
- `extension/lean/laboratory-verification/verification.json`
- `extension/verification/lab-certificate-bridge.json`
- `extension/review/final-pass/lab-certificates/`
- `extension/review/final-pass/cosmology-moments/`

The finite-resolution chapter and source note explain spatial, temporal,
finite-box, phase-aliasing and roundoff boundaries before a numerical residual
enters a control recurrence. These records do not claim new continuum
Navier–Stokes, GRH or Yang–Mills results.
