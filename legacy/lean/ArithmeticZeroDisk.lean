import Mathlib.Analysis.SpecialFunctions.Pow.Complex

open Complex Metric

namespace GRHResearch.Analytic

/-- Rational center of the independently certified finite Dirichlet-sum zero disk. -/
noncomputable def arithmeticZeroCenter : ℂ :=
  (337261 / 1000000 : ℂ) + (11027504 / 1000000 : ℂ) * I

/-- Every point in the closed certificate disk is in the left half of the critical strip. -/
theorem arithmetic_zero_disk_in_left_strip {z : ℂ}
    (hz : dist z arithmeticZeroCenter ≤ (1 / 10000 : ℝ)) :
    0 < z.re ∧ z.re < 1 / 2 := by
  have hnorm : ‖z - arithmeticZeroCenter‖ ≤ (1 / 10000 : ℝ) := by
    simpa only [dist_eq_norm] using hz
  have hreal := Complex.abs_re_le_norm (z - arithmeticZeroCenter)
  have hc : arithmeticZeroCenter.re = (337261 / 1000000 : ℝ) := by
    norm_num [arithmeticZeroCenter]
  rw [Complex.sub_re, hc] at hreal
  have hbounds := abs_le.mp (hreal.trans hnorm)
  constructor <;> linarith [hbounds.1, hbounds.2]

/-- The strict Rouché comparison margin used in the rational certificate is positive.
The function/derivative estimates and the Rouché inference remain prose proofs. -/
theorem arithmetic_zero_certificate_margin :
    (1 / 10000 : ℝ) - 1 / 1000000 - (9 / 2) * (1 / 10000)^2 =
      19791 / 200000000 ∧ (0 : ℝ) < 19791 / 200000000 := by
  norm_num

#print axioms arithmetic_zero_disk_in_left_strip
#print axioms arithmetic_zero_certificate_margin
end GRHResearch.Analytic
