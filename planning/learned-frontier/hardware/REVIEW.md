# Source-based hardware review

Review date: 2026-11-04 UTC. The repository manifest pins all GitHub references;
the repository table links immutable README versions. Scope is the first 100
README lines plus the separately recorded source/license ranges. Paper scope is
abstract, title and version metadata. We did not install, build, reproduce
benchmarks, audit entire repositories, or run quantum/control hardware.

## AI-assisted and manually directed classical chip design

AlphaChip's public implementation is `google-research/circuit_training`.
Its input is a netlist/placement problem, with macro locations and orientations,
spacing/grid constraints, and wirelength/congestion/density proxy objectives.
It uses distributed reinforcement learning and can delegate standard-cell
placement to DREAMPlace. The README labels the implementation a research
project, specifies Linux, and explains its release/dependency expectations.
It supplies a component of physical design, not a netlist-independent invention
engine or a replacement for clocks, routing, extraction, signoff and fabrication.
Production use is an upstream claim; nothing here reproduces a TPU tapeout.
[AlphaChip README](https://github.com/google-research/circuit_training).

DREAMPlace uses differentiable placement optimization implemented through a
deep-learning toolkit. This does not make every optimized placement the output
of a learned policy. Its README provides CPU/GPU modes, placement papers and
benchmark-specific speed claims. OpenROAD and OpenROAD-flow-scripts (ORFS)
address a wider digital implementation flow, combining synthesis, floorplanning,
placement, clock-tree synthesis, routing and finishing. ORFS also explicitly
supports manually directed Tcl/Python intervention. Yosys, ABC and Chisel
provide synthesis, Boolean optimization/verification and parameterized RTL
construction respectively. They are useful baselines for carefully specified
datapaths even when no learning is involved. The term "manual baseline" should
mean a documented engineer-directed flow, not a deliberately weak placement.
[DREAMPlace](https://github.com/limbo018/DREAMPlace),
[ORFS](https://github.com/The-OpenROAD-Project/OpenROAD-flow-scripts),
[Yosys](https://github.com/YosysHQ/yosys).

The primary comparison needs both the AlphaChip result and the public
MacroPlacement reassessment. The latter's March 2026 revision documents
stronger simulated-annealing baselines, from-scratch and fine-tuned CT runs,
sub-10nm testcases and post-route PPA evaluation. Its repository's January 2026
update also describes CT-with-DREAMPlace results. These motivate matching
netlist, library, constraints, initialization, preprocessing, seeds, compute
budget and physical completion flow. Proxy cost alone is insufficient for a
claim about timing/power/area. This survey does not adjudicate every disputed
experimental choice or infer that one method dominates every technology.
[Updated assessment, v3](https://arxiv.org/abs/2302.11014v3),
[MacroPlacement](https://github.com/ABKGroup/MacroPlacement).

## Quantum chip geometry and classical control are different stages

The current `qiskit-community/qiskit-metal` README calls the project **Quantum
Metal**, formerly Qiskit Metal, and names the package `quantum-metal`. At the
pinned revision it still demonstrates `import qiskit_metal`. It distinguishes
headless geometry/GDS export, desktop GUI, meshing and Ansys integrations, whose
requirements differ. This is directly relevant to manual parametric transmon,
resonator, routing and packaging work. GDS export is not a fabrication process,
EM solution, Hamiltonian certification, coherence measurement or gate-fidelity
certificate. Commercial solver access remains separate from the software's
Apache-2.0 license. No existing project Qiskit environment was upgraded.
[Quantum Metal README](https://github.com/qiskit-community/qiskit-metal).

SQuADDS couples reusable superconducting layouts to simulation and target
parameter search. Its 2024 paper reports experimental agreement for many
database designs; the current repository still labels its software alpha.
Database validation does not validate a newly interpolated device or arbitrary
manufacturing stack. A practical learned-design experiment would compare a
surrogate's parameter proposals with a matched manual/optimizer baseline and
hold out geometry families, process corners and measured chips. Solver and
fabrication costs must be counted separately.
[SQuADDS paper](https://quantum-journal.org/papers/q-2024-09-09-1465/),
[SQuADDS repository](https://github.com/LFL-Lab/SQuADDS).

QICK supplies firmware, software and optional RF front ends for specified RFSoC
boards. It is classical electronics controlling and reading quantum devices.
Its README warns that development APIs and demo compatibility can change.
The October 2026 QICK Box preprint reports a modular front end and measurements
on a six-transmon device, not a new neural training ASIC. The 2025 QICK+hls4ml
paper demonstrates a much closer precedent for candidate C: quantization-aware
training, HLS conversion and a physically tested single-transmon readout model.
Its reported 32 ns classifier latency and 96% single-shot fidelity belong to
that experiment; they are not measurements of our reference or full host/QPU
round-trip latency. hls4ml describes FPGA inference and lists specific HLS
backends, which require their own toolchain availability.
[QICK Box v1](https://arxiv.org/abs/2610.03609v1),
[QICK+hls4ml v1](https://arxiv.org/abs/2501.14663v1),
[hls4ml](https://github.com/fastmachinelearning/hls4ml).

Qibolab supplies pulse/platform/instrument abstractions for self-hosted devices;
its usage example explicitly connects to instruments. Qiskit supplies circuits,
transpilation, operators and primitives; its current README also documents a C
API. Neither fact establishes a hard real-time bare-metal control path. The
GitHub `m-labs/artiq` README now points to a different repository host, so that
GitHub pin is evidence of a move, not evidence of the current ARTIQ control API.
We did not silently follow that move into an unpinned implementation.
[Qibolab paper](https://quantum-journal.org/papers/q-2024-02-12-1247/),
[Qiskit](https://github.com/Qiskit/qiskit),
[ARTIQ move](https://github.com/m-labs/artiq).

`baremetalQiskit` remains an unresolved public identifier. Any extension should
first identify its actual repository/license/version and then distinguish a
host-side compiler adapter from deterministic firmware. Candidate C provides
an offline frame/feature/action-request contract that could be adapted later;
it is not advertised as an implementation of an unknown upstream API.

## Tropical and hybrid accelerator evidence

The Tropical Attention primary paper is NeurIPS 2025, arXiv v2. Its public
implementation has real max-plus products, but the selected source also uses
ReLU, log1p, expm1 and an ordinary output linear layer. Its symmetric score
uses a max-minus-min projective distance; it is not simply conventional dot
product attention with softmax removed. A hardware implementation must specify
which score function it computes. Candidate A accepts already computed scores
and implements only the max-plus context. The newer repository backend routes
compatible inputs to `TensorBFS/tropical-gemm` with a PyTorch fallback; the
latter repository documents SIMD/CUDA, semiring variants and argmax tracking.
These are documented software capabilities, not synthesized ASIC PPA results.
[Tropical Attention v2](https://arxiv.org/abs/2505.17190v2),
[TropicalAttention.py at the audited pin](https://github.com/Baran-phys/Tropical-Attention/blob/e3c12f3e7c401245b9b5577d7181922b0150efc6/TropicalAttention.py),
[tropical-gemm](https://github.com/TensorBFS/tropical-gemm).

Tie differentiation is material: the selected PyTorch fallback uses `amax`,
whose reduction semantics must be matched when reproducing training. Our
reference explicitly selects the earliest-index witness and routes its integer
subgradient there. It therefore is not a claim of identical upstream training
gradients at tied maxima. Saturated outputs deliberately reject that backward
path until a quantization-gradient policy is chosen.

AdderNet's selected source computes negative L1 distances, not a max-plus
matrix product. Its backward method includes products, gradient normalization
and a square root; "no convolution multiplies" is not "no training multiplies."
Likewise MatMul-free LM is a distinct recurrent/ternary architecture and
bitnet.cpp is primarily a ternary inference engine. Their papers and code are
useful hardware/algorithm co-design comparators but cannot substitute for
tropical training evidence. The MatMul-free paper has evolved between the
2024 initial version and the audited 2025 v7; old FPGA power statements should
not be mixed with newer neuromorphic comparisons as one measurement.
[AdderNet paper](https://arxiv.org/abs/1912.13200),
[audited adder.py](https://github.com/huawei-noah/AdderNet/blob/2fb8aad20aa251a87480842ebea568372d5903a0/adder.py),
[MatMul-free LM v7](https://arxiv.org/abs/2406.02528v7),
[bitnet.cpp v1](https://arxiv.org/abs/2502.11880v1).

The 2021 tropical-backpropagation note is theoretical motivation. Its abstract's
constant-factor claim is not a manufactured training-chip result. Training
needs winner storage/recomputation, masked scatter reductions, optimizer state,
normalization, data movement and often ordinary multiplications. No universal
hardware or GRH speedup follows from replacing one primitive's multiply-accumulate
with add/compare. The architecture campaign specifies the measurements needed
to test a restricted benefit.
[Tropical backpropagation note](https://arxiv.org/abs/2101.00717v1).
