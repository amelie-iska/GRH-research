import BridgeTheorems
import FluidInterfaces

/-!
# Exact contracts for selected live laboratories

These results reuse the project's existing Hodge family and integer quadratic
order matrix. They add domain-restricted coercivity, a complete coordinate
description of the two-dimensional kernel, and positivity of every power's
determinant. A final algebraic error estimate supports the finite-resolution
discussion, without claiming its trigonometric or continuum assumptions.

The browser can replay rational instances of these statements and export
fixed-template Lean specializations. That is separate from running a Lean
kernel in the browser. Determinant positivity alone is not a formalization of
the topological covering theorem, a complete fibre enumeration, or a
continuum fluid limit.
-/

set_option autoImplicit false

namespace LaboratoryContracts

open Matrix
open scoped Matrix

/-- On the displayed domain, epsilon squared is a coercivity constant for
the actual existing Hodge energy; it is positive exactly away from zero. -/
theorem hodge_family_certificate (ε : ℝ) (hε0 : 0 ≤ ε) (hε1 : ε ≤ 1) :
    ResearchBridge.hodgeMatrix ε 0 0 1 = !![ε ^ 2, 0; 0, 1] ∧
      (∀ a b : ℝ, ε ^ 2 * (a ^ 2 + b ^ 2) ≤
        ResearchBridge.hodgeEnergy ε 0 0 1 a b) ∧
      (0 < ε ^ 2 ↔ ε ≠ 0) := by
  refine ⟨ResearchBridge.hodge_family_diagonal ε, ?_, sq_pos_iff⟩
  intro a b
  have hsq : ε ^ 2 ≤ 1 := by nlinarith
  have hbound := mul_nonneg (sub_nonneg.mpr hsq) (sq_nonneg b)
  calc
    ε ^ 2 * (a ^ 2 + b ^ 2) ≤ ε ^ 2 * a ^ 2 + b ^ 2 := by nlinarith
    _ = ResearchBridge.hodgeEnergy ε 0 0 1 a b := by
      simp [ResearchBridge.hodgeEnergy]
      ring

/-- The actual matrix kernel is the first coordinate line at epsilon zero,
and is trivial for nonzero epsilon. This is a coordinate characterization,
not a separate dimension or eigenvalue enumeration theorem. -/
theorem hodge_family_kernel (ε a b : ℝ) :
    ResearchBridge.hodgeMatrix ε 0 0 1 *ᵥ ![a, b] = 0 ↔
      ((ε = 0 ∨ a = 0) ∧ b = 0) := by
  constructor
  · intro h
    have hleft : ε ^ 2 * a = 0 := by
      simpa [ResearchBridge.hodgeMatrix, Matrix.mulVec, dotProduct, Fin.sum_univ_two,
        pow_two] using congr_fun h 0
    have hright : b = 0 := by
      simpa [ResearchBridge.hodgeMatrix, Matrix.mulVec, dotProduct, Fin.sum_univ_two]
        using congr_fun h 1
    refine ⟨?_, hright⟩
    rcases mul_eq_zero.mp hleft with hε | ha
    · exact Or.inl (by simpa using hε)
    · exact Or.inr ha
  · rintro ⟨hleft, hb⟩
    subst b
    rcases hleft with hε | ha
    · subst ε
      ext i
      fin_cases i <;> simp [ResearchBridge.hodgeMatrix, Matrix.mulVec, dotProduct,
        Fin.sum_univ_two]
    · subst a
      ext i
      fin_cases i <;> simp [ResearchBridge.hodgeMatrix, Matrix.mulVec, dotProduct,
        Fin.sum_univ_two]

/-- The existing determinant identity supplies a strictly positive exact
integer determinant for every natural power, including the identity power. -/
theorem quadratic_cover_certificate (k : ℕ) :
    Matrix.det (FluidInterfaces.renormalizationMatrix ^ k) = (14 : ℤ) ^ k ∧
      0 < Matrix.det (FluidInterfaces.renormalizationMatrix ^ k) := by
  refine ⟨FluidInterfaces.renormalization_power_determinant k, ?_⟩
  rw [FluidInterfaces.renormalization_power_determinant]
  exact pow_pos (by norm_num) k

/-- A certified additive scalar error gives an explicit error on its square.
No differentiability, discretization, or asymptotic claim is assumed here. -/
theorem square_perturbation_bound (B e d : ℝ) (he : |e| ≤ d) :
    |(B + e) ^ 2 - B ^ 2| ≤ d * (2 * |B| + d) := by
  have hd : 0 ≤ d := (abs_nonneg e).trans he
  have habs : |2 * B + e| ≤ 2 * |B| + |e| := by
    calc
      |2 * B + e| ≤ |2 * B| + |e| := abs_add_le (2 * B) e
      _ = 2 * |B| + |e| := by norm_num [abs_mul]
  calc
    |(B + e) ^ 2 - B ^ 2| = |e| * |2 * B + e| := by
      rw [← abs_mul]
      congr 1
      ring
    _ ≤ |e| * (2 * |B| + |e|) := mul_le_mul_of_nonneg_left habs (abs_nonneg e)
    _ ≤ d * (2 * |B| + d) := mul_le_mul he (add_le_add_left he _)
      (add_nonneg (mul_nonneg (by norm_num) (abs_nonneg B)) (abs_nonneg e)) hd

end LaboratoryContracts
