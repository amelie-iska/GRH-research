# Analytic verification with pinned mathlib

This separate layer uses actual complex numbers, exponential Euler weights, differentiability on a domain and continuity on its closure, the maximum-modulus principle, pointwise filter limits, and uniform boundary convergence. It is distinct from the standalone finite-arithmetic layer.

Run `sh scripts/check_analytic.sh` from the project root. The script verifies the exact mathlib commit and manifest before checking the source with warnings treated as errors. All six declarations print their axioms. Their only dependencies reported at that level are the standard Lean foundations `propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx` or project-specific axiom is used.

## Checked theorems

- `norm_eulerWeight_lt_one`: for real p>1 and complex s with positive real part, the norm of exp(−s log p) is less than one.
- `euler_factor_ne_zero`: a coefficient of norm at most one cannot make1−a exp(−s log p) vanish there.
- `finite_euler_product_ne_zero`: the corresponding finite product is nonzero. The indices need not even be prime; the stated p>1 hypotheses suffice.
- `boundary_lower_bound`: a zero-free complex differentiable function on a bounded domain, continuous and nonzero on its closure, inherits a positive boundary norm bound throughout its closure. This is proved by applying maximum modulus to its reciprocal.
- `limit_ne_zero_of_boundary_lower_bound`: an eventual positive boundary margin for a sequence of such functions prevents its pointwise interior limit from vanishing.
- `boundary_uniform_limit_ne_zero`: uniform convergence on the boundary to a function bounded away from zero, plus convergence at an interior/closure point, rules out a zero there. The boundary and convergence hypotheses are explicit and not presumed for any L-function.

This is a genuine local analytic component of the no-go argument, not a formal proof of full Hurwitz, the whole papers, arithmetic partial-sum convergence, or GRH. Finding an isolated zero and its compact boundary margin is still done in prose. There is no self-adjoint arithmetic determinant in this layer.

## Reproduce dependencies

Lean4.24.0 is the same project-local toolchain as the standalone layer. Mathlib is cloned under ignored `.tools/mathlib4-v4.24.0` at tagv4.24.0 and exact commit recorded in DEPENDENCIES.json. Its package revisions are in mathlib-manifest.json. No supplied repository was modified and no global Lean configuration was changed.

For a fresh machine, obtain the official toolchain, clone the pinned mathlib tag into that path, confirm its hash, and from the mathlib directory run:

```sh
lake exe cache get Mathlib.Analysis.Complex.LocallyUniformLimit Mathlib.Analysis.SpecialFunctions.Pow.Complex Mathlib.Analysis.Complex.AbsMax
```

The cache command downloads public build artifacts for those imports and uses mathlib's default cache directory. No existing cache was cleaned or reindexed. All cache/tool artifacts are retained; no cache-clean or dependency-upgrade command is needed. Use the pinned manifest, not `lake update`.
