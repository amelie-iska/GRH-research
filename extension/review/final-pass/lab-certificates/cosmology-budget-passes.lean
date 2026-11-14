-- Generated from validated grh-lab-certificate-v1; no imported Lean code is executed.
-- Contract: cosmology-calibration-v1
-- Check with the pinned project: cd extension/lean && lake env lean -DwarningAsError=true LaboratoryInstance.lean
import BridgeTheorems
import FluidInterfaces
import WeightedGainContracts
import LaboratoryContracts
import CosmologyCalibration
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FinCases

open Matrix
open scoped BigOperators
namespace LaboratoryInstance

open MeasureTheory

-- Conditional on actual measurable scores, integrability and the stated true
-- moment bound. No PRNG law, Gaussian moment identity or observational model
-- is proved by these numerical literals. Choose the threshold before testing.
example {Ω : Type*} [MeasurableSpace Ω]
    (μ : Measure Ω) [IsProbabilityMeasure μ] (score : Fin 288 → Ω → ℝ)
    (hmeas : ∀ j, Measurable (score j))
    (hint : ∀ j, Integrable (fun ω => |score j ω| ^ (2 * 8)) μ)
    (hmoment : ∀ j, (∫ ω, |score j ω| ^ (2 * 8) ∂μ) ≤ ((81081000000648648000002270268000004540536000005675670000004540536000002270268000000648648000000081081 : ℝ) / 40000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)) :
    μ.real (CosmologyCalibration.scanEvent (Finset.univ : Finset (Fin 288)) score ((6 : ℝ) / 1)) ≤ ((1 : ℝ) / 20) := by
  have h := CosmologyCalibration.scan_even_moment_threshold μ
    (Finset.univ : Finset (Fin 288)) score 8 ((6 : ℝ) / 1) ((81081000000648648000002270268000004540536000005675670000004540536000002270268000000648648000000081081 : ℝ) / 40000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000) ((1 : ℝ) / 20)
    (by norm_num) (by intro j _; exact hmeas j)
    (by intro j _; exact hint j) (by intro j _; exact hmoment j) (by norm_num)
  exact h.2

-- Exact rank arithmetic only; no probability law for the stored rank is asserted.
example : CosmologyCalibration.rankFraction 4095 1892 = ((1893 : ℚ) / 4096) := by
  norm_num [CosmologyCalibration.rankFraction]

example : 0 < CosmologyCalibration.rankFraction 4095 1892 ∧
    1 / ((4095 : ℚ) + 1) ≤ CosmologyCalibration.rankFraction 4095 1892 ∧
    CosmologyCalibration.rankFraction 4095 1892 ≤ 1 :=
  CosmologyCalibration.rank_fraction_bounds 4095 1892 (by norm_num)

end LaboratoryInstance
