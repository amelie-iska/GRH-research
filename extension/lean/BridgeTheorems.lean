import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FinCases

/-!
# Selected exact interfaces for the research monograph

These declarations formalize elementary statements used in the exposition. They
do not formalize the Buchsbaum–Eisenbud acyclicity theorem, Atiyah–Singer theorem,
Shor's quantum circuit, an LWE security reduction, or quantum Yang–Mills theory.

The scalar cone models complexes of dimension vector (1,2,1). The finite matrix
Laplacian is the middle Hodge Laplacian. The ZMod computation is the algebra of a
cyclic hidden subgroup, and the cancellation identity is only the correctness
algebra of a linear encryption template. No security claim follows from it.

Each named theorem is followed by `#print axioms` in the final audit block.
-/

set_option autoImplicit false

open Matrix
open scoped Matrix ComplexOrder

namespace ResearchBridge

section LinearComplex

variable {K V₀ V₁ V₂ : Type*} [Field K]
variable [AddCommGroup V₀] [AddCommGroup V₁] [AddCommGroup V₂]
variable [Module K V₀] [Module K V₁] [Module K V₂]

/-- A zero composite puts the incoming image inside the outgoing kernel. -/
theorem complex_range_le_kernel (A : V₀ →ₗ[K] V₁) (B : V₁ →ₗ[K] V₂)
    (h : B.comp A = 0) : LinearMap.range A ≤ LinearMap.ker B :=
  LinearMap.range_le_ker_iff.mpr h

/-- The adjacent ranks of a finite-dimensional complex cannot exceed the
dimension of the middle vector space. -/
theorem complex_rank_bound [FiniteDimensional K V₁]
    (A : V₀ →ₗ[K] V₁) (B : V₁ →ₗ[K] V₂) (h : B.comp A = 0) :
    Module.finrank K (LinearMap.range A) + Module.finrank K (LinearMap.range B)
      ≤ Module.finrank K V₁ := by
  have hr := Submodule.finrank_mono (complex_range_le_kernel A B h)
  have hn := B.finrank_range_add_finrank_ker
  omega

/-- With the complex condition already present, middle exactness is equivalent
to equality in the rank bound. -/
theorem middle_exact_iff_rank_sum [FiniteDimensional K V₁]
    (A : V₀ →ₗ[K] V₁) (B : V₁ →ₗ[K] V₂) (h : B.comp A = 0) :
    LinearMap.range A = LinearMap.ker B ↔
      Module.finrank K (LinearMap.range A) + Module.finrank K (LinearMap.range B)
        = Module.finrank K V₁ := by
  have hn := B.finrank_range_add_finrank_ker
  constructor
  · intro he
    rw [he]
    omega
  · intro he
    apply Submodule.eq_of_le_of_finrank_eq (complex_range_le_kernel A B h)
    omega

end LinearComplex

/-- Once the cohomology dimensions are expressed as a-r, b-r-s, c-s,
their alternating sum is independent of the ranks. Signed integers avoid
silently using truncated subtraction. -/
theorem euler_rank_identity (a b c r s : ℤ) :
    (a - r) - (b - r - s) + (c - s) = a - b + c := by
  ring

section Cone

variable {R : Type*} [CommRing R]

/-- The (1,2,1) complex equation in four scalar coordinates. -/
def cone (x₁ x₂ y₁ y₂ : R) : R := x₁ * y₁ + x₂ * y₂

/-- The exact polynomial expansion, including its quadratic remainder. -/
theorem cone_perturbation (x₁ x₂ y₁ y₂ u₁ u₂ v₁ v₂ t : R) :
    cone (x₁ + t * u₁) (x₂ + t * u₂) (y₁ + t * v₁) (y₂ + t * v₂) =
      cone x₁ x₂ y₁ y₂ +
        t * (y₁ * u₁ + y₂ * u₂ + v₁ * x₁ + v₂ * x₂) +
        t ^ 2 * cone u₁ u₂ v₁ v₂ := by
  simp only [cone]
  ring

/-- A tangent direction removes the constant and linear terms, but generally
leaves a quadratic obstruction. -/
theorem cone_tangent_second_order (x₁ x₂ y₁ y₂ u₁ u₂ v₁ v₂ t : R)
    (h₀ : cone x₁ x₂ y₁ y₂ = 0)
    (h₁ : y₁ * u₁ + y₂ * u₂ + v₁ * x₁ + v₂ * x₂ = 0) :
    cone (x₁ + t * u₁) (x₂ + t * u₂) (y₁ + t * v₁) (y₂ + t * v₂) =
      t ^ 2 * cone u₁ u₂ v₁ v₂ := by
  rw [cone_perturbation, h₀, h₁]
  ring

/-- Unnormalized sum/difference coordinates diagonalize the split quadric. -/
theorem cone_split_identity (u₁ u₂ v₁ v₂ : R) :
    cone (u₁ + v₁) (u₂ + v₂) (u₁ - v₁) (u₂ - v₂) =
      (u₁ ^ 2 + u₂ ^ 2) - (v₁ ^ 2 + v₂ ^ 2) := by
  simp only [cone]
  ring

/-- This is the equal-radius equation underlying the torus link. The
topological assertion that the link is a torus is not formalized here. -/
theorem cone_equal_norm_iff (u₁ u₂ v₁ v₂ : R) :
    cone (u₁ + v₁) (u₂ + v₂) (u₁ - v₁) (u₂ - v₂) = 0 ↔
      u₁ ^ 2 + u₂ ^ 2 = v₁ ^ 2 + v₂ ^ 2 := by
  rw [cone_split_identity, sub_eq_zero]

/-- The two-generator Koszul maps compose to zero over any commutative ring.
Exactness requires additional regular-sequence assumptions. -/
theorem koszul_zero_composite (x y c : R) : x * (-y * c) + y * (x * c) = 0 := by
  ring

end Cone

section Hodge

/-- Middle Hodge matrix for A=(x₁,x₂)ᵀ and B=(y₁,y₂). -/
def hodgeMatrix (x₁ x₂ y₁ y₂ : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![x₁ ^ 2 + y₁ ^ 2, x₁ * x₂ + y₁ * y₂;
     x₁ * x₂ + y₁ * y₂, x₂ ^ 2 + y₂ ^ 2]

def hodgeEnergy (x₁ x₂ y₁ y₂ z₁ z₂ : ℝ) : ℝ :=
  (x₁ * z₁ + x₂ * z₂) ^ 2 + (y₁ * z₁ + y₂ * z₂) ^ 2

/-- Every finite Hodge matrix is positive semidefinite. The complex condition
BA=0 is not needed for this particular conclusion. -/
theorem hodge_positive_semidefinite {m n p : Type*}
    [Fintype m] [Fintype n] [Fintype p]
    (A : Matrix n m ℝ) (B : Matrix p n ℝ) :
    (A * Aᴴ + Bᴴ * B).PosSemidef :=
  (Matrix.posSemidef_self_mul_conjTranspose A).add
    (Matrix.posSemidef_conjTranspose_mul_self B)

/-- The middle quadratic form is the sum of the two squared differential
components, with coordinates made explicit. -/
theorem hodge_quadratic_identity (x₁ x₂ y₁ y₂ z₁ z₂ : ℝ) :
    ![z₁, z₂] ⬝ᵥ (hodgeMatrix x₁ x₂ y₁ y₂ *ᵥ ![z₁, z₂]) =
      hodgeEnergy x₁ x₂ y₁ y₂ z₁ z₂ := by
  simp [hodgeMatrix, hodgeEnergy, Matrix.mulVec, dotProduct, Fin.sum_univ_two]
  ring

theorem hodge_energy_nonnegative (x₁ x₂ y₁ y₂ z₁ z₂ : ℝ) :
    0 ≤ hodgeEnergy x₁ x₂ y₁ y₂ z₁ z₂ := by
  exact add_nonneg (sq_nonneg _) (sq_nonneg _)

/-- Zero energy means both differential components vanish. -/
theorem hodge_energy_zero_iff (x₁ x₂ y₁ y₂ z₁ z₂ : ℝ) :
    hodgeEnergy x₁ x₂ y₁ y₂ z₁ z₂ = 0 ↔
      x₁ * z₁ + x₂ * z₂ = 0 ∧ y₁ * z₁ + y₂ * z₂ = 0 := by
  constructor
  · intro h
    unfold hodgeEnergy at h
    have hx := sq_nonneg (x₁ * z₁ + x₂ * z₂)
    have hy := sq_nonneg (y₁ * z₁ + y₂ * z₂)
    constructor <;> nlinarith
  · rintro ⟨hx, hy⟩
    simp [hodgeEnergy, hx, hy]

/-- The characteristic determinant includes the squared complex defect. -/
theorem hodge_characteristic_identity (x₁ x₂ y₁ y₂ t : ℝ) :
    Matrix.det (t • (1 : Matrix (Fin 2) (Fin 2) ℝ) - hodgeMatrix x₁ x₂ y₁ y₂) =
      (t - (x₁ ^ 2 + x₂ ^ 2)) * (t - (y₁ ^ 2 + y₂ ^ 2)) -
        (cone x₁ x₂ y₁ y₂) ^ 2 := by
  simp [Matrix.det_fin_two, hodgeMatrix, cone]
  ring

/-- On the variety of complexes, the middle characteristic determinant
factors into the two squared-length eigenvalue factors. -/
theorem hodge_characteristic_factor (x₁ x₂ y₁ y₂ t : ℝ)
    (h : cone x₁ x₂ y₁ y₂ = 0) :
    Matrix.det (t • (1 : Matrix (Fin 2) (Fin 2) ℝ) - hodgeMatrix x₁ x₂ y₁ y₂) =
      (t - (x₁ ^ 2 + x₂ ^ 2)) * (t - (y₁ ^ 2 + y₂ ^ 2)) := by
  rw [hodge_characteristic_identity, h]
  ring

theorem hodge_family_diagonal (t : ℝ) :
    hodgeMatrix t 0 0 1 = !![t ^ 2, 0; 0, 1] := by
  simp [hodgeMatrix]

/-- Positive t keeps the two scalar maps nonzero, but the energy in a fixed
unit direction can be arbitrarily small. This is a finite-dimensional
counterexample to deriving a uniform positive energy bound from rank alone. -/
theorem hodge_family_arbitrarily_small_energy (ε : ℝ) (hε : 0 < ε) :
    ∃ t : ℝ, 0 < t ∧ cone t 0 0 1 = 0 ∧
      hodgeEnergy t 0 0 1 1 0 < ε := by
  let t : ℝ := min ε 1 / 2
  have hp : 0 < min ε 1 := lt_min hε zero_lt_one
  have h₁ : min ε 1 ≤ ε := min_le_left _ _
  have h₂ : min ε 1 ≤ 1 := min_le_right _ _
  have hsq : (min ε 1) ^ 2 ≤ min ε 1 := by
    nlinarith [mul_nonneg (le_of_lt hp) (sub_nonneg.mpr h₂)]
  refine ⟨t, by dsimp [t]; linarith, by simp [cone], ?_⟩
  simp only [hodgeEnergy, mul_one, zero_mul, add_zero, zero_add]
  dsimp [t]
  nlinarith

end Hodge

section Shear

/-- An integral basis change with determinant one. -/
def shear (n : ℤ) : Matrix (Fin 2) (Fin 2) ℤ := !![1, n; 0, 1]

theorem shear_determinant_one (n : ℤ) : Matrix.det (shear n) = 1 := by
  simp [shear, Matrix.det_fin_two]

theorem shear_inverse (n : ℤ) : shear n * shear (-n) = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [shear, Matrix.mul_apply, Fin.sum_univ_two]

theorem shear_e2_image (n : ℤ) : shear n *ᵥ ![0, 1] = ![n, 1] := by
  ext i
  fin_cases i <;> simp [shear, Matrix.mulVec, dotProduct, Fin.sum_univ_two]

/-- The squared Euclidean norm of the transformed unit basis vector grows
quadratically even though the integral determinant remains one. -/
theorem shear_e2_norm_squared (n : ℤ) :
    ((shear n *ᵥ ![0, 1]) 0 : ℝ) ^ 2 +
      ((shear n *ᵥ ![0, 1]) 1 : ℝ) ^ 2 = (n : ℝ) ^ 2 + 1 := by
  rw [shear_e2_image]
  simp

end Shear

section CyclicKernel

variable {q : ℕ}

/-- Coordinates for the additive cyclic hidden-subgroup equation. -/
def hiddenLinear (x a b : ZMod q) : ZMod q := a + x * b

theorem hidden_kernel_relation (x a b : ZMod q) :
    hiddenLinear x a b = 0 ↔ a = -(x * b) := by
  simp only [hiddenLinear, add_eq_zero_iff_eq_neg]

/-- Equal function values differ by an element of the cyclic kernel. -/
theorem hidden_collision_relation (x a b c d : ZMod q) :
    hiddenLinear x a b = hiddenLinear x c d ↔
      (a - c) + x * (b - d) = 0 := by
  constructor
  · intro h
    calc
      (a - c) + x * (b - d) = hiddenLinear x a b - hiddenLinear x c d := by
        simp only [hiddenLinear]
        ring
      _ = 0 := sub_eq_zero.mpr h
  · intro h
    apply sub_eq_zero.mp
    calc
      hiddenLinear x a b - hiddenLinear x c d = (a - c) + x * (b - d) := by
        simp only [hiddenLinear]
        ring
      _ = 0 := h

end CyclicKernel

section Noise

/-- Algebraic cancellation in a linear encryption template. This identity
holds over any commutative ring, including modular rings; correctness of
decoding additionally requires a quantitative noise bound. -/
theorem noise_cancellation {R m n : Type*} [CommRing R]
    [Fintype m] [Fintype n]
    (A : Matrix m n R) (s : n → R) (e r : m → R) (μ : R) :
    (((A *ᵥ s + e) ⬝ᵥ r) + μ) - (s ⬝ᵥ (Aᵀ *ᵥ r)) =
      e ⬝ᵥ r + μ := by
  rw [add_dotProduct, Matrix.mulVec_transpose, dotProduct_comm s,
    ← Matrix.dotProduct_mulVec, dotProduct_comm r]
  ring

/-- A concrete two-coordinate error bound for binary selector coefficients.
It is a correctness estimate, not an LWE hardness assertion. -/
theorem binary_noise_bound (e₁ e₂ r₁ r₂ E : ℝ)
    (hE : 0 ≤ E) (h₁ : |e₁| ≤ E) (h₂ : |e₂| ≤ E)
    (hr₁ : r₁ = 0 ∨ r₁ = 1) (hr₂ : r₂ = 0 ∨ r₂ = 1) :
    |e₁ * r₁ + e₂ * r₂| ≤ 2 * E := by
  rcases hr₁ with rfl | rfl <;> rcases hr₂ with rfl | rfl
  · simpa using (show 0 ≤ 2 * E by linarith)
  · simpa using (show |e₂| ≤ 2 * E by linarith)
  · simpa using (show |e₁| ≤ 2 * E by linarith)
  · simpa using (show |e₁ + e₂| ≤ 2 * E from
      le_trans (abs_add_le e₁ e₂) (by linarith))

end Noise

end ResearchBridge

-- Kernel-auditable declaration inventory. Standard foundational axioms from
-- Lean/mathlib may occur; there must be no `sorryAx` or project-specific axiom.
#print axioms ResearchBridge.complex_range_le_kernel
#print axioms ResearchBridge.complex_rank_bound
#print axioms ResearchBridge.middle_exact_iff_rank_sum
#print axioms ResearchBridge.euler_rank_identity
#print axioms ResearchBridge.cone_perturbation
#print axioms ResearchBridge.cone_tangent_second_order
#print axioms ResearchBridge.cone_split_identity
#print axioms ResearchBridge.cone_equal_norm_iff
#print axioms ResearchBridge.koszul_zero_composite
#print axioms ResearchBridge.hodge_positive_semidefinite
#print axioms ResearchBridge.hodge_quadratic_identity
#print axioms ResearchBridge.hodge_energy_nonnegative
#print axioms ResearchBridge.hodge_energy_zero_iff
#print axioms ResearchBridge.hodge_characteristic_identity
#print axioms ResearchBridge.hodge_characteristic_factor
#print axioms ResearchBridge.hodge_family_diagonal
#print axioms ResearchBridge.hodge_family_arbitrarily_small_energy
#print axioms ResearchBridge.shear_determinant_one
#print axioms ResearchBridge.shear_inverse
#print axioms ResearchBridge.shear_e2_image
#print axioms ResearchBridge.shear_e2_norm_squared
#print axioms ResearchBridge.hidden_kernel_relation
#print axioms ResearchBridge.hidden_collision_relation
#print axioms ResearchBridge.noise_cancellation
#print axioms ResearchBridge.binary_noise_bound
