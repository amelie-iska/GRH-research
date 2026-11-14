-- Generated from validated grh-lab-certificate-v1; no imported Lean code is executed.
-- Contract: weighted-gain-v1
-- Check with the pinned project: cd extension/lean && lake env lean -DwarningAsError=true LaboratoryInstance.lean
import BridgeTheorems
import FluidInterfaces
import WeightedGainContracts
import LaboratoryContracts
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FinCases

open Matrix
open scoped BigOperators
namespace LaboratoryInstance

def G : Matrix (Fin 2) (Fin 2) ℚ := !![((1 : ℚ) / 4), ((3 : ℚ) / 2); ((3 : ℚ) / 32), ((1 : ℚ) / 4)]
def w : Fin 2 → ℚ := ![((4 : ℚ) / 1), ((1 : ℚ) / 1)]
def q : ℚ := ((3 : ℚ) / 5)

theorem positive_weights : ∀ i, 0 < w i := by
  intro i
  fin_cases i <;> norm_num [w]

example : (∀ i, (G *ᵥ w) i / w i ≤ q) ↔ (∀ i, (G *ᵥ w) i ≤ q * w i) :=
  WeightedGainContracts.row_ratio_iff G w q positive_weights

-- This proposed bound fails; the exact violated row is certified instead.
example : q * w 0 < (G *ᵥ w) 0 := by
  norm_num [G, w, q, Matrix.mulVec, dotProduct, Fin.sum_univ_two]

end LaboratoryInstance
