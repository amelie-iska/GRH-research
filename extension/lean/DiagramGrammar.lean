import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.Data.Complex.Basic
import Mathlib.LinearAlgebra.Matrix.Kronecker
import Mathlib.LinearAlgebra.Matrix.Trace

/-!
# A typed sequential fragment of diagram rewriting

Objects are labels and each label is assigned a module. The syntax below has
only identity, typed generators, and sequential composition. A context has one
typed hole; replacing that hole by an equal linear map preserves denotation.
Sound basic rewrite rules therefore remain sound under every finite sequence of
contextual rewrites. No termination, confluence, semantic completeness, tensor
word syntax, graphical isotopy, traced symmetric-monoidal coherence, dagger,
measurement, classical control, or CP/TP channel theorem is asserted here.

Separate finite-matrix lemmas record tensor interchange and closed-loop
contractions. They are exact algebraic components, not an identification of the
sequential syntax with a full tensor graph grammar. Algebraic changes of bases
preserve complexes and exactness; a separate finite matrix identity gives
Hodge conjugacy under its stated unitary endpoint assumptions. No uniform
analytic bound or infinite-dimensional spectral theorem is asserted.
-/

set_option autoImplicit false

universe u v w z

namespace DiagramGrammar

inductive Diagram {Obj : Type u} (Gen : Obj → Obj → Type v) :
    Obj → Obj → Type (max u v) where
  | ident (a : Obj) : Diagram Gen a a
  | atom {a b : Obj} (g : Gen a b) : Diagram Gen a b
  | seq {a b c : Obj} (f : Diagram Gen a b) (g : Diagram Gen b c) : Diagram Gen a c

inductive Context {Obj : Type u} (Gen : Obj → Obj → Type v) (a b : Obj) :
    Obj → Obj → Type (max u v) where
  | hole : Context Gen a b a b
  | before {x y z : Obj} (f : Diagram Gen x y) (C : Context Gen a b y z) :
      Context Gen a b x z
  | after {x y z : Obj} (C : Context Gen a b x y) (f : Diagram Gen y z) :
      Context Gen a b x z

def fill {Obj : Type u} {Gen : Obj → Obj → Type v} {a b x y : Obj}
    (C : Context Gen a b x y) (d : Diagram Gen a b) : Diagram Gen x y :=
  match C with
  | .hole => d
  | .before f C => .seq f (fill C d)
  | .after C f => .seq (fill C d) f

section Semantics

variable {Obj : Type u} {Gen : Obj → Obj → Type v}
variable {K : Type z} [Semiring K]
variable {V : Obj → Type w}
variable [∀ a, AddCommMonoid (V a)] [∀ a, Module K (V a)]

def denote (rho : ∀ (a b : Obj), Gen a b → V a →ₗ[K] V b) :
    ∀ {a b}, Diagram Gen a b → V a →ₗ[K] V b
  | _, _, .ident _ => LinearMap.id
  | _, _, .atom g => rho _ _ g
  | _, _, .seq f g => (denote rho g).comp (denote rho f)

/-- Equality of the interpreted hole is preserved by every typed sequential context. -/
theorem context_sound (rho : ∀ (a b : Obj), Gen a b → V a →ₗ[K] V b)
    {a b x y : Obj} {d e : Diagram Gen a b}
    (h : denote rho d = denote rho e) (C : Context Gen a b x y) :
    denote rho (fill C d) = denote rho (fill C e) := by
  induction C with
  | hole => exact h
  | before f C ih => simp only [fill, denote, ih]
  | after C f ih => simp only [fill, denote, ih]

inductive StructuralRule : ∀ {a b : Obj}, Diagram Gen a b → Diagram Gen a b → Prop
  | left_id {a b} (d : Diagram Gen a b) :
      StructuralRule (.seq (.ident a) d) d
  | right_id {a b} (d : Diagram Gen a b) :
      StructuralRule (.seq d (.ident b)) d
  | assoc {a b c d} (f : Diagram Gen a b) (g : Diagram Gen b c) (h : Diagram Gen c d) :
      StructuralRule (.seq (.seq f g) h) (.seq f (.seq g h))

/-- The actual identity and associativity rewrite rules are semantically sound. -/
theorem structural_sound (rho : ∀ (a b : Obj), Gen a b → V a →ₗ[K] V b)
    {a b : Obj} {d e : Diagram Gen a b} (h : StructuralRule d e) :
    denote rho d = denote rho e := by
  cases h <;> ext v <;> rfl

inductive RewriteStep
    (Rules : ∀ {a b : Obj}, Diagram Gen a b → Diagram Gen a b → Prop) :
    ∀ {x y : Obj}, Diagram Gen x y → Diagram Gen x y → Prop
  | in_context {a b x y} {d e : Diagram Gen a b}
      (h : Rules d e) (C : Context Gen a b x y) :
      RewriteStep Rules (fill C d) (fill C e)

def Derives
    (Rules : ∀ {a b : Obj}, Diagram Gen a b → Diagram Gen a b → Prop)
    {x y : Obj} (d e : Diagram Gen x y) : Prop :=
  Relation.ReflTransGen (RewriteStep Rules) d e

/-- A single basic sound rule can be applied within any sequential context. -/
theorem rewriteStep_sound
    (rho : ∀ (a b : Obj), Gen a b → V a →ₗ[K] V b)
    (Rules : ∀ {a b : Obj}, Diagram Gen a b → Diagram Gen a b → Prop)
    (valid : ∀ {a b} {d e : Diagram Gen a b}, Rules d e → denote rho d = denote rho e)
    {x y : Obj} {d e : Diagram Gen x y} (h : RewriteStep Rules d e) :
    denote rho d = denote rho e := by
  cases h with
  | in_context h C => exact context_sound rho (valid h) C

/-- Every finite derivation using sound contextual rules preserves the exact linear map. -/
theorem derivation_sound
    (rho : ∀ (a b : Obj), Gen a b → V a →ₗ[K] V b)
    (Rules : ∀ {a b : Obj}, Diagram Gen a b → Diagram Gen a b → Prop)
    (valid : ∀ {a b} {d e : Diagram Gen a b}, Rules d e → denote rho d = denote rho e)
    {x y : Obj} {d e : Diagram Gen x y} (h : Derives Rules d e) :
    denote rho d = denote rho e := by
  induction h with
  | refl => rfl
  | tail first last ih => exact ih.trans (rewriteStep_sound rho Rules valid last)

/-- An exact consequence for the fixed identity/associativity rewrite system. -/
theorem structural_derivation_sound
    (rho : ∀ (a b : Obj), Gen a b → V a →ₗ[K] V b)
    {x y : Obj} {d e : Diagram Gen x y} (h : Derives StructuralRule d e) :
    denote rho d = denote rho e :=
  derivation_sound rho StructuralRule (structural_sound rho) h

/-- Linear equivalences supply an actual inverse-cancellation rule. This does
not assert that arbitrary generators, measurements, or channels are invertible. -/
theorem linearEquiv_cancellation {a b : Obj} (e : V a ≃ₗ[K] V b) :
    denote (fun (i j : Obj) (g : V i ≃ₗ[K] V j) => g.toLinearMap)
      (.seq (.atom e) (.atom e.symm)) =
    denote (fun (i j : Obj) (g : V i ≃ₗ[K] V j) => g.toLinearMap) (.ident a) := by
  ext x
  exact e.symm_apply_apply x

/-- A concrete basic rule family for generators interpreted as linear
 equivalences: structural rules and inverse-pair cancellation. -/
inductive EquivRule : ∀ {a b : Obj},
    Diagram (fun i j => V i ≃ₗ[K] V j) a b →
    Diagram (fun i j => V i ≃ₗ[K] V j) a b → Prop
  | structural {a b} {d e : Diagram (fun i j => V i ≃ₗ[K] V j) a b}
      (h : StructuralRule d e) : EquivRule d e
  | cancel {a b} (e : V a ≃ₗ[K] V b) :
      EquivRule (.seq (.atom e) (.atom e.symm)) (.ident a)

/-- Each rule of the explicit equivalence-generator system has an actual proof. -/
theorem equivRule_sound {a b : Obj}
    {d e : Diagram (fun i j => V i ≃ₗ[K] V j) a b} (h : EquivRule d e) :
    denote (fun (i j : Obj) (g : V i ≃ₗ[K] V j) => g.toLinearMap) d =
    denote (fun (i j : Obj) (g : V i ≃ₗ[K] V j) => g.toLinearMap) e := by
  cases h with
  | structural hs => exact structural_sound _ hs
  | cancel e => exact linearEquiv_cancellation e

/-- Any finite sequence of contextual structural/inverse rewrites preserves
 the exact linear map, without assuming every pair of equivalent maps can be
 connected by this limited rule set. -/
theorem equiv_derivation_sound {a b : Obj}
    {d e : Diagram (fun i j => V i ≃ₗ[K] V j) a b} (h : Derives EquivRule d e) :
    denote (fun (i j : Obj) (g : V i ≃ₗ[K] V j) => g.toLinearMap) d =
    denote (fun (i j : Obj) (g : V i ≃ₗ[K] V j) => g.toLinearMap) e :=
  derivation_sound _ EquivRule equivRule_sound h

end Semantics

section MatrixComponents

open scoped Kronecker

variable {R : Type u} [CommSemiring R]

/-- Tensor interchange is a finite matrix identity with explicit product indices. -/
theorem tensor_interchange {a b c d e f : Type v} [Fintype b] [Fintype e]
    (A : Matrix a b R) (B : Matrix b c R) (C : Matrix d e R) (D : Matrix e f R) :
    (A ⊗ₖ C) * (B ⊗ₖ D) = (A * B) ⊗ₖ (C * D) :=
  (Matrix.mul_kronecker_mul A B C D).symm

/-- Two disjoint closed matrix contractions multiply their scalar values. -/
theorem tensor_trace_factorization {a b : Type v} [Fintype a] [Fintype b]
    (A : Matrix a a R) (B : Matrix b b R) :
    Matrix.trace (A ⊗ₖ B) = Matrix.trace A * Matrix.trace B :=
  Matrix.trace_kronecker A B

/-- Cyclicity also permits the two sides to have different finite dimensions. -/
theorem rectangular_trace_cyclicity {a b : Type v} [Fintype a] [Fintype b]
    (A : Matrix a b R) (B : Matrix b a R) :
    Matrix.trace (A * B) = Matrix.trace (B * A) :=
  Matrix.trace_mul_comm A B

/-- A closed identity wire contributes the dimension, not the scalar one. -/
theorem identity_loop_value {a : Type v} [Fintype a] [DecidableEq a] :
    Matrix.trace (1 : Matrix a a R) = (Fintype.card a : R) :=
  Matrix.trace_one

end MatrixComponents

section ChangeOfBasis

variable {K V0 V1 V2 W0 W1 W2 : Type*} [Semiring K]
variable [AddCommMonoid V0] [AddCommMonoid V1] [AddCommMonoid V2]
variable [AddCommMonoid W0] [AddCommMonoid W1] [AddCommMonoid W2]
variable [Module K V0] [Module K V1] [Module K V2]
variable [Module K W0] [Module K W1] [Module K W2]

/-- Independent changes of bases preserve the zero-composition equation.
The equivalences are algebraic; no norm or spectral bound is asserted. -/
theorem complex_transport
    (A : V0 →ₗ[K] V1) (B : V1 →ₗ[K] V2) (h : B.comp A = 0)
    (e0 : V0 ≃ₗ[K] W0) (e1 : V1 ≃ₗ[K] W1) (e2 : V2 ≃ₗ[K] W2) :
    (e2.toLinearMap.comp (B.comp e1.symm.toLinearMap)).comp
      (e1.toLinearMap.comp (A.comp e0.symm.toLinearMap)) = 0 := by
  ext x
  have hz := LinearMap.congr_fun h (e0.symm x)
  simpa using congrArg e2 hz

/-- A middle contracting-homotopy identity proves exactness, provided the
successive maps also form a complex. This abstracts the exactness step in the
Koszul and finite Hodge arguments without formalizing exterior algebra. -/
theorem homotopy_implies_exact
    (A : V0 →ₗ[K] V1) (B : V1 →ₗ[K] V2) (hcomplex : B.comp A = 0)
    (s : V1 →ₗ[K] V0) (t : V2 →ₗ[K] V1)
    (hhomotopy : A.comp s + t.comp B = LinearMap.id) :
    LinearMap.range A = LinearMap.ker B := by
  apply le_antisymm (LinearMap.range_le_ker_iff.mpr hcomplex)
  intro v hv
  refine ⟨s v, ?_⟩
  have h := LinearMap.congr_fun hhomotopy v
  have hv0 : B v = 0 := hv
  simpa [hv0] using h

/-- Exactness itself is preserved under the independent algebraic changes of
bases; this includes an explicit witness for every vector in the new kernel. -/
theorem exact_transport
    (A : V0 →ₗ[K] V1) (B : V1 →ₗ[K] V2)
    (hexact : LinearMap.range A = LinearMap.ker B)
    (e0 : V0 ≃ₗ[K] W0) (e1 : V1 ≃ₗ[K] W1) (e2 : V2 ≃ₗ[K] W2) :
    LinearMap.range (e1.toLinearMap.comp (A.comp e0.symm.toLinearMap)) =
      LinearMap.ker (e2.toLinearMap.comp (B.comp e1.symm.toLinearMap)) := by
  have hcomplex : B.comp A = 0 := LinearMap.range_le_ker_iff.mp hexact.le
  apply le_antisymm
    (LinearMap.range_le_ker_iff.mpr (complex_transport A B hcomplex e0 e1 e2))
  intro w hw
  change e2 (B (e1.symm w)) = 0 at hw
  have hb : B (e1.symm w) = 0 := e2.injective (by simpa using hw)
  have hr : e1.symm w ∈ LinearMap.range A := by
    rw [hexact]
    exact hb
  rcases hr with ⟨v, hv⟩
  refine ⟨e0 v, ?_⟩
  simpa using congrArg e1 hv

end ChangeOfBasis

section HodgeConjugacy

open Matrix

/-- A finite matrix Hodge identity under unitary changes at the endpoint
spaces. The middle matrix may be arbitrary for this identity; choosing it
unitary yields the usual unitary-conjugacy formula. No spectral theorem or
infinite-dimensional operator domain is formalized by this statement. -/
theorem matrix_hodge_conjugacy
    {n0 n1 n2 : Type*} [Fintype n0] [Fintype n1] [Fintype n2]
    [DecidableEq n0] [DecidableEq n2]
    (A : Matrix n1 n0 ℂ) (B : Matrix n2 n1 ℂ)
    (U0 : Matrix n0 n0 ℂ) (U1 : Matrix n1 n1 ℂ) (U2 : Matrix n2 n2 ℂ)
    (h0 : U0ᴴ * U0 = 1) (h2 : U2ᴴ * U2 = 1) :
    (U1 * A * U0ᴴ) * (U1 * A * U0ᴴ)ᴴ +
      (U2 * B * U1ᴴ)ᴴ * (U2 * B * U1ᴴ) =
      U1 * (A * Aᴴ + Bᴴ * B) * U1ᴴ := by
  simp only [Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose]
  calc
    _ = U1 * A * (U0ᴴ * U0) * Aᴴ * U1ᴴ +
        U1 * Bᴴ * (U2ᴴ * U2) * B * U1ᴴ := by simp only [Matrix.mul_assoc]
    _ = U1 * A * Aᴴ * U1ᴴ + U1 * Bᴴ * B * U1ᴴ := by
      rw [h0, h2]
      simp only [Matrix.mul_one]
    _ = _ := by simp only [Matrix.mul_add, Matrix.add_mul, Matrix.mul_assoc]

end HodgeConjugacy

end DiagramGrammar

-- Exact declaration types, followed by foundational dependency inventories.
#check DiagramGrammar.context_sound
#check DiagramGrammar.structural_sound
#check DiagramGrammar.rewriteStep_sound
#check DiagramGrammar.derivation_sound
#check DiagramGrammar.structural_derivation_sound
#check DiagramGrammar.linearEquiv_cancellation
#check DiagramGrammar.equivRule_sound
#check DiagramGrammar.equiv_derivation_sound
#check DiagramGrammar.tensor_interchange
#check DiagramGrammar.tensor_trace_factorization
#check DiagramGrammar.rectangular_trace_cyclicity
#check DiagramGrammar.identity_loop_value
#check DiagramGrammar.complex_transport
#check DiagramGrammar.homotopy_implies_exact
#check DiagramGrammar.exact_transport
#check DiagramGrammar.matrix_hodge_conjugacy

#print axioms DiagramGrammar.context_sound
#print axioms DiagramGrammar.structural_sound
#print axioms DiagramGrammar.rewriteStep_sound
#print axioms DiagramGrammar.derivation_sound
#print axioms DiagramGrammar.structural_derivation_sound
#print axioms DiagramGrammar.linearEquiv_cancellation
#print axioms DiagramGrammar.equivRule_sound
#print axioms DiagramGrammar.equiv_derivation_sound
#print axioms DiagramGrammar.tensor_interchange
#print axioms DiagramGrammar.tensor_trace_factorization
#print axioms DiagramGrammar.rectangular_trace_cyclicity
#print axioms DiagramGrammar.identity_loop_value
#print axioms DiagramGrammar.complex_transport
#print axioms DiagramGrammar.homotopy_implies_exact
#print axioms DiagramGrammar.exact_transport
#print axioms DiagramGrammar.matrix_hodge_conjugacy
