import Mathlib.Algebra.Polynomial.Degree.TrailingDegree
import Mathlib.Analysis.Normed.Group.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# Exact reduction contracts and signed tropical cancellation

The factorization theorem characterizes when retained information suffices for
an exact deterministic output. Its dynamical specialization concerns discrete
state updates. For continuous-time vector fields, the analogous observed
derivative is `D P(x) F(x)`; it is `P (F x)` only when `P` is linear.

The polynomial examples use the order of vanishing at zero, with the correct
value infinity for the zero polynomial. They prove that signed cancellations
can raise order by an arbitrarily large amount even when both summands and
their sum are nonzero. A minimum of the two orders cannot certify a residual
cancellation. This is an exact symbolic obstruction, not a numerical example.

These results add no continuum Navier--Stokes or arithmetic hypothesis and do
not assert a new fluid blowup, GRH, or Yang--Mills theorem.
-/

set_option autoImplicit false

namespace ReductionContracts

section Fibers

variable {A B C : Type*}

/-- An output is retained exactly when it is constant on the observation fibers.
Surjectivity specifies the reduced state space as the actual observation image. -/
theorem factorization_iff_fiber_constant
    (P : A → B) (Q : A → C) (hP : Function.Surjective P) :
    (∃ G : B → C, ∀ x, G (P x) = Q x) ↔
      (∀ x y, P x = P y → Q x = Q y) := by
  constructor
  · rintro ⟨G, hG⟩ x y hxy
    rw [← hG x, ← hG y, hxy]
  · intro hQ
    classical
    refine ⟨fun b => Q (Classical.choose (hP b)), ?_⟩
    intro x
    exact hQ _ x (Classical.choose_spec (hP (P x)))

/-- The reduced output is unique on a surjective observation space. -/
theorem reduced_output_unique
    (P : A → B) (Q : A → C) (hP : Function.Surjective P)
    (G H : B → C) (hG : ∀ x, G (P x) = Q x)
    (hH : ∀ x, H (P x) = Q x) : G = H := by
  funext b
  obtain ⟨x, rfl⟩ := hP b
  exact (hG x).trans (hH x).symm

/-- Exact discrete closure is equivalent to preservation of observation fibers. -/
theorem discrete_closure_iff
    (P : A → B) (F : A → A) (hP : Function.Surjective P) :
    (∃ G : B → B, ∀ x, G (P x) = P (F x)) ↔
      (∀ x y, P x = P y → P (F x) = P (F y)) :=
  factorization_iff_fiber_constant P (fun x => P (F x)) hP

/-- One mismatched fiber rules out every deterministic memoryless closure. -/
theorem mismatched_fiber_excludes_closure
    (P : A → B) (Q : A → C) (x y : A)
    (hxy : P x = P y) (hQ : Q x ≠ Q y) :
    ¬ ∃ G : B → C, ∀ a, G (P a) = Q a := by
  rintro ⟨G, hG⟩
  apply hQ
  rw [← hG x, ← hG y, hxy]

/-- A commuting update diagram intertwines every finite trajectory exactly. -/
theorem discrete_trajectory_preserved
    (P : A → B) (F : A → A) (G : B → B)
    (hcomm : ∀ x, P (F x) = G (P x))
    (u : ℕ → A) (v : ℕ → B)
    (hu : ∀ n, u (n + 1) = F (u n))
    (hv : ∀ n, v (n + 1) = G (v n))
    (hzero : P (u 0) = v 0) : ∀ n, P (u n) = v n := by
  intro n
  induction n with
  | zero => exact hzero
  | succ n ih => rw [hu, hv, hcomm, ih]

end Fibers

section ApproximateClosure

variable {A B V : Type*} [SeminormedAddCommGroup V]

/-- The separation of two unresolved outputs lower-bounds the sum of errors. -/
theorem fiber_error_lower_bound
    (P : A → B) (Q : A → V) (G : B → V) (x y : A)
    (hxy : P x = P y) :
    ‖Q x - Q y‖ ≤ ‖Q x - G (P x)‖ + ‖Q y - G (P y)‖ := by
  rw [← hxy]
  have htriangle := norm_add_le (Q x - G (P x)) (G (P x) - Q y)
  rw [sub_add_sub_cancel] at htriangle
  simpa only [norm_sub_rev (G (P x)) (Q y)] using
    htriangle

/-- Uniform error epsilon on a fiber requires diameter at most 2 epsilon. -/
theorem fiber_diameter_le_twice_error
    (P : A → B) (Q : A → V) (G : B → V) (x y : A) (ε : ℝ)
    (hxy : P x = P y)
    (hx : ‖Q x - G (P x)‖ ≤ ε) (hy : ‖Q y - G (P y)‖ ≤ ε) :
    ‖Q x - Q y‖ ≤ 2 * ε := by
  calc
    ‖Q x - Q y‖ ≤ ‖Q x - G (P x)‖ + ‖Q y - G (P y)‖ :=
      fiber_error_lower_bound P Q G x y hxy
    _ ≤ ε + ε := add_le_add hx hy
    _ = 2 * ε := by ring

end ApproximateClosure

section SignedOrders

open Polynomial

/-- A signed polynomial with leading term `-X` and an arbitrary later term. -/
noncomputable def signedPartner (k : ℕ) : Polynomial ℚ := -X + X ^ (k + 2)

theorem signedPartner_constant_coefficient (k : ℕ) :
    (signedPartner k).coeff 0 = 0 := by
  simp [signedPartner, Polynomial.coeff_X_pow]

theorem signedPartner_linear_coefficient (k : ℕ) :
    (signedPartner k).coeff 1 = -1 := by
  simp [signedPartner, Polynomial.coeff_X_pow]

theorem signedPartner_ne_zero (k : ℕ) : signedPartner k ≠ 0 := by
  intro h
  have hc := signedPartner_linear_coefficient k
  rw [h, Polynomial.coeff_zero] at hc
  norm_num at hc

/-- Both summands have order one, independent of the eventual residual order. -/
theorem signedPartner_order (k : ℕ) : (signedPartner k).trailingDegree = 1 := by
  apply (Polynomial.trailingDegree_eq_iff_natTrailingDegree_eq
    (signedPartner_ne_zero k)).2
  apply le_antisymm
  · apply Polynomial.natTrailingDegree_le_of_ne_zero
    rw [signedPartner_linear_coefficient]
    norm_num
  · apply Polynomial.le_natTrailingDegree (signedPartner_ne_zero k)
    intro m hm
    have hm0 : m = 0 := by omega
    subst m
    exact signedPartner_constant_coefficient k

theorem signed_cancellation_identity (k : ℕ) :
    (X : Polynomial ℚ) + signedPartner k = X ^ (k + 2) := by
  simp [signedPartner]

theorem signed_cancellation_sum_ne_zero (k : ℕ) :
    (X : Polynomial ℚ) + signedPartner k ≠ 0 := by
  rw [signed_cancellation_identity]
  exact pow_ne_zero _ Polynomial.X_ne_zero

/-- Cancellation raises the exact order to any prescribed integer at least two. -/
theorem signed_cancellation_order (k : ℕ) :
    ((X : Polynomial ℚ) + signedPartner k).trailingDegree = (k + 2 : ℕ) := by
  rw [signed_cancellation_identity, Polynomial.trailingDegree_X_pow]

/-- A strict inequality holds with no zero summand or zero residual. -/
theorem signed_cancellation_strict (k : ℕ) :
    min (X : Polynomial ℚ).trailingDegree (signedPartner k).trailingDegree <
      ((X : Polynomial ℚ) + signedPartner k).trailingDegree := by
  rw [Polynomial.trailingDegree_X, signedPartner_order, signed_cancellation_order,
    min_self]
  exact_mod_cast (show 1 < k + 2 by omega)

/-- Therefore minimum-of-orders is not an exact rule for signed addition. -/
theorem no_universal_minimum_rule :
    ¬ ∀ p q : Polynomial ℚ, p ≠ 0 → q ≠ 0 → p + q ≠ 0 →
      (p + q).trailingDegree = min p.trailingDegree q.trailingDegree := by
  intro h
  have heq := h X (signedPartner 0) Polynomial.X_ne_zero
    (signedPartner_ne_zero 0) (signed_cancellation_sum_ne_zero 0)
  exact (ne_of_gt (signed_cancellation_strict 0)) heq

end SignedOrders

end ReductionContracts

#print axioms ReductionContracts.factorization_iff_fiber_constant
#print axioms ReductionContracts.reduced_output_unique
#print axioms ReductionContracts.discrete_closure_iff
#print axioms ReductionContracts.mismatched_fiber_excludes_closure
#print axioms ReductionContracts.discrete_trajectory_preserved
#print axioms ReductionContracts.fiber_error_lower_bound
#print axioms ReductionContracts.fiber_diameter_le_twice_error
#print axioms ReductionContracts.signedPartner_constant_coefficient
#print axioms ReductionContracts.signedPartner_linear_coefficient
#print axioms ReductionContracts.signedPartner_ne_zero
#print axioms ReductionContracts.signedPartner_order
#print axioms ReductionContracts.signed_cancellation_identity
#print axioms ReductionContracts.signed_cancellation_sum_ne_zero
#print axioms ReductionContracts.signed_cancellation_order
#print axioms ReductionContracts.signed_cancellation_strict
#print axioms ReductionContracts.no_universal_minimum_rule
