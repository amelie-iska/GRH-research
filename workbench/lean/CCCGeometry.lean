import Mathlib.Tactic

/-! Polynomial identities for the existing conformal/cubic discussion.
The Hodge-star transformation law and genus hypotheses are in the written
mathematics. These declarations check their coefficient/exponent interfaces,
not a physical CCC crossover, an observational detection or a global spacetime. -/
set_option autoImplicit false
namespace CCCGeometry

theorem middle_form_conformal_exponent (Ω : ℝ) : Ω ^ ((4:ℕ)-2*2)=1 := by norm_num

theorem quartic_root_expansion (a b c d e r x : ℝ) :
 a*(r+x)^4+b*(r+x)^3+c*(r+x)^2+d*(r+x)+e
 = (a*r^4+b*r^3+c*r^2+d*r+e)
   +(4*a*r^3+3*b*r^2+2*c*r+d)*x
   +(6*a*r^2+3*b*r+c)*x^2+(4*a*r+b)*x^3+a*x^4 := by ring

theorem quartic_root_reciprocal (a b c d e r u : ℝ) (hu : u≠0)
 (hr : a*r^4+b*r^3+c*r^2+d*r+e=0) :
 u^4*(a*(r+1/u)^4+b*(r+1/u)^3+c*(r+1/u)^2+d*(r+1/u)+e)
 = (4*a*r^3+3*b*r^2+2*c*r+d)*u^3
   +(6*a*r^2+3*b*r+c)*u^2+(4*a*r+b)*u+a := by
 field_simp
 nlinarith only [congrArg (fun z : ℝ => z*u^4) hr]

theorem cubic_weierstrass_identity (A B C D u : ℝ) :
 A^2*(A*u^3+B*u^2+C*u+D)
 = (A*u+B/3)^3+(A*C-B^2/3)*(A*u+B/3)
   +(2*B^3/27-A*B*C/3+A^2*D) := by ring

theorem cubic_solution_transport (A B C D u v : ℝ)
 (h : v^2=A*u^3+B*u^2+C*u+D) :
 (A*v)^2=(A*u+B/3)^3+(A*C-B^2/3)*(A*u+B/3)
   +(2*B^3/27-A*B*C/3+A^2*D) := by
 calc (A*v)^2=A^2*v^2 := by ring
      _=A^2*(A*u^3+B*u^2+C*u+D) := by rw [h]
      _=_ := cubic_weierstrass_identity A B C D u

end CCCGeometry
#check CCCGeometry.middle_form_conformal_exponent
#check CCCGeometry.quartic_root_expansion
#check CCCGeometry.quartic_root_reciprocal
#check CCCGeometry.cubic_weierstrass_identity
#check CCCGeometry.cubic_solution_transport
#print axioms CCCGeometry.middle_form_conformal_exponent
#print axioms CCCGeometry.quartic_root_expansion
#print axioms CCCGeometry.quartic_root_reciprocal
#print axioms CCCGeometry.cubic_weierstrass_identity
#print axioms CCCGeometry.cubic_solution_transport
