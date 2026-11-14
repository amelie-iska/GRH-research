import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.MeasureTheory.Measure.Typeclasses.Probability
import Mathlib.Tactic.Linarith

/-!
# Finite-search false-positive bounds with explicit probability assumptions

The browser's statistic is the maximum of a fixed finite family of real
matched-filter scores. Exceedance of a common threshold is therefore the
union of the corresponding score events. These results prove finite-family
subadditivity and derive full-search bounds from actual integrable absolute
even moments. They require no independence between the scores.

The Gaussian moment formula, the null law of a numerical generator, and a
match between that law and the exported filter model are separate obligations.
In particular, these theorems do not certify the empirical calibration ranks,
exchangeability of a stored sample, a pseudorandom generator, or observational
cosmology. A threshold chosen after seeing the same score vector does not
automatically satisfy a theorem stated for a fixed threshold.

The natural parameter `k` gives moment order `2*k`. The mathematical theorem
also permits `k = 0`, where it is normally trivial; the live interface uses
positive orders. The real-valued measure is a probability because the
`IsProbabilityMeasure` instance is an explicit assumption.
-/

set_option autoImplicit false

namespace CosmologyCalibration

open MeasureTheory
open scoped BigOperators

variable {Ω ι : Type*} [MeasurableSpace Ω]

/-- A positive full scan rejects when at least one declared score crosses
the same fixed threshold. This includes ties, as does the browser's `>=`. -/
def scanEvent (tests : Finset ι) (score : ι → Ω → ℝ) (threshold : ℝ) : Set Ω :=
  {ω | ∃ j ∈ tests, threshold ≤ score j ω}

/-- Measurable per-test events and per-test false-positive bounds give a
familywise bound. Neither disjointness nor independence is assumed. -/
theorem finite_family_false_positive_bound (μ : Measure Ω) [IsProbabilityMeasure μ]
    (tests : Finset ι) (events : ι → Set Ω) (budget : ι → ℝ)
    (hmeas : ∀ j ∈ tests, MeasurableSet (events j))
    (htail : ∀ j ∈ tests, μ.real (events j) ≤ budget j) :
    MeasurableSet (⋃ j ∈ tests, events j) ∧
      μ.real (⋃ j ∈ tests, events j) ≤ min 1 (∑ j ∈ tests, budget j) := by
  refine ⟨MeasurableSet.biUnion tests.finite_toSet.countable hmeas, ?_⟩
  apply le_min measureReal_le_one
  exact (measureReal_biUnion_finset_le tests events).trans
    (Finset.sum_le_sum htail)

private theorem one_sided_even_moment_bound (μ : Measure Ω) [IsProbabilityMeasure μ]
    (X : Ω → ℝ) (k : ℕ) (t M : ℝ) (ht : 0 < t)
    (hint : Integrable (fun ω => |X ω| ^ (2 * k)) μ)
    (hmoment : (∫ ω, |X ω| ^ (2 * k) ∂μ) ≤ M) :
    μ.real {ω | t ≤ X ω} ≤ M / t ^ (2 * k) := by
  have hsub : {ω | t ≤ X ω} ⊆ {ω | t ^ (2 * k) ≤ |X ω| ^ (2 * k)} := by
    intro ω hω
    exact pow_le_pow_left₀ ht.le (hω.trans (le_abs_self _)) _
  have hmarkov := mul_meas_ge_le_integral_of_nonneg
    (μ := μ) (f := fun ω => |X ω| ^ (2 * k))
    (Filter.Eventually.of_forall fun ω => pow_nonneg (abs_nonneg (X ω)) _)
    hint (t ^ (2 * k))
  have htail : μ.real {ω | t ^ (2 * k) ≤ |X ω| ^ (2 * k)} ≤ M / t ^ (2 * k) := by
    apply (le_div_iff₀ (pow_pos ht _)).mpr
    simpa only [mul_comm] using hmarkov.trans hmoment
  exact (measureReal_mono hsub).trans htail

/-- Each score's integrable absolute even moment controls its one-sided
tail, and finite subadditivity controls the actual complete scan. -/
theorem scan_even_moment_bound (μ : Measure Ω) [IsProbabilityMeasure μ]
    (tests : Finset ι) (score : ι → Ω → ℝ) (k : ℕ) (t : ℝ) (M : ι → ℝ)
    (ht : 0 < t) (hmeas : ∀ j ∈ tests, Measurable (score j))
    (hint : ∀ j ∈ tests, Integrable (fun ω => |score j ω| ^ (2 * k)) μ)
    (hmoment : ∀ j ∈ tests, (∫ ω, |score j ω| ^ (2 * k) ∂μ) ≤ M j) :
    MeasurableSet (scanEvent tests score t) ∧
      μ.real (scanEvent tests score t) ≤ min 1 ((∑ j ∈ tests, M j) / t ^ (2 * k)) := by
  have hset : scanEvent tests score t = ⋃ j ∈ tests, {ω | t ≤ score j ω} := by
    ext ω
    simp [scanEvent]
  rw [hset]
  have h := finite_family_false_positive_bound μ tests (fun j => {ω | t ≤ score j ω})
    (fun j => M j / t ^ (2 * k))
    (fun j hj => measurableSet_le measurable_const (hmeas j hj))
    (fun j hj => one_sided_even_moment_bound μ (score j) k t (M j) ht
      (hint j hj) (hmoment j hj))
  simpa only [← Finset.sum_div] using h

/-- The uniform-moment specialization used by the exact scalar runtime
certificate. `M` must bound a true moment of every declared score. -/
theorem scan_uniform_even_moment_bound (μ : Measure Ω) [IsProbabilityMeasure μ]
    (tests : Finset ι) (score : ι → Ω → ℝ) (k : ℕ) (t M : ℝ)
    (ht : 0 < t) (hmeas : ∀ j ∈ tests, Measurable (score j))
    (hint : ∀ j ∈ tests, Integrable (fun ω => |score j ω| ^ (2 * k)) μ)
    (hmoment : ∀ j ∈ tests, (∫ ω, |score j ω| ^ (2 * k) ∂μ) ≤ M) :
    MeasurableSet (scanEvent tests score t) ∧
      μ.real (scanEvent tests score t) ≤ min 1 ((tests.card : ℝ) * M / t ^ (2 * k)) := by
  simpa only [Finset.sum_const, nsmul_eq_mul] using
    scan_even_moment_bound μ tests score k t (fun _ => M) ht hmeas hint hmoment

/-- A replayable exact scalar inequality implies the desired probability
budget under the explicit measurable-score and moment assumptions. -/
theorem scan_even_moment_threshold (μ : Measure Ω) [IsProbabilityMeasure μ]
    (tests : Finset ι) (score : ι → Ω → ℝ) (k : ℕ) (t M α : ℝ)
    (ht : 0 < t) (hmeas : ∀ j ∈ tests, Measurable (score j))
    (hint : ∀ j ∈ tests, Integrable (fun ω => |score j ω| ^ (2 * k)) μ)
    (hmoment : ∀ j ∈ tests, (∫ ω, |score j ω| ^ (2 * k) ∂μ) ≤ M)
    (hbudget : (tests.card : ℝ) * M ≤ α * t ^ (2 * k)) :
    MeasurableSet (scanEvent tests score t) ∧
      μ.real (scanEvent tests score t) ≤ α := by
  have h := scan_uniform_even_moment_bound μ tests score k t M ht hmeas hint hmoment
  refine ⟨h.1, (h.2.trans (min_le_right _ _)).trans ?_⟩
  exact (div_le_iff₀ (pow_pos ht _)).mpr hbudget

/-- The exact finite arithmetic used for the stored calibration rank.
This definition is not a claim about the distribution of a rank. -/
def rankFraction (draws exceedances : ℕ) : ℚ :=
  (1 + (exceedances : ℚ)) / ((draws : ℚ) + 1)

/-- A legitimate count gives a positive rank fraction, its exact resolution
floor, and an upper bound of one. No sampling law is assumed or concluded. -/
theorem rank_fraction_bounds (draws exceedances : ℕ) (hcount : exceedances ≤ draws) :
    0 < rankFraction draws exceedances ∧
      1 / ((draws : ℚ) + 1) ≤ rankFraction draws exceedances ∧
      rankFraction draws exceedances ≤ 1 := by
  have hden : (0 : ℚ) < (draws : ℚ) + 1 := by positivity
  unfold rankFraction
  refine ⟨div_pos (by positivity) hden, ?_, ?_⟩
  · exact div_le_div_of_nonneg_right (le_add_of_nonneg_right (Nat.cast_nonneg _)) hden.le
  · apply (div_le_iff₀ hden).mpr
    have hc : (exceedances : ℚ) ≤ (draws : ℚ) := by exact_mod_cast hcount
    linarith

/-- The exact denominator-clearing rule replayed by a finite rank witness.
It says nothing about exchangeability or a false-positive probability. -/
theorem rank_fraction_threshold_iff (draws exceedances : ℕ) (α : ℚ) :
    rankFraction draws exceedances ≤ α ↔
      1 + (exceedances : ℚ) ≤ α * ((draws : ℚ) + 1) := by
  exact div_le_iff₀ (by positivity)

end CosmologyCalibration
