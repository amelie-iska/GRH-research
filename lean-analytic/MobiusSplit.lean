import Mathlib.NumberTheory.ArithmeticFunction
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-! Exact truncated Möbius identities in the actual natural-number Dirichlet
ring. Ideal convolution, Hecke/sextic characters, prime-ideal asymptotics and
the missing signed mean square are not claimed formalized by this file. -/
set_option autoImplicit false
namespace GRHResearch.MobiusSplit
noncomputable section
open ArithmeticFunction
open scoped ArithmeticFunction

theorem inverse_split_identity {R : Type*} [CommRing R]
    (m z a : R) (hm : m*z=1) :
    2*a-a*a*z+(m-a)*(m-a)*z=m := by
  calc
    _ = m*(m*z)+2*a*(1-m*z) := by ring
    _ = m := by rw [hm]; ring

def truncated (U : ℕ) : ArithmeticFunction ℤ where
  toFun n := if n ≤ U then μ n else 0
  map_zero' := by simp

theorem truncated_apply (U n : ℕ) :
    truncated U n = if n ≤ U then μ n else 0 := rfl

theorem tail_apply (U n : ℕ) :
    (μ-truncated U) n = if U < n then μ n else 0 := by
  change μ n-(if n ≤ U then μ n else 0)=if U<n then μ n else 0
  by_cases h : n ≤ U
  · simp [h,not_lt.mpr h]
  · simp [h,Nat.lt_of_not_ge h]

theorem moebius_split (U : ℕ) :
    2*truncated U-truncated U*truncated U*(ζ : ArithmeticFunction ℤ)+
      (μ-truncated U)*(μ-truncated U)*(ζ : ArithmeticFunction ℤ)=μ :=
  inverse_split_identity μ (ζ : ArithmeticFunction ℤ) (truncated U)
    ArithmeticFunction.moebius_mul_coe_zeta

theorem unit_cutoff : truncated 1 = 1 := by
  ext n
  by_cases h : n ≤ 1
  · rcases Nat.le_one_iff_eq_zero_or_eq_one.mp h with rfl | rfl <;> simp [truncated]
  · have hn : n ≠ 1 := by intro he; exact h (by simp [he])
    simp [truncated,h,ArithmeticFunction.one_apply_ne hn]

theorem unit_tail_identity :
    (μ-1)*(μ-1)*(ζ : ArithmeticFunction ℤ)=
      μ+(ζ : ArithmeticFunction ℤ)-2 := by
  calc
    _ = μ*(μ*(ζ : ArithmeticFunction ℤ))-2*(μ*(ζ : ArithmeticFunction ℤ))+
      (ζ : ArithmeticFunction ℤ) := by ring
    _ = _ := by rw [ArithmeticFunction.moebius_mul_coe_zeta]; ring

theorem unit_tail_coefficient (n : ℕ) (hn : 1<n) :
    ((μ-1)*(μ-1)*(ζ : ArithmeticFunction ℤ)) n=μ n+1 := by
  rw [unit_tail_identity]
  have h0 : n ≠ 0 := Nat.ne_zero_of_lt hn
  have h1 : n ≠ 1 := Nat.ne_of_gt hn
  change μ n+(ζ : ArithmeticFunction ℤ) n-(if n=1 then 2 else 0)=μ n+1
  simp [ArithmeticFunction.natCoe_apply,ArithmeticFunction.zeta_apply_ne h0,
    h1]

theorem unit_tail_nonnegative (n : ℕ) (hn : 1<n) :
    0 ≤ ((μ-1)*(μ-1)*(ζ : ArithmeticFunction ℤ)) n := by
  rw [unit_tail_coefficient n hn]
  rcases ArithmeticFunction.moebius_eq_or n with h | h | h <;> rw [h] <;> norm_num

#check inverse_split_identity
#check truncated_apply
#check tail_apply
#check moebius_split
#check unit_cutoff
#check unit_tail_identity
#check unit_tail_coefficient
#check unit_tail_nonnegative
#print axioms inverse_split_identity
#print axioms truncated_apply
#print axioms tail_apply
#print axioms moebius_split
#print axioms unit_cutoff
#print axioms unit_tail_identity
#print axioms unit_tail_coefficient
#print axioms unit_tail_nonnegative
end
end GRHResearch.MobiusSplit
