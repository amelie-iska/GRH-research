import Mathlib.Algebra.QuadraticAlgebra
import Mathlib.Algebra.MvPolynomial.CommRing
import Mathlib.RingTheory.Ideal.Quotient.Defs
import Mathlib.RingTheory.Ideal.Span
import Mathlib.LinearAlgebra.Quotient.Basic
import Mathlib.Algebra.Module.Projective
import Mathlib.Tactic.Ring

/-!
Concrete exterior-line/Koszul algebra and differential components.
The degree-zero and degree-minus-one pieces are the re and im coordinates
of QuadraticAlgebra S 0 0. The source proves differential, sign-Leibniz,
homotopy and augmentation identities and the actual nodal polynomial
underlying resolution. A categorical Z-graded DGA, completed topology and
derived-equivalence objects are not packaged by these declarations.
-/
set_option autoImplicit false
namespace GRHResearch.NodalDG
noncomputable section
variable {S : Type*} [CommRing S]
abbrev Total (S : Type*) [CommRing S] := QuadraticAlgebra S 0 0
local instance regularModule : Module S S := Semiring.toModule

def even (a : S) : Total S := ⟨a,0⟩
def odd (b : S) : Total S := ⟨0,b⟩
def sign (p : Total S) : Total S := ⟨p.re,-p.im⟩

def differential (f : S) : Total S →ₗ[S] Total S where
  toFun p := ⟨f*p.im,0⟩
  map_add' p q := by ext <;> simp [mul_add]
  map_smul' r p := by
    ext
    · change f*(r*p.im)=r*(f*p.im); ring
    · simp

def homotopy : Total S →ₗ[S] Total S where
  toFun p := ⟨0,p.re⟩
  map_add' p q := by ext <;> simp
  map_smul' r p := by ext <;> simp

theorem odd_square_product (a b : S) : odd a * odd b = 0 := by
  ext <;> simp [odd]

theorem differential_even (f a : S) : differential f (even a) = 0 := by
  ext <;> simp [differential,even]

theorem differential_odd (f b : S) : differential f (odd b) = even (f*b) := rfl

theorem differential_square_zero (f : S) : (differential f).comp (differential f) = 0 := by
  apply LinearMap.ext
  intro p
  ext <;> simp [differential]

/-- Graded Leibniz extended linearly to the two homogeneous pieces. -/
theorem sign_leibniz (f : S) (p q : Total S) :
    differential f (p*q) = differential f p*q + sign p*differential f q := by
  ext <;> simp [differential,sign,QuadraticAlgebra.re_mul,QuadraticAlgebra.im_mul] <;> ring

/-- Multiplication by the relation is explicitly chain null-homotopic. -/
theorem koszul_homotopy (f : S) (p : Total S) :
    differential f (homotopy p) + homotopy (differential f p) = f • p := by
  ext <;> simp [differential,homotopy]

/-- A unit boundary contracts the complex instead of resolving a nonzero ground field. -/
theorem unit_contracts (p : Total S) :
    differential (1:S) (homotopy p) + homotopy (differential (1:S) p) = p := by
  simpa using koszul_homotopy (1:S) p

theorem unit_cycle_boundary (p : Total S) (hp : differential (1:S) p = 0) :
    ∃ q : Total S, differential (1:S) q = p := by
  refine ⟨homotopy p, ?_⟩
  simpa [hp] using unit_contracts p

/-- Degree -1 to degree 0: actual multiplication over the ambient coefficient ring. -/
def boundary (f : S) : S →ₗ[S] S where
  toFun a := f*a
  map_add' a b := mul_add f a b
  map_smul' r a := by change f*(r*a)=r*(f*a); ring

def ideal (f : S) : Ideal S := Ideal.span {f}
abbrev Quotient (f : S) := S ⧸ ideal f

def augmentation (f : S) : S →ₗ[S] Quotient f := (ideal f).mkQ

theorem boundary_range (f : S) : LinearMap.range (boundary f) = ideal f := by
  ext z
  constructor
  · rintro ⟨a,rfl⟩
    apply Ideal.mem_span_singleton'.mpr
    exact ⟨a, mul_comm a f⟩
  · intro hz
    obtain ⟨a,ha⟩ := Ideal.mem_span_singleton'.mp hz
    exact ⟨a, by simpa [boundary,mul_comm] using ha⟩

theorem augmentation_kernel (f : S) :
    LinearMap.ker (augmentation f) = LinearMap.range (boundary f) := by
  rw [augmentation, Submodule.ker_mkQ, boundary_range]

theorem augmentation_surjective (f : S) : Function.Surjective (augmentation f) :=
  Submodule.mkQ_surjective (ideal f)

theorem boundary_injective [IsDomain S] (f : S) (hf : f ≠ 0) :
    Function.Injective (boundary f) := by
  intro a b hab
  exact mul_left_cancel₀ hf hab

/-- Projection of the exterior algebra onto its degree-zero coefficient is multiplicative. -/
def reHom : Total S →+* S where
  toFun p := p.re
  map_one' := rfl
  map_zero' := rfl
  map_add' _ _ := rfl
  map_mul' p q := by simp [QuadraticAlgebra.re_mul]

def totalAugmentation (f : S) : Total S →+* Quotient f :=
  (Ideal.Quotient.mk (ideal f)).comp reHom

theorem totalAugmentation_differential (f : S) (p : Total S) :
    totalAugmentation f (differential f p) = 0 := by
  apply Ideal.Quotient.eq_zero_iff_mem.mpr
  apply Ideal.mem_span_singleton'.mpr
  exact ⟨p.im, mul_comm p.im f⟩

/-- A coefficient automorphism lifts, with its semilinearity kept explicit. -/
def clock (e : S ≃+* S) : Total S ≃+* Total S where
  toFun p := ⟨e p.re,e p.im⟩
  invFun p := ⟨e.symm p.re,e.symm p.im⟩
  left_inv p := by ext <;> simp
  right_inv p := by ext <;> simp
  map_add' p q := by ext <;> simp
  map_mul' p q := by
    ext <;> simp [QuadraticAlgebra.re_mul,QuadraticAlgebra.im_mul]

theorem clock_semilinear (e : S ≃+* S) (r : S) (p : Total S) :
    clock e (r • p) = e r • clock e p := by
  ext <;> simp [clock]

theorem clock_commutes (e : S ≃+* S) (f : S) (hf : e f = f) (p : Total S) :
    clock e (differential f p) = differential f (clock e p) := by
  ext <;> simp [clock,differential,hf]

variable (k : Type*) [Field k]
abbrev PolynomialRing := MvPolynomial (Fin 2) k

def relation : PolynomialRing k := MvPolynomial.X 0 * MvPolynomial.X 1

theorem relation_ne_zero : relation k ≠ 0 :=
  mul_ne_zero (MvPolynomial.X_ne_zero 0) (MvPolynomial.X_ne_zero 1)

theorem nodal_boundary_injective : Function.Injective (boundary (relation k)) :=
  boundary_injective _ (relation_ne_zero k)

theorem nodal_augmentation_exact :
    LinearMap.ker (augmentation (relation k)) = LinearMap.range (boundary (relation k)) :=
  augmentation_kernel _

theorem nodal_augmentation_surjective : Function.Surjective (augmentation (relation k)) :=
  augmentation_surjective _

theorem ambient_term_projective : Module.Projective (PolynomialRing k) (PolynomialRing k) :=
  Module.Projective.of_free

#check odd_square_product
#check differential_even
#check differential_odd
#check differential_square_zero
#check sign_leibniz
#check koszul_homotopy
#check unit_contracts
#check unit_cycle_boundary
#check boundary_range
#check augmentation_kernel
#check augmentation_surjective
#check boundary_injective
#check totalAugmentation_differential
#check clock_semilinear
#check clock_commutes
#check relation_ne_zero
#check nodal_boundary_injective
#check nodal_augmentation_exact
#check nodal_augmentation_surjective
#check ambient_term_projective
#print axioms odd_square_product
#print axioms differential_even
#print axioms differential_odd
#print axioms differential_square_zero
#print axioms sign_leibniz
#print axioms koszul_homotopy
#print axioms unit_contracts
#print axioms unit_cycle_boundary
#print axioms boundary_range
#print axioms augmentation_kernel
#print axioms augmentation_surjective
#print axioms boundary_injective
#print axioms totalAugmentation_differential
#print axioms clock_semilinear
#print axioms clock_commutes
#print axioms relation_ne_zero
#print axioms nodal_boundary_injective
#print axioms nodal_augmentation_exact
#print axioms nodal_augmentation_surjective
#print axioms ambient_term_projective

end
end GRHResearch.NodalDG
