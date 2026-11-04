import Mathlib.Analysis.SpecialFunctions.Pow.Complex
import Mathlib.Algebra.BigOperators.Field

/-! Finite Euler restoration for full zero-extension. Primitive coefficients
at a deleted prime can change from zero to nonzero when the character is
squared. Infinite Hecke functions and Mellin contours are separate objects. -/
set_option autoImplicit false
namespace GRHResearch.HeckeTypeI
noncomputable section
open Finset

def ratio (a b z : ℂ) : ℂ := (1-b*z^2)/(1-a*z)
def restore (a b z : ℂ) : ℂ := (1-a*z)/(1-b*z^2)

theorem squarefree_local (z : ℂ) : (1+z)*(1-z)=1-z^2 := by ring

theorem unramified_ratio (a z : ℂ) (h : 1-a*z ≠ 0) :
    ratio a (a^2) z = 1+a*z := by
  unfold ratio
  field_simp
  ring

theorem deleted_local (a b z : ℂ)
    (ha : 1-a*z ≠ 0) (hb : 1-b*z^2 ≠ 0) :
    ratio a b z * restore a b z = 1 := by
  unfold ratio restore
  rw [div_mul_div_comm, mul_comm (1-b*z^2) (1-a*z)]
  exact div_self (mul_ne_zero ha hb)

theorem quadratic_collapse (z : ℂ) :
    restore 0 1 z = (1-z^2)⁻¹ := by simp [restore]

theorem sixth_power_mask (z : ℂ) (hm : 1-z ≠ 0) (hp : 1+z ≠ 0) :
    restore 1 1 z = (1+z)⁻¹ := by
  have h2 : 1-z^2 ≠ 0 := by
    rw [← squarefree_local]
    exact mul_ne_zero hp hm
  unfold restore
  field_simp
  ring

theorem zero_square_is_not_unramified : (0 : ℂ)^2 ≠ 1 := by simp

/-- Arrays agree by squaring only outside the entire deleted set; at a
conductor-drop prime a=0,b≠0 is allowed. -/
theorem finite_restoration {I : Type*} [DecidableEq I]
    (P T : Finset I) (a b z : I → ℂ)
    (ha : ∀ p ∈ P, 1-a p*z p ≠ 0)
    (hb : ∀ p ∈ P, 1-b p*(z p)^2 ≠ 0)
    (hsquare : ∀ p ∈ P, p ∉ T → b p=(a p)^2) :
    (∏ p ∈ P, ratio (a p) (b p) (z p)) *
        (∏ p ∈ P, if p ∈ T then restore (a p) (b p) (z p) else 1) =
      ∏ p ∈ P.filter (fun p => p ∉ T), (1+a p*z p) := by
  rw [← prod_mul_distrib, prod_filter]
  apply prod_congr rfl
  intro p hp
  by_cases ht : p ∈ T
  · simp only [ht,if_pos,not_true_eq_false,if_false]
    exact deleted_local _ _ _ (ha p hp) (hb p hp)
  · simp only [ht,if_false,not_false_eq_true,if_true,mul_one]
    rw [hsquare p hp ht]
    exact unramified_ratio _ _ (ha p hp)

end
end GRHResearch.HeckeTypeI

#check GRHResearch.HeckeTypeI.squarefree_local
#print axioms GRHResearch.HeckeTypeI.squarefree_local
#check GRHResearch.HeckeTypeI.unramified_ratio
#print axioms GRHResearch.HeckeTypeI.unramified_ratio
#check GRHResearch.HeckeTypeI.deleted_local
#print axioms GRHResearch.HeckeTypeI.deleted_local
#check GRHResearch.HeckeTypeI.quadratic_collapse
#print axioms GRHResearch.HeckeTypeI.quadratic_collapse
#check GRHResearch.HeckeTypeI.sixth_power_mask
#print axioms GRHResearch.HeckeTypeI.sixth_power_mask
#check GRHResearch.HeckeTypeI.zero_square_is_not_unramified
#print axioms GRHResearch.HeckeTypeI.zero_square_is_not_unramified
#check GRHResearch.HeckeTypeI.finite_restoration
#print axioms GRHResearch.HeckeTypeI.finite_restoration
