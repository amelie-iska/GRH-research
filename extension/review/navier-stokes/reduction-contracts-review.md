# Final-pass audit: exact reduction and signed orders

Review date: 13 November 2026.

## Result and scope

The existing `navier-stokes-release.tex` chapter preserves the distinction between
the released forced Navier–Stokes result and the unforced problem. The new
`reduction-contracts.tex` chapter adds a necessary-and-sufficient condition for
exact deterministic reduction, a quantitative lower bound on approximation
error, and a signed polynomial obstruction to replacing residual cancellation
by minimum-of-order arithmetic. All sixteen declarations in the new
`ReductionContracts.lean` module were compiled with the project's exact cached
Lean 4.24.0 and mathlib pins, with exit code zero, no warnings, and no unexpected
axioms. The complete evidence is in `extension/lean/reduction-verification.json`
and its accompanying log.

This pass read all 844 lines of the existing Navier–Stokes release chapter and
all 465 lines of `FluidInterfaces.lean`. It independently retrieved the current
official release, upstream metadata, final theorem adapters, independent
reference definitions, and the main statement of the analytic-forcing
follow-up. It does **not** claim a fresh manual rereading of every page of the
166-page source or every module of the upstream continuum proof. The earlier
complete-paper reading ledger remains the source of that previous coverage.

## Current source checks

| Item | Exact source | Observation |
|---|---|---|
| Official release | [OpenAI, 8 September 2026](https://openai.com/index/navier-stokes-solution/) | The release exists and concerns the forced problem. |
| Main manuscript | [Finite time blowup for Navier–Stokes](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf) | Theorem 1.1 and Corollary 10.6 agree with the chapter's retained scope. |
| Official response | [Clay, 11 September 2026](https://www.claymath.org/news/navier-stokes-announcement/) | Apparent settlement is acknowledged; no award decision is established by this page. |
| Problem definition | [Fefferman's formulation](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf) | Alternatives C/D permit forcing; the release does not prove A/B false. |
| Formal source | [Pinned upstream repository](https://github.com/openai/NavierStokesAndEuler/tree/f9e8bc5b38b6e212696e8a30e3e91517af887bbd) | The final declarations and challenge/solution separation remain as documented. |
| New structural obstruction | [Constantin–Ignatova–Vicol, arXiv:2609.20803v2](https://arxiv.org/abs/2609.20803v2) | The new chapter cites Theorem 1.1 with its exact restricted scope and references to the required estimates. It is not a global unforced regularity result. |
| Tropical context | [Litvinov, math/0507014](https://arxiv.org/abs/math/0507014) | Context for dequantization; the polynomial example is proved independently. |

The upstream revision still resolves to
`f9e8bc5b38b6e212696e8a30e3e91517af887bbd`, with tree
`a503f07635f200c0f2f9c5361df1fa07f95c4741`. Its metadata declares review
status `self-assessed`. The independent challenge files intentionally contain
placeholders. The final solution adapters import separate definition modules;
the presence of challenge placeholders is not evidence that they occur in the
solution dependency closure. Conversely, inspecting this separation does not
replace a completed kernel build and Comparator execution.

## Mathematical audit of the existing chapter

The quadratic residual formula retains the nonlinear correction term. The
averaging proposition explicitly assumes the multiplication identity needed
for conditional expectation and does not attribute that property to arbitrary
orthogonal spectral truncation. The concentration family is explicitly an
independent test family, rather than an asserted solution of the PDE.

The sparse Volterra argument includes the derivative of an intervening
coefficient; the block relation eliminates that term as well as the naive
double-derivative product. The text correctly avoids identifying the abstract
one-vertex algebra with a gentle algebra. Its cutoff realization fixes each
derivative order before choosing the finite stage, and the full curl includes
the differentiated cutoff. The pressure-class and disjoint-support cautions
are retained in the comparison and periodization sections. No correction to
these audited interfaces was required in this pass.

The fresh finite Lean checks prove the statements actually present in their
types. They do not verify the Volterra convergence proof, the PDE compactness
arguments, or every manuscript assertion. The preceding full-upstream build
attempt remains incomplete after the previously documented cache failure;
this new module does not change that status.

## New formal results and their meaning

### Exact factorization and dynamics

`factorization_iff_fiber_constant` is a genuine equivalence for arbitrary
functions with a surjective observation map. Its reverse implication constructs
the reduced map from representatives of the fibers. `reduced_output_unique`
proves uniqueness. These claims concern set-theoretic maps: regularity,
efficient computability, and neural representability are not implicit.

`discrete_closure_iff` specializes the theorem to state updates.
`discrete_trajectory_preserved` proves the commuting relation for every finite
trajectory by induction. `mismatched_fiber_excludes_closure` requires no
surjectivity and records the exact obstruction. Continuous-time use must
factor the observed derivative `D P(x) F(x)`, using `P(F(x))` only for linear
`P`. This calculus distinction is explicit in both module and chapter.

### Quantitative error

`fiber_error_lower_bound` and `fiber_diameter_le_twice_error` use actual norms
and the triangle inequality. They bound deterministic worst-case approximation
on a pair with equal observations. They do not assume a probability law or
promote sampled training loss into a continuum certificate.

### Signed tropical cancellation

The last nine declarations concern actual rational polynomials. For every
natural `k`, `X` and `-X + X^(k+2)` each have order one, whereas their sum is
the nonzero polynomial `X^(k+2)`. `trailingDegree` assigns infinity to the zero
polynomial, but all terms in this counterexample are nonzero. The result
therefore proves a substantive cancellation obstruction, rather than exploiting
a special convention at zero. `no_universal_minimum_rule` formally negates the
unqualified min-order rule even when all three nonvanishing conditions are
required.

## Reproduce this module

Use the exact compiler and mathlib revisions recorded in the manifest. From
the pinned mathlib checkout, run the pinned Lake executable with `env`, followed
by the pinned Lean executable and the absolute path to
`extension/lean/ReductionContracts.lean`. The manifest records the exact
successful command. The sixteen `#print axioms` commands must all produce
their recorded dependencies, with no `sorryAx` or other additional axiom.
This procedure performs local elaboration; it does not download or substitute
another compiler, alter the upstream proof, or claim an independent exported
kernel replay.
