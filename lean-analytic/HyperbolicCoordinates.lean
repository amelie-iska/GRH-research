import Mathlib.Analysis.Complex.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace GRHResearch.HyperbolicCoordinates

/-- Actual rational Poincare-to-Lorentz coordinates satisfy the hyperboloid equation. -/
theorem disk_to_hyperboloid (x y : ℝ) (h : 1-x^2-y^2 ≠ 0) :
    ((1+x^2+y^2)/(1-x^2-y^2))^2 -
    (2*x/(1-x^2-y^2))^2 - (2*y/(1-x^2-y^2))^2 = 1 := by
  field_simp [h]
  ring

/-- Inverse stereographic coordinates preserve the exact disk defect. -/
theorem inverse_disk_defect (X Y T : ℝ) (hT : T+1 ≠ 0)
    (h : T^2-X^2-Y^2=1) :
    1-(X/(T+1))^2-(Y/(T+1))^2=2/(T+1) := by
  field_simp [hT]
  nlinarith

/-- A genuine rotation in one real coordinate plane preserves four-dimensional norm. -/
theorem rotation_four_norm (a b c d p q : ℝ) (h : p^2+q^2=1) :
    (p*a-q*c)^2+b^2+(q*a+p*c)^2+d^2=a^2+b^2+c^2+d^2 := by
  calc
    _=(p^2+q^2)*(a^2+c^2)+b^2+d^2 := by ring
    _=_ := by rw [h]; ring

#check disk_to_hyperboloid
#check inverse_disk_defect
#check rotation_four_norm
#print axioms disk_to_hyperboloid
#print axioms inverse_disk_defect
#print axioms rotation_four_norm
end GRHResearch.HyperbolicCoordinates
