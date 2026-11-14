import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.ConjTranspose
set_option autoImplicit false
open scoped BigOperators
namespace IntegratedOperatorContracts

theorem power_intertwines {m n : Type*} [Fintype m] [Fintype n]
 [DecidableEq m] [DecidableEq n]
 (A : Matrix m m ℝ) (B : Matrix n n ℝ) (U : Matrix m n ℝ)
 (h : A * U = U * B) (k : ℕ) : A ^ k * U = U * B ^ k := by
 induction k with
 | zero => simp
 | succ k ih =>
  calc A ^ (k+1) * U = A * (A^k * U) := by rw [pow_succ']; simp only [Matrix.mul_assoc]
       _ = A * (U * B^k) := by rw [ih]
       _ = (A*U) * B^k := by rw [Matrix.mul_assoc]
       _ = (U*B) * B^k := by rw [h]
       _ = U * B ^ (k+1) := by rw [pow_succ']; simp only [Matrix.mul_assoc]

theorem scalar_model_error (actual surrogate delta alpha : ℝ)
 (herror : |actual-surrogate| ≤ delta) (hcal : surrogate ≤ alpha) :
 actual ≤ alpha+delta := by
 have h := (abs_le.mp herror).2
 linarith

theorem long_division_step (p r bit : ℕ) (hp : 0<p) (hr : r<p) (hb : bit≤1) :
 (if 2*r+bit<p then 2*r+bit else 2*r+bit-p)<p := by
 split_ifs <;> omega

theorem xor_output_involution (value output : Bool) :
 (output ^^ value) ^^ value=output := by
 cases value <;> cases output <;> decide
end IntegratedOperatorContracts
#print axioms IntegratedOperatorContracts.power_intertwines
#print axioms IntegratedOperatorContracts.scalar_model_error
#print axioms IntegratedOperatorContracts.long_division_step
#print axioms IntegratedOperatorContracts.xor_output_involution
#check IntegratedOperatorContracts.power_intertwines
#check IntegratedOperatorContracts.scalar_model_error
#check IntegratedOperatorContracts.long_division_step
#check IntegratedOperatorContracts.xor_output_involution
