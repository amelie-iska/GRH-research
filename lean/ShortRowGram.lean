import Mathlib.NumberTheory.JacobiSum.Basic
import Mathlib.Algebra.QuadraticAlgebra
import Mathlib.Data.ZMod.Basic
import Mathlib.Analysis.Complex.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

namespace GRHResearch.ShortRowGram
open Finset
variable {F : Type*} [Field F] [Fintype F]
attribute [local instance] Classical.propDecidable

/-- Canceling a common finite-field character retains its zero mask. -/
theorem character_pair_mask (χ : MulChar F ℂ) (x : F) :
    χ x*star (χ x)=if x=0 then 0 else 1 := by
  by_cases hx : x=0
  · simp [hx,MulChar.map_zero]
  · rw [if_neg hx,MulChar.star_apply']
    change (χ*χ⁻¹) x=1
    rw [mul_inv_cancel,MulChar.one_apply (isUnit_iff_ne_zero.mpr hx)]

/-- Exact common-prime cancellation, leaving independent residual factors. -/
theorem common_character_mask (χ : MulChar F ℂ) (x : F) (a b : ℂ) :
    (χ x*a)*star (χ x*b)=(if x=0 then 0 else 1)*a*star b := by
  rw [star_mul]
  calc
    _=(χ x*star (χ x))*a*star b := by ring
    _=_ := by rw [character_pair_mask]

/-- Matched coefficients count actual nonzero residues, including all collisions. -/
theorem matched_character_sum {ι : Type*} (s : Finset ι) (χ : MulChar F ℂ) (r : ι → F) :
    (∑ b ∈ s, star (χ (r b))*χ (r b))=((s.filter fun b => r b≠0).card : ℂ) := by
  classical
  calc
    _=∑ b ∈ s, if r b=0 then (0:ℂ) else 1 := by
      apply Finset.sum_congr rfl
      intro b _
      rw [mul_comm,character_pair_mask]
    _=_ := by
      rw [Finset.card_filter]
      push_cast
      apply Finset.sum_congr rfl
      intro b _
      by_cases h : r b=0 <;> simp [h]

/-- A selected arithmetic row gives a genuine lower bound for the whole energy. -/
theorem matched_row_energy_lower {ρ ι : Type*}
    (rows : Finset ρ) (columns : Finset ι) (row : ρ) (hr : row∈rows)
    (χ : MulChar F ℂ) (r : ι → F) (kernel : ρ → ι → ℂ)
    (hk : ∀ b∈columns, kernel row b=χ (r b)) :
    ((columns.filter fun b => r b≠0).card : ℝ)^2 ≤
      ∑ k ∈ rows, ‖∑ b ∈ columns, star (χ (r b))*kernel k b‖^2 := by
  classical
  have he : (∑ b ∈ columns, star (χ (r b))*kernel row b)=
      ((columns.filter fun b => r b≠0).card : ℂ) := by
    rw [← matched_character_sum columns χ r]
    exact Finset.sum_congr rfl fun b hb => by rw [hk b hb]
  have hle := Finset.single_le_sum (fun k (_ : k∈rows) =>
    sq_nonneg ‖∑ b ∈ columns, star (χ (r b))*kernel k b‖) hr
  simpa only [he,Complex.norm_natCast] using hle

/-- Complete residue correlations; this is not orthogonality on a short ball. -/
theorem complete_character_gram (χ ψ : MulChar F ℂ) :
    (∑ x : F, χ x*star (ψ x))=
      if χ=ψ then (Fintype.card F : ℂ)-1 else 0 := by
  have hsum : (∑ x : F, χ x*star (ψ x))=∑ x : F, (χ*ψ⁻¹) x := by
    apply Finset.sum_congr rfl
    intro x _
    rw [MulChar.star_apply']
    rfl
  rw [hsum]
  by_cases h : χ=ψ
  · subst ψ
    rw [if_pos rfl,mul_inv_cancel,MulChar.sum_one_eq_card_units]
    have hc := Fintype.card_eq_card_units_add_one (α:=F)
    rw [hc]
    push_cast
    ring
  · rw [if_neg h,MulChar.sum_eq_zero_of_ne_one]
    intro he
    apply h
    have hh := congrArg (fun z : MulChar F ℂ => z*ψ) he
    simpa only [mul_assoc,inv_mul_cancel,mul_one,one_mul] using hh

/-- Finite original-family Gram expansion, with every zero kept in the kernel. -/
theorem finite_gram_expansion {ρ ι : Type*} (rows : Finset ρ) (columns : Finset ι)
    (c : ι → ℂ) (kernel : ρ → ι → ℂ) :
    (∑ k ∈ rows, ‖∑ n ∈ columns, c n*kernel k n‖^2)=
      (∑ n ∈ columns, ∑ m ∈ columns, c n*star (c m)*
        ∑ k ∈ rows, kernel k n*star (kernel k m)).re := by
  have hc : (∑ k ∈ rows, (∑ n ∈ columns, c n*kernel k n)*
      star (∑ m ∈ columns, c m*kernel k m))=
      ∑ n ∈ columns, ∑ m ∈ columns, c n*star (c m)*
        ∑ k ∈ rows, kernel k n*star (kernel k m) := by
    simp_rw [star_sum,star_mul,Finset.sum_mul,Finset.mul_sum]
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro n _
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro m _
    apply Finset.sum_congr rfl
    intro k _
    ring
  have hre := congrArg Complex.re hc
  have hn (z : ℂ) : (z*star z).re = ‖z‖^2 := by
    rw [Complex.star_def,Complex.mul_conj]
    simp only [Complex.ofReal_re,Complex.normSq_eq_norm_sq]
  simpa only [Complex.re_sum, hn] using hre

/-- The actual Eisenstein integer algebra, not a formal free parameter. -/
abbrev Eisenstein := QuadraticAlgebra ℤ (-1) (-1)
def normE (x : Eisenstein) : ℤ := x.re^2-x.re*x.im+x.im^2

theorem eisenstein_norm_mul (x y : Eisenstein) : normE (x*y)=normE x*normE y := by
  simp [normE,QuadraticAlgebra.re_mul,QuadraticAlgebra.im_mul]
  ring

theorem eisenstein_norm_square_identity (x : Eisenstein) :
    (2*x.re-x.im)^2+3*x.im^2=4*normE x := by
  simp [normE]
  ring

/-- Evaluation omega -> 2 in the actual field of seven elements. -/
def residueSeven : Eisenstein →+* ZMod 7 where
  toFun x := (x.re : ZMod 7)+2*(x.im : ZMod 7)
  map_one' := by change (1:ZMod 7)+2*0=1; ring
  map_zero' := by change (0:ZMod 7)+2*0=0; ring
  map_add' x y := by simp; ring
  map_mul' x y := by
    simp [QuadraticAlgebra.re_mul,QuadraticAlgebra.im_mul]
    have h : (-3 : ZMod 7)=4 := by decide
    linear_combination (x.im : ZMod 7)*(y.im : ZMod 7)*h

theorem norm_seven_prime_data : normE (⟨1,3⟩ : Eisenstein)=7 ∧
    residueSeven (⟨1,3⟩ : Eisenstein)=0 := by
  norm_num [normE,residueSeven]
  decide

#check character_pair_mask
#check common_character_mask
#check matched_character_sum
#check matched_row_energy_lower
#check complete_character_gram
#check finite_gram_expansion
#check eisenstein_norm_mul
#check eisenstein_norm_square_identity
#check norm_seven_prime_data
#print axioms character_pair_mask
#print axioms common_character_mask
#print axioms matched_character_sum
#print axioms matched_row_energy_lower
#print axioms complete_character_gram
#print axioms finite_gram_expansion
#print axioms eisenstein_norm_mul
#print axioms eisenstein_norm_square_identity
#print axioms norm_seven_prime_data
end GRHResearch.ShortRowGram
