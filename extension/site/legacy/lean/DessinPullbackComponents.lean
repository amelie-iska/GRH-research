import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Algebra.Ring.Subring.Basic
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum

/-! Algebraic components of the actual dessin gluing construction.
No C*-completion, functional calculus, K-theory or categorical equivalence is assumed here.
-/
namespace GRHResearch.DessinPullback
open Matrix
variable {R : Type*} [CommRing R]

def e00 : Matrix (Fin 2) (Fin 2) R := !![1,0;0,0]
def e01 : Matrix (Fin 2) (Fin 2) R := !![0,1;0,0]
def e10 : Matrix (Fin 2) (Fin 2) R := !![0,0;1,0]
def e11 : Matrix (Fin 2) (Fin 2) R := !![0,0;0,1]

theorem matrix_unit_forward : (e01 : Matrix (Fin 2) (Fin 2) R)*e10=e00 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [e01,e10,e00,Matrix.mul_apply,Fin.sum_univ_two]

theorem matrix_unit_reverse : (e10 : Matrix (Fin 2) (Fin 2) R)*e01=e11 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [e01,e10,e11,Matrix.mul_apply,Fin.sum_univ_two]

theorem matrix_unit_orthogonal : (e00 : Matrix (Fin 2) (Fin 2) R)*e11=0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [e00,e11,Matrix.mul_apply,Fin.sum_univ_two]

theorem matrix_unit_square : (e00 : Matrix (Fin 2) (Fin 2) R)*e00=e00 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [e00,Matrix.mul_apply,Fin.sum_univ_two]

theorem matrix_unit_sum : (e00 : Matrix (Fin 2) (Fin 2) R)+e11=1 := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [e00,e11]

/-- Raw diagonal evaluation is not multiplicative, already on actual two-state matrices. -/
theorem diagonal_extraction_not_multiplicative [Nontrivial R] :
    ((e01*e10 : Matrix (Fin 2) (Fin 2) R) 0 0) ≠ e01 (R:=R) 0 0*e10 (R:=R) 0 0 := by
  rw [matrix_unit_forward]
  simp [e00,e01,e10]

/-- The full two-state matrix algebra has no unital map to a nonzero commutative ring. -/
theorem no_commutative_matrix_residue {S : Type*} [CommRing S] [Nontrivial S]
    (f : Matrix (Fin 2) (Fin 2) R →+* S) : False := by
  have heq : f e00=f e11 := by
    rw [← matrix_unit_forward,← matrix_unit_reverse,map_mul,map_mul,mul_comm]
  have hzero : f e00=0 := by
    calc
      f e00=f (e00*e00) := congrArg f matrix_unit_square.symm
      _=f e00*f e00 := f.map_mul _ _
      _=f e00*f e11 := by rw [heq]
      _=f (e00*e11) := (f.map_mul _ _).symm
      _=0 := by rw [matrix_unit_orthogonal,map_zero]
  have hsum := congrArg f (matrix_unit_sum (R:=R))
  rw [map_add,map_one,hzero,← heq,hzero,zero_add] at hsum
  exact zero_ne_one hsum

/-- Restricting the fiber to diagonal matrices makes the same boundary coordinate multiplicative. -/
theorem diagonal_fiber_multiplicative (a b : Fin 2 → R) (i : Fin 2) :
    ((Matrix.diagonal a)*(Matrix.diagonal b)) i i=a i*b i := by
  simp

variable {B C D : Type*} [Ring B] [Ring C] [Ring D]

/-- Actual equal-image subring: the algebraic core of a continuous-function pullback. -/
def pullbackSubring (f : B →+* D) (g : C →+* D) : Subring (B × C) where
  carrier := {p | f p.1=g p.2}
  zero_mem' := by simp
  one_mem' := by simp
  add_mem' := by
    intro a b ha hb
    change f a.1=g a.2 at ha
    change f b.1=g b.2 at hb
    change f (a.1+b.1)=g (a.2+b.2)
    simp only [map_add,ha,hb]
  mul_mem' := by
    intro a b ha hb
    change f a.1=g a.2 at ha
    change f b.1=g b.2 at hb
    change f (a.1*b.1)=g (a.2*b.2)
    simp only [map_mul,ha,hb]
  neg_mem' := by
    intro a ha
    change f a.1=g a.2 at ha
    change f (-a.1)=g (-a.2)
    simp only [map_neg,ha]

/-- A prescribed compatible section gives a genuinely surjective pullback projection. -/
theorem pullback_projection_surjective (f : B →+* D) (g : C →+* D)
    (s : C →+* B) (hs : ∀c,f (s c)=g c) :
    Function.Surjective (fun p : pullbackSubring f g => p.val.2) := by
  intro c
  exact ⟨⟨(s c,c),hs c⟩,rfl⟩

/-- The projection's kernel is exactly the first-component zero-fiber. -/
theorem pullback_zero_fiber (f : B →+* D) (g : C →+* D)
    (p : pullbackSubring f g) (hp : p.val.2=0) : f p.val.1=0 := by
  have h := p.property
  change f p.val.1=g p.val.2 at h
  simpa [hp] using h

#check matrix_unit_forward
#check matrix_unit_reverse
#check matrix_unit_orthogonal
#check matrix_unit_square
#check matrix_unit_sum
#check diagonal_extraction_not_multiplicative
#check no_commutative_matrix_residue
#check diagonal_fiber_multiplicative
#check pullback_projection_surjective
#check pullback_zero_fiber
#print axioms matrix_unit_forward
#print axioms matrix_unit_reverse
#print axioms matrix_unit_orthogonal
#print axioms matrix_unit_square
#print axioms matrix_unit_sum
#print axioms diagonal_extraction_not_multiplicative
#print axioms no_commutative_matrix_residue
#print axioms diagonal_fiber_multiplicative
#print axioms pullback_projection_surjective
#print axioms pullback_zero_fiber
end GRHResearch.DessinPullback
