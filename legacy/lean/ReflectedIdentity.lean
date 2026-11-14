import Mathlib.NumberTheory.JacobiSum.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Complex
import Mathlib.MeasureTheory.Integral.Bochner.Basic

namespace GRHResearch.Analytic

attribute [local instance] Classical.propDecidable

/-- Row columns retain the natural zero, also when the two dual factors meet. -/
theorem reflected_row_column {F : Type*} [Field F] (A : MulChar F ℂ)
    (hA : A^6 = 1) (n b : F) : (A^3) (n*b^3) = (A^3) (n*b) := by
  have hp : (A^3)^3 = A^3 := by
    rw [← pow_mul]
    calc
      A^(3*3) = A^6*A^3 := by rw [← pow_add]
      _ = A^3 := by rw [hA, one_mul]
  have hb : (A^3) (b^3) = (A^3) b := by
    rw [map_pow, ← MulChar.pow_apply' (A^3) (by decide : 3 ≠ 0), hp]
  rw [map_mul, map_mul, hb]

/-- An active mark keeps the cube-factor nonunit mask; it cannot cancel it. -/
theorem reflected_mark_column {F : Type*} [Field F] (A : MulChar F ℂ)
    (hA : A^6 = 1) (n b : F) :
    ((A⁻¹)^2) (n*b^3) = ((A⁻¹)^2) n * (if b=0 then 0 else 1) := by
  have hp : ((A⁻¹)^2)^3 = 1 := by
    rw [← pow_mul]
    norm_num
    exact hA
  rw [map_mul, map_pow, ← MulChar.pow_apply' ((A⁻¹)^2) (by decide : 3 ≠ 0), hp]
  by_cases hb : b=0
  · simp [hb, MulChar.map_zero]
  · rw [MulChar.one_apply (isUnit_iff_ne_zero.mpr hb)]
    simp [hb]

/-- Removing this mask changes an actual character value from zero to one. -/
theorem reflected_mark_mask_witness {F : Type*} [Field F] (A : MulChar F ℂ) :
    ((A⁻¹)^2) ((1:F)*0^3) = 0 ∧ ((A⁻¹)^2) (1:F) = 1 := by
  simp [MulChar.map_zero, MulChar.map_one]

/-- The j=4 Ramanujan divisibility split never deletes the shared cube part. -/
theorem reflected_ramanujan_partition {F : Type*} [Field F] (n b : F) :
    (if n*b^3=0 then (1:ℂ) else 0) =
      (if n=0 then 1 else 0)+(if n=0 then 0 else 1)*(if b=0 then 1 else 0) := by
  by_cases hn : n=0 <;> by_cases hb : b=0 <;> simp [hn, hb]

/-- A unit at an active prime permits the exact cross-prime exponent extraction. -/
theorem reflected_unit_cross_phase (z w : ℂˣ) (j : ℤ) :
    z^(-2:ℤ)*(w*z^(-2:ℤ))^(-(j+2)) = w^(-(j+2))*z^(2*j+2) := by
  rw [mul_zpow]
  rw [mul_left_comm, ← zpow_mul, ← zpow_add]
  congr 1
  congr 1
  ring

/-- The only reciprocity input here is equality of the two cubic symbols. -/
theorem reflected_pair_phase (a b : ℂ) (hcubic : a^2=b^2) (j k : ℕ) :
    a^(2*j+2)*b^(2*k+2) = (a^2)^(j+k+2) := by
  calc
    a^(2*j+2)*b^(2*k+2) = (a^2)^(j+1)*(b^2)^(k+1) := by
      rw [← pow_mul, ← pow_mul]
      congr 1
    _ = (a^2)^(j+k+2) := by rw [← hcubic, ← pow_add]; congr 1; omega

theorem reflected_row_mark_phase (a b : ℂ) (hsextic : a^6=1)
    (hcubic : a^2=b^2) : a^4*b^2=1 := by
  rw [← hcubic, ← pow_add]
  exact hsextic

theorem reflected_moving_j4_phase (a b : ℂ) (hsextic : a^6=1)
    (hcubic : a^2=b^2) : a^4*b^10=a^2 := by
  rw [reflected_pair_phase a b hcubic 1 4]
  calc
    (a^2)^(1+4+2) = (a^6)^2*a^2 := by ring
    _ = a^2 := by rw [hsextic]; ring

/-- The extracted profile scalar occurs once before the common vector norm.
The source Fourier representation and its integrability still require proof. -/
theorem reflected_common_density {T E : Type*} [MeasurableSpace T]
    [NormedAddCommGroup E] [NormedSpace ℂ E] [CompleteSpace E]
    (μ : MeasureTheory.Measure T) (φ : T → ℂ) (B : T → E) (c : ℂ)
    (hB : MeasureTheory.Integrable (fun t => φ t • B t) μ) :
    ‖∫ t, (c*φ t) • B t ∂μ‖ ≤ ‖c‖ * ∫ t, ‖φ t‖*‖B t‖ ∂μ := by
  have hscalar : (∫ t, (c*φ t) • B t ∂μ) = c • ∫ t, φ t • B t ∂μ := by
    simpa [mul_smul] using hB.integral_smul c
  rw [hscalar, norm_smul]
  apply mul_le_mul_of_nonneg_left _ (norm_nonneg c)
  simpa only [norm_smul] using MeasureTheory.norm_integral_le_integral_norm (fun t => φ t • B t)

#print axioms reflected_row_column
#print axioms reflected_mark_column
#print axioms reflected_mark_mask_witness
#print axioms reflected_ramanujan_partition
#print axioms reflected_unit_cross_phase
#print axioms reflected_pair_phase
#print axioms reflected_row_mark_phase
#print axioms reflected_moving_j4_phase
#print axioms reflected_common_density
end GRHResearch.Analytic
