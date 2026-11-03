import Mathlib.Analysis.SpecialFunctions.Pow.Complex

namespace GRHResearch.Analytic

/-- A finite complex moment and pointwise spikes give an actual cardinality bound.
Arithmetic moment estimates and witness construction are not assumed proved here. -/
theorem count_from_complex_moment {ι : Type*} (F : Finset ι) (w p : ι → ℂ)
    {A B M : ℝ} (hB : 0 ≤ B)
    (hw : ∀ i ∈ F, A ≤ ‖w i‖ ^ 2) (hp : ∀ i ∈ F, B ≤ ‖p i‖ ^ 2)
    (hm : (∑ i ∈ F, ‖w i * p i‖ ^ 2) ≤ M) :
    (F.card : ℝ) * A * B ≤ M := by
  calc
    (F.card : ℝ) * A * B = ∑ _i ∈ F, A * B := by simp [mul_assoc]
    _ ≤ ∑ i ∈ F, ‖w i * p i‖ ^ 2 := by
      apply Finset.sum_le_sum
      intro i hi
      rw [norm_mul, mul_pow]
      exact mul_le_mul (hw i hi) (hp i hi) hB (sq_nonneg _)
    _ ≤ M := hm

/-- The endpoint kappa=3/4 is permitted by the inherited fourth-moment statement.
This checks its exact capacity, not the fourth-moment estimate itself. -/
theorem frozen_plain_capacity (m : ℝ) :
    2*m + 6*(3/4 : ℝ)*((1-2*m)/(9/2 : ℝ)) = 1 := by ring

noncomputable def rowD (x : ℝ) : ℝ := 3-17*x/9
noncomputable def rowP (x : ℝ) : ℝ := (2-8*x/9)*(1-x)
noncomputable def rowCrossing (x τ : ℝ) : ℝ := ((2-8*x/9)*τ-5*x/9)/rowD x

theorem frozen_row_coefficients {x : ℝ} (hx1 : x ≤ 1/2) :
    37/18 ≤ rowD x ∧ 7/9 ≤ rowP x := by
  dsimp [rowD, rowP]
  constructor
  · linarith
  · nlinarith [sq_nonneg (x-1/2)]

/-- Uniform crossing bounds supply the positive marked-moment margin and the
7/37 maximum requested inverse slot length. -/
theorem frozen_crossing_bounds {x τ : ℝ} (hx0 : 0 ≤ x) (hx1 : x ≤ 1/2)
    (ht0 : 1 ≤ τ) (ht1 : τ ≤ 3/2) :
    23/37 ≤ rowCrossing x τ ∧ rowCrossing x τ ≤ 1 ∧
      1/3 ≤ τ-rowCrossing x τ ∧ τ-rowCrossing x τ ≤ 1/2 := by
  have hD : 0 < rowD x := by
    have := (frozen_row_coefficients hx1).1
    linarith
  have hB : 0 < 2-8*x/9 := by linarith
  have hC : 0 ≤ 1-x := by linarith
  have hmul0 := mul_le_mul_of_nonneg_left ht0 (le_of_lt hB)
  have hmul1 := mul_le_mul_of_nonneg_left ht1 (le_of_lt hB)
  have hmul2 := mul_le_mul_of_nonneg_left ht0 hC
  have hmul3 := mul_le_mul_of_nonneg_left ht1 hC
  have heq : τ-rowCrossing x τ = ((1-x)*τ+5*x/9)/rowD x := by
    apply (eq_div_iff (ne_of_gt hD)).mpr
    rw [sub_mul, rowCrossing, div_mul_cancel₀ _ (ne_of_gt hD)]
    dsimp [rowD]
    ring
  constructor
  · apply (le_div_iff₀ hD).mpr
    dsimp [rowD] at *
    linarith
  constructor
  · apply (div_le_iff₀ hD).mpr
    dsimp [rowD] at *
    linarith
  rw [heq]
  constructor
  · apply (le_div_iff₀ hD).mpr
    dsimp [rowD] at *
    linarith
  · apply (div_le_iff₀ hD).mpr
    dsimp [rowD] at *
    linarith

/-- The selected inverse and plain affine counts cross at exactly the same value. -/
theorem frozen_short_crossing {x : ℝ} (hD : rowD x ≠ 0) (δ τ : ℝ) :
    (1-δ*(x+(1-x)*rowCrossing x τ)) =
      1-δ+δ*rowP x/rowD x*(3/2-τ) ∧
    (1-δ*(4*x/9+(2-8*x/9)*(τ-rowCrossing x τ))) =
      1-δ+δ*rowP x/rowD x*(3/2-τ) := by
  constructor <;> dsimp only [rowCrossing] <;> field_simp [hD] <;>
    dsimp [rowD, rowP] <;> ring

/-- Balance the short and long counts without a Delta/4 capacity loss. -/
theorem frozen_balanced_cutoff {δ x : ℝ} (hδ0 : 0 ≤ δ) (hδ1 : δ ≤ 3/4)
    (hx1 : x ≤ 1/2) :
    let J := (5/6-δ)*rowD x+δ*rowP x
    let τ := 1+δ*rowP x/(2*J)
    0 < J ∧ 1 ≤ τ ∧ τ < 3/2 ∧
      1-δ+δ*rowP x/rowD x*(3/2-τ) = 1-δ+(5/6-δ)*(τ-1) := by
  dsimp only
  have hcoef := frozen_row_coefficients hx1
  have hD : 0 < rowD x := by linarith [hcoef.1]
  have hP : 0 < rowP x := by linarith [hcoef.2]
  have hα : 0 < (5/6 : ℝ)-δ := by linarith
  have hDP : 0 < (5/6-δ)*rowD x := mul_pos hα hD
  have hδP : 0 ≤ δ*rowP x := mul_nonneg hδ0 (le_of_lt hP)
  have hJ : 0 < (5/6-δ)*rowD x+δ*rowP x := by linarith
  refine ⟨hJ, ?_, ?_, ?_⟩
  · exact le_add_of_nonneg_right (div_nonneg hδP (by positivity))
  · have : δ*rowP x/(2*((5/6-δ)*rowD x+δ*rowP x)) < 1/2 := by
      apply (div_lt_iff₀ (by positivity)).mpr
      nlinarith
    linarith
  · generalize hj : (5/6-δ)*rowD x+δ*rowP x = j at *
    field_simp [ne_of_gt hJ, ne_of_gt hD]
    nlinarith [hj]

/-- A slot supply margin persists above the perturbed central endpoint. -/
theorem frozen_supply_margin {t ζ : ℝ} (hζ : ζ < 23/336+53*t/14) :
    (7/37 : ℝ)*(13/16+3*t/2+ζ) < 1/6+t := by linarith

#print axioms count_from_complex_moment
#print axioms frozen_plain_capacity
#print axioms frozen_row_coefficients
#print axioms frozen_crossing_bounds
#print axioms frozen_short_crossing
#print axioms frozen_balanced_cutoff
#print axioms frozen_supply_margin
end GRHResearch.Analytic
