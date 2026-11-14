# Formal declaration and manuscript component map

Exact declaration types and manually reviewed component correspondences, not a claim that all manuscript environments are formalized.

This snapshot records **82 verified declarations**; 35 are mapped to precise manuscript components. No composite manuscript environment is marked fully formalized.

Prefer kernel_printed_type when present: it includes elaborated implicit parameters and typeclass hypotheses. Otherwise the unchanged source signature and recorded section context are provided, with the exact source hash. Local definitions in the same module remain part of its interpretation.

Fresh local checks are recorded in `navier-stokes/local-kernel-verification.json` and its four raw logs. Those checks concern the local Lean 4.24 companion; the upstream continuum Lean 4.34 build has its separate incomplete status.

## Boundaries

- This map does not assert: Global ODE continuation from a finite energy derivative alone.
- This map does not assert: Continuous memory from a discrete recurrence theorem.
- This map does not assert: Covering-space degree or Haar averaging from a matrix determinant alone.
- This map does not assert: Analytic Volterra convergence from zero block composition alone.
- This map does not assert: Weighted POD/SVD optimality from a fixed Euclidean projector lemma alone.
- This map does not assert: Any fresh verification of the upstream continuum Navier--Stokes release.

## Declarations

### DiagramGrammar.complex_transport

Source: `extension/lean/DiagramGrammar.lean`. Verification: `extension/lean/diagram-verification.json`.

Reported foundational dependencies: `Quot.sound`, `propext`.

Elaborated type:

```lean
DiagramGrammar.complex_transport.{u_1, u_2, u_3, u_4, u_5, u_6, u_7} {K : Type u_1} {V0 : Type u_2} {V1 : Type u_3}
  {V2 : Type u_4} {W0 : Type u_5} {W1 : Type u_6} {W2 : Type u_7} [Semiring K] [AddCommMonoid V0] [AddCommMonoid V1]
  [AddCommMonoid V2] [AddCommMonoid W0] [AddCommMonoid W1] [AddCommMonoid W2] [Module K V0] [Module K V1] [Module K V2]
  [Module K W0] [Module K W1] [Module K W2] (A : V0 →ₗ[K] V1) (B : V1 →ₗ[K] V2) (h : B ∘ₗ A = 0) (e0 : V0 ≃ₗ[K] W0)
  (e1 : V1 ≃ₗ[K] W1) (e2 : V2 ≃ₗ[K] W2) : (↑e2 ∘ₗ B ∘ₗ ↑e1.symm) ∘ₗ ↑e1 ∘ₗ A ∘ₗ ↑e0.symm = 0
```

- **tensor-grammars.009** (thm:unitary-chain-transport): The zero-composition equation is preserved under independent linear equivalences. Match A=d2, B=d1, e0=F2, e1=F1, e2=F0. The general homology-quotient isomorphism is not proved by this declaration.

### DiagramGrammar.context_sound

Source: `extension/lean/DiagramGrammar.lean`. Verification: `extension/lean/diagram-verification.json`.

Reported foundational dependencies: `Quot.sound`, `propext`.

Elaborated type:

```lean
DiagramGrammar.context_sound.{u, v, w, z} {Obj : Type u} {Gen : Obj → Obj → Type v} {K : Type z} [Semiring K]
  {V : Obj → Type w} [(a : Obj) → AddCommMonoid (V a)] [(a : Obj) → Module K (V a)]
  (rho : (a b : Obj) → Gen a b → V a →ₗ[K] V b) {a b x y : Obj} {d e : DiagramGrammar.Diagram Gen a b}
  (h : DiagramGrammar.denote rho d = DiagramGrammar.denote rho e) (C : DiagramGrammar.Context Gen a b x y) :
  DiagramGrammar.denote rho (DiagramGrammar.fill C d) = DiagramGrammar.denote rho (DiagramGrammar.fill C e)
```

- **tensor-grammars.007** (thm:typed-rewrite-soundness): Equality is preserved by typed one-hole sequential contexts. This syntax has identity, typed generators, and sequential composition; no tensor-context or density-operator syntax is formalized here.

### DiagramGrammar.derivation_sound

Source: `extension/lean/DiagramGrammar.lean`. Verification: `extension/lean/diagram-verification.json`.

Reported foundational dependencies: `Quot.sound`, `propext`.

Elaborated type:

```lean
DiagramGrammar.derivation_sound.{u, v, w, z} {Obj : Type u} {Gen : Obj → Obj → Type v} {K : Type z} [Semiring K]
  {V : Obj → Type w} [(a : Obj) → AddCommMonoid (V a)] [(a : Obj) → Module K (V a)]
  (rho : (a b : Obj) → Gen a b → V a →ₗ[K] V b)
  (Rules : {a b : Obj} → DiagramGrammar.Diagram Gen a b → DiagramGrammar.Diagram Gen a b → Prop)
  (valid :
    ∀ {a b : Obj} {d e : DiagramGrammar.Diagram Gen a b},
      Rules d e → DiagramGrammar.denote rho d = DiagramGrammar.denote rho e)
  {x y : Obj} {d e : DiagramGrammar.Diagram Gen x y} (h : DiagramGrammar.Derives (fun {a b} => Rules) d e) :
  DiagramGrammar.denote rho d = DiagramGrammar.denote rho e
```

- **tensor-grammars.007** (thm:typed-rewrite-soundness): Every finite derivation of contextual sequential rewrites preserves the exact linear-map denotation, conditional on soundness of each basic rule.

### DiagramGrammar.equivRule_sound

Source: `extension/lean/DiagramGrammar.lean`. Verification: `extension/lean/diagram-verification.json`.

Reported foundational dependencies: `Quot.sound`, `propext`.

Elaborated type:

```lean
DiagramGrammar.equivRule_sound.{u, w, z} {Obj : Type u} {K : Type z} [Semiring K] {V : Obj → Type w}
  [(a : Obj) → AddCommMonoid (V a)] [(a : Obj) → Module K (V a)] {a b : Obj}
  {d e : DiagramGrammar.Diagram (fun i j => V i ≃ₗ[K] V j) a b} (h : DiagramGrammar.EquivRule d e) :
  DiagramGrammar.denote (fun i j g => ↑g) d = DiagramGrammar.denote (fun i j g => ↑g) e
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### DiagramGrammar.equiv_derivation_sound

Source: `extension/lean/DiagramGrammar.lean`. Verification: `extension/lean/diagram-verification.json`.

Reported foundational dependencies: `Quot.sound`, `propext`.

Elaborated type:

```lean
DiagramGrammar.equiv_derivation_sound.{u, w, z} {Obj : Type u} {K : Type z} [Semiring K] {V : Obj → Type w}
  [(a : Obj) → AddCommMonoid (V a)] [(a : Obj) → Module K (V a)] {a b : Obj}
  {d e : DiagramGrammar.Diagram (fun i j => V i ≃ₗ[K] V j) a b}
  (h : DiagramGrammar.Derives (fun {a b} => DiagramGrammar.EquivRule) d e) :
  DiagramGrammar.denote (fun i j g => ↑g) d = DiagramGrammar.denote (fun i j g => ↑g) e
```

- **tensor-grammars.007** (thm:typed-rewrite-soundness): For the explicit linear-equivalence generator system, structural rules and inverse-pair cancellation are proved sound under finite contextual derivations. This is not completeness, confluence, or a certificate for floating-point code.

### DiagramGrammar.exact_transport

Source: `extension/lean/DiagramGrammar.lean`. Verification: `extension/lean/diagram-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
DiagramGrammar.exact_transport.{u_1, u_2, u_3, u_4, u_5, u_6, u_7} {K : Type u_1} {V0 : Type u_2} {V1 : Type u_3}
  {V2 : Type u_4} {W0 : Type u_5} {W1 : Type u_6} {W2 : Type u_7} [Semiring K] [AddCommMonoid V0] [AddCommMonoid V1]
  [AddCommMonoid V2] [AddCommMonoid W0] [AddCommMonoid W1] [AddCommMonoid W2] [Module K V0] [Module K V1] [Module K V2]
  [Module K W0] [Module K W1] [Module K W2] (A : V0 →ₗ[K] V1) (B : V1 →ₗ[K] V2)
  (hexact : LinearMap.range A = LinearMap.ker B) (e0 : V0 ≃ₗ[K] W0) (e1 : V1 ≃ₗ[K] W1) (e2 : V2 ≃ₗ[K] W2) :
  LinearMap.range (↑e1 ∘ₗ A ∘ₗ ↑e0.symm) = LinearMap.ker (↑e2 ∘ₗ B ∘ₗ ↑e1.symm)
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### DiagramGrammar.homotopy_implies_exact

Source: `extension/lean/DiagramGrammar.lean`. Verification: `extension/lean/diagram-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
DiagramGrammar.homotopy_implies_exact.{u_1, u_2, u_3, u_4} {K : Type u_1} {V0 : Type u_2} {V1 : Type u_3}
  {V2 : Type u_4} [Semiring K] [AddCommMonoid V0] [AddCommMonoid V1] [AddCommMonoid V2] [Module K V0] [Module K V1]
  [Module K V2] (A : V0 →ₗ[K] V1) (B : V1 →ₗ[K] V2) (hcomplex : B ∘ₗ A = 0) (s : V1 →ₗ[K] V0) (t : V2 →ₗ[K] V1)
  (hhomotopy : A ∘ₗ s + t ∘ₗ B = LinearMap.id) : LinearMap.range A = LinearMap.ker B
```

- **complexes.025** (): The abstract implication from a zero composite and a middle contracting-homotopy identity to image=kernel. The exterior operations, their identity, and the full graded contracting homotopy are not formalized by this declaration.
- **standard-monomials.004** (): The abstract middle exactness consequence once the contraction/creation homotopy and zero-composition equations have been supplied. The exterior algebra and its shuffle signs remain the manuscript's proof.

### DiagramGrammar.identity_loop_value

Source: `extension/lean/DiagramGrammar.lean`. Verification: `extension/lean/diagram-verification.json`.

Reported foundational dependencies: `Quot.sound`, `propext`.

Elaborated type:

```lean
DiagramGrammar.identity_loop_value.{u, v} {R : Type u} [CommSemiring R] {a : Type v} [Fintype a] [DecidableEq a] :
  Matrix.trace 1 = ↑(Fintype.card a)
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### DiagramGrammar.linearEquiv_cancellation

Source: `extension/lean/DiagramGrammar.lean`. Verification: `extension/lean/diagram-verification.json`.

Reported foundational dependencies: `Quot.sound`, `propext`.

Elaborated type:

```lean
DiagramGrammar.linearEquiv_cancellation.{u, w, z} {Obj : Type u} {K : Type z} [Semiring K] {V : Obj → Type w}
  [(a : Obj) → AddCommMonoid (V a)] [(a : Obj) → Module K (V a)] {a b : Obj} (e : V a ≃ₗ[K] V b) :
  DiagramGrammar.denote (fun i j g => ↑g) ((DiagramGrammar.Diagram.atom e).seq (DiagramGrammar.Diagram.atom e.symm)) =
    DiagramGrammar.denote (fun i j g => ↑g) (DiagramGrammar.Diagram.ident a)
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### DiagramGrammar.matrix_hodge_conjugacy

Source: `extension/lean/DiagramGrammar.lean`. Verification: `extension/lean/diagram-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
DiagramGrammar.matrix_hodge_conjugacy.{u_1, u_2, u_3} {n0 : Type u_1} {n1 : Type u_2} {n2 : Type u_3} [Fintype n0]
  [Fintype n1] [Fintype n2] [DecidableEq n0] [DecidableEq n2] (A : Matrix n1 n0 ℂ) (B : Matrix n2 n1 ℂ)
  (U0 : Matrix n0 n0 ℂ) (U1 : Matrix n1 n1 ℂ) (U2 : Matrix n2 n2 ℂ) (h0 : U0.conjTranspose * U0 = 1)
  (h2 : U2.conjTranspose * U2 = 1) :
  U1 * A * U0.conjTranspose * (U1 * A * U0.conjTranspose).conjTranspose +
      (U2 * B * U1.conjTranspose).conjTranspose * (U2 * B * U1.conjTranspose) =
    U1 * (A * A.conjTranspose + B.conjTranspose * B) * U1.conjTranspose
```

- **tensor-grammars.009** (thm:unitary-chain-transport): The finite complex-matrix Hodge conjugacy identity, with A=d2, B=d1, U0=F2, U1=F1, U2=F0 and endpoint U-adjoint*U=I hypotheses. Choosing all changes unitary makes inverse equal adjoint as in the text. Infinite-dimensional spectral assertions and homology are outside this lemma.

### DiagramGrammar.rectangular_trace_cyclicity

Source: `extension/lean/DiagramGrammar.lean`. Verification: `extension/lean/diagram-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
DiagramGrammar.rectangular_trace_cyclicity.{u, v} {R : Type u} [CommSemiring R] {a b : Type v} [Fintype a] [Fintype b]
  (A : Matrix a b R) (B : Matrix b a R) : (A * B).trace = (B * A).trace
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### DiagramGrammar.rewriteStep_sound

Source: `extension/lean/DiagramGrammar.lean`. Verification: `extension/lean/diagram-verification.json`.

Reported foundational dependencies: `Quot.sound`, `propext`.

Elaborated type:

```lean
DiagramGrammar.rewriteStep_sound.{u, v, w, z} {Obj : Type u} {Gen : Obj → Obj → Type v} {K : Type z} [Semiring K]
  {V : Obj → Type w} [(a : Obj) → AddCommMonoid (V a)] [(a : Obj) → Module K (V a)]
  (rho : (a b : Obj) → Gen a b → V a →ₗ[K] V b)
  (Rules : {a b : Obj} → DiagramGrammar.Diagram Gen a b → DiagramGrammar.Diagram Gen a b → Prop)
  (valid :
    ∀ {a b : Obj} {d e : DiagramGrammar.Diagram Gen a b},
      Rules d e → DiagramGrammar.denote rho d = DiagramGrammar.denote rho e)
  {x y : Obj} {d e : DiagramGrammar.Diagram Gen x y} (h : DiagramGrammar.RewriteStep (fun {a b} => Rules) d e) :
  DiagramGrammar.denote rho d = DiagramGrammar.denote rho e
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### DiagramGrammar.structural_derivation_sound

Source: `extension/lean/DiagramGrammar.lean`. Verification: `extension/lean/diagram-verification.json`.

Reported foundational dependencies: `Quot.sound`, `propext`.

Elaborated type:

```lean
DiagramGrammar.structural_derivation_sound.{u, v, w, z} {Obj : Type u} {Gen : Obj → Obj → Type v} {K : Type z}
  [Semiring K] {V : Obj → Type w} [(a : Obj) → AddCommMonoid (V a)] [(a : Obj) → Module K (V a)]
  (rho : (a b : Obj) → Gen a b → V a →ₗ[K] V b) {x y : Obj} {d e : DiagramGrammar.Diagram Gen x y}
  (h : DiagramGrammar.Derives (fun {a b} => DiagramGrammar.StructuralRule) d e) :
  DiagramGrammar.denote rho d = DiagramGrammar.denote rho e
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### DiagramGrammar.structural_sound

Source: `extension/lean/DiagramGrammar.lean`. Verification: `extension/lean/diagram-verification.json`.

Reported foundational dependencies: `Quot.sound`, `propext`.

Elaborated type:

```lean
DiagramGrammar.structural_sound.{u, v, w, z} {Obj : Type u} {Gen : Obj → Obj → Type v} {K : Type z} [Semiring K]
  {V : Obj → Type w} [(a : Obj) → AddCommMonoid (V a)] [(a : Obj) → Module K (V a)]
  (rho : (a b : Obj) → Gen a b → V a →ₗ[K] V b) {a b : Obj} {d e : DiagramGrammar.Diagram Gen a b}
  (h : DiagramGrammar.StructuralRule d e) : DiagramGrammar.denote rho d = DiagramGrammar.denote rho e
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### DiagramGrammar.tensor_interchange

Source: `extension/lean/DiagramGrammar.lean`. Verification: `extension/lean/diagram-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
DiagramGrammar.tensor_interchange.{u, v} {R : Type u} [CommSemiring R] {a b c d e f : Type v} [Fintype b] [Fintype e]
  (A : Matrix a b R) (B : Matrix b c R) (C : Matrix d e R) (D : Matrix e f R) :
  Matrix.kroneckerMap (fun x1 x2 => x1 * x2) A C * Matrix.kroneckerMap (fun x1 x2 => x1 * x2) B D =
    Matrix.kroneckerMap (fun x1 x2 => x1 * x2) (A * B) (C * D)
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### DiagramGrammar.tensor_trace_factorization

Source: `extension/lean/DiagramGrammar.lean`. Verification: `extension/lean/diagram-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
DiagramGrammar.tensor_trace_factorization.{u, v} {R : Type u} [CommSemiring R] {a b : Type v} [Fintype a] [Fintype b]
  (A : Matrix a a R) (B : Matrix b b R) : (Matrix.kroneckerMap (fun x1 x2 => x1 * x2) A B).trace = A.trace * B.trace
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### FluidInterfaces.boundary_flux_divergence_zero

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.boundary_flux_divergence_zero.{u_1, u_2, u_3} {n : Type u_1} {m : Type u_2} {p : Type u_3} [Fintype n]
  [Fintype p] (B : Matrix m n ℝ) (C : Matrix n p ℝ) (hcomplex : B * C = 0) (q : p → ℝ) : B *ᵥ C *ᵥ q = 0
```

- **fluid-structures.011** (prop:fluid-discrete-hodge): Given matrices B,C with BC=0, B(Cq)=0. With B=delta_1 and C=delta_2 this is the proposition's final divergence-free consequence once delta_1 delta_2=0 is supplied; mass-matrix adjoints and Hodge positivity are not proved by this declaration.

### FluidInterfaces.boundary_flux_update_preserves_divergence

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.boundary_flux_update_preserves_divergence.{u_1, u_2, u_3} {n : Type u_1} {m : Type u_2} {p : Type u_3}
  [Fintype n] [Fintype p] (B : Matrix m n ℝ) (C : Matrix n p ℝ) (hcomplex : B * C = 0) (u : n → ℝ) (q : p → ℝ) :
  B *ᵥ (u + C *ᵥ q) = B *ᵥ u
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### FluidInterfaces.dot_self_nonneg

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.dot_self_nonneg.{u_1} {n : Type u_1} [Fintype n] (u : n → ℝ) : 0 ≤ u ⬝ᵥ u
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### FluidInterfaces.factorized_viscosity_nonneg

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.factorized_viscosity_nonneg.{u_1, u_2} {n : Type u_1} {m : Type u_2} [Fintype n] [Fintype m]
  (L : Matrix m n ℝ) (u : n → ℝ) : 0 ≤ u ⬝ᵥ (Lᵀ * L) *ᵥ u
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### FluidInterfaces.factorized_viscosity_work

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.factorized_viscosity_work.{u_1, u_2} {n : Type u_1} {m : Type u_2} [Fintype n] [Fintype m]
  (L : Matrix m n ℝ) (u : n → ℝ) : u ⬝ᵥ (Lᵀ * L) *ᵥ u = L *ᵥ u ⬝ᵥ L *ᵥ u
```

- **fluid-structures.012** (thm:fluid-finite-closure): The Euclidean Gram term has work u^T(L^T L)u=|Lu|^2. The manuscript's learned closure uses this factorized form; existence of a factorization of a general positive semidefinite physical viscosity matrix is separate.

### FluidInterfaces.finite_fluid_energy_derivative

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.finite_fluid_energy_derivative.{u_1, u_2, u_3} {n : Type u_1} {m : Type u_2} {p : Type u_3} [Fintype n]
  [Fintype m] [Fintype p] (J : Matrix n n ℝ) (hJ : Jᵀ = -J) (D : Matrix m n ℝ) (L : Matrix p n ℝ) (ν : ℝ)
  (u : ℝ → n → ℝ) (force : n → ℝ) (t : ℝ)
  (hu : ∀ (i : n), HasDerivAt (fun s => u s i) ((J *ᵥ u t - ν • (Dᵀ * D) *ᵥ u t - (Lᵀ * L) *ᵥ u t + force) i) t) :
  HasDerivAt (fun s => FluidInterfaces.kineticEnergy (u s))
    (u t ⬝ᵥ force - ν * D *ᵥ u t ⬝ᵥ D *ᵥ u t - L *ᵥ u t ⬝ᵥ L *ᵥ u t) t
```

- **fluid-structures.012** (thm:fluid-finite-closure): At a specified time with the displayed coordinate derivatives, the finite energy derivative equals forcing work minus the two Gram dissipations. State-dependent coefficients may be evaluated at this time, but local existence, Gronwall, continuation, and continuum regularity are not part of the declaration.

### FluidInterfaces.finite_fluid_work_identity

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.finite_fluid_work_identity.{u_1, u_2, u_3} {n : Type u_1} {m : Type u_2} {p : Type u_3} [Fintype n]
  [Fintype m] [Fintype p] (J : Matrix n n ℝ) (hJ : Jᵀ = -J) (D : Matrix m n ℝ) (L : Matrix p n ℝ) (ν : ℝ)
  (u force : n → ℝ) :
  u ⬝ᵥ (J *ᵥ u - ν • (Dᵀ * D) *ᵥ u - (Lᵀ * L) *ᵥ u + force) = u ⬝ᵥ force - ν * D *ᵥ u ⬝ᵥ D *ᵥ u - L *ᵥ u ⬝ᵥ L *ᵥ u
```

- **fluid-structures.012** (thm:fluid-finite-closure): The algebraic work balance for skew transport, factorized physical viscosity, factorized learned dissipation, and forcing.

### FluidInterfaces.hidden_recurrence_expansion

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.hidden_recurrence_expansion.{u_1, u_2, u_3} {K : Type u_1} {X : Type u_2} {Y : Type u_3} [Field K]
  [AddCommGroup X] [Module K X] [AddCommGroup Y] [Module K Y] (C : X →ₗ[K] Y) (D : Module.End K Y) (p : ℕ → X)
  (q : ℕ → Y) (hstep : ∀ (n : ℕ), q (n + 1) = D (q n) + C (p n)) (n : ℕ) :
  q n = (D ^ n) (q 0) + ∑ k ∈ Finset.range n, (D ^ (n - 1 - k)) (C (p k))
```

- **quantum-fluid.003** (prop:fluid-discrete-memory): The all-natural-time expansion z_n=D^n z_0+sum_{k<n}D^(n-1-k)Cx_k from the exact hidden recurrence, including the empty sum at zero.

### FluidInterfaces.hidden_state_prevents_autonomous_closure

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `propext`.

Elaborated type:

```lean
FluidInterfaces.hidden_state_prevents_autonomous_closure.{u_1, u_2, u_3} {K : Type u_1} {X : Type u_2} {Y : Type u_3}
  [Field K] [AddCommGroup X] [Module K X] [AddCommGroup Y] [Module K Y] (A : Module.End K X) (B : Y →ₗ[K] X) (y : Y)
  (hy : B y ≠ 0) : ¬∃ F, ∀ (x : X) (z : Y), F x = A x + B z
```

- **quantum-fluid.001** (prop:fluid-closure-obstruction): For linear A and B with B(y) nonzero, no function F of the retained state alone agrees with Ax+Bz for all retained and hidden states. No assertion is made about a restricted invariant manifold or a probabilistic conditional-expectation closure.

### FluidInterfaces.kineticEnergy_nonneg

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.kineticEnergy_nonneg.{u_1} {n : Type u_1} [Fintype n] (u : n → ℝ) : 0 ≤ FluidInterfaces.kineticEnergy u
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### FluidInterfaces.kinetic_energy_derivative

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.kinetic_energy_derivative.{u_1} {n : Type u_1} [Fintype n] (u : ℝ → n → ℝ) (v : n → ℝ) (t : ℝ)
  (hu : ∀ (i : n), HasDerivAt (fun s => u s i) (v i) t) :
  HasDerivAt (fun s => FluidInterfaces.kineticEnergy (u s)) (u t ⬝ᵥ v) t
```

- **fluid-structures.012** (thm:fluid-finite-closure): Actual finite Euclidean kinetic-energy differentiation from coordinate HasDerivAt hypotheses; it neither constructs a trajectory nor proves an ODE existence theorem.

### FluidInterfaces.lower_diagonal_lower_zero

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.lower_diagonal_lower_zero.{u_1, u_2, u_3} {K : Type u_1} {X : Type u_2} {Y : Type u_3} [Field K]
  [AddCommGroup X] [Module K X] [AddCommGroup Y] [Module K Y] (L M : X →ₗ[K] Y) (DX : Module.End K X)
  (DY : Module.End K Y) : FluidInterfaces.lowerBlock L ∘ₗ LinearMap.prodMap DX DY ∘ₗ FluidInterfaces.lowerBlock M = 0
```

- **navier-stokes-release.008** (prop:ns-sparse-volterra): The composition of a strict lower block, a block diagonal map, and another strict lower block is zero. The two lower blocks may differ, as needed when a derivative hits a coefficient. This is only the block algebra; no function-space, Volterra, holomorphic, or convergence theorem is formalized by this declaration.

### FluidInterfaces.no_commuting_complex_structure

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.no_commuting_complex_structure (I : Matrix (Fin 2) (Fin 2) ℝ)
  (hc : I * !![3, 1; 1, 5] = !![3, 1; 1, 5] * I) : I * I ≠ -1
```

- **fluid-structures.005** (prop:fluid-no-complex): For a real 2-by-2 matrix C commuting with the displayed J, C*C is not minus the identity. This exact linear-algebra statement does not formalize the subsequent geometry of elliptic curves.

### FluidInterfaces.pressure_work_zero

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.pressure_work_zero.{u_1, u_3} {n : Type u_1} {p : Type u_3} [Fintype n] [Fintype p] (B : Matrix p n ℝ)
  (u : n → ℝ) (pressure : p → ℝ) (hu : B *ᵥ u = 0) : u ⬝ᵥ Bᵀ *ᵥ pressure = 0
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### FluidInterfaces.projection_best_approximation

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.projection_best_approximation.{u_1} {n : Type u_1} [Fintype n] (P : Matrix n n ℝ) (hs : Pᵀ = P)
  (hi : P * P = P) (u v : n → ℝ) (hv : P *ᵥ v = v) :
  FluidInterfaces.kineticEnergy (u - P *ᵥ u) ≤ FluidInterfaces.kineticEnergy (u - v)
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### FluidInterfaces.projection_energy_nonincrease

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.projection_energy_nonincrease.{u_1} {n : Type u_1} [Fintype n] (P : Matrix n n ℝ) (hs : Pᵀ = P)
  (hi : P * P = P) (u : n → ℝ) : FluidInterfaces.kineticEnergy (P *ᵥ u) ≤ FluidInterfaces.kineticEnergy u
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### FluidInterfaces.projection_energy_split

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.projection_energy_split.{u_1} {n : Type u_1} [Fintype n] (P : Matrix n n ℝ) (hs : Pᵀ = P)
  (hi : P * P = P) (u : n → ℝ) :
  FluidInterfaces.kineticEnergy u = FluidInterfaces.kineticEnergy (P *ᵥ u) + FluidInterfaces.kineticEnergy (u - P *ᵥ u)
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### FluidInterfaces.projection_residual_kernel

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.projection_residual_kernel.{u_1} {n : Type u_1} [Fintype n] (P : Matrix n n ℝ) (hP : P * P = P)
  (u : n → ℝ) : P *ᵥ (u - P *ᵥ u) = 0
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### FluidInterfaces.projection_residual_orthogonal

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.projection_residual_orthogonal.{u_1} {n : Type u_1} [Fintype n] (P : Matrix n n ℝ) (hs : Pᵀ = P)
  (hi : P * P = P) (u v : n → ℝ) : (u - P *ᵥ u) ⬝ᵥ P *ᵥ v = 0
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### FluidInterfaces.quadratic_generator_square

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.quadratic_generator_square :
  FluidInterfaces.quadraticGenerator * FluidInterfaces.quadraticGenerator = 2 • 1
```

- **fluid-structures.003** (prop:fluid-order): The displayed integer generator A satisfies A*A=2*I.

### FluidInterfaces.quadratic_order_addition

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.quadratic_order_addition (a b c d : ℤ) :
  FluidInterfaces.quadraticOrderMatrix a b + FluidInterfaces.quadraticOrderMatrix c d =
    FluidInterfaces.quadraticOrderMatrix (a + c) (b + d)
```

- **fluid-structures.003** (prop:fluid-order): The coefficient-pair matrices obey rho(a,b)+rho(c,d)=rho(a+c,b+d).

### FluidInterfaces.quadratic_order_determinant

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.quadratic_order_determinant (a b : ℤ) :
  (FluidInterfaces.quadraticOrderMatrix a b).det = a ^ 2 - 2 * b ^ 2
```

- **fluid-structures.003** (prop:fluid-order): The exact norm determinant det(rho(a,b))=a^2-2b^2 over integer pairs.

### FluidInterfaces.quadratic_order_multiplication

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.quadratic_order_multiplication (a b c d : ℤ) :
  FluidInterfaces.quadraticOrderMatrix a b * FluidInterfaces.quadraticOrderMatrix c d =
    FluidInterfaces.quadraticOrderMatrix (a * c + 2 * b * d) (a * d + b * c)
```

- **fluid-structures.003** (prop:fluid-order): The coefficient-pair matrices obey rho(a,b)rho(c,d)=rho(ac+2bd,ad+bc). A bundled ring homomorphism from an algebraic number-field order is not constructed by this identity.

### FluidInterfaces.quadratic_order_one

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.quadratic_order_one : FluidInterfaces.quadraticOrderMatrix 1 0 = 1
```

- **fluid-structures.003** (prop:fluid-order): The integer coefficient-pair matrix rho(1,0) is the identity.

### FluidInterfaces.quadratic_order_representation_injective

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.quadratic_order_representation_injective :
  Function.Injective fun ab => FluidInterfaces.quadraticOrderMatrix ab.1 ab.2
```

- **fluid-structures.003** (prop:fluid-order): The map from integer pairs (a,b) to their displayed matrix is injective. Identification of these pairs with the order is the manuscript's argument.

### FluidInterfaces.renormalization_determinant

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.renormalization_determinant : FluidInterfaces.renormalizationMatrix.det = 14
```

- **fluid-structures.003** (prop:fluid-order): The exact integer determinant of J is 14.

### FluidInterfaces.renormalization_is_quadratic_order_element

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.renormalization_is_quadratic_order_element :
  FluidInterfaces.renormalizationMatrix = FluidInterfaces.quadraticOrderMatrix 4 1
```

- **fluid-structures.003** (prop:fluid-order): The displayed matrix J is the coefficient-pair matrix rho(4,1).

### FluidInterfaces.renormalization_power_determinant

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.renormalization_power_determinant (k : ℕ) : (FluidInterfaces.renormalizationMatrix ^ k).det = 14 ^ k
```

- **fluid-structures.003** (prop:fluid-order): For every natural k, det(J^k)=14^k; no topological degree is included.
- **fluid-structures.004** (prop:fluid-covering): Only the arithmetic input det(J^k)=14^k. Neither the size of the lattice quotient, the covering degree, nor invariance of normalized Haar integration is proved by this Lean declaration.

### FluidInterfaces.renormalization_quadratic_identity

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.renormalization_quadratic_identity :
  FluidInterfaces.renormalizationMatrix * FluidInterfaces.renormalizationMatrix -
        8 • FluidInterfaces.renormalizationMatrix +
      14 • 1 =
    0
```

- **fluid-structures.003** (prop:fluid-order): The displayed matrix J satisfies J*J-8*J+14*I=0 over the integers.

### FluidInterfaces.resolved_memory_identity

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.resolved_memory_identity.{u_1, u_2, u_3} {K : Type u_1} {X : Type u_2} {Y : Type u_3} [Field K]
  [AddCommGroup X] [Module K X] [AddCommGroup Y] [Module K Y] (A : Module.End K X) (B : Y →ₗ[K] X) (C : X →ₗ[K] Y)
  (D : Module.End K Y) (p : ℕ → X) (q : ℕ → Y) (hp : ∀ (n : ℕ), p (n + 1) = A (p n) + B (q n))
  (hq : ∀ (n : ℕ), q (n + 1) = D (q n) + C (p n)) (n : ℕ) :
  p (n + 1) = A (p n) + B ((D ^ n) (q 0)) + ∑ k ∈ Finset.range n, B ((D ^ (n - 1 - k)) (C (p k)))
```

- **quantum-fluid.003** (prop:fluid-discrete-memory): The resulting exact discrete convolution in the retained recurrence. No continuous matrix exponential, continuous-time memory integral, or block-resolvent determinant identity is included.

### FluidInterfaces.schur_elimination_iff

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.schur_elimination_iff.{u_1, u_2, u_3} {K : Type u_1} {X : Type u_2} {Y : Type u_3} [Field K]
  [AddCommGroup X] [Module K X] [AddCommGroup Y] [Module K Y] (A : X →ₗ[K] X) (B : Y →ₗ[K] X) (C : X →ₗ[K] Y)
  (D : Y ≃ₗ[K] Y) (x : X) (y : Y) (f : X) (g : Y) :
  A x + B y = f ∧ C x + D y = g ↔ (FluidInterfaces.schurComplement A B C D) x = f - B (D.symm g) ∧ y = D.symm (g - C x)
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### FluidInterfaces.skew_transport_work

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.skew_transport_work.{u_1} {n : Type u_1} [Fintype n] (J : Matrix n n ℝ) (hJ : Jᵀ = -J) (u : n → ℝ) :
  u ⬝ᵥ J *ᵥ u = 0
```

- **fluid-structures.012** (thm:fluid-finite-closure): A finite real skew-symmetric matrix has zero quadratic work; use J=-K(a) at the current state.

### FluidInterfaces.transpose_work

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.transpose_work.{u_1, u_2} {n : Type u_1} {m : Type u_2} [Fintype n] [Fintype m] (L : Matrix m n ℝ)
  (u : n → ℝ) (v : m → ℝ) : u ⬝ᵥ Lᵀ *ᵥ v = L *ᵥ u ⬝ᵥ v
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### FluidInterfaces.unforced_work_nonpositive

Source: `extension/lean/FluidInterfaces.lean`. Verification: `extension/lean/fluid-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
FluidInterfaces.unforced_work_nonpositive.{u_1, u_2, u_3} {n : Type u_1} {m : Type u_2} {p : Type u_3} [Fintype n]
  [Fintype m] [Fintype p] (J : Matrix n n ℝ) (hJ : Jᵀ = -J) (D : Matrix m n ℝ) (L : Matrix p n ℝ) (ν : ℝ) (hν : 0 ≤ ν)
  (u : n → ℝ) : u ⬝ᵥ (J *ᵥ u - ν • (Dᵀ * D) *ᵥ u - (Lᵀ * L) *ᵥ u) ≤ 0
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### ResearchBridge.binary_noise_bound

Source: `extension/lean/BridgeTheorems.lean`. Verification: `extension/lean/verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Verified source signature (with reviewed section context where needed):

```lean
theorem binary_noise_bound (e₁ e₂ r₁ r₂ E : ℝ)
    (hE : 0 ≤ E) (h₁ : |e₁| ≤ E) (h₂ : |e₂| ≤ E)
    (hr₁ : r₁ = 0 ∨ r₁ = 1) (hr₂ : r₂ = 0 ∨ r₂ = 1) :
    |e₁ * r₁ + e₂ * r₂| ≤ 2 * E
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### ResearchBridge.complex_range_le_kernel

Source: `extension/lean/BridgeTheorems.lean`. Verification: `extension/lean/verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Verified source signature (with reviewed section context where needed):

```lean
variable {K V₀ V₁ V₂ : Type*} [Field K]
variable [AddCommGroup V₀] [AddCommGroup V₁] [AddCommGroup V₂]
variable [Module K V₀] [Module K V₁] [Module K V₂]
theorem complex_range_le_kernel (A : V₀ →ₗ[K] V₁) (B : V₁ →ₗ[K] V₂)
    (h : B.comp A = 0) : LinearMap.range A ≤ LinearMap.ker B
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### ResearchBridge.complex_rank_bound

Source: `extension/lean/BridgeTheorems.lean`. Verification: `extension/lean/verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Verified source signature (with reviewed section context where needed):

```lean
variable {K V₀ V₁ V₂ : Type*} [Field K]
variable [AddCommGroup V₀] [AddCommGroup V₁] [AddCommGroup V₂]
variable [Module K V₀] [Module K V₁] [Module K V₂]
theorem complex_rank_bound [FiniteDimensional K V₁]
    (A : V₀ →ₗ[K] V₁) (B : V₁ →ₗ[K] V₂) (h : B.comp A = 0) :
    Module.finrank K (LinearMap.range A) + Module.finrank K (LinearMap.range B)
      ≤ Module.finrank K V₁
```

- **complexes.011** (): The adjacent-rank inequality rank(A)+rank(B)<=dim(V1), assuming BA=0.

### ResearchBridge.cone_equal_norm_iff

Source: `extension/lean/BridgeTheorems.lean`. Verification: `extension/lean/verification.json`.

Reported foundational dependencies: `Quot.sound`, `propext`.

Verified source signature (with reviewed section context where needed):

```lean
variable {R : Type*} [CommRing R]
theorem cone_equal_norm_iff (u₁ u₂ v₁ v₂ : R) :
    cone (u₁ + v₁) (u₂ + v₂) (u₁ - v₁) (u₂ - v₂) = 0 ↔
      u₁ ^ 2 + u₂ ^ 2 = v₁ ^ 2 + v₂ ^ 2
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### ResearchBridge.cone_perturbation

Source: `extension/lean/BridgeTheorems.lean`. Verification: `extension/lean/verification.json`.

Reported foundational dependencies: `propext`.

Verified source signature (with reviewed section context where needed):

```lean
variable {R : Type*} [CommRing R]
theorem cone_perturbation (x₁ x₂ y₁ y₂ u₁ u₂ v₁ v₂ t : R) :
    cone (x₁ + t * u₁) (x₂ + t * u₂) (y₁ + t * v₁) (y₂ + t * v₂) =
      cone x₁ x₂ y₁ y₂ +
        t * (y₁ * u₁ + y₂ * u₂ + v₁ * x₁ + v₂ * x₂) +
        t ^ 2 * cone u₁ u₂ v₁ v₂
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### ResearchBridge.cone_split_identity

Source: `extension/lean/BridgeTheorems.lean`. Verification: `extension/lean/verification.json`.

Reported foundational dependencies: `Quot.sound`, `propext`.

Verified source signature (with reviewed section context where needed):

```lean
variable {R : Type*} [CommRing R]
theorem cone_split_identity (u₁ u₂ v₁ v₂ : R) :
    cone (u₁ + v₁) (u₂ + v₂) (u₁ - v₁) (u₂ - v₂) =
      (u₁ ^ 2 + u₂ ^ 2) - (v₁ ^ 2 + v₂ ^ 2)
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### ResearchBridge.cone_tangent_second_order

Source: `extension/lean/BridgeTheorems.lean`. Verification: `extension/lean/verification.json`.

Reported foundational dependencies: `propext`.

Verified source signature (with reviewed section context where needed):

```lean
variable {R : Type*} [CommRing R]
theorem cone_tangent_second_order (x₁ x₂ y₁ y₂ u₁ u₂ v₁ v₂ t : R)
    (h₀ : cone x₁ x₂ y₁ y₂ = 0)
    (h₁ : y₁ * u₁ + y₂ * u₂ + v₁ * x₁ + v₂ * x₂ = 0) :
    cone (x₁ + t * u₁) (x₂ + t * u₂) (y₁ + t * v₁) (y₂ + t * v₂) =
      t ^ 2 * cone u₁ u₂ v₁ v₂
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### ResearchBridge.euler_rank_identity

Source: `extension/lean/BridgeTheorems.lean`. Verification: `extension/lean/verification.json`.

Reported foundational dependencies: `Quot.sound`, `propext`.

Verified source signature (with reviewed section context where needed):

```lean
theorem euler_rank_identity (a b c r s : ℤ) :
    (a - r) - (b - r - s) + (c - s) = a - b + c
```

- **complexes.012** (): The integer identity (a-r)-(b-r-s)+(c-s)=a-b+c after dimension substitution.

### ResearchBridge.hidden_collision_relation

Source: `extension/lean/BridgeTheorems.lean`. Verification: `extension/lean/verification.json`.

Reported foundational dependencies: `Quot.sound`, `propext`.

Verified source signature (with reviewed section context where needed):

```lean
variable {q : ℕ}
theorem hidden_collision_relation (x a b c d : ZMod q) :
    hiddenLinear x a b = hiddenLinear x c d ↔
      (a - c) + x * (b - d) = 0
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### ResearchBridge.hidden_kernel_relation

Source: `extension/lean/BridgeTheorems.lean`. Verification: `extension/lean/verification.json`.

Reported foundational dependencies: `Quot.sound`, `propext`.

Verified source signature (with reviewed section context where needed):

```lean
variable {q : ℕ}
theorem hidden_kernel_relation (x a b : ZMod q) :
    hiddenLinear x a b = 0 ↔ a = -(x * b)
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### ResearchBridge.hodge_characteristic_factor

Source: `extension/lean/BridgeTheorems.lean`. Verification: `extension/lean/verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Verified source signature (with reviewed section context where needed):

```lean
theorem hodge_characteristic_factor (x₁ x₂ y₁ y₂ t : ℝ)
    (h : cone x₁ x₂ y₁ y₂ = 0) :
    Matrix.det (t • (1 : Matrix (Fin 2) (Fin 2) ℝ) - hodgeMatrix x₁ x₂ y₁ y₂) =
      (t - (x₁ ^ 2 + x₂ ^ 2)) * (t - (y₁ ^ 2 + y₂ ^ 2))
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### ResearchBridge.hodge_characteristic_identity

Source: `extension/lean/BridgeTheorems.lean`. Verification: `extension/lean/verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Verified source signature (with reviewed section context where needed):

```lean
theorem hodge_characteristic_identity (x₁ x₂ y₁ y₂ t : ℝ) :
    Matrix.det (t • (1 : Matrix (Fin 2) (Fin 2) ℝ) - hodgeMatrix x₁ x₂ y₁ y₂) =
      (t - (x₁ ^ 2 + x₂ ^ 2)) * (t - (y₁ ^ 2 + y₂ ^ 2)) -
        (cone x₁ x₂ y₁ y₂) ^ 2
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### ResearchBridge.hodge_energy_nonnegative

Source: `extension/lean/BridgeTheorems.lean`. Verification: `extension/lean/verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Verified source signature (with reviewed section context where needed):

```lean
theorem hodge_energy_nonnegative (x₁ x₂ y₁ y₂ z₁ z₂ : ℝ) :
    0 ≤ hodgeEnergy x₁ x₂ y₁ y₂ z₁ z₂
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### ResearchBridge.hodge_energy_zero_iff

Source: `extension/lean/BridgeTheorems.lean`. Verification: `extension/lean/verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Verified source signature (with reviewed section context where needed):

```lean
theorem hodge_energy_zero_iff (x₁ x₂ y₁ y₂ z₁ z₂ : ℝ) :
    hodgeEnergy x₁ x₂ y₁ y₂ z₁ z₂ = 0 ↔
      x₁ * z₁ + x₂ * z₂ = 0 ∧ y₁ * z₁ + y₂ * z₂ = 0
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### ResearchBridge.hodge_family_arbitrarily_small_energy

Source: `extension/lean/BridgeTheorems.lean`. Verification: `extension/lean/verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Verified source signature (with reviewed section context where needed):

```lean
theorem hodge_family_arbitrarily_small_energy (ε : ℝ) (hε : 0 < ε) :
    ∃ t : ℝ, 0 < t ∧ cone t 0 0 1 = 0 ∧
      hodgeEnergy t 0 0 1 1 0 < ε
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### ResearchBridge.hodge_family_diagonal

Source: `extension/lean/BridgeTheorems.lean`. Verification: `extension/lean/verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Verified source signature (with reviewed section context where needed):

```lean
theorem hodge_family_diagonal (t : ℝ) :
    hodgeMatrix t 0 0 1 = !![t ^ 2, 0; 0, 1]
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### ResearchBridge.hodge_positive_semidefinite

Source: `extension/lean/BridgeTheorems.lean`. Verification: `extension/lean/verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Verified source signature (with reviewed section context where needed):

```lean
theorem hodge_positive_semidefinite {m n p : Type*}
    [Fintype m] [Fintype n] [Fintype p]
    (A : Matrix n m ℝ) (B : Matrix p n ℝ) :
    (A * Aᴴ + Bᴴ * B).PosSemidef
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### ResearchBridge.hodge_quadratic_identity

Source: `extension/lean/BridgeTheorems.lean`. Verification: `extension/lean/verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Verified source signature (with reviewed section context where needed):

```lean
theorem hodge_quadratic_identity (x₁ x₂ y₁ y₂ z₁ z₂ : ℝ) :
    ![z₁, z₂] ⬝ᵥ (hodgeMatrix x₁ x₂ y₁ y₂ *ᵥ ![z₁, z₂]) =
      hodgeEnergy x₁ x₂ y₁ y₂ z₁ z₂
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### ResearchBridge.koszul_zero_composite

Source: `extension/lean/BridgeTheorems.lean`. Verification: `extension/lean/verification.json`.

Reported foundational dependencies: `Quot.sound`, `propext`.

Verified source signature (with reviewed section context where needed):

```lean
variable {R : Type*} [CommRing R]
theorem koszul_zero_composite (x y c : R) : x * (-y * c) + y * (x * c) = 0
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### ResearchBridge.middle_exact_iff_rank_sum

Source: `extension/lean/BridgeTheorems.lean`. Verification: `extension/lean/verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Verified source signature (with reviewed section context where needed):

```lean
variable {K V₀ V₁ V₂ : Type*} [Field K]
variable [AddCommGroup V₀] [AddCommGroup V₁] [AddCommGroup V₂]
variable [Module K V₀] [Module K V₁] [Module K V₂]
theorem middle_exact_iff_rank_sum [FiniteDimensional K V₁]
    (A : V₀ →ₗ[K] V₁) (B : V₁ →ₗ[K] V₂) (h : B.comp A = 0) :
    LinearMap.range A = LinearMap.ker B ↔
      Module.finrank K (LinearMap.range A) + Module.finrank K (LinearMap.range B)
        = Module.finrank K V₁
```

- **complexes.011** (): Middle exactness iff equality in the adjacent-rank bound, assuming BA=0.

### ResearchBridge.noise_cancellation

Source: `extension/lean/BridgeTheorems.lean`. Verification: `extension/lean/verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Verified source signature (with reviewed section context where needed):

```lean
theorem noise_cancellation {R m n : Type*} [CommRing R]
    [Fintype m] [Fintype n]
    (A : Matrix m n R) (s : n → R) (e r : m → R) (μ : R) :
    (((A *ᵥ s + e) ⬝ᵥ r) + μ) - (s ⬝ᵥ (Aᵀ *ᵥ r)) =
      e ⬝ᵥ r + μ
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### ResearchBridge.shear_determinant_one

Source: `extension/lean/BridgeTheorems.lean`. Verification: `extension/lean/verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Verified source signature (with reviewed section context where needed):

```lean
theorem shear_determinant_one (n : ℤ) : Matrix.det (shear n) = 1
```

- **cryptography.006** (): The displayed integer shear has determinant one.

### ResearchBridge.shear_e2_image

Source: `extension/lean/BridgeTheorems.lean`. Verification: `extension/lean/verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Verified source signature (with reviewed section context where needed):

```lean
theorem shear_e2_image (n : ℤ) : shear n *ᵥ ![0, 1] = ![n, 1]
```

- **cryptography.006** (): The shear sends the second basis vector to (N,1).

### ResearchBridge.shear_e2_norm_squared

Source: `extension/lean/BridgeTheorems.lean`. Verification: `extension/lean/verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Verified source signature (with reviewed section context where needed):

```lean
theorem shear_e2_norm_squared (n : ℤ) :
    ((shear n *ᵥ ![0, 1]) 0 : ℝ) ^ 2 +
      ((shear n *ᵥ ![0, 1]) 1 : ℝ) ^ 2 = (n : ℝ) ^ 2 + 1
```

- **cryptography.006** (): The real squared-coordinate length of that image is N^2+1; the square-root and unbounded-operator-norm conclusion are not formalized here.

### ResearchBridge.shear_inverse

Source: `extension/lean/BridgeTheorems.lean`. Verification: `extension/lean/verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Verified source signature (with reviewed section context where needed):

```lean
theorem shear_inverse (n : ℤ) : shear n * shear (-n) = 1
```

- **cryptography.006** (): The displayed shear multiplied by the opposite shear is the identity.

### ResearchQuantum.binarySign_add

Source: `extension/lean/QuantumInterfaces.lean`. Verification: `extension/lean/quantum-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
ResearchQuantum.binarySign_add.{u_1} {R : Type u_1} [CommRing R] (a b : ZMod 2) :
  ResearchQuantum.binarySign (a + b) = ResearchQuantum.binarySign a * ResearchQuantum.binarySign b
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### ResearchQuantum.boundary_phase_shift_commute

Source: `extension/lean/QuantumInterfaces.lean`. Verification: `extension/lean/quantum-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
ResearchQuantum.boundary_phase_shift_commute.{u_1, u_2, u_3, u_4} {R : Type u_1} {C0 : Type u_2} {C1 : Type u_3}
  {C2 : Type u_4} [CommRing R] [AddCommGroup C0] [AddCommGroup C1] [AddCommGroup C2] [Module (ZMod 2) C0]
  [Module (ZMod 2) C1] [Module (ZMod 2) C2] (d1 : C1 →ₗ[ZMod 2] C0) (d2 : C2 →ₗ[ZMod 2] C1) (hcomplex : d1 ∘ₗ d2 = 0)
  (ell : C0 →ₗ[ZMod 2] ZMod 2) (f : C2) (psi : C1 → R) :
  ResearchQuantum.bitShift (d2 f) (ResearchQuantum.parityPhase (ell ∘ₗ d1) psi) =
    ResearchQuantum.parityPhase (ell ∘ₗ d1) (ResearchQuantum.bitShift (d2 f) psi)
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### ResearchQuantum.euler_surface_rank_substitution

Source: `extension/lean/QuantumInterfaces.lean`. Verification: `extension/lean/quantum-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
ResearchQuantum.euler_surface_rank_substitution (V E F g : ℤ) (hEuler : V - E + F = 2 - 2 * g) :
  E - (V - 1) - (F - 1) = 2 * g
```

- **quantum-surfaces.004** (): The integer substitution E-(V-1)-(F-1)=2g, assuming V-E+F=2-2g; the surface and stabilizer rank hypotheses are not proved by this declaration.

### ResearchQuantum.pauliX_square

Source: `extension/lean/QuantumInterfaces.lean`. Verification: `extension/lean/quantum-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
ResearchQuantum.pauliX_square : ResearchQuantum.pauliX * ResearchQuantum.pauliX = 1
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### ResearchQuantum.pauliZ_square

Source: `extension/lean/QuantumInterfaces.lean`. Verification: `extension/lean/quantum-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
ResearchQuantum.pauliZ_square : ResearchQuantum.pauliZ * ResearchQuantum.pauliZ = 1
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### ResearchQuantum.pauli_anticommutation

Source: `extension/lean/QuantumInterfaces.lean`. Verification: `extension/lean/quantum-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
ResearchQuantum.pauli_anticommutation :
  ResearchQuantum.pauliX * ResearchQuantum.pauliZ = -(ResearchQuantum.pauliZ * ResearchQuantum.pauliX)
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.

### ResearchQuantum.shift_phase_commutation

Source: `extension/lean/QuantumInterfaces.lean`. Verification: `extension/lean/quantum-verification.json`.

Reported foundational dependencies: `Classical.choice`, `Quot.sound`, `propext`.

Elaborated type:

```lean
ResearchQuantum.shift_phase_commutation.{u_1, u_2} {R : Type u_1} {C : Type u_2} [CommRing R] [AddCommGroup C]
  [Module (ZMod 2) C] (a : C) (ell : C →ₗ[ZMod 2] ZMod 2) (psi : C → R) :
  ResearchQuantum.bitShift a (ResearchQuantum.parityPhase ell psi) = fun v =>
    ResearchQuantum.binarySign (ell a) * ResearchQuantum.parityPhase ell (ResearchQuantum.bitShift a psi) v
```

No manuscript environment is assigned to this declaration. Its own precise type remains verified; no broader claim is inferred.
