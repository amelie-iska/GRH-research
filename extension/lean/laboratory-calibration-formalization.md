# Laboratory instances and finite-search probability contracts

This continuation adds **ten registered declarations**: four in
[`LaboratoryContracts.lean`](LaboratoryContracts.lean) and six in
[`CosmologyCalibration.lean`](CosmologyCalibration.lean). The complete current
extension audit contains **131 declarations in nine modules**. Its actual
printed types and axiom dependencies appear in
[`final-verification/verification.json`](final-verification/verification.json),
[`LaboratoryContracts.log`](final-verification/LaboratoryContracts.log), and
[`CosmologyCalibration.log`](final-verification/CosmologyCalibration.log).
Every reported dependency is among `propext`, `Classical.choice`, and
`Quot.sound`. No additional theorem declaration is counted for a generated
concrete laboratory instance or an executable regression check.

The compiler is Lean 4.24.0, revision
`797c613eb9b6d4ec95db23e3e00af9ac6657f24b`; mathlib is pinned to
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. The preceding
121-declaration manifest is preserved at project commit
`6838f5292b345fc5eff4f2bc2109dc5b46a9a8b8`.

## Exact live-laboratory contracts

| Declaration | Proved conclusion | Required interpretation boundary |
|---|---|---|
| `LaboratoryContracts.hodge_family_certificate` | For real `0 ≤ ε ≤ 1`, the existing Hodge matrix is `diag(ε²,1)`, its existing quadratic energy is at least `ε²(a²+b²)`, and `ε² > 0` iff `ε ≠ 0`. | The domain restriction makes `ε²` the appropriate lower coercivity constant. Exact rational controls can be embedded in the real theorem. A logarithmic floating control is not silently treated as an exact rational parameter. |
| `LaboratoryContracts.hodge_family_kernel` | The actual matrix kills `(a,b)` iff `(ε = 0 or a = 0)` and `b = 0`. | This completely describes the coordinates of the kernel. The theorem does not separately assert a computed `finrank` or validate a browser eigensolver. |
| `LaboratoryContracts.quadratic_cover_certificate` | For every natural `k`, `det(J^k) = 14^k > 0` for the original integer matrix `J = [[3,1],[1,5]]`. | The matrix identity does not itself formalize the topological torus-cover theorem, a complete fibre list, or a browser point-map implementation. |
| `LaboratoryContracts.square_perturbation_bound` | From `|e| ≤ d`, derive `|(B+e)²−B²| ≤ d(2|B|+d)`. | A spatial, temporal, curvature, or measurement model must separately supply the additive error premise. No trigonometric Taylor remainder or continuum limit is formalized by this declaration. |

The Hodge and determinant proofs import and reuse the original definitions and
theorems in `BridgeTheorems` and `FluidInterfaces`. The verification driver
freshly compiles those imports into an isolated temporary directory, then
checks all registered theorem types and foundational dependencies. It records
the imported source hashes and checks that they remain unchanged throughout
the run. Cached mathlib imports and the pinned compiler remain part of the
declared trusted environment.

## A genuine measure-theoretic false-positive bound

Let `μ` be a probability measure on a measurable space `Ω`, let `S` be a fixed
finite test family, and let `X_j : Ω → ℝ` be its score functions. The formal
event is

\[
E_t=\{\omega:\exists j\in S,\ t\le X_j(\omega)\}.
\]

This is exactly the mathematical event that a maximum over the declared finite
family meets or exceeds a common threshold. The use of `≤` includes ties. The
browser's finite scan is a maximum of positive matched-filter scores, rather
than a maximum of their absolute values.

`finite_family_false_positive_bound` starts with measurable events `E_j` and
per-test bounds `μ.real(E_j) ≤ b_j`, and proves measurability of their finite
union together with

\[
\mu(E)\le\min\left(1,\sum_{j\in S}b_j\right).
\]

The stronger `scan_even_moment_bound` derives the per-test bounds from actual
moment assumptions. For a fixed natural `k`, assume `t > 0`, measurability of
each `X_j`, integrability of `|X_j|^(2k)`, and

\[
\int |X_j|^{2k}\,d\mu\le M_j.
\]

If `t ≤ X_j`, then `t^(2k) ≤ |X_j|^(2k)`. Applying Markov's integral inequality
to that nonnegative power gives the per-test tail bound; finite subadditivity
then proves

\[
\mu(E_t)\le\min\left(1,\frac{\sum_{j\in S}M_j}{t^{2k}}\right).
\]

The formal proof uses the pinned mathlib definitions and proofs of
[`mul_meas_ge_le_integral_of_nonneg`](https://github.com/leanprover-community/mathlib4/blob/f897ebcf72cd16f89ab4577d0c826cd14afaafc7/Mathlib/MeasureTheory/Integral/Bochner/Basic.lean)
and
[`measureReal_biUnion_finset_le`](https://github.com/leanprover-community/mathlib4/blob/f897ebcf72cd16f89ab4577d0c826cd14afaafc7/Mathlib/MeasureTheory/Measure/Real.lean).
The new proof constructs the score-event inclusion and combines these results;
it does not assume the desired full-scan conclusion.

`scan_uniform_even_moment_bound` specializes to a common moment bound `M`:

\[
\mu(E_t)\le\min\left(1,\frac{|S|M}{t^{2k}}\right).
\]

`scan_even_moment_threshold` consumes the exact scalar inequality

\[
|S|M\le\alpha\,t^{2k}
\]

and concludes `μ.real(E_t) ≤ α`, retaining all of the measurable-score,
integrability, and true-moment premises. A runtime rational witness can verify
this finite scalar inequality. The generated Lean specialization keeps the
probability space and moment premises visible.

No independence between the `288` score functions is needed. The natural
parameter also allows `k = 0`, which gives a typically trivial bound; the live
interface restricts attention to positive moment orders. The theorem concerns
a fixed statistic and threshold. Additional data-dependent searches or a
threshold chosen after inspecting the same data need their own analysis.

### The Gaussian model remains an explicit application obligation

The accompanying runtime application may declare an ideal model `Y = L ξ`
with independent standard-normal coordinates of `ξ`, exact finite coefficients
in `L`, and fixed filters `w_j`. Its finite arithmetic can bound
`||Lᵀ w_j||²` by an outward rational variance `v`. The additional Gaussian
moment identity supplies the candidate

\[
M=(2k-1)!!\,v^k.
\]

This module does **not** formalize the Gaussian moment identity, establish the
independent-normal law of `ξ`, certify a numerical pseudorandom generator, or
identify an observed sky with the declared null model. Those are explicit
conditions for applying the checked moment theorem. Correlation between
filters is compatible with the finite-union proof.

## Exact calibration ranks have a separate status

`rankFraction B E` is the rational number `(1+E)/(B+1)`.
`rank_fraction_bounds` proves, from the legitimate-count condition `E ≤ B`,

\[
0<\frac{1+E}{B+1},\qquad
\frac1{B+1}\le\frac{1+E}{B+1}\le1.
\]

`rank_fraction_threshold_iff` proves the exact denominator-clearing rule for
comparison with a rational level `α`. These declarations match the arithmetic
of the stored `4095`-draw calibration and its `>=` exceedance count. They do not
prove the binary-search implementation or the probability law of that count.

A fixed archive of pseudorandomly generated maxima is not itself an abstract
exchangeable sample theorem. Neither rank arithmetic nor a finite validation
rejection fraction proves that the rank is a valid p-value for every future
data-generating process. Exchangeability, sampling, statistic selection, and
the relationship to a physical null must be supplied separately.

## Replay and negative controls

[`verify_laboratory_contracts.py`](verify_laboratory_contracts.py) compiles the
actual fixed-template exports emitted by the browser bridge, using freshly
built current project imports. It binds the generator, theorem sources,
compiler, dependency manifest, generated source bytes, and output logs by
SHA-256. Its negative controls require rejection of false mathematical goals,
rather than accepting a missing-import or syntax failure as a successful test.
The results live in
[`laboratory-verification/verification.json`](laboratory-verification/verification.json).

```sh
python extension/lean/verify_laboratory_contracts.py \
  --toolchain /absolute/path/to/lean-4.24.0-linux \
  --mathlib /absolute/path/to/mathlib4-v4.24.0 \
  --generated-dir /absolute/path/to/generated-fixed-template-exports
```

The generic probability and laboratory declarations are kernel checked. The
browser replays exact contract instances and exports Lean source; the browser
does not run a Lean kernel. Source/type hashes identify the intended theorem
and assumptions but do not turn arbitrary JavaScript execution into a formal
proof. All conclusions remain finite or explicitly conditional; this work
does not establish a Millennium-problem solution, a physical cosmological
detection, or a general cryptographic security theorem.
