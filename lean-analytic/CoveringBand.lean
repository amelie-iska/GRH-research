import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Data.Matrix.Mul
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum

/-! A genuine finite quotient of the infinite theta dessin algebra.
The six X-edges and three Y-edges form a cyclic string. Both actions are
nilpotent and annihilate one another. No characteristic-zero Euler operator
can assign degree one to both. This verifies the explicit obstruction; it
does not formalize a covering/AR classification or the full derived functor. -/
namespace GRHResearch.CoveringBand
open Matrix

variable {R : Type*} [CommRing R]

def bandX : Matrix (Fin 9) (Fin 9) R := fun i j =>
  if (i.val, j.val) ∈ [(1,0),(3,2),(4,3),(6,5),(7,6),(0,8)] then 1 else 0

def bandY : Matrix (Fin 9) (Fin 9) R := fun i j =>
  if (i.val, j.val) ∈ [(1,2),(4,5),(7,8)] then 1 else 0

theorem mixed_products :
    (bandX : Matrix (Fin 9) (Fin 9) R) * bandY = 0 ∧
      (bandY : Matrix (Fin 9) (Fin 9) R) * bandX = 0 := by
  constructor <;> ext i j <;> fin_cases i <;> fin_cases j <;>
    simp [bandX, bandY, Matrix.mul_apply, Fin.sum_univ_succ]

set_option maxHeartbeats 4000000 in
theorem cubic_nilpotence :
    (bandX : Matrix (Fin 9) (Fin 9) R) ^ 3 = 0 ∧
      (bandY : Matrix (Fin 9) (Fin 9) R) ^ 3 = 0 := by
  constructor
  · ext i j
    fin_cases i <;> fin_cases j <;>
      simp [pow_succ, bandX, Matrix.mul_apply, Fin.sum_univ_succ]
  · ext i j
    fin_cases i <;> fin_cases j <;>
      simp [pow_succ, bandY, Matrix.mul_apply, Fin.sum_univ_succ]

theorem no_euler_operator [CharZero R] (D : Matrix (Fin 9) (Fin 9) R) :
    ¬ (D * bandX - bandX * D = bandX ∧ D * bandY - bandY * D = bandY) := by
  rintro ⟨hx, hy⟩
  have a0 := congrArg (fun M : Matrix (Fin 9) (Fin 9) R => M 1 0) hx
  have a1 := congrArg (fun M : Matrix (Fin 9) (Fin 9) R => M 3 2) hx
  have a2 := congrArg (fun M : Matrix (Fin 9) (Fin 9) R => M 4 3) hx
  have a3 := congrArg (fun M : Matrix (Fin 9) (Fin 9) R => M 6 5) hx
  have a4 := congrArg (fun M : Matrix (Fin 9) (Fin 9) R => M 7 6) hx
  have a5 := congrArg (fun M : Matrix (Fin 9) (Fin 9) R => M 0 8) hx
  have b0 := congrArg (fun M : Matrix (Fin 9) (Fin 9) R => M 1 2) hy
  have b1 := congrArg (fun M : Matrix (Fin 9) (Fin 9) R => M 4 5) hy
  have b2 := congrArg (fun M : Matrix (Fin 9) (Fin 9) R => M 7 8) hy
  simp [bandX, bandY, Matrix.mul_apply, Fin.sum_univ_succ] at a0 a1 a2 a3 a4 a5 b0 b1 b2
  have bad : (3 : R) = 0 := by
    linear_combination -(a0 + a1 + a2 + a3 + a4 + a5 - b0 - b1 - b2)
  norm_num at bad

#check mixed_products
#check cubic_nilpotence
#check no_euler_operator
#print axioms mixed_products
#print axioms cubic_nilpotence
#print axioms no_euler_operator
end GRHResearch.CoveringBand
