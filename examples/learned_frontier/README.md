# Learned physics, width limits and quantum geometry

This extension has executed numerical models and exact algebraic examples.
It does not prove GRH or formalize the whole new chapter in Lean.
The canonical interactive lab is http://127.0.0.1:8765/learned.html and the
existing tensor inspector accepts `?collection=frontier` for all five new
checkpoint architectures, including the coherent purification circuit.

## What is executed

- Twelve trained GPU hybrid runs: diffusion and conditional flow matching,
  matched entangled/product four-qubit circuits, three fixed seeds. The target
  is the dequantized two-black-spin measurement marginal of the actual
  seven-spin quantum Gibbs state on the genus-two clean dessin incidence graph.
- One trained coherent four-qubit purification-flow model, two system and two
  ancilla qubits. It uses full known target purifications; it is not universal
  denoising or tomography from samples. All33 tested grid states are retained.
- Real cuStateVec and cuTensorNet execution at7/11/23qubits, tied to genus2/4/10
  clean-dessin physical circuits. The23qubit case is untrained and checked by
  norm and inverse echo; independent dense NumPy reference only through11qubits.
- A specified frozen one-qubit-feature infinite-width/RBF/readout limit,
  exact32configuration classical RG action fits, tropical bounds and discrete
  finite-field coefficient learners with reversible complex-Hilbert oracles.
- Actual infinite genus-two polynomial path-module resolutions, Hom/Ext/Tor,
  graph covers, Frobenius pants gluing/heralding and CHSH exact calculations.
- Three executable digital accelerator/control references, twenty pinned
  repositories and13primary hardware papers. No synthesis, fabrication, PPA,
  RF feedback or physical quantum processor is claimed.

The two RG teachers differ: the width experiment eliminates classical black
spins and retains all32white configurations; the generative experiment traces
quantum white spins and retains the two black spins. Neither is replaced by an
unrelated compression proxy. Incidence sites, quiver vertices and auxiliary
feature wires are distinct objects.

## Linux GPU reproduction

Host alias: `iska-linux-vscode`. Snapshot/working root:
`/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104`.
The Mac project is preserved. Copied macOS environment binaries are archives,
not runnable Linux environments. Do not clean or upgrade either source copy.

The existing `tokengt` environment was used unchanged (Torch2.8.0+cu128).
Run from the Linux project root, always with a new output directory:

```sh
/home/iska/miniconda3/envs/tokengt/bin/python examples/learned_frontier/generative.py --device cuda --steps 2000 --output outputs/experiments/learned-frontier/new-generative-run
/home/iska/miniconda3/envs/tokengt/bin/python examples/learned_frontier/controls.py --seed 20261105 --output outputs/experiments/learned-frontier/new-seed-run
/home/iska/miniconda3/envs/tokengt/bin/python examples/learned_frontier/state_flow.py --output outputs/experiments/learned-frontier/new-stateflow-run
/home/iska/miniconda3/envs/tokengt/bin/python examples/learned_frontier/check_generative.py --device cuda --output outputs/checks/new-generative-checks.json
```

The user-approved new cuQuantum environment is separate. See
`envs/grh-cuda12-linux-64.lock` and
`planning/learned-frontier/GPU_ENVIRONMENT.md` for the exact resolved packages,
installation history and primary NVIDIA/CuPy setup references. Recreate a NEW
prefix from the explicit Linux lock only after dependency approval if needed;
never point it at an existing environment. Activation matters for CUDA headers:

```sh
/home/iska/miniconda3/bin/conda run --no-capture-output --prefix /home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104/.tools/grh-cuda12 python examples/learned_frontier/cuquantum_surface.py --output outputs/experiments/learned-frontier/new-cuquantum.json
```

No cloud job, OAuth flow, paid resource or new public service is used.

## Local exact checks and exports

```sh
.tools/book-quantum-cpu/bin/python examples/learned_frontier/width_limits.py --output outputs/checks/new-width.json
python3 examples/learned_frontier/coefficient_fields.py --output outputs/checks/new-fields.json
.tools/book-quantum-cpu/bin/python examples/learned_frontier/geometry/check_geometry.py
python3 examples/learned_frontier/hardware/check_reference_designs.py
python3 examples/learned_frontier/summarize.py
.tools/book-quantum-cpu/bin/python examples/learned_frontier/plot.py
node examples/learned_frontier/check_web.mjs
```

`export.py` and `export_state_flow.py` run in the existing Linux Torch environment
and replay saved checkpoints through every gate/head before writing numerical
DAGs and paired paths. The original learned architecture viewport is reused;
new source tensors are not decorative or fabricated weights. All nominal and
phase-readout limitations are labelled. The exporter records source/checkpoint
hashes, and the browser verifies data hashes.

## Scientific limits

Classical noise/velocity models generate a measured marginal, not coherent
states. The separate state-flow circuit is a finite known-target control fit.
Exact-oracle DDPM still uses a Gaussian reverse-kernel approximation; the
known-teacher reverse-mixture control removes it and initializes from the exact
forward terminal mixture. Heun integration and finite samples have their own
errors. Three-seed means/SD are descriptive; the entangled model does not show
an advantage. The RBF feature theorem is not a theorem about arbitrary trained
quantum transformers, QFT limits or arithmetic positive metrics. Arithmetic
operator/determinant/zero-location, category/AR and full formalization gates
remain explicit research work.

Materials/molecular and biochemical data validation, learned arbitrary CFT or
string amplitudes, nontrivial holographic reconstruction, larger conditional
chemical benchmarks, quantum hardware and actual chip PPA remain further
research/implementation tasks. Do not label them as executed by this lab.
