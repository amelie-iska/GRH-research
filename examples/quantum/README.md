# Quantum and hybrid computations

All examples are finite, reproducible CPU models. They do not construct an arithmetic self-adjoint operator or prove GRH. The completed order, polynomial algebra, a finite central quotient, graph-spin Hamiltonian and photonic carrier are separate objects.

The user approved a **new isolated** environment `.tools/book-quantum-cpu` on 2026-11-03. No existing environment was upgraded. Python 3.12 and the complete `requirements-cpu.lock` record the successful runtime. The framework versions are deliberately compatible: NumPy 1.26.4, SciPy 1.13.1, PennyLane 0.40.0, Cirq-core 1.4.1, Qiskit 1.3.3, Strawberry Fields 0.23.0, The Walrus 0.21.0 and setuptools 80.9.0. Strawberry Fields uses the legacy pkg_resources interface; its deprecation warning is retained in the logs. No Xanadu/cloud login or network backend is used.

Run from the project root:

```
.tools/book-quantum-cpu/bin/python examples/quantum/train_pennylane.py
.tools/book-quantum-cpu/bin/python examples/quantum/train_photonic.py
.tools/book-quantum-cpu/bin/python examples/quantum/toricgt_hybrid.py
```

`train_renormalization.py` is the independent NumPy reference. `train_pennylane.py` trains the same circuits using actual PennyLane default.qubit expectation calls. It checks random nontrivial feature agreement before training. The three architectures are QCNN state compression, shared quantum graph convolution for exact Ising decimation, and quantum-feature graph attention for exact star-to-triangle labels. Finite expectation derivatives use parameter shift plus the classical chain rule; attention uses central differences through the nonlinear head. Adam updates and data splits are explicit. Seed 20261103 fixes all three data sets and initial parameters. Results include the entire loss history, held-out final predictions, parameters, target definitions and checks.

`train_higher_genus_qcnn.py` trains a larger nine-qubit QCNN on edge labels of the genus-four m=9 dessin. Its finite Ising ground states are computed by a sparse eigensolver with recorded residuals; it is not a faithful order action. The remaining discard loss is substantial and reported.

`train_photonic.py` trains a shared beamsplitter in the Strawberry Fields Gaussian CPU simulator. It learns the principal-axis angle of a specified two-mode covariance family, with an independently known optimum. It minimizes Var(x0)+Var(p1), using ordering (x0,x1,p0,p1). It is a finite Gaussian coarse-graining model, not an interacting QFT RG theorem.

`toricgt_hybrid.py` imports only the pinned upstream ToricGT toric_algebra module, trains a two-qubit PennyLane surrogate for a finite Harper spectral problem, and checks or repairs six rational lower-bound proposals using all fifteen exact rational principal minors. It does not reproduce the upstream language-model training or certify any number-field L-function spectrum.

Cross-backend carrier comparison:

```
.tools/book-quantum-cpu/bin/python examples/quantum/backend_adapters.py --backend cirq
.tools/book-quantum-cpu/bin/python examples/quantum/backend_adapters.py --backend qiskit
.tools/book-quantum-cpu/bin/python examples/quantum/backend_adapters.py --backend pennylane
.tools/book-quantum-cpu/bin/python examples/quantum/backend_adapters.py --backend strawberryfields
```

These use a Fourier-prepared four-level state with nonconstant phases. The photonic test compares the full one-photon density block; cutoff 2 is exact because these passive gates preserve total photon number 1. All four CPU comparisons have run successfully. The cuQuantum and CUDA-Q adapters are supplied but **not run**: this Apple machine has no supported NVIDIA GPU runtime. `upstream-pins.json` records the requested public upstream forks and local source-clone commits. Their code is not installed into the environment or silently executed.

Outputs live under `outputs/experiments`; originals and source clones remain immutable. The local page is rebuilt with `python3 scripts/prepare_companion.py` and served by `python3 scripts/serve_book.py`. No CDN, telemetry, external scripts, paid jobs or public deployment are required.

The existing Manim environment rendered `manim_surface.py` into `outputs/animations/videos/manim_surface/480p15/SurfaceClock.mp4`. Its torus and moving clock labels are a visualization, not claimed arithmetic geodesics. The Sage file is supplied under `examples/sage`; the local Sage launcher currently points to a missing app, so its Sage execution is not reported as passed.
