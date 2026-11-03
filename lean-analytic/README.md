# Analytic verification with pinned mathlib

This separate layer uses actual complex numbers, exponential Euler weights, differentiability on a domain and continuity on its closure, the maximum-modulus principle, pointwise filter limits, and uniform boundary convergence. It is distinct from the standalone finite-arithmetic layer.

Run `sh scripts/check_analytic.sh` from the project root. The script verifies the exact mathlib commit and manifest before checking the source with warnings treated as errors. All 110 declarations print their axioms. Their only dependencies reported at that level are the standard Lean foundations `propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx` or project-specific axiom is used.

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
lake exe cache get Mathlib.Analysis.Complex.LocallyUniformLimit Mathlib.Analysis.SpecialFunctions.Pow.Complex Mathlib.Analysis.Complex.AbsMax Mathlib.Analysis.Complex.OpenMapping Mathlib.Analysis.Complex.ReImTopology Mathlib.LinearAlgebra.Matrix.Hermitian Mathlib.LinearAlgebra.Matrix.PosDef Mathlib.LinearAlgebra.Matrix.ToLinearEquiv Mathlib.Analysis.SpecialFunctions.Log.Summable Mathlib.NumberTheory.JacobiSum.Basic Mathlib.Algebra.QuadraticAlgebra
```

The cache command downloads public build artifacts for those imports and uses mathlib's default cache directory. No existing cache was cleaned or reindexed. All cache/tool artifacts are retained; no cache-clean or dependency-upgrade command is needed. Use the pinned manifest, not `lake update`.

## Jensen metric components

`JensenMetric.lean` adds seven actual finite-product/matrix/algebra statements: a universal product-defect inequality; real eigenvalues of an actual complex matrix with a positive symmetrizing metric; the quadratic companion's Newton-sum symmetrization, determinant and completed-square form; positive definiteness under an explicit discriminant inequality; and the Gaussian-mixture Turan gap identity. The discriminant/metric positivity hypotheses are explicit. These declarations do not assert arithmetic xi metric positivity.

The entire-function error summation, xi coefficients and kernel, Gaussian measure integrals, general Hermite criterion, and the full conditional block-determinant construction remain prose/classical dependencies. `scripts/check_jensen_metric.py` checks specified rational model sequences, including positive, indefinite and repeated-root cases; these are not xi coefficient certificates. See research/jensen-metric.md for exact assumptions and the remaining RH-equivalent obligation.

## Euler correction components

`EulerCorrection.lean` adds eight statements: the exact unramified residual identity; principal specialization, remainder defect and Euler factorization; local nonvanishing by an actual complex norm convexity bound; actual complex infinite-product nonvanishing and norm error with explicit summability assumptions; and shifted zero transport under an explicit factorization and zero input. The last statement does not establish existence of a Hecke zero.

The source's preceding Gauss/reciprocity identity, arithmetic power estimates, ideal counting, multivariable normal convergence and classical infinite-order Hecke completion theory remain prose/external dependencies. In particular the7/12 obstruction is not asserted as a complete Lean theorem. The added mathlib import `Mathlib.Analysis.SpecialFunctions.Log.Summable` uses the same pinned version; its public cache artifacts were added without cleaning existing caches or changing the manifest.

## Principal residue components

`PrincipalResidue.lean` adds six actual complex algebra/finite-sum statements: exact multiplier evaluation when r=d, the two local error identities, weighted slot factorization with the correct sign, transfer of an error bound through nonnegative weights with positive total mass, and a finite-product relative-error bound. The last estimate uses a common error bound at most1; the empty product is included. Each theorem has explicit hypotheses and prints its standard foundational dependencies.

The arithmetic inert-prime identification at s=3/5, fixed-ray prime theorem, prime-power asymptotics, slot admissibility and contour integration remain prose/external inputs. The module does not certify the inherited high representation or the remaining energy/row-count estimates. No new imports, dependencies or cache downloads were needed for this module.

## Frozen row-count components

`FrozenRowCount.lean` adds seven declarations: an actual finite complex moment-to-cardinality inequality, the exact kappa=3/4 plain capacity, real coefficient bounds, crossing bounds on the full parameter rectangle, the exact short-count crossing, balanced cutoff and supply inequality. The coefficient/cutoff statements permit the larger x<=1/2 domain where the formulas still hold; the crossing theorem keeps0<=x<=1/2. All theorem types and standard axiom dependencies are explicit.

These check finite algebra and inequalities, not the arithmetic moment bounds, saturated detector witnesses, selection rounding theorem, floor-bin estimates or global7/8 theorem. The full conditional counting argument and quantifier order remain prose in research/frozen-row-count.md. No imports, pinned dependencies or cache artifacts were added.

## Low-energy components

`LowEnergy.lean` adds seven declarations: the hybrid minimum dichotomy, kernel quarter-range charge, the actual reflected real-exponent inequality with support offsets and retained-range slack, exact rescaling identities, universal scale/Gram margins, subset-loss absorption and an actual real-power bound. The generic exponent theorem uses explicit inequalities for the actual row and dual centers, including nonnegative v and ell_b and a permitted negative unit exponent. It assumes no L-function zero locations.

These results do not establish the arithmetic reflected-energy or Gram estimates, sector/reflection identities, common Fourier-density summability or exact finite low separation. They verify the real inequalities used in their conditional application. The already-present `Mathlib.Analysis.SpecialFunctions.Pow.Real` module cache supplies real powers, at the same pinned mathlib commit; no dependency, manifest, cache download or global environment changed.

## Central contour and integral components

`CentralContour.lean` adds ten declarations: real retained-rectangle geometry, an actual finite cumulative height sum and buffer inclusion, strict and simultaneous real-power conductor credit, exact central normalization/reference/perturbation identities, an actual complex Bochner-integral envelope, and existence of a late real height exponent and natural tail order. The integral theorem explicitly uses integrability of the original function and kernel and an almost-everywhere norm bound. It does not assume measurable pointwise partition labels or integrate unverified pieces.

The module does not formalize the contour deformation, arithmetic conductor identification, scalar/high identity, buffered L-function bounds, trace tails or row moments. Those are explicit inputs to the prose conditional interface. Both real-power and Bochner-integral modules were already cached at the pinned mathlib version; no download or dependency/manifest change occurred.

## Genuine finite-field correlation and Gauss components

`FiniteCorrelation.lean` adds sixteen declarations using actual arbitrary finite fields, complex MulChar/AddChar objects, finite sums and the mathlib Jacobi/Gauss theorems. They cover zero extension of character powers, principal sum, unit norm/diagonal, shifted autocorrelation, solved congruence, both-unit and one-zero local kernels, the both-zero corner and its actual F7 value36, nonprincipality of powers with6 not dividing the exponent, principal Gauss value, conjugation and nonprincipal Gauss norm squared. The symmetric a-zero case follows in prose by variable swap/conjugation. No desired field-correlation formula or analytic cancellation estimate is assumed as a premise.

Prime-power quotient-ring lifting, CRT, the source trace pairing and the identification of the unit-phase ratio with its fixed reciprocity bicharacter remain prose or external arithmetic inputs. Finite tests do not certify Gram or reflected moments. The selective JacobiSum.Basic public cache graph was added at the unchanged mathlib/manifest pins without cleaning or upgrades; logs are retained locally. All sixteen full theorem types and standard axiom dependencies were independently reviewed.

## Gram Fourier and dyadic components

`GramPoisson.lean` adds nine declarations: the norm and trivial mode of an actual normalized finite additive Fourier coefficient; two nonprincipal finite-field independent-coordinate means allowing arbitrary coupling of the other labels; the exact finite dyadic head, actual infinite total and tail; a uniform finite head inequality; and the exact nonexceptional scale cancellation. All statements print standard foundational dependencies and assume no zero locations or arithmetic positivity.

The lattice Poisson formula, annular point count, fixed source reciprocity/ray modulus, ideal counts, smooth seminorms and the full arithmetic Gram/moment theorem are not formalized here. The prose application retains their exact scope in research/gram-poisson.md. The already-cached SpecificLimits.Normed module supplies actual real tsums; no dependency, manifest or toolchain changed and no cache was downloaded. The finite checker is a diagnostic, not a substitute for the universal analytic argument.

## Actual Eisenstein quotient-ring reciprocity phase

`ReciprocityPeriod.lean` adds thirteen declarations in QuadraticAlgebra over ZMod4 and over the integers. The generator satisfies omega²+omega+1=0 with actual Eisenstein multiplication. Theorems verify the twelve odd units, inverse/closure, the square-class map and its square kernel, the complex four-term phase table/refinement, the sign bicharacter/diagonal and the integer period under adding4z in either column. Finite reductions run in the kernel, with no native_decide or project-specific axioms. The increased local heartbeat limit permits the finite phase-table proof; it changes no toolchain setting.

The identification with quadratic Gauss sums, classical cubic reciprocity, Kummer/Artin maps, conductor-discriminant and the exact full source coefficient period are prose/classical arguments in research/reciprocity-period.md, not claimed as full Lean theorems. The source application now has a proved classical common defining modulus; no exact conductor or zero-free region is asserted. The one newly missing QuadraticAlgebra public cache artifact was added at unchanged pins without cleaning prior artifacts or changing a manifest.

## Reflected local characters, phases and common density

`ReflectedIdentity.lean` adds nine declarations. Actual arbitrary-field MulChar objects satisfy the two zero-preserving row/mark column identities under the explicit finite-order hypothesis A^6=1. The principal character remains zero at nonunits. A mask-deletion witness and exact Ramanujan partition retain shared cube primes. Complex-unit integer powers verify the local scalar extraction; actual complex powers verify the general pair phase under the explicit cubic-symbol equality, row-mark cancellation and moving-j4 residue. An actual Bochner integral in a complete complex normed space, with integrability stated, proves extraction of the one common density scalar before the norm.

These statements do not assume GRH or desired arithmetic positivity. They do not establish the global theta automorphy/cusp identification, actual cubic reciprocity or source Fourier representation, gamma/Stirling bounds, or the hybrid mean square. The arithmetic reduction is conditional on the exact source block/representation hypotheses; the kernel-profile proof is prose with named classical gamma inputs. The nine declarations were independently compiled; the complete110-declaration suite was run separately by the primary agent. Existing pinned modules/caches sufficed: no dependency, manifest, toolchain or cache download changed.
