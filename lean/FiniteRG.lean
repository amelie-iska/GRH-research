import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic.Linarith

namespace GRHResearch.FiniteRG
open Finset
noncomputable section
variable {U V W : Type*} [Fintype V] [Fintype W]

def marginal (w : U → V → ℝ) (u : U) : ℝ := ∑ v, w u v
def effectiveAction (A : U → V → ℝ) (u : U) : ℝ :=
  Real.log (marginal (fun u v => Real.exp (A u v)) u)

theorem marginal_nonneg (w : U → V → ℝ) (hw : ∀ u v, 0 ≤ w u v) (u : U) :
    0 ≤ marginal w u := by
  exact Finset.sum_nonneg fun v _ => hw u v

theorem gibbs_marginal_pos [Nonempty V] (A : U → V → ℝ) (u : U) :
    0 < marginal (fun u v => Real.exp (A u v)) u := by
  exact Finset.sum_pos (fun v _ => Real.exp_pos (A u v)) Finset.univ_nonempty

/-- The full unnormalized action includes its additive constant. -/
theorem exp_effective_action [Nonempty V] (A : U → V → ℝ) (u : U) :
    Real.exp (effectiveAction A u) = marginal (fun u v => Real.exp (A u v)) u := by
  exact Real.exp_log (gibbs_marginal_pos A u)

theorem partition_exact [Fintype U] [Nonempty V] (A : U → V → ℝ) :
    (∑ u, Real.exp (effectiveAction A u)) = ∑ p : U × V, Real.exp (A p.1 p.2) := by
  simp only [exp_effective_action, marginal, Fintype.sum_prod_type]

theorem retained_observable_exact [Fintype U] (w : U → V → ℝ) (O : U → ℝ) :
    (∑ u, marginal w u * O u) = ∑ p : U × V, w p.1 p.2 * O p.1 := by
  simp only [marginal, Finset.sum_mul, Fintype.sum_prod_type]

theorem nested_marginal (w : U → V → W → ℝ) (u : U) :
    marginal (fun u v => marginal (fun v z => w u v z) v) u =
      marginal (fun (u : U) (p : V × W) => w u p.1 p.2) u := by
  simp only [marginal, Fintype.sum_prod_type]

/-- A pointwise positive-weight sandwich survives exactly the same elimination. -/
theorem marginal_sandwich (w wh : U → V → ℝ) (lo hi : ℝ)
    (hlo : ∀ u v, lo * w u v ≤ wh u v)
    (hhi : ∀ u v, wh u v ≤ hi * w u v) (u : U) :
    lo * marginal w u ≤ marginal wh u ∧ marginal wh u ≤ hi * marginal w u := by
  constructor
  · simp only [marginal, Finset.mul_sum]
    exact Finset.sum_le_sum fun v _ => hlo u v
  · simp only [marginal, Finset.mul_sum]
    exact Finset.sum_le_sum fun v _ => hhi u v

/-- This is a classical scalar action bound, not a noncommutative exponential claim. -/
theorem gibbs_error_sandwich (A Ah : U → V → ℝ) (ε : ℝ)
    (h : ∀ u v, |Ah u v - A u v| ≤ ε) (u : U) :
    Real.exp (-ε) * marginal (fun u v => Real.exp (A u v)) u ≤
        marginal (fun u v => Real.exp (Ah u v)) u ∧
      marginal (fun u v => Real.exp (Ah u v)) u ≤
        Real.exp ε * marginal (fun u v => Real.exp (A u v)) u := by
  apply marginal_sandwich
  · intro u v
    rw [← Real.exp_add]
    apply Real.exp_le_exp.mpr
    have hh := (abs_le.mp (h u v)).1
    linarith
  · intro u v
    rw [← Real.exp_add]
    apply Real.exp_le_exp.mpr
    have hh := (abs_le.mp (h u v)).2
    linarith

/-- The even periodic chain partition is retained by T -> T squared. -/
theorem transfer_partition_step {I : Type*} [Fintype I] [DecidableEq I]
    (T : Matrix I I ℝ) (n : ℕ) :
    Matrix.trace ((T * T) ^ n) = Matrix.trace (T ^ (2 * n)) := by
  rw [pow_mul, pow_two]

#check marginal_nonneg
#check gibbs_marginal_pos
#check exp_effective_action
#check partition_exact
#check retained_observable_exact
#check nested_marginal
#check marginal_sandwich
#check gibbs_error_sandwich
#check transfer_partition_step
#print axioms marginal_nonneg
#print axioms gibbs_marginal_pos
#print axioms exp_effective_action
#print axioms partition_exact
#print axioms retained_observable_exact
#print axioms nested_marginal
#print axioms marginal_sandwich
#print axioms gibbs_error_sandwich
#print axioms transfer_partition_step
end
end GRHResearch.FiniteRG
