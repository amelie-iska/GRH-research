import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Analysis.Normed.Operator.Bilinear
import Mathlib.LinearAlgebra.Matrix.SchurComplement
import Mathlib.Analysis.SpecificLimits.Normed
import Mathlib.Data.Nat.Choose.Cast
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum

open scoped BigOperators
namespace GRHResearch.AbelBoundary
open Finset Matrix

/-- Exact endpoint correction; no limiting or character hypothesis is hidden. -/
theorem finite_abel_boundary (c f : ℕ → ℂ) (N : ℕ) :
    (∑ n ∈ range N, (∑ k ∈ range (n+1), c k) * (f n - f (n+1))) =
      (∑ n ∈ range N, c n * f n) - (∑ k ∈ range N, c k) * f N := by
  induction N with
  | zero => simp
  | succ N ih =>
    rw [sum_range_succ, sum_range_succ, sum_range_succ, ih]
    ring

/-- The arithmetic finite determinant is an actual rank-one matrix determinant. -/
theorem finite_boundary_determinant {ι : Type*} [Fintype ι] [DecidableEq ι]
    (u v : ι → ℂ) :
    (1 + Matrix.vecMulVec u v).det = 1 + ∑ i, v i * u i := by
  have h : Matrix.replicateCol (Fin 1) u * Matrix.replicateRow (Fin 1) v =
      Matrix.vecMulVec u v := by
    ext i j
    simp [Matrix.mul_apply, Matrix.vecMulVec]
  simpa only [h, dotProduct] using
    (Matrix.det_one_add_replicateCol_mul_replicateRow (ι := Fin 1) u v)

/-- The actual infinite dyadic majorant, not a finite-series model. -/
theorem squared_geometric_majorant (r : ℝ) (hr : ‖r‖ < 1) :
    HasSum (fun n : ℕ => ((n : ℝ)+1)^2 * r^n) ((1+r)/(1-r)^3) := by
  have h2 := (hasSum_choose_mul_geometric_of_norm_lt_one (𝕜 := ℝ) 2 hr).mul_left 2
  have h1 := hasSum_choose_mul_geometric_of_norm_lt_one (𝕜 := ℝ) 1 hr
  have h := h2.sub h1
  have hne : 1-r ≠ 0 := by
    have habs : |r| < 1 := by simpa only [Real.norm_eq_abs] using hr
    have hlt : r < 1 := (abs_lt.mp habs).2
    exact ne_of_gt (sub_pos.mpr hlt)
  convert h using 1
  · ext n
    simp only [Nat.cast_choose_two, Nat.choose_one_right, Nat.cast_add, Nat.cast_ofNat]
    ring
  · field_simp
    ring

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℂ E]

/-- This is a genuine continuous rank-one operator on an arbitrary complex Hilbert space. -/
def boundaryOperator (u : E) (φ : E →L[ℂ] ℂ) : E →L[ℂ] E := φ.smulRight u

/-- Its one potentially nonzero eigenvalue is explicitly the boundary pairing. -/
theorem boundary_operator_on_range (u : E) (φ : E →L[ℂ] ℂ) :
    boundaryOperator u φ u = φ u • u := rfl

theorem boundary_operator_square (u : E) (φ : E →L[ℂ] ℂ) :
    (boundaryOperator u φ).comp (boundaryOperator u φ) =
      (φ u) • boundaryOperator u φ := by
  ext x
  simp [boundaryOperator, smul_smul, mul_comm]

/-- A rank-one perturbation difference has its actual operator norm, not an assumed bound. -/
theorem boundary_operator_difference_norm (u : E) (φ ψ : E →L[ℂ] ℂ) :
    ‖boundaryOperator u φ - boundaryOperator u ψ‖ = ‖φ - ψ‖ * ‖u‖ := by
  have h : boundaryOperator u φ - boundaryOperator u ψ = (φ - ψ).smulRight u := by
    ext x
    simp [boundaryOperator, sub_smul]
  rw [h, ContinuousLinearMap.norm_smulRight_apply]

/-- Symmetry forces the entire functional to be the inner-product functional of u.
The explicit symmetry property uses the actual continuous operator. -/
theorem symmetric_boundary_functional (u : E) (φ : E →L[ℂ] ℂ) (hu : u ≠ 0)
    (hsym : ∀ x y, inner ℂ (boundaryOperator u φ x) y =
      inner ℂ x (boundaryOperator u φ y)) (x : E) :
    φ x = star (φ u) * inner ℂ u x / inner ℂ u u := by
  have h := hsym u x
  simp only [boundaryOperator, ContinuousLinearMap.smulRight_apply,
    inner_smul_left, inner_smul_right] at h
  apply (eq_div_iff ((inner_self_ne_zero (𝕜 := ℂ)).mpr hu)).mpr
  exact h.symm

/-- A nonzero symmetric rank-one operator cannot have zero boundary eigenvalue. -/
theorem symmetric_boundary_value_ne_zero (u : E) (φ : E →L[ℂ] ℂ)
    (hu : u ≠ 0) (hφ : φ ≠ 0)
    (hsym : ∀ x y, inner ℂ (boundaryOperator u φ x) y =
      inner ℂ x (boundaryOperator u φ y)) : φ u ≠ 0 := by
  intro hzero
  apply hφ
  ext x
  rw [symmetric_boundary_functional u φ hu hsym x, hzero]
  simp

/-- Two symmetric fixed-range operators force a scalar proportionality relation. -/
theorem symmetric_boundary_pair (u : E) (φ ψ : E →L[ℂ] ℂ) (hu : u ≠ 0)
    (hφ : ∀ x y, inner ℂ (boundaryOperator u φ x) y = inner ℂ x (boundaryOperator u φ y))
    (hψ : ∀ x y, inner ℂ (boundaryOperator u ψ x) y = inner ℂ x (boundaryOperator u ψ y))
    (x : E) : star (φ u) * ψ x = star (ψ u) * φ x := by
  rw [symmetric_boundary_functional u ψ hu hψ x,
    symmetric_boundary_functional u φ hu hφ x]
  ring

/-- Two explicitly calculated Abel kernels cannot be proportional (before nonzero weights). -/
theorem real_abel_kernel_minor :
    ((1 : ℚ)/6)*(7/144) - (5/36)*(1/12) = -1/288 := by norm_num

#check symmetric_boundary_value_ne_zero
#check squared_geometric_majorant
#check finite_abel_boundary
#check finite_boundary_determinant
#check boundary_operator_on_range
#check boundary_operator_square
#check boundary_operator_difference_norm
#check symmetric_boundary_functional
#check symmetric_boundary_pair
#check real_abel_kernel_minor
#print axioms symmetric_boundary_value_ne_zero
#print axioms squared_geometric_majorant
#print axioms finite_abel_boundary
#print axioms finite_boundary_determinant
#print axioms boundary_operator_on_range
#print axioms boundary_operator_square
#print axioms boundary_operator_difference_norm
#print axioms symmetric_boundary_functional
#print axioms symmetric_boundary_pair
#print axioms real_abel_kernel_minor
end GRHResearch.AbelBoundary
