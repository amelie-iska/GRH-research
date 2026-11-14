import Mathlib.LinearAlgebra.Matrix.SchurComplement
import Mathlib.Data.Complex.Basic
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

namespace GRHResearch.Hodge
open Matrix
open scoped ComplexOrder

/-- Factoring a nonzero scalar shift from an actual square matrix. -/
theorem shifted_matrix_factor {ι : Type*} [Fintype ι] [DecidableEq ι]
    (M : Matrix ι ι ℂ) (μ : ℂ) (hμ : μ ≠ 0) :
    μ • (1 : Matrix ι ι ℂ) + M = μ • (1 + μ⁻¹ • M) := by
  rw [smul_add, smul_smul, mul_inv_cancel₀ hμ, one_smul]

/-- Squaring the actual odd self-adjoint block gives the two parity Laplacians. -/
theorem odd_dirac_square {m n : Type*}
    [Fintype m] [DecidableEq m] [Fintype n] [DecidableEq n]
    (B : Matrix n m ℂ) :
    Matrix.fromBlocks 0 B.conjTranspose B 0 * Matrix.fromBlocks 0 B.conjTranspose B 0 =
      Matrix.fromBlocks (B.conjTranspose * B) 0 0 (B * B.conjTranspose) := by
  rw [Matrix.fromBlocks_multiply]
  simp

/-- Both partners are actual positive semidefinite Hermitian matrices. -/
theorem gram_partners_positive {m n : Type*}
    [Fintype m] [DecidableEq m] [Fintype n] [DecidableEq n]
    (B : Matrix n m ℂ) :
    (B.conjTranspose * B).PosSemidef ∧ (B * B.conjTranspose).PosSemidef := by
  exact ⟨Matrix.posSemidef_conjTranspose_mul_self B,
    Matrix.posSemidef_self_mul_conjTranspose B⟩

/-- The two actual Gram Laplacians have the same normalized determinant. -/
theorem normalized_gram_determinants {m n : Type*}
    [Fintype m] [DecidableEq m] [Fintype n] [DecidableEq n]
    (B : Matrix n m ℂ) (z : ℂ) :
    (1 + z • (B.conjTranspose * B)).det =
      (1 + z • (B * B.conjTranspose)).det := by
  simpa only [Matrix.smul_mul, Matrix.mul_smul] using
    Matrix.det_one_add_mul_comm (z • B.conjTranspose) B

/-- Away from zero mass, the shifted superdeterminant has only an index power.
This is a cleared equality; no determinant nonvanishing is assumed. -/
theorem shifted_gram_determinants {m n : Type*}
    [Fintype m] [DecidableEq m] [Fintype n] [DecidableEq n]
    (B : Matrix n m ℂ) (μ : ℂ) (hμ : μ ≠ 0) :
    (μ • (1 : Matrix m m ℂ) + B.conjTranspose * B).det * μ ^ Fintype.card n =
      (μ • (1 : Matrix n n ℂ) + B * B.conjTranspose).det * μ ^ Fintype.card m := by
  rw [shifted_matrix_factor _ μ hμ, shifted_matrix_factor _ μ hμ,
    Matrix.det_smul, Matrix.det_smul, normalized_gram_determinants]
  ring

/-- The normalized alternating determinant is exactly one wherever the ratio is defined. -/
theorem normalized_gram_superdet {m n : Type*}
    [Fintype m] [DecidableEq m] [Fintype n] [DecidableEq n]
    (B : Matrix n m ℂ) (z : ℂ)
    (h : (1 + z • (B * B.conjTranspose)).det ≠ 0) :
    (1 + z • (B.conjTranspose * B)).det /
      (1 + z • (B * B.conjTranspose)).det = 1 := by
  rw [normalized_gram_determinants]
  exact div_self h

/-- Both target metrics in the example are genuinely positive Hermitian metrics. -/
theorem identity_metric_positive (r : ℝ) (hr : 0 < r) :
    (((r : ℂ) • (1 : Matrix (Fin 1) (Fin 1) ℂ))).PosDef := by
  have h : (r • (1 : Matrix (Fin 1) (Fin 1) ℂ)).PosDef := Matrix.PosDef.one.smul hr
  convert h using 1

/-- Actual weighted adjoint identity for the fixed differential d=I in dimension one.
The source metric is 1, the target metric is r; positivity is proved separately. -/
theorem identity_weighted_adjoint (r : ℝ) :
    (1 : Matrix (Fin 1) (Fin 1) ℂ).conjTranspose * ((r : ℂ) • 1) =
      ((r : ℂ) • (1 : Matrix (Fin 1) (Fin 1) ℂ)) := by
  simp

/-- Changing the target metric in a fixed exact identity complex changes both ordinary factors. -/
theorem identity_metric_laplacian_det (r : ℝ) (z : ℂ) :
    (((r : ℂ) • (1 : Matrix (Fin 1) (Fin 1) ℂ)) - z • 1).det = (r : ℂ) - z := by
  simp

/-- The metrics r=1 and r=4 give different ordinary spectral zeros on the same complex. -/
theorem identity_metric_moves_zero :
    (((1 : ℂ) • (1 : Matrix (Fin 1) (Fin 1) ℂ)) - 1 • 1).det = 0 ∧
    (((4 : ℂ) • (1 : Matrix (Fin 1) (Fin 1) ℂ)) - 1 • 1).det ≠ 0 := by
  norm_num [Matrix.det_fin_one]

/-- Boundary relative-product identity in any unital ring, including operator rings.
The inverse and commutation hypotheses are explicit; no positivity is assumed. -/
theorem boundary_relative_product {R : Type*} [Ring R] (P M N : R)
    (hMP : M * P = P * M) (hN : (1 - M) * N = 1) :
    (1 - M) * (P + (1 - P) * N) = 1 - P * M := by
  have hAP : (1 - M) * P = P * (1 - M) := by
    simp only [sub_mul, one_mul, mul_sub, mul_one]
    rw [hMP]
  have hAQ : (1 - M) * (1 - P) = (1 - P) * (1 - M) := by
    simp only [mul_sub, sub_mul, mul_one, one_mul]
    rw [hMP]
    abel
  calc
    (1 - M) * (P + (1 - P) * N) =
        P * (1 - M) + (1 - P) * ((1 - M) * N) := by
          rw [mul_add, ← mul_assoc, hAP, hAQ, mul_assoc]
    _ = 1 - P * M := by rw [hN, mul_one, mul_sub, mul_one]; abel

#check boundary_relative_product
#check odd_dirac_square
#check gram_partners_positive
#check shifted_matrix_factor
#check identity_metric_positive
#check normalized_gram_determinants
#check shifted_gram_determinants
#check normalized_gram_superdet
#check identity_weighted_adjoint
#check identity_metric_laplacian_det
#check identity_metric_moves_zero
#print axioms boundary_relative_product
#print axioms odd_dirac_square
#print axioms gram_partners_positive
#print axioms shifted_matrix_factor
#print axioms identity_metric_positive
#print axioms normalized_gram_determinants
#print axioms shifted_gram_determinants
#print axioms normalized_gram_superdet
#print axioms identity_weighted_adjoint
#print axioms identity_metric_laplacian_det
#print axioms identity_metric_moves_zero
end GRHResearch.Hodge
