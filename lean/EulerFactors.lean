import Mathlib.Analysis.SpecialFunctions.Pow.Complex
import Mathlib.Analysis.Complex.AbsMax
import Mathlib.Analysis.Complex.LocallyUniformLimit

open Set Filter Complex
open scoped Topology

namespace GRHResearch.Analytic

/-- The usual Euler weight p^(-s), expressed using the real logarithm of p>1. -/
noncomputable def eulerWeight (p : ℝ) (s : ℂ) : ℂ :=
  Complex.exp (-(s * (Real.log p : ℂ)))

/-- Actual complex Euler weights are strictly inside the unit disk on Re(s)>0. -/
theorem norm_eulerWeight_lt_one {p : ℝ} {s : ℂ} (hp : 1 < p) (hs : 0 < s.re) :
    ‖eulerWeight p s‖ < 1 := by
  rw [eulerWeight, Complex.norm_exp, Real.exp_lt_one_iff]
  simp only [Complex.neg_re, Complex.mul_re, Complex.ofReal_re, Complex.ofReal_im,
    mul_zero, sub_zero]
  exact neg_neg_of_pos (mul_pos hs (Real.log_pos hp))

/-- A character value of norm at most one cannot make a local Euler factor vanish. -/
theorem euler_factor_ne_zero {p : ℝ} {s a : ℂ} (hp : 1 < p) (hs : 0 < s.re)
    (ha : ‖a‖ ≤ 1) : 1 - a * eulerWeight p s ≠ 0 := by
  have hlt : ‖a * eulerWeight p s‖ < 1 := by
    rw [norm_mul]
    calc
      ‖a‖ * ‖eulerWeight p s‖ ≤ 1 * ‖eulerWeight p s‖ :=
        mul_le_mul_of_nonneg_right ha (norm_nonneg _)
      _ = ‖eulerWeight p s‖ := one_mul _
      _ < 1 := norm_eulerWeight_lt_one hp hs
  intro heq
  have heq' : a * eulerWeight p s = 1 := (sub_eq_zero.mp heq).symm
  rw [heq', norm_one] at hlt
  exact (lt_irrefl (1 : ℝ)) hlt

/-- Every finite Euler determinant is zero-free in the positive half-plane. -/
theorem finite_euler_product_ne_zero {ι : Type*} (P : Finset ι) (p : ι → ℝ)
    (a : ι → ℂ) (s : ℂ) (hs : 0 < s.re)
    (hp : ∀ i ∈ P, 1 < p i) (ha : ∀ i ∈ P, ‖a i‖ ≤ 1) :
    (∏ i ∈ P, (1 - a i * eulerWeight (p i) s)) ≠ 0 := by
  exact Finset.prod_ne_zero_iff.mpr fun i hi =>
    euler_factor_ne_zero (hp i hi) hs (ha i hi)

/-- A minimum-modulus bound obtained by applying maximum modulus to the reciprocal. -/
theorem boundary_lower_bound {U : Set ℂ} {f : ℂ → ℂ} {δ : ℝ} {z : ℂ}
    (hU : Bornology.IsBounded U) (hf : DiffContOnCl ℂ f U)
    (hzero : ∀ w ∈ closure U, f w ≠ 0) (hδ : 0 < δ)
    (hboundary : ∀ w ∈ frontier U, δ ≤ ‖f w‖) (hz : z ∈ closure U) :
    δ ≤ ‖f z‖ := by
  have hinv : ‖(f z)⁻¹‖ ≤ δ⁻¹ := by
    apply Complex.norm_le_of_forall_mem_frontier_norm_le hU (hf.inv hzero) ?_ hz
    intro w hw
    change ‖(f w)⁻¹‖ ≤ δ⁻¹
    rw [norm_inv]
    exact (inv_le_inv₀ (lt_of_lt_of_le hδ (hboundary w hw)) hδ).mpr (hboundary w hw)
  rw [norm_inv] at hinv
  exact (inv_le_inv₀ (norm_pos_iff.mpr (hzero z hz)) hδ).mp hinv

/-- A genuine analytic limit theorem with an explicit eventual boundary margin. -/
theorem limit_ne_zero_of_boundary_lower_bound {U : Set ℂ} {F : ℕ → ℂ → ℂ}
    {z value : ℂ} {δ : ℝ} (hU : Bornology.IsBounded U)
    (hF : ∀ n, DiffContOnCl ℂ (F n) U)
    (hzero : ∀ n w, w ∈ closure U → F n w ≠ 0) (hδ : 0 < δ)
    (hboundary : ∀ᶠ n in atTop, ∀ w ∈ frontier U, δ ≤ ‖F n w‖)
    (hz : z ∈ closure U) (hlimit : Tendsto (fun n => F n z) atTop (𝓝 value)) :
    value ≠ 0 := by
  have hlower : ∀ᶠ n in atTop, δ ≤ ‖F n z‖ := by
    filter_upwards [hboundary] with n hn
    exact boundary_lower_bound hU (hF n) (hzero n) hδ hn hz
  have hnorm : δ ≤ ‖value‖ := ge_of_tendsto hlimit.norm hlower
  exact norm_pos_iff.mp (lt_of_lt_of_le hδ hnorm)

/-- Uniform boundary convergence and a nonzero boundary margin prevent a zero limit inside. -/
theorem boundary_uniform_limit_ne_zero {U : Set ℂ} {F : ℕ → ℂ → ℂ}
    {f : ℂ → ℂ} {z : ℂ} {m : ℝ} (hU : Bornology.IsBounded U)
    (hF : ∀ n, DiffContOnCl ℂ (F n) U)
    (hzero : ∀ n w, w ∈ closure U → F n w ≠ 0) (hm : 0 < m)
    (hboundary : ∀ w ∈ frontier U, m ≤ ‖f w‖)
    (huniform : TendstoUniformlyOn F f atTop (frontier U))
    (hz : z ∈ closure U) (hlimit : Tendsto (fun n => F n z) atTop (𝓝 (f z))) :
    f z ≠ 0 := by
  have hm2 : 0 < m / 2 := half_pos hm
  have hevent : ∀ᶠ n in atTop, ∀ w ∈ frontier U, m / 2 ≤ ‖F n w‖ := by
    filter_upwards [(Metric.tendstoUniformlyOn_iff.mp huniform) (m / 2) hm2] with n hn w hw
    have hdist := hn w hw
    rw [dist_eq_norm] at hdist
    have htriangle := norm_sub_norm_le (f w) (F n w)
    have hmargin := hboundary w hw
    linarith
  exact limit_ne_zero_of_boundary_lower_bound hU hF hzero hm2 hevent hz hlimit

#print axioms norm_eulerWeight_lt_one
#print axioms euler_factor_ne_zero
#print axioms finite_euler_product_ne_zero
#print axioms boundary_lower_bound
#print axioms limit_ne_zero_of_boundary_lower_bound
#print axioms boundary_uniform_limit_ne_zero
end GRHResearch.Analytic
