import Mathlib.NumberTheory.JacobiSum.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Complex

open Finset

namespace GRHResearch.Analytic

variable {F : Type*} [Field F] [Fintype F]

attribute [local instance] Classical.propDecidable

/-- Even the zeroth character power is zero at zero: MulChar.one is zero-extended. -/
theorem finite_character_power_zero {K : Type*} [Field K] (A : MulChar K ℂ) (n : ℕ) : (A^n) 0 = 0 :=
  (A^n).map_zero

theorem finite_trivial_character_sum :
    (∑ x : F, (1 : MulChar F ℂ) x) = (Fintype.card F : ℂ)-1 := by
  classical
  rw [MulChar.sum_one_eq_card_units, Fintype.card_eq_card_units_add_one (α := F)]
  push_cast
  ring

theorem finite_character_unit_product (A : MulChar F ℂ) {b : F} (hb : b ≠ 0) :
    A b * star (A b) = 1 := by
  rw [MulChar.star_apply']
  change (A*A⁻¹) b = 1
  rw [mul_inv_cancel, MulChar.one_apply (isUnit_iff_ne_zero.mpr hb)]

theorem finite_character_diagonal (A : MulChar F ℂ) :
    (∑ x : F, A x*star (A x)) = (Fintype.card F : ℂ)-1 := by
  classical
  calc
    _ = ∑ x : F, (1 : MulChar F ℂ) x := by
      apply Finset.sum_congr rfl
      intro x _
      rw [MulChar.star_apply']
      change (A*A⁻¹) x = (1 : MulChar F ℂ) x
      rw [mul_inv_cancel]
    _ = _ := finite_trivial_character_sum

/-- Autocorrelation at a nonzero shift, including the principal zero-extended case. -/
theorem finite_character_unit_shift (A : MulChar F ℂ) :
    (∑ x : F, A (x+1)*star (A x)) =
      if A = 1 then (Fintype.card F : ℂ)-2 else -1 := by
  classical
  have hchange : (∑ x : F, A (x+1)*star (A x)) =
      A⁻¹ (-1)*jacobiSum A⁻¹ A := by
    rw [jacobiSum, Finset.mul_sum]
    calc
      _ = ∑ x : F, A (-x+1)*star (A (-x)) :=
        Equiv.sum_comp (Equiv.neg F) (fun x => A (x+1)*star (A x)) |>.symm
      _ = _ := by
        apply Finset.sum_congr rfl
        intro x _
        rw [show -x+1 = 1-x by ring, MulChar.star_apply', neg_eq_neg_one_mul x, map_mul]
        ring
  rw [hchange]
  split_ifs with hA
  · subst A
    have hval : (1 : MulChar F ℂ) (-1 : F) = 1 := MulChar.one_apply isUnit_neg_one
    simp only [inv_one, jacobiSum_one_one, hval, one_mul]
  · have hi : A⁻¹ ≠ 1 := inv_ne_one.mpr hA
    have hj : jacobiSum A⁻¹ A = -A⁻¹ (-1) := by
      simpa only [inv_inv] using jacobiSum_nontrivial_inv hi
    have hsq : A⁻¹ (-1)*A⁻¹ (-1) = (1 : ℂ) := by
      rw [← map_mul]
      norm_num
    rw [hj]
    calc
      _ = -(A⁻¹ (-1)*A⁻¹ (-1)) := by ring
      _ = -1 := by rw [hsq]

/-- This is a genuine finite-field/MulChar statement, not an assumed analytic bound. -/
theorem finite_character_autocorrelation (A : MulChar F ℂ) (b : F) :
    (∑ x : F, A (x+b)*star (A x)) =
      if b = 0 then (Fintype.card F : ℂ)-1
      else if A = 1 then (Fintype.card F : ℂ)-2 else -1 := by
  classical
  by_cases hb : b = 0
  · subst b
    simpa using finite_character_diagonal A
  rw [if_neg hb]
  have hmul := finite_character_unit_product A hb
  calc
    _ = ∑ x : F, A (b*x+b)*star (A (b*x)) :=
      Equiv.sum_comp (Equiv.mulLeft₀ b hb) (fun x => A (x+b)*star (A x)) |>.symm
    _ = ∑ x : F, (A b*star (A b))*(A (x+1)*star (A x)) := by
      apply Finset.sum_congr rfl
      intro x _
      rw [show b*x+b = b*(x+1) by ring, map_mul, map_mul, star_mul]
      ring
    _ = _ := by simp only [hmul, one_mul]; exact finite_character_unit_shift A

noncomputable def fieldCorrelation (A : MulChar F ℂ) (a b k : F) : ℂ :=
  ∑ x : F, ∑ y : F, if a*x-b*y = k then A x*star (A y) else 0

/-- Solve the finite congruence rather than dropping any zero extensions. -/
theorem field_correlation_solve (A : MulChar F ℂ) {a : F} (ha : a ≠ 0) (b k : F) :
    fieldCorrelation A a b k = ∑ y : F, A ((k+b*y)/a)*star (A y) := by
  classical
  unfold fieldCorrelation
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro y _
  have hrel (x : F) : a*x-b*y = k ↔ x = (k+b*y)/a := by
    rw [eq_div_iff ha]
    constructor <;> intro h <;> linear_combination h
  simp only [hrel]
  simp

/-- The common-prime local formula when both residual coefficients are units. -/
theorem field_correlation_units (A : MulChar F ℂ) {a b : F}
    (ha : a ≠ 0) (hb : b ≠ 0) (k : F) :
    fieldCorrelation A a b k = A (b/a) *
      (if k = 0 then (Fintype.card F : ℂ)-1
       else if A = 1 then (Fintype.card F : ℂ)-2 else -1) := by
  classical
  rw [field_correlation_solve A ha]
  have heq (y : F) : (k+b*y)/a = (b/a)*(y+k/b) := by field_simp; ring
  simp_rw [heq, map_mul, mul_assoc]
  rw [← Finset.mul_sum, finite_character_autocorrelation]
  simp [div_eq_zero_iff, hb]

/-- The common-prime case in which one residual coefficient vanishes. -/
theorem field_correlation_one_zero (A : MulChar F ℂ) {a : F} (ha : a ≠ 0) (k : F) :
    fieldCorrelation A a 0 k =
      if k = 0 then 0 else if A = 1 then (Fintype.card F : ℂ)-1 else 0 := by
  classical
  rw [field_correlation_solve A ha]
  simp_rw [zero_mul, add_zero]
  rw [← Finset.mul_sum, ← star_sum]
  split_ifs with hk hA
  · simp [hk, A.map_zero]
  · subst A
    have hval : (1 : MulChar F ℂ) (k/a) = 1 :=
      MulChar.one_apply (isUnit_iff_ne_zero.mpr (div_ne_zero hk ha))
    rw [hval, finite_trivial_character_sum]
    simp
  · rw [MulChar.sum_eq_zero_of_ne_one hA]
    simp

/-- Exact degenerate corner; the artificial zero extension is not this genuine sum. -/
theorem field_correlation_zero_coefficients (A : MulChar F ℂ) (k : F) :
    fieldCorrelation A 0 0 k =
      if k = 0 then (∑ x : F, A x)*star (∑ y : F, A y) else 0 := by
  classical
  by_cases hk : k = 0
  · subst k
    simp only [fieldCorrelation, zero_mul, sub_zero, ite_true]
    rw [star_sum, Finset.sum_mul_sum]
  · simp [fieldCorrelation, hk, eq_comm]

theorem field_correlation_principal_corner :
    fieldCorrelation (1 : MulChar F ℂ) 0 0 0 = ((Fintype.card F : ℂ)-1)^2 := by
  rw [field_correlation_zero_coefficients, if_pos rfl, finite_trivial_character_sum]
  simp
  ring

local instance : Fact (Nat.Prime 7) := ⟨by decide⟩

/-- An actual F7 counterexample to extending the genuine kernel bound off its locus. -/
theorem field_correlation_f7_corner :
    fieldCorrelation (1 : MulChar (ZMod 7) ℂ) 0 0 0 = 36 := by
  rw [field_correlation_principal_corner, ZMod.card]
  norm_num

/-- Order six, not a pointwise convention at zero, determines principality. -/
theorem sextic_character_power_nontrivial {K : Type*} [Field K]
    (A : MulChar K ℂ) (horder : orderOf A = 6) {n : ℕ} (hn : ¬6 ∣ n) : A^n ≠ 1 := by
  intro h
  apply hn
  rw [← horder, orderOf_dvd_iff_pow_eq_one]
  exact h

/-- Principal zero-extended multiplicative character and nontrivial additive phase. -/
theorem finite_gauss_trivial (ψ : AddChar F ℂ) (hψ : ψ ≠ 1) :
    gaussSum (1 : MulChar F ℂ) ψ = -1 := by
  classical
  have hpoint (x : F) : (1 : MulChar F ℂ) x*ψ x = ψ x-(if x=0 then 1 else 0) := by
    by_cases hx : x=0
    · simp [hx, MulChar.map_zero, ψ.map_zero_eq_one]
    · rw [MulChar.one_apply (isUnit_iff_ne_zero.mpr hx)]
      simp [hx]
  simp_rw [gaussSum, hpoint]
  rw [Finset.sum_sub_distrib, AddChar.sum_eq_zero_of_ne_one hψ]
  simp

theorem finite_gauss_conjugate (A : MulChar F ℂ) (ψ : AddChar F ℂ) :
    gaussSum A⁻¹ ψ⁻¹ = star (gaussSum A ψ) := by
  simp only [gaussSum, star_sum, star_mul, MulChar.star_apply', AddChar.inv_apply,
    AddChar.map_neg_eq_conj, RCLike.star_def, mul_comm]

theorem finite_gauss_norm_sq {A : MulChar F ℂ} (hA : A ≠ 1)
    {ψ : AddChar F ℂ} (hψ : ψ ≠ 1) :
    ‖gaussSum A ψ‖^2 = (Fintype.card F : ℝ) := by
  have hp := gaussSum_mul_gaussSum_eq_card hA (AddChar.IsPrimitive.of_ne_one hψ)
  rw [finite_gauss_conjugate] at hp
  have hr := congrArg Complex.re hp
  simpa only [Complex.star_def, Complex.mul_conj, Complex.ofReal_re, Complex.normSq_eq_norm_sq,
    Complex.natCast_re] using hr

#print axioms finite_character_power_zero
#print axioms finite_trivial_character_sum
#print axioms finite_character_unit_product
#print axioms finite_character_diagonal
#print axioms finite_character_unit_shift
#print axioms finite_character_autocorrelation
#print axioms field_correlation_solve
#print axioms field_correlation_units
#print axioms field_correlation_one_zero
#print axioms field_correlation_zero_coefficients
#print axioms field_correlation_principal_corner
#print axioms field_correlation_f7_corner
#print axioms sextic_character_power_nontrivial
#print axioms finite_gauss_trivial
#print axioms finite_gauss_conjugate
#print axioms finite_gauss_norm_sq
end GRHResearch.Analytic
