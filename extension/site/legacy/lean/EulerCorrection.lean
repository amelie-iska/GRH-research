import Mathlib.Analysis.SpecialFunctions.Pow.Complex
import Mathlib.Analysis.SpecialFunctions.Log.Summable

open Complex Filter
open scoped Topology

namespace GRHResearch.Analytic

/-- The unramified local P-star expression, with D W = eta(p) Q^(-x-w). -/
noncomputable def goodPStar (q v w d r : ℂ) : ℂ :=
  ((r * (1-q⁻¹) - d*w*(q-1)*v)/(1-v) - d + w*r)/(1-r)

/-- Exact cancellation that supplies the improved unramified defect estimate. -/
theorem good_residual_identity (q v w d r : ℂ)
    (hv : 1-v ≠ 0) (hr : 1-r ≠ 0) :
    goodPStar q v w d r + d =
      (r*((1-q⁻¹)/(1-v)+w-d)-d*w*(q-1)*v/(1-v))/(1-r) := by
  unfold goodPStar
  field_simp
  ring

/-- Principal local correction at w=1,z=1/6; v is the inverse prime norm. -/
noncomputable def principalCorrection (v d r : ℂ) : ℂ :=
  (1-v^2)*(1-v*r-(1-v)*d)/((1-r)*(1-d))

/-- Removing the (1-r) Euler factor leaves the normally convergent remainder. -/
noncomputable def principalRemainder (v d r : ℂ) : ℂ :=
  (1-v^2)*(1-v*r-(1-v)*d)/(1-d)

theorem principal_correction_from_local (v d r : ℂ)
    (hv : 1-v ≠ 0) (hd : 1-d ≠ 0) (hr : 1-r ≠ 0) :
    (1/(1-v)+v/(1-v)+
      ((r*(1-v)-d*v*(1-v))/(1-v)-d+v*r)/(1-r)) *
        (1-v)^2/(1-d) = principalCorrection v d r := by
  unfold principalCorrection
  field_simp
  ring

theorem principal_remainder_defect (v d r : ℂ) (hd : 1-d ≠ 0) :
    principalRemainder v d r - 1 =
      -v^2 + (1-v^2)*v*(d-r)/(1-d) := by
  unfold principalRemainder
  field_simp
  ring

theorem principal_euler_factorization (v d r : ℂ)
    (hd : 1-d ≠ 0) (hr : 1-r ≠ 0) :
    principalCorrection v d r = principalRemainder v d r / (1-r) := by
  unfold principalCorrection principalRemainder
  field_simp

/-- Convexity, rather than an L-function zero-location premise, makes each local
principal factor nonzero. Convergence of its infinite product is separate. -/
theorem principal_correction_ne_zero {v : ℝ} {d r : ℂ}
    (hv0 : 0 < v) (hv1 : v < 1) (hd : ‖d‖ < 1) (hr : ‖r‖ < 1) :
    principalCorrection (v : ℂ) d r ≠ 0 := by
  have hd0 : 1-d ≠ 0 := by
    intro h
    have : d = 1 := (sub_eq_zero.mp h).symm
    simp [this] at hd
  have hr0 : 1-r ≠ 0 := by
    intro h
    have : r = 1 := (sub_eq_zero.mp h).symm
    simp [this] at hr
  have hvnorm : ‖(v : ℂ)‖ = v := by simp [abs_of_pos hv0]
  have h1vnorm : ‖(1-(v : ℂ))‖ = 1-v := by
    rw [← Complex.ofReal_one, ← Complex.ofReal_sub, Complex.norm_real,
      Real.norm_eq_abs, abs_of_pos (sub_pos.mpr hv1)]
  have hconvex : ‖(v : ℂ)*r+(1-(v : ℂ))*d‖ < 1 := by
    calc
      _ ≤ ‖(v : ℂ)*r‖ + ‖(1-(v : ℂ))*d‖ := norm_add_le _ _
      _ = v*‖r‖ + (1-v)*‖d‖ := by rw [norm_mul, norm_mul, hvnorm, h1vnorm]
      _ < v*1+(1-v)*1 := add_lt_add
        (mul_lt_mul_of_pos_left hr hv0)
        (mul_lt_mul_of_pos_left hd (sub_pos.mpr hv1))
      _ = 1 := by ring
  have hn : 1-(v : ℂ)*r-(1-(v : ℂ))*d ≠ 0 := by
    intro h
    have heq : (v : ℂ)*r+(1-(v : ℂ))*d = 1 := by linear_combination -h
    simp [heq] at hconvex
  have hv2 : 1-(v : ℂ)^2 ≠ 0 := by
    have hreal : (1-v^2 : ℝ) ≠ 0 := by nlinarith
    exact_mod_cast hreal
  exact div_ne_zero (mul_ne_zero hv2 hn) (mul_ne_zero hr0 hd0)

/-- An actual complex infinite-product nonvanishing statement. The application
must separately prove norm summability and local nonvanishing. -/
theorem correction_tprod_ne_zero {ι : Type*} (f : ι → ℂ)
    (hlocal : ∀ i, 1+f i ≠ 0) (hsum : Summable (fun i => ‖f i‖)) :
    ∏' i, (1+f i) ≠ 0 := by
  exact tprod_one_add_ne_zero_of_summable hlocal hsum

/-- Finite exponential error control passes to the actual complex infinite product. -/
theorem correction_tprod_error {ι : Type*} (f : ι → ℂ)
    (hsum : Summable (fun i => ‖f i‖)) :
    ‖(∏' i, (1+f i))-1‖ ≤ Real.exp (∑' i, ‖f i‖)-1 := by
  have hprod := (multipliable_one_add_of_summable hsum).hasProd
  have hlimit := (hprod.sub_const (1 : ℂ)).norm
  apply le_of_tendsto hlimit
  filter_upwards [] with s
  calc
    ‖(∏ i ∈ s, (1+f i))-1‖ ≤ Real.exp (∑ i ∈ s, ‖f i‖)-1 :=
      s.norm_prod_one_add_sub_one_le f
    _ ≤ Real.exp (∑' i, ‖f i‖)-1 := by
      exact sub_le_sub_right (Real.exp_le_exp.mpr
        (hsum.sum_le_tsum s (fun i _ => norm_nonneg (f i)))) 1

/-- Actual zero transport under the displayed shifted factorization. Existence of
the Hecke zero and the analytic arithmetic factorization are separate inputs. -/
theorem shifted_zero_transport {A L H : ℂ → ℂ} {ρ : ℂ}
    (hρ : (1/2 : ℝ) ≤ ρ.re) (hzero : L ρ = 0)
    (hfactor : ∀ s : ℂ, (1/2 : ℝ) < s.re → H s = A s * L (6*s-3)) :
    H ((ρ+3)/6) = 0 ∧ (7/12 : ℝ) ≤ ((ρ+3)/6).re := by
  have hre : ((ρ+3)/6).re = (ρ.re+3)/6 := by
    simp
  have hregion : (1/2 : ℝ) < ((ρ+3)/6).re := by rw [hre]; linarith
  constructor
  · rw [hfactor _ hregion]
    have heq : 6*((ρ+3)/6)-3 = ρ := by ring
    rw [heq, hzero, mul_zero]
  · rw [hre]
    linarith

#print axioms good_residual_identity
#print axioms principal_correction_from_local
#print axioms principal_remainder_defect
#print axioms principal_euler_factorization
#print axioms principal_correction_ne_zero
#print axioms correction_tprod_ne_zero
#print axioms correction_tprod_error
#print axioms shifted_zero_transport
end GRHResearch.Analytic
