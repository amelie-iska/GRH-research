import Mathlib.Tactic

/-! Selected coefficient identities used by the written sl2/BGG example.
This is not a formalization of category O, an infinite Verma module, exactness
of the BGG resolution, Koszul duality, or any learned/physical model. -/
set_option autoImplicit false
namespace WorkbenchBGG

def eCoeff (lam i : ℤ) : ℤ := i * (lam - i + 1)

theorem sl2_commutator_coefficient (lam i : ℤ) :
    eCoeff lam (i+1) - eCoeff lam i = lam - 2*i := by
  unfold eCoeff
  ring

theorem twice_casimir_coefficient (lam i : ℤ) :
    2 * (eCoeff lam (i+1) + eCoeff lam i) + (lam-2*i)^2 = lam*(lam+2) := by
  unfold eCoeff
  ring

theorem reflected_casimir (lam : ℤ) :
    (-lam-2)*((-lam-2)+2) = lam*(lam+2) := by ring

theorem singular_coefficient (n : ℤ) : eCoeff n (n+1) = 0 := by
  unfold eCoeff
  ring

theorem singular_embedding_coefficient (n j : ℤ) :
    eCoeff n (n+1+j) = eCoeff (-n-2) j := by
  unfold eCoeff
  ring

theorem cutoff_defect (lam k : ℤ) :
    -eCoeff lam (k-1) - (lam-2*(k-1)) = k*(k-1-lam) := by
  unfold eCoeff
  ring

end WorkbenchBGG
#check WorkbenchBGG.sl2_commutator_coefficient
#check WorkbenchBGG.twice_casimir_coefficient
#check WorkbenchBGG.reflected_casimir
#check WorkbenchBGG.singular_coefficient
#check WorkbenchBGG.singular_embedding_coefficient
#check WorkbenchBGG.cutoff_defect
#print axioms WorkbenchBGG.sl2_commutator_coefficient
#print axioms WorkbenchBGG.twice_casimir_coefficient
#print axioms WorkbenchBGG.reflected_casimir
#print axioms WorkbenchBGG.singular_coefficient
#print axioms WorkbenchBGG.singular_embedding_coefficient
#print axioms WorkbenchBGG.cutoff_defect
