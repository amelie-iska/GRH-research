import Mathlib.RingTheory.PowerSeries.Basic
import Mathlib.Algebra.Ring.Subring.Basic
import Mathlib.Algebra.Module.Projective
import Mathlib.LinearAlgebra.Basis.Prod
import Mathlib.Tactic.Ring

/-!
The actual completed order of the clean sphere dessin beta=4z(1-z):
the fiber product k[[X]] x_k k[[X]]. No finite-dimensional algebra replaces it.
-/
namespace GRHResearch.DessinNode
noncomputable section
open PowerSeries
variable (k : Type*) [Field k]

/-- Pairs of formal branch series with equal residue constants. -/
def orderSubring : Subring (PowerSeries k × PowerSeries k) where
  carrier := {p | constantCoeff p.1 = constantCoeff p.2}
  zero_mem' := by simp
  one_mem' := by simp
  add_mem' := by
    intro a b ha hb
    change constantCoeff a.1=constantCoeff a.2 at ha
    change constantCoeff b.1=constantCoeff b.2 at hb
    change constantCoeff (a.1+b.1) = constantCoeff (a.2+b.2)
    simp only [map_add, ha, hb]
  mul_mem' := by
    intro a b ha hb
    change constantCoeff a.1=constantCoeff a.2 at ha
    change constantCoeff b.1=constantCoeff b.2 at hb
    change constantCoeff (a.1*b.1) = constantCoeff (a.2*b.2)
    simp only [map_mul, ha, hb]
  neg_mem' := by
    intro a ha
    change constantCoeff a.1=constantCoeff a.2 at ha
    change constantCoeff (-a.1) = constantCoeff (-a.2)
    simp only [map_neg, ha]

abbrev Order := orderSubring k
local instance regularModule : Module (Order k) (Order k) := Semiring.toModule

def x : Order k := ⟨(X,0), by simp [orderSubring]⟩
def y : Order k := ⟨(0,X), by simp [orderSubring]⟩
def parameter : Order k := x k+y k

def diagonal : PowerSeries k →+* Order k where
  toFun f := ⟨(f,f), rfl⟩
  map_one' := rfl
  map_mul' _ _ := rfl
  map_zero' := rfl
  map_add' _ _ := rfl

theorem diagonal_injective : Function.Injective (diagonal k) := by
  intro a b h
  exact congrArg (fun z : Order k => z.val.1) h

theorem x_ne_zero : x k ≠ 0 := by
  intro h
  have heq := congrArg (fun z : Order k => z.val.1) h
  exact (PowerSeries.X_ne_zero (R := k)) heq

theorem y_ne_zero : y k ≠ 0 := by
  intro h
  have heq := congrArg (fun z : Order k => z.val.2) h
  exact (PowerSeries.X_ne_zero (R := k)) heq

theorem xy_zero : x k*y k=0 := by
  apply Subtype.ext
  exact Prod.ext (by simp [x,y]) (by simp [x,y])

theorem yx_zero : y k*x k=0 := by rw [mul_comm, xy_zero]

/-- Factor a formal series along the y branch, inside the actual glued order. -/
theorem first_branch_zero_factor (z : Order k) (hz : z.val.1=0) :
    ∃ w : Order k, y k*w=z := by
  have hc : constantCoeff z.val.2=0 := by
    have h := z.property
    change constantCoeff z.val.1=constantCoeff z.val.2 at h
    rw [hz, map_zero] at h
    exact h.symm
  obtain ⟨f,hf⟩ := PowerSeries.X_dvd_iff.mpr hc
  let w : Order k := ⟨(C (constantCoeff f),f), by simp [orderSubring]⟩
  refine ⟨w, ?_⟩
  apply Subtype.ext
  apply Prod.ext
  · simpa [y,w] using hz.symm
  · change X*f=z.val.2
    exact hf.symm

theorem second_branch_zero_factor (z : Order k) (hz : z.val.2=0) :
    ∃ w : Order k, x k*w=z := by
  have hc : constantCoeff z.val.1=0 := by
    have h := z.property
    change constantCoeff z.val.1=constantCoeff z.val.2 at h
    rw [hz, map_zero] at h
    exact h
  obtain ⟨f,hf⟩ := PowerSeries.X_dvd_iff.mpr hc
  let w : Order k := ⟨(f,C (constantCoeff f)), by simp [orderSubring]⟩
  refine ⟨w, ?_⟩
  apply Subtype.ext
  apply Prod.ext
  · change X*f=z.val.1
    exact hf.symm
  · simpa [x,w] using hz.symm

theorem ann_x_is_y (z : Order k) : x k*z=0 ↔ ∃w, y k*w=z := by
  constructor
  · intro h
    have hf := congrArg (fun z : Order k => z.val.1) h
    have hz : z.val.1=0 := PowerSeries.X_mul_cancel (by simpa [x] using hf)
    exact first_branch_zero_factor k z hz
  · rintro ⟨w,rfl⟩
    rw [← mul_assoc,xy_zero,zero_mul]

theorem ann_y_is_x (z : Order k) : y k*z=0 ↔ ∃w, x k*w=z := by
  constructor
  · intro h
    have hf := congrArg (fun z : Order k => z.val.2) h
    have hz : z.val.2=0 := PowerSeries.X_mul_cancel (by simpa [y] using hf)
    exact second_branch_zero_factor k z hz
  · rintro ⟨w,rfl⟩
    rw [← mul_assoc,yx_zero,zero_mul]

theorem parameter_regular (z : Order k) : parameter k*z=0 ↔ z=0 := by
  constructor
  · intro h
    apply Subtype.ext
    apply Prod.ext
    · have hf := congrArg (fun z : Order k => z.val.1) h
      exact PowerSeries.X_mul_cancel (by simpa [parameter,x,y] using hf)
    · have hf := congrArg (fun z : Order k => z.val.2) h
      exact PowerSeries.X_mul_cancel (by simpa [parameter,x,y] using hf)
  · rintro rfl; simp

/-- Right-linear first row of the actual completed-node simple resolution. -/
def firstBoundary : (Order k × Order k) →ₗ[Order k] Order k where
  toFun z := x k*z.1+y k*z.2
  map_add' z w := by
    change x k*(z.1+w.1)+y k*(z.2+w.2)=(x k*z.1+y k*z.2)+(x k*w.1+y k*w.2)
    ring
  map_smul' r z := by change x k*(r*z.1)+y k*(r*z.2)=r*(x k*z.1+y k*z.2); ring

def evenBoundary : (Order k × Order k) →ₗ[Order k] (Order k × Order k) where
  toFun z := (y k*z.1,x k*z.2)
  map_add' z w := by ext <;> simp [mul_add]
  map_smul' r z := by
    apply Prod.ext
    · change y k*(r*z.1)=r*(y k*z.1); ring
    · change x k*(r*z.2)=r*(x k*z.2); ring

def oddBoundary : (Order k × Order k) →ₗ[Order k] (Order k × Order k) where
  toFun z := (x k*z.1,y k*z.2)
  map_add' z w := by ext <;> simp [mul_add]
  map_smul' r z := by
    apply Prod.ext
    · change x k*(r*z.1)=r*(x k*z.1); ring
    · change y k*(r*z.2)=r*(y k*z.2); ring

theorem first_boundary_square_zero :
    (firstBoundary k).comp (evenBoundary k)=0 := by
  apply LinearMap.ext
  intro z
  change x k*(y k*z.1)+y k*(x k*z.2)=0
  rw [← mul_assoc,xy_zero,zero_mul,← mul_assoc,yx_zero,zero_mul,add_zero]

theorem alternating_boundaries_square_zero :
    (evenBoundary k).comp (oddBoundary k)=0 ∧
    (oddBoundary k).comp (evenBoundary k)=0 := by
  constructor
  · apply LinearMap.ext
    intro z
    apply Prod.ext
    · change y k*(x k*z.1)=0
      rw [← mul_assoc,yx_zero,zero_mul]
    · change x k*(y k*z.2)=0
      rw [← mul_assoc,xy_zero,zero_mul]
  · apply LinearMap.ext
    intro z
    apply Prod.ext
    · change x k*(y k*z.1)=0
      rw [← mul_assoc,xy_zero,zero_mul]
    · change y k*(x k*z.2)=0
      rw [← mul_assoc,yx_zero,zero_mul]

theorem first_boundary_exact :
    LinearMap.ker (firstBoundary k)=LinearMap.range (evenBoundary k) := by
  ext z
  constructor
  · intro hz
    have heq : firstBoundary k z=0 := hz
    have hx : x k*z.1=0 := by
      apply Subtype.ext
      apply Prod.ext
      · have h:=congrArg (fun w : Order k => w.val.1) heq
        simpa [firstBoundary,x,y] using h
      · simp [x]
    have hy : y k*z.2=0 := by
      apply Subtype.ext
      apply Prod.ext
      · simp [y]
      · have h:=congrArg (fun w : Order k => w.val.2) heq
        simpa [firstBoundary,x,y] using h
    obtain ⟨a,ha⟩ := (ann_x_is_y k z.1).mp hx
    obtain ⟨b,hb⟩ := (ann_y_is_x k z.2).mp hy
    exact ⟨(a,b),Prod.ext ha hb⟩
  · rintro ⟨w,rfl⟩
    change firstBoundary k (evenBoundary k w)=0
    exact DFunLike.congr_fun (first_boundary_square_zero k) w

theorem even_boundary_exact :
    LinearMap.ker (evenBoundary k)=LinearMap.range (oddBoundary k) := by
  ext z
  constructor
  · intro hz
    have heq : evenBoundary k z=0 := hz
    have hy : y k*z.1=0 := congrArg Prod.fst heq
    have hx : x k*z.2=0 := congrArg Prod.snd heq
    obtain ⟨a,ha⟩ := (ann_y_is_x k z.1).mp hy
    obtain ⟨b,hb⟩ := (ann_x_is_y k z.2).mp hx
    exact ⟨(a,b),Prod.ext ha hb⟩
  · rintro ⟨w,rfl⟩
    change evenBoundary k (oddBoundary k w)=0
    exact DFunLike.congr_fun (alternating_boundaries_square_zero k).1 w

theorem odd_boundary_exact :
    LinearMap.ker (oddBoundary k)=LinearMap.range (evenBoundary k) := by
  ext z
  constructor
  · intro hz
    have heq : oddBoundary k z=0 := hz
    have hx : x k*z.1=0 := congrArg Prod.fst heq
    have hy : y k*z.2=0 := congrArg Prod.snd heq
    obtain ⟨a,ha⟩ := (ann_x_is_y k z.1).mp hx
    obtain ⟨b,hb⟩ := (ann_y_is_x k z.2).mp hy
    exact ⟨(a,b),Prod.ext ha hb⟩
  · rintro ⟨w,rfl⟩
    change oddBoundary k (evenBoundary k w)=0
    exact DFunLike.congr_fun (alternating_boundaries_square_zero k).2 w

theorem resolution_terms_projective :
    Module.Projective (Order k) (Order k) ∧
    Module.Projective (Order k) (Order k × Order k) := by
  exact ⟨Module.Projective.of_free,Module.Projective.of_free⟩

/-- The common DVR parameter is the diagonal formal variable. -/
theorem parameter_diagonal : parameter k=diagonal k X := by
  apply Subtype.ext
  exact Prod.ext (by simp [parameter,x,y,diagonal]) (by simp [parameter,x,y,diagonal])

def augmentation : Order k →+* k where
  toFun z := constantCoeff z.val.1
  map_one' := by simp
  map_mul' z w := by change constantCoeff (z.val.1*w.val.1)=_; rw [map_mul]
  map_zero' := by simp
  map_add' z w := by change constantCoeff (z.val.1+w.val.1)=_; rw [map_add]

local instance residueModule : Module (Order k) k := Module.compHom k (augmentation k)

def augmentationLinear : Order k →ₗ[Order k] k := Module.compHom.toLinearMap (augmentation k)

theorem augmentation_surjective : Function.Surjective (augmentationLinear k) := by
  intro a
  refine ⟨diagonal k (C a), ?_⟩
  change constantCoeff (C a)=a
  exact constantCoeff_C a

theorem augmentation_exact :
    LinearMap.ker (augmentationLinear k)=LinearMap.range (firstBoundary k) := by
  ext z
  constructor
  · intro hz
    have hc1 : constantCoeff z.val.1=0 := hz
    have hc2 : constantCoeff z.val.2=0 := by
      have h:=z.property
      change constantCoeff z.val.1=constantCoeff z.val.2 at h
      exact h.symm.trans hc1
    let p : Order k := ⟨(z.val.1,0),by simpa [orderSubring] using hc1⟩
    let q : Order k := ⟨(0,z.val.2),by simpa [orderSubring] using hc2.symm⟩
    obtain ⟨a,ha⟩ := second_branch_zero_factor k p rfl
    obtain ⟨b,hb⟩ := first_branch_zero_factor k q rfl
    refine ⟨(a,b), ?_⟩
    change x k*a+y k*b=z
    rw [ha,hb]
    apply Subtype.ext
    exact Prod.ext (by simp [p,q]) (by simp [p,q])
  · rintro ⟨w,rfl⟩
    change constantCoeff ((x k*w.1+y k*w.2).val.1)=0
    simp [x,y]

/-- Every element has unique coordinates a+b*x over the diagonal power-series ring. -/
theorem common_dvr_coordinates : Function.Bijective
    (fun ab : PowerSeries k × PowerSeries k => diagonal k ab.1+diagonal k ab.2*x k) := by
  constructor
  · intro a b h
    have hs := congrArg (fun z : Order k => z.val.2) h
    have ha : a.1=b.1 := by simpa [diagonal,x] using hs
    have hf := congrArg (fun z : Order k => z.val.1) h
    have hmul : X*a.2=X*b.2 := by
      have hsum : a.1+a.2*X=b.1+b.2*X := hf
      rw [ha] at hsum
      have hc := add_left_cancel hsum
      simpa [mul_comm] using hc
    exact Prod.ext ha (PowerSeries.X_mul_cancel hmul)
  · intro z
    have hc : constantCoeff (z.val.1-z.val.2)=0 := by
      have h:=z.property
      change constantCoeff z.val.1=constantCoeff z.val.2 at h
      simp only [map_sub,h,sub_self]
    obtain ⟨b,hb⟩ := PowerSeries.X_dvd_iff.mpr hc
    refine ⟨(z.val.2,b), ?_⟩
    apply Subtype.ext
    apply Prod.ext
    · change z.val.2+b*X=z.val.1
      rw [mul_comm,← hb]
      exact add_sub_cancel _ _
    · simp [diagonal,x]

#check parameter_diagonal
#check augmentation_surjective
#check augmentation_exact
#check common_dvr_coordinates
#check first_boundary_square_zero
#check alternating_boundaries_square_zero
#check first_boundary_exact
#check even_boundary_exact
#check odd_boundary_exact
#check resolution_terms_projective
#check diagonal_injective
#check x_ne_zero
#check y_ne_zero
#check xy_zero
#check yx_zero
#check first_branch_zero_factor
#check second_branch_zero_factor
#check ann_x_is_y
#check ann_y_is_x
#check parameter_regular
#print axioms parameter_diagonal
#print axioms augmentation_surjective
#print axioms augmentation_exact
#print axioms common_dvr_coordinates
#print axioms first_boundary_square_zero
#print axioms alternating_boundaries_square_zero
#print axioms first_boundary_exact
#print axioms even_boundary_exact
#print axioms odd_boundary_exact
#print axioms resolution_terms_projective
#print axioms diagonal_injective
#print axioms x_ne_zero
#print axioms y_ne_zero
#print axioms xy_zero
#print axioms yx_zero
#print axioms first_branch_zero_factor
#print axioms second_branch_zero_factor
#print axioms ann_x_is_y
#print axioms ann_y_is_x
#print axioms parameter_regular
end
end GRHResearch.DessinNode
