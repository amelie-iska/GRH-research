# Holomorphic learning and coherent continuum densities

Independent review2026-11-04. Read both `holomorphic-learning-*.tex` files,
`holomorphic_learning.py`, `electron_clouds.py`, its independent integral
checker, and received cloud physics/generation evidence. No production edits,
remote host, credentials, model repository, installation or training action.

Verdict: the load-bearing mathematical claims and physical boundaries are
accepted after explicitly adding `beta>0` to the infinite-feature rate statement.
That correction was applied by the root agent and independently confirmed.
No GRH-equivalent positivity premise is hidden in the approximation theorem.
Bibliography/domain clarifications sent below remain integration checks.

## Four-term Fourier/Cauchy theorem

With `m>N`, the sampled monomial columns are exactly orthogonal. The real and
imaginary gradient of the stated `1/(2m)` complex squared loss is `b-b*`, so
the optimizer factor is exactly `(1-gamma)^k` for `0<gamma<2`. The evaluation
norm is bounded by the geometric-series factor stated in the theorem. Numerical
coefficient rounding is separately budgeted, rather than silently included in
exact GD.

For exact circle samples the retained coefficient is
`a_n rho^n + sum_(ell>=1) a_(n+ell*m) rho^(n+ell*m)`. Because `n<m`, no negative
alias appears. Dividing by `rho^n`, using Cauchy's coefficient estimate and
evaluating at radiusR gives exactly the displayed alias geometric series in
`w=(rho/r)^m` and `v=R/r`. Pointwise sample errors contribute the separate
`eta sum_(n=0)^N (R/rho)^n`. The Taylor remainder is
`M_r v^(N+1)/(1-v)`. All terms and radius ratios are correct.

Choosing degree, sampling count, certified oracle tolerance and optimization
tolerance successively proves arbitrary requested approximation accuracy on a
fixed compact subdisk for the stated finite family. This is an exact fixed
holomorphic feature/readout theorem, not nonlinear feature learning, a zero
location result or a claim of feasible uniform complexity at all conductors.
The ordinary high-precision demo has assumed evaluation error and unvalidated
floating arithmetic; its conditional error budgets are not interval certificates.

## Infinite Szego readout

The kernel's geometric compact-uniform convergence and PSD follow directly
from its monomial features. On the specified population circle, Gram
eigenvalues are `(rho/r0)^(2n)`. Analytic target coefficients `a_n r0^n` lie in
ell2. For any ell2 initial error, diagonal semigroup decay plus dominated
convergence yields norm convergence and compact-uniform evaluation convergence.

The source condition and rate are correct for **beta>0**: writing initial
error as `lambda_n^beta` times an ell2 sequence gives the supremum
`sup_(lambda>0) lambda^beta exp(-t lambda)=(beta/(e*t))^beta`. Cauchy's bound
gives the claimed explicit geometric B_beta bound when
`(r0/r)(r0/rho)^(2beta)<1`. There exists a positive allowable beta because
`rho<r0<r`. No width-uniform exponential rate follows as eigenvalues approach
zero. The text correctly separates an unbounded infinite whitening operator,
ridge bias and a GP initialization which need not be in the RKHS/ell2.

## Unconditional primitive Dirichlet bound

For primitive nonprincipal characters, the positive-n theta convention and
Mellin normalization agree with the usual completed L-function. The transformed
second integral correctly retains the conjugate character, root number and
exponent `(1-s+a)/2-1`. Primitivity/nonprincipality and character parity are
material hypotheses; the claims do not silently cover principal poles or
general Artin holomorphy.

The integer k bounds both real Mellin exponents on the whole disk. Integration
by parts gives the exact `exp(-x) Q_k(x)` formula. Absolute theta bounds then
give `2 sum n^a exp(-d*n^2) Q_k(d*n^2)`. For the remaining sum from n0,
`n^a exp(-d*n^2/2) <= C_a` with `C0=1`, `C1=(d*e)^(-1/2)`; decreasing Q and
`(n0+j)^2 >= n0^2+2n0*j` yield exactly the stated denominator
`1-exp(-d*n0)`. Twice that majorant covers both Mellin terms.

These exponential tails plus compact-interval validated quadrature give a
computable oracle without GRH. For clarity, state `n0>=1` and `delta>0` in
the separate logarithmic-derivative tail paragraph; the intended positive
domains were communicated to the root agent. The logarithmic-derivative
tail integral itself is correct for `N>=3, delta>0`. The main numerical demo
uses three real primitive characters and explicitly remains a diagnostic,
rather than claiming this general certified oracle has already been implemented.

## Positivity and zero-location boundary

The Rouché circle centered at i of radius1/4 has
`|1+z^2| >= (1/4)(2-1/4)=7/16`. A smaller uniform error by a real-rooted
polynomial would force a nonreal root inside it. The floor and impossibility
of local-uniform approximation are correct. This explicitly blocks an invalid
universal approximation claim for an already-real-zero determinant class.
The text does not assume Weil/arithmetic positivity, a self-adjoint arithmetic
identification, Artin holomorphy or the missing signed moment estimate.
Rouché contour transfer, trace-class determinant continuity and their domain/
Schatten hypotheses retain the appropriate separate acceptance conditions.

The integration check initially found citations `HLNTK`, `HLDirichlet`,
`HLFredholm` without bibliography definitions. The root agent was notified to
add pinned primary entries before the final paper/book build. This is a source
integration item, not a mathematical objection to the elementary proofs above.

## Gaussian integrals and continuum particle density

For normalized s Gaussians the source implements the correct overlap S,
kinetic integral `mu*(3-2*mu*distance^2)*S`, and nuclear attraction
`-Z*Ni*Nj*exp(-mu*distance^2)*(2*pi/p)*F0(p*|P-R|^2)`. The Boys function's
small-argument replacement by one is a disclosed ordinary numerical
approximation, not an interval certificate. Symmetric Lowdin L=`S^(-1/2)`
gives `L S L=I`, and the orthonormal Hamiltonian is `L H_AO L`.

The density is `sum_a |sum_i g_i(r) [L U(t) C0]_ia|^2`. It includes the
cross terms of actual coherent occupied orbitals; it is not independent atom
smearing. Its full-space integral is the occupied rank because
`C0* C0=I` and U is unitary. H2+ has one occupied state; its initial
`C0=S^(1/2)e0` maps back exactly to the first normalized left Gaussian. Six s
functions at fixed proton separation2bohr define a legitimate finite Galerkin
Coulomb model, with nuclear repulsion1/2hartree separated from electronic
energy. The finite basis is not asserted converged.

The Trp-cage case instead realizes the explicitly uncalibrated contact
Hamiltonian in an orthonormalized Gaussian span with model half filling.
Coordinates/exponents and density units are consistent. It is a density of
that chosen finite fermion model, not real protein valence charge, DFT,
ab-initio many-electron chemistry or measured electron-transfer dynamics.
Finite64-cubed grids,8bit square-root encoding and display interpolation are
separate approximations with integrated/decoded charge diagnostics.

## Fresh local evidence and received receipts

`check_holomorphic_clouds.py` tests actual four-term bounds with noisy circle
samples/GD, source-condition rates, direct theta-tail quadrature, independent
kinetic Hermite/Coulomb Laplace integrals and the initial Lowdin state.
`holomorphic-cloud-review.json` records all checks passing. Integral discrepancy
is `8.89e-16`, overlap error `2.71e-15` and initial local-Gaussian discrepancy
`8.89e-16`. These are ordinary diagnostic calculations, not interval proofs.

The received `cloud-physics.json` independently checks all nuclear integrals,
coherent state normalization and file hashes. H2+ voxel charge is
`1..1.0000001504`; Trp model charge is10 to floating precision. Maximum decoded
charge errors are about `.00158` and `.00140`, respectively. These do not turn
the displayed protein model into a calibrated electronic-structure result.
No new Lean, unconditional GRH, quantum advantage or all-conductor uniform
theorem is asserted by the reviewed work.

## Integration follow-up

The root agent subsequently added explicit `n0>=1` and `delta>0` and the
HLNTK/HLDirichlet/HLFredholm bibliography entries. These were independently
confirmed during the games/hubs review. All previously requested mathematical
parameter and citation-integration fixes are resolved; no new validated-oracle
or full-GRH claim has been introduced.
