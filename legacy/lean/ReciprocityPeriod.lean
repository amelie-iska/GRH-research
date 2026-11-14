import Mathlib.Algebra.QuadraticAlgebra
import Mathlib.NumberTheory.JacobiSum.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Complex

namespace GRHResearch.Analytic

/-- The actual Eisenstein quadratic algebra: omega² = -1-omega. -/
abbrev EisensteinZ := QuadraticAlgebra ℤ (-1) (-1)
abbrev Eisenstein4 := QuadraticAlgebra (ZMod 4) (-1) (-1)

instance : Fintype Eisenstein4 :=
  Fintype.ofEquiv (ZMod 4 × ZMod 4) (QuadraticAlgebra.equivProd (-1) (-1)).symm

def odd4 (x : Eisenstein4) : Prop := x.re.val % 2 ≠ 0 ∨ x.im.val % 2 ≠ 0
instance (x : Eisenstein4) : Decidable (odd4 x) := inferInstanceAs (Decidable (_ ∨ _))

/-- Coordinates of the square class (-1)^e lambda^f modulo4. -/
def squareClass4 (x : Eisenstein4) : ZMod 2 × ZMod 2 :=
  match x.re.val, x.im.val with
  | 1, 0 | 0, 1 | 3, 3 => (0, 0)
  | 1, 2 | 2, 3 | 1, 3 => (0, 1)
  | 3, 0 | 0, 3 | 1, 1 => (1, 0)
  | 3, 2 | 2, 1 | 3, 1 => (1, 1)
  | _, _ => (0, 0)

noncomputable def gammaClass4 (x : ZMod 2 × ZMod 2) : ℂ :=
  match x.1.val, x.2.val with
  | 0, 1 => Complex.I
  | 1, 1 => -Complex.I
  | _, _ => 1

/-- Actual four-term finite phase, not a presumed Gauss-sum evaluation. -/
noncomputable def gammaFour4 (x : Eisenstein4) : ℂ :=
  (1 + Complex.I^((4-x.im.val)%4) + Complex.I^x.re.val +
    Complex.I^((x.im.val+4-x.re.val)%4))/2

def signClass4 (x y : ZMod 2 × ZMod 2) : ℤ :=
  (-1)^((x.1*y.2+x.2*y.1+x.2*y.2).val)

def reciprocityPhase4 (x y : Eisenstein4) : ℤ := signClass4 (squareClass4 x) (squareClass4 y)

def reduceEisenstein4 (x : EisensteinZ) : Eisenstein4 := ⟨x.re, x.im⟩

set_option maxRecDepth 4096 in
theorem eisenstein4_relation :
    (⟨0, 1⟩ : Eisenstein4)^2 + ⟨0, 1⟩ + 1 = 0 := by decide

set_option maxRecDepth 4096 in
theorem odd4_has_inverse : ∀ x : Eisenstein4, odd4 x → ∃ y : Eisenstein4, x*y = 1 := by decide

set_option maxRecDepth 4096 in
theorem odd4_card : Fintype.card {x : Eisenstein4 // odd4 x} = 12 := by decide

set_option maxRecDepth 4096 in
theorem squareClass4_mul : ∀ x y : Eisenstein4, odd4 x → odd4 y →
    squareClass4 (x*y) = squareClass4 x + squareClass4 y := by decide

set_option maxRecDepth 4096 in
theorem odd4_mul : ∀ x y : Eisenstein4, odd4 x → odd4 y → odd4 (x*y) := by decide

set_option maxRecDepth 4096 in
theorem squareClass4_kernel : ∀ x : Eisenstein4, odd4 x →
    (squareClass4 x = 0 ↔ ∃ y : Eisenstein4, odd4 y ∧ y^2 = x) := by decide

set_option maxHeartbeats 2000000 in
theorem gammaFour4_table (x : Eisenstein4) (hx : odd4 x) :
    gammaFour4 x = gammaClass4 (squareClass4 x) := by
  rcases x with ⟨a, b⟩
  fin_cases a <;> fin_cases b <;>
    norm_num [odd4, gammaFour4, squareClass4, gammaClass4, Complex.I_sq, ZMod.val_one, ZMod.val_natCast, ZMod.val, ZMod] at * <;> ring

set_option maxRecDepth 4096 in
theorem signClass4_bicharacter : ∀ x y z : ZMod 2 × ZMod 2,
    signClass4 (x+y) z = signClass4 x z * signClass4 y z ∧
    signClass4 x (y+z) = signClass4 x y * signClass4 x z ∧
    signClass4 x y = signClass4 y x := by decide

set_option maxRecDepth 4096 in
theorem signClass4_diagonal : ∀ x y : ZMod 2 × ZMod 2,
    signClass4 (x+y) (x+y) = signClass4 x x * signClass4 y y := by decide

theorem gammaClass4_refinement (x y : ZMod 2 × ZMod 2) :
    gammaClass4 (x+y) = gammaClass4 x * gammaClass4 y * (signClass4 x y : ℂ) := by
  have h2 : (2 : ZMod 2) = 0 := by decide
  have h3 : (3 : ZMod 2) = 1 := by decide
  rcases x with ⟨e, f⟩
  rcases y with ⟨g, h⟩
  fin_cases e <;> fin_cases f <;> fin_cases g <;> fin_cases h <;>
    norm_num [gammaClass4, signClass4, Complex.I_sq, ZMod.val_one, ZMod.val_natCast, ZMod.val_add, ZMod.val_mul, h2, h3] <;>
    norm_num [show (2 : ZMod 2).val = 0 by decide,
      show (3 : ZMod 2).val = 1 by decide]

theorem gammaFour4_refinement (x y : Eisenstein4) (hx : odd4 x) (hy : odd4 y) :
    gammaFour4 (x*y) = gammaFour4 x * gammaFour4 y * (reciprocityPhase4 x y : ℂ) := by
  rw [gammaFour4_table (x*y) (odd4_mul x y hx hy), squareClass4_mul x y hx hy,
    gammaClass4_refinement, gammaFour4_table x hx, gammaFour4_table y hy]
  rfl

theorem reduceEisenstein4_period (x z : EisensteinZ) :
    reduceEisenstein4 (x+4*z) = reduceEisenstein4 x := by
  have h4 : (4 : ZMod 4) = 0 := by decide
  ext <;> simp [reduceEisenstein4, QuadraticAlgebra.re_mul, QuadraticAlgebra.im_mul, QuadraticAlgebra.re_ofNat, QuadraticAlgebra.im_ofNat, h4]

theorem reciprocityPhase4_period (x y z w : EisensteinZ) :
    reciprocityPhase4 (reduceEisenstein4 (x+4*z)) (reduceEisenstein4 (y+4*w)) =
      reciprocityPhase4 (reduceEisenstein4 x) (reduceEisenstein4 y) := by
  rw [reduceEisenstein4_period, reduceEisenstein4_period]

#print axioms eisenstein4_relation
#print axioms odd4_has_inverse
#print axioms odd4_card
#print axioms squareClass4_mul
#print axioms odd4_mul
#print axioms squareClass4_kernel
#print axioms gammaFour4_table
#print axioms signClass4_bicharacter
#print axioms signClass4_diagonal
#print axioms gammaClass4_refinement
#print axioms gammaFour4_refinement
#print axioms reduceEisenstein4_period
#print axioms reciprocityPhase4_period
end GRHResearch.Analytic
