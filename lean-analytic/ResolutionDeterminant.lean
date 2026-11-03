import Mathlib.LinearAlgebra.Matrix.SchurComplement
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Ring

namespace GRHResearch.Resolutions
open Matrix

/-- Cleared arrow-state determinant identity over any commutative ring.
`W` inverts `1-U`; composable pairs split as `T*S*D=U+V`.
There is no spectral or arithmetic hypothesis. -/
theorem arrow_state_determinant {R : Type*} [CommRing R]
    {n m : Type*} [Fintype n] [DecidableEq n] [Fintype m] [DecidableEq m]
    (S : Matrix n m R) (T : Matrix m n R) (D U V W : Matrix m m R)
    (hinv : (1 - U) * W = 1) (hsplit : T * S * D = U + V) :
    (1 + S * D * W * T).det * (1 - U).det = (1 + V).det := by
  have hmatrix : (1 - U) * (1 + W * T * S * D) = 1 + V := by
    calc
      (1 - U) * (1 + W * T * S * D) =
          (1 - U) + ((1 - U) * W) * T * S * D := by
            simp only [Matrix.mul_add, Matrix.mul_one, Matrix.mul_assoc]
      _ = (1 - U) + (U + V) := by rw [hinv, Matrix.one_mul, hsplit]
      _ = 1 + V := by abel
  have hsyl : (1 + S * D * W * T).det = (1 + W * T * S * D).det := by
    simpa only [Matrix.mul_assoc] using Matrix.det_one_add_mul_comm (S * D) (W * T)
  rw [hsyl, mul_comm, ← Matrix.det_mul, hmatrix]

/-- Conjugate chain terms in an acyclic pair have equal characteristic determinants. -/
theorem acyclic_pair_determinant {R : Type*} [CommRing R]
    {n : Type*} [Fintype n] [DecidableEq n]
    (A B E : Matrix n n R) (hAB : A * B = 1) (t : R) :
    (1 - t • (A * E * B)).det = (1 - t • E).det := by
  have h : 1 - t • (A * E * B) = A * (1 - t • E) * B := by
    simp only [Matrix.mul_sub, Matrix.mul_one, Matrix.sub_mul, Matrix.mul_smul,
      Matrix.smul_mul, hAB]
  rw [h, Matrix.det_mul, Matrix.det_mul]
  have hd : A.det * B.det = 1 := by rw [← Matrix.det_mul, hAB, Matrix.det_one]
  calc
    A.det * (1 - t • E).det * B.det = (A.det * B.det) * (1 - t • E).det := by ring
    _ = (1 - t • E).det := by rw [hd, one_mul]

/-- Alternating duality alone does not imply weight-one purity. -/
theorem alternating_duality_without_purity :
    let F : Matrix (Fin 2) (Fin 2) ℚ := !![2, 0; 0, 1]
    let J : Matrix (Fin 2) (Fin 2) ℚ := !![0, 1; -1, 0]
    F.transpose * J * F = 2 • J ∧ (2 : ℚ)^2 ≠ 2 := by
  dsimp
  constructor
  · ext i j
    fin_cases i <;> fin_cases j <;>
      norm_num [Matrix.mul_apply, Fin.sum_univ_two]
  · norm_num

#check arrow_state_determinant
#check acyclic_pair_determinant
#check alternating_duality_without_purity
#print axioms arrow_state_determinant
#print axioms acyclic_pair_determinant
#print axioms alternating_duality_without_purity
end GRHResearch.Resolutions
