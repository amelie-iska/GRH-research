import Mathlib.Analysis.SpecialFunctions.Pow.Real

namespace GRHResearch.Analytic

noncomputable def hybridMinimum (v z : ℝ) : ℝ := min (min v z) ((v+z)/3)

/-- The two branches actually used in the reflected-energy application. -/
theorem hybrid_minimum_dichotomy {v z : ℝ} (hv : 0 ≤ v) :
    hybridMinimum v z = z ∨ v/2 ≤ hybridMinimum v z := by
  by_cases hz : z ≤ v/2
  · left
    dsimp [hybridMinimum]
    have h1 : z ≤ v := by linarith
    have h2 : z ≤ (v+z)/3 := by linarith
    rw [min_eq_right h1, min_eq_left h2]
  · right
    dsimp [hybridMinimum]
    apply le_min
    · exact le_min (by linarith) (by linarith)
    · linarith

/-- The kernel's positive-part saving pays a quarter of the dual range. -/
theorem kernel_quarter_charge (T y : ℝ) :
    T/4 ≤ y/4 + max 0 (T-y)/2 := by
  have h0 : 0 ≤ max 0 (T-y) := le_max_left _ _
  have h1 : T-y ≤ max 0 (T-y) := le_max_right _ _
  linarith

noncomputable def dualLength (H A z ell θ N B : ℝ) : ℝ :=
  2*H+2*A+2*z-1-ell-θ-N-3*B

noncomputable def reflectedEnergy (O H A S N B z ell θ v lb e : ℝ) : ℝ :=
  O/2 + max H (v+lb) - S-B+z-hybridMinimum v z-lb-2*e/3
    - max 0 (dualLength H A z ell θ N B-v-3*lb-e)/2

/-- A uniform algebraic bound for the actual reflected exponent, allowing finite
support offsets, a displaced Gaussian annulus and a retained-range slack.
This does not assert the arithmetic reflected-energy estimate itself. -/
theorem reflected_energy_upper {O H A S N B z ell θ v lb e M ε τ : ℝ}
    (hε : 0 ≤ ε) (hτ : 0 ≤ τ) (hO : -ε ≤ O)
    (hH : H ≤ M-O+ε) (hA : 0 ≤ A) (hAwidth : 2*A ≤ O+ε)
    (hS : 0 ≤ S) (hN : 0 ≤ N) (hNA : N ≤ A) (hB : 0 ≤ B)
    (hz : z ≤ ell) (hsum : M+ell ≤ 1)
    (hv : 0 ≤ v) (hlb : 0 ≤ lb) (he : -ε ≤ e)
    (hret : v+3*lb+e ≤ dualLength H A z ell θ N B+τ) :
    reflectedEnergy O H A S N B z ell θ v lb e ≤
      M+max 0 ((1+3*ell-2*M)/4)+6*ε+2*|θ|+τ := by
  have hθ : θ ≤ |θ| := le_abs_self θ
  have hθ' : -θ ≤ |θ| := neg_le_abs θ
  have haθ : 0 ≤ |θ| := abs_nonneg θ
  have hT : dualLength H A z ell θ N B ≤ H+2*ε+|θ| := by
    dsimp [dualLength]
    linarith
  have hmax : max H (v+lb) ≤ H+3*ε+|θ|+τ := by
    apply max_le
    · linarith
    · linarith
  have hg0 : 0 ≤ max 0 ((1+3*ell-2*M)/4) := le_max_left _ _
  have hg1 : (1+3*ell-2*M)/4 ≤ max 0 ((1+3*ell-2*M)/4) := le_max_right _ _
  rcases hybrid_minimum_dichotomy hv with hmin | hmin
  · have hk : 0 ≤ max 0 (dualLength H A z ell θ N B-v-3*lb-e) := le_max_left _ _
    dsimp [reflectedEnergy]
    rw [hmin]
    linarith
  · have hk := kernel_quarter_charge (dualLength H A z ell θ N B) (v+3*lb+e)
    have hy : dualLength H A z ell θ N B-(v+3*lb+e) =
        dualLength H A z ell θ N B-v-3*lb-e := by ring
    rw [hy] at hk
    have hcharge : dualLength H A z ell θ N B/4-5*ε/12 ≤
        hybridMinimum v z+lb+2*e/3+
          max 0 (dualLength H A z ell θ N B-v-3*lb-e)/2 := by
      linarith
    dsimp [reflectedEnergy, dualLength]
    dsimp [dualLength] at hcharge
    linarith

/-- Exact identities for every rescaled subset of the perturbed physical probe. -/
theorem perturbed_rescaling_identities (t d : ℝ) :
    ((5/6-t)-2*d)+((1/6+t)-d)-1 = -3*d ∧
    1+3*((1/6+t)-d)-2*((5/6-t)-2*d) = -1/6+5*t+d ∧
    (23/48-t/2)-(17/48-t/2) = 1/8 ∧
    (17/48-t/2)/2-1+(13/16+3*t/2)/6 = -11/16 ∧
    (17/48-t/2)/2+(1/8)/12 = 3/16-t/4 := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩ <;> ring

/-- Scale positivity and the quantitative Gram comparison hold for all subsets. -/
theorem perturbed_scale_margins {t d : ℝ} (ht : t ≤ 1/30) (hd : d ≤ 1/6+t) :
    11/80 ≤ 17/48-t/2-d ∧ 21/80 ≤ 23/48-t/2-d ∧
    2/5 ≤ 5/6-t-2*d ∧ 1/30 ≤ 23/48-t/2-d-11*(1/8)/6 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> linarith

/-- The tuple saving absorbs even the potential squared-row norm loss. -/
theorem perturbed_rescaling_loss {t d : ℝ} (ht : t ≤ 1/30) (hd : 0 ≤ d) :
    -d+max 0 ((-1/6+5*t+d)/4)/2 ≤ -7*d/8 := by
  have hmax : max 0 ((-1/6+5*t+d)/4) ≤ d/4 := by
    exact max_le (by linarith) (by linarith)
  linarith

/-- Actual real powers, rather than a formal exponent name, are bounded here. -/
theorem perturbed_rescaling_power {Z t d : ℝ} (hZ : 1 ≤ Z)
    (ht : t ≤ 1/30) (hd : 0 ≤ d) :
    Z ^ (-d+max 0 ((-1/6+5*t+d)/4)/2) ≤ 1 := by
  apply Real.rpow_le_one_of_one_le_of_nonpos hZ
  have := perturbed_rescaling_loss ht hd
  linarith

#print axioms hybrid_minimum_dichotomy
#print axioms kernel_quarter_charge
#print axioms reflected_energy_upper
#print axioms perturbed_rescaling_identities
#print axioms perturbed_scale_margins
#print axioms perturbed_rescaling_loss
#print axioms perturbed_rescaling_power
end GRHResearch.Analytic
