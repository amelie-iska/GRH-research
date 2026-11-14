import Mathlib.Analysis.SpecialFunctions.Pow.Complex
import Mathlib.LinearAlgebra.Matrix.PosDef

open Matrix Complex
open scoped ComplexOrder

namespace GRHResearch.Analytic

/-- The universal finite-product estimate underlying the scaled Jensen coefficient
error. Analytic summation and the xi specialization remain prose proofs. -/
theorem finite_product_defect_bound {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (a : ι → ℝ) (ha : ∀ i ∈ s, 0 ≤ a i ∧ a i ≤ 1) :
    0 ≤ ∏ i ∈ s, (1 - a i) ∧ (∏ i ∈ s, (1 - a i)) ≤ 1 ∧
      1 - (∏ i ∈ s, (1 - a i)) ≤ ∑ i ∈ s, a i := by
  induction s using Finset.induction_on with
  | empty => simp
  | @insert i s hi ih =>
    have hai := ha i (Finset.mem_insert_self i s)
    have has : ∀ j ∈ s, 0 ≤ a j ∧ a j ≤ 1 := by
      intro j hj
      exact ha j (Finset.mem_insert_of_mem hj)
    obtain ⟨h0, h1, hdef⟩ := ih has
    simp only [Finset.prod_insert hi, Finset.sum_insert hi]
    refine ⟨mul_nonneg (sub_nonneg.mpr hai.2) h0, ?_, ?_⟩
    · nlinarith [mul_nonneg hai.1 h0]
    · nlinarith [mul_nonneg hai.1 (sub_nonneg.mpr h1)]

/-- A positive coefficient-defined metric makes an actual matrix's eigenvalues real.
The arithmetic problem is to prove positivity for the proposed metric. -/
theorem positive_metric_eigenvalue_real {ι : Type*} [Fintype ι]
    {C H : Matrix ι ι ℂ} {v : ι → ℂ} {z : ℂ}
    (hH : H.PosDef) (hHC : (H * C).IsHermitian) (hv : v ≠ 0)
    (heigen : C *ᵥ v = z • v) : z.im = 0 := by
  have heq : star v ⬝ᵥ ((H * C) *ᵥ v) = z * (star v ⬝ᵥ (H *ᵥ v)) := by
    rw [← Matrix.mulVec_mulVec, heigen, Matrix.mulVec_smul, dotProduct_smul]
    rfl
  have him := congrArg Complex.im heq
  have ha : (star v ⬝ᵥ ((H * C) *ᵥ v)).im = 0 :=
    hHC.im_star_dotProduct_mulVec_self v
  have hb : (star v ⬝ᵥ (H *ᵥ v)).im = 0 :=
    hH.isHermitian.im_star_dotProduct_mulVec_self v
  have hp : 0 < (star v ⬝ᵥ (H *ᵥ v)).re := hH.re_dotProduct_pos hv
  simp only [Complex.mul_im, ha, hb, mul_zero, zero_add] at him
  nlinarith

/-- Companion for x²+b x+a, in the basis (1,x). -/
def quadraticCompanion (a b : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![0, -a; 1, -b]

/-- The Newton-sum Hermite matrix, not the moment matrix of a Fourier kernel. -/
def quadraticHermite (a b : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![2, -b; -b, b^2 - 2*a]

theorem quadratic_hermite_symmetrizes (a b : ℝ) :
    quadraticHermite a b * quadraticCompanion a b =
      (quadraticHermite a b * quadraticCompanion a b)ᵀ := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [quadraticHermite, quadraticCompanion, Matrix.mul_apply, Fin.sum_univ_two] <;> ring

theorem quadratic_hermite_det (a b : ℝ) :
    (quadraticHermite a b).det = b^2 - 4*a := by
  simp [quadraticHermite, Matrix.det_fin_two]
  ring

theorem quadratic_hermite_form (a b : ℝ) (v : Fin 2 → ℝ) :
    star v ⬝ᵥ (quadraticHermite a b *ᵥ v) =
      2 * (v 0 - b*v 1/2)^2 + ((b^2 - 4*a)/2) * (v 1)^2 := by
  simp [quadraticHermite, dotProduct, Matrix.mulVec, Fin.sum_univ_two]
  ring

/-- The displayed discriminant inequality is an explicit hypothesis, not an RH proof. -/
theorem quadratic_hermite_posDef {a b : ℝ} (hdisc : 0 < b^2 - 4*a) :
    (quadraticHermite a b).PosDef := by
  constructor
  · ext i j
    fin_cases i <;> fin_cases j <;> simp [quadraticHermite, Matrix.conjTranspose_apply]
  · intro v hv
    rw [quadratic_hermite_form]
    by_cases h1 : v 1 = 0
    · have h0 : v 0 ≠ 0 := by
        intro h0
        apply hv
        funext i
        fin_cases i <;> simp [h0, h1]
      simpa [h1] using mul_pos (by norm_num : (0 : ℝ) < 2) (sq_pos_of_ne_zero h0)
    · exact add_pos_of_nonneg_of_pos (mul_nonneg (by norm_num) (sq_nonneg _))
        (mul_pos (div_pos hdisc (by norm_num)) (sq_pos_of_ne_zero h1))

/-- Gaussian smoothing of the explicit positive two-atom moment example does not
repair the degree-two Jensen inequality. The measure integral identities are prose. -/
theorem gaussian_mixture_turan_obstruction (variance : ℝ) :
    ((variance + 1/10)/2)^2 -
      (3*variance^2 + (3/5)*variance + 1/10)/12 = -(7/1200 : ℝ) := by
  ring

#print axioms finite_product_defect_bound
#print axioms positive_metric_eigenvalue_real
#print axioms quadratic_hermite_symmetrizes
#print axioms quadratic_hermite_det
#print axioms quadratic_hermite_form
#print axioms quadratic_hermite_posDef
#print axioms gaussian_mixture_turan_obstruction
end GRHResearch.Analytic
