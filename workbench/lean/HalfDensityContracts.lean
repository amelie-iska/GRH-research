import Mathlib.Tactic
import Mathlib.Algebra.Star.Unitary

/-! Algebraic interfaces for energy-controlled flow and its half-density lift.
The global ODE/Stone theorem is proved in the written exposition, using its
stated analytic hypotheses; it is not introduced as an axiom in this module. -/
set_option autoImplicit false
namespace HalfDensityContracts

theorem triad_energy (a b c x y z ν l1 l2 l3 f1 f2 f3 : ℝ)
 (hc : a+b+c=0) :
 x*(a*y*z-ν*l1*x+f1)+y*(b*x*z-ν*l2*y+f2)+z*(c*x*y-ν*l3*z+f3)
 = -ν*(l1*x^2+l2*y^2+l3*z^2)+(x*f1+y*f2+z*f3) := by
 have h := congrArg (fun s : ℝ => s*x*y*z) hc
 nlinarith only [h]

theorem triad_divergence (ν l1 l2 l3 : ℝ) :
 -ν*l1 + -ν*l2 + -ν*l3 = -ν*(l1+l2+l3) := by ring

theorem half_density_weight (J f : ℝ) (hJ : 0 ≤ J) :
 (Real.sqrt J*f)^2=J*f^2 := by
 calc (Real.sqrt J*f)^2=(Real.sqrt J)^2*f^2 := by ring
      _=J*f^2 := by rw [Real.sq_sqrt hJ]

theorem skew_shift_normal {R : Type*} [Ring R] [StarRing R]
 (x : R) (hx : star x = -x) : Commute (1+x) (star (1+x)) := by
 change (1+x)*star (1+x)=star (1+x)*(1+x)
 simp only [star_add, star_one, hx]
 noncomm_ring

theorem normal_unit_cayley {R : Type*} [Ring R] [StarRing R]
 (u : Rˣ) (h : Commute u (star u)) :
 star ((star u)*u⁻¹) * ((star u)*u⁻¹)=1 := by
 calc star ((star u)*u⁻¹) * ((star u)*u⁻¹)
       = (star u)⁻¹ * (u*star u) * u⁻¹ := by simp [star_mul, mul_assoc]
      _ = (star u)⁻¹ * (star u*u) * u⁻¹ := by rw [h.eq]
      _ = 1 := by group

end HalfDensityContracts
#check HalfDensityContracts.triad_energy
#check HalfDensityContracts.triad_divergence
#check HalfDensityContracts.half_density_weight
#check HalfDensityContracts.skew_shift_normal
#check HalfDensityContracts.normal_unit_cayley
#print axioms HalfDensityContracts.triad_energy
#print axioms HalfDensityContracts.triad_divergence
#print axioms HalfDensityContracts.half_density_weight
#print axioms HalfDensityContracts.skew_shift_normal
#print axioms HalfDensityContracts.normal_unit_cayley
