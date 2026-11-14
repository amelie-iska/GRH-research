import Mathlib.MeasureTheory.Measure.MeasureSpace
import Mathlib.Tactic

/-! Finite-search risk bounds. Event-level calibration and model discrepancy
are explicit premises. No assertion about observed CMB data, exchangeability,
CCC truth, optional stopping, or estimated covariance is inferred here. -/
set_option autoImplicit false
open MeasureTheory
open scoped ENNReal BigOperators
namespace WorkbenchRisk
variable {Ω ι : Type*} [MeasurableSpace Ω] [Fintype ι]

theorem familywise_bound (μ : Measure Ω) (A : ι → Set Ω)
    (p : ι → ℝ≥0∞) (h : ∀ i, μ (A i) ≤ p i) :
    μ (⋃ i, A i) ≤ ∑ i, p i := by
  exact (measure_iUnion_fintype_le μ A).trans (Finset.sum_le_sum (fun i _ => h i))

theorem rejection_subset_bound (μ : Measure Ω) (A : ι → Set Ω)
    (p : ι → ℝ≥0∞) (reject : Set Ω)
    (hsubset : reject ⊆ ⋃ i, A i) (h : ∀ i, μ (A i) ≤ p i) :
    μ reject ≤ ∑ i, p i := by
  exact (measure_mono hsubset).trans (familywise_bound μ A p h)

theorem model_discrepancy_bound (μ ν : Measure Ω) (A : ι → Set Ω)
    (p : ι → ℝ≥0∞) (δ : ℝ≥0∞)
    (h : ∀ i, μ (A i) ≤ p i)
    (hmodel : ν (⋃ i, A i) ≤ μ (⋃ i, A i) + δ) :
    ν (⋃ i, A i) ≤ (∑ i, p i) + δ := by
  exact hmodel.trans (add_le_add_right (familywise_bound μ A p h) δ)

theorem budget_bound (μ ν : Measure Ω) (A : ι → Set Ω)
    (p : ι → ℝ≥0∞) (δ α : ℝ≥0∞)
    (h : ∀ i, μ (A i) ≤ p i)
    (hmodel : ν (⋃ i, A i) ≤ μ (⋃ i, A i) + δ)
    (hbudget : (∑ i, p i) + δ ≤ α) : ν (⋃ i, A i) ≤ α := by
  exact (model_discrepancy_bound μ ν A p δ h hmodel).trans hbudget

end WorkbenchRisk
#check WorkbenchRisk.familywise_bound
#check WorkbenchRisk.rejection_subset_bound
#check WorkbenchRisk.model_discrepancy_bound
#check WorkbenchRisk.budget_bound
#print axioms WorkbenchRisk.familywise_bound
#print axioms WorkbenchRisk.rejection_subset_bound
#print axioms WorkbenchRisk.model_discrepancy_bound
#print axioms WorkbenchRisk.budget_bound
