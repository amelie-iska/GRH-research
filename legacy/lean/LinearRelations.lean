import Mathlib.LinearAlgebra.Prod
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.Algebra.GroupWithZero.Action.Units

/-! Actual submodule relations and finite-length Fitting decomposition.
These are not the whole infinite string classification or a completed-order
equivalence. Morphism hypotheses are explicit semiconjugacy identities. -/
set_option autoImplicit false
namespace GRHResearch.LinearRelations
noncomputable section
variable {R V W : Type*} [CommRing R] [AddCommGroup V] [Module R V]
  [AddCommGroup W] [Module R W]

def inverse (C : Submodule R (V × V)) : Submodule R (V × V) where
  carrier := {p | (p.2,p.1) ∈ C}
  zero_mem' := C.zero_mem
  add_mem' h h' := C.add_mem h h'
  smul_mem' r _ h := C.smul_mem r h

def compose (D C : Submodule R (V × V)) : Submodule R (V × V) where
  carrier := {p | ∃ y, (p.1,y) ∈ C ∧ (y,p.2) ∈ D}
  zero_mem' := ⟨0,C.zero_mem,D.zero_mem⟩
  add_mem' := by
    rintro a b ⟨y,hy,hy'⟩ ⟨z,hz,hz'⟩
    exact ⟨y+z,C.add_mem hy hz,D.add_mem hy' hz'⟩
  smul_mem' := by
    rintro r p ⟨y,hy,hy'⟩
    exact ⟨r • y,C.smul_mem r hy,D.smul_mem r hy'⟩

theorem graph_zero_output (f : V →ₗ[R] V) (x : V) :
    (x,0) ∈ f.graph ↔ x ∈ LinearMap.ker f := by
  simp [LinearMap.mem_graph_iff,eq_comm]

theorem graph_zero_input (f : V →ₗ[R] V) (y : V) :
    (0,y) ∈ f.graph ↔ y = 0 := by
  simp [LinearMap.mem_graph_iff]

theorem inverse_graph_zero_input (f : V →ₗ[R] V) (y : V) :
    (0,y) ∈ inverse f.graph ↔ y ∈ LinearMap.ker f := by
  exact graph_zero_output f y

theorem graph_composition (f g : V →ₗ[R] V) :
    compose g.graph f.graph = (g.comp f).graph := by
  ext p
  simp only [compose, Submodule.mem_mk,
    LinearMap.mem_graph_iff, LinearMap.comp_apply]
  constructor
  · rintro ⟨y,hy,hy'⟩
    simpa [← hy] using hy'
  · intro h
    exact ⟨f p.1,rfl,h⟩

theorem inverse_involution (C : Submodule R (V × V)) :
    inverse (inverse C) = C := by ext p; rfl

theorem intertwine_power (f : V →ₗ[R] V) (g : W →ₗ[R] W)
    (h : V →ₗ[R] W) (hc : h.comp f = g.comp h) (n : ℕ) (x : V) :
    h ((f ^ n) x) = (g ^ n) (h x) := by
  induction n with
  | zero => rfl
  | succ n ih =>
    have hh (v : V) : h (f v) = g (h v) := LinearMap.congr_fun hc v
    simp only [pow_succ', Module.End.mul_apply]
    rw [hh, ih]

theorem kernel_filtration_functorial (f : V →ₗ[R] V) (g : W →ₗ[R] W)
    (h : V →ₗ[R] W) (hc : h.comp f = g.comp h) (n : ℕ)
    {x : V} (hx : x ∈ LinearMap.ker (f ^ n)) :
    h x ∈ LinearMap.ker (g ^ n) := by
  change (g ^ n) (h x) = 0
  rw [← intertwine_power f g h hc n x]
  simpa using congrArg h hx

theorem image_filtration_functorial (f : V →ₗ[R] V) (g : W →ₗ[R] W)
    (h : V →ₗ[R] W) (hc : h.comp f = g.comp h) (n : ℕ)
    {x : V} (hx : x ∈ LinearMap.range (f ^ n)) :
    h x ∈ LinearMap.range (g ^ n) := by
  obtain ⟨y,rfl⟩ := hx
  exact ⟨h y,(intertwine_power f g h hc n y).symm⟩

theorem finite_kernel_stabilizes {K : Type*} [Field K] [Module K V]
    [FiniteDimensional K V] (f : V →ₗ[K] V) (n : ℕ)
    (hn : Module.finrank K V ≤ n) :
    LinearMap.ker (f ^ n) = LinearMap.ker (f ^ Module.finrank K V) :=
  Module.End.ker_pow_eq_ker_pow_finrank_of_le hn

theorem finite_dimensional_fitting {K : Type*} [Field K] [Module K V]
    [FiniteDimensional K V] (f : V →ₗ[K] V) :
    IsCompl (LinearMap.ker (f ^ Module.finrank K V))
      (LinearMap.range (f ^ Module.finrank K V)) := by
  let n := Module.finrank K V
  have hk : LinearMap.ker (f ^ (n+n)) = LinearMap.ker (f ^ n) :=
    Module.End.ker_pow_eq_ker_pow_finrank_of_le (Nat.le_add_right n n)
  have hd : Disjoint (LinearMap.ker (f ^ n)) (LinearMap.range (f ^ n)) := by
    apply Submodule.disjoint_def.mpr
    rintro x hx ⟨y,rfl⟩
    have hy : y ∈ LinearMap.ker (f ^ (n+n)) := by
      change (f ^ (n+n)) y = 0
      simpa only [pow_add,Module.End.mul_apply] using hx
    rw [hk] at hy
    exact hy
  apply (Submodule.isCompl_iff_disjoint _ _ ?_).mpr hd
  simpa only [add_comm] using (f ^ n).finrank_range_add_finrank_ker.symm.le

theorem unit_power_annihilation (a : R) (ha : IsUnit a) (n : ℕ) (x : V)
    (hx : a ^ n • x = 0) : x = 0 :=
  (ha.pow n).smul_eq_zero.mp hx

#check graph_zero_output
#check graph_zero_input
#check inverse_graph_zero_input
#check graph_composition
#check inverse_involution
#check intertwine_power
#check kernel_filtration_functorial
#check image_filtration_functorial
#check finite_kernel_stabilizes
#check finite_dimensional_fitting
#check unit_power_annihilation
#print axioms graph_zero_output
#print axioms graph_zero_input
#print axioms inverse_graph_zero_input
#print axioms graph_composition
#print axioms inverse_involution
#print axioms intertwine_power
#print axioms kernel_filtration_functorial
#print axioms image_filtration_functorial
#print axioms finite_kernel_stabilizes
#print axioms finite_dimensional_fitting
#print axioms unit_power_annihilation
end
end GRHResearch.LinearRelations
