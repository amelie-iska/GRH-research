import Mathlib.Algebra.QuadraticAlgebra
import Mathlib.Algebra.Module.Projective

/-!
# The explicit periodic resolution over the dual numbers

For an arbitrary field k, R is the actual algebra QuadraticAlgebra k 0 0.
Every nonnegative resolution term is the regular R-module R, the positive
boundary maps multiply by epsilon, and the augmentation takes the real part.
The residue module k carries the R-action induced by that augmentation.

This file verifies square-zero, exactness at every positive term and at the
augmentation, surjectivity, projectivity of the terms, and vanishing of the
induced Hom_R(R,k) boundaries. It does not construct a categorical resolution
object, identify Ext groups, or assert an abstract projective-dimension theorem.
-/

namespace GRHResearch.Analytic.DualNumberResolution

variable (k : Type*) [Field k]

abbrev Ring := QuadraticAlgebra k 0 0

/-- Each nonnegative resolution term is the regular rank-one free module. -/
abbrev Term (_n : ℕ) := Ring k

/-- Use the regular module action, rather than a coordinatewise lifted action. -/
local instance regularModule : Module (Ring k) (Ring k) := Semiring.toModule

/-- The nonzero nilpotent element of the actual dual-number algebra. -/
def epsilon : Ring k := ⟨0, 1⟩

/-- Multiplication by epsilon, as a map of regular R-modules. -/
def boundary : Ring k →ₗ[Ring k] Ring k where
  toFun x := epsilon k * x
  map_add' x y := mul_add (epsilon k) x y
  map_smul' r x := by
    change epsilon k * (r * x) = r * (epsilon k * x)
    exact mul_left_comm (epsilon k) r x

/-- The constant positive-degree boundary at each homological index. -/
def differential (_n : ℕ) : Ring k →ₗ[Ring k] Ring k := boundary k

/-- The augmentation R -> k is an actual ring homomorphism. -/
def augmentation : Ring k →+* k where
  toFun x := x.re
  map_one' := rfl
  map_mul' x y := by simp [QuadraticAlgebra.re_mul]
  map_zero' := rfl
  map_add' x y := rfl

/-- The residue-module action is r • a = augmentation(r) * a. -/
local instance residueModule : Module (Ring k) k := Module.compHom k (augmentation k)

/-- The augmentation is R-linear for the specified residue-module action. -/
def augmentationLinear : Ring k →ₗ[Ring k] k :=
  Module.compHom.toLinearMap (augmentation k)

@[simp] theorem boundary_coordinates (x : Ring k) :
    boundary k x = (⟨0, x.re⟩ : Ring k) := by
  ext <;> simp [boundary, epsilon, QuadraticAlgebra.re_mul, QuadraticAlgebra.im_mul]

theorem epsilon_ne_zero : epsilon k ≠ 0 := by
  intro h
  have hi := congrArg QuadraticAlgebra.im h
  change (1 : k) = 0 at hi
  exact one_ne_zero hi

theorem epsilon_square_zero : epsilon k * epsilon k = 0 := by
  ext <;> simp [epsilon]

theorem boundary_square_zero : (boundary k).comp (boundary k) = 0 := by
  apply LinearMap.ext
  intro x
  change boundary k (boundary k x) = 0
  rw [boundary_coordinates, boundary_coordinates]
  rfl

theorem boundary_exact : LinearMap.ker (boundary k) = LinearMap.range (boundary k) := by
  ext x
  constructor
  · intro hx
    have hx0 : boundary k x = 0 := hx
    have hre : x.re = 0 := by
      have hi := congrArg QuadraticAlgebra.im hx0
      simpa [boundary_coordinates] using hi
    refine ⟨(⟨x.im, 0⟩ : Ring k), ?_⟩
    rw [boundary_coordinates]
    ext <;> simp [hre]
  · rintro ⟨y, rfl⟩
    change boundary k (boundary k y) = 0
    rw [boundary_coordinates, boundary_coordinates]
    rfl

theorem differential_exact_all_degrees (n : ℕ) :
    LinearMap.ker (differential k n) = LinearMap.range (differential k (n + 1)) :=
  boundary_exact k

theorem differential_square_zero (n : ℕ) :
    (differential k n).comp (differential k (n + 1)) = 0 :=
  boundary_square_zero k

theorem augmentation_surjective : Function.Surjective (augmentationLinear k) := by
  intro a
  exact ⟨⟨a, 0⟩, rfl⟩

theorem augmentation_exact :
    LinearMap.ker (augmentationLinear k) = LinearMap.range (differential k 0) := by
  ext x
  constructor
  · intro hx
    have hre : x.re = 0 := hx
    refine ⟨(⟨x.im, 0⟩ : Ring k), ?_⟩
    change boundary k _ = x
    rw [boundary_coordinates]
    ext <;> simp [hre]
  · rintro ⟨y, rfl⟩
    change (boundary k y).re = 0
    simp [boundary_coordinates]

theorem resolution_terms_projective (n : ℕ) :
    Module.Projective (Ring k) (Term k n) := by
  exact Module.Projective.of_free

@[simp] theorem epsilon_smul_residue (a : k) : epsilon k • a = 0 := by
  change (epsilon k).re * a = 0
  simp [epsilon]

/-- Every induced Hom boundary is zero, for actual R-linear maps to k. -/
theorem hom_boundary_zero (f : Ring k →ₗ[Ring k] k) (n : ℕ) :
    f.comp (differential k n) = 0 := by
  apply LinearMap.ext
  intro x
  change f (epsilon k * x) = 0
  rw [← smul_eq_mul, f.map_smul]
  exact epsilon_smul_residue k (f x)

/-- The Hom term has a concrete nonzero element: the augmentation. -/
theorem augmentationLinear_ne_zero : augmentationLinear k ≠ 0 := by
  intro h
  have h1 := DFunLike.congr_fun h (1 : Ring k)
  exact one_ne_zero (by simpa [augmentationLinear, augmentation] using h1)

#check epsilon_ne_zero
#check epsilon_square_zero
#check boundary_coordinates
#check boundary_square_zero
#check boundary_exact
#check differential_exact_all_degrees
#check differential_square_zero
#check augmentation_surjective
#check augmentation_exact
#check resolution_terms_projective
#check epsilon_smul_residue
#check hom_boundary_zero
#check augmentationLinear_ne_zero

#print axioms epsilon_ne_zero
#print axioms epsilon_square_zero
#print axioms boundary_coordinates
#print axioms boundary_square_zero
#print axioms boundary_exact
#print axioms differential_exact_all_degrees
#print axioms differential_square_zero
#print axioms augmentation_surjective
#print axioms augmentation_exact
#print axioms resolution_terms_projective
#print axioms epsilon_smul_residue
#print axioms hom_boundary_zero
#print axioms augmentationLinear_ne_zero

end GRHResearch.Analytic.DualNumberResolution
