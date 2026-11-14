import Mathlib.NumberTheory.JacobiSum.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Complex
import Mathlib.Analysis.SpecificLimits.Normed

open Finset

namespace GRHResearch.Analytic

/-- Normalized complete Fourier coefficient on an actual finite additive group. -/
noncomputable def normalizedFiniteFourier {G : Type*} [AddCommGroup G] [Fintype G]
    (a : G → ℂ) (ψ : AddChar G ℂ) : ℂ :=
  (∑ x : G, a x*star (ψ x))/(Fintype.card G : ℂ)

theorem normalized_finite_fourier_norm {G : Type*} [AddCommGroup G] [Fintype G]
    (a : G → ℂ) (ψ : AddChar G ℂ) {M : ℝ} (ha : ∀ x, ‖a x‖ ≤ M) :
    ‖normalizedFiniteFourier a ψ‖ ≤ M := by
  have hcard : 0 < (Fintype.card G : ℝ) := by exact_mod_cast Fintype.card_pos
  rw [normalizedFiniteFourier, norm_div, Complex.norm_natCast]
  apply (div_le_iff₀ hcard).mpr
  calc
    ‖∑ x : G, a x*star (ψ x)‖ ≤ ∑ x : G, ‖a x*star (ψ x)‖ := norm_sum_le _ _
    _ ≤ ∑ _x : G, M := by
      apply Finset.sum_le_sum
      intro x _
      simpa only [norm_mul, norm_star, AddChar.norm_apply, mul_one] using ha x
    _ = M*(Fintype.card G : ℝ) := by simp [mul_comm]

theorem normalized_finite_fourier_zero {G : Type*} [AddCommGroup G] [Fintype G]
    (a : G → ℂ) (ha : (∑ x : G, a x) = 0) :
    normalizedFiniteFourier a (1 : AddChar G ℂ) = 0 := by
  simp [normalizedFiniteFourier, ha]

/-- Arbitrary remaining columns and CRT labels may couple; independence of the
one nonprincipal field coordinate suffices for the complete mean to vanish. -/
theorem nonprincipal_independent_coordinate_mean {F I : Type*} [Field F] [Fintype F]
    [Fintype I] (χ : MulChar F ℂ) (hχ : χ ≠ 1) (b : I → ℂ) :
    (∑ x : F, ∑ i : I, χ x*b i) = 0 := by
  simp_rw [← Finset.mul_sum]
  rw [← Finset.sum_mul, MulChar.sum_eq_zero_of_ne_one hχ, zero_mul]

/-- The two-column complete mean may retain any coefficient independent of x. -/
theorem nonprincipal_joint_mean {F I J : Type*} [Field F] [Fintype F]
    [Fintype I] [Fintype J] (χ : MulChar F ℂ) (hχ : χ ≠ 1) (b : I → J → ℂ) :
    (∑ x : F, ∑ i : I, ∑ j : J, χ x*b i j) = 0 := by
  simp_rw [← Finset.mul_sum]
  rw [← Finset.sum_mul, MulChar.sum_eq_zero_of_ne_one hχ, zero_mul]

/-- Exact finite head of the dyadic majorant. -/
theorem gram_dyadic_head (L : ℕ) :
    (∑ n ∈ Finset.range (L+1), ((n+1 : ℕ) : ℝ)*(2 : ℝ)^n) =
      (L : ℝ)*2^(L+1)+1 := by
  induction L with
  | zero => norm_num
  | succ L ih =>
    rw [Finset.sum_range_succ, ih]
    push_cast
    simp only [pow_succ]
    ring

/-- This infinite series is the trivial bound used when the cutoff is subunit. -/
theorem gram_dyadic_total :
    (∑' n : ℕ, ((n+1 : ℕ) : ℝ)*(1/2 : ℝ)^n) = 4 := by
  have h := tsum_choose_mul_geometric_of_norm_lt_one (𝕜 := ℝ) 1
    (r := (1/2 : ℝ)) (by norm_num)
  norm_num at h ⊢
  exact h

/-- The exact dyadic tail after L, including the multiplicity n+1. -/
theorem gram_dyadic_tail (L : ℕ) :
    (∑' n : ℕ, ((n+L+2 : ℕ) : ℝ)*(1/2 : ℝ)^(n+L+1)) =
      ((L : ℝ)+3)*(1/2 : ℝ)^L := by
  have hg : Summable (fun n : ℕ => (1/2 : ℝ)^n) := summable_geometric_of_norm_lt_one (by norm_num)
  have hn : Summable (fun n : ℕ => (n : ℝ)*(1/2 : ℝ)^n) :=
    (hasSum_coe_mul_geometric_of_norm_lt_one (r := (1/2 : ℝ)) (by norm_num)).summable
  have hge : (∑' n : ℕ, (1/2 : ℝ)^n) = 2 := by
    have h := tsum_geometric_of_norm_lt_one (show ‖(1/2 : ℝ)‖ < 1 by norm_num)
    norm_num at h ⊢
    exact h
  have hne : (∑' n : ℕ, (n : ℝ)*(1/2 : ℝ)^n) = 2 := by
    have h := (hasSum_coe_mul_geometric_of_norm_lt_one (r := (1/2 : ℝ)) (by norm_num)).tsum_eq
    norm_num at h ⊢
    exact h
  have heq (n : ℕ) : ((n+L+2 : ℕ) : ℝ)*(1/2 : ℝ)^(n+L+1) =
      (1/2 : ℝ)^(L+1)*((n : ℝ)*(1/2 : ℝ)^n+((L : ℝ)+2)*(1/2 : ℝ)^n) := by
    push_cast
    rw [show n+L+1 = n+(L+1) by omega, pow_add]
    ring
  simp_rw [heq]
  rw [tsum_mul_left, hn.tsum_add (hg.mul_left _), tsum_mul_left, hge, hne, pow_succ]
  ring

/-- A finite head bound with the correct inverse Lambda scale, not a constant loss. -/
theorem gram_dyadic_head_bound (L : ℕ) {Λ : ℝ} (hΛ : (2 : ℝ)^L ≤ Λ) :
    (∑ n ∈ Finset.range (L+1), ((n+1 : ℕ) : ℝ)*(2 : ℝ)^n)/Λ^2 ≤
      2*((L : ℝ)+1)/Λ := by
  have hpow : 1 ≤ (2 : ℝ)^L := one_le_pow₀ (by norm_num)
  have hpos : 0 < Λ := by linarith
  rw [gram_dyadic_head]
  apply (div_le_iff₀ (sq_pos_of_pos hpos)).mpr
  field_simp
  have hL : 0 ≤ (L : ℝ) := Nat.cast_nonneg _
  have hmul := mul_le_mul_of_nonneg_left hΛ (by linarith : 0 ≤ 2*(L : ℝ))
  rw [pow_succ]
  nlinarith

/-- Exact squared-scale normalization in dimension four removes the period volume. -/
theorem gram_nonexceptional_accounting (Q Y R P C D : ℝ)
    (hY : Y ≠ 0) (hC : C ≠ 0) (hD : D ≠ 0) :
    (Q/Y^3)*(C*D*(R*P/C))*C*(Y/(C*D))^2 =
      (Q/Y)*(R*P/(C*D)) := by field_simp

#print axioms normalized_finite_fourier_norm
#print axioms normalized_finite_fourier_zero
#print axioms nonprincipal_independent_coordinate_mean
#print axioms nonprincipal_joint_mean
#print axioms gram_dyadic_head
#print axioms gram_dyadic_total
#print axioms gram_dyadic_tail
#print axioms gram_dyadic_head_bound
#print axioms gram_nonexceptional_accounting
end GRHResearch.Analytic
