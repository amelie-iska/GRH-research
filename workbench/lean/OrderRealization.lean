import Mathlib.Tactic

/-! Coordinates of the explicit rank-four order [[a,b],[pi*c,d]].
The specialization pi=0 is the radical-square-zero two-cycle multiplication.
The generic-fiber matrix algebra and global representation theory are proved
in the accompanying written argument, not added as axioms here. -/
set_option autoImplicit false
open scoped BigOperators
namespace OrderRealization

structure Coordinates (R : Type*) where
 a : R
 b : R
 c : R
 d : R
 deriving DecidableEq

variable {R : Type*} [CommRing R]

def mul (pi : R) (x y : Coordinates R) : Coordinates R :=
 ⟨x.a*y.a+pi*x.b*y.c, x.a*y.b+x.b*y.d,
  x.c*y.a+x.d*y.c, pi*x.c*y.b+x.d*y.d⟩
def one : Coordinates R := ⟨1,0,0,1⟩
def e1 : Coordinates R := ⟨1,0,0,0⟩
def e2 : Coordinates R := ⟨0,0,0,1⟩
def arrowU : Coordinates R := ⟨0,1,0,0⟩
def arrowV : Coordinates R := ⟨0,0,1,0⟩

theorem multiplication_associative (pi : R) (x y z : Coordinates R) :
 mul pi (mul pi x y) z = mul pi x (mul pi y z) := by
 cases x; cases y; cases z
 simp only [mul, Coordinates.mk.injEq]
 constructor
 · ring
 constructor
 · ring
 constructor <;> ring

theorem unit_left (pi : R) (x : Coordinates R) : mul pi one x=x := by
 cases x; simp [mul,one]
theorem unit_right (pi : R) (x : Coordinates R) : mul pi x one=x := by
 cases x; simp [mul,one]

theorem arrows_uv (pi : R) : mul pi arrowU arrowV = (⟨pi,0,0,0⟩ : Coordinates R) := by
 simp [mul,arrowU,arrowV]
theorem arrows_vu (pi : R) : mul pi arrowV arrowU = (⟨0,0,0,pi⟩ : Coordinates R) := by
 simp [mul,arrowU,arrowV]
theorem special_fiber_uv : mul (0:R) arrowU arrowV = (⟨0,0,0,0⟩ : Coordinates R) := by
 simp [mul,arrowU,arrowV]
theorem special_fiber_vu : mul (0:R) arrowV arrowU = (⟨0,0,0,0⟩ : Coordinates R) := by
 simp [mul,arrowU,arrowV]
theorem arrow_u_squared (pi : R) : mul pi arrowU arrowU = (⟨0,0,0,0⟩ : Coordinates R) := by
 simp [mul,arrowU]
theorem arrow_v_squared (pi : R) : mul pi arrowV arrowV = (⟨0,0,0,0⟩ : Coordinates R) := by
 simp [mul,arrowV]

theorem heat_weight_sum (r : ℝ) : (1-4*r)+r+r+r+r=1 := by ring

theorem heat_weight_positive (r : ℝ) (hr : 0≤r) (h : r≤1/4) :
 0≤1-4*r ∧ 0≤r := by constructor <;> linarith

theorem sector_gap_expectation {ι : Type*} [Fintype ι]
 (p energy ground : ι → ℝ) (gap : ℝ)
 (hp : ∀ i, 0≤p i) (hmass : ∑ i, p i = 1)
 (h : ∀ i, gap*(1-ground i)≤energy i) :
 gap*(1-∑ i,p i*ground i) ≤ ∑ i,p i*energy i := by
 have hh : (∑ i, p i*(gap*(1-ground i))) ≤ ∑ i,p i*energy i :=
   Finset.sum_le_sum (fun i _ => mul_le_mul_of_nonneg_left (h i) (hp i))
 have he : (∑ i, p i*(gap*(1-ground i))) = gap*(1-∑ i,p i*ground i) := by
   calc (∑ i, p i*(gap*(1-ground i))) = ∑ i, (gap*p i-gap*(p i*ground i)) := by
          apply Finset.sum_congr rfl
          intro i _
          ring
        _ = gap*(∑ i,p i)-gap*(∑ i,p i*ground i) := by rw [Finset.sum_sub_distrib,← Finset.mul_sum,← Finset.mul_sum]
        _ = gap*(1-∑ i,p i*ground i) := by rw [hmass]; ring
 rw [he] at hh
 exact hh

end OrderRealization
#check OrderRealization.multiplication_associative
#check OrderRealization.unit_left
#check OrderRealization.unit_right
#check OrderRealization.arrows_uv
#check OrderRealization.arrows_vu
#check OrderRealization.special_fiber_uv
#check OrderRealization.special_fiber_vu
#check OrderRealization.arrow_u_squared
#check OrderRealization.arrow_v_squared
#check OrderRealization.heat_weight_sum
#check OrderRealization.heat_weight_positive
#check OrderRealization.sector_gap_expectation
#print axioms OrderRealization.multiplication_associative
#print axioms OrderRealization.unit_left
#print axioms OrderRealization.unit_right
#print axioms OrderRealization.arrows_uv
#print axioms OrderRealization.arrows_vu
#print axioms OrderRealization.special_fiber_uv
#print axioms OrderRealization.special_fiber_vu
#print axioms OrderRealization.arrow_u_squared
#print axioms OrderRealization.arrow_v_squared
#print axioms OrderRealization.heat_weight_sum
#print axioms OrderRealization.heat_weight_positive
#print axioms OrderRealization.sector_gap_expectation
