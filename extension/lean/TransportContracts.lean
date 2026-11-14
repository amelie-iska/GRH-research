import Mathlib.Algebra.Module.LinearMap.End
import Mathlib.Data.Real.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# Correctly ordered transport along a finite quiver path

These are finite linear-algebra statements. `holonomy` composes later
arrows on the left. `transportedResidual` transports every edge residual
through the remaining suffix of the path. Neither construction assumes
commuting arrows, invertibility, or flatness. Flatness is needed for the
closed-path residual to vanish, and is stated explicitly when used.

The rational counterexample reproduces the forward-prefix transport error
in the pinned Tropical_Quivers_of_Archs manuscript. The final inequality
records why a Lipschitz bound larger than one cannot be made contractive
merely by shrinking a positive residual damping parameter.

The final matrix witness has square zero but arbitrarily large squared
gain on an explicit unit vector. Successive Jacobian-vector products can
therefore vanish even though a one-step gain is large. No unproved
spectral-radius, singular-value, or generic convergence theorem is used.
-/

set_option autoImplicit false

namespace TransportContracts

section Path

variable {R V : Type*} [Semiring R] [AddCommGroup V] [Module R V]

/-- Product of the first n arrows, with composition in chronological order. -/
def holonomy (A : ℕ → Module.End R V) : ℕ → Module.End R V
  | 0 => 1
  | n + 1 => A n * holonomy A n

/-- Recursive form of the suffix-transported sum of edge residuals. -/
def transportedResidual (A : ℕ → Module.End R V) (x : ℕ → V) : ℕ → V
  | 0 => 0
  | n + 1 => A n (transportedResidual A x n) + (x (n + 1) - A n (x n))

theorem suffix_transport_telescope (A : ℕ → Module.End R V) (x : ℕ → V)
    (n : ℕ) : transportedResidual A x n = x n - holonomy A n (x 0) := by
  induction n with
  | zero => simp [transportedResidual, holonomy]
  | succ n ih =>
    simp only [transportedResidual, holonomy, ih, map_sub, Module.End.mul_apply]
    abel

theorem closed_path_residual (A : ℕ → Module.End R V) (x : ℕ → V)
    (n : ℕ) (hclosed : x n = x 0) :
    transportedResidual A x n = x 0 - holonomy A n (x 0) := by
  rw [suffix_transport_telescope, hclosed]

theorem flat_closed_path_zero (A : ℕ → Module.End R V) (x : ℕ → V)
    (n : ℕ) (hclosed : x n = x 0) (hflat : holonomy A n = 1) :
    transportedResidual A x n = 0 := by
  rw [closed_path_residual A x n hclosed, hflat]
  simp

theorem two_arrow_transport (A B : Module.End R V) (x y z : V) :
    B (y - A x) + (z - B y) = z - (B * A) x := by
  simp only [map_sub, Module.End.mul_apply]
  abel

/-- Only the initial vector need be fixed; full flatness is sufficient but stronger. -/
theorem fixed_vector_closed_path_zero (A : ℕ → Module.End R V) (x : ℕ → V)
    (n : ℕ) (hclosed : x n = x 0) (hfixed : holonomy A n (x 0) = x 0) :
    transportedResidual A x n = 0 := by
  rw [closed_path_residual A x n hclosed, hfixed, sub_self]

end Path

/-- The two scalar arrows have identity holonomy. -/
theorem scalar_counterexample_flat : (1 / 2 : ℚ) * 2 = 1 := by norm_num

/-- Forward prefixes nevertheless fail to telescope for x0=0, x1=1, x2=0. -/
theorem scalar_prefix_counterexample :
    (2 : ℚ) * (1 - 2 * 0) + (2 * (1 / 2)) * (0 - (1 / 2) * 1) = 3 / 2 := by
  norm_num

/-- The correct suffix convention gives zero on the same flat cycle. -/
theorem scalar_suffix_correction :
    (1 / 2 : ℚ) * (1 - 2 * 0) + (0 - (1 / 2) * 1) = 0 := by
  norm_num

theorem positive_damping_bound_not_contracting (L eta : ℝ)
    (hL : 1 ≤ L) (heta : 0 ≤ eta) :
    1 ≤ (1 - eta) + eta * L := by
  nlinarith [mul_nonneg heta (sub_nonneg.mpr hL)]

theorem expanding_scalar_damping (eta : ℝ) (heta : 0 < eta) :
    1 < (1 - eta) + eta * 2 := by linarith

/-- A zero relation cannot be represented by two trace-preserving arrows on a
space containing a normalized state. Positivity is not needed for this
obstruction, so it applies in particular to CPTP quantum channels. -/
theorem trace_preserving_composite_nonzero
    {V : Type*} [AddCommGroup V] [Module ℝ V]
    (trace : V →ₗ[ℝ] ℝ) (A B : Module.End ℝ V)
    (hA : ∀ x, trace (A x) = trace x)
    (hB : ∀ x, trace (B x) = trace x)
    (rho : V) (hnormalized : trace rho = 1) : B * A ≠ 0 := by
  intro hzero
  have h : trace ((B * A) rho) = 1 := by
    rw [Module.End.mul_apply, hB, hA, hnormalized]
  rw [hzero] at h
  simp at h

section NonnormalWitness

open Matrix
open scoped Matrix

/-- A nilpotent real shear with explicit, unbounded one-step amplification. -/
def nonnormalShear (M : ℝ) : Matrix (Fin 2) (Fin 2) ℝ := !![0, M; 0, 0]

theorem nonnormal_shear_square_zero (M : ℝ) :
    nonnormalShear M * nonnormalShear M = 0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [nonnormalShear, Matrix.mul_apply, Fin.sum_univ_two]

/-- The input vector (0,1) has Euclidean norm one. -/
theorem nonnormal_shear_unit_image (M : ℝ) :
    nonnormalShear M *ᵥ ![0, 1] = ![M, 0] := by
  ext i
  fin_cases i <;>
    simp [nonnormalShear, Matrix.mulVec, dotProduct, Fin.sum_univ_two]

/-- Exact squared Euclidean gain, expressed in coordinates to avoid any
implicit operator-norm or singular-value assumption. -/
theorem nonnormal_shear_gain_squared (M : ℝ) :
    ((nonnormalShear M *ᵥ ![0, 1]) 0) ^ 2 +
      ((nonnormalShear M *ᵥ ![0, 1]) 1) ^ 2 = M ^ 2 := by
  rw [nonnormal_shear_unit_image]
  simp

theorem nonnormal_shear_strict_gain (M : ℝ) (hM : 1 < M) :
    1 < ((nonnormalShear M *ᵥ ![0, 1]) 0) ^ 2 +
      ((nonnormalShear M *ᵥ ![0, 1]) 1) ^ 2 := by
  rw [nonnormal_shear_gain_squared]
  nlinarith

/-- A second Jacobian-vector product is zero despite the first-step gain. -/
theorem nonnormal_shear_second_jvp_zero (M : ℝ) (v : Fin 2 → ℝ) :
    nonnormalShear M *ᵥ (nonnormalShear M *ᵥ v) = 0 := by
  rw [Matrix.mulVec_mulVec, nonnormal_shear_square_zero, Matrix.zero_mulVec]

/-- The witness is genuinely nonnormal whenever its shear is nonzero. -/
theorem nonnormal_shear_not_normal (M : ℝ) (hM : M ≠ 0) :
    (nonnormalShear M)ᵀ * nonnormalShear M ≠
      nonnormalShear M * (nonnormalShear M)ᵀ := by
  intro h
  have h00 := congrArg (fun A : Matrix (Fin 2) (Fin 2) ℝ => A 0 0) h
  simp [nonnormalShear, Matrix.mul_apply, Fin.sum_univ_two] at h00
  exact hM h00

end NonnormalWitness

end TransportContracts
