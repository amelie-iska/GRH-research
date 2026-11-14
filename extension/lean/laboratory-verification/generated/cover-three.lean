-- Generated from validated grh-lab-certificate-v1; no imported Lean code is executed.
-- Contract: quadratic-cover-v1
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

example : Matrix.det (FluidInterfaces.renormalizationMatrix ^ 3) = (14 : ℤ) ^ 3 ∧
    0 < Matrix.det (FluidInterfaces.renormalizationMatrix ^ 3) :=
  LaboratoryContracts.quadratic_cover_certificate 3

example : Matrix.det (FluidInterfaces.renormalizationMatrix ^ 3) = 2744 := by
  rw [FluidInterfaces.renormalization_power_determinant]
  norm_num

end LaboratoryInstance
