import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Algebra.Module.LinearMap.End
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
# Finite fluid and information-reduction interfaces

The matrix results below concern actual finite real matrices, not a continuum
existence or regularity theorem. In particular, an energy identity for every
finite discretization supplies no mesh-uniform derivative or compactness bound.
Skew transport, positive factorized closures, orthogonal projection, and chain
complexes provide independently checkable structural constraints for a fluid
model on a surface cellulation. A learned closure may depend on the current
state: the corresponding matrix identities apply pointwise at that state.

The block-elimination and memory results describe exact finite linear reduction.
They do not identify its memory kernel with the nonlinear Navier--Stokes one,
and do not assert that an instantaneous closure is exact.

This file adds selected mathematical interfaces to the existing formalization.
It does not reprove or import the OpenAI Navier--Stokes release.
-/

set_option autoImplicit false

open Matrix
open scoped BigOperators Matrix

namespace FluidInterfaces

section Energy

variable {n m p : Type*} [Fintype n] [Fintype m] [Fintype p]

/-- Finite Euclidean kinetic energy with unit mass matrix. -/
noncomputable def kineticEnergy (u : n → ℝ) : ℝ := (u ⬝ᵥ u) / 2

theorem dot_self_nonneg (u : n → ℝ) : 0 ≤ u ⬝ᵥ u := by
  exact Finset.sum_nonneg (fun i _ => mul_self_nonneg (u i))

theorem kineticEnergy_nonneg (u : n → ℝ) : 0 ≤ kineticEnergy u :=
  div_nonneg (dot_self_nonneg u) (by norm_num)

/-- The transpose identity is valid also for rectangular finite matrices. -/
theorem transpose_work (L : Matrix m n ℝ) (u : n → ℝ) (v : m → ℝ) :
    u ⬝ᵥ (Lᵀ *ᵥ v) = (L *ᵥ u) ⬝ᵥ v := by
  rw [dotProduct_mulVec, vecMul_transpose]

/-- Actual matrix skew-symmetry implies exactly zero quadratic work. -/
theorem skew_transport_work (J : Matrix n n ℝ) (hJ : Jᵀ = -J)
    (u : n → ℝ) : u ⬝ᵥ (J *ᵥ u) = 0 := by
  have h := transpose_work J u u
  rw [hJ, neg_mulVec, dotProduct_neg, dotProduct_comm (J *ᵥ u) u] at h
  linarith

/-- A factorized dissipative closure has exactly squared-flux work. -/
theorem factorized_viscosity_work (L : Matrix m n ℝ) (u : n → ℝ) :
    u ⬝ᵥ ((Lᵀ * L) *ᵥ u) = (L *ᵥ u) ⬝ᵥ (L *ᵥ u) := by
  rw [← mulVec_mulVec, transpose_work]

theorem factorized_viscosity_nonneg (L : Matrix m n ℝ) (u : n → ℝ) :
    0 ≤ u ⬝ᵥ ((Lᵀ * L) *ᵥ u) := by
  rw [factorized_viscosity_work]
  exact dot_self_nonneg _

/-- Discrete gradient pressure does no work on a divergence-free velocity. -/
theorem pressure_work_zero (B : Matrix p n ℝ) (u : n → ℝ) (pressure : p → ℝ)
    (hu : B *ᵥ u = 0) : u ⬝ᵥ (Bᵀ *ᵥ pressure) = 0 := by
  rw [transpose_work, hu, zero_dotProduct]

/-- Exact finite energy-work balance including pressure, physical viscosity,
and a separately factorized learned closure. No continuum limit is asserted. -/
theorem finite_fluid_work_identity
    (J : Matrix n n ℝ) (hJ : Jᵀ = -J)
    (D : Matrix m n ℝ) (L : Matrix p n ℝ) (ν : ℝ)
    (u force : n → ℝ) :
    u ⬝ᵥ (J *ᵥ u - ν • ((Dᵀ * D) *ᵥ u) - (Lᵀ * L) *ᵥ u + force) =
      u ⬝ᵥ force - ν * ((D *ᵥ u) ⬝ᵥ (D *ᵥ u)) -
        (L *ᵥ u) ⬝ᵥ (L *ᵥ u) := by
  rw [dotProduct_add, dotProduct_sub, dotProduct_sub,
    skew_transport_work J hJ, dotProduct_smul,
    factorized_viscosity_work, factorized_viscosity_work]
  simp only [smul_eq_mul]
  ring

theorem unforced_work_nonpositive
    (J : Matrix n n ℝ) (hJ : Jᵀ = -J)
    (D : Matrix m n ℝ) (L : Matrix p n ℝ) (ν : ℝ) (hν : 0 ≤ ν)
    (u : n → ℝ) :
    u ⬝ᵥ (J *ᵥ u - ν • ((Dᵀ * D) *ᵥ u) - (Lᵀ * L) *ᵥ u) ≤ 0 := by
  have h := finite_fluid_work_identity J hJ D L ν u 0
  simp only [add_zero, dotProduct_zero] at h
  rw [h]
  have hv := mul_nonneg hν (dot_self_nonneg (D *ᵥ u))
  have hl := dot_self_nonneg (L *ᵥ u)
  linarith

/-- This is an actual time derivative, proved from the coordinate derivatives. -/
theorem kinetic_energy_derivative (u : ℝ → n → ℝ) (v : n → ℝ) (t : ℝ)
    (hu : ∀ i, HasDerivAt (fun s => u s i) (v i) t) :
    HasDerivAt (fun s => kineticEnergy (u s)) ((u t) ⬝ᵥ v) t := by
  have hi : ∀ i, HasDerivAt (fun s => u s i * u s i / 2) (u t i * v i) t := by
    intro i
    convert ((hu i).mul (hu i)).div_const 2 using 1; ring
  have hs := HasDerivAt.fun_sum (u := Finset.univ) (fun i _ => hi i)
  simpa only [kineticEnergy, dotProduct, Finset.sum_div] using hs

/-- The exact semidiscrete ODE yields a genuine differential energy identity.
It remains a finite model: no uniform continuum estimate is implicit. -/
theorem finite_fluid_energy_derivative
    (J : Matrix n n ℝ) (hJ : Jᵀ = -J)
    (D : Matrix m n ℝ) (L : Matrix p n ℝ) (ν : ℝ)
    (u : ℝ → n → ℝ) (force : n → ℝ) (t : ℝ)
    (hu : ∀ i, HasDerivAt (fun s => u s i)
      ((J *ᵥ u t - ν • ((Dᵀ * D) *ᵥ u t) - (Lᵀ * L) *ᵥ u t + force) i) t) :
    HasDerivAt (fun s => kineticEnergy (u s))
      (u t ⬝ᵥ force - ν * ((D *ᵥ u t) ⬝ᵥ (D *ᵥ u t)) -
        (L *ᵥ u t) ⬝ᵥ (L *ᵥ u t)) t := by
  have h := kinetic_energy_derivative u _ t hu
  rwa [finite_fluid_work_identity J hJ D L ν (u t) force] at h

end Energy

section OrthogonalReduction

variable {n : Type*} [Fintype n]

/-- Idempotence sends the discarded part into the projector's kernel. -/
theorem projection_residual_kernel (P : Matrix n n ℝ) (hP : P * P = P)
    (u : n → ℝ) : P *ᵥ (u - P *ᵥ u) = 0 := by
  rw [mulVec_sub, mulVec_mulVec, hP, sub_self]

/-- Symmetry and idempotence imply orthogonality of retained and discarded data. -/
theorem projection_residual_orthogonal (P : Matrix n n ℝ)
    (hs : Pᵀ = P) (hi : P * P = P) (u v : n → ℝ) :
    (u - P *ᵥ u) ⬝ᵥ (P *ᵥ v) = 0 := by
  rw [← hs, transpose_work, hs, projection_residual_kernel P hi, zero_dotProduct]

/-- Exact information loss of an orthogonal linear reduction in kinetic energy. -/
theorem projection_energy_split (P : Matrix n n ℝ)
    (hs : Pᵀ = P) (hi : P * P = P) (u : n → ℝ) :
    kineticEnergy u = kineticEnergy (P *ᵥ u) + kineticEnergy (u - P *ᵥ u) := by
  have ho := projection_residual_orthogonal P hs hi u u
  simp only [sub_dotProduct] at ho
  have hc := dotProduct_comm u (P *ᵥ u)
  simp only [kineticEnergy, sub_dotProduct, dotProduct_sub]
  linarith

theorem projection_energy_nonincrease (P : Matrix n n ℝ)
    (hs : Pᵀ = P) (hi : P * P = P) (u : n → ℝ) :
    kineticEnergy (P *ᵥ u) ≤ kineticEnergy u := by
  have hsplit := projection_energy_split P hs hi u
  have hnonneg := kineticEnergy_nonneg (u - P *ᵥ u)
  linarith

/-- The same split proves optimality against every vector in the retained range. -/
theorem projection_best_approximation (P : Matrix n n ℝ)
    (hs : Pᵀ = P) (hi : P * P = P) (u v : n → ℝ) (hv : P *ᵥ v = v) :
    kineticEnergy (u - P *ᵥ u) ≤ kineticEnergy (u - v) := by
  have hsplit := projection_energy_split P hs hi (u - v)
  have hp : P *ᵥ (u - v) = P *ᵥ u - v := by rw [mulVec_sub, hv]
  have hr : u - v - (P *ᵥ u - v) = u - P *ᵥ u := by abel
  rw [hp, hr] at hsplit
  rw [hsplit]
  exact le_add_of_nonneg_left (kineticEnergy_nonneg _)

end OrthogonalReduction

section Continuity

variable {n m p : Type*} [Fintype n] [Fintype p]

/-- A flux represented by the next boundary automatically preserves divergence. -/
theorem boundary_flux_divergence_zero (B : Matrix m n ℝ) (C : Matrix n p ℝ)
    (hcomplex : B * C = 0) (q : p → ℝ) : B *ᵥ (C *ᵥ q) = 0 := by
  rw [mulVec_mulVec, hcomplex, zero_mulVec]

/-- The exact algebraic continuity constraint survives every such flux update. -/
theorem boundary_flux_update_preserves_divergence
    (B : Matrix m n ℝ) (C : Matrix n p ℝ) (hcomplex : B * C = 0)
    (u : n → ℝ) (q : p → ℝ) :
    B *ᵥ (u + C *ᵥ q) = B *ᵥ u := by
  rw [mulVec_add, boundary_flux_divergence_zero B C hcomplex, add_zero]

end Continuity

section BlockElimination

variable {K X Y : Type*} [Field K]
variable [AddCommGroup X] [Module K X] [AddCommGroup Y] [Module K Y]

/-- The exact reduced block; invertibility is an explicit analytic obstruction. -/
def schurComplement (A : X →ₗ[K] X) (B : Y →ₗ[K] X)
    (C : X →ₗ[K] Y) (D : Y ≃ₗ[K] Y) : X →ₗ[K] X :=
  A - B.comp (D.symm.toLinearMap.comp C)

/-- Eliminating the hidden variable is equivalent to the original block system,
not merely a one-way necessary condition. -/
theorem schur_elimination_iff
    (A : X →ₗ[K] X) (B : Y →ₗ[K] X)
    (C : X →ₗ[K] Y) (D : Y ≃ₗ[K] Y)
    (x : X) (y : Y) (f : X) (g : Y) :
    (A x + B y = f ∧ C x + D y = g) ↔
      (schurComplement A B C D x = f - B (D.symm g) ∧
        y = D.symm (g - C x)) := by
  have hy : C x + D y = g ↔ y = D.symm (g - C x) := by
    constructor
    · intro h
      have hd : D y = g - C x := by rw [← h]; abel
      simpa only [D.symm_apply_apply] using congrArg D.symm hd
    · intro h
      rw [h, D.apply_symm_apply]
      abel
  rw [hy]
  constructor
  · rintro ⟨hf, hy'⟩
    refine ⟨?_, hy'⟩
    rw [hy', map_sub, map_sub] at hf
    simp only [schurComplement, LinearMap.sub_apply, LinearMap.comp_apply,
      LinearEquiv.coe_coe]
    rw [← hf]
    abel
  · rintro ⟨hf, hy'⟩
    refine ⟨?_, hy'⟩
    simp only [schurComplement, LinearMap.sub_apply, LinearMap.comp_apply,
      LinearEquiv.coe_coe] at hf
    rw [hy', map_sub, map_sub]
    rw [sub_eq_iff_eq_add] at hf
    rw [hf]
    abel

end BlockElimination

section ExactMemory

variable {K X Y : Type*} [Field K]
variable [AddCommGroup X] [Module K X] [AddCommGroup Y] [Module K Y]

/-- Eliminating a hidden linear recurrence produces its entire past dependence. -/
theorem hidden_recurrence_expansion (C : X →ₗ[K] Y) (D : Module.End K Y)
    (p : ℕ → X) (q : ℕ → Y)
    (hstep : ∀ n : ℕ, q (n + 1) = D (q n) + C (p n)) (n : ℕ) :
    q n = (D ^ n) (q 0) +
      ∑ k ∈ Finset.range n, (D ^ (n - 1 - k)) (C (p k)) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [hstep, ih, map_add, map_sum, Finset.sum_range_succ]
    simp only [Nat.add_sub_cancel, Nat.sub_self, pow_zero, Module.End.one_apply]
    have hsum :
        (∑ k ∈ Finset.range n, D ((D ^ (n - 1 - k)) (C (p k)))) =
          ∑ k ∈ Finset.range n, (D ^ (n - k)) (C (p k)) := by
      apply Finset.sum_congr rfl
      intro k hk
      have hklt : k < n := Finset.mem_range.mp hk
      have he : n - k = (n - 1 - k) + 1 := by omega
      rw [he, pow_succ', Module.End.mul_apply]
    rw [hsum, pow_succ', Module.End.mul_apply]
    abel

/-- The exact reduced dynamics contains a forcing from the hidden initial state
and the finite convolution with kernel B D^j C. -/
theorem resolved_memory_identity (A : Module.End K X) (B : Y →ₗ[K] X)
    (C : X →ₗ[K] Y) (D : Module.End K Y) (p : ℕ → X) (q : ℕ → Y)
    (hp : ∀ n : ℕ, p (n + 1) = A (p n) + B (q n))
    (hq : ∀ n : ℕ, q (n + 1) = D (q n) + C (p n)) (n : ℕ) :
    p (n + 1) = A (p n) + B ((D ^ n) (q 0)) +
      ∑ k ∈ Finset.range n, B ((D ^ (n - 1 - k)) (C (p k))) := by
  rw [hp, hidden_recurrence_expansion C D p q hq n, map_add, map_sum]
  abel

/-- There need be no exact autonomous deterministic closure on retained data:
two states with the same retained coordinates can have distinct next states. -/
theorem hidden_state_prevents_autonomous_closure
    (A : Module.End K X) (B : Y →ₗ[K] X) (y : Y) (hy : B y ≠ 0) :
    ¬ ∃ F : X → X, ∀ (x : X) (z : Y), F x = A x + B z := by
  rintro ⟨F, hF⟩
  have h₀ := hF 0 0
  have hy' := hF 0 y
  simp only [map_zero, add_zero, zero_add] at h₀ hy'
  exact hy (hy'.symm.trans h₀)

end ExactMemory

section NilpotentBlocks

variable {K X Y : Type*} [Field K]
variable [AddCommGroup X] [Module K X] [AddCommGroup Y] [Module K Y]

/-- A strict lower rectangular block on the direct sum of retained spaces. -/
def lowerBlock (L : X →ₗ[K] Y) : Module.End K (X × Y) where
  toFun xy := (0, L xy.1)
  map_add' a b := by simp
  map_smul' c a := by simp

/-- Any diagonal block between two strict lower blocks leaves zero composite.
The left and right lower blocks may differ, covering a parameter derivative. -/
theorem lower_diagonal_lower_zero (L M : X →ₗ[K] Y)
    (DX : Module.End K X) (DY : Module.End K Y) :
    (lowerBlock L).comp ((DX.prodMap DY).comp (lowerBlock M)) = 0 := by
  apply LinearMap.ext
  intro xy
  change (0, L (DX 0)) = (0, 0)
  simp

end NilpotentBlocks

section QuadraticOrder

/-- The integer matrix for multiplication by sqrt(2), in a conjugate basis. -/
def quadraticGenerator : Matrix (Fin 2) (Fin 2) ℤ := !![-1, 1; 1, 1]

/-- The degree-fourteen matrix appearing in the reviewed proof's toral stage. -/
def renormalizationMatrix : Matrix (Fin 2) (Fin 2) ℤ := !![3, 1; 1, 5]

/-- An exact faithful representation of the underlying quadratic order. -/
def quadraticOrderMatrix (a b : ℤ) : Matrix (Fin 2) (Fin 2) ℤ :=
  !![a - b, b; b, a + b]

theorem renormalization_is_quadratic_order_element :
    renormalizationMatrix = quadraticOrderMatrix 4 1 := by
  decide

theorem quadratic_order_one :
    quadraticOrderMatrix 1 0 = (1 : Matrix (Fin 2) (Fin 2) ℤ) := by
  decide

theorem quadratic_order_addition (a b c d : ℤ) :
    quadraticOrderMatrix a b + quadraticOrderMatrix c d =
      quadraticOrderMatrix (a + c) (b + d) := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [quadraticOrderMatrix] <;> ring

theorem quadratic_generator_square : quadraticGenerator * quadraticGenerator =
    (2 : ℤ) • (1 : Matrix (Fin 2) (Fin 2) ℤ) := by
  decide

theorem renormalization_quadratic_identity :
    renormalizationMatrix * renormalizationMatrix - 8 • renormalizationMatrix +
      (14 : ℤ) • (1 : Matrix (Fin 2) (Fin 2) ℤ) = 0 := by
  decide

theorem renormalization_determinant : Matrix.det renormalizationMatrix = 14 := by
  norm_num [renormalizationMatrix, Matrix.det_fin_two]

theorem renormalization_power_determinant (k : ℕ) :
    Matrix.det (renormalizationMatrix ^ k) = 14 ^ k := by
  rw [Matrix.det_pow, renormalization_determinant]

theorem quadratic_order_multiplication (a b c d : ℤ) :
    quadraticOrderMatrix a b * quadraticOrderMatrix c d =
      quadraticOrderMatrix (a * c + 2 * b * d) (a * d + b * c) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [quadraticOrderMatrix, Matrix.mul_apply, Fin.sum_univ_two] <;> ring

theorem quadratic_order_determinant (a b : ℤ) :
    Matrix.det (quadraticOrderMatrix a b) = a ^ 2 - 2 * b ^ 2 := by
  simp [quadraticOrderMatrix, Matrix.det_fin_two]
  ring

theorem quadratic_order_representation_injective :
    Function.Injective (fun ab : ℤ × ℤ => quadraticOrderMatrix ab.1 ab.2) := by
  intro ab cd h
  have h₀ := congrArg (fun M : Matrix (Fin 2) (Fin 2) ℤ => M 0 0) h
  have h₁ := congrArg (fun M : Matrix (Fin 2) (Fin 2) ℤ => M 0 1) h
  change ab.1 - ab.2 = cd.1 - cd.2 at h₀
  change ab.2 = cd.2 at h₁
  apply Prod.ext
  · linarith
  · exact h₁

/-- This real toral endomorphism cannot be complex-linear for any real linear
complex structure: no commuting real matrix squares to minus the identity. -/
theorem no_commuting_complex_structure (I : Matrix (Fin 2) (Fin 2) ℝ)
    (hc : I * !![3, 1; 1, 5] = !![3, 1; 1, 5] * I) :
    I * I ≠ -(1 : Matrix (Fin 2) (Fin 2) ℝ) := by
  intro hsq
  have hc₀ := congrArg (fun M : Matrix (Fin 2) (Fin 2) ℝ => M 0 0) hc
  have hs₀ := congrArg (fun M : Matrix (Fin 2) (Fin 2) ℝ => M 0 0) hsq
  simp [Matrix.mul_apply, Fin.sum_univ_two] at hc₀ hs₀
  have hb : I 0 1 = I 1 0 := by linarith
  rw [← hb] at hs₀
  nlinarith [sq_nonneg (I 0 0), sq_nonneg (I 0 1)]

end QuadraticOrder

end FluidInterfaces

/-! Exact theorem types and trusted-kernel foundational dependency audit. -/
#check FluidInterfaces.renormalization_is_quadratic_order_element
#check FluidInterfaces.quadratic_order_one
#check FluidInterfaces.quadratic_order_addition
#check FluidInterfaces.dot_self_nonneg
#check FluidInterfaces.kineticEnergy_nonneg
#check FluidInterfaces.transpose_work
#check FluidInterfaces.skew_transport_work
#check FluidInterfaces.factorized_viscosity_work
#check FluidInterfaces.factorized_viscosity_nonneg
#check FluidInterfaces.pressure_work_zero
#check FluidInterfaces.finite_fluid_work_identity
#check FluidInterfaces.unforced_work_nonpositive
#check FluidInterfaces.kinetic_energy_derivative
#check FluidInterfaces.finite_fluid_energy_derivative
#check FluidInterfaces.projection_residual_kernel
#check FluidInterfaces.projection_residual_orthogonal
#check FluidInterfaces.projection_energy_split
#check FluidInterfaces.projection_energy_nonincrease
#check FluidInterfaces.projection_best_approximation
#check FluidInterfaces.boundary_flux_divergence_zero
#check FluidInterfaces.boundary_flux_update_preserves_divergence
#check FluidInterfaces.schur_elimination_iff
#check FluidInterfaces.hidden_recurrence_expansion
#check FluidInterfaces.resolved_memory_identity
#check FluidInterfaces.hidden_state_prevents_autonomous_closure
#check FluidInterfaces.lower_diagonal_lower_zero
#check FluidInterfaces.quadratic_generator_square
#check FluidInterfaces.renormalization_quadratic_identity
#check FluidInterfaces.renormalization_determinant
#check FluidInterfaces.renormalization_power_determinant
#check FluidInterfaces.quadratic_order_multiplication
#check FluidInterfaces.quadratic_order_determinant
#check FluidInterfaces.quadratic_order_representation_injective
#check FluidInterfaces.no_commuting_complex_structure

#print axioms FluidInterfaces.renormalization_is_quadratic_order_element
#print axioms FluidInterfaces.quadratic_order_one
#print axioms FluidInterfaces.quadratic_order_addition
#print axioms FluidInterfaces.dot_self_nonneg
#print axioms FluidInterfaces.kineticEnergy_nonneg
#print axioms FluidInterfaces.transpose_work
#print axioms FluidInterfaces.skew_transport_work
#print axioms FluidInterfaces.factorized_viscosity_work
#print axioms FluidInterfaces.factorized_viscosity_nonneg
#print axioms FluidInterfaces.pressure_work_zero
#print axioms FluidInterfaces.finite_fluid_work_identity
#print axioms FluidInterfaces.unforced_work_nonpositive
#print axioms FluidInterfaces.kinetic_energy_derivative
#print axioms FluidInterfaces.finite_fluid_energy_derivative
#print axioms FluidInterfaces.projection_residual_kernel
#print axioms FluidInterfaces.projection_residual_orthogonal
#print axioms FluidInterfaces.projection_energy_split
#print axioms FluidInterfaces.projection_energy_nonincrease
#print axioms FluidInterfaces.projection_best_approximation
#print axioms FluidInterfaces.boundary_flux_divergence_zero
#print axioms FluidInterfaces.boundary_flux_update_preserves_divergence
#print axioms FluidInterfaces.schur_elimination_iff
#print axioms FluidInterfaces.hidden_recurrence_expansion
#print axioms FluidInterfaces.resolved_memory_identity
#print axioms FluidInterfaces.hidden_state_prevents_autonomous_closure
#print axioms FluidInterfaces.lower_diagonal_lower_zero
#print axioms FluidInterfaces.quadratic_generator_square
#print axioms FluidInterfaces.renormalization_quadratic_identity
#print axioms FluidInterfaces.renormalization_determinant
#print axioms FluidInterfaces.renormalization_power_determinant
#print axioms FluidInterfaces.quadratic_order_multiplication
#print axioms FluidInterfaces.quadratic_order_determinant
#print axioms FluidInterfaces.quadratic_order_representation_injective
#print axioms FluidInterfaces.no_commuting_complex_structure
