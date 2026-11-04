import Mathlib.Analysis.Complex.Basic
import Mathlib.Algebra.BigOperators.Field
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace GRHResearch.ShortRowPairBarrier
open Finset
noncomputable section
attribute [local instance] Classical.propDecidable
variable {U I : Type*} [Fintype U] [Fintype I]

def columnGram (A : U → I → ℂ) (i j : I) : ℂ :=
  ∑ u, A u i * star (A u j)
def rowGram (A : U → I → ℂ) (u v : U) : ℂ :=
  ∑ i, A u i * star (A v i)

theorem frame_potential_duality (A : U → I → ℂ) :
    (∑ i, ∑ j, ‖columnGram A i j‖ ^ 2) =
      ∑ u, ∑ v, ‖rowGram A u v‖ ^ 2 := by
  have hc : (∑ i, ∑ j, columnGram A i j * star (columnGram A i j)) =
      ∑ u, ∑ v, rowGram A u v * star (rowGram A u v) := by
    have ec (i j : I) : columnGram A i j * star (columnGram A i j) =
        ∑ u, ∑ v, (A u i * star (A u j)) * (star (A v i) * A v j) := by
      simp only [columnGram, star_sum, star_mul', star_star]
      rw [Finset.sum_mul]
      apply Finset.sum_congr rfl
      intro u _
      rw [Finset.mul_sum]
    have er (u v : U) : rowGram A u v * star (rowGram A u v) =
        ∑ i, ∑ j, (A u i * star (A v i)) * (star (A u j) * A v j) := by
      simp only [rowGram, star_sum, star_mul', star_star]
      rw [Finset.sum_mul]
      apply Finset.sum_congr rfl
      intro i _
      rw [Finset.mul_sum]
    simp_rw [ec, er]
    calc
      _ = ∑ i, ∑ u, ∑ j, ∑ v,
          (A u i * star (A u j)) * (star (A v i) * A v j) := by
            apply Finset.sum_congr rfl
            intro i _
            rw [Finset.sum_comm]
      _ = ∑ u, ∑ i, ∑ v, ∑ j,
          (A u i * star (A u j)) * (star (A v i) * A v j) := by
            rw [Finset.sum_comm]
            apply Finset.sum_congr rfl
            intro u _
            apply Finset.sum_congr rfl
            intro i _
            rw [Finset.sum_comm]
      _ = ∑ u, ∑ v, ∑ i, ∑ j,
          (A u i * star (A u j)) * (star (A v i) * A v j) := by
            apply Finset.sum_congr rfl
            intro u _
            rw [Finset.sum_comm]
      _ = _ := by
            apply Finset.sum_congr rfl
            intro u _
            apply Finset.sum_congr rfl
            intro v _
            apply Finset.sum_congr rfl
            intro i _
            apply Finset.sum_congr rfl
            intro j _
            ring
  have hn (z : ℂ) : (z * star z).re = ‖z‖ ^ 2 := by
    rw [Complex.star_def, Complex.mul_conj]
    simp only [Complex.ofReal_re, Complex.normSq_eq_norm_sq]
  have hr := congrArg Complex.re hc
  simpa only [Complex.re_sum, hn] using hr

theorem row_diagonal_lower (A : U → I → ℂ) :
    (∑ u, ‖rowGram A u u‖ ^ 2) ≤ ∑ i, ∑ j, ‖columnGram A i j‖ ^ 2 := by
  classical
  rw [frame_potential_duality]
  apply Finset.sum_le_sum
  intro u _
  exact Finset.single_le_sum (fun v _ => sq_nonneg ‖rowGram A u v‖) (Finset.mem_univ u)

/-- Each row may have its own nonnegative weight, forced by squared norms. -/
theorem weighted_pair_square_lower (A : U → I → ℂ) (w : U → ℝ)
    (hw : ∀ u i, ‖A u i‖ ^ 2 = w u) :
    (Fintype.card I : ℝ) ^ 2 * (∑ u, w u ^ 2) -
        (Fintype.card I : ℝ) * (∑ u, w u) ^ 2 ≤
      ∑ i, ∑ j, if i = j then 0 else ‖columnGram A i j‖ ^ 2 := by
  classical
  have hc (i : I) : columnGram A i i = ((∑ u, w u : ℝ) : ℂ) := by
    simp only [columnGram]
    calc
      _ = ∑ u, ((w u : ℝ) : ℂ) := by
        apply Finset.sum_congr rfl
        intro u _
        rw [Complex.star_def, Complex.mul_conj]
        rw [Complex.normSq_eq_norm_sq, hw]
      _ = _ := by push_cast; rfl
  have hr (u : U) : rowGram A u u = (((Fintype.card I : ℝ) * w u) : ℂ) := by
    simp only [rowGram]
    calc
      _ = ∑ i : I, ((w u : ℝ) : ℂ) := by
        apply Finset.sum_congr rfl
        intro i _
        rw [Complex.star_def, Complex.mul_conj]
        rw [Complex.normSq_eq_norm_sq, hw]
      _ = _ := by simp
  have hd : (∑ i, ∑ j, ‖columnGram A i j‖ ^ 2) =
      (∑ i, ∑ j, if i = j then 0 else ‖columnGram A i j‖ ^ 2) +
      (Fintype.card I : ℝ) * (∑ u, w u) ^ 2 := by
    calc
      _ = ∑ i, ((∑ j, if i = j then 0 else ‖columnGram A i j‖ ^ 2) +
          ‖columnGram A i i‖ ^ 2) := by
        apply Finset.sum_congr rfl
        intro i _
        calc
          _ = ∑ j, ((if i = j then 0 else ‖columnGram A i j‖ ^ 2) +
              (if i = j then ‖columnGram A i j‖ ^ 2 else 0)) := by
                apply Finset.sum_congr rfl
                intro j _
                by_cases hij : i = j <;> simp [hij]
          _ = _ := by rw [Finset.sum_add_distrib]; simp
      _ = _ := by
        rw [Finset.sum_add_distrib]
        simp only [hc, Complex.norm_real, Real.norm_eq_abs, sq_abs, Finset.sum_const,
          Finset.card_univ, nsmul_eq_mul]
  have h := row_diagonal_lower A
  have he : (∑ u, ‖rowGram A u u‖ ^ 2) =
      (Fintype.card I : ℝ) ^ 2 * ∑ u, w u ^ 2 := by
    simp only [hr, norm_mul, Complex.norm_real, Real.norm_eq_abs, mul_pow, sq_abs]
    rw [Finset.mul_sum]
  rw [he, hd] at h
  linarith

/-- In a short ball below prime column norm all original character zeros are absent. -/
theorem unimodular_pair_square_lower (A : U → I → ℂ)
    (hA : ∀ u i, ‖A u i‖ = 1) :
    (Fintype.card I : ℝ) * (Fintype.card U : ℝ) *
        ((Fintype.card I : ℝ) - (Fintype.card U : ℝ)) ≤
      ∑ i, ∑ j, if i = j then 0 else ‖columnGram A i j‖ ^ 2 := by
  have h := weighted_pair_square_lower A (fun _ => 1) (by intros; rw [hA]; norm_num)
  simp only [one_pow, Finset.sum_const, Finset.card_univ, nsmul_eq_mul, mul_one] at h
  nlinarith

#check frame_potential_duality
#check row_diagonal_lower
#check weighted_pair_square_lower
#check unimodular_pair_square_lower
#print axioms frame_potential_duality
#print axioms row_diagonal_lower
#print axioms weighted_pair_square_lower
#print axioms unimodular_pair_square_lower
end
end GRHResearch.ShortRowPairBarrier
