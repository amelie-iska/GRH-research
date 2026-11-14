import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.ConjTranspose

/-! Reversible cleanup, finite-cover averaging, Kraus composition and conservative
finite ranks. Statistical null invariance and physical interpretation are separate
premises in the accompanying manuscript; none is introduced as an axiom here. -/
set_option autoImplicit false
open scoped BigOperators
namespace Program3Contracts

def xorOracle {X : Type*} (f : X → Bool) (input : X × Bool) : X × Bool :=
 (input.1, input.2 ^^ f input.1)

theorem xor_oracle_involution {X : Type*} (f : X → Bool) (input : X × Bool) :
 xorOracle f (xorOracle f input)=input := by
 rcases input with ⟨x,b⟩
 cases b <;> cases h : f x <;> simp [xorOracle,h]

theorem compute_copy_uncompute (x a y : Bool) :
 ((x ^^ a) ^^ a, y ^^ a)=(x,y ^^ a) := by
 cases x <;> cases a <;> cases y <;> decide

theorem cyclic_voltage_closure {A : Type*} [AddGroup A]
 (s u v : A) (h : u+v=0) : (s+u)+v=s := by
 rw [add_assoc,h,add_zero]

theorem fiber_average_constant {ι : Type*} [Fintype ι] [Nonempty ι]
 (x : ℝ) : (∑ _i : ι,x)/(Fintype.card ι : ℝ)=x := by
 have h : (Fintype.card ι : ℝ) ≠ 0 := by exact_mod_cast Fintype.card_ne_zero
 simp only [Finset.sum_const,Finset.card_univ,nsmul_eq_mul]
 field_simp

theorem replicated_normalization (d numerator denominator : ℝ)
 (hd : d ≠ 0) (hz : denominator ≠ 0) :
 (d*numerator)/(d*denominator)=numerator/denominator := by field_simp

theorem normalized_maxplus_error (a b a' b' δa δb : ℝ)
 (ha : |a'-a|≤δa) (hb : |b'-b|≤δb) :
 |(a'-b')-(a-b)|≤δa+δb := by
 rw [abs_le] at ha hb ⊢
 constructor <;> linarith

theorem ising_projection_residual (full projected exact : ℝ) :
 |full-exact|≤|full-projected|+|projected-exact| := by
 calc |full-exact|=|(full-projected)+(projected-exact)| := by congr 1; ring
      _≤|full-projected|+|projected-exact| := abs_add_le _ _

theorem kraus_composition_complete
 {I J A B C : Type*} [Fintype I] [Fintype J] [Fintype A] [Fintype B] [Fintype C]
 [DecidableEq A] [DecidableEq B]
 (K : I → Matrix B A ℂ) (L : J → Matrix C B ℂ)
 (hK : ∑ i, (K i).conjTranspose * K i = 1)
 (hL : ∑ j, (L j).conjTranspose * L j = 1) :
 (∑ i, ∑ j, (L j*K i).conjTranspose * (L j*K i))=1 := by
 calc (∑ i, ∑ j, (L j*K i).conjTranspose * (L j*K i))
      = ∑ i, (K i).conjTranspose * ((∑ j, (L j).conjTranspose * L j) * K i) := by
        apply Finset.sum_congr rfl
        intro i _
        simp only [Matrix.conjTranspose_mul,Matrix.mul_assoc,Matrix.sum_mul,Matrix.mul_sum]
      _ = ∑ i, (K i).conjTranspose * K i := by rw [hL]; simp
      _ = 1 := hK

noncomputable def upperRank {n : ℕ} (scores : Fin n → ℝ) (i : Fin n) : ℕ :=
 (Finset.univ.filter (fun j => scores i≤scores j)).card

theorem conservative_rank_count {n : ℕ} (scores : Fin n → ℝ) (k : ℕ) :
 (Finset.univ.filter (fun i => upperRank scores i≤k)).card≤k := by
 classical
 let bad := Finset.univ.filter (fun i => upperRank scores i≤k)
 change bad.card≤k
 by_cases he : bad.Nonempty
 · let values := bad.image scores
   have hv : values.Nonempty := Finset.Nonempty.image he scores
   obtain ⟨i,hi,hmin⟩ := Finset.mem_image.mp (Finset.min'_mem values hv)
   have subset : bad ⊆ Finset.univ.filter (fun j => scores i≤scores j) := by
    intro j hj
    refine Finset.mem_filter.mpr ⟨Finset.mem_univ j,?_⟩
    have h := Finset.min'_le values (scores j) (Finset.mem_image.mpr ⟨j,hj,rfl⟩)
    rw [←hmin] at h
    exact h
   have hk : upperRank scores i≤k := (Finset.mem_filter.mp hi).2
   exact (Finset.card_le_card subset).trans hk
 · have hzero : bad=∅ := Finset.not_nonempty_iff_eq_empty.mp he
   simp [hzero]

theorem rank_probability_bound (m n k : ℕ) (hn : 0<n) (hm : m≤k) :
 (m:ℝ)/n≤(k:ℝ)/n := by
 apply div_le_div_of_nonneg_right
 · exact_mod_cast hm
 · positivity

theorem false_positive_budget {ι : Type*} [Fintype ι]
 (p : ι → ℝ) (α : ℝ) (h : ∀ i, p i≤α/(Fintype.card ι : ℝ))
 [Nonempty ι] : (∑ i,p i)≤α := by
 have hn : (Fintype.card ι : ℝ) ≠ 0 := by exact_mod_cast Fintype.card_ne_zero
 calc (∑ i,p i)≤∑ _i : ι,α/(Fintype.card ι : ℝ) := Finset.sum_le_sum (fun i _ => h i)
      _=α := by simp only [Finset.sum_const,Finset.card_univ,nsmul_eq_mul]; field_simp

end Program3Contracts
#check Program3Contracts.xor_oracle_involution
#check Program3Contracts.compute_copy_uncompute
#check Program3Contracts.cyclic_voltage_closure
#check Program3Contracts.fiber_average_constant
#check Program3Contracts.replicated_normalization
#check Program3Contracts.normalized_maxplus_error
#check Program3Contracts.ising_projection_residual
#check Program3Contracts.kraus_composition_complete
#check Program3Contracts.conservative_rank_count
#check Program3Contracts.rank_probability_bound
#check Program3Contracts.false_positive_budget
#print axioms Program3Contracts.xor_oracle_involution
#print axioms Program3Contracts.compute_copy_uncompute
#print axioms Program3Contracts.cyclic_voltage_closure
#print axioms Program3Contracts.fiber_average_constant
#print axioms Program3Contracts.replicated_normalization
#print axioms Program3Contracts.normalized_maxplus_error
#print axioms Program3Contracts.ising_projection_residual
#print axioms Program3Contracts.kraus_composition_complete
#print axioms Program3Contracts.conservative_rank_count
#print axioms Program3Contracts.rank_probability_bound
#print axioms Program3Contracts.false_positive_budget
