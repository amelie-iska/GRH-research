import Mathlib.Algebra.MvPolynomial.CommRing
import Mathlib.Algebra.MvPolynomial.Equiv
import Mathlib.Algebra.Polynomial.Div
import Mathlib.RingTheory.Ideal.Span
import Mathlib.LinearAlgebra.Quotient.Basic
import Mathlib.LinearAlgebra.Basis.Prod
import Mathlib.Algebra.Module.Projective
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

/-!
Actual polynomial free resolution of k[x,y]/(x²,xy,y²).
The polynomial ring is the auxiliary filtration ring, not the primary dessin
algebra. This proves kernel/image equalities, not just the complex identity.
General staircases, graded minimality, CW and surface-order tensor cones are
separate interfaces; no arithmetic determinant or zero-location is asserted.
-/
set_option autoImplicit false
namespace GRHResearch.PersistenceResolution
noncomputable section

section RegularPair
variable {S : Type*} [CommRing S] [IsDomain S]

/-- Explicit syzygy generation from a nonzero x and y regular modulo x. -/
theorem relation_decomposition (x y : S) (hx : x ≠ 0)
    (hregular : ∀ z : S, x ∣ y * z → x ∣ z) (a b c : S)
    (h : x^2*a + x*y*b + y^2*c = 0) :
    ∃ p q : S, a = -y*p ∧ b = x*p-y*q ∧ c = x*q := by
  have hdiv : x ∣ y * (y*c) := by
    refine ⟨-(x*a+y*b), ?_⟩
    linear_combination h
  obtain ⟨q, hq⟩ := hregular c (hregular (y*c) hdiv)
  have hcancel : x * (x*a+y*b+y^2*q) = 0 := by
    rw [hq] at h
    linear_combination h
  have he : x*a+y*b+y^2*q = 0 := (mul_eq_zero.mp hcancel).resolve_left hx
  have hbdiv : x ∣ y * (b+y*q) := by
    refine ⟨-a, ?_⟩
    linear_combination he
  obtain ⟨p, hp⟩ := hregular (b+y*q) hbdiv
  have ha : x * (a+y*p) = 0 := by
    linear_combination he - y*hp
  refine ⟨p, q, ?_, ?_, hq⟩
  · have hh := (mul_eq_zero.mp ha).resolve_left hx
    linear_combination hh
  · linear_combination hp
end RegularPair

variable (k : Type*) [Field k]
abbrev Ring := MvPolynomial (Fin 2) k
/-- Fix multiplication on regular modules, even after the residue action is introduced. -/
local instance regularModule : Module (Ring k) (Ring k) := Semiring.toModule

abbrev F1 := Ring k × Ring k × Ring k
abbrev F2 := Ring k × Ring k

def x : Ring k := MvPolynomial.X 0
def y : Ring k := MvPolynomial.X 1

theorem x_ne_zero : x k ≠ 0 := MvPolynomial.X_ne_zero 0
theorem y_ne_zero : y k ≠ 0 := MvPolynomial.X_ne_zero 1

/-- Y is a non-zero-divisor modulo (X), proved via actual polynomial coefficients. -/
theorem x_dvd_of_y_mul (z : Ring k) (h : x k ∣ y k * z) : x k ∣ z := by
  let e := MvPolynomial.finSuccEquiv k 1
  have ex : e (x k) = Polynomial.X := MvPolynomial.finSuccEquiv_X_zero
  have ey : e (y k) = Polynomial.C (MvPolynomial.X (0 : Fin 1)) :=
    MvPolynomial.finSuccEquiv_X_succ (R := k) (j := (0 : Fin 1))
  have hm : (Polynomial.X : Polynomial (MvPolynomial (Fin 1) k)) ∣
      Polynomial.C (MvPolynomial.X (0 : Fin 1)) * e z := by
    obtain ⟨q, hq⟩ := h
    refine ⟨e q, ?_⟩
    simpa only [map_mul, ex, ey] using congrArg e hq
  have hz : (e z).coeff 0 = 0 := by
    have heq := Polynomial.X_dvd_iff.mp hm
    simp only [Polynomial.coeff_C_mul] at heq
    exact (mul_eq_zero.mp heq).resolve_left (MvPolynomial.X_ne_zero 0)
  obtain ⟨q, hq⟩ := Polynomial.X_dvd_iff.mpr hz
  refine ⟨e.symm q, ?_⟩
  apply e.injective
  simpa only [map_mul, ex, e.apply_symm_apply] using hq

/-- Rows are the actual generators x²,xy,y² of the auxiliary ideal. -/
def d1 : F1 k →ₗ[Ring k] Ring k where
  toFun v := x k^2*v.1 + x k*y k*v.2.1 + y k^2*v.2.2
  map_add' a b := by dsimp; ring
  map_smul' r v := by
    change x k^2*(r*v.1)+x k*y k*(r*v.2.1)+y k^2*(r*v.2.2) =
      r*(x k^2*v.1+x k*y k*v.2.1+y k^2*v.2.2)
    ring

/-- Columns (-y,x,0) and (0,-y,x); products carry the genuine R-action. -/
def d2 : F2 k →ₗ[Ring k] F1 k where
  toFun v := (-y k*v.1, x k*v.1-y k*v.2, x k*v.2)
  map_add' a b := by
    apply Prod.ext
    · dsimp; ring
    · apply Prod.ext <;> dsimp <;> ring
  map_smul' r v := by
    apply Prod.ext
    · change -y k*(r*v.1)=r*(-y k*v.1); ring
    · apply Prod.ext
      · change x k*(r*v.1)-y k*(r*v.2)=r*(x k*v.1-y k*v.2); ring
      · change x k*(r*v.2)=r*(x k*v.2); ring

theorem complex_identity : (d1 k).comp (d2 k) = 0 := by
  apply LinearMap.ext
  intro v
  change x k^2*(-y k*v.1)+x k*y k*(x k*v.1-y k*v.2)+y k^2*(x k*v.2)=0
  ring

theorem d2_injective : Function.Injective (d2 k) := by
  apply (LinearMap.ker_eq_bot).mp
  apply eq_bot_iff.mpr
  intro v hv
  change v = 0
  have h0 : d2 k v = 0 := hv
  have hp : v.1 = 0 := by
    have hfirst := congrArg Prod.fst h0
    change -y k*v.1=0 at hfirst
    exact (mul_eq_zero.mp hfirst).resolve_left (neg_ne_zero.mpr (y_ne_zero k))
  have hq : v.2 = 0 := by
    have hlast := congrArg (fun w : F1 k => w.2.2) h0
    change x k*v.2=0 at hlast
    exact (mul_eq_zero.mp hlast).resolve_left (x_ne_zero k)
  exact Prod.ext hp hq

/-- Nontrivial exactness: every polynomial relation comes from the two columns. -/
theorem d1_kernel : LinearMap.ker (d1 k) = LinearMap.range (d2 k) := by
  ext v
  constructor
  · intro hv
    obtain ⟨p,q,ha,hb,hc⟩ := relation_decomposition (x k) (y k) (x_ne_zero k)
      (x_dvd_of_y_mul k) v.1 v.2.1 v.2.2 hv
    exact ⟨(p,q), Prod.ext ha.symm (Prod.ext hb.symm hc.symm)⟩
  · rintro ⟨v,rfl⟩
    have h := DFunLike.congr_fun (complex_identity k) v
    exact h

/-- This ideal is an actual Submodule R R, not a finite scalar matrix carrier. -/
def ideal : Ideal (Ring k) := Ideal.span {x k^2, x k*y k, y k^2}

/-- The presentation image equals the stated ideal, including all coefficients. -/
theorem d1_range : LinearMap.range (d1 k) = ideal k := by
  apply le_antisymm
  · rintro z ⟨v,rfl⟩
    have h0 : x k^2 ∈ ideal k := Ideal.subset_span (by simp)
    have h1 : x k*y k ∈ ideal k := Ideal.subset_span (by simp)
    have h2 : y k^2 ∈ ideal k := Ideal.subset_span (by simp)
    have H := (ideal k).add_mem ((ideal k).add_mem
      ((ideal k).smul_mem v.1 h0) ((ideal k).smul_mem v.2.1 h1))
      ((ideal k).smul_mem v.2.2 h2)
    simpa only [d1, LinearMap.coe_mk, AddHom.coe_mk, smul_eq_mul, mul_comm] using H
  · apply Ideal.span_le.mpr
    intro z hz
    simp only [Set.mem_insert_iff, Set.mem_singleton_iff] at hz
    rcases hz with rfl | rfl | rfl
    · exact ⟨(1,0,0), by simp [d1]⟩
    · exact ⟨(0,1,0), by simp [d1]⟩
    · exact ⟨(0,0,1), by simp [d1]⟩

abbrev ModuleQuotient := Ring k ⧸ ideal k

def augmentation : Ring k →ₗ[Ring k] ModuleQuotient k := (ideal k).mkQ

theorem augmentation_surjective : Function.Surjective (augmentation k) :=
  Submodule.mkQ_surjective (ideal k)

theorem augmentation_kernel :
    LinearMap.ker (augmentation k) = LinearMap.range (d1 k) := by
  rw [augmentation, Submodule.ker_mkQ, d1_range]

theorem free_terms_projective :
    Module.Projective (Ring k) (Ring k) ∧ Module.Projective (Ring k) (F1 k) ∧
      Module.Projective (Ring k) (F2 k) := by
  exact ⟨Module.Projective.of_free, Module.Projective.of_free, Module.Projective.of_free⟩

/-- The residue field has the actual R-action induced by constant coefficient. -/
local instance residueModule : Module (Ring k) k :=
  Module.compHom k (MvPolynomial.constantCoeff : Ring k →+* k)

/-- Explicit action contracts guard the regular/residue instance boundary. -/
theorem regular_action (r q : Ring k) : r • q = r*q := rfl

theorem residue_action (r : Ring k) (a : k) :
    r • a = MvPolynomial.constantCoeff r * a := rfl

theorem residue_x_smul (a : k) : x k • a = 0 := by
  change MvPolynomial.constantCoeff (x k) * a = 0
  simp [x]

theorem residue_y_smul (a : k) : y k • a = 0 := by
  change MvPolynomial.constantCoeff (y k) * a = 0
  simp [y]

theorem hom_x_smul_zero {N : Type*} [AddCommMonoid N] [Module (Ring k) N]
    (f : N →ₗ[Ring k] k) (v : N) : f (x k • v) = 0 := by
  rw [f.map_smul, residue_x_smul]

theorem hom_y_smul_zero {N : Type*} [AddCommMonoid N] [Module (Ring k) N]
    (f : N →ₗ[Ring k] k) (v : N) : f (y k • v) = 0 := by
  rw [f.map_smul, residue_y_smul]

/-- The induced Hom differential really vanishes for every R-linear map. -/
theorem hom_d1_zero (f : Ring k →ₗ[Ring k] k) : (f ∘ₗ d1 k) = 0 := by
  apply LinearMap.ext
  intro v
  have h : d1 k v = x k • (x k*v.1+y k*v.2.1)+y k • (y k*v.2.2) := by
    change x k^2*v.1+x k*y k*v.2.1+y k^2*v.2.2 =
      x k*(x k*v.1+y k*v.2.1)+y k*(y k*v.2.2)
    ring
  change f (d1 k v) = 0
  rw [h, f.map_add, hom_x_smul_zero k f, hom_y_smul_zero k f, add_zero]

/-- The higher induced Hom differential uses the same constant-coefficient action. -/
theorem hom_d2_zero (f : F1 k →ₗ[Ring k] k) : (f ∘ₗ d2 k) = 0 := by
  apply LinearMap.ext
  intro v
  have h : d2 k v = x k • (0,v.1,v.2)+y k • (-v.1,-v.2,0) := by
    apply Prod.ext
    · change -y k*v.1=x k*0+y k*(-v.1); ring
    · apply Prod.ext
      · change x k*v.1-y k*v.2=x k*v.1+y k*(-v.2); ring
      · change x k*v.2=x k*v.2+y k*0; ring
  change f (d2 k v) = 0
  rw [h, f.map_add, hom_x_smul_zero k f, hom_y_smul_zero k f, add_zero]

#check x_ne_zero
#check y_ne_zero
#check regular_action
#check residue_action
#check residue_x_smul
#check residue_y_smul
#check hom_x_smul_zero
#check hom_y_smul_zero
#check hom_d1_zero
#check hom_d2_zero
#check relation_decomposition
#check x_dvd_of_y_mul
#check complex_identity
#check d2_injective
#check d1_kernel
#check d1_range
#check augmentation_surjective
#check augmentation_kernel
#check free_terms_projective
#print axioms x_ne_zero
#print axioms y_ne_zero
#print axioms regular_action
#print axioms residue_action
#print axioms residue_x_smul
#print axioms residue_y_smul
#print axioms hom_x_smul_zero
#print axioms hom_y_smul_zero
#print axioms hom_d1_zero
#print axioms hom_d2_zero
#print axioms relation_decomposition
#print axioms x_dvd_of_y_mul
#print axioms complex_identity
#print axioms d2_injective
#print axioms d1_kernel
#print axioms d1_range
#print axioms augmentation_surjective
#print axioms augmentation_kernel
#print axioms free_terms_projective
end
end GRHResearch.PersistenceResolution
