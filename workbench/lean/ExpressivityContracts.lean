import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-! Selected transfer and robustness statements used by the source-led repair.
The full continuous compact-domain graph theorem has a written constructive
proof; these declarations verify specific interfaces in that argument. They do
not introduce a universal-approximation theorem as an axiom. -/
set_option autoImplicit false
namespace ExpressivityContracts

 theorem faithful_encoding_injective {X Z : Type*} (E : X → Z) (D : Z → X)
    (h : ∀ x, D (E x) = x) : Function.Injective E := by
  intro x y he
  calc x = D (E x) := (h x).symm
       _ = D (E y) := congrArg D he
       _ = y := h y

 theorem fiber_obstruction {X Z Y : Type*} (E : X → Z) (F : X → Y)
    (x y : X) (hE : E x = E y) (hF : F x ≠ F y) :
    ¬ ∃ A : Z → Y, ∀ t, A (E t) = F t := by
  rintro ⟨A, hA⟩
  apply hF
  calc F x = A (E x) := (hA x).symm
       _ = A (E y) := congrArg A hE
       _ = F y := hA y

 theorem encoded_uniform_bound {X Z Y : Type*} [PseudoMetricSpace Y]
    (E : X → Z) (F : X → Y) (G A : Z → Y) (K : Set X) (ε : ℝ)
    (hF : ∀ x ∈ K, G (E x) = F x)
    (h : ∀ z ∈ E '' K, dist (A z) (G z) ≤ ε) :
    ∀ x ∈ K, dist (A (E x)) (F x) ≤ ε := by
  intro x hx
  have q := h (E x) ⟨x,hx,rfl⟩
  simpa only [hF x hx] using q

 theorem decoder_error_bound {Y Z : Type*} [PseudoMetricSpace Y] [PseudoMetricSpace Z]
    (D : Y → Z) (y y' : Y) (L ε : ℝ) (hL : 0 ≤ L)
    (hD : dist (D y) (D y') ≤ L * dist y y') (he : dist y y' ≤ ε) :
    dist (D y) (D y') ≤ L * ε := by
  exact hD.trans (mul_le_mul_of_nonneg_left he hL)

 theorem margin_preservation (a b a' b' ε : ℝ)
    (ha : |a' - a| ≤ ε) (hb : |b' - b| ≤ ε)
    (hgap : 2 * ε < a - b) : b' < a' := by
  rw [abs_le] at ha hb
  linarith

 theorem max_nonexpansive (a b c d ε : ℝ)
    (ha : |a-c| ≤ ε) (hb : |b-d| ≤ ε) :
    |max a b - max c d| ≤ ε := by
  rw [abs_le] at ha hb ⊢
  have hac : a ≤ max c d + ε := by have := le_max_left c d; linarith
  have hbd : b ≤ max c d + ε := by have := le_max_right c d; linarith
  have hca : c ≤ max a b + ε := by have := le_max_left a b; linarith
  have hdb : d ≤ max a b + ε := by have := le_max_right a b; linarith
  have h1 := max_le hac hbd
  have h2 := max_le hca hdb
  constructor <;> linarith

 theorem maxplus_shift (a b t : ℝ) : max (a+t) (b+t) = max a b + t := by
  rcases le_total a b with h | h
  · rw [max_eq_right h, max_eq_right (add_le_add_right h t)]
  · rw [max_eq_left h, max_eq_left (add_le_add_right h t)]

 theorem boolean_and (x y : ℝ) (hx : x=0 ∨ x=1) (hy : y=0 ∨ y=1) :
    max 0 (x+y-1) = x*y := by
  rcases hx with rfl | rfl <;> rcases hy with rfl | rfl <;> norm_num

 theorem boolean_or (x y : ℝ) (hx : x=0 ∨ x=1) (hy : y=0 ∨ y=1) :
    x+y-max 0 (x+y-1) = x+y-x*y := by
  rw [boolean_and x y hx hy]

 theorem finite_average_error {ι : Type*} [Fintype ι]
    (e : ι → ℝ) (ε : ℝ) (h : ∀ i, |e i| ≤ ε) :
    |∑ i, e i| ≤ (Fintype.card ι : ℝ) * ε := by
  calc |∑ i, e i| ≤ ∑ i, |e i| := Finset.abs_sum_le_sum_abs _ _
       _ ≤ ∑ _i : ι, ε := Finset.sum_le_sum (fun i _ => h i)
       _ = (Fintype.card ι : ℝ) * ε := by simp

 theorem composition_error {X : Type*} [PseudoMetricSpace X]
    (F A : X → X) (x y : X) (L e δ : ℝ) (hL : 0 ≤ L)
    (hF : dist (F x) (F y) ≤ L * dist x y)
    (hA : dist (A y) (F y) ≤ δ) (he : dist x y ≤ e) :
    dist (F x) (A y) ≤ L * e + δ := by
  calc dist (F x) (A y) ≤ dist (F x) (F y) + dist (F y) (A y) := dist_triangle _ _ _
       _ ≤ L * e + δ := by
          rw [dist_comm (F y) (A y)]
          exact add_le_add (hF.trans (mul_le_mul_of_nonneg_left he hL)) hA

 theorem exact_bypass (a b : ℝ) : a + 0*b = a := by ring

 theorem binary_hessian_counterexample :
    2 * ((3:ℚ)/4) * (1-3/4) > (1:ℚ)/3 := by norm_num

 theorem rational_rotation_norm (c s x y : ℝ) (h : c*c+s*s=1) :
    (c*x-s*y)^2+(s*x+c*y)^2=x^2+y^2 := by
  nlinarith [sq_nonneg (c*x-s*y),sq_nonneg (s*x+c*y)]

end ExpressivityContracts
#check ExpressivityContracts.faithful_encoding_injective
#check ExpressivityContracts.fiber_obstruction
#check ExpressivityContracts.encoded_uniform_bound
#check ExpressivityContracts.decoder_error_bound
#check ExpressivityContracts.margin_preservation
#check ExpressivityContracts.max_nonexpansive
#check ExpressivityContracts.maxplus_shift
#check ExpressivityContracts.boolean_and
#check ExpressivityContracts.boolean_or
#check ExpressivityContracts.finite_average_error
#check ExpressivityContracts.composition_error
#check ExpressivityContracts.exact_bypass
#check ExpressivityContracts.binary_hessian_counterexample
#check ExpressivityContracts.rational_rotation_norm
#print axioms ExpressivityContracts.faithful_encoding_injective
#print axioms ExpressivityContracts.fiber_obstruction
#print axioms ExpressivityContracts.encoded_uniform_bound
#print axioms ExpressivityContracts.decoder_error_bound
#print axioms ExpressivityContracts.margin_preservation
#print axioms ExpressivityContracts.max_nonexpansive
#print axioms ExpressivityContracts.maxplus_shift
#print axioms ExpressivityContracts.boolean_and
#print axioms ExpressivityContracts.boolean_or
#print axioms ExpressivityContracts.finite_average_error
#print axioms ExpressivityContracts.composition_error
#print axioms ExpressivityContracts.exact_bypass
#print axioms ExpressivityContracts.binary_hessian_counterexample
#print axioms ExpressivityContracts.rational_rotation_norm
