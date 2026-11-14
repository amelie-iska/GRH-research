import Mathlib.Tactic

/-! A complete finite-domain construction, not a numerical sample test.
Boolean circuits are interpreted both discretely and by affine/ReLU operations.
The structural theorem covers every finite syntax tree. Pattern circuits then
realize every table on a finite Boolean graph encoding, coordinate by coordinate.
The table is exponentially large; no efficient training or uniform unbounded
computation is inferred. A DAG can be unfolded into this syntax at its size cost.
-/
set_option autoImplicit false
open scoped BigOperators
namespace FiniteGraphNetworks

inductive Circuit (n : ℕ) where
 | input : Fin n → Circuit n
 | constant : Bool → Circuit n
 | neg : Circuit n → Circuit n
 | conj : Circuit n → Circuit n → Circuit n
 | disj : Circuit n → Circuit n → Circuit n

def bit (b : Bool) : ℝ := if b then 1 else 0

def discrete {n : ℕ} (x : Fin n → Bool) : Circuit n → Bool
 | .input i => x i
 | .constant b => b
 | .neg c => !(discrete x c)
 | .conj a b => discrete x a && discrete x b
 | .disj a b => discrete x a || discrete x b

noncomputable def neural {n : ℕ} (x : Fin n → ℝ) : Circuit n → ℝ
 | .input i => x i
 | .constant b => bit b
 | .neg c => 1-neural x c
 | .conj a b => max 0 (neural x a+neural x b-1)
 | .disj a b => neural x a+neural x b-max 0 (neural x a+neural x b-1)

theorem neural_correct {n : ℕ} (c : Circuit n) (x : Fin n → Bool) :
 neural (fun i => bit (x i)) c = bit (discrete x c) := by
 induction c with
 | input i => rfl
 | constant b => rfl
 | neg c ih =>
   simp only [neural,discrete,ih]
   cases discrete x c <;> norm_num [bit]
 | conj a b ia ib =>
   simp only [neural,discrete,ia,ib]
   cases discrete x a <;> cases discrete x b <;> norm_num [bit]
 | disj a b ia ib =>
   simp only [neural,discrete,ia,ib]
   cases discrete x a <;> cases discrete x b <;> norm_num [bit]

def literal {n : ℕ} (pattern : Fin n → Bool) (i : Fin n) : Circuit n :=
 if pattern i then .input i else .neg (.input i)

def indicatorList {n : ℕ} (pattern : Fin n → Bool) : List (Fin n) → Circuit n
 | [] => .constant true
 | i::is => .conj (literal pattern i) (indicatorList pattern is)

theorem literal_spec {n : ℕ} (s x : Fin n → Bool) (i : Fin n) :
 discrete x (literal s i) = true ↔ x i=s i := by
 simp only [literal]
 cases hs : s i <;> cases hx : x i <;> simp [hx,discrete]

theorem indicatorList_spec {n : ℕ} (s x : Fin n → Bool) (is : List (Fin n)) :
 discrete x (indicatorList s is)=true ↔ ∀ i∈is, x i=s i := by
 induction is with
 | nil => simp [indicatorList,discrete]
 | cons i is ih =>
   simp only [indicatorList,discrete,Bool.and_eq_true,literal_spec,ih,List.mem_cons]
   constructor
   · rintro ⟨hi,his⟩ j (hj|hj)
     · simpa only [hj] using hi
     · exact his j hj
   · intro h
     exact ⟨h i (Or.inl rfl),fun j hj => h j (Or.inr hj)⟩

def indicator {n : ℕ} (s : Fin n → Bool) : Circuit n :=
 indicatorList s (List.finRange n)

theorem indicator_spec {n : ℕ} (s x : Fin n → Bool) :
 discrete x (indicator s)=true ↔ x=s := by
 rw [indicator,indicatorList_spec]
 simp only [List.mem_finRange,true_implies]
 exact ⟨fun h => funext h, fun h i => congrFun h i⟩

theorem neural_indicator {n : ℕ} (s x : Fin n → Bool) :
 neural (fun i => bit (x i)) (indicator s) = if x=s then 1 else 0 := by
 rw [neural_correct]
 by_cases h : x=s
 · have q := (indicator_spec s x).mpr h
   rw [q]
   simp [h,bit]
 · have q : discrete x (indicator s)=false := Bool.eq_false_iff.mpr (fun q => h ((indicator_spec s x).mp q))
   rw [q]
   simp [h,bit]

noncomputable def tableNetwork {n : ℕ} (F : (Fin n → Bool) → ℝ) (x : Fin n → ℝ) : ℝ :=
 ∑ s : Fin n → Bool, F s * neural x (indicator s)

theorem finite_function_exact {n : ℕ} (F : (Fin n → Bool) → ℝ) (x : Fin n → Bool) :
 tableNetwork F (fun i => bit (x i)) = F x := by
 classical
 simp only [tableNetwork,neural_indicator]
 simp

theorem finite_graph_to_graph_exact {n m : ℕ}
 (F : (Fin n → Bool) → (Fin m → ℝ)) (x : Fin n → Bool) :
 (fun j => tableNetwork (fun s => F s j) (fun i => bit (x i))) = F x := by
 funext j
 exact finite_function_exact (fun s => F s j) x

end FiniteGraphNetworks
#check FiniteGraphNetworks.neural_correct
#check FiniteGraphNetworks.literal_spec
#check FiniteGraphNetworks.indicatorList_spec
#check FiniteGraphNetworks.indicator_spec
#check FiniteGraphNetworks.neural_indicator
#check FiniteGraphNetworks.finite_function_exact
#check FiniteGraphNetworks.finite_graph_to_graph_exact
#print axioms FiniteGraphNetworks.neural_correct
#print axioms FiniteGraphNetworks.literal_spec
#print axioms FiniteGraphNetworks.indicatorList_spec
#print axioms FiniteGraphNetworks.indicator_spec
#print axioms FiniteGraphNetworks.neural_indicator
#print axioms FiniteGraphNetworks.finite_function_exact
#print axioms FiniteGraphNetworks.finite_graph_to_graph_exact
