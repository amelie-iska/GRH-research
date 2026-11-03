# Analytic verification with pinned mathlib

This separate layer uses actual complex numbers, exponential Euler weights, differentiability on a domain and continuity on its closure, the maximum-modulus principle, pointwise filter limits, and uniform boundary convergence. It is distinct from the standalone finite-arithmetic layer.

Run `sh scripts/check_analytic.sh` from the project root. The script verifies the exact mathlib commit and manifest before checking the source with warnings treated as errors. All 203 declarations print their axioms. Their only dependencies reported at that level are the standard Lean foundations `propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx` or project-specific axiom is used.

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


## Projective resolutions and arrow-state determinants

`DualNumberResolution.lean` adds thirteen declarations over the actual nonsemisimple algebra `QuadraticAlgebra k 0 0`, for arbitrary fields. The regular algebra module is explicit; the residue action is pulled back through the actual augmentation ring homomorphism. Theorems prove epsilon nonzero/square-zero, boundary coordinates, all-degree square-zero and kernel=image, surjective linear augmentation with kernel=image, projectivity of every regular term, zero induced Hom differentials, and a nonzero augmentation functional. This is an actual infinite resolution's exactness/projectivity data, not a toy recurrence. A categorical projective-resolution object, derived Ext identification and abstract infinite-projective-dimension theorem are not yet implemented.

`ResolutionDeterminant.lean` adds three declarations. `arrow_state_determinant` proves the universal cleared rectangular determinant identity over any commutative ring, with the right-inverse and composable-pair splitting explicitly assumed. It does not assume the determinant conclusion or any spectral fact. `acyclic_pair_determinant` proves conjugacy cancellation under an explicit inverse identity; this is a component of, not the entire cohomological cancellation theorem. `alternating_duality_without_purity` proves an actual rational2×2 symplectic-similitude counterexample. The full forbidden-chain resolution, partial-permutation cycle factorization, surface equivalences, Grothendieck trace formula, Deligne purity and arithmetic GRH comparison remain prose/external/open as indicated in the new papers.

At the projective-resolution milestone all 126 analytic declarations were checked by the existing pinned suite, each printing standard foundation dependencies. The selective public SchurComplement/Projective cache was added at unchanged toolchain, HEAD and manifest; no production dependency, cleanup or upgrade occurred. Sixteen new theorem types and axiom reports are in outputs/checks/2026-11-03-projective. Prior upstream3125-module Lean4.34.1 verification remains unrun and distinct.


## Finite Hodge cancellation and relative boundary algebra

`HodgeDeterminant.lean` adds eleven declarations: actual odd block-Dirac squaring; positivity of both Gram partners; nonzero scalar-shift factorization; equality of normalized Gram determinants; a cleared shifted equality assuming nonzero mass; the normalized parity quotient where its denominator is nonzero; positive scalar metrics on a fixed one-dimensional complex; the weighted-adjoint identity; the ordinary metric-dependent characteristic determinant and explicit moving-zero witness; and a relative boundary-product identity in an arbitrary noncommutative unital ring, with inverse/commutation hypotheses explicit. All types and standard foundation dependencies are printed. At that milestone the complete analytic suite had137 declarations.

The full finite-complex/cohomology interpretation, polynomial extension of the shifted equality to mass0, ℓ² shift, finite-rank Fredholm determinant, infinite relative boundary realization and trace-norm/strong-limit proofs remain prose in research/hodge-boundary-determinants.md and the focused preprints. No bounded Hilbert operator or Fredholm determinant is claimed constructed in Lean from the abstract ring identity. No arithmetic determinant or desired positivity is assumed. Existing pinned modules/caches sufficed; no dependency, cache download, manifest or toolchain changed.


## Arithmetic Abel boundary components

`AbelBoundary.lean` adds ten declarations: exact finite Abel summation with its endpoint term; universal finite rank-one determinant; an actual HasSum for the infinite squared geometric majorant; genuine continuous rank-one operators, their square/range evaluation and exact operator-norm difference on arbitrary complex inner-product spaces; necessary functional form, nonzero boundary value and pairwise proportionality for symmetric fixed-range rank-one maps; and the exact real Abel-kernel minor −1/288. All full types and standard foundation dependencies are printed. The complete suite147 passes warnings-as-errors at unchanged pins.

The particular dyadic arithmetic vectors u/v are constructed on ℓ² in prose; their Banach/trace-norm holomorphy, trace-class norm and Fredholm identity, explicit dyadic tails, completed/raw arithmetic comparison and critical-height subsequence obstruction are not claimed fully formalized. The formal symmetry hypotheses are actual universal operator properties used to derive a necessary condition, not assumed arithmetic positivity or a GRH-equivalent axiom. Exact finite character/determinant/tail diagnostics supplement the proofs. No dependency, cache, manifest, toolchain, infrastructure or MCP activation changed.


## Actual completed dessin order and Schur components (2026-11-03)

`DessinNodeOrder.lean` defines the node as the actual equal-constant subring of two `PowerSeries k` rings. Twenty declarations prove diagonal injectivity, nonzero x/y branches and zero products, branch factorization, ann(x)=(y) and ann(y)=(x), regular u=x+y, its diagonal-X identity, augmentation surjectivity/exactness, bijective common-DVR coordinates, square-zero alternating boundary maps, the three kernel=range statements and projectivity of the actual regular/product terms. These are universal all-degree components of the nodal residue resolution, not a finite dual-number replacement. The coordinate map is a bijection; an R-linear equivalence/general order freeness declaration has not yet been packaged.

`DessinInvariantComponents.lean` adds ten declarations. Three actual ring identities prove ordinary CK1 plus closed forbidden successors kills arrows and covered vertices. The determinant statement verifies the cleared basis-change weight. The explicit 3-by-3 symmetric-square matrix of a 2-by-2 endomorphism preserves zero, identity and composition universally over a commutative ring, hence preserves monomial zero relations. The remaining statements are the degree-two Schur character identity and the actual mixed-vector failure of the node's fixed central parameter on Sym². No general Young/Schur-Weyl/LR theorem is claimed formalized.

The full 177-declaration suite passed warnings-as-errors at unchanged Lean4.24/mathlib pins; types and dependencies are in outputs/checks/2026-11-03-dessins/analytic-verification.log. Only standard foundations occur. General dessins, abstract Ext/Tor and AR, all derived/curve equivalences, operator C* extensions and K-theory, Fredholm determinants and arithmetic descent remain prose or external-theorem dependencies. No GRH-equivalent positivity is introduced as a purported unconditional theorem.


## Graph residue and pullback algebra components (2026-11-03)

`DessinPullbackComponents.lean` adds ten declarations, using literal matrix units over a commutative ring: forward/reverse products, orthogonality, square and sum; raw diagonal extraction fails multiplicativity; no unital map from the two-state full matrix algebra to a nonzero commutative ring; the corrected diagonal fiber is multiplicative. An actual equal-image subring of a product of arbitrary rings has a surjective second projection under its explicit compatible-section hypothesis and the stated zero-fiber identity.

These are universal algebraic components. The continuous circle C* subalgebras, graph gauge uniqueness, functional calculus and uniform generation, K-theory and the full formal-completion obstruction are proved in prose or use named external theorems. The full187-declaration suite prints every type and standard-foundation dependency, with no project assumptions or admissions. The standalone layer is unchanged and its previous7-declaration result is preserved; this extension does not claim a fresh upstream4.34.1 build or a formal GRH proof.


## Arithmetic theta Jacobi and cellular components (2026-11-03)

`ThetaJacobi.lean` adds16printed declarations. Genuine finite-field MulChar Jacobi sums satisfy conjugation, squared norm=cardinality with three explicit nontrivialities, and shifted rescaling. Cubic/quadratic powers force the required noncancellation. Actual2×2CM matrices have the proved determinant/local polynomial/Gram similitude and positive real quadratic form, plus the exact post-character prime7matrix polynomials. Actual theta boundary2×3/inclusion3×2 matrices satisfy dB=0, homology restriction, the3-edge determinant polynomial and the rational vertex/edge chain equation. Full203analytic declarations pass warnings-as-errors at unchanged pins, standard foundations only.

The file does not choose cubic/quadratic characters, prove the elliptic cube/square fiber count, define every arithmetic j/λ/π object, formalize Kummer descent, the H0/H2 zeta cancellation or full rational homotopy, identify a canonical integral Frobenius lattice, or construct an order-to-Frobenius functor. These are proved prose deductions or explicitly named external interpretations. No GRH-equivalent positivity is assumed. See outputs/checks/2026-11-03-jacobi/ for full types and evidence.

The final three declarations prove the actual conjugation-matrix identities and the universal real2inert-prime determinant obstruction. They rule out the specified fixed real2cubic-deck carrier with positive Frobenius determinant, not complex/enlarged models. The complex one-qrepair and its extension-power limits remain prose, independently reviewed.
