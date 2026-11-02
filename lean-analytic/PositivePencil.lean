import Mathlib.Analysis.SpecialFunctions.Pow.Complex
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.LinearAlgebra.Matrix.ToLinearEquiv

open Matrix Complex
open scoped ComplexOrder

namespace GRHResearch.Analytic

/-- The scalar quadratic-form identity for a positive Hermitian generalized eigenpair. -/
theorem real_ratio_from_positive_form {a b z : ℂ} (ha : a.im = 0) (hb : b.im = 0)
    (hpositive : 0 < b.re) (heq : a = z * b) : z.im = 0 := by
  have him := congrArg Complex.im heq
  simp only [Complex.mul_im, ha, hb, mul_zero, zero_add] at him
  nlinarith

/-- Positive-definite B forces every generalized eigenvalue of (A,B) to be real. -/
theorem positive_pencil_eigenvalue_real {ι : Type*} [Fintype ι]
    {A B : Matrix ι ι ℂ} {v : ι → ℂ} {z : ℂ}
    (hA : A.IsHermitian) (hB : B.PosDef) (hv : v ≠ 0)
    (heigen : A *ᵥ v = z • (B *ᵥ v)) : z.im = 0 := by
  have heq : star v ⬝ᵥ (A *ᵥ v) = z * (star v ⬝ᵥ (B *ᵥ v)) := by
    rw [heigen, dotProduct_smul]
    rfl
  exact real_ratio_from_positive_form
    (hA.im_star_dotProduct_mulVec_self v)
    (hB.isHermitian.im_star_dotProduct_mulVec_self v)
    (hB.re_dotProduct_pos hv) heq

/-- Singular generalized positive Hermitian pencils have real spectral parameter. -/
theorem positive_pencil_det_zero_real {ι : Type*} [Fintype ι] [DecidableEq ι]
    {A B : Matrix ι ι ℂ} {z : ℂ} (hA : A.IsHermitian) (hB : B.PosDef)
    (hdet : (A - z • B).det = 0) : z.im = 0 := by
  obtain ⟨v, hv, hkernel⟩ := Matrix.exists_mulVec_eq_zero_iff.mpr hdet
  have heigen : A *ᵥ v = z • (B *ᵥ v) := by
    rw [Matrix.sub_mulVec, Matrix.smul_mulVec] at hkernel
    exact sub_eq_zero.mp hkernel
  exact positive_pencil_eigenvalue_real hA hB hv heigen

/-- This is an actual matrix nonvanishing theorem, not an assumed spectral bridge. -/
theorem positive_pencil_det_ne_zero {ι : Type*} [Fintype ι] [DecidableEq ι]
    {A B : Matrix ι ι ℂ} {z : ℂ} (hA : A.IsHermitian) (hB : B.PosDef)
    (hz : z.im ≠ 0) : (A - z • B).det ≠ 0 := by
  intro hdet
  exact hz (positive_pencil_det_zero_real hA hB hdet)

/-- The substitution z=-i(s-1/2) transports the real spectrum to the critical line. -/
theorem centered_positive_pencil_zero_on_line {ι : Type*} [Fintype ι] [DecidableEq ι]
    {A B : Matrix ι ι ℂ} {s : ℂ} (hA : A.IsHermitian) (hB : B.PosDef)
    (hdet : (A - ((-I) * (s - (1 / 2 : ℂ))) • B).det = 0) : s.re = 1 / 2 := by
  have hz := positive_pencil_det_zero_real hA hB hdet
  simp [Complex.mul_im] at hz
  linarith

/-- Strict imaginary quadratic-form positivity excludes a matrix kernel at that point. -/
theorem det_ne_zero_of_strict_imaginary_form {ι : Type*} [Fintype ι] [DecidableEq ι]
    {M : Matrix ι ι ℂ}
    (hpositive : ∀ v : ι → ℂ, v ≠ 0 → 0 < (star v ⬝ᵥ (M *ᵥ v)).im) :
    M.det ≠ 0 := by
  intro hdet
  obtain ⟨v, hv, hkernel⟩ := Matrix.exists_mulVec_eq_zero_iff.mpr hdet
  have hpos := hpositive v hv
  rw [hkernel, dotProduct_zero] at hpos
  exact (lt_irrefl (0 : ℝ)) hpos

/-- An explicit indefinite Hermitian-pencil determinant has a zero at s=1/4. -/
theorem indefinite_pencil_off_line_witness :
    ((!![(0 : ℂ), 1 / 4; 1 / 4, 0] -
      ((-I) * ((1 / 4 : ℂ) - 1 / 2)) • !![(1 : ℂ), 0; 0, -1]).det = 0) ∧
    (1 / 4 : ℝ) ≠ 1 / 2 := by
  constructor
  · norm_num [Matrix.det_fin_two]
    ring_nf
    norm_num
  · norm_num

#print axioms real_ratio_from_positive_form
#print axioms positive_pencil_eigenvalue_real
#print axioms positive_pencil_det_zero_real
#print axioms positive_pencil_det_ne_zero
#print axioms centered_positive_pencil_zero_on_line
#print axioms det_ne_zero_of_strict_imaginary_form
#print axioms indefinite_pencil_off_line_witness
end GRHResearch.Analytic
