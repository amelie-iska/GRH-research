# An ordinary conductor comparison and a certified finite arithmetic learner

This is a refinement of the project's application of classical large sieves,
not a new classical sieve or a proof of GRH. The complete prose derivation is
in [the book](https://amelie-iska.github.io/GRH-research/book/main.html#mcs:core).
The [exponent inspector](https://amelie-iska.github.io/GRH-research/quadratic-pivot.html)
compares upper bounds, rather than measured operator norms.

For the original raw sextic family, the first-five-factor radical conductor
has size Q = A1 A2 A3 A4 A5. Freeze the arbitrary overlapping sixth factor
as its actual common-prime coefficient mask. An ordinary all-primitive-character
large sieve then gives block operator bound A6(D + Q²), up to fixed-S and
subpower factors. The proof includes primitive Gauss sums at all moduli,
nonunit-frequency vanishing, reduced Eisenstein-fraction spacing and a
Gaussian/Poisson two-dimensional lattice sieve. It retains original zeros
and the safe tuple multiplicity 5^ω(q); it does not assert that every mixed
radical family satisfies the higher-order-family reciprocity hypotheses.

Combining with the previously accepted powered-family estimate and the actual
capacity inequalities gives the all-row, residue-subtracted envelope

    sum_(0<Nu<=H) |E_u|² << ||W||∞² (HD)^epsilon
                              [H + D H^(1/6) + (DH)^(2/3)].

The twist ν and S are fixed; W is one common, possibly complex, smooth profile
supported in [1,2]. All original conductor, squarefree, ray and collision
conditions remain. At H = D^(3/4), the exponent improves from 5/4 to 7/6;
the remaining excess over H is D^(5/12). On the entire old A1=A2=A,
A3=B, AB=H^(1/3) face, the new comparison costs D^(1+epsilon).
The new available upper envelope still reaches 7/6 at (log_D A1,log_D A2)
= (5/12,1/6) and at the pure A1=D^(3/4) point. These are witnesses for
upper-bound monomials, not actual energy lower bounds. The signed joint
h,q,K estimate and independent determinant/zero-location bridge remain open.

## Learning the actual finite coupled correlations

The separate [arithmetic learning replay](https://amelie-iska.github.io/GRH-research/arithmetic-learning.html)
shows executed classical Fourier-feature readout training. It targets every
actual correlation Γ_(h,q,r), including its complex phase and full raw zero
mask. It is separate from the preserved q=3,4,5 analytic-label experiment.

For positive rational weights λ_i = 1 + |d_i^CC|² + |d_i^CM|², the full
spectral-metric loss is L = sum_i λ_i |g_i − Γ_i|². Weighted Cauchy–Schwarz
transfers this full-vector error to both signed CC and Cμ observables;
the predicted sums retain μ(q) and complex W conjugation. The executed
metric-gradient update g_next = (g + Γ)/2 gives exact L_next = L/4.
A separate ordinary-coordinate trajectory is also executed and explicitly
budget-limited. Neither is upstream quantum training.

The specified common smooth four-bump profile activates **all 15 original
squarefree ideal columns** at norms7507,7519,8281,10507. D=6000,U=60,H=625,
principal ν and S above2,3 are fixed. The two row cases have2262 literal rows
and2148 guaranteed nonprincipal rows; the latter is a subset, not the whole
nonprincipal family. There are95 blocks (65 with h=1),210 offdiagonal learned
coordinates and4530 raw column zeros per row case. Real and complex profiles
produce four requested1e-12 certificates after53/55/53/55 metric updates.
Every one of the216 metric and200 ordinary updates is saved in exact rational
coordinates. The full-vector and both observable certificates pass.

The full labels are evaluated exactly before training: this proves a finite
supervised approximation certificate, without a computational speedup,
generalization, asymptotic signed saving, PSD/positive arithmetic determinant,
zero location or GRH conclusion. For every positive rational request the
finite metric construction terminates with unlimited resources; the actual
CLI has a10000-update guard and refuses without certifying when exceeded.
The web page displays floating projections of saved states, not browser
training or a replacement for exact rational verification.

## Reproduction and evidence

- `examples/arithmetic_learning/README.md` states the loss, exact profile,
  seed20261105, reproduction CLI, resource guard and refusal contracts.
- `outputs/experiments/2026-11-05-arithmetic-learning-v2/manifest.json` binds
  all input, source and saved-state bytes. The logging-only partial v1 run
  remains preserved and is not the accepted run.
- `planning/arithmetic-learning-20261105/review-mixed/REVIEW-v1.md` audits
  the full analytic proof; fresh wild-modulus checks are supporting finite
  diagnostics, not its proof.
- `outputs/checks/2026-11-05-arithmetic-learning/review-learning/` records
  the independent local-symbol, Gram, histogram, every-update, certificate
  and tamper checks.
- New shared sources are `papers/mixed-conductor-{core,details}.tex` and
  `papers/arithmetic-learning-{core,details}.tex`, included in all editions.

No new Lean declaration is supplied. The existing request for approval of
an isolated official Linux4.24 compiler remains pending; no toolchain was
installed or substituted. Original manuscripts, sources, environments,
datasets and unrelated progress remain protected. Both completion gates
remain false.
