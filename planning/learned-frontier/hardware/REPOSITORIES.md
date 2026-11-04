# Pinned public repository survey

All twenty repositories were resolved through unauthenticated public GitHub HTTPS.
The JSON manifest records exact retrieval timestamps, full 40-character commits,
document hashes and reviewed ranges. The table links immutable reviewed README
versions. Status labels mean documented upstream availability, not locally reproduced
functioning, release assurance, a full code audit or an endorsement.

| Repository / pinned README | Stage | Core license classification | Audited availability and limit |
|---|---|---|---|
| [google-research/circuit_training](https://github.com/google-research/circuit_training/blob/c417a3a13f40867b649c719c03daaf1b39a909bc/README.md) (`c417a3a13f40`) | AI macro floorplanning | Apache-2.0 | Research release; Linux; TF-Agents; placement-cost binary and external components must be checked |
| [The-OpenROAD-Project/OpenROAD](https://github.com/The-OpenROAD-Project/OpenROAD/blob/f131605002c80444f79b18e95e0c7cb657ec024d/README.md) (`f131605002c8`) | Digital physical implementation | BSD-3-Clause | Documented open flow; no local build or post-route result |
| [The-OpenROAD-Project/OpenROAD-flow-scripts](https://github.com/The-OpenROAD-Project/OpenROAD-flow-scripts/blob/3ff0197f070c65f2dd8ec10b06d1fdcb3bc3c993/README.md) (`3ff0197f070c`) | RTL-to-GDS flow and manual intervention | NOASSERTION | License API says NOASSERTION; per-file/platform/tool/PDK terms require review |
| [limbo018/DREAMPlace](https://github.com/limbo018/DREAMPlace/blob/6627f3327e6cc17db7782c0b90073a498531ca3c/README.md) (`6627f3327e6c`) | Analytic/differentiable CPU/GPU placement | BSD-3-Clause | Documented software; benchmark claims not rerun |
| [ABKGroup/MacroPlacement](https://github.com/ABKGroup/MacroPlacement/blob/20eddb6b35232e86e6008b9deec8da77633a2f07/README.md) (`20eddb6b3523`) | Public baselines and CT reassessment | BSD-3-Clause | Includes 2026 update; commercial-tool results require separate access |
| [berkeley-abc/abc](https://github.com/berkeley-abc/abc/blob/0d3399a4d62f6fe56851206f480e7328ff2f3748/README.md) (`0d3399a4d62f`) | Boolean synthesis and formal verification | NOASSERTION | Custom permissive copyright.txt inspected; API NOASSERTION |
| [YosysHQ/yosys](https://github.com/YosysHQ/yosys/blob/b8d84f8235d3f04af7ad669fac111740612fe7ba/README.md) (`b8d84f8235d3`) | Scripted RTL synthesis | ISC | ISC core; third-party libraries retain their licenses |
| [qiskit-community/qiskit-metal](https://github.com/qiskit-community/qiskit-metal/blob/911b3e835a8fd4a4348a098f4b58f6b982363895/README.md) (`911b3e835a8f`) | Quantum-device geometry / EM interfaces | Apache-2.0 | Current name Quantum Metal; package quantum-metal; existing import qiskit_metal; solver requirements separate |
| [openquantumhardware/qick](https://github.com/openquantumhardware/qick/blob/80753a9c55142f00b00bc236d91074b5901d9743/README.md) (`80753a9c5514`) | RFSoC quantum control/readout | MIT | Firmware/software/front-end; board and calibration required for execution |
| [m-labs/artiq](https://github.com/m-labs/artiq/blob/7d7b85f377e0c172ae3496f0c03cfb6cb85ba022/README.rst) (`7d7b85f377e0`) | Repository-move evidence | LGPL-3.0 | Pinned README only points to git.m-labs.hk; no current control API audit |
| [fastmachinelearning/hls4ml](https://github.com/fastmachinelearning/hls4ml/blob/3c0bef2782846e93a41399fa3ec4d13633c39559/README.md) (`3c0bef278284`) | ML-to-HLS FPGA inference | Apache-2.0 | Source documented; specific HLS toolchains remain separate |
| [qiboteam/qibolab](https://github.com/qiboteam/qibolab/blob/8c94a22dfca49e97ae83d77fc2e2ae018397fcd4/README.md) (`8c94a22dfca4`) | Self-hosted pulse/platform drivers | Apache-2.0 | Usage connects to lab instruments; not run here |
| [huawei-noah/AdderNet](https://github.com/huawei-noah/AdderNet/blob/2fb8aad20aa251a87480842ebea568372d5903a0/README.md) (`2fb8aad20aa2`) | Negative-L1 neural primitive | BSD-3-Clause | Research demo; selected backward source contains products and normalization |
| [ridgerchu/matmulfreellm](https://github.com/ridgerchu/matmulfreellm/blob/8222c153636c04bc322f1c99d927ff4499c40a06/README.md) (`8222c153636c`) | Ternary/recurrent LM implementation | Apache-2.0 | Research implementation; not max-plus and not local hardware/training evidence |
| [microsoft/BitNet](https://github.com/microsoft/BitNet/blob/0b341e582afbf9e1011f24744b554c96a3477eb5/README.md) (`0b341e582afb`) | Ternary CPU/GPU inference | MIT | Actual inference code documented; hardware claims scoped to upstream evaluations |
| [chipsalliance/chisel](https://github.com/chipsalliance/chisel/blob/09c18756161d41fe52f3dfb07bdcd580d3f10d0a/README.md) (`09c18756161d`) | Parameterized HDL generation | Apache-2.0 | Manual construction route; does not itself supply a completed chip |
| [Qiskit/qiskit](https://github.com/Qiskit/qiskit/blob/fd49574ec08b43a942c9b06609575841a06f567f/README.md) (`fd49574ec08b`) | Quantum circuits/transpilation/primitives and C API | Apache-2.0 | SDK capability does not imply deterministic device control |
| [LFL-Lab/SQuADDS](https://github.com/LFL-Lab/SQuADDS/blob/185f4e6cb013bb1e0421dc780e3df750b1befca7/README.md) (`185f4e6cb013`) | Device database, simulation and target matching | MIT | Repository marks alpha; new design needs own simulation/measurement |
| [Baran-phys/Tropical-Attention](https://github.com/Baran-phys/Tropical-Attention/blob/e3c12f3e7c401245b9b5577d7181922b0150efc6/README.md) (`e3c12f3e7c40`) | Tropical/projective attention research | MIT | Selected full 98-line kernel read; ordinary output linear and transcendental maps remain |
| [TensorBFS/tropical-gemm](https://github.com/TensorBFS/tropical-gemm/blob/75f5799a91eb8b72c0b535307ea396160865ee9a/README.md) (`75f5799a91eb`) | SIMD/CUDA tropical matrix primitives | MIT | README documents semirings/argmax; no source/build/performance verification |

Core license classifications come from GitHub metadata except the separately
inspected ABC copyright notice. They do not license all dependencies, checkpoints,
datasets, fonts, firmware components, process libraries, binaries or proprietary
EDA integrations. NOASSERTION is unresolved classification, not evidence of either
permission or a prohibited use. No upstream source has been incorporated into the
reference designs; those are original integer specifications.

`baremetalQiskit`: exact-spelling public GitHub repository search returned zero
matches at the manifest timestamp. Identity, version, implementation and licensing
remain unresolved. A private repository or alternate spelling is possible.

Repository moves and release-name changes were kept as findings instead of
silently substituting an unrelated project.
