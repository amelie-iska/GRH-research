import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Matrix.Mul
import Mathlib.Tactic.Ring

/-!
# Exact weighted gain certificates and propagated error budgets

The certificate is the finite family `G *ᵥ w ≤ q * w`, with nonnegative
gain entries and strictly positive weights. The ordered-field statements
apply both to exact rational witnesses and to real gain bounds. No floating
point comparison or approximate decision procedure occurs in these proofs.

The matrix-action theorem derives its estimate from the actual signed sum,
rather than assuming the desired weighted bound. The iteration theorems
allow time-varying gain matrices sharing the same weights and rate and
include an explicit geometric convolution of per-step residuals.

Feasibility alone is not a proof of strict contraction: that interpretation
additionally requires `q < 1` and valid gain bounds on the claimed domain.
For nonlinear updates, the block-error comparison is a separate hypothesis.
These theorems do not verify a parser, a numerical optimizer, the Python
checker, a global Jacobian envelope, or a continuum fluid theorem.
-/

set_option autoImplicit false

namespace WeightedGainContracts

open Matrix
open scoped BigOperators

variable {K ι : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
  [Fintype ι]

/-- Positive denominators make the row-ratio and componentwise certificates
equivalent. For a nonempty finite index set, these are exactly the inequalities
that the maximum row ratio is at most `q`. -/
theorem row_ratio_iff (G : Matrix ι ι K) (w : ι → K) (q : K)
    (hw : ∀ i, 0 < w i) :
    (∀ i, (G *ᵥ w) i / w i ≤ q) ↔
      (∀ i, (G *ᵥ w) i ≤ q * w i) := by
  constructor
  · intro h i
    exact (div_le_iff₀ (hw i)).mp (h i)
  · intro h i
    exact (div_le_iff₀ (hw i)).mpr (h i)

/-- A fixed positive weight vector remains feasible when the rate increases. -/
theorem feasibility_mono (G : Matrix ι ι K) (w : ι → K) (q q' : K)
    (hw : ∀ i, 0 < w i) (hqq' : q ≤ q')
    (hgain : ∀ i, (G *ᵥ w) i ≤ q * w i) :
    ∀ i, (G *ᵥ w) i ≤ q' * w i := by
  intro i
  exact (hgain i).trans (mul_le_mul_of_nonneg_right hqq' (hw i).le)

/-- A nonnegative block-gain comparison propagates a componentwise envelope.
This comparison itself does not use division, so it does not need positive
weights; positivity is needed for the weighted-norm interpretation. -/
theorem gain_bound (G : Matrix ι ι K) (w d d' : ι → K) (q r : K)
    (hG : ∀ i j, 0 ≤ G i j)
    (hgain : ∀ i, (G *ᵥ w) i ≤ q * w i) (hr : 0 ≤ r)
    (hd : ∀ i, d i ≤ r * w i)
    (hstep : ∀ i, d' i ≤ (G *ᵥ d) i) :
    ∀ i, d' i ≤ (q * r) * w i := by
  intro i
  calc
    d' i ≤ ∑ j, G i j * d j := hstep i
    _ ≤ ∑ j, G i j * (r * w j) :=
      Finset.sum_le_sum fun j _ => mul_le_mul_of_nonneg_left (hd j) (hG i j)
    _ = r * (G *ᵥ w) i := by
      simp only [Matrix.mulVec, dotProduct, Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro j _
      ring
    _ ≤ r * (q * w i) := mul_le_mul_of_nonneg_left (hgain i) hr
    _ = (q * r) * w i := by ring

/-- The actual signed matrix sum obeys the certificate's weighted component
bound. Positive weights and the input envelope imply the radius is
nonnegative whenever a coordinate is being considered. -/
theorem matrix_action_weighted_bound (A G : Matrix ι ι K) (w x : ι → K)
    (q r : K) (hw : ∀ i, 0 < w i)
    (hG : ∀ i j, 0 ≤ G i j)
    (hgain : ∀ i, (G *ᵥ w) i ≤ q * w i)
    (hA : ∀ i j, |A i j| ≤ G i j)
    (hx : ∀ i, |x i| ≤ r * w i) :
    ∀ i, |(A *ᵥ x) i| ≤ (q * r) * w i := by
  have hstep : ∀ i, |(A *ᵥ x) i| ≤ (G *ᵥ fun j => |x j|) i := by
    intro i
    calc
      |∑ j, A i j * x j| ≤ ∑ j, |A i j * x j| :=
        Finset.abs_sum_le_sum_abs _ _
      _ ≤ ∑ j, G i j * |x j| := by
        apply Finset.sum_le_sum
        intro j _
        rw [abs_mul]
        exact mul_le_mul_of_nonneg_right (hA i j) (abs_nonneg _)
  intro i
  have hr : 0 ≤ r := (mul_nonneg_iff_of_pos_right (hw i)).mp
    ((abs_nonneg (x i)).trans (hx i))
  exact gain_bound G w (fun j => |x j|) (fun j => |(A *ᵥ x) j|)
    q r hG hgain hr hx hstep i

/-- Initial error multiplied by the common gain, plus every residual
multiplied by the gains of its remaining time steps. -/
noncomputable def errorBudget (q r₀ : K) (δ : ℕ → K) (n : ℕ) : K :=
  q ^ n * r₀ + ∑ k ∈ Finset.range n, q ^ (n - (k + 1)) * δ k

private theorem errorBudget_nonneg (q r₀ : K) (δ : ℕ → K)
    (hq : 0 ≤ q) (hr₀ : 0 ≤ r₀) (hδ : ∀ k, 0 ≤ δ k) (n : ℕ) :
    0 ≤ errorBudget q r₀ δ n := by
  apply add_nonneg (mul_nonneg (pow_nonneg hq n) hr₀)
  exact Finset.sum_nonneg fun k _ => mul_nonneg (pow_nonneg hq _) (hδ k)

omit [LinearOrder K] [IsStrictOrderedRing K] in
private theorem errorBudget_succ (q r₀ : K) (δ : ℕ → K) (n : ℕ) :
    errorBudget q r₀ δ (n + 1) = q * errorBudget q r₀ δ n + δ n := by
  unfold errorBudget
  rw [Finset.sum_range_succ]
  have hsum : (∑ k ∈ Finset.range n, q ^ (n + 1 - (k + 1)) * δ k) =
      q * ∑ k ∈ Finset.range n, q ^ (n - (k + 1)) * δ k := by
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro k hk
    have hklt := Finset.mem_range.mp hk
    have hexp : n + 1 - (k + 1) = (n - (k + 1)) + 1 := by omega
    rw [hexp, pow_succ]
    ring
  rw [hsum]
  simp only [Nat.sub_self, pow_zero, one_mul, pow_succ]
  ring

/-- Time-varying block gains with a common certificate propagate the exact
finite-time geometric residual budget. Nonlinear applications must separately
establish `hstep` along the trajectories or on an invariant domain. -/
theorem gain_iteration_with_residual (G : ℕ → Matrix ι ι K)
    (w : ι → K) (q r₀ : K) (δ : ℕ → K) (d : ℕ → ι → K)
    (hG : ∀ n i j, 0 ≤ G n i j)
    (hgain : ∀ n i, (G n *ᵥ w) i ≤ q * w i)
    (hq : 0 ≤ q) (hr₀ : 0 ≤ r₀) (hδ : ∀ n, 0 ≤ δ n)
    (hzero : ∀ i, d 0 i ≤ r₀ * w i)
    (hstep : ∀ n i, d (n + 1) i ≤ (G n *ᵥ d n) i + δ n * w i) :
    ∀ n i, d n i ≤ errorBudget q r₀ δ n * w i := by
  intro n
  induction n with
  | zero => simpa [errorBudget] using hzero
  | succ n ih =>
    intro i
    have hlinear := gain_bound (G n) w (d n) (G n *ᵥ d n)
      q (errorBudget q r₀ δ n) (hG n) (hgain n)
      (errorBudget_nonneg q r₀ δ hq hr₀ hδ n) ih (fun _ => le_rfl) i
    calc
      d (n + 1) i ≤ (G n *ᵥ d n) i + δ n * w i := hstep n i
      _ ≤ (q * errorBudget q r₀ δ n) * w i + δ n * w i :=
        add_le_add_right hlinear _
      _ = errorBudget q r₀ δ (n + 1) * w i := by
        rw [errorBudget_succ]
        ring

/-- The actual inhomogeneous, time-varying matrix recurrence satisfies the
budget, including every signed perturbation. The same statement with zero
residual radii yields `q^n * r₀ * w i` without any commutativity assumption. -/
theorem matrix_iteration_with_residual (A G : ℕ → Matrix ι ι K)
    (w : ι → K) (q r₀ : K) (δ : ℕ → K) (u e : ℕ → ι → K)
    (hG : ∀ n i j, 0 ≤ G n i j)
    (hgain : ∀ n i, (G n *ᵥ w) i ≤ q * w i)
    (hA : ∀ n i j, |A n i j| ≤ G n i j)
    (hq : 0 ≤ q) (hr₀ : 0 ≤ r₀) (hδ : ∀ n, 0 ≤ δ n)
    (hzero : ∀ i, |u 0 i| ≤ r₀ * w i)
    (he : ∀ n i, |e n i| ≤ δ n * w i)
    (hu : ∀ n, u (n + 1) = A n *ᵥ u n + e n) :
    ∀ n i, |u n i| ≤ errorBudget q r₀ δ n * w i := by
  apply gain_iteration_with_residual G w q r₀ δ (fun n i => |u n i|)
    hG hgain hq hr₀ hδ hzero
  intro n i
  rw [hu]
  calc
    |(A n *ᵥ u n + e n) i| ≤ |(A n *ᵥ u n) i| + |e n i| := abs_add_le _ _
    _ ≤ (G n *ᵥ fun j => |u n j|) i + δ n * w i := by
      apply add_le_add _ (he n i)
      calc
        |∑ j, A n i j * u n j| ≤ ∑ j, |A n i j * u n j| :=
          Finset.abs_sum_le_sum_abs _ _
        _ ≤ ∑ j, G n i j * |u n j| := by
          apply Finset.sum_le_sum
          intro j _
          rw [abs_mul]
          exact mul_le_mul_of_nonneg_right (hA n i j) (abs_nonneg _)

end WeightedGainContracts
