import Mathlib.Analysis.SpecialFunctions.Pow.Complex

open Complex

namespace GRHResearch.Analytic

/-- Principal two-term multiplier after the source's local scalar specialization. -/
noncomputable def principalSlotMultiplier (v d r : ℂ) : ℂ :=
  (1-v)*(r-d)/(d*(1-v*r-(1-v)*d))-v

/-- For r=d the marked part vanishes exactly. Arithmetic inert primes at the
real endpoint s=3/5 give this equality; the power identification is prose. -/
theorem principal_multiplier_when_equal (v d : ℂ) :
    principalSlotMultiplier v d d = -v := by
  simp [principalSlotMultiplier]

theorem principal_multiplier_error (v d r : ℂ)
    (hd : d ≠ 0) (hn : 1-v*r-(1-v)*d ≠ 0) :
    principalSlotMultiplier v d r + 1 =
      (1-v)*(r/d-v*r-(1-v)*d)/(1-v*r-(1-v)*d) := by
  unfold principalSlotMultiplier
  field_simp
  ring

/-- This exact identity isolates the leading term in the pointwise 3/5 obstruction.
The asymptotic estimates for arithmetic prime powers remain prose. -/
theorem principal_multiplier_scaled_error (v d r : ℂ)
    (hd : d ≠ 0) (hr : r ≠ 0) (hn : 1-v*r-(1-v)*d ≠ 0) :
    (principalSlotMultiplier v d r + 1)/(r/d)-1 =
      (-v*(1-r)+(1-v)^2*d*(1-d/r))/(1-v*r-(1-v)*d) := by
  unfold principalSlotMultiplier
  field_simp
  ring

/-- Exact finite weighted-slot normalization; all weights here may be complex. -/
theorem weighted_slot_factorization {ι : Type*} (P : Finset ι) (a b : ι → ℂ)
    (hS : (∑ i ∈ P, a i) ≠ 0) :
    (∑ i ∈ P, a i*b i) =
      -(∑ i ∈ P, a i) *
        (1-(∑ i ∈ P, a i*(b i+1))/(∑ i ∈ P, a i)) := by
  have hsum : (∑ i ∈ P, a i*(b i+1)) =
      (∑ i ∈ P, a i*b i)+(∑ i ∈ P, a i) := by
    simp_rw [mul_add, mul_one]
    exact Finset.sum_add_distrib
  rw [hsum]
  field_simp
  ring

/-- Nonnegative weights prevent cancellation in the denominator and transfer a
uniform local complex error to the normalized slot, without using prime asymptotics. -/
theorem weighted_slot_error_bound {ι : Type*} (P : Finset ι)
    (a : ι → ℝ) (b : ι → ℂ) {δ : ℝ}
    (ha : ∀ i ∈ P, 0 ≤ a i) (hS : 0 < ∑ i ∈ P, a i)
    (hb : ∀ i ∈ P, ‖b i+1‖ ≤ δ) :
    ‖-(∑ i ∈ P, (a i : ℂ)*(b i+1))/((∑ i ∈ P, a i : ℝ) : ℂ)‖ ≤ δ := by
  rw [norm_div, norm_neg, Complex.norm_real, Real.norm_eq_abs, abs_of_pos hS]
  apply (div_le_iff₀ hS).mpr
  calc
    ‖∑ i ∈ P, (a i : ℂ)*(b i+1)‖ ≤
        ∑ i ∈ P, ‖(a i : ℂ)*(b i+1)‖ := norm_sum_le _ _
    _ ≤ ∑ i ∈ P, a i*δ := by
      apply Finset.sum_le_sum
      intro i hi
      rw [norm_mul, Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg (ha i hi)]
      exact mul_le_mul_of_nonneg_left (hb i hi) (ha i hi)
    _ = δ*(∑ i ∈ P, a i) := by rw [Finset.mul_sum]; apply Finset.sum_congr rfl; intro i _; ring

/-- A fixed finite product preserves a common small relative error. -/
theorem finite_product_relative_error {ι : Type*} [DecidableEq ι]
    (P : Finset ι) (ρ : ι → ℂ) {δ : ℝ} (hδ1 : δ ≤ 1)
    (hρ : ∀ i ∈ P, ‖ρ i‖ ≤ δ) :
    ‖(∏ i ∈ P, (1+ρ i))-1‖ ≤ ((2 : ℝ)^P.card-1)*δ := by
  induction P using Finset.induction_on with
  | empty => simp
  | @insert i P hi ih =>
    have hiρ := hρ i (Finset.mem_insert_self i P)
    have hP : ∀ j ∈ P, ‖ρ j‖ ≤ δ := by
      intro j hj
      exact hρ j (Finset.mem_insert_of_mem hj)
    have hih := ih hP
    have htwo : ‖1+ρ i‖ ≤ 2 := by
      calc
        _ ≤ ‖(1 : ℂ)‖+‖ρ i‖ := norm_add_le _ _
        _ ≤ 2 := by rw [norm_one]; linarith
    rw [Finset.prod_insert hi, Finset.card_insert_of_notMem hi, pow_succ]
    have heq : (1+ρ i)*(∏ j ∈ P, (1+ρ j))-1 =
        (1+ρ i)*((∏ j ∈ P, (1+ρ j))-1)+ρ i := by ring
    rw [heq]
    calc
      _ ≤ ‖(1+ρ i)*((∏ j ∈ P, (1+ρ j))-1)‖+‖ρ i‖ := norm_add_le _ _
      _ = ‖1+ρ i‖*‖(∏ j ∈ P, (1+ρ j))-1‖+‖ρ i‖ := by rw [norm_mul]
      _ ≤ 2*‖(∏ j ∈ P, (1+ρ j))-1‖+δ := by gcongr
      _ ≤ 2*(((2 : ℝ)^P.card-1)*δ)+δ := by gcongr
      _ = ((2 : ℝ)^P.card*2-1)*δ := by ring

#print axioms principal_multiplier_when_equal
#print axioms principal_multiplier_error
#print axioms principal_multiplier_scaled_error
#print axioms weighted_slot_factorization
#print axioms weighted_slot_error_bound
#print axioms finite_product_relative_error
end GRHResearch.Analytic
