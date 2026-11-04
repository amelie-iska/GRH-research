# Quantum-feature TokenGT and finite physical exploration

This original, small CPU prototype trains four models on the exact same
`outputs/experiments/actual-rg/dataset.json` split: 120 training, 40 heldout,
40 out-of-distribution examples. The teacher is actual black-spin decimation
of the clean-dessin incidence graph K₂,₅. All 32 white-spin logweights,
including the constant coefficient, are prediction targets. This is a
three-control family of physical actions, not the space of all 32 independent
coarse couplings.

The physical input contains seven spin-node tokens and ten incidence-edge
tokens, plus one masked padding position. Each token explicitly carries its
type and endpoint metadata through the angle map. Three **auxiliary** qubits
encode each token: RY(data), fixed RZ rotations, CNOT01, CNOT12, fixed RX
rotations. Six Z/ZZ expectations form classical features. Q/K/V and a small
nonlinear readout are trained with Autograd. The quantum circuit parameters
are frozen; no joint circuit training, hardware or quantum advantage is
claimed. A separate literal replay of the immutable elliptic theta fixture
is included, with its original hash and explicit representational boundary.

The four variants share initialization, data, batches, optimizer, parameter
count (1,076), training steps and head dimensions. Softmax, max-plus tropical
and half-softmax/half-tropical variants use the quantum feature map; the
matched classical hybrid uses six local sine/cosine features. Exact classical
teacher cost and the frozen feature-map cost are not a speed advantage claim.
At the saved seed the classical baseline performs better than every quantum
variant on heldout full-logweight RMSE. No statistical significance is claimed
from one seed. Training, heldout and OOD metrics, including derived logZ,
retained magnetizations, probability TV and the constant coefficient, are
stored separately. The scalar target normalization uses training rows only.

A learned three-direction basis and classifier optimize a defined
**variational mutual-information lower bound**. C is uniform over six
(direction, sign) codes. The random embedding change is
Δ=tanh(.3z+.7 sign(C) B_direction(C))−tanh(.3z).
The loss is CE(C, critic(Δ))+.08||BBᵀ−I||², with normalized basis rows.
The reported log6−CE is an empirical heldout estimate of the variational
lower-bound functional for I(C;Δ) under this intervention distribution. It is
not a certified population-MI lower bound without sampling uncertainty control.
It measures code recoverability, not proven semantic
interpretability; calling fixed basis vectors independent random variables
would be incorrect. This is GraphCG-inspired, not a reproduction of the
paper's pretrained molecular models or its benchmarks.

The forest evaluates 61 candidates, branching along both signs of the
learned directions with a width-three beam and depth four. A ridge decoder
maps pooled embeddings to physical couplings. Every candidate is scored by
**exact** coarse logZ and the five retained magnetizations. This finite latent
optimization does not claim human or language-model reasoning.

The analogy task learns a mean displacement from transformed training pairs
and transfers it to 40 heldout base embeddings, using a fixed parameter shift
(.07, −.04, .06) clipped to the training domain. The decoded parameters are
fed back into the exact teacher, and both transferred and no-transfer controls
are measured. Persistent H₁ is computed by actual boundary-column reduction
over F₂ on the complete Rips 2-skeleton of 12 heldout six-dimensional learned
embeddings. Additional target and transferred **physical observable** point
clouds use scaled coordinates (logZ/3, m₀/.25, …, m₄/.25); their barcodes and
pairwise distance error are saved. These are finite geometric diagnostics,
not a proof of analogy, homological mirror symmetry or topological order.

The continuous GFlowNet has time-expanded state space {(t,x): t=1,2,3,
x∈R²}, a root point mass at x=0, Lebesgue state measures elsewhere and
termination at t=3. Its forward MLP gives Gaussian means and learned
diagonal standard deviations. Backward kernels at t=2,3 are normalized
Brownian-bridge Gaussians with mean ((t−1)/t)x_t and covariance
((t−1)/(3t))I; the last backward step is the unit root point mass.
The trajectory balance residual is

```
logZ_parameter + Σ log p_F − Σ log p_B − log R(x_3).
```

The positive integrable reward is
exp(−||x||²/2+.35(logZ_K₂,₅(.62+.35tanh x₀,.58+.34tanh x₁,.12)−7)).
The physical logZ factor is bounded since the controls range in a compact
set; the confining Gaussian makes the reward integrable. The model trains
1,800 steps on 10,000 fixed continuous off-policy Gaussian trajectories.
Fresh heldout-proposal and on-policy TB errors are saved. Ten thousand new
terminal samples are compared on a20×20 histogram grid on [−5,5]²
(cell width.5). The separate normalizer quadrature uses a201×201 grid at
spacing.05. Both grids are evaluation only, never the state space or policy.
The histogram TV is an approximate diagnostic, not a certified total
variation distance between continuous measures; quadrature omits tails.

Actual QEC is demonstrated independently: a Bell-reference qubit plus three
encoded data qubits, independent BitFlip channels, parity projectors,
conditional corrective X operations, decode and trace. PennyLane's actual
mixed-state noise density is compared against an independent sum of eight
error patterns. The recovered logical error matches 3p²−2p³ and the
entanglement fidelity matches 1−3p²+2p³. This repetition code corrects one
X error under ideal correction, with no phase-error protection or universal
fault tolerance. It is not a topological quantum code.

## Run and inspect

The approved existing environment and its
`examples/quantum/requirements-cpu.lock` are used without installing packages.
No imports train models, access the network or modify existing data.

```
.tools/book-quantum-cpu/bin/python examples/quantum_tokengt/check.py
.tools/book-quantum-cpu/bin/python examples/quantum_tokengt/train.py --run NEW_UNIQUE_RUN
.tools/book-quantum-cpu/bin/python examples/quantum_tokengt/export_traces.py
.tools/book-quantum-cpu/bin/python examples/quantum_tokengt/export_components.py
.tools/book-quantum-cpu/bin/python examples/quantum_tokengt/check_saved.py
node --check web/qtoken.mjs
```

The trainer refuses to reuse a named output directory. It records every
optimizer step, final parameters, seeds, training-only normalization, input
hashes, source hashes and exact limits. Previous failed and smoke run
directories remain preserved. Successful saved runs contain
`trained-models.json`, `record.json`, and `manifest.json`. The active web
manifest selects a content-addressed record; older generations remain intact.
The prediction and component exporters together add six trained-replay DAGs under the same
collection manifest, retaining the full original experiment record pointer.
It replays a token's gate states and verifies PennyLane agreement plus all
17 scalar attention rows. After a new training run, rerun the exporter.

[Interactive lab](http://127.0.0.1:8765/qtoken.html) and
[3D tensor inspector](http://127.0.0.1:8765/architecture.html?collection=qtoken&trace=quantum-tokengt-rg-hybrid)
load local arrays only. The concept basis, quantum token features, Q/K/V,
scores, weights and context can be read as literal tables. Primary reference
versions and actual read scope are recorded in `sources.json`.

No full upstream TokenGT/GraphCG campaign, coherent quantum attention,
physical topological phase, Fukaya/HMS equivalence, materials discovery,
quantum hardware/GPU/non-Gaussian backend or arithmetic GRH bridge is claimed.

A separate exact cellular CSS diagnostic runs with `python examples/quantum_tokengt/cellular_code.py`. On the actual one-face genus-two clean cellulation, ten edge qubits and vertex/face checks give rank(HX)=6, rank(HZ)=0 and an exact [[10,4,1]] code (X-distance1, Z-distance4). The single face has zero F₂ boundary. This is an executed example showing why genus alone supplies no useful memory protection; it is distinct from the three-qubit repetition channel. Results: `outputs/checks/2026-11-03-actual-rg/quantum-tokengt/cellular-css.json`.

## Executed QEC layer within token inference

`qec_layer.py` inserts an ideal quantum memory channel after each token's
prepared three-qubit feature state and before feature measurement. Each of
these three logical qubits is separately encoded/recovered using the checked
three-bit repetition block. For independent physical X probability p, the
recovered logical channel has f(p)=3p²−2p³; two ideal concatenation levels give
f(f(p)). A measured Z product of weight w attenuates by (1−2p_eff)^w. This
channel identity holds for entangled logical feature states: disjoint blocks
with independent noise yield a tensor product of recovered logical channels.

The unchanged softmax, tropical and hybrid heads are evaluated on all40
heldout physical inputs for p∈{0,.02,.05,.1,.2} at levels0,1,2. Their physical
resources are3,9,27qubits per token. Complete predicted actions, logZ and
retained-observable errors, TV and identity-coefficient error are saved in a
separate content-addressed sidecar selected by `manifest.qec_layer`. At p=.1,
hybrid full-action RMSE changes from.89766 without encoding to.31589 with one
ideal recovery level and.10608 with two; its clean baseline is.10125. The
improvement here is ideal memory-noise suppression, not a quantum advantage
against the classical clean comparator.

Seventy-five explicit eight-logical-error density mixtures on actual saved
feature states agree with feature attenuation to4.45e-16. An independent
complete prediction replay uses density mixtures instead of attenuation and
checks the physical metrics in all45model/noise/level cases. The original
trained record and checkpoints remain byte-identical. No9/27-qubit noisy-gate
simulation is claimed: the larger encoding/recovery blocks are represented
by their analytically derived and Bell-reference-checked logical channels.
Encoding gates, syndrome measurements, correction and decoding are ideal;
correlated noise, phase errors and fault-tolerant computation are not covered.

```
.tools/book-quantum-cpu/bin/python examples/quantum_tokengt/check_qec_layer.py
.tools/book-quantum-cpu/bin/python examples/quantum_tokengt/qec_layer.py --run NEW_UNIQUE_LAYER_RUN
.tools/book-quantum-cpu/bin/python examples/quantum_tokengt/check_qec_layer_saved.py
```

After creating a new training run, rerun `export_traces.py`, then create a new
QEC-layer evaluation for that run. The UI verifies both sidecar checksum and
its source-record hash before displaying the layer table and error curves.

## Component architectures in the tensor inspector

The collection also contains `quantum-tokengt-rg-concept-critic` and
`quantum-tokengt-rg-continuous-gfn`. Both replay the original saved trained
parameters, without new optimization or checkpoint edits. The concept DAG
shows the explicit seeded random intervention code, normalized basis,
nonlinear change, critic logits/softmax, code CE and Gram penalty. Its heldout
240-code replay matches the saved empirical variational-MI functional; this
sample estimate is not a certified population-MI lower bound. The GFN DAG
shows all three actual forward MLP passes, learned diagonal Gaussian scales,
saved innovations/states, continuous forward/backward densities, root point
mass, exact physical terminal reward and scalar TB residual. Latent axes
are explicitly distinct from physical spin sites and quiver vertices. No
quantum gates are fabricated for either classical learned component.

`export_traces.py` exports the four prediction DAGs. Then append the two
component traces, preserving the four prediction entries, with
`python examples/quantum_tokengt/export_components.py`. Rebuilding all six
therefore requires both exporters in that order. Focused replay tests:
`python examples/quantum_tokengt/check_components.py`.
