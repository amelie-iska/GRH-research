import Std.Tactic

/-! Exact obstructions to specific claims in the source manuscripts.
No analytic statement about zeta functions is asserted in this module. -/
namespace GRHResearch

/-- If a geodesic had norm 2 its integral trace would satisfy this impossible equation. -/
theorem no_integral_trace_norm_two (t : Int) : 2 * (t * t) ≠ 9 := by
  omega

/-- The integral trace equation forced by an integer hyperbolic norm is impossible.
The geometric derivation remains in prose; this arithmetic obstruction is universal. -/
theorem no_integer_norm_trace_equation (n t : Int) (hn : 1 < n) :
    n * (t * t) ≠ (n + 1) * (n + 1) := by
  intro h
  simp only [Int.add_mul, Int.mul_add, Int.one_mul, Int.mul_one] at h
  have hprod : n * (t * t - n - 2) = 1 := by
    simp only [Int.mul_sub]
    omega
  have hdiv : n ∣ 1 := ⟨t * t - n - 2, hprod.symm⟩
  have hle : n ≤ 1 := Int.le_of_dvd (by decide) hdiv
  omega

/-- Degrees of arbitrary integral combinations of even-degree characters remain even. -/
def cyclicDegrees : List Int → Int
  | [] => 0
  | a :: xs => 2 * a + cyclicDegrees xs

theorem cyclicDegrees_even (xs : List Int) : ∃ k : Int, cyclicDegrees xs = 2 * k := by
  induction xs with
  | nil => exact ⟨0, rfl⟩
  | cons a xs ih =>
    obtain ⟨k, hk⟩ := ih
    refine ⟨a + k, ?_⟩
    simp only [cyclicDegrees, hk]
    omega

theorem no_integral_cyclic_induction_degree_one (xs : List Int) : cyclicDegrees xs ≠ 1 := by
  obtain ⟨k, hk⟩ := cyclicDegrees_even xs
  omega

/-- Integer matrices are represented by their four entries in row order. -/
structure Mat2 where
  a : Int
  b : Int
  c : Int
  d : Int
  deriving DecidableEq, Repr

def mul (x y : Mat2) : Mat2 :=
  ⟨x.a*y.a+x.b*y.c, x.a*y.b+x.b*y.d,
   x.c*y.a+x.d*y.c, x.c*y.b+x.d*y.d⟩
def det (x : Mat2) : Int := x.a*x.d-x.b*x.c

theorem symmetrization_changes_determinant :
    det ⟨1,-1,1,1⟩ = 2 ∧ det ⟨1,0,0,1⟩ = 1 := by decide

/-- A degree-two unipotent matrix need not have exponent at most two. -/
theorem unipotence_does_not_bound_exponent :
    mul ⟨1,1,0,1⟩ ⟨1,1,0,1⟩ ≠ ⟨1,0,0,1⟩ := by decide

/-- Upper-Iwahori shift witness after clearing denominators: S E12 S = E21. -/
theorem iwahori_shift_witness :
    mul (mul ⟨0,2,1,0⟩ ⟨0,1,0,0⟩) ⟨0,2,1,0⟩ = ⟨0,0,1,0⟩ := by decide

#print axioms no_integral_trace_norm_two
#print axioms no_integer_norm_trace_equation
#print axioms cyclicDegrees_even
#print axioms no_integral_cyclic_induction_degree_one
#print axioms symmetrization_changes_determinant
#print axioms unipotence_does_not_bound_exponent
#print axioms iwahori_shift_witness
end GRHResearch
