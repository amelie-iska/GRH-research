-- Generated from validated grh-lab-certificate-v1; no imported Lean code is executed.
-- Contract: hodge-family-v1
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

example : ResearchBridge.hodgeMatrix ((1 : ℝ) / 1) 0 0 1 = !![((1 : ℝ) / 1) ^ 2, 0; 0, 1] ∧
    (∀ a b : ℝ, ((1 : ℝ) / 1) ^ 2 * (a ^ 2 + b ^ 2) ≤ ResearchBridge.hodgeEnergy ((1 : ℝ) / 1) 0 0 1 a b) ∧
    (0 < ((1 : ℝ) / 1) ^ 2 ↔ ((1 : ℝ) / 1) ≠ 0) :=
  LaboratoryContracts.hodge_family_certificate ((1 : ℝ) / 1) (by norm_num) (by norm_num)

example (a b : ℝ) : (ResearchBridge.hodgeMatrix ((1 : ℝ) / 1) 0 0 1 *ᵥ ![a, b] = 0) ↔
    ((((1 : ℝ) / 1) = 0 ∨ a = 0) ∧ b = 0) :=
  LaboratoryContracts.hodge_family_kernel ((1 : ℝ) / 1) a b

example : ((1 : ℝ) / 1) ^ 2 > 0 := by norm_num

example : ((1 : ℝ) / 1) ^ 2 = ((1 : ℝ) / 1) := by norm_num

end LaboratoryInstance
