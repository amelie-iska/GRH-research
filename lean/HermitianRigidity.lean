import Mathlib.Analysis.SpecialFunctions.Pow.Complex
import Mathlib.Analysis.Complex.OpenMapping
import Mathlib.Analysis.Complex.ReImTopology
import Mathlib.LinearAlgebra.Matrix.Hermitian

open Set Complex

namespace GRHResearch.Analytic

/-- A real-valued holomorphic function is constant on a connected open set. -/
theorem real_valued_holomorphic_constant {U : Set ℂ} {f : ℂ → ℂ}
    (hU : IsOpen U) (hc : IsPreconnected U) (hf : DifferentiableOn ℂ f U)
    (hreal : ∀ z ∈ U, (f z).im = 0) {x y : ℂ} (hx : x ∈ U) (hy : y ∈ U) :
    f x = f y := by
  rcases (hf.analyticOnNhd hU).is_constant_or_isOpen hc with ⟨c, hconst⟩ | hopen
  · exact (hconst x hx).trans (hconst y hy).symm
  · have himage : f '' U ⊆ Complex.im ⁻¹' ({0} : Set ℝ) := by
      rintro w ⟨z, hz, rfl⟩
      exact hreal z hz
    have hi : interior (Complex.im ⁻¹' ({0} : Set ℝ)) = ∅ := by
      rw [Complex.interior_preimage_im, interior_singleton]
      simp
    have hsub : f '' U ⊆ interior (Complex.im ⁻¹' ({0} : Set ℝ)) := by
      rw [← (hopen U Subset.rfl hU).interior_eq]
      exact interior_mono himage
    rw [hi] at hsub
    exact False.elim (hsub (mem_image_of_mem f hx))

/-- Two holomorphic functions related by conjugation must be constant. -/
theorem conjugate_holomorphic_pair_constant {U : Set ℂ} {f g : ℂ → ℂ}
    (hU : IsOpen U) (hc : IsPreconnected U)
    (hf : DifferentiableOn ℂ f U) (hg : DifferentiableOn ℂ g U)
    (hconj : ∀ z ∈ U, g z = star (f z))
    {x y : ℂ} (hx : x ∈ U) (hy : y ∈ U) : f x = f y := by
  have hu : ∀ z ∈ U, (f z + g z).im = 0 := by
    intro z hz
    simp [hconj z hz]
  have hv : ∀ z ∈ U, (I * (f z - g z)).im = 0 := by
    intro z hz
    simp [hconj z hz, Complex.mul_im]
  have hsum := real_valued_holomorphic_constant hU hc (hf.add hg) hu hx hy
  have hmul := real_valued_holomorphic_constant hU hc
    ((hf.sub hg).const_mul I) hv hx hy
  have hdiff : f x - g x = f y - g y := mul_left_cancel₀ I_ne_zero hmul
  apply Complex.ext
  · have h1 := congrArg Complex.re hsum
    have h2 := congrArg Complex.re hdiff
    simp only [Pi.add_apply, Complex.add_re, Complex.sub_re] at h1 h2
    linarith
  · have h1 := congrArg Complex.im hsum
    have h2 := congrArg Complex.im hdiff
    simp only [Pi.add_apply, Complex.add_im, Complex.sub_im] at h1 h2
    linarith

/-- Entrywise holomorphic, pointwise Hermitian matrix families are constant.
No statement about families that are Hermitian only on a real parameter line is made. -/
theorem holomorphic_hermitian_family_constant {ι : Type*} {U : Set ℂ}
    {H : ℂ → Matrix ι ι ℂ} (hU : IsOpen U) (hc : IsPreconnected U)
    (hentry : ∀ i j, DifferentiableOn ℂ (fun z => H z i j) U)
    (hHermitian : ∀ z ∈ U, (H z).IsHermitian)
    {x y : ℂ} (hx : x ∈ U) (hy : y ∈ U) : H x = H y := by
  ext i j
  apply conjugate_holomorphic_pair_constant hU hc (hentry i j) (hentry j i) ?_ hx hy
  intro z hz
  simpa only [Complex.star_def] using ((hHermitian z hz).apply j i).symm

#print axioms real_valued_holomorphic_constant
#print axioms conjugate_holomorphic_pair_constant
#print axioms holomorphic_hermitian_family_constant
end GRHResearch.Analytic
