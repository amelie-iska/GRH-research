import Mathlib.LinearAlgebra.Matrix.Block
import Mathlib.RingTheory.PowerSeries.Basic
import Mathlib.Algebra.Polynomial.Degree.Operations
import Lean.Elab.Tactic.Omega
import Mathlib.Tactic.Ring

/-! Components of the actual theta-order special-fiber argument.
The passage from order endomorphisms to these six path blocks is proved in prose;
it is not an additional formal hypothesis claiming arithmetic positivity. -/
namespace GRHResearch.ThetaProjectiveMultiplicity
open Finset Matrix
variable {R : Type*} [CommRing R]
variable {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- The fiber of the path-block index is genuinely equivalent to its coefficient index. -/
def blockFiberEquiv (k : Fin 6) : {x : Fin 6 × ι // x.1 = k} ≃ ι where
  toFun x := x.val.2
  invFun i := ⟨(k,i),rfl⟩
  left_inv x := by apply Subtype.ext; exact Prod.ext x.property.symm rfl
  right_inv _ := rfl

/-- Six identical path diagonal blocks force a sixth power, allowing every upper block. -/
theorem six_path_blocks_det (M : Matrix (Fin 6 × ι) (Fin 6 × ι) R)
    (A : Matrix ι ι R) (ht : M.BlockTriangular Prod.fst)
    (hd : ∀ k i j, M (k,i) (k,j)=A i j) : M.det=A.det^6 := by
  rw [ht.det_fintype]
  have hb (k : Fin 6) : (M.toSquareBlock Prod.fst k).det=A.det := by
    rw [← Matrix.det_reindex_self (blockFiberEquiv k) (M.toSquareBlock Prod.fst k)]
    congr 1
    ext i j
    exact hd k i j
  simp_rw [hb]
  simp

/-- Characteristic factors use the same six-block argument, with an explicit scalar parameter. -/
theorem six_path_blocks_local_det (M : Matrix (Fin 6 × ι) (Fin 6 × ι) R)
    (A : Matrix ι ι R) (ht : M.BlockTriangular Prod.fst)
    (hd : ∀ k i j, M (k,i) (k,j)=A i j) (t : R) :
    (1-t • M).det=(1-t • A).det^6 := by
  apply six_path_blocks_det
  · intro i j hij
    have hn : i≠j := fun h => (ne_of_lt hij) (congrArg Prod.fst h.symm)
    simp [Matrix.sub_apply,Matrix.smul_apply,Matrix.one_apply_ne hn,ht hij]
  · intro k i j
    simp only [Matrix.sub_apply,Matrix.smul_apply,smul_eq_mul,hd]
    congr 1
    simp [Matrix.one_apply]

/-- Literal constant-coefficient specialization on matrices over the completed base. -/
theorem power_series_det_specialization (M : Matrix ι ι (PowerSeries R)) (t : R) :
    PowerSeries.constantCoeff ((1-PowerSeries.C t • M).det)=
      (1-t • M.map PowerSeries.constantCoeff).det := by
  rw [RingHom.map_det]
  congr 1
  ext i j
  simp [Matrix.one_apply]

/-- A nonconstant quadratic cannot be a rational-function sixth power, even with cancellation. -/
theorem quadratic_not_ratio_sixth (P A B : Polynomial ℚ)
    (hp : P.natDegree=2) (hb : B≠0) : P*B^6≠A^6 := by
  have hp0 : P≠0 := by intro h; simp [h] at hp
  intro h
  have ha : A≠0 := by
    intro h0
    rw [h0,zero_pow (by decide : 6≠0)] at h
    exact (mul_ne_zero hp0 (pow_ne_zero 6 hb)) h
  have hd := congrArg Polynomial.natDegree h
  rw [Polynomial.natDegree_mul hp0 (pow_ne_zero 6 hb),
    Polynomial.natDegree_pow,Polynomial.natDegree_pow,hp] at hd
  omega

/-- Genuine formal-series obstruction to a central-fixed cyclic rank-one branch carrier.
The two equivalences record what invertible rank-one deck intertwiners imply on residues. -/
theorem no_cyclic_rank_one_arrows {K : Type*} [Field K]
    (a b c : PowerSeries K)
    (hab : PowerSeries.constantCoeff a=0 ↔ PowerSeries.constantCoeff b=0)
    (hbc : PowerSeries.constantCoeff b=0 ↔ PowerSeries.constantCoeff c=0)
    (hprod : a*b*c=PowerSeries.X) : False := by
  have hz : PowerSeries.constantCoeff a*PowerSeries.constantCoeff b*
      PowerSeries.constantCoeff c=0 := by
    simpa only [map_mul,PowerSeries.constantCoeff_X] using
      congrArg PowerSeries.constantCoeff hprod
  have ha : PowerSeries.constantCoeff a=0 := by
    rcases mul_eq_zero.mp hz with h|h
    · rcases mul_eq_zero.mp h with h|h
      · exact h
      · exact hab.mpr h
    · exact hab.mpr (hbc.mpr h)
  have hb := hab.mp ha
  obtain ⟨a',ha'⟩ := PowerSeries.X_dvd_iff.mpr ha
  obtain ⟨b',hb'⟩ := PowerSeries.X_dvd_iff.mpr hb
  have hf : PowerSeries.X*(PowerSeries.X*(a'*b'*c))=
      (PowerSeries.X : PowerSeries K)*1 := by
    calc
      _=a*b*c := by rw [ha',hb']; ring
      _=PowerSeries.X := hprod
      _=_ := (mul_one _).symm
  have hc := PowerSeries.X_mul_cancel hf
  have he := congrArg PowerSeries.constantCoeff hc
  simp at he

#check six_path_blocks_det
#check six_path_blocks_local_det
#check power_series_det_specialization
#check quadratic_not_ratio_sixth
#check no_cyclic_rank_one_arrows
#print axioms six_path_blocks_det
#print axioms six_path_blocks_local_det
#print axioms power_series_det_specialization
#print axioms quadratic_not_ratio_sixth
#print axioms no_cyclic_rank_one_arrows
end GRHResearch.ThetaProjectiveMultiplicity
