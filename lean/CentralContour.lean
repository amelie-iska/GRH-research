import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.MeasureTheory.Integral.Bochner.Basic

namespace GRHResearch.Analytic

/-- All of a retained s-rectangle lies in the first Euler region. -/
theorem central_rectangle_geometry {a β e s : ℝ}
    (ha : 51/100 ≤ a) (haβ : a ≤ β) (hβ : β ≤ 1)
    (he : 0 < e) (he1 : e ≤ 1/1000) (hs : a+16*e ≤ s) :
    51/100 ≤ s ∧ -1/100 ≤ 1-a-6*e ∧
    1+10*e ≤ s+(1-a-6*e) ∧ 1+14*e ≤ (β+20*e)+(1-a-6*e) := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> linarith

/-- The finite coordinate budget controls the actual sum of all added heights. -/
theorem retained_height_budget {ι : Type*} (F : Finset ι) (hF : F.Nonempty)
    (a v cap : ι → ℝ) {T : ℝ}
    (ha : ∀ i ∈ F, |a i| ≤ cap i)
    (hv : ∀ i ∈ F, |v i| ≤ T/(2*(F.card : ℝ)*(1+cap i))) :
    |∑ i ∈ F, a i*v i| ≤ T/2 := by
  have hcard : 0 < (F.card : ℝ) := by exact_mod_cast Finset.card_pos.mpr hF
  calc
    |∑ i ∈ F, a i*v i| ≤ ∑ i ∈ F, |a i*v i| := Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ _i ∈ F, T/(2*(F.card : ℝ)) := by
      apply Finset.sum_le_sum
      intro i hi
      have hc : 0 < 1+cap i := by have := ha i hi; have := abs_nonneg (a i); linarith
      calc
        |a i*v i| = |a i| * |v i| := abs_mul _ _
        _ ≤ (1+cap i) * |v i| := mul_le_mul_of_nonneg_right (by linarith [ha i hi]) (abs_nonneg _)
        _ ≤ (1+cap i)*(T/(2*(F.card : ℝ)*(1+cap i))) :=
          mul_le_mul_of_nonneg_left (hv i hi) (le_of_lt hc)
        _ = T/(2*(F.card : ℝ)) := by field_simp
    _ = T/2 := by simp; field_simp

/-- A single cumulative budget fits the original buffered argument. -/
theorem buffered_height_from_budget {γ added T : ℝ} {i : ℕ}
    (hT : 0 ≤ T) (hγ : |γ| ≤ (3*(i : ℝ)+1)*T) (hv : |added| ≤ T/2) :
    |γ+added| ≤ (3*(i : ℝ)+2)*T := by
  have := abs_add_le γ added
  linarith

/-- One strict ramified label uses its own excess valuation in the conductor. -/
theorem strict_ramified_credit {w : ℝ} (hw : w ≤ 1/2) {j : ℕ} (hj : 2 ≤ j) :
    -w-((j : ℝ)-1)*(1/2-w) ≤ -1/2 := by
  have hjR : (2 : ℝ) ≤ j := by exact_mod_cast hj
  have hprod : 0 ≤ ((j : ℝ)-2)*(1/2-w) := mul_nonneg (by linarith) (by linarith)
  nlinarith

/-- Distinct labels spend the one numerator allowance simultaneously, not once per slot.
The arithmetic conductor inequality and functional equation remain separate inputs. -/
theorem simultaneous_ramified_power_credit {ι : Type*} (F : Finset ι)
    (Q : ι → ℝ) (j : ι → ℕ) {w : ℝ} (hw : w ≤ 1/2)
    (hQ : ∀ i ∈ F, 1 ≤ Q i) (hj : ∀ i ∈ F, 2 ≤ j i) :
    (∏ i ∈ F, (Q i)^(-w-((j i : ℝ)-1)*(1/2-w))) ≤
      ∏ i ∈ F, (Q i)^(-(1/2 : ℝ)) := by
  apply Finset.prod_le_prod
  · intro i hi
    exact Real.rpow_nonneg (by linarith [hQ i hi]) _
  · intro i hi
    apply Real.rpow_le_rpow_of_exponent_le (hQ i hi)
    have := strict_ramified_credit hw (hj i hi)
    linarith

noncomputable def centralExponent (σ a h ly ell g d R δ z : ℝ) : ℝ :=
  a-σ+h*(z-1/6)-a*ly-ell/2+g+d*(R+δ/2-z)

/-- Exact outside-power and aggregate-row accounting at any reference boundary. -/
theorem central_normalization_identity (σ a h lx ly ell g d R δ z e εc εd : ℝ)
    (hh : h = 1-lx+ell) :
    (lx*(1/2-z)+a+z-1-a*ly-d*z+(16-6*ly)*e)
      +(d*(R+δ/2+εc)+ell*(z-1/2)+g+εc+d*εd)
      -(σ+lx/2-1+h/6) =
    centralExponent σ a h ly ell g d R δ z
      +(16-6*ly)*e+(1+d)*εc+d*εd := by
  rw [hh]
  dsimp [centralExponent]
  ring

theorem central_reference_shift (σ β a h ly ell g d R δ z : ℝ) :
    centralExponent σ a h ly ell g d R δ z-(β-σ) =
      centralExponent β a h ly ell g d R δ z := by
  dsimp [centralExponent]
  ring

/-- Fixed-d and moving-endpoint perturbations keep the same algebraic envelope.
This does not identify pointwise row partitions between two different probes. -/
theorem central_perturbation_identities (t δ q R d : ℝ) :
    centralExponent (7/8-t/4) ((1+δ)/2) (13/16+3*t/2) (23/48-t/2)
      (1/6+t) (q*(1/6+t)) d R δ (17/50)
      - centralExponent (7/8) ((1+δ)/2) (13/16) (23/48)
        (1/6) (q/6) d R δ (17/50) = t*(13/50+δ/4+q) ∧
    centralExponent (7/8-t/4) ((1+δ)/2) (13/16+3*t/2) (23/48-t/2)
      (1/6+t) (q*(1/6+t)) (13/16+3*t/2) R δ (17/50)
      - centralExponent (7/8) ((1+δ)/2) (13/16) (23/48)
        (1/6) (q/6) (13/16) R δ (17/50) = t*(-1/4+δ+q+3*R/2) := by
  constructor <;> dsimp [centralExponent] <;> ring

/-- Bound the original integrable function, without integrating any pointwise pieces.
No measurability of the labels of a pointwise partition is required or assumed. -/
theorem original_integral_envelope {α : Type*} [MeasurableSpace α]
    (μ : MeasureTheory.Measure α) (f : α → ℂ) (k : α → ℝ) (C : ℝ)
    (hf : MeasureTheory.Integrable f μ) (hk : MeasureTheory.Integrable k μ)
    (hbound : ∀ᵐ x ∂μ, ‖f x‖ ≤ C*k x) :
    ‖∫ x, f x ∂μ‖ ≤ C*(∫ x, k x ∂μ) := by
  calc
    _ ≤ ∫ x, ‖f x‖ ∂μ := MeasureTheory.norm_integral_le_integral_norm f
    _ ≤ ∫ x, C*k x ∂μ := MeasureTheory.integral_mono_ae hf.norm (hk.const_mul C) hbound
    _ = _ := MeasureTheory.integral_const_mul C k

/-- A finite height order fixed before N permits a later target-dependent tail choice. -/
theorem late_height_and_tail_choice {A m cap B C : ℝ}
    (hA : 0 ≤ A) (hm : 0 < m) (hcap : 0 < cap) :
    ∃ τ : ℝ, 0 < τ ∧ τ ≤ cap ∧ A*τ ≤ m/4 ∧
      ∃ N : ℕ, B-(N : ℝ)*τ < C-m/2 := by
  let τ := min cap (m/(4*(A+1)))
  have hτ : 0 < τ := lt_min hcap (by positivity)
  have hτcap : τ ≤ cap := min_le_left _ _
  have hτm : τ ≤ m/(4*(A+1)) := min_le_right _ _
  have hpay : A*τ ≤ m/4 := by
    have hmul := (le_div_iff₀ (show 0 < 4*(A+1) by positivity)).mp hτm
    nlinarith
  obtain ⟨N, hN⟩ := exists_nat_gt ((B-C+m/2)/τ)
  refine ⟨τ, hτ, hτcap, hpay, N, ?_⟩
  have := (div_lt_iff₀ hτ).mp hN
  linarith

#print axioms central_rectangle_geometry
#print axioms retained_height_budget
#print axioms buffered_height_from_budget
#print axioms strict_ramified_credit
#print axioms simultaneous_ramified_power_credit
#print axioms central_normalization_identity
#print axioms central_perturbation_identities
#print axioms central_reference_shift
#print axioms original_integral_envelope
#print axioms late_height_and_tail_choice
end GRHResearch.Analytic
