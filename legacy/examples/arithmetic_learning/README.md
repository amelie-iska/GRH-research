# Exact learned arithmetic Fourier readout

This new finite learner targets the actual coupled sextic-character correlations
Gamma_(h,q,r)=sum_(0<Nu<=625) theta_(r,q/r)(u) 1_((u,h)=1).
It uses D6000,U60, principal nu, and **all15 squarefree ideal columns** at
norms7507,7519,8281,10507:2+4+1+8 ideals, with actual r_U=0,2,4.
Every raw common-prime zero, all six literal units and S-powers are retained.
The second2148-row case is a guaranteed nonprincipal subset of the2262 literal
rows, not the entire nonprincipal family. S consists of the primes above2,3.

The common smooth profile is

    phi(t)=exp(1-1/(1-t^2)) for |t|<1, and0 otherwise;
    W(y)=sum_(N in{7507,7519,8281,10507}) w_N phi(4*(6000*y-N)).

For the real case w_N=1; for the complex case
w_N=1+zeta6*(4N-30000)/6000. The four disjoint bumps lie in(1,2).
Thus W(n/6000)=w_n at these four integer norms and0 at every other integer norm.
The computation activates the complete original squarefree column family for
this specified W, rather than replacing all other annular columns by an
undeclared selection. No exponential is evaluated: every finite node is exact.
This does not study every possible smooth profile or the whole nonprincipal family.

Each (h,q) block has an active orientation set J in the finite phase group
G=(Z/6)^omega(q). Actual admissible rows form its exact sparse phase histogram.
The model is F_g(e)=sum_(r in J) g_r conjugate(theta_r(e)). Distinct orientation
characters are orthonormal under the full finite uniform group measure, so its
readout coordinates are g_r. The full finite projection loss is evaluated
**exactly through Parseval**, not by unexecuted sampled-feature training:

    L=sum_all210orderedoffdiagonalpairs lambda_r |g_r-Gamma_r|^2,
    lambda_r=1+|d_r^CC|^2+|d_r^CM|^2 >0.

The implementation uses zeta6 coordinates (a,b), with
|a+b*zeta6|^2=a^2+ab+b^2 and M=[[1,1/2],[1/2,1]]. The executed update

    g_next=(g+Gamma)/2

is preconditioned gradient descent of L/2 in the positive block metric
lambda_r*M. It is not ordinary real-coordinate GD. Every actual update and
complete rational state is saved. Conjugate initialization and the metric step
preserve the Hermitian offdiagonal targets; the diagonal is computed exactly.
This does not assert that the learned Gram is PSD. A separate50-update actual
ordinary-coordinate trajectory is saved as budget-limited, with no requested
error certification claim. Its step2/(3lambda_max) has the proved contraction
rho=1-lambda_min/(3lambda_max).

For CC and CM, predicted contributions keep mu(q) INSIDE the signed sum,
including complex W_m conjugate(W_n), actual r_U and all h deletions. Exact
Cauchy-Schwarz certificates satisfy

    |Ehat_X-E_X|^2 <= D^-2 [sum_r |d_r^X|^2/lambda_r] L;
    max_r |g_r-Gamma_r|^2 <= L/lambda_min.

The run accepts only when BOTH squared energy bounds AND the full-coordinate
uniform bound are <=tau^2. Because L_T=4^-T L0, every positive rational request
terminates on this fixed finite exact instance with unrestricted resources.
The CLI has a10000-update resource guard, which fails without certifying if
exceeded. No global conductor/range/runtime uniformity follows. The training
uses exact Gamma labels and therefore claims no asymptotic computational
advantage over their exact evaluation. It is separate from old q3/q4/q5
analytic-label learning and from upstream quantum-model training.

From the Linux repository root, use a **fresh** output directory:

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 nice -n15 python3 examples/arithmetic_learning/learn.py --tau 1e-12 --output outputs/experiments/2026-11-05-arithmetic-learning-v2
ARITHMETIC_LEARNING_RUN=outputs/experiments/2026-11-05-arithmetic-learning-v2 PYTHONDONTWRITEBYTECODE=1 nice -n15 python3 examples/arithmetic_learning/test_learning.py
PYTHONDONTWRITEBYTECODE=1 python3 examples/arithmetic_learning/learn.py --verify outputs/experiments/2026-11-05-arithmetic-learning-v2
```

Binary float tau values and nonpositive requests are refused. Existing output
directories are refused before computation. Source/helper bytes are captured
and checked before/after execution; all saved artifacts bind the exact input
hash, and the manifest freezes every artifact and source hash. Verification
refuses stale sources, inputs or artifacts. No prior checkpoint is imported.
The deterministic seed20261105 specifies SHA256-derived rational conjugate
initial values, with exact Fraction arithmetic and no random sampling.

Input records include all literal rows/local phases/raw zeros, columns/factors,
all225 exact Gram entries for each row set, pair-to-(h,q,r) metadata, sparse
phase histograms and common-profile semantics. Each case saves all210-vector
states, exact losses/predictions/error certificates, ordinary GD states and
actual learned feature values at selected phase tuples for inspection.

Focused checks independently reconstruct all31668 local symbols and all450
Gram targets with direct finite-field exponentiation and doubled rational/
sqrt(-3) coordinates. They test coefficient counts, finite phase orthogonality,
complex metric/gradient, loss normalization, raw common-prime deletions, literal
units, signed q terms, complex profile conjugation, scalar-only cancellation,
exact tolerance parsing, stale-byte refusal, immutable-output refusal and full
metric trajectory replay. These are new arithmetic checks, not reruns of the
accepted991 joint-Gauss or old analytic-training fixtures.

No analytic saving, BT_sigma bound, positivity of covariance, PSD or positive
arithmetic determinant, zero-location bridge, Lean declaration, quantum
advantage, generalization or GRH result is claimed. No dependency, GPU job,
authentication, environment or publication change is required.
