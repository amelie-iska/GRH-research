import Mathlib.Tactic

/-! Exact constructive interfaces. These declarations prove the displayed
identities and conditional transfer statements. The continuous compact-domain
network construction is proved in the accompanying exposition; the separate
FiniteGraphNetworks module proves complete finite-table realization. -/
set_option autoImplicit false
open scoped BigOperators
namespace ConstructiveGraph

 theorem softmax_gather_inverse (S x n : ℝ) (hn : n ≠ 0) (hp : n+1 ≠ 0) :
    (n+1)*((S+x)/(n+1))-n*(S/n)=x := by
  field_simp
  ring

 theorem one_hot_slot (x B b : ℝ) (hx : |x| ≤ B)
    (hb : b=0 ∨ b=1) :
    max 0 (x+B*b)-max 0 (x-B*b)-B*b=x*b := by
  rw [abs_le] at hx
  rcases hb with rfl | rfl
  · simp
  · simp only [mul_one]
    rw [max_eq_right (by linarith : 0 ≤ x+B), max_eq_left (by linarith : x-B ≤ 0)]
    ring

 theorem square_interpolation_error (a b x : ℝ) (ha : a ≤ x) (hb : x ≤ b) :
    0 ≤ (a+b)*x-a*b-x^2 ∧
    (a+b)*x-a*b-x^2 ≤ (b-a)^2/4 := by
  constructor
  · nlinarith [mul_nonneg (sub_nonneg.mpr ha) (sub_nonneg.mpr hb)]
  · nlinarith [sq_nonneg (2*x-a-b)]

 theorem neural_product_error (splus sminus x y ε : ℝ)
    (hp : |splus-(x+y)^2| ≤ ε) (hm : |sminus-(x-y)^2| ≤ ε) :
    |(splus-sminus)/4-x*y| ≤ ε/2 := by
  rw [abs_le] at hp hm ⊢
  constructor <;> nlinarith

 theorem uniform_class_transfer {X Z Y : Type*} [PseudoMetricSpace Y]
    (E : X → Z) (F : X → Y) (G : Z → Y)
    (K : Set X) (A : Set (Z → Y))
    (hG : ∀ x ∈ K, G (E x)=F x)
    (hA : ∀ ε : ℝ, 0 < ε → ∃ a ∈ A, ∀ z ∈ E '' K, dist (a z) (G z)<ε) :
    ∀ ε : ℝ, 0 < ε → ∃ a ∈ A, ∀ x ∈ K, dist (a (E x)) (F x)<ε := by
  intro ε hε
  obtain ⟨a, ha, h⟩ := hA ε hε
  refine ⟨a, ha, ?_⟩
  intro x hx
  have q := h (E x) ⟨x,hx,rfl⟩
  simpa only [hG x hx] using q

 theorem decoder_margin_composition (δ L ε γ : ℝ)
    (hδ : δ ≤ L*ε) (hm : 2*(L*ε)<γ) : 2*δ<γ := by linarith

 theorem zero_extension_preserves {X Y : Type*} [AddGroup Y]
    (F R : X → Y) (h : ∀ x, R x=0) : (fun x => F x+R x)=F := by
  funext x
  rw [h x, add_zero]

end ConstructiveGraph
#check ConstructiveGraph.softmax_gather_inverse
#check ConstructiveGraph.one_hot_slot
#check ConstructiveGraph.square_interpolation_error
#check ConstructiveGraph.neural_product_error
#check ConstructiveGraph.uniform_class_transfer
#check ConstructiveGraph.decoder_margin_composition
#check ConstructiveGraph.zero_extension_preserves
#print axioms ConstructiveGraph.softmax_gather_inverse
#print axioms ConstructiveGraph.one_hot_slot
#print axioms ConstructiveGraph.square_interpolation_error
#print axioms ConstructiveGraph.neural_product_error
#print axioms ConstructiveGraph.uniform_class_transfer
#print axioms ConstructiveGraph.decoder_margin_composition
#print axioms ConstructiveGraph.zero_extension_preserves
