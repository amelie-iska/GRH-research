# Quantum circuits on clean dessins and surface cellulations

`surface_codes.py` builds oriented surface cellulations, derives clean-dessin
permutations and CSS stabilizers, and emits actual preparation gates. The live
browser case is an **18-qubit [[18,2,3]] toric code**. Connected sums provide
**[[32,4,3]]** and **[[46,6,3]]** higher-genus codes with nonzero checks.

## Reproduce the certificates

Run from the repository root with Python 3 and NumPy installed:

```sh
python extension/quantum/surface_codes.py --site-data extension/site/data
```

The standard-library topology code checks:

- Ordered oriented face boundaries and two opposite incidences per edge.
- A single rotation cycle at every vertex and connectivity.
- Exact clean-dessin permutations and Euler characteristic.
- Sparse `H_X H_Z^T = 0` and exact binary ranks.
- Code distance by increasing-weight exhaustive search for the four small cases.
- The deterministic RREF/Hadamard/CNOT preparation specification.

The NumPy validation then executes the 18-qubit gates on a full complex128
state vector, compares every amplitude to an independently constructed row-space
state, measures all stabilizer expectations, and checks the four-parameter
variational circuit on all 16 binary inputs. It does not merely evaluate the
analytic prediction in place of a circuit.

`--skip-cpu` regenerates only the exact topology and circuit data. The already
recorded `cpu-validation.json` is not overwritten in that mode.

## Cases

| ID | Data qubits | Genus | Logical qubits | Distance | Encoder |
|---|---:|---:|---:|---:|---:|
| `torus3x3` | 18 | 1 | 2 | 3 | 8 H + 34 CX |
| `torus3x5` | 30 | 1 | 2 | 3 | 14 H + 60 CX |
| `genus2_3x3` | 32 | 2 | 4 | 3 | 13 H + 69 CX |
| `genus3_3x3` | 46 | 3 | 6 | 3 | 18 H + 116 CX |
| `torus32x32` | 2048 | 1 | 2 | 32 by theorem | omitted for sparse execution |

The first four distance certificates are exhaustive through weight three. The
large rectangular-torus distance follows from the proved winding-number bound.
Higher-genus coordinates are gluing charts, not an asserted smooth embedding or
an explicit numerical uniformization of the associated Belyi pair.

## Shared circuit and topology contract

Every manifest contains `id`, `n`, `genus`, `vertices`, `edges`, `faces`,
`x_checks`, `z_checks`, `metadata`, and `prepare_circuit`. Each check has an `id`
and a `qubits` support. Integer qubit `q` is **bit q** in an array basis index.

Single-qubit gate:

```json
{"gate":"RY","target":2,"qubits":[2],"angle":0.3}
```

CNOT:

```json
{"gate":"CX","control":2,"target":9,"qubits":[2,9]}
```

The gate alphabet is `H`, `X`, `Z`, `CX`, `RY`, `RZ`. Rotation definitions are
`RY(t)=exp(-i*t*Y/2)` and `RZ(t)=exp(-i*t*Z/2)`.

`permutations` gives `sigma0`, `sigma1`, `sigma_infinity`, and
`face_permutation`. Composition is right to left and
`sigma0 * sigma1 = face_permutation`. The involution `sigma1` has no fixed
points. Qubits are the original edges/white midpoint vertices, **not all darts**:
there are `2*n` darts and the Belyi degree is `2*n`.

`preparation.rref_generators` and `preparation.pivots` specify the exact row-space
basis. The prepared state is the uniform positive sum over `row(H_X)`, normalized
by `2^(-rankX/2)`. Its logical Z eigenvalues are all +1. The RREF encoder is not
claimed to be a nearest-neighbor hardware compilation.

## Sparse API for large GPU cases

```python
from surface_codes import torus_checks
x_supports, z_supports = torus_checks(256, 256)
```

This constructs only sparse checks for 131,072 data qubits. It does not allocate
a state vector, a dense matrix, or a generic tableau. With `nv=lx*ly`, the indexing
is `h(x,y)=y*lx+x`, `v(x,y)=nv+y*lx+x`, with periodic coordinates. Each support has
four entries. Use the proved ranks `nv-1` for both types if exact elimination is
unnecessary; label this as a theorem-based rank, not an executed elimination.

`square_torus(lx,ly,...)` generates geometry and permutation manifests as well,
and `connected_sum(left,right,...)` explicitly glues two disk boundaries. These
full manifests are intended for small and medium cases.

## Variational circuit

The ordered patch is the first star, `[0,2,9,15]`. Prepare the encoded state,
apply `RY(sign_i*pi/2 + theta_i)` to each patch qubit, then CX from patch qubits
1,2,3 into patch qubit 0, and read Z on patch qubit 0. Its proved expectation is

`product(signs) * product(cos(theta_i))`.

This is an original pedagogical surface-local correlator with four parameters.
It does not implement the multiscale QCNN of Cong–Choi–Lukin, a trained decoder,
or a demonstrated quantum advantage. Its simple analytic baseline is intentional
and provides an independent check of actual circuit execution.

## Completed GPU experiments

The authorized workstation executed these experiments on 13 November 2026
using an NVIDIA GeForce RTX 4090, cuQuantum Python 26.11.0, cuStateVec 1.15.1,
cuStabilizer 0.5.0, and CuPy 14.2.0. `results/gpu-results.json` retains the
original nine experiments. `results/capacity-results.json` records a separate
two-experiment followup, with the seed, memory policy, library path, source
hashes, case hashes, and unchanged-input check. Both runs passed.

| Representation and workload | Data qubits | Ancillas | Shots | Dominant stored data | Apply/preparation interval | Timed body |
|---|---:|---:|---:|---:|---:|---:|
| Dense complex64 torus 3×3 | 18 | 0 | exact expectation | 2 MiB state | 0.000312 s preparation | 0.000537 s |
| Dense complex64 torus 3×5 | 30 | 0 | exact expectation | 8 GiB state | 0.918804 s preparation | 1.204211 s |
| Dense complex64 plus syndrome ancilla | 30 | 1 | exact expectation | 16 GiB state | 1.838463 s preparation | 2.528538 s |
| Genus-two Pauli frames | 32 | 30 | 32,768 | 630,784 bytes estimated tables | 0.004756 s apply | 3.025362 s |
| Genus-three Pauli frames, followup | 46 | 42 | 32,768 | 892,928 bytes estimated tables | 0.002198 s apply | 0.081878 s |
| Torus 32×32 Pauli frames | 2,048 | 2,048 | 32,768 | 40 MiB estimated tables | 0.005072 s apply | 0.013088 s |
| Torus 128×128 Pauli frames | 32,768 | 32,768 | 32,768 | 640 MiB estimated tables | 0.073878 s apply | 0.165669 s |
| Torus 512×512 Pauli frames | 524,288 | 524,288 | 32,768 | 10 GiB estimated tables | 1.147181 s apply | 2.693085 s |
| Torus 640×640 Pauli frames, followup | 819,200 | 819,200 | 32,768 | 15.625 GiB estimated tables | 1.791833 s apply | 4.327947 s |

The largest tested frame workload has **1,638,400 total data-plus-ancilla
qubits per frame**, at 32,768 frames. Its full function call, including topology
generation and cleanup, took 4.813268 s. All 3,355,443,200 packed syndrome bytes
were checked against sparse GF(2) propagation, with zero mismatches. This is a
bounded tested workload under the recorded policy, not an absolute universal
qubit maximum. Changing the shot count or representation changes capacity.

The frame backend propagates Pauli errors relative to an **assumed ideal encoded
CSS reference with all listed checks +1**. It does not construct or evolve that
reference's amplitude vector. Data X and Z errors each occur independently with
probability 0.001; ancillas and extraction gates are ideal. Measured frame bits
represent sign changes relative to the deterministic ideal outcomes. The check
validates syndrome extraction; no recovery algorithm or logical error rate is
measured.

Timing definitions matter. Dense preparation times include synchronization;
their body timer begins after state allocation. Frame apply times are
synchronized wall intervals around circuit application, including host dispatch,
not isolated CUDA kernel timings. Frame body times include setup and syndrome
verification but omit topology generation and cleanup. The new full-call timer
includes those two operations, but not interpreter startup or result-file
serialization. Table-memory estimates are analytic, not measured peak VRAM.

### Variational training result

The actual 18-qubit GPU circuit was trained for 24 parameter-shift updates at
learning rate 0.2 on four parity inputs. MSE decreased from
`0.21987940665826008` to `0.0027618471230164243`. The maximum training-history
discrepancy from the exact analytic expectation was `3.09201986903318e-7`.
All 16 final input signs were correct, including the 12 inputs omitted from
updates. The initial angles already gave correct thresholded signs on every
input: training improved expectation calibration, not classification accuracy.
The implied ideal single-shot parity success probability rose from about
0.76554 to 0.97372; these are Born-rule deductions, not sampled frequencies.

### Reproduction and evidence integrity

Use a compatible CUDA installation and the package versions in the records.
The original run was:

```sh
python extension/quantum/gpu_experiments.py --mode all --max-frame-lattice 512 --output new-gpu-results.json
```

The separate adaptive followup is:

```sh
python extension/quantum/gpu_capacity.py --output new-capacity-results.json
```

Run one GPU process at a time. The followup fixes 32,768 shots and chooses the
largest lattice side divisible by 32 for which `1.25 * estimated_tables` fits
after a 2 GiB reserve. It refuses to overwrite its existing output and never
overwrites the original experiment record. The actual source imports
`frame_case` and `environment` from the unchanged original script.

`results/gpu-results-remote-original.json` is the byte-exact first-run record
whose hash appears under `results/gpu-results.json` in the followup's remote
input ledger. The ordinary local `gpu-results.json` has identical parsed data
with harmless numeric-formatting differences from its original transfer; it
was preserved. All script and case hashes in the ledger match the local files.
The followup's raw JSON is also copied to `extension/site/data` for the UI.

## Evidence boundaries

These mathematical results are proved in `quantum-surfaces.tex`; the JSON
certificates and Python checks are executable verification, not Lean proofs of
the whole quantum formalism. GPU execution reports identify the actual backend,
precision, hardware, measured workload and timings separately. A large
stabilizer/Pauli-frame run is not a generic state-vector computation, and syndrome
generation without recovery is not an error-correction performance result.

## Recreate the executed Python environment

Use Python 3.12 and a compatible NVIDIA driver. Create a project-local virtual environment, install the exact recorded package set with `python -m pip install -r extension/quantum/requirements-gpu.lock`, then invoke the selected interpreter through `extension/quantum/run_gpu.py experiments --mode all` or `extension/quantum/run_gpu.py capacity`. The launcher adds only that environment’s wheel library directories to the child process library path; it changes no global shell or driver settings. The original recorded scripts and their hashes remain unchanged. The launcher itself is a convenience wrapper, not an additional GPU benchmark.
