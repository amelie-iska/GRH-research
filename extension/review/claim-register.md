# Manuscript claim register

This register inventories every theorem, proposition, lemma, corollary, conjecture, and problem environment reachable from the current manuscript main file. It records what evidence is present; it is not a universal proof certificate.

The snapshot contains **264 claim environments** in **31 included TeX files**. **257** have attached local proof environments. 6 general results are explicitly cited external theorems. 5 local arguments are classified as conditional transfer or deduction criteria because their additional inputs are not established by those claims.

A separate list classifies 9 major external statements from the new fluid chapters, including the released continuum theorem and the kinetic-limit and quantum-algorithm literature. These prose records are not added to the number of locally proved environments.

The 115 verified Lean declarations are governed by their successful verification manifests and raw logs. This register maps 68 declarations to exact components of 25 manuscript claims. **No complete composite environment is marked as fully formalized.** A partial map is never counted as a Lean proof of the entire proposition.

## Meaning of the status labels

- **Local argument present:** the manuscript supplies an attached proof. This label does not certify every inference or reprove all background results.
- **Conditional local argument:** the implication is argued, but the specified quantitative, convergence, or duality inputs are assumptions.
- **External cited:** the general theorem is attributed to the listed primary reference and is not proved in full here.
- **Conjectural / proposed open problem:** reserved for such environments; they are not counted as proved. Additional research directions in prose are listed separately below.

All statements inherit notation and hypotheses from their chapters. The JSON retains their exact statement text, labels, proof-source metadata, source hashes, and the precise types for the manually matched formal components.

A separate mathematical reading, with per-claim findings and its own reviewed source snapshots, is recorded in second-pass-math-audit.json/md. Generating this inventory does not itself conduct that proof review.

## Complete environment inventory

| ID | Source | Environment and name | Evidence | Formal mapping |
|---|---|---|---|---|
| foundations.001 | foundations.tex | proposition: Normalization and conductor of the nodal order | Local argument | Not mapped |
| foundations.002 | foundations.tex | proposition: Positive pencils have real generalized eigenvalues | Local argument | Not mapped |
| foundations.003 | foundations.tex | proposition: A precise conditional zero-location transfer | Conditional local argument | Not mapped |
| orders.001 | orders.tex | proposition: Common denominators | Local argument | Not mapped |
| orders.002 | orders.tex | proposition: A stable integral model | Local argument | Not mapped |
| orders.003 | orders.tex | proposition: Endomorphisms of a full lattice | Local argument | Not mapped |
| orders.004 | orders.tex | proposition: Multiplier orders | Local argument | Not mapped |
| orders.005 | orders.tex | lemma: A local membership test | Local argument | Not mapped |
| orders.006 | orders.tex | proposition: Equality from localized inclusions | Local argument | Not mapped |
| orders.007 | orders.tex | lemma: Linearity over an overorder | Local argument | Not mapped |
| orders.008 | orders.tex | theorem: Matrix Morita equivalence | Local argument | Not mapped |
| orders.009 | orders.tex | proposition: Trace duality | Local argument | Not mapped |
| orders.010 | orders.tex | proposition: Change of lattice and discriminant | Local argument | Not mapped |
| orders.011 | orders.tex | proposition: When a transport controls minima | Conditional local argument | Not mapped |
| orders.012 | orders.tex | proposition: Multiplicativity of the quaternion norm | Local argument | Not mapped |
| orders.013 | orders.tex | proposition: Bounding all overorders | Local argument | Not mapped |
| orders.014 | orders.tex | proposition: An integral averaging lift | Local argument | Not mapped |
| orders.015 | orders.tex | proposition: Homomorphisms of complex tori | Local argument | Not mapped |
| orders.016 | orders.tex | theorem: The elementary complex-multiplication dichotomy | Local argument | Not mapped |
| orders.017 | orders.tex | theorem: Quadratic conductor classification | Local argument | Not mapped |
| orders.018 | orders.tex | proposition: The ideal-class torsor | Local argument | Not mapped |
| orders.019 | orders.tex | proposition: The Frobenius order | Local argument | Not mapped |
| orders.020 | orders.tex | lemma: Faithfulness on prime-to-characteristic torsion | Local argument | Not mapped |
| orders.021 | orders.tex | lemma: Endomorphisms of a right ideal lattice | Local argument | Not mapped |
| orders.022 | orders.tex | proposition: Degree multiplicativity from duality | Conditional local argument | Not mapped |
| orders.023 | orders.tex | proposition: Centralizer of the quarter-turn | Local argument | Not mapped |
| orders.024 | orders.tex | proposition: Trace dual of the Gaussian suborder | Local argument | Not mapped |
| complexes.001 | complexes.tex | proposition: Extension closure of lattices | Local argument | Not mapped |
| complexes.002 | complexes.tex | proposition: Universal property | Local argument | Not mapped |
| complexes.003 | complexes.tex | proposition: Equality in a split group | Local argument | Not mapped |
| complexes.004 | complexes.tex | theorem: Algebraic Euler identity | Local argument | Not mapped |
| complexes.005 | complexes.tex | proposition: Bounded acyclic projective complexes | Local argument | Not mapped |
| complexes.006 | complexes.tex | theorem: Schanuel's lemma | Local argument | Not mapped |
| complexes.007 | complexes.tex | proposition: A one-step lattice presentation | Local argument | Not mapped |
| complexes.008 | complexes.tex | proposition: Embedding a lattice into a free module | Local argument | Not mapped |
| complexes.009 | complexes.tex | corollary: Untitled corollary | Local argument | Not mapped |
| complexes.010 | complexes.tex | proposition: Weighted Gram kernel and rank | Local argument | Not mapped |
| complexes.011 | complexes.tex | proposition: Rank constraint and cohomology | Local argument | Partial components: ResearchBridge.complex_rank_bound, ResearchBridge.middle_exact_iff_rank_sum |
| complexes.012 | complexes.tex | corollary: Euler characteristic | Local argument | Partial components: ResearchBridge.euler_rank_identity |
| complexes.013 | complexes.tex | theorem: Normal form over a field | Local argument | Not mapped |
| complexes.014 | complexes.tex | theorem: Dimension formula | Local argument | Not mapped |
| complexes.015 | complexes.tex | proposition: Tangent-space dimension | Local argument | Not mapped |
| complexes.016 | complexes.tex | corollary: Transverse infinitesimal directions | Local argument | Not mapped |
| complexes.017 | complexes.tex | proposition: The singularity of the four-coordinate model | Local argument | Not mapped |
| complexes.018 | complexes.tex | proposition: Endomorphism differential | Local argument | Not mapped |
| complexes.019 | complexes.tex | proposition: Second-order obstruction | Local argument | Not mapped |
| complexes.020 | complexes.tex | lemma: Splitting off a unit pivot | Local argument | Not mapped |
| complexes.021 | complexes.tex | theorem: Buchsbaum--Eisenbud criterion; external theorem | External cited theorem | Not mapped |
| complexes.022 | complexes.tex | theorem: Regular two-generator Koszul complex | Local argument | Not mapped |
| complexes.023 | complexes.tex | proposition: Flat base change | Local argument | Not mapped |
| complexes.024 | complexes.tex | lemma: Wedge--contraction identity | Local argument | Not mapped |
| complexes.025 | complexes.tex | theorem: Exactness of the nonzero-covector Koszul complex | Local argument | Partial components: DiagramGrammar.homotopy_implies_exact |
| complexes.026 | complexes.tex | theorem: Finite-dimensional Hodge decomposition | Local argument | Not mapped |
| complexes.027 | complexes.tex | theorem: Atiyah--Singer index theorem; external theorem | External cited theorem | Not mapped |
| complexes.028 | complexes.tex | proposition: Curvature identity | Local argument | Not mapped |
| complexes.029 | complexes.tex | proposition: Complex identity at an ASD connection | Local argument | Not mapped |
| complexes.030 | complexes.tex | proposition: Ellipticity of the ASD complex | Local argument | Not mapped |
| standard-monomials.001 | standard-monomials.tex | proposition: The exterior basis | Local argument | Not mapped |
| standard-monomials.002 | standard-monomials.tex | proposition: Cauchy--Binet with specified indices | Local argument | Not mapped |
| standard-monomials.003 | standard-monomials.tex | proposition: Shuffle identities over a ring | Local argument | Not mapped |
| standard-monomials.004 | standard-monomials.tex | lemma: Contraction and a contracting homotopy | Local argument | Partial components: DiagramGrammar.homotopy_implies_exact |
| standard-monomials.005 | standard-monomials.tex | theorem: External general Schur basis theorem | External cited theorem | Not mapped |
| standard-monomials.006 | standard-monomials.tex | proposition: Three elementary Schur cases | Local argument | Not mapped |
| standard-monomials.007 | standard-monomials.tex | proposition: A characteristic-zero Schur complex | Local argument | Not mapped |
| standard-monomials.008 | standard-monomials.tex | theorem: Rank-one straightening, with full proof | Local argument | Not mapped |
| standard-monomials.009 | standard-monomials.tex | lemma: The elementary Plucker shuffle | Local argument | Not mapped |
| standard-monomials.010 | standard-monomials.tex | theorem: The two-row standard monomial basis | Local argument | Not mapped |
| standard-monomials.011 | standard-monomials.tex | proposition: Geometry and basis of the basic complex | Local argument | Not mapped |
| standard-monomials.012 | standard-monomials.tex | proposition: The bihomogeneous Schur calculation | Local argument | Not mapped |
| standard-monomials.013 | standard-monomials.tex | theorem: External standard basis theorem for complexes | External cited theorem | Not mapped |
| standard-monomials.014 | standard-monomials.tex | proposition: Orbits, closure, and dimension | Local argument | Not mapped |
| standard-monomials.015 | standard-monomials.tex | theorem: External Schur filtration and its characteristic-zero splitting | External cited theorem | Not mapped |
| standard-monomials.016 | standard-monomials.tex | proposition: An explicit straightening degeneration | Local argument | Not mapped |
| standard-monomials.017 | standard-monomials.tex | proposition: The two-row minors are a SAGBI basis | Local argument | Not mapped |
| standard-monomials.018 | standard-monomials.tex | theorem: The diagonal semigroup and its inequalities | Local argument | Not mapped |
| standard-monomials.019 | standard-monomials.tex | proposition: Normality from these integral inequalities | Local argument | Not mapped |
| standard-monomials.020 | standard-monomials.tex | proposition: Flatness and different special fibers | Local argument | Not mapped |
| gentle-invariants.001 | gentle-invariants.tex | proposition: Complete module decomposition for the two-arrow relation | Local argument | Not mapped |
| gentle-invariants.002 | gentle-invariants.tex | proposition: Untitled proposition | Local argument | Not mapped |
| gentle-invariants.003 | gentle-invariants.tex | proposition: The elementary extension complex | Local argument | Not mapped |
| gentle-invariants.004 | gentle-invariants.tex | proposition: The two-factor character test | Local argument | Not mapped |
| gentle-invariants.005 | gentle-invariants.tex | theorem: Corrected explicit presentation | Local argument | Not mapped |
| gentle-invariants.006 | gentle-invariants.tex | theorem: Exterior determinant identity | Local argument | Not mapped |
| gentle-invariants.007 | gentle-invariants.tex | proposition: Cancellation through cohomology | Local argument | Not mapped |
| cryptography.001 | cryptography.tex | proposition: Kernel and cosets | Local argument | Not mapped |
| cryptography.002 | cryptography.tex | lemma: Character cancellation | Local argument | Not mapped |
| cryptography.003 | cryptography.tex | theorem: Exact annihilator distribution | Local argument | Not mapped |
| cryptography.004 | cryptography.tex | proposition: Relation lattice and covolume | Local argument | Not mapped |
| cryptography.005 | cryptography.tex | proposition: Dual-basis formula | Local argument | Not mapped |
| cryptography.006 | cryptography.tex | proposition: Unimodular changes can have unbounded metric distortion | Local argument | Partial components: ResearchBridge.shear_determinant_one, ResearchBridge.shear_inverse, ResearchBridge.shear_e2_image, ResearchBridge.shear_e2_norm_squared |
| cryptography.007 | cryptography.tex | proposition: Noise cancellation identity | Local argument | Not mapped |
| cryptography.008 | cryptography.tex | proposition: A deterministic bound on the toy error | Local argument | Not mapped |
| cryptography.009 | cryptography.tex | proposition: Product decomposition of a noisy module equation | Local argument | Not mapped |
| quantum-surfaces.001 | quantum-surfaces.tex | proposition: Genus from permutation cycles | Local argument | Not mapped |
| quantum-surfaces.002 | quantum-surfaces.tex | proposition: A clean degree-four elliptic dessin | Local argument | Not mapped |
| quantum-surfaces.003 | quantum-surfaces.tex | theorem: Commutation from the chain identity | Local argument | Not mapped |
| quantum-surfaces.004 | quantum-surfaces.tex | theorem: Logical qubits on a closed oriented surface | Local argument | Partial components: ResearchQuantum.euler_surface_rank_substitution |
| quantum-surfaces.005 | quantum-surfaces.tex | proposition: Distance of the rectangular torus code | Local argument | Not mapped |
| quantum-surfaces.006 | quantum-surfaces.tex | proposition: Stabilizers and logical sector of the prepared state | Local argument | Not mapped |
| quantum-surfaces.007 | quantum-surfaces.tex | theorem: Correctness of the encoder | Local argument | Not mapped |
| quantum-surfaces.008 | quantum-surfaces.tex | proposition: Gap in the specified projector normalization | Local argument | Not mapped |
| quantum-surfaces.009 | quantum-surfaces.tex | theorem: Exact output of the variational correlator | Local argument | Not mapped |
| tensor-grammars.001 | tensor-grammars.tex | proposition: Elementary diagram semantics | Local argument | Not mapped |
| tensor-grammars.002 | tensor-grammars.tex | proposition: Snake identity and the closed loop | Local argument | Not mapped |
| tensor-grammars.003 | tensor-grammars.tex | proposition: Alternating projector and its rank | Local argument | Not mapped |
| tensor-grammars.004 | tensor-grammars.tex | proposition: Exterior functoriality and Cauchy--Binet | Local argument | Not mapped |
| tensor-grammars.005 | tensor-grammars.tex | proposition: Fundamental completeness and Casimir | Local argument | Not mapped |
| tensor-grammars.006 | tensor-grammars.tex | theorem: Finite Choi--Kraus criterion | Local argument | Not mapped |
| tensor-grammars.007 | tensor-grammars.tex | theorem: Typed rewrite soundness | Local argument | Partial components: DiagramGrammar.context_sound, DiagramGrammar.derivation_sound, DiagramGrammar.equiv_derivation_sound |
| tensor-grammars.008 | tensor-grammars.tex | proposition: Termination and accumulated approximation error | Local argument | Not mapped |
| tensor-grammars.009 | tensor-grammars.tex | proposition: Transport of a complex and its metric | Local argument | Partial components: DiagramGrammar.complex_transport, DiagramGrammar.matrix_hodge_conjugacy |
| tensor-grammars.010 | tensor-grammars.tex | proposition: A controlled enlargement | Local argument | Not mapped |
| tensor-grammars.011 | tensor-grammars.tex | proposition: Bounded interfaces give bounded treewidth | Local argument | Not mapped |
| tensor-grammars.012 | tensor-grammars.tex | proposition: Context-free graph generation can have a non-context-free string yield | Local argument | Not mapped |
| tensor-grammars.013 | tensor-grammars.tex | proposition: Unrestricted effective graph rewriting can express Type-0 recognition | Local argument | Not mapped |
| tensor-grammars.014 | tensor-grammars.tex | proposition: Dynamic contraction along a derivation tree | Local argument | Not mapped |
| quantum-toricgt.001 | quantum-toricgt.tex | proposition: Bellman recursion on a finite token DAG | Local argument | Not mapped |
| quantum-toricgt.002 | quantum-toricgt.tex | proposition: A checkable primal--dual certificate | Local argument | Not mapped |
| quantum-toricgt.003 | quantum-toricgt.tex | lemma: Integral unit flows on an ordered DAG | Local argument | Not mapped |
| quantum-toricgt.004 | quantum-toricgt.tex | proposition: An exact lower bound from a rational LP dual | Local argument | Not mapped |
| quantum-toricgt.005 | quantum-toricgt.tex | proposition: Finite Weyl relations and matrix basis | Local argument | Not mapped |
| quantum-toricgt.006 | quantum-toricgt.tex | lemma: Normalization and feature bounds | Local argument | Not mapped |
| quantum-toricgt.007 | quantum-toricgt.tex | proposition: Single-occurrence Pauli parameter shift | Local argument | Not mapped |
| quantum-toricgt.008 | quantum-toricgt.tex | proposition: Hybrid gradient with shared parameters | Local argument | Not mapped |
| quantum-toricgt.009 | quantum-toricgt.tex | lemma: Associativity of finite max-plus contraction | Local argument | Not mapped |
| quantum-toricgt.010 | quantum-toricgt.tex | proposition: Equivariance of the implemented mathematical architecture | Local argument | Not mapped |
| quantum-toricgt.011 | quantum-toricgt.tex | proposition: The binomial kernel of the boundary code | Local argument | Not mapped |
| quantum-toricgt.012 | quantum-toricgt.tex | proposition: A constrained rewrite preserves legal tokenization | Local argument | Not mapped |
| quantum-toricgt.013 | quantum-toricgt.tex | proposition: Preserving a finite affine sign pattern | Local argument | Not mapped |
| quantum-toricgt.014 | quantum-toricgt.tex | lemma: A conservative circuit-offset perturbation bound | Local argument | Not mapped |
| quantum-toricgt.015 | quantum-toricgt.tex | proposition: The parity semigroup is normal in its own group | Local argument | Not mapped |
| quantum-toricgt.016 | quantum-toricgt.tex | proposition: A point, a circle, and a filled triangle | Local argument | Not mapped |
| quantum-toricgt.017 | quantum-toricgt.tex | proposition: A constraint-preserving variational interface | Local argument | Not mapped |
| gauge-theory.001 | gauge-theory.tex | proposition: Curvature is the failure of the complex identity | Local argument | Not mapped |
| gauge-theory.002 | gauge-theory.tex | proposition: First and second variations | Local argument | Not mapped |
| gauge-theory.003 | gauge-theory.tex | proposition: Energy bound and classical minimizers | Local argument | Not mapped |
| gauge-theory.004 | gauge-theory.tex | theorem: Exactness of the anti-self-dual symbol sequence | Local argument | Not mapped |
| gauge-theory.005 | gauge-theory.tex | theorem: Atiyah--Hitchin--Singer index formula, external | External cited theorem | Not mapped |
| gauge-theory.006 | gauge-theory.tex | proposition: Exactness does not control the smallest singular value | Local argument | Not mapped |
| gauge-theory.007 | gauge-theory.tex | proposition: Finite-volume normalization and gauge invariance | Local argument | Not mapped |
| gauge-theory.008 | gauge-theory.tex | proposition: Positive-type Wilson link weight | Local argument | Not mapped |
| gauge-theory.009 | gauge-theory.tex | proposition: Null vectors and positive quotient | Local argument | Not mapped |
| gauge-theory.010 | gauge-theory.tex | theorem: Spectral gap and Euclidean-time decay | Local argument | Not mapped |
| gauge-theory.011 | gauge-theory.tex | proposition: Identical leading ultraviolet behavior, different gaps | Local argument | Not mapped |
| gauge-theory.012 | gauge-theory.tex | proposition: Passage of a uniform gap bound | Conditional local argument | Not mapped |
| gauge-theory.013 | gauge-theory.tex | proposition: A contractive recurrence with controlled errors | Local argument | Not mapped |
| gauge-theory.014 | gauge-theory.tex | proposition: Order action and dual action | Local argument | Not mapped |
| character-bridge.001 | character-bridge.tex | proposition: Universal exactness and the exceptional fiber | Local argument | Not mapped |
| character-bridge.002 | character-bridge.tex | proposition: Finite Laplacians and a quantitative homotopy | Local argument | Not mapped |
| character-bridge.003 | character-bridge.tex | theorem: A character pullback bridge | Local argument | Not mapped |
| microscopic-fluid-limits.001 | microscopic-fluid-limits.tex | proposition: Finite-dimensional informational completeness | Local argument | Not mapped |
| microscopic-fluid-limits.002 | microscopic-fluid-limits.tex | proposition: Local operations do not transmit a signal through a marginal | Local argument | Not mapped |
| microscopic-fluid-limits.003 | microscopic-fluid-limits.tex | proposition: Slater normalization and dimension | Local argument | Not mapped |
| microscopic-fluid-limits.004 | microscopic-fluid-limits.tex | proposition: Exact coupled nuclear equations | Local argument | Not mapped |
| microscopic-fluid-limits.005 | microscopic-fluid-limits.tex | proposition: Energy gradients and the gap denominator | Local argument | Not mapped |
| microscopic-fluid-limits.006 | microscopic-fluid-limits.tex | proposition: Unitary evolution does not supply ground-state relaxation | Local argument | Not mapped |
| microscopic-fluid-limits.007 | microscopic-fluid-limits.tex | proposition: Localization controls the mean-force error | Local argument | Not mapped |
| microscopic-fluid-limits.008 | microscopic-fluid-limits.tex | proposition: Liouville volume and fine-grained entropy | Local argument | Not mapped |
| microscopic-fluid-limits.009 | microscopic-fluid-limits.tex | proposition: Elastic reflection | Local argument | Not mapped |
| microscopic-fluid-limits.010 | microscopic-fluid-limits.tex | proposition: Classification of smooth collision invariants | Local argument | Not mapped |
| microscopic-fluid-limits.011 | microscopic-fluid-limits.tex | proposition: Weak collision identity | Local argument | Not mapped |
| microscopic-fluid-limits.012 | microscopic-fluid-limits.tex | theorem: Classical homogeneous $H$ theorem under explicit regularity | Local argument | Not mapped |
| microscopic-fluid-limits.013 | microscopic-fluid-limits.tex | proposition: Finite energy does not imply finite positive entropy | Local argument | Not mapped |
| microscopic-fluid-limits.014 | microscopic-fluid-limits.tex | proposition: Maxwellian minimizes $H$ at fixed first two moments | Local argument | Not mapped |
| microscopic-fluid-limits.015 | microscopic-fluid-limits.tex | proposition: Moment equations before closure | Local argument | Not mapped |
| microscopic-fluid-limits.016 | microscopic-fluid-limits.tex | proposition: Flux sampling at an equilibrium wall | Local argument | Not mapped |
| microscopic-fluid-limits.017 | microscopic-fluid-limits.tex | proposition: The exact frozen-rate majorant identity | Local argument | Not mapped |
| microscopic-fluid-limits.018 | microscopic-fluid-limits.tex | proposition: Sampling variance with correlations | Local argument | Not mapped |
| microscopic-fluid-limits.019 | microscopic-fluid-limits.tex | proposition: What weighted POD actually minimizes | Local argument | Not mapped |
| microscopic-fluid-limits.020 | microscopic-fluid-limits.tex | proposition: Interpolation exactness and amplification | Local argument | Not mapped |
| microscopic-fluid-limits.021 | microscopic-fluid-limits.tex | proposition: Nonnegative constitutive entropy production | Local argument | Not mapped |
| navier-stokes-release.001 | navier-stokes-release.tex | proposition: Quadratic residual identity | Local argument | Not mapped |
| navier-stokes-release.002 | navier-stokes-release.tex | proposition: A transverse wave and its covariance | Local argument | Not mapped |
| navier-stokes-release.003 | navier-stokes-release.tex | proposition: Averaging and nonlinear closure | Local argument | Not mapped |
| navier-stokes-release.004 | navier-stokes-release.tex | proposition: Energy estimate from rest | Local argument | Not mapped |
| navier-stokes-release.005 | navier-stokes-release.tex | proposition: Anisotropic concentration test | Local argument | Not mapped |
| navier-stokes-release.006 | navier-stokes-release.tex | proposition: Coordinate existence and derivative weights | Local argument | Not mapped |
| navier-stokes-release.007 | navier-stokes-release.tex | lemma: Words with no adjacent derivative letters | Local argument | Not mapped |
| navier-stokes-release.008 | navier-stokes-release.tex | proposition: Sparse Volterra systems | Local argument | Partial components: FluidInterfaces.lower_diagonal_lower_zero |
| navier-stokes-release.009 | navier-stokes-release.tex | lemma: A diagonal realization estimate | Local argument | Not mapped |
| navier-stokes-release.010 | navier-stokes-release.tex | proposition: All-order residual realization | Local argument | Not mapped |
| navier-stokes-release.011 | navier-stokes-release.tex | proposition: Localization without a divergence defect | Local argument | Not mapped |
| navier-stokes-release.012 | navier-stokes-release.tex | lemma: Realization of terminal force jets | Local argument | Not mapped |
| navier-stokes-release.013 | navier-stokes-release.tex | proposition: Residual-to-solution estimate on the flat torus | Local argument | Not mapped |
| navier-stokes-release.014 | navier-stokes-release.tex | proposition: Viscosity conversion | Local argument | Not mapped |
| navier-stokes-release.015 | navier-stokes-release.tex | proposition: Disjoint-support periodization | Local argument | Not mapped |
| fluid-structures.001 | fluid-structures.tex | proposition: The differential-form momentum equation | Local argument | Not mapped |
| fluid-structures.002 | fluid-structures.tex | proposition: Energy and the work of a differential | Local argument | Not mapped |
| fluid-structures.003 | fluid-structures.tex | proposition: The integral quadratic-order representation | Local argument | Partial components: FluidInterfaces.quadratic_generator_square, FluidInterfaces.renormalization_quadratic_identity, FluidInterfaces.renormalization_determinant, FluidInterfaces.renormalization_power_determinant, FluidInterfaces.renormalization_is_quadratic_order_element, FluidInterfaces.quadratic_order_one, FluidInterfaces.quadratic_order_addition, FluidInterfaces.quadratic_order_multiplication, FluidInterfaces.quadratic_order_determinant, FluidInterfaces.quadratic_order_representation_injective |
| fluid-structures.004 | fluid-structures.tex | proposition: Covering multiplicity and exact averaging | Local argument | Partial components: FluidInterfaces.renormalization_power_determinant |
| fluid-structures.005 | fluid-structures.tex | proposition: Why this is not a complex elliptic-curve endomorphism | Local argument | Partial components: FluidInterfaces.no_commuting_complex_structure |
| fluid-structures.006 | fluid-structures.tex | lemma: A quadratic small-divisor bound | Local argument | Not mapped |
| fluid-structures.007 | fluid-structures.tex | proposition: A tame inverse of a torus directional derivative | Local argument | Not mapped |
| fluid-structures.008 | fluid-structures.tex | proposition: Positive realization and a signed tangent inverse | Local argument | Not mapped |
| fluid-structures.009 | fluid-structures.tex | proposition: Independence of ordered moment functionals | Local argument | Not mapped |
| fluid-structures.010 | fluid-structures.tex | lemma: A controlled quadratic moment correction | Local argument | Not mapped |
| fluid-structures.011 | fluid-structures.tex | proposition: Discrete Hodge energy and incompressible subspace | Local argument | Partial components: FluidInterfaces.boundary_flux_divergence_zero |
| fluid-structures.012 | fluid-structures.tex | theorem: An energy-certified finite learned evolution | Local argument | Partial components: FluidInterfaces.skew_transport_work, FluidInterfaces.factorized_viscosity_work, FluidInterfaces.finite_fluid_work_identity, FluidInterfaces.kinetic_energy_derivative, FluidInterfaces.finite_fluid_energy_derivative |
| quantum-fluid.001 | quantum-fluid.tex | proposition: The obstruction to an exact instantaneous closure | Local argument | Partial components: FluidInterfaces.hidden_state_prevents_autonomous_closure |
| quantum-fluid.002 | quantum-fluid.tex | theorem: Exact memory from a linear hidden subsystem | Local argument | Not mapped |
| quantum-fluid.003 | quantum-fluid.tex | proposition: Discrete memory and the resolvent determinant | Local argument | Partial components: FluidInterfaces.hidden_recurrence_expansion, FluidInterfaces.resolved_memory_identity |
| quantum-fluid.004 | quantum-fluid.tex | proposition: Covariance as the exact quadratic defect | Local argument | Not mapped |
| quantum-fluid.005 | quantum-fluid.tex | proposition: A trace-preserving quantum diffusion step | Local argument | Not mapped |
| quantum-fluid.006 | quantum-fluid.tex | proposition: Discrete heat energy and eigenvalues | Local argument | Not mapped |
| quantum-fluid.007 | quantum-fluid.tex | proposition: The local quantum hydrodynamic equations | Local argument | Not mapped |
| quantum-fluid.008 | quantum-fluid.tex | proposition: An exact scalar truncation calculation | Local argument | Not mapped |
| quantum-fluid.009 | quantum-fluid.tex | proposition: A counterexample to eigenvalue-only norm decay | Local argument | Not mapped |
| quantum-fluid.010 | quantum-fluid.tex | proposition: A sufficient dissipative norm hypothesis | Local argument | Not mapped |
| quantum-fluid.011 | quantum-fluid.tex | proposition: Real nonresonance excludes neutral oscillatory modes | Local argument | Not mapped |
| quantum-fluid.012 | quantum-fluid.tex | proposition: A norm-controlled short-time Carleman estimate | Local argument | Not mapped |
| quantum-fluid.013 | quantum-fluid.tex | proposition: A parameterized positive constitutive coefficient | Local argument | Not mapped |
| quantum-fluid.014 | quantum-fluid.tex | proposition: The circuit derivative and a nonlinear loss | Local argument | Not mapped |
| fluid-circuit-repairs.001 | fluid-circuit-repairs.tex | proposition: Equality map as a partial isometry | Local argument | Not mapped |
| fluid-circuit-repairs.002 | fluid-circuit-repairs.tex | proposition: Reversible equality encoding and its success probability | Local argument | Not mapped |
| fluid-circuit-repairs.003 | fluid-circuit-repairs.tex | proposition: Contraction-normalized rectangular dilation | Local argument | Not mapped |
| fluid-circuit-repairs.004 | fluid-circuit-repairs.tex | proposition: Linear instrument, conditional normalization | Local argument | Not mapped |
| quantum-spin-scope.001 | quantum-spin-scope.tex | proposition: Periodic compatibility for a smooth global lift | Local argument | Not mapped |
| quantum-spin-scope.002 | quantum-spin-scope.tex | proposition: A smooth fluid solution excluded by these global-lift assumptions | Local argument | Not mapped |
| reduction-contracts.001 | reduction-contracts.tex | theorem: Factorization through retained information | Local argument | Partial components: ReductionContracts.factorization_iff_fiber_constant, ReductionContracts.reduced_output_unique, ReductionContracts.discrete_closure_iff, ReductionContracts.mismatched_fiber_excludes_closure |
| reduction-contracts.002 | reduction-contracts.tex | proposition: Propagation of an exact discrete reduction | Local argument | Partial components: ReductionContracts.discrete_trajectory_preserved |
| reduction-contracts.003 | reduction-contracts.tex | proposition: Unresolved diameter bounds approximation error | Local argument | Partial components: ReductionContracts.fiber_error_lower_bound, ReductionContracts.fiber_diameter_le_twice_error |
| reduction-contracts.004 | reduction-contracts.tex | proposition: Arbitrarily large cancellation gain | Local argument | Partial components: ReductionContracts.signedPartner_constant_coefficient, ReductionContracts.signedPartner_linear_coefficient, ReductionContracts.signedPartner_ne_zero, ReductionContracts.signedPartner_order, ReductionContracts.signed_cancellation_identity, ReductionContracts.signed_cancellation_sum_ne_zero, ReductionContracts.signed_cancellation_order, ReductionContracts.signed_cancellation_strict, ReductionContracts.no_universal_minimum_rule |
| toric-transport-audit.001 | toric-transport-audit.tex | theorem: Typed transport telescope | Local argument | Partial components: TransportContracts.suffix_transport_telescope, TransportContracts.closed_path_residual, TransportContracts.flat_closed_path_zero, TransportContracts.two_arrow_transport, TransportContracts.fixed_vector_closed_path_zero |
| toric-transport-audit.002 | toric-transport-audit.tex | proposition: A flat-cycle counterexample to prefix transport | Local argument | Partial components: TransportContracts.scalar_counterexample_flat, TransportContracts.scalar_prefix_counterexample, TransportContracts.scalar_suffix_correction |
| toric-transport-audit.003 | toric-transport-audit.tex | proposition: Exact hypothesis for orthogonal Hodge components | Local argument | Not mapped |
| toric-transport-audit.004 | toric-transport-audit.tex | proposition: Deterministic certificates have zero extra Bayes information | Local argument | Not mapped |
| toric-transport-audit.005 | toric-transport-audit.tex | proposition: Actual predictor improvement includes approximation error | Local argument | Not mapped |
| toric-transport-audit.006 | toric-transport-audit.tex | proposition: Damping cannot repair every expanding cycle | Local argument | Partial components: TransportContracts.positive_damping_bound_not_contracting, TransportContracts.expanding_scalar_damping |
| toric-transport-audit.007 | toric-transport-audit.tex | proposition: A sufficient dissipativity condition for relaxation | Local argument | Not mapped |
| toric-transport-audit.008 | toric-transport-audit.tex | proposition: Trace preservation obstructs a zero path relation | Local argument | Partial components: TransportContracts.trace_preserving_composite_nonzero |
| toric-transport-audit.009 | toric-transport-audit.tex | proposition: Exact logarithmic identities and dequantization error | Local argument | Not mapped |
| toric-transport-audit.010 | toric-transport-audit.tex | proposition: When a finite tropical mask is exact | Local argument | Not mapped |
| toric-transport-audit.011 | toric-transport-audit.tex | proposition: Exact-step and bounded-length tropical paths | Local argument | Not mapped |
| toric-transport-audit.012 | toric-transport-audit.tex | proposition: A nilpotent Jacobian with arbitrarily large gain | Local argument | Partial components: TransportContracts.nonnormal_shear_square_zero, TransportContracts.nonnormal_shear_unit_image, TransportContracts.nonnormal_shear_gain_squared, TransportContracts.nonnormal_shear_strict_gain, TransportContracts.nonnormal_shear_second_jvp_zero, TransportContracts.nonnormal_shear_not_normal |
| cyclic-cosmology.001 | cyclic-cosmology.tex | proposition: Connection change and null trajectories | Local argument | Not mapped |
| cyclic-cosmology.002 | cyclic-cosmology.tex | proposition: Hodge scaling and the four-dimensional Maxwell system | Local argument | Not mapped |
| cyclic-cosmology.003 | cyclic-cosmology.tex | theorem: Quartic compactification and conformal time | Local argument | Not mapped |
| cyclic-cosmology.004 | cyclic-cosmology.tex | proposition: Spin lowering and Stokes invariance | Local argument | Not mapped |
| cyclic-cosmology.005 | cyclic-cosmology.tex | theorem: Classical data processing | Local argument | Not mapped |
| cyclic-cosmology.006 | cyclic-cosmology.tex | proposition: Identifiability and its quantitative obstruction | Local argument | Not mapped |
| cyclic-cosmology.007 | cyclic-cosmology.tex | proposition: Finite records and a decoding requirement | Local argument | Not mapped |
| cyclic-cosmology.008 | cyclic-cosmology.tex | proposition: Trace-distance contraction | Local argument | Not mapped |
| cyclic-cosmology.009 | cyclic-cosmology.tex | corollary: No deterministic cloning of nonorthogonal pure states | Local argument | Not mapped |
| cyclic-cosmology.010 | cyclic-cosmology.tex | proposition: No signalling by a local unconditioned operation | Local argument | Not mapped |
| cyclic-cosmology.011 | cyclic-cosmology.tex | proposition: Quadratic-form moments | Local argument | Not mapped |
| cyclic-cosmology.012 | cyclic-cosmology.tex | theorem: A fixed-template matched filter | Local argument | Not mapped |
| cyclic-cosmology.013 | cyclic-cosmology.tex | theorem: Finite Monte Carlo rank calibration | Local argument | Not mapped |
| cyclic-cosmology.014 | cyclic-cosmology.tex | proposition: The elementary full-sky cosmic-variance calculation | Local argument | Not mapped |
| cyclic-cosmology.015 | cyclic-cosmology.tex | proposition: A forecast with linear nuisance templates | Local argument | Not mapped |
| cyclic-cosmology.016 | cyclic-cosmology.tex | problem: An end-to-end cross-aeon inference problem | Proposed open problem | Not mapped |
| learning-languages.001 | learning-languages.tex | theorem: A fixed ReLU recurrence recognizes $D_1$ | Local argument | Not mapped |
| learning-languages.002 | learning-languages.tex | proposition: Why the unbounded language is not regular | Local argument | Not mapped |
| learning-languages.003 | learning-languages.tex | proposition: Exact Boolean mechanisms in a ReLU network | Local argument | Not mapped |
| learning-languages.004 | learning-languages.tex | theorem: Finite structural counterfactuals have exact neural implementations | Local argument | Not mapped |
| learning-languages.005 | learning-languages.tex | proposition: Observational ambiguity survives every learner | Local argument | Not mapped |
| learning-languages.006 | learning-languages.tex | proposition: A learned policy inherits certified rewrite correctness | Local argument | Not mapped |
| learning-languages.007 | learning-languages.tex | lemma: Bounded-variable exponential bound | Local argument | Not mapped |
| learning-languages.008 | learning-languages.tex | theorem: Uniform error for a finite candidate family | Local argument | Not mapped |
| synthesis.001 | synthesis.tex | proposition: An exact periodic complex | Local argument | Not mapped |
| synthesis.002 | synthesis.tex | proposition: An explicit derived obstruction | Local argument | Not mapped |
| synthesis.003 | synthesis.tex | proposition: Exactness and an explicit metric gap | Local argument | Not mapped |
| synthesis.004 | synthesis.tex | proposition: Transport of a coercivity bound | Conditional local argument | Not mapped |
| synthesis.005 | synthesis.tex | corollary: Why pointwise equivalence is insufficient | Local argument | Not mapped |
| source-concordance.001 | source-concordance.tex | proposition: Trace-zero cubic presentation | Local argument | Not mapped |

## Conditional and external statements

- **foundations.003 — A precise conditional zero-location transfer.** Proves a zero-location transfer assuming local uniform convergence and a nonzero holomorphic limit. It does not establish these hypotheses for an L-function; Rouche's theorem is named background.
- **orders.011 — When a transport controls minima.** A metric transport criterion assuming two-sided quantitative norm bounds. It does not construct bounds uniform in an arithmetic family.
- **orders.022 — Degree multiplicativity from duality.** Derives degree multiplicativity from explicitly assumed dual-isogeny identities. It is not a proof of those duality identities.
- **complexes.021 — Buchsbaum--Eisenbud criterion; external theorem.** Buchsbaum--Eisenbud exactness criterion is cited, not proved locally. Bibliography keys: v2BE1973.
- **complexes.027 — Atiyah--Singer index theorem; external theorem.** Analytic/topological index equality is an external theorem. Bibliography keys: v2AS1968I.
- **standard-monomials.005 — External general Schur basis theorem.** The general integral Schur basis theorem is cited immediately before the environment; the elementary special cases have separate proofs. Bibliography keys: smtABW1982.
- **standard-monomials.013 — External standard basis theorem for complexes.** The general complex standard basis, reducedness, normality, and Cohen--Macaulay assertions are external results. Bibliography keys: v2DEP1982, v2DS1981.
- **standard-monomials.015 — External Schur filtration and its characteristic-zero splitting.** The general Schur filtration is external; the characteristic-zero representation splitting and convention checks are explained locally. Bibliography keys: v2DS1981, smtCW2011.
- **gauge-theory.005 — Atiyah--Hitchin--Singer index formula, external.** The AHS index formula is external. The current statement explicitly assumes connectedness; a separate symbol calculation is proved locally. Bibliography keys: AHS1978.
- **gauge-theory.012 — Passage of a uniform gap bound.** Assumes the preceding strong semigroup/projector convergence and a common positive gap bound. It does not construct these data for the continuum Yang--Mills limit.
- **synthesis.004 — Transport of a coercivity bound.** Transports an already supplied coercivity bound through an isomorphism with an already supplied positive lower singular-value bound.

## Selected external statements in the fluid chapters

These records classify source use and proof boundaries. They do not treat reported external results as newly proved local theorems.

### Released forced whole-space and periodic Navier--Stokes breakdown

Status: `external_cited_not_locally_reproved`. Bibliography keys: NSOpenAI2026.

Positive viscosity, smooth compactly supported external force, initial rest, bounded L2 energy, and finite-time unbounded L-infinity velocity; whole-space and periodic conclusions under their exact smoothness, support, and energy quantifiers. The analytic construction is supplied by the released paper, not by the interface propositions.

The complete 166-page paper was jointly read. Source review and dependency scan were completed, but the separate fresh upstream kernel and Comparator checks did not complete. The successful local Lean 4.24 checks do not verify this continuum theorem.

Source: `extension/manuscript/chapters/navier-stokes-release.tex`.

### Clay alternatives and periodic-pressure requirement

Status: `external_problem_statement`. Bibliography keys: NSFefferman.

Alternatives A and B impose zero force; C and D permit the specified smooth decaying forcing. The periodic formulation also requires periodic pressure, as clarified by the erratum. These are authoritative problem definitions, not new existence theorems.

Forced existential breakdown does not establish unforced positive-viscosity breakdown.

Source: `extension/manuscript/chapters/navier-stokes-release.tex`.

### Short-time hard-sphere Boltzmann--Grad convergence

Status: `external_cited_not_locally_reproved`. Bibliography keys: microGallagher2013.

The referenced hard-sphere theorem requires admissible asymptotic initial factorization and weighted hierarchy bounds, and gives short-time convergence of the specified observables away from positional diagonals. The full recollision proof is not reproduced.

Only the source's introduction, main convergence statement and concluding scope were reviewed; the monograph was not read or independently verified in full. No arbitrary-data, arbitrary-potential, or long-time particle-to-fluid theorem is inferred.

Source: `extension/manuscript/chapters/microscopic-fluid-limits.tex`.

### Golse--Saint-Raymond incompressible Navier--Stokes--Fourier limit

Status: `external_cited_not_locally_reproved`. Bibliography keys: microGolseSaintRaymond2009.

Theorem 2.4 is cited for the stated hard-cutoff collision kernels, whole-space incompressible scaling, entropy-controlled initial data, renormalized kinetic solutions and weak fluctuation topology. The limit solves the specified Navier--Stokes--Fourier system with an energy inequality; stronger initial-energy conclusions require the additional preparation assumptions.

An external weak-limit theorem, not a local regularity/uniqueness proof or a direct composition with the short-time particle limit. Source-reading coverage is bounded as recorded in the ledger.

Source: `extension/manuscript/chapters/microscopic-fluid-limits.tex`.

### Finite element exterior calculus stability requirements

Status: `external_framework_cited`. Bibliography keys: NSFEEC2006, NSFEEC2010.

The cited framework supplies the role of compatible projections and norm estimates in approximation stability. The local finite boundary and Hodge identities do not establish those estimates for a mesh family.

No complete FEEC theorem, mesh-uniform convergence theorem, or continuum limit is locally formalized.

Source: `extension/manuscript/chapters/fluid-structures.tex`.

### Dissipative quantum linearization and a source norm-gap correction

Status: `external_claim_with_local_counterexample`. Bibliography keys: NSLiu2021.

The reviewed version 4 reports a favorable R<1 regime with sparse access, preparation, solution-norm and error assumptions, and the added forcing-size condition. Its normalized quantum-state output does not include cost-free classical full-field readout.

The manuscript proves a specific counterexample to the source's eigenvalue-only Euclidean norm-decay inference, then uses an independently proved Hermitian-part condition. The unrepaired general norm-decay statement is not adopted as a dependency.

Source: `extension/manuscript/chapters/quantum-fluid.tex`.

### Nonresonant Carleman estimate with an explicit resonance gap

Status: `external_claim_hypotheses_audited_not_locally_reproved`. Bibliography keys: NSWu2025.

The cited Theorem 1.1 assumes diagonalizability, nonpositive spectral real parts, a uniform solution bound, and a strictly positive infimum resonance gap. The displayed geometric-convergence parameter must be less than one. Pointwise nonresonance alone does not establish a positive gap.

The source estimate is not a dependency of the singularity proof. The manuscript separately proves the real-spectrum obstruction and a short-time contractive-semigroup estimate, without claiming a theorem for arbitrary neutral real fluid systems.

Source: `extension/manuscript/chapters/quantum-fluid.tex`.

### End-to-end quantum lattice-Boltzmann cost and truncation study

Status: `external_study_with_local_interface_corrections`. Bibliography keys: NSJennings2026.

The cited study analyzes specified observables, lifting and time discretization, conditioning, unitary block construction, and observable extraction. Its numerical scaling and convergence reports are distinguished from its proved bounds.

The report supplies no universal quantum advantage theorem or continuum Navier--Stokes singularity proof for this project. The separate fluid-circuit-repairs input proves corrections to two reviewed finite-interface formulas, without claiming complete algorithm repair.

Source: `extension/manuscript/chapters/quantum-fluid.tex`.

### Reported normalization of the source collision matrix

Status: `external_formula_not_locally_rederived`. Bibliography keys: NSJennings2026.

The value alpha=6/bar(tau-star) is attributed to equation D58a for that source's D=2 collision matrix and parameter conventions. It is not rederived as a norm formula for an arbitrary collision model.

The local rectangular dilation theorem assumes alpha>0 and alpha>=||A|| explicitly. Its proof does not depend on treating this particular external numerical normalization as universal.

Source: `extension/manuscript/chapters/fluid-circuit-repairs.tex`.


## Exact scope of the partial Lean correspondences

### complexes.011 — Rank constraint and cohomology

- **ResearchBridge.complex_rank_bound**: The adjacent-rank inequality rank(A)+rank(B)<=dim(V1), assuming BA=0.
- **ResearchBridge.middle_exact_iff_rank_sum**: Middle exactness iff equality in the adjacent-rank bound, assuming BA=0.

### complexes.012 — Euler characteristic

- **ResearchBridge.euler_rank_identity**: The integer identity (a-r)-(b-r-s)+(c-s)=a-b+c after dimension substitution.

### complexes.025 — Exactness of the nonzero-covector Koszul complex

- **DiagramGrammar.homotopy_implies_exact**: The abstract implication from a zero composite and a middle contracting-homotopy identity to image=kernel. The exterior operations, their identity, and the full graded contracting homotopy are not formalized by this declaration.

### standard-monomials.004 — Contraction and a contracting homotopy

- **DiagramGrammar.homotopy_implies_exact**: The abstract middle exactness consequence once the contraction/creation homotopy and zero-composition equations have been supplied. The exterior algebra and its shuffle signs remain the manuscript's proof.

### cryptography.006 — Unimodular changes can have unbounded metric distortion

- **ResearchBridge.shear_determinant_one**: The displayed integer shear has determinant one.
- **ResearchBridge.shear_inverse**: The displayed shear multiplied by the opposite shear is the identity.
- **ResearchBridge.shear_e2_image**: The shear sends the second basis vector to (N,1).
- **ResearchBridge.shear_e2_norm_squared**: The real squared-coordinate length of that image is N^2+1; the square-root and unbounded-operator-norm conclusion are not formalized here.

### quantum-surfaces.004 — Logical qubits on a closed oriented surface

- **ResearchQuantum.euler_surface_rank_substitution**: The integer substitution E-(V-1)-(F-1)=2g, assuming V-E+F=2-2g; the surface and stabilizer rank hypotheses are not proved by this declaration.

### tensor-grammars.007 — Typed rewrite soundness

- **DiagramGrammar.context_sound**: Equality is preserved by typed one-hole sequential contexts. This syntax has identity, typed generators, and sequential composition; no tensor-context or density-operator syntax is formalized here.
- **DiagramGrammar.derivation_sound**: Every finite derivation of contextual sequential rewrites preserves the exact linear-map denotation, conditional on soundness of each basic rule.
- **DiagramGrammar.equiv_derivation_sound**: For the explicit linear-equivalence generator system, structural rules and inverse-pair cancellation are proved sound under finite contextual derivations. This is not completeness, confluence, or a certificate for floating-point code.

### tensor-grammars.009 — Transport of a complex and its metric

- **DiagramGrammar.complex_transport**: The zero-composition equation is preserved under independent linear equivalences. Match A=d2, B=d1, e0=F2, e1=F1, e2=F0. The general homology-quotient isomorphism is not proved by this declaration.
- **DiagramGrammar.matrix_hodge_conjugacy**: The finite complex-matrix Hodge conjugacy identity, with A=d2, B=d1, U0=F2, U1=F1, U2=F0 and endpoint U-adjoint*U=I hypotheses. Choosing all changes unitary makes inverse equal adjoint as in the text. Infinite-dimensional spectral assertions and homology are outside this lemma.

### navier-stokes-release.008 — Sparse Volterra systems

- **FluidInterfaces.lower_diagonal_lower_zero**: The composition of a strict lower block, a block diagonal map, and another strict lower block is zero. The two lower blocks may differ, as needed when a derivative hits a coefficient. This is only the block algebra; no function-space, Volterra, holomorphic, or convergence theorem is formalized by this declaration.

### fluid-structures.003 — The integral quadratic-order representation

- **FluidInterfaces.quadratic_generator_square**: The displayed integer generator A satisfies A*A=2*I.
- **FluidInterfaces.renormalization_quadratic_identity**: The displayed matrix J satisfies J*J-8*J+14*I=0 over the integers.
- **FluidInterfaces.renormalization_determinant**: The exact integer determinant of J is 14.
- **FluidInterfaces.renormalization_power_determinant**: For every natural k, det(J^k)=14^k; no topological degree is included.
- **FluidInterfaces.renormalization_is_quadratic_order_element**: The displayed matrix J is the coefficient-pair matrix rho(4,1).
- **FluidInterfaces.quadratic_order_one**: The integer coefficient-pair matrix rho(1,0) is the identity.
- **FluidInterfaces.quadratic_order_addition**: The coefficient-pair matrices obey rho(a,b)+rho(c,d)=rho(a+c,b+d).
- **FluidInterfaces.quadratic_order_multiplication**: The coefficient-pair matrices obey rho(a,b)rho(c,d)=rho(ac+2bd,ad+bc). A bundled ring homomorphism from an algebraic number-field order is not constructed by this identity.
- **FluidInterfaces.quadratic_order_determinant**: The exact norm determinant det(rho(a,b))=a^2-2b^2 over integer pairs.
- **FluidInterfaces.quadratic_order_representation_injective**: The map from integer pairs (a,b) to their displayed matrix is injective. Identification of these pairs with the order is the manuscript's argument.

### fluid-structures.004 — Covering multiplicity and exact averaging

- **FluidInterfaces.renormalization_power_determinant**: Only the arithmetic input det(J^k)=14^k. Neither the size of the lattice quotient, the covering degree, nor invariance of normalized Haar integration is proved by this Lean declaration.

### fluid-structures.005 — Why this is not a complex elliptic-curve endomorphism

- **FluidInterfaces.no_commuting_complex_structure**: For a real 2-by-2 matrix C commuting with the displayed J, C*C is not minus the identity. This exact linear-algebra statement does not formalize the subsequent geometry of elliptic curves.

### fluid-structures.011 — Discrete Hodge energy and incompressible subspace

- **FluidInterfaces.boundary_flux_divergence_zero**: Given matrices B,C with BC=0, B(Cq)=0. With B=delta_1 and C=delta_2 this is the proposition's final divergence-free consequence once delta_1 delta_2=0 is supplied; mass-matrix adjoints and Hodge positivity are not proved by this declaration.

### fluid-structures.012 — An energy-certified finite learned evolution

- **FluidInterfaces.skew_transport_work**: A finite real skew-symmetric matrix has zero quadratic work; use J=-K(a) at the current state.
- **FluidInterfaces.factorized_viscosity_work**: The Euclidean Gram term has work u^T(L^T L)u=|Lu|^2. The manuscript's learned closure uses this factorized form; existence of a factorization of a general positive semidefinite physical viscosity matrix is separate.
- **FluidInterfaces.finite_fluid_work_identity**: The algebraic work balance for skew transport, factorized physical viscosity, factorized learned dissipation, and forcing.
- **FluidInterfaces.kinetic_energy_derivative**: Actual finite Euclidean kinetic-energy differentiation from coordinate HasDerivAt hypotheses; it neither constructs a trajectory nor proves an ODE existence theorem.
- **FluidInterfaces.finite_fluid_energy_derivative**: At a specified time with the displayed coordinate derivatives, the finite energy derivative equals forcing work minus the two Gram dissipations. State-dependent coefficients may be evaluated at this time, but local existence, Gronwall, continuation, and continuum regularity are not part of the declaration.

### quantum-fluid.001 — The obstruction to an exact instantaneous closure

- **FluidInterfaces.hidden_state_prevents_autonomous_closure**: For linear A and B with B(y) nonzero, no function F of the retained state alone agrees with Ax+Bz for all retained and hidden states. No assertion is made about a restricted invariant manifold or a probabilistic conditional-expectation closure.

### quantum-fluid.003 — Discrete memory and the resolvent determinant

- **FluidInterfaces.hidden_recurrence_expansion**: The all-natural-time expansion z_n=D^n z_0+sum_{k<n}D^(n-1-k)Cx_k from the exact hidden recurrence, including the empty sum at zero.
- **FluidInterfaces.resolved_memory_identity**: The resulting exact discrete convolution in the retained recurrence. No continuous matrix exponential, continuous-time memory integral, or block-resolvent determinant identity is included.

### reduction-contracts.001 — Factorization through retained information

- **ReductionContracts.factorization_iff_fiber_constant**: Exact set-theoretic equivalence for a surjective observation map
- **ReductionContracts.reduced_output_unique**: Uniqueness on the surjective observed state space
- **ReductionContracts.discrete_closure_iff**: Specialization to a discrete state update
- **ReductionContracts.mismatched_fiber_excludes_closure**: Two indistinguishable inputs with different outputs exclude every deterministic closure

### reduction-contracts.002 — Propagation of an exact discrete reduction

- **ReductionContracts.discrete_trajectory_preserved**: Exact intertwining at every natural-number step

### reduction-contracts.003 — Unresolved diameter bounds approximation error

- **ReductionContracts.fiber_error_lower_bound**: Triangle-inequality error lower bound in a seminormed additive group
- **ReductionContracts.fiber_diameter_le_twice_error**: Uniform epsilon error implies at most twice-epsilon pair separation

### reduction-contracts.004 — Arbitrarily large cancellation gain

- **ReductionContracts.signedPartner_constant_coefficient**: Constant coefficient of the explicit rational polynomial
- **ReductionContracts.signedPartner_linear_coefficient**: Linear coefficient of the explicit rational polynomial
- **ReductionContracts.signedPartner_ne_zero**: The second summand is nonzero
- **ReductionContracts.signedPartner_order**: The second summand has order one
- **ReductionContracts.signed_cancellation_identity**: The sum is exactly the prescribed higher monomial
- **ReductionContracts.signed_cancellation_sum_ne_zero**: The residual polynomial is nonzero
- **ReductionContracts.signed_cancellation_order**: Its order is the arbitrary integer k+2
- **ReductionContracts.signed_cancellation_strict**: The residual order strictly exceeds the minimum summand order
- **ReductionContracts.no_universal_minimum_rule**: There is no universal exact minimum rule for signed polynomial addition

### toric-transport-audit.001 — Typed transport telescope

- **TransportContracts.suffix_transport_telescope**: Arbitrary finite path with all arrows acting on the same module
- **TransportContracts.closed_path_residual**: Closed-path endpoint residual
- **TransportContracts.flat_closed_path_zero**: Identity holonomy makes the closed residual zero
- **TransportContracts.two_arrow_transport**: Two-arrow noncommutative telescope
- **TransportContracts.fixed_vector_closed_path_zero**: Fixing the initial vector suffices without full flatness

### toric-transport-audit.002 — A flat-cycle counterexample to prefix transport

- **TransportContracts.scalar_counterexample_flat**: The counterexample has identity holonomy
- **TransportContracts.scalar_prefix_counterexample**: The incorrect prefix sum is exactly 3/2
- **TransportContracts.scalar_suffix_correction**: Correct suffix transport gives zero for the same data

### toric-transport-audit.006 — Damping cannot repair every expanding cycle

- **TransportContracts.positive_damping_bound_not_contracting**: The displayed upper bound is at least one for L≥1 and eta≥0
- **TransportContracts.expanding_scalar_damping**: The scalar multiplier is greater than one for positive damping

### toric-transport-audit.008 — Trace preservation obstructs a zero path relation

- **TransportContracts.trace_preserving_composite_nonzero**: Two real linear trace-preserving maps cannot have zero composite if a trace-one vector exists

### toric-transport-audit.012 — A nilpotent Jacobian with arbitrarily large gain

- **TransportContracts.nonnormal_shear_square_zero**: The explicit real matrix [[0,M],[0,0]] squares to zero
- **TransportContracts.nonnormal_shear_unit_image**: Its image on the explicit Euclidean unit vector (0,1) is (M,0)
- **TransportContracts.nonnormal_shear_gain_squared**: Exact coordinate squared norm of that image is M squared
- **TransportContracts.nonnormal_shear_strict_gain**: The one-step squared gain exceeds one when M>1
- **TransportContracts.nonnormal_shear_second_jvp_zero**: A second Jacobian-vector product is zero on every input
- **TransportContracts.nonnormal_shear_not_normal**: For nonzero M, the matrix does not commute with its transpose

The remaining verified declarations are not forced into a broader manuscript statement. They still have the scope and types recorded in their source files and verification manifests. Examples include scalar quadric expansions, abstract binary-character commutation, and a restricted binary-noise bound. Similar terminology alone does not establish a formal correspondence.

## Proposed research and incomplete goals outside the environment list

- **Arithmetic zero-location/GRH bridge** — No GRH theorem is asserted; arithmetic identification and analytic convergence inputs remain obligations. Source: extension/manuscript/chapters/foundations.tex.
- **Uniform metric control for arithmetic modules** — Construct and certify distortion bounds with explicit dependence on arithmetic input sizes. Source: extension/manuscript/chapters/synthesis.tex.
- **Resource-certified improvements to ECC quantum arithmetic** — A full reversible circuit, ancilla policy, success probability, and cost comparison are required; no general speedup is established. Source: extension/manuscript/chapters/synthesis.tex.
- **New lattice-cryptographic security reduction** — Module structure and correctness identities are not claimed to prove hardness or a new security reduction. Source: extension/manuscript/chapters/cryptography.tex.
- **Uniform physical Yang--Mills mass gap** — Requires an analytic infrared estimate surviving the stated limits and the correct reconstructed vacuum sector; no mass-gap theorem is asserted. Source: extension/manuscript/chapters/synthesis.tex.
- **Complete Lean formalization and complete linked-source proof audit** — The companion verifies 115 selected declarations and documents source coverage; it does not formalize all manuscript or source theorems or fully review every outbound linked work. Source: extension/manuscript/chapters/source-concordance.tex.
- **Fresh upstream continuum Navier--Stokes kernel and Comparator verification** — Exact upstream tools and sources were pinned. The fresh build attempt stopped at dependency artifacts after rate-limited cache retrieval; source inspection and the successful local companion checks are not substituted for that verification. Source: extension/manuscript/chapters/navier-stokes-release.tex.
- **New continuum conclusions from finite learned fluid models** — Finite energy stability, exact recurrence identities and circuit simulations do not establish mesh-uniform regularity, a hydrodynamic joint limit, unforced positive-viscosity blowup, or an improved continuum existence theorem. Source: extension/manuscript/chapters/fluid-structures.tex.
- **Trained quantum fluid ToricGT with demonstrated quantum advantage** — The new fluid companion supplies an explicit finite circuit and constrained model proposal, with classical simulation and structural checks. It does not claim a trained fluid model, quantum hardware execution of those new examples, or a proved end-to-end speedup. Source: extension/manuscript/chapters/quantum-fluid.tex.

## Lean source audit

The source audit checked all registered theorem modules and the Lean configuration after stripping nested block comments, line comments, and strings. It found no project axiom declaration, sorry/admit/sorryAx placeholder, unsafe declaration, or native_decide invocation. The module hashes, declaration sets, and print-axioms inventories match the existing successful verification manifests. Their reported dependencies are limited to propext, Classical.choice, and Quot.sound; the audit does not claim that foundational axioms are absent.

**The inventory generator itself does not run Lean.** Fresh second-pass kernel runs of all six modules are recorded in extension/lean/final-verification/verification.json and its six module logs. All 115 declaration-level dependency reports, printed types, source hashes and log hashes match the current successful record. The existing 35 precise component declarations remain mapped; validated additions are merged without reclassifying any composite manuscript statement as fully formalized. Earlier three-, four-, and 109-declaration six-module checks remain historical records.

The local successful check does not complete the upstream continuum Navier--Stokes build, which used a different toolchain and stopped at missing dependency artifacts. That outcome remains in navier-stokes/release-build-verification.json.

## Reproduction and limits

From the project root, run python extension/review/build_claim_register.py (or invoke the script by absolute path from any directory). The script reads manuscript and Lean sources and writes the JSON and Markdown claim register and formal-type-map, and refreshes the fluid-only review map's component references. It does not modify original Lean sources, verification manifests, or logs. Manual status annotations and type matches are visible in the script. The script enforces matching Lean source hashes. If manuscript claims are reordered or substantively changed, review the manual annotations before regenerating.

The inventory excludes unnumbered definitions, ordinary explanatory equations, prose results outside the explicitly selected external list, every theorem inside cited papers, and the inherited upstream project. It therefore does not constitute an assertion that all mathematical claims in all sources have been independently proved or formalized.
