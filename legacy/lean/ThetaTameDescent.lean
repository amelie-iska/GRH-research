import Mathlib.RingTheory.PowerSeries.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-! Actual formal-series and matrix components of the balanced theta-column descent.
The completed theta-order and valuation/category interfaces remain explicit prose. -/
namespace GRHResearch.ThetaTameDescent
open Matrix
variable {K : Type*} [Field K]

/-- The actual vertex rotation on the balanced three-column carrier. -/
def rotation {R : Type*} [CommRing R] : Matrix (Fin 3) (Fin 3) R := !![0,0,1;1,0,0;0,1,0]
def clock {R : Type*} [CommRing R] (z : R) : Matrix (Fin 3) (Fin 3) R := !![1,0,0;0,z^2,0;0,0,z]

lemma cubic_fourth (z : K) (hz : z^3=1) : z^4=z := by
  calc z^4=z*z^3 := by ring
       _=z := by rw [hz,mul_one]

/-- Clock/shift commutator with the sign determined by i -> i+1. -/
theorem clock_rotation (z : K) (hz : z^3=1) :
    clock z*rotation=z^2 • (rotation*clock z) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [clock,rotation,Matrix.mul_apply,Fin.sum_univ_three]
  · calc 1=z^3 := hz.symm
         _=_ := by ring
  · calc z=z^4 := (cubic_fourth z hz).symm
         _=_ := by ring

def weights : Fin 3 → ℕ := ![0,2,1]

/-- Genuine semilinear tame action on vectors of formal power series in v. -/
noncomputable def tame (z : K) (w : Fin 3 → PowerSeries K) : Fin 3 → PowerSeries K :=
  fun i => PowerSeries.C (z^(weights i))*PowerSeries.rescale z (w i)

/-- Exact coefficient action, including infinitely many formal coefficients. -/
theorem tame_coefficient (z : K) (w : Fin 3 → PowerSeries K) (i : Fin 3) (n : ℕ) :
    PowerSeries.coeff n (tame z w i)=z^(weights i+n)*PowerSeries.coeff n (w i) := by
  change PowerSeries.coeff n (PowerSeries.C (z^(weights i))*PowerSeries.rescale z (w i))=_
  rw [PowerSeries.coeff_C_mul,PowerSeries.coeff_rescale,pow_add,mul_assoc]

/-- An invariant coefficient must vanish unless its literal tame character is trivial. -/
theorem invariant_coefficient_zero (z : K) (w : Fin 3 → PowerSeries K)
    (hw : tame z w=w) (i : Fin 3) (n : ℕ) (hn : z^(weights i+n)≠1) :
    PowerSeries.coeff n (w i)=0 := by
  have he := congrArg (fun x : Fin 3 → PowerSeries K => PowerSeries.coeff n (x i)) hw
  change PowerSeries.coeff n (tame z w i)=PowerSeries.coeff n (w i) at he
  rw [tame_coefficient] at he
  have hzero : (z^(weights i+n)-1)*PowerSeries.coeff n (w i)=0 := by
    calc _=z^(weights i+n)*PowerSeries.coeff n (w i)-PowerSeries.coeff n (w i) := by ring
         _=0 := sub_eq_zero.mpr he
  exact (mul_eq_zero.mp hzero).resolve_left (sub_ne_zero.mpr hn)

/-- The actual tame power-series operator has order dividing three. -/
theorem tame_cube (z : K) (hz : z^3=1) (w : Fin 3 → PowerSeries K) :
    tame z (tame z (tame z w))=w := by
  ext i n
  rw [tame_coefficient,tame_coefficient,tame_coefficient]
  have hc : (z^(weights i+n))^3=1 := by
    rw [← pow_mul,Nat.mul_comm (weights i+n) 3,pow_mul,hz,one_pow]
  calc
    _=(z^(weights i+n))^3*PowerSeries.coeff n (w i) := by ring
    _=_ := by rw [hc,one_mul]

/-- Constant coefficient exposes the actual loss of two vertex fibers. -/
noncomputable def comparison : Matrix (Fin 3) (Fin 3) (PowerSeries K) :=
  !![1,0,0;0,PowerSeries.X,0;0,0,PowerSeries.X^2]

theorem comparison_determinant : (comparison : Matrix (Fin 3) (Fin 3) (PowerSeries K)).det=
    PowerSeries.X^3 := by
  simp [comparison,Matrix.det_fin_three]
  ring

theorem comparison_closed_fiber :
    (comparison.map PowerSeries.constantCoeff : Matrix (Fin 3) (Fin 3) K)=
      !![1,0,0;0,0,0;0,0,0] := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [comparison]

/-- The descended rotation is an actual u-weighted cycle, not an integral unit. -/
def weightedRotation {R : Type*} [CommRing R] (u : R) : Matrix (Fin 3) (Fin 3) R :=
  !![0,0,u;1,0,0;0,1,0]

variable {R : Type*} [CommRing R]
theorem weighted_rotation_cube (u : R) : (weightedRotation u)^3=u • (1 : Matrix (Fin 3) (Fin 3) R) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [weightedRotation,pow_succ,Matrix.mul_apply,Fin.sum_univ_three]

theorem weighted_rotation_polynomial (a b u t : R) :
    (1-t • (a • 1+b • weightedRotation u)).det=(1-a*t)^3-u*b^3*t^3 := by
  simp [weightedRotation,Matrix.det_fin_three]
  ring

/-- The commutator also forbids the nonconstant Jacobi rotation polynomial. -/
theorem rotation_polynomial_commutator (z a b : K) (hz : z^3=1) :
    clock z*(a • 1+b • rotation)-(a • 1+b • rotation)*clock z=
      (b*(z^2-1)) • (rotation*clock z) := by
  rw [mul_add,add_mul,Matrix.mul_smul,Matrix.mul_smul,Matrix.smul_mul,Matrix.smul_mul,
    Matrix.mul_one,Matrix.one_mul,clock_rotation z hz]
  ext i j
  simp
  ring

/-- Primitive cubic clock cannot commute with a+b*rotation when b is nonzero. -/
theorem no_nonconstant_rotation_descent (z a b : K) (hz : z^3=1) (hne : z≠1)
    (hb : b≠0) : clock z*(a • 1+b • rotation)≠(a • 1+b • rotation)*clock z := by
  intro he
  have hentry := congrArg (fun M : Matrix (Fin 3) (Fin 3) K => M 1 0) he
  simp [clock,rotation,Matrix.mul_apply,Fin.sum_univ_three] at hentry
  have hz2 : z^2=1 := by
    have : b*(z^2-1)=0 := by
      calc _=z^2*b-b := by ring
           _=0 := sub_eq_zero.mpr hentry
    exact sub_eq_zero.mp ((mul_eq_zero.mp this).resolve_left hb)
  apply hne
  calc z=z^2*z := by rw [hz2,one_mul]
       _=z^3 := by ring
       _=1 := hz

/-- The determinant line of the whole column has trivial clock and rotation. -/
theorem clock_rotation_determinants (z : K) (hz : z^3=1) :
    (clock z).det=1 ∧ (rotation : Matrix (Fin 3) (Fin 3) K).det=1 := by
  constructor
  · simp [clock,Matrix.det_fin_three]
    linear_combination hz
  · simp [rotation,Matrix.det_fin_three]

/-- Same-operator comparison: v*rotation descends to the u-weighted cycle. -/
theorem weighted_lift_intertwining :
    (comparison : Matrix (Fin 3) (Fin 3) (PowerSeries K))*weightedRotation (PowerSeries.X^3)=
      ((PowerSeries.X : PowerSeries K) • (rotation : Matrix (Fin 3) (Fin 3) (PowerSeries K)))*comparison := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [comparison,weightedRotation,rotation,Matrix.mul_apply,Fin.sum_univ_three] <;> ring

#check clock_rotation
#check tame_coefficient
#check invariant_coefficient_zero
#check tame_cube
#check comparison_determinant
#check comparison_closed_fiber
#check weighted_rotation_cube
#check weighted_rotation_polynomial
#check rotation_polynomial_commutator
#check no_nonconstant_rotation_descent
#check clock_rotation_determinants
#check weighted_lift_intertwining
#print axioms clock_rotation
#print axioms tame_coefficient
#print axioms invariant_coefficient_zero
#print axioms tame_cube
#print axioms comparison_determinant
#print axioms comparison_closed_fiber
#print axioms weighted_rotation_cube
#print axioms weighted_rotation_polynomial
#print axioms rotation_polynomial_commutator
#print axioms no_nonconstant_rotation_descent
#print axioms clock_rotation_determinants
#print axioms weighted_lift_intertwining
end GRHResearch.ThetaTameDescent
