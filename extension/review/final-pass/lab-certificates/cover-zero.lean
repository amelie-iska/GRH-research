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

example : Matrix.det (FluidInterfaces.renormalizationMatrix ^ 0) = (14 : ℤ) ^ 0 ∧
    0 < Matrix.det (FluidInterfaces.renormalizationMatrix ^ 0) :=
  LaboratoryContracts.quadratic_cover_certificate 0

example : Matrix.det (FluidInterfaces.renormalizationMatrix ^ 0) = 1 := by
  rw [FluidInterfaces.renormalization_power_determinant]
  norm_num

end LaboratoryInstance
