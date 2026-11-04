import Mathlib.LinearAlgebra.LinearIndependent.Basic
import Mathlib.Algebra.QuadraticAlgebra
import Mathlib.Algebra.Algebra.Subalgebra.Lattice
import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.RingTheory.Polynomial.Basic
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Ring

/-! Actual infinite polynomial dessin algebra and a nonsplit module extension.
The algebra is the generated polynomial matrix-pair realization of the
genus-two clean dessin. The path-normal-form identification is separate prose.
Its module actions below are on all elements of this algebra, not sampled
generator matrices or an assumed representation predicate. -/
set_option autoImplicit false
namespace GRHResearch.BranchExtension
noncomputable section
open Polynomial Matrix
variable (k : Type*) [Field k]
abbrev Vertex := Fin 5
abbrev Mat (R : Type*) := Matrix Vertex Vertex R
abbrev P := Polynomial k
abbrev D := QuadraticAlgebra k 0 0

def previous (i : Vertex) : Vertex := ![4,0,1,2,3] i
def edge {R : Type*} [Ring R] (z : R) (i : Vertex) : Mat R :=
  Matrix.single (previous i) i (if i=0 then z else 1)

inductive Gen where
  | vertex : Vertex → Gen
  | a : Vertex → Gen
  | b : Vertex → Gen

def rawGenerator : Gen → Mat (P k) × Mat (P k)
  | .vertex i => (Matrix.single i i 1,Matrix.single i i 1)
  | .a i => (edge (X : P k) i,0)
  | .b i => (0,edge (X : P k) i)

def surface : Subalgebra k (Mat (P k) × Mat (P k)) :=
  Algebra.adjoin k (Set.range (rawGenerator k))
def A : Type _ := ↥(surface k)
instance : Ring (A k) := inferInstanceAs (Ring ↥(surface k))
instance : Algebra k (A k) := inferInstanceAs (Algebra k ↥(surface k))

def generator (g : Gen) : A k :=
  ⟨rawGenerator k g,Algebra.subset_adjoin ⟨g,rfl⟩⟩

def view : A k →ₐ[k] Mat (P k) × Mat (P k) := (surface k).val

theorem view_injective : Function.Injective (view k) := by
  intro a b h
  exact Subtype.ext h

@[simp] theorem view_generator (g : Gen) : view k (generator k g)=rawGenerator k g := rfl

def first : A k →+* Mat (P k) :=
  (RingHom.fst _ _).comp (surface k).val.toRingHom

def firstAlg : A k →ₐ[k] Mat (P k) where
  toRingHom := first k
  commutes' _ := rfl

@[simp] theorem first_generator (g : Gen) : first k (generator k g)=(rawGenerator k g).1 := rfl

theorem mixed_products_zero (i j : Vertex) :
    generator k (.a i)*generator k (.b j)=0 ∧
    generator k (.b j)*generator k (.a i)=0 := by
  constructor <;> apply view_injective k
  all_goals simp [rawGenerator]

theorem sum_vertices : (∑ i : Vertex, generator k (.vertex i))=1 := by
  apply view_injective k
  rw [map_sum,map_one]
  apply Prod.ext
  all_goals
    simp only [Prod.fst_sum,Prod.snd_sum,view_generator,rawGenerator]
    funext i j
    simp [Matrix.sum_apply,Matrix.single,Matrix.one_apply,ite_and]

def loop : A k := generator k (.a 1)*generator k (.a 2)*
  generator k (.a 3)*generator k (.a 4)*generator k (.a 0)

theorem loop_first : first k (loop k)=Matrix.single 0 0 (X:P k) := by
  simp [loop,rawGenerator,edge,previous]

private theorem single_power (n : ℕ) :
    (Matrix.single 0 0 (X:P k) : Mat (P k))^(n+1)=
      Matrix.single 0 0 ((X:P k)^(n+1)) := by
  induction n with
  | zero => simp
  | succ n ih =>
    calc
      _ = (Matrix.single 0 0 (X:P k) : Mat (P k))^(n+1)*
          Matrix.single 0 0 (X:P k) := pow_succ _ _
      _ = Matrix.single 0 0 ((X:P k)^(n+1)*X) := by rw [ih,Matrix.single_mul_single_same]
      _ = _ := congrArg (fun a : P k => (Matrix.single 0 0 a : Mat (P k)))
        (pow_succ (X:P k) (n+1)).symm

theorem loop_power_entry (n : ℕ) :
    (first k ((loop k)^n)) 0 0=(X:P k)^n := by
  rw [map_pow,loop_first]
  cases n with
  | zero => simp
  | succ n => rw [single_power]; simp

theorem polynomial_recovery (f : P k) :
    (firstAlg k ((Polynomial.aeval (loop k)) f)) 0 0=f := by
  induction f using Polynomial.induction_on' with
  | add f g hf hg => simp only [map_add,Matrix.add_apply,hf,hg]
  | monomial n a =>
    have hm : (Polynomial.aeval (loop k)) (monomial n a)=a • (loop k)^n := by
      simp [Polynomial.aeval_monomial,Algebra.smul_def]
    rw [hm,map_smul]
    change a • (first k ((loop k)^n) 0 0)=_
    rw [loop_power_entry,Polynomial.smul_eq_C_mul,Polynomial.C_mul_X_pow_eq_monomial]

theorem polynomial_embedding_injective :
    Function.Injective (Polynomial.aeval (R:=k) (loop k)) := by
  intro f g h
  have he := congrArg (fun a : A k => firstAlg k a 0 0) h
  simpa only [polynomial_recovery] using he

theorem algebra_not_finite : ¬ Module.Finite k (A k) := by
  intro h
  letI := h
  letI : Module.Finite k (P k) := Module.Finite.of_injective
    (Polynomial.aeval (loop k)).toLinearMap (polynomial_embedding_injective k)
  exact Polynomial.not_finite (R:=k) inferInstance

def representation {R : Type*} [CommRing R] [Algebra k R] (z : R) :
    A k →+* Mat R :=
  ((Polynomial.aeval z).toRingHom.mapMatrix).comp (first k)

def epsilon : D k := ⟨0,1⟩

def residue : D k →+* k where
  toFun x := x.re
  map_one' := rfl
  map_zero' := rfl
  map_add' _ _ := rfl
  map_mul' x y := by simp [QuadraticAlgebra.re_mul]

theorem residue_evaluation (f : P k) :
    residue k ((Polynomial.aeval (epsilon k)) f) = Polynomial.eval 0 f := by
  induction f using Polynomial.induction_on' with
  | add f g hf hg => simp only [map_add,eval_add,hf,hg]
  | monomial n a =>
    have hp : ((epsilon k)^n).re = (0:k)^n := by
      simpa [residue,epsilon] using (residue k).map_pow (epsilon k) n
    simp [Polynomial.aeval_monomial,residue,QuadraticAlgebra.re_mul,hp]

@[simp] theorem evaluation_re (f : P k) :
    ((Polynomial.aeval (epsilon k)) f).re = Polynomial.eval 0 f :=
  residue_evaluation k f

private def imagAdd : D k →+ k where
  toFun x := x.im
  map_zero' := rfl
  map_add' _ _ := rfl

@[simp] private theorem dual_re_sum {I : Type*} [Fintype I] (f : I → D k) :
    (∑ i, f i).re = ∑ i, (f i).re :=
  map_sum (residue k) f Finset.univ

@[simp] private theorem dual_im_sum {I : Type*} [Fintype I] (f : I → D k) :
    (∑ i, f i).im = ∑ i, (f i).im :=
  map_sum (imagAdd k) f Finset.univ

abbrev M1 := Vertex → k
abbrev M2 := Vertex → D k

def action0 : A k →+* Module.End k (M1 k) :=
  Matrix.toLinAlgEquiv'.toRingHom.comp (representation k (0:k))
def action2 : A k →+* Module.End (D k) (M2 k) :=
  Matrix.toLinAlgEquiv'.toRingHom.comp (representation k (epsilon k))

instance moduleOne : Module (A k) (M1 k) := Module.compHom _ (action0 k)
instance moduleTwo : Module (A k) (M2 k) := Module.compHom _ (action2 k)

theorem action_one_formula (a : A k) (x : M1 k) (i : Vertex) :
    (a • x) i = ∑ j, Polynomial.eval 0 (a.val.1 i j)*x j := rfl

theorem action_two_formula (a : A k) (x : M2 k) (i : Vertex) :
    (a • x) i = ∑ j, (Polynomial.aeval (epsilon k)) (a.val.1 i j)*x j := rfl

def inclusion : M1 k →ₗ[A k] M2 k where
  toFun x i := ⟨0,x i⟩
  map_add' x y := by funext i; apply QuadraticAlgebra.ext <;> simp
  map_smul' a x := by
    funext i
    apply QuadraticAlgebra.ext
    · simp [action_two_formula,QuadraticAlgebra.re_mul]
    · simp [action_two_formula,action_one_formula,QuadraticAlgebra.im_mul,
        evaluation_re]

def project : M2 k →ₗ[A k] M1 k where
  toFun x i := (x i).re
  map_add' x y := rfl
  map_smul' a x := by
    funext i
    simp [action_two_formula,action_one_formula,QuadraticAlgebra.re_mul]

theorem include_injective : Function.Injective (inclusion k) := by
  intro x y h
  funext i
  exact congrArg (fun v : M2 k => (v i).im) h

theorem project_surjective : Function.Surjective (project k) := by
  intro x
  exact ⟨fun i => ⟨x i,0⟩,rfl⟩

theorem project_include : (project k).comp (inclusion k) = 0 := by
  ext x i
  rfl

theorem range_include_eq_kernel_project :
    LinearMap.range (inclusion k) = LinearMap.ker (project k) := by
  ext x
  constructor
  · rintro ⟨y,rfl⟩
    rfl
  · intro hx
    refine ⟨fun i => (x i).im,?_⟩
    funext i
    apply QuadraticAlgebra.ext
    · exact (congrFun hx i).symm
    · rfl

theorem a0_zero_on_one (x : M1 k) : generator k (.a 0) • x = 0 := by
  funext i
  simp [action_one_formula,generator,rawGenerator,edge,Matrix.single,
    previous,apply_ite]

theorem a0_on_two (x : M2 k) :
    (generator k (.a 0) • x) 4 = epsilon k * x 0 := by
  simp [action_two_formula,generator,rawGenerator,edge,Matrix.single,previous,apply_ite]

theorem no_module_section :
    ¬ ∃ s : M1 k →ₗ[A k] M2 k, (project k).comp s = LinearMap.id := by
  rintro ⟨s,hs⟩
  let v : M1 k := Pi.single 0 1
  have hz : generator k (.a 0) • s v = 0 := by
    rw [← s.map_smul, a0_zero_on_one, map_zero]
  have hr : (s v 0).re = 1 := by
    have h := congrFun (LinearMap.congr_fun hs v) 0
    simpa [project,v] using h
  have he := congrArg (fun x : M2 k => (x 4).im) hz
  dsimp only at he
  rw [a0_on_two] at he
  simp [epsilon,QuadraticAlgebra.im_mul,hr] at he

end
end GRHResearch.BranchExtension

#check GRHResearch.BranchExtension.view_injective
#print axioms GRHResearch.BranchExtension.view_injective
#check GRHResearch.BranchExtension.view_generator
#print axioms GRHResearch.BranchExtension.view_generator
#check GRHResearch.BranchExtension.first_generator
#print axioms GRHResearch.BranchExtension.first_generator
#check GRHResearch.BranchExtension.mixed_products_zero
#print axioms GRHResearch.BranchExtension.mixed_products_zero
#check GRHResearch.BranchExtension.sum_vertices
#print axioms GRHResearch.BranchExtension.sum_vertices
#check GRHResearch.BranchExtension.loop_first
#print axioms GRHResearch.BranchExtension.loop_first
#check GRHResearch.BranchExtension.loop_power_entry
#print axioms GRHResearch.BranchExtension.loop_power_entry
#check GRHResearch.BranchExtension.polynomial_recovery
#print axioms GRHResearch.BranchExtension.polynomial_recovery
#check GRHResearch.BranchExtension.polynomial_embedding_injective
#print axioms GRHResearch.BranchExtension.polynomial_embedding_injective
#check GRHResearch.BranchExtension.algebra_not_finite
#print axioms GRHResearch.BranchExtension.algebra_not_finite
#check GRHResearch.BranchExtension.residue_evaluation
#print axioms GRHResearch.BranchExtension.residue_evaluation
#check GRHResearch.BranchExtension.evaluation_re
#print axioms GRHResearch.BranchExtension.evaluation_re
#check GRHResearch.BranchExtension.action_one_formula
#print axioms GRHResearch.BranchExtension.action_one_formula
#check GRHResearch.BranchExtension.action_two_formula
#print axioms GRHResearch.BranchExtension.action_two_formula
#check GRHResearch.BranchExtension.include_injective
#print axioms GRHResearch.BranchExtension.include_injective
#check GRHResearch.BranchExtension.project_surjective
#print axioms GRHResearch.BranchExtension.project_surjective
#check GRHResearch.BranchExtension.project_include
#print axioms GRHResearch.BranchExtension.project_include
#check GRHResearch.BranchExtension.range_include_eq_kernel_project
#print axioms GRHResearch.BranchExtension.range_include_eq_kernel_project
#check GRHResearch.BranchExtension.a0_zero_on_one
#print axioms GRHResearch.BranchExtension.a0_zero_on_one
#check GRHResearch.BranchExtension.a0_on_two
#print axioms GRHResearch.BranchExtension.a0_on_two
#check GRHResearch.BranchExtension.no_module_section
#print axioms GRHResearch.BranchExtension.no_module_section

/-! Unbounded normal path-image coordinates. This does not assume that the
ambient family spans the generated algebra or is a path-quotient equivalence. -/
namespace GRHResearch.BranchExtension.NormalPath
noncomputable section
open Polynomial Matrix
variable (k : Type*) [Field k]

structure Slot where
  row : Vertex
  col : Vertex
  degree : ℕ
  allowed : row < col ∨ 0 < degree

instance : DecidableEq Slot := Classical.decEq _
abbrev Key := Vertex ⊕ (Bool × Slot)
abbrev Ambient := Mat (P k) × Mat (P k)

@[ext] theorem slot_ext {s t : Slot} (hr : s.row=t.row)
    (hc : s.col=t.col) (hq : s.degree=t.degree) : s=t := by
  cases s; cases t
  cases hr; cases hc; cases hq
  rfl

def length (s : Slot) : ℕ := 5*s.degree+s.col.val-s.row.val

theorem positive_length (s : Slot) : 0 < length s := by
  have hi := s.row.isLt
  have hj := s.col.isLt
  rcases s.allowed with h | h
  · have hv : s.row.val < s.col.val := h
    unfold length
    omega
  · unfold length
    omega

theorem length_equation (s : Slot) :
    length s+s.row.val=5*s.degree+s.col.val := by
  have h := positive_length s
  unfold length at *
  omega

theorem same_start_length {s t : Slot} (hc : s.col=t.col)
    (hl : length s=length t) : s=t := by
  have hs := length_equation s
  have ht := length_equation t
  have hi := s.row.isLt
  have hj := t.row.isLt
  have hv := congrArg Fin.val hc
  apply slot_ext
  · apply Fin.ext
    omega
  · exact hc
  · omega

def vector : Key → Ambient k
  | .inl i => (Matrix.single i i 1,Matrix.single i i 1)
  | .inr (b,s) => if b then
      (0,Matrix.single s.row s.col (monomial s.degree 1)) else
      (Matrix.single s.row s.col (monomial s.degree 1),0)

def coefficient (x : Key) (M : Ambient k) : k :=
  match x with
  | .inl i => (M.1 i i).coeff 0
  | .inr (b,s) => ((if b then M.2 else M.1) s.row s.col).coeff s.degree

def selector (x : Key) : Ambient k →ₗ[k] k where
  toFun := coefficient k x
  map_add' M N := by
    cases x with
    | inl i => simp [coefficient]
    | inr bs => rcases bs with ⟨b,s⟩; cases b <;> simp [coefficient]
  map_smul' a M := by
    cases x with
    | inl i => simp [coefficient]
    | inr bs => rcases bs with ⟨b,s⟩; cases b <;> simp [coefficient]

private theorem single_coefficient (i j r c : Vertex) (q n : ℕ) :
    (Matrix.single i j (monomial q (1:k)) r c).coeff n =
      if i=r ∧ j=c ∧ q=n then 1 else 0 := by
  by_cases hi : i=r <;> by_cases hj : j=c <;>
    simp [Matrix.single,hi,hj,Polynomial.coeff_monomial]

private theorem no_constant_diagonal (s : Slot) (i : Vertex) :
    (Matrix.single s.row s.col (monomial s.degree (1:k)) i i).coeff 0=0 := by
  rw [single_coefficient]
  split_ifs with h
  · rcases s.allowed with hlt | hpos
    · have : s.row=s.col := h.1.trans h.2.1.symm
      exact False.elim ((ne_of_lt hlt) this)
    · exact False.elim ((Nat.ne_of_gt hpos) h.2.2)
  · rfl

private theorem positive_on_vertex (b : Bool) (s : Slot) (i : Vertex) :
    coefficient k (.inr (b,s)) (vector k (.inl i))=0 := by
  by_cases hr : i=s.row
  · subst i
    by_cases hc : s.row=s.col
    · have hq : s.degree≠0 := by
        rcases s.allowed with h | h
        · exact False.elim ((ne_of_lt h) hc)
        · exact Nat.ne_of_gt h
      cases b <;> simp [coefficient,vector,Matrix.single,hc,Polynomial.coeff_one,hq]
    · cases b <;> simp [coefficient,vector,Matrix.single,hc]
  · cases b <;> simp [coefficient,vector,Matrix.single,hr]

private theorem slot_coordinates {s t : Slot} :
    (t.row=s.row ∧ t.col=s.col ∧ t.degree=s.degree) ↔ s=t := by
  constructor
  · rintro ⟨hr,hc,hq⟩
    exact slot_ext hr.symm hc.symm hq.symm
  · rintro rfl
    exact ⟨rfl,rfl,rfl⟩

theorem selector_vector (x y : Key) :
    selector k x (vector k y) = if x=y then 1 else 0 := by
  change coefficient k x (vector k y)=_
  cases x with
  | inl i =>
    cases y with
    | inl j =>
      by_cases h : i=j
      · subst j; simp [coefficient,vector,Matrix.single]
      · simp [coefficient,vector,Matrix.single,h,Ne.symm h]
    | inr bs =>
      rcases bs with ⟨b,s⟩
      cases b <;> simp [coefficient,vector,no_constant_diagonal]
  | inr bs =>
    rcases bs with ⟨b,s⟩
    cases y with
    | inl i => simp [positive_on_vertex]
    | inr ct =>
      rcases ct with ⟨c,t⟩
      cases b <;> cases c <;>
        simp [coefficient,vector,single_coefficient,slot_coordinates]


theorem coefficient_recovery (x : Key) (l : Key →₀ k) :
    selector k x (Finsupp.linearCombination k (vector k) l)=l x := by
  classical
  induction l using Finsupp.induction_linear with
  | zero => simp
  | add l m hl hm => simp [hl,hm]
  | single y a =>
    by_cases h : x=y
    · subst y; simp [selector_vector]
    · simp [selector_vector,h]

theorem normal_vectors_independent : LinearIndependent k (vector k) := by
  rw [linearIndependent_iff]
  intro l hl
  ext x
  have h := congrArg (fun M => selector k x M) hl
  simpa only [coefficient_recovery,map_zero,Finsupp.zero_apply] using h

theorem normal_form_injective :
    Function.Injective (Finsupp.linearCombination k (vector k)) :=
  normal_vectors_independent k

end
end GRHResearch.BranchExtension.NormalPath

#check GRHResearch.BranchExtension.NormalPath.slot_ext
#print axioms GRHResearch.BranchExtension.NormalPath.slot_ext
#check GRHResearch.BranchExtension.NormalPath.positive_length
#print axioms GRHResearch.BranchExtension.NormalPath.positive_length
#check GRHResearch.BranchExtension.NormalPath.length_equation
#print axioms GRHResearch.BranchExtension.NormalPath.length_equation
#check GRHResearch.BranchExtension.NormalPath.same_start_length
#print axioms GRHResearch.BranchExtension.NormalPath.same_start_length
#check GRHResearch.BranchExtension.NormalPath.selector_vector
#print axioms GRHResearch.BranchExtension.NormalPath.selector_vector
#check GRHResearch.BranchExtension.NormalPath.coefficient_recovery
#print axioms GRHResearch.BranchExtension.NormalPath.coefficient_recovery
#check GRHResearch.BranchExtension.NormalPath.normal_vectors_independent
#print axioms GRHResearch.BranchExtension.NormalPath.normal_vectors_independent
#check GRHResearch.BranchExtension.NormalPath.normal_form_injective
#print axioms GRHResearch.BranchExtension.NormalPath.normal_form_injective
