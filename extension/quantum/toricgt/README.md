# Trainable quantum features for a small ToricGT graph model

This directory contains an actual jointly trained **three-qubit-per-token** quantum feature model, matched classical and frozen-feature comparators, exact token-path certificates, independent references, and a full browser inference implementation.

The nine reported runs used **PyTorch CUDA statevector simulation** on an RTX 4090. They did not run on a quantum computer and did not use cuStateVec for training. The separate surface-code experiments in the parent directory use different circuits and backends. No quantum advantage is established here.

The original ToricGT ingredients retained are vertex/edge tokens, endpoint incidence, mixed softmax/max-plus attention, and four Soft-MoE experts with two slots each. This is a bounded original extension of those ingredients, not a reproduction of the full upstream language-model or proposed ToricBLM program. Source pins and corrections are documented in [the source review](../../review/quantum-toricgt/review.md).

## Measured outcome

The model learns weighted shortest-path values on fixed-vocabulary tokenization DAGs. A legal tokenization is a path through byte boundaries. An independent integer-potential checker certifies optimality when a candidate attains a feasible lower bound; exact dynamic programming repairs uncertified outputs.

All statistics below are means ± sample standard deviations across seeds 17, 29, and 43. Ordinary test strings have length 4–8; the length-shift set has length 9–12. Each set contains 128 graphs.

| Variant | Trainable parameters | Test optimal proposal | Longer-string optimal proposal | Test mean cost regret |
|---|---:|---:|---:|---:|
| Trainable quantum | 25,515 | 83.85% ± 2.39 pp | 54.69% ± 3.41 pp | 0.0386 |
| Classical trigonometric features | 25,515 | 84.38% ± 0.78 pp | 50.00% ± 4.75 pp | 0.0356 |
| Frozen quantum encoder | 25,449 | 83.07% ± 1.97 pp | 52.86% ± 0.90 pp | 0.0399 |

One reported cost unit is the cost of a byte fallback (16 integer units). The network predicts distances divided by 32. The matched classical model is slightly better on ordinary-test proposal accuracy and regret; the trainable quantum model is somewhat better on those means for longer strings. Frozen quantum features have a slightly lower mean longer-string node RMSE than the trainable quantum encoder. Three seeds on one synthetic task do not establish a general ordering.

Final certified accuracy after exact repair is 100% for every reported split and run. That guarantee belongs to the separate dynamic program and checker; it is **not** the neural model's proposal accuracy. The JSON records retain every original proposal, regret, certificate, and repair flag.

The twelve trained circuit offsets change by Euclidean norms 0.146, 0.151, and 0.158. They remain unchanged in the frozen ablation, which also freezes the 54-parameter angle encoder. The measured maximum PyTorch allocation was 183,426,048 bytes, approximately 175 MiB. A batch of 32 graph forwards took about 2.56 ms for the quantum model and 1.81 ms for the classical model. These measurements exclude data preparation and exact repair. They do not establish a speed advantage over dynamic programming.

## Architecture and conventions

Each graph token has eight attributes: vertex/edge indicators, two intrinsic byte positions, token span, edge cost, control, and edge-cost slope. Endpoint equality produces an incidence matrix invariant under a coordinated renaming. Arbitrary learned vertex-ID embeddings are not used. Intrinsic positions travel with tokens under storage permutations.

The angle encoder computes `pi*tanh(W*x+b)` with six outputs. Each of two circuit layers applies RY then RZ to each of three qubits, followed by CNOT 0→1 and CNOT 1→2. Qubit 0 is the most significant bit. Twelve shared offsets have shape `[2][3][2]`, with the final axis indexing RY and RZ. Input angles are reused in both layers.

The finite Weyl clock and backward shift have dimension eight:

- `U[j,j] = exp(2*pi*i*j/8)`;
- `V |j> = |j-1 mod 8>`;
- `VU = exp(2*pi*i/8) UV`.

Six real features are the real and imaginary parts of expectations of U, V, and UV. The graph model has width 24, two attention heads, two blocks, and a scalar per-token readout. Node targets alone contribute to loss. The task uses the whole observed graph and is not autoregressive language modeling.

The classical comparator replaces the six expectation features by six bounded sine/cosine features with twelve learned phases. All other dimensions, data, seed, ordering, optimizer, and training schedule match. The frozen ablation deliberately has fewer trainable parameters.

## Files and evidence

| File | Role |
|---|---|
| `data.py` | Dataset generator, integer dynamic program, independent path certificate, learned proposal, small colored-flow LP |
| `model.py` | PyTorch model and batched differentiable circuit |
| `reference.py` | Independent dense NumPy Kronecker implementation and shift Jacobian |
| `verify.py` | Circuit/gradient/chain-rule, permutation, padding, routing, exact path, and rational-dual checks |
| `train.py` | Predeclared three-seed protocol, validation selection, complete metrics, non-pickle checkpoints |
| `reference.js` | Standalone circuit and parameter-shift reference |
| `graph-reference.js` | Entire selected trained model in JavaScript, including path certificates and repair |
| `verify-reference.mjs` | Independent JavaScript versus NumPy circuit comparison |
| `verify-graph-reference.mjs` | Full model comparison against saved GPU outputs on four held-out graphs |
| `algebra_checks.py` | Exact finite checks accompanying the three source qualifications |
| `data/dataset-v1.json` | Fixed 896-graph dataset, with 512/128/128/128 split counts |
| `results/training-v1/` | All nine checkpoints, histories, losses, predictions, certificates, protocol, and aggregate results |
| `results/cuda-verification-final.json` | Actual final CUDA verification, fixtures, exact LP certificate, and source hashes |
| `results/browser-*.json` | Compact benchmark, four graph examples, weights, and circuit/full-forward verification |

The dataset SHA-256 is `4147088938a0742d956aceb7e50a3c7206d349b8f1196cb7a3b6fefb1a774156`. All 896 underlying strings are distinct. The training manifest hashes its five Python source files and the exact dataset. Subsequent documentation and browser additions are not retrospectively claimed as training inputs.

Independent GPU checks found maximum state and feature discrepancies below 4.5e-16 against NumPy, a shift/autograd Jacobian discrepancy below 3.4e-16, and a full nonlinear-loss chain-rule discrepancy below 1.2e-16. Those are numerical results on finite tests. The associated analytic identities are proved separately in the manuscript. In particular, parameter shift is applied to feature expectations and then composed with the classical adjoint; shifting the whole nonlinear loss is generally incorrect.

## Reproduction

Use a project-local environment with NumPy and SciPy for the exact/reference checks, and PyTorch for the model. The recorded GPU environment was Python 3.11.6, NumPy 2.4.6, SciPy 1.17.1, PyTorch 2.8.0+cu128, CUDA runtime 12.8. No global package modification is required. The fixed dataset is supplied so regeneration across library versions is unnecessary.

From this directory:

```bash
python verify.py --numpy-only --output results/recheck-numpy.json
python verify.py --device cuda --output results/recheck-cuda.json
node verify-reference.mjs results/numpy-verification.json
node verify-graph-reference.mjs
python algebra_checks.py
```

The reported experiment can be repeated into a **new** output directory:

```bash
python train.py --dataset data/dataset-v1.json \
  --output results/reproduction-1 --device cuda \
  --seeds 17,29,43 --modes quantum,classical,frozen --epochs 80
```

`train.py` refuses to overwrite an existing run directory, uses two CPU threads, and caps its own CUDA allocator at 10% of device memory. The scripts do not stop or alter other jobs. `--device cpu` is supported, but CPU timing is a different measurement. The recorded checkpoints use `.npz` arrays loaded with `allow_pickle=False` in the export procedure.

## Browser API

The browser needs `reference.js`, `graph-reference.js`, and the JSON weights. It needs no Python runtime, network inference service, or GPU backend.

```javascript
import {runGraph} from './graph-reference.js';
const graph = graphs.cases[0].graph; // browser-graphs.json
const theta = structuredClone(weights.state_dict.theta);
theta[0][0][0] += 0.4;
const result = runGraph(graph, weights, theta);
```

`runGraph(graph, weights, thetaOverride=null)` returns:

```text
predictionsNormalized: number[token]
predictedDistancesUnits: number[vertex]
angles: number[token][6]
features: number[token][6]
tokenInfo: vertex/edge metadata[token]
blocks: attention scores, weights, mixture, dispatch, combine
pathResult: proposal, regret, initial certificate, repair flag, certified path
```

Graph examples use ASCII strings over a–d of length at most 12, integer-cost forward edges, intrinsic byte positions, and recorded control/slope attributes. Every nonterminal vertex must reach the final boundary. This API is intended for the bounded experiment domain; arbitrary larger graph families are not validated by its four full-forward test cases.

The JavaScript implementation recomputes the full graph prediction after a theta change. It uses double arithmetic and an error-function approximation for GELU. Four held-out graph comparisons have maximum normalized node error 6.81e-7 against saved PyTorch float32 GPU predictions, with matching learned paths and final certificates. The selected checkpoint was chosen by validation loss. Recorded graph predictions remain available for provenance, but the interactive forward pass does not substitute them for live computation.

## Proof and application boundaries

The manuscript contains seventeen elementary proofs, including Bellman optimality, path and LP dual certificates, finite Weyl relations, feature bounds, the single-occurrence parameter-shift rule, its hybrid chain rule, graph equivariance, binomial path kernels, constrained rewrites, affine margins, and source counterexamples. Their presence does not assert that these entire claims have been formalized in Lean. The repository's Lean inventory remains authoritative for exactly mapped declarations.

The trained circuit preserves state normalization. The classical checker preserves legal tokenization and verifies optimality. These are separate guarantees. The chapter's feasible-Hilbert-space theorem describes a possible future constraint-preserving quantum interface under explicit commuting-projector hypotheses; it is not a property silently attributed to this three-qubit token encoder.

No result here establishes improved Shor complexity, a cryptographic break, a general graph-grammar decision procedure, continuum Yang–Mills theory, a mass gap, cosmological evidence, or a validated biological design model. The concrete deliverable is the trained finite model, measured comparisons, proved interfaces, and independently checkable outputs.
