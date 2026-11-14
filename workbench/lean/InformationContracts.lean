import Mathlib.Tactic
set_option autoImplicit false
open scoped BigOperators
namespace InformationContracts

 theorem deterministic_augmentation_fibers {X H Z : Type*}
   (context : X → H) (certificate : H → Z) (x y : X) :
   (context x, certificate (context x)) = (context y, certificate (context y)) ↔ context x=context y := by
  constructor
  · intro h
    exact congrArg Prod.fst h
  · intro h
    simp only [h]

 theorem likelihood_step_mean {ι : Type*} [Fintype ι]
   (p q : ι → ℝ) (w : ℝ) (hp : ∀ i, p i ≠ 0)
   (hq : ∑ i, q i = 1) : (∑ i, p i*(w*q i/p i))=w := by
  calc (∑ i, p i*(w*q i/p i)) = ∑ i,w*q i := by
          apply Finset.sum_congr rfl
          intro i _
          field_simp
       _ = w := by rw [← Finset.mul_sum,hq,mul_one]

 theorem first_crossing_budget {ι : Type*} [Fintype ι]
   (nullMass alternativeMass : ι → ℝ) (α : ℝ) (ha : 0≤α)
   (hprefix : ∑ i, alternativeMass i ≤ 1)
   (hcross : ∀ i, nullMass i ≤ α*alternativeMass i) :
   (∑ i,nullMass i) ≤ α := by
  calc (∑ i,nullMass i) ≤ ∑ i,α*alternativeMass i := Finset.sum_le_sum (fun i _ => hcross i)
       _ = α*(∑ i,alternativeMass i) := by rw [Finset.mul_sum]
       _ ≤ α*1 := mul_le_mul_of_nonneg_left hprefix ha
       _ = α := mul_one α

end InformationContracts
#check InformationContracts.deterministic_augmentation_fibers
#check InformationContracts.likelihood_step_mean
#check InformationContracts.first_crossing_budget
#print axioms InformationContracts.deterministic_augmentation_fibers
#print axioms InformationContracts.likelihood_step_mean
#print axioms InformationContracts.first_crossing_budget
