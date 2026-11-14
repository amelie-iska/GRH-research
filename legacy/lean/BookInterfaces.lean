import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Ring

/-! Finite algebraic interfaces for the book. These are actual matrix and
Kraus-map identities. No AR classification, continuum QFT reconstruction,
arithmetic spectral comparison or RH/GRH theorem is asserted. -/
namespace GRHResearch.BookInterfaces
open Matrix
open scoped ComplexOrder

section Polynomial
variable {R : Type*} [CommRing R]

/-- The literal minor of columns i,j in an actual two-by-four matrix. -/
def minor24 (A : Matrix (Fin 2) (Fin 4) R) (i j : Fin 4) : R :=
  A 0 i*A 1 j-A 0 j*A 1 i

theorem plucker24 (A : Matrix (Fin 2) (Fin 4) R) :
    minor24 A 0 1*minor24 A 2 3-minor24 A 0 2*minor24 A 1 3+
      minor24 A 0 3*minor24 A 1 2=0 := by
  dsimp [minor24]
  ring

/-- A triangular nodal representation; b records extension data. -/
def nodeX (u b : R) : Matrix (Fin 2) (Fin 2) R := !![u,b;0,0]
def nodeY (u b : R) : Matrix (Fin 2) (Fin 2) R := !![0,-b;0,u]

theorem node_relations (u b : R) :
    nodeX u b+nodeY u b=u • (1 : Matrix (Fin 2) (Fin 2) R) ∧
    nodeX u b*nodeY u b=0 ∧ nodeY u b*nodeX u b=0 := by
  constructor
  · ext i j
    fin_cases i <;> fin_cases j <;> simp [nodeX,nodeY]
  constructor
  · ext i j
    fin_cases i <;> fin_cases j <;>
      simp [nodeX,nodeY,Matrix.mul_apply,Fin.sum_univ_two]
    ring
  · ext i j
    fin_cases i <;> fin_cases j <;>
      simp [nodeX,nodeY,Matrix.mul_apply,Fin.sum_univ_two]

theorem node_triangular_determinant (u b s t : R) :
    (1-s • nodeX u b-t • nodeY u b).det=(1-s*u)*(1-t*u) := by
  simp [nodeX,nodeY,Matrix.det_fin_two]

/-- A valuation-aware two-cycle and its sign clock. -/
def twistedShift (u : R) : Matrix (Fin 2) (Fin 2) R := !![0,u;1,0]
def signClock : Matrix (Fin 2) (Fin 2) R := !![1,0;0,-1]

theorem twisted_shift_square (u : R) :
    twistedShift u*twistedShift u=u • (1 : Matrix (Fin 2) (Fin 2) R) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [twistedShift,Matrix.mul_apply,Fin.sum_univ_two]

theorem clock_shift_anticommute (u : R) :
    signClock*twistedShift u=-(twistedShift u*signClock) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [signClock,twistedShift,Matrix.mul_apply,Fin.sum_univ_two]

/-- Basis order 00,01,10,11: shift the first bit, clock the second. -/
def firstBitShift : Matrix (Fin 4) (Fin 4) R :=
  !![0,0,1,0;0,0,0,1;1,0,0,0;0,1,0,0]
def secondBitClock : Matrix (Fin 4) (Fin 4) R :=
  !![1,0,0,0;0,-1,0,0;0,0,1,0;0,0,0,-1]

theorem distinct_site_commutation :
    (firstBitShift : Matrix (Fin 4) (Fin 4) R)*secondBitClock=
      secondBitClock*firstBitShift := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [firstBitShift,secondBitClock,Matrix.mul_apply,Fin.sum_univ_succ]
end Polynomial

section Pooling
variable {n m ι : Type*} [Fintype n] [Fintype m] [Fintype ι]

/-- A finite rectangular Kraus sum on actual complex matrices. -/
noncomputable def krausPool (K : ι → Matrix m n ℂ) (A : Matrix n n ℂ) : Matrix m m ℂ :=
  ∑ i, K i*A*(K i)ᴴ

theorem kraus_pool_trace [DecidableEq n] (K : ι → Matrix m n ℂ)
    (hK : ∑ i, (K i)ᴴ*K i=1) (A : Matrix n n ℂ) :
    (krausPool K A).trace=A.trace := by
  calc
    _=∑ i, (K i*A*(K i)ᴴ).trace := by rw [krausPool,Matrix.trace_sum]
    _=∑ i, ((K i)ᴴ*K i*A).trace := by
      apply Finset.sum_congr rfl
      intro i _
      exact Matrix.trace_mul_cycle _ _ _
    _=((∑ i, (K i)ᴴ*K i)*A).trace := by
      rw [Finset.sum_mul,Matrix.trace_sum]
    _=A.trace := by rw [hK,Matrix.one_mul]

theorem kraus_pool_positive (K : ι → Matrix m n ℂ) (A : Matrix n n ℂ)
    (hA : A.PosSemidef) : (krausPool K A).PosSemidef := by
  classical
  have hs (s : Finset ι) : (∑ i ∈ s, K i*A*(K i)ᴴ).PosSemidef := by
    induction s using Finset.induction_on with
    | empty => simpa using (Matrix.PosSemidef.zero : (0 : Matrix m m ℂ).PosSemidef)
    | @insert i s hi ih =>
      rw [Finset.sum_insert hi]
      exact (hA.mul_mul_conjTranspose_same (K i)).add ih
  exact hs Finset.univ
end Pooling

#check plucker24
#check node_relations
#check node_triangular_determinant
#check twisted_shift_square
#check clock_shift_anticommute
#check distinct_site_commutation
#check kraus_pool_trace
#check kraus_pool_positive
#print axioms plucker24
#print axioms node_relations
#print axioms node_triangular_determinant
#print axioms twisted_shift_square
#print axioms clock_shift_anticommute
#print axioms distinct_site_commutation
#print axioms kraus_pool_trace
#print axioms kraus_pool_positive
end GRHResearch.BookInterfaces
