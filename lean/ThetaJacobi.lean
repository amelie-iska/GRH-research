import Mathlib.NumberTheory.JacobiSum.Basic
import Mathlib.Analysis.Complex.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace GRHResearch.ThetaJacobi
open Finset
variable {F : Type*} [Field F] [Fintype F]

/-- Conjugation of the genuine zero-extended finite-field Jacobi sum. -/
theorem jacobi_conjugate (rho eta : MulChar F ℂ) :
    star (jacobiSum rho eta)=jacobiSum rho⁻¹ eta⁻¹ := by
  simp only [jacobiSum,star_sum,star_mul,MulChar.star_apply',mul_comm]

/-- Actual finite-field character norm identity; nontrivialities are explicit. -/
theorem jacobi_norm_sq (rho eta : MulChar F ℂ)
    (hr : rho≠1) (he : eta≠1) (hre : rho*eta≠1) :
    ‖jacobiSum rho eta‖^2=(Fintype.card F : ℝ) := by
  have hc : ringChar ℂ≠ringChar F := by
    rw [ringChar.eq_zero]
    exact (CharP.ringChar_ne_zero_of_finite F).symm
  have h := jacobiSum_mul_jacobiSum_inv hc hr he hre
  rw [← jacobi_conjugate] at h
  have hreal := congrArg Complex.re h
  simpa only [Complex.star_def,Complex.mul_conj,Complex.ofReal_re,
    Complex.normSq_eq_norm_sq,Complex.natCast_re] using hreal

/-- Multiplicative rescaling, including zero character values at the endpoints. -/
theorem shifted_jacobi (rho eta : MulChar F ℂ) (d : F) (hd : d≠0) :
    (∑ t : F, rho t*eta (t-d))=rho d*eta (-d)*jacobiSum rho eta := by
  classical
  calc
    _=∑ u : F, rho (d*u)*eta (d*u-d) :=
      (Equiv.sum_comp (Equiv.mulLeft₀ d hd) (fun t => rho t*eta (t-d))).symm
    _=∑ u : F, rho d*eta (-d)*(rho u*eta (1-u)) := by
      apply Finset.sum_congr rfl
      intro u _
      rw [show d*u-d=(-d)*(1-u) by ring,map_mul,map_mul]
      ring
    _=_ := by rw [← Finset.mul_sum,jacobiSum]

/-- Cubic and quadratic characters cannot cancel each other nontrivially. -/
theorem cubic_quadratic_product_ne_one {K : Type*} [Field K] (rho eta : MulChar K ℂ)
    (hr : rho^3=1) (he : eta^2=1) (hrn : rho≠1) : rho*eta≠1 := by
  intro h
  have hi : rho=eta⁻¹ := by
    calc
      rho=rho*eta*eta⁻¹ := by simp
      _=eta⁻¹ := by rw [h,one_mul]
  have h2 : rho^2=1 := by rw [hi,inv_pow,he,inv_one]
  apply hrn
  calc
    rho=rho^2*rho := by rw [h2,one_mul]
    _=rho^3 := (pow_succ rho 2).symm
    _=1 := hr

variable {R : Type*} [CommRing R]

def cmMatrix (a b : R) : Matrix (Fin 2) (Fin 2) R := !![a,-b;b,a-b]
def gram : Matrix (Fin 2) (Fin 2) R := !![2,-1;-1,2]

theorem cm_determinant (a b : R) : (cmMatrix a b).det=a^2-a*b+b^2 := by
  simp [cmMatrix,Matrix.det_fin_two]
  ring

theorem cm_local_polynomial (a b t : R) :
    (1-t • cmMatrix a b).det=1-(2*a-b)*t+(a^2-a*b+b^2)*t^2 := by
  simp [cmMatrix,Matrix.det_fin_two]
  ring

/-- The fixed positive CM Gram form gives a scaled isometry, not self-adjointness. -/
theorem cm_gram_identity (a b : R) :
    (cmMatrix a b).transpose*gram*cmMatrix a b=(a^2-a*b+b^2) • gram := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [cmMatrix,gram,Matrix.mul_apply,Fin.sum_univ_two] <;> ring

theorem cm_gram_positive (x y : ℝ) (h : x≠0 ∨ y≠0) :
    0 < 2*x^2-2*x*y+2*y^2 := by
  have hs := sq_nonneg (x-y)
  have hx := sq_nonneg x
  have hy := sq_nonneg y
  rcases h with h|h
  · have hp := sq_pos_of_ne_zero h
    nlinarith
  · have hp := sq_pos_of_ne_zero h
    nlinarith

/-- Exact split-prime7 arithmetic multiplication matrices, after the character sum computation. -/
theorem f7_local_polynomials (t : ℤ) :
    (1-t • cmMatrix (3:ℤ) 2).det=1-4*t+7*t^2 ∧
    (1-t • cmMatrix (-1:ℤ) (-3)).det=1-t+7*t^2 := by
  constructor <;> rw [cm_local_polynomial] <;> ring

/-- Boundary of the genuine cellular theta graph (both vertices and all three edges). -/
def cellularBoundary : Matrix (Fin 2) (Fin 3) R := !![-1,-1,-1;1,1,1]
def cyclePermutation : Matrix (Fin 3) (Fin 3) R := !![0,0,1;1,0,0;0,1,0]
def homologyInclusion : Matrix (Fin 3) (Fin 2) R := !![1,0;-1,1;0,-1]
def cellularEdge (a b : R) : Matrix (Fin 3) (Fin 3) R := a • 1+b • cyclePermutation

theorem cellular_inclusion_cycles :
    (cellularBoundary : Matrix (Fin 2) (Fin 3) R)*homologyInclusion (R:=R)=0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [cellularBoundary,homologyInclusion,Matrix.mul_apply,Fin.sum_univ_three]

theorem cellular_homology_restriction (a b : R) :
    cellularEdge a b*homologyInclusion=homologyInclusion*cmMatrix a b := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [cellularEdge,homologyInclusion,cyclePermutation,cmMatrix,
      Matrix.mul_apply,Fin.sum_univ_two,Fin.sum_univ_three] <;> ring

theorem cellular_edge_polynomial (a b t : R) :
    (1-t • cellularEdge a b).det=
      (1-(a+b)*t)*(1-(2*a-b)*t+(a^2-a*b+b^2)*t^2) := by
  simp [cellularEdge,cyclePermutation,Matrix.det_fin_three]
  ring

/-- Actual rational vertex action; the half factors normalize H0 and the boundary separately. -/
def cellularVertex (a b : ℚ) : Matrix (Fin 2) (Fin 2) ℚ :=
  !![(1+a+b)/2,(1-a-b)/2;(1-a-b)/2,(1+a+b)/2]

theorem cellular_chain_map (a b : ℚ) :
    cellularVertex a b*cellularBoundary=cellularBoundary*cellularEdge a b := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [cellularVertex,cellularBoundary,cellularEdge,cyclePermutation,
      Matrix.mul_apply,Fin.sum_univ_two,Fin.sum_univ_three] <;> ring

def conjugationMatrix : Matrix (Fin 2) (Fin 2) R := !![1,-1;0,-1]

theorem conjugation_matrix_identities :
    (conjugationMatrix : Matrix (Fin 2) (Fin 2) R)*conjugationMatrix=1 ∧
    conjugationMatrix*cmMatrix (0:R) 1=
      (cmMatrix (0:R) 1*cmMatrix (0:R) 1)*conjugationMatrix ∧
    conjugationMatrix.transpose*gram*conjugationMatrix=(gram : Matrix (Fin 2) (Fin 2) R) := by
  constructor
  · ext i j
    fin_cases i <;> fin_cases j <;>
      simp [conjugationMatrix,Matrix.mul_apply,Fin.sum_univ_two]
  constructor <;> ext i j <;>
    fin_cases i <;> fin_cases j <;>
    simp [conjugationMatrix,cmMatrix,gram,Matrix.mul_apply,Fin.sum_univ_two] <;> ring

/-- Inert Frobenius cannot be a real two-dimensional map with the fixed cubic deck action. -/
theorem inert_real_determinant_nonpositive (M : Matrix (Fin 2) (Fin 2) ℝ)
    (h : M*cmMatrix 0 1=(cmMatrix 0 1*cmMatrix 0 1)*M) : M.det≤0 := by
  have h00 := congrArg (fun N : Matrix (Fin 2) (Fin 2) ℝ => N 0 0) h
  have h01 := congrArg (fun N : Matrix (Fin 2) (Fin 2) ℝ => N 0 1) h
  simp [cmMatrix,Matrix.mul_apply,Fin.sum_univ_two] at h00 h01
  have hc : M 1 0=M 0 0+M 0 1 := by linarith
  have hd : M 1 1= -M 0 0 := by linarith
  rw [Matrix.det_fin_two,hc,hd]
  nlinarith [sq_nonneg (M 0 0+M 0 1),sq_nonneg (M 0 0),sq_nonneg (M 0 1)]

theorem no_inert_real_frobenius (q : ℝ) (hq : 0<q)
    (M : Matrix (Fin 2) (Fin 2) ℝ)
    (h : M*cmMatrix 0 1=(cmMatrix 0 1*cmMatrix 0 1)*M) (hd : M.det=q) : False := by
  have hn := inert_real_determinant_nonpositive M h
  linarith

#check jacobi_conjugate
#check jacobi_norm_sq
#check shifted_jacobi
#check cubic_quadratic_product_ne_one
#check cm_determinant
#check cm_local_polynomial
#check cm_gram_identity
#check cm_gram_positive
#check f7_local_polynomials
#check cellular_inclusion_cycles
#check cellular_homology_restriction
#check cellular_edge_polynomial
#check cellular_chain_map
#print axioms cellular_inclusion_cycles
#print axioms cellular_homology_restriction
#print axioms cellular_edge_polynomial
#print axioms cellular_chain_map
#check conjugation_matrix_identities
#check inert_real_determinant_nonpositive
#check no_inert_real_frobenius
#print axioms conjugation_matrix_identities
#print axioms inert_real_determinant_nonpositive
#print axioms no_inert_real_frobenius
#print axioms jacobi_conjugate
#print axioms jacobi_norm_sq
#print axioms shifted_jacobi
#print axioms cubic_quadratic_product_ne_one
#print axioms cm_determinant
#print axioms cm_local_polynomial
#print axioms cm_gram_identity
#print axioms cm_gram_positive
#print axioms f7_local_polynomials
end GRHResearch.ThetaJacobi
