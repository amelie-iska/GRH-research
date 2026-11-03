# Analytic verification with pinned mathlib

This separate layer uses actual complex numbers, exponential Euler weights, differentiability on a domain and continuity on its closure, the maximum-modulus principle, pointwise filter limits, and uniform boundary convergence. It is distinct from the standalone finite-arithmetic layer.

Run `sh scripts/check_analytic.sh` from the project root. The script verifies the exact mathlib commit and manifest before checking the source with warnings treated as errors. All 33 declarations print their axioms. Their only dependencies reported at that level are the standard Lean foundations `propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx` or project-specific axiom is used.

## Checked theorems

- `norm_eulerWeight_lt_one`: for real p>1 and complex s with positive real part, the norm of exp(−s log p) is less than one.
- `euler_factor_ne_zero`: a coefficient of norm at most one cannot make1−a exp(−s log p) vanish there.
- `finite_euler_product_ne_zero`: the corresponding finite product is nonzero. The indices need not even be prime; the stated p>1 hypotheses suffice.
- `boundary_lower_bound`: a zero-free complex differentiable function on a bounded domain, continuous and nonzero on its closure, inherits a positive boundary norm bound throughout its closure. This is proved by applying maximum modulus to its reciprocal.
- `limit_ne_zero_of_boundary_lower_bound`: an eventual positive boundary margin for a sequence of such functions prevents its pointwise interior limit from vanishing.
- `boundary_uniform_limit_ne_zero`: uniform convergence on the boundary to a function bounded away from zero, plus convergence at an interior/closure point, rules out a zero there. The boundary and convergence hypotheses are explicit and not presumed for any L-function.

This is a genuine local analytic component of the no-go argument, not a formal proof of full Hurwitz, the whole papers, arithmetic partial-sum convergence, or GRH. Finding an isolated zero and its compact boundary margin is still done in prose. There is no self-adjoint arithmetic determinant in this layer.

## Holomorphic Hermitian rigidity

`HermitianRigidity.lean` adds three kernel-checked declarations: `real_valued_holomorphic_constant`, `conjugate_holomorphic_pair_constant`, and `holomorphic_hermitian_family_constant`. They use actual complex differentiability on a connected open domain and `Matrix.IsHermitian`. The last theorem is entrywise and even permits an arbitrary index type; the paper uses finite matrices with a fixed inner product. It does not apply to families Hermitian only for real parameter values, or prove any arithmetic determinant identity.

## Positive generalized spectral pencils

`PositivePencil.lean` adds seven actual complex/matrix declarations: `real_ratio_from_positive_form`, `positive_pencil_eigenvalue_real`, `positive_pencil_det_zero_real`, `positive_pencil_det_ne_zero`, `centered_positive_pencil_zero_on_line`, `det_ne_zero_of_strict_imaginary_form`, and `indefinite_pencil_off_line_witness`. The matrix theorems use fixed `Matrix.IsHermitian` A and actual `Matrix.PosDef` B, including the required `ComplexOrder` scope. Singularity is converted into a nonzero kernel vector; quadratic-form reality/strict positivity gives a real generalized eigenvalue and the centered critical-line conclusion. The last theorem checks the explicit off-line determinant witness at s=1/4 when B is indefinite; Hermitian-entry facts for that transparent example are discussed in prose.

This verifies a genuine sufficient spectral mechanism and its positivity caveat. It does not construct arithmetic A_N,B_N, prove determinant matching/convergence, or formalize the operator-norm inverse estimate. The strict-imaginary-form theorem is pointwise and imposes the displayed nontrivial positivity hypothesis; it does not assume or verify that any L-function satisfies it.

## Arithmetic zero certificate: formal scope

`ArithmeticZeroDisk.lean` verifies `arithmetic_zero_disk_in_left_strip` using actual complex distance and `arithmetic_zero_certificate_margin` using exact real rational arithmetic. These are the geometry and final margin of the separate certificate for S5(s,chi_mod3). The exact logarithm/exponential enclosure computations are performed by Python Fraction arithmetic and their analytic error estimates/Rouche inference are prose proofs. Neither declaration asserts a kernel-checked zero of the full L-function, a full Lean zero-existence certificate, or a counterexample to GRH.

## Reproduce dependencies

Lean4.24.0 is the same project-local toolchain as the standalone layer. Mathlib is cloned under ignored `.tools/mathlib4-v4.24.0` at tagv4.24.0 and exact commit recorded in DEPENDENCIES.json. Its package revisions are in mathlib-manifest.json. No supplied repository was modified and no global Lean configuration was changed.

For a fresh machine, obtain the official toolchain, clone the pinned mathlib tag into that path, confirm its hash, and from the mathlib directory run:

```sh
lake exe cache get Mathlib.Analysis.Complex.LocallyUniformLimit Mathlib.Analysis.SpecialFunctions.Pow.Complex Mathlib.Analysis.Complex.AbsMax Mathlib.Analysis.Complex.OpenMapping Mathlib.Analysis.Complex.ReImTopology Mathlib.LinearAlgebra.Matrix.Hermitian Mathlib.LinearAlgebra.Matrix.PosDef Mathlib.LinearAlgebra.Matrix.ToLinearEquiv Mathlib.Analysis.SpecialFunctions.Log.Summable
```

The cache command downloads public build artifacts for those imports and uses mathlib's default cache directory. No existing cache was cleaned or reindexed. All cache/tool artifacts are retained; no cache-clean or dependency-upgrade command is needed. Use the pinned manifest, not `lake update`.

## Jensen metric components

`JensenMetric.lean` adds seven actual finite-product/matrix/algebra statements: a universal product-defect inequality; real eigenvalues of an actual complex matrix with a positive symmetrizing metric; the quadratic companion's Newton-sum symmetrization, determinant and completed-square form; positive definiteness under an explicit discriminant inequality; and the Gaussian-mixture Turan gap identity. The discriminant/metric positivity hypotheses are explicit. These declarations do not assert arithmetic xi metric positivity.

The entire-function error summation, xi coefficients and kernel, Gaussian measure integrals, general Hermite criterion, and the full conditional block-determinant construction remain prose/classical dependencies. `scripts/check_jensen_metric.py` checks specified rational model sequences, including positive, indefinite and repeated-root cases; these are not xi coefficient certificates. See research/jensen-metric.md for exact assumptions and the remaining RH-equivalent obligation.

## Euler correction components

`EulerCorrection.lean` adds eight statements: the exact unramified residual identity; principal specialization, remainder defect and Euler factorization; local nonvanishing by an actual complex norm convexity bound; actual complex infinite-product nonvanishing and norm error with explicit summability assumptions; and shifted zero transport under an explicit factorization and zero input. The last statement does not establish existence of a Hecke zero.

The source's preceding Gauss/reciprocity identity, arithmetic power estimates, ideal counting, multivariable normal convergence and classical infinite-order Hecke completion theory remain prose/external dependencies. In particular the7/12 obstruction is not asserted as a complete Lean theorem. The added mathlib import `Mathlib.Analysis.SpecialFunctions.Log.Summable` uses the same pinned version; its public cache artifacts were added without cleaning existing caches or changing the manifest.
