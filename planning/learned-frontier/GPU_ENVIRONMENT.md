# Approved isolated Linux cuQuantum environment: proposal and execution

Target: /home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104/.tools/grh-cuda12
Host: iska-linux-vscode; observed RTX4090,24564MiB, driver580.178.04.
Existing /home/iska/miniconda3/envs/tokengt is left unchanged. It already
provides torch2.8.0+cu128 with a working CUDA12.8 runtime, NumPy and SciPy.
It lacks cuQuantum, CuPy, PennyLane and Qiskit. This paragraph describes the
pre-install inventory; the separate approved environment below is now installed.

The user explicitly approved this new prefix. The original creation proposal
was to create a new environment only (do not clone or
upgrade the existing tokengt environment):

```sh
/home/iska/miniconda3/bin/conda create --prefix /home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104/.tools/grh-cuda12 -c conda-forge python=3.11 cuda-version=12 cuquantum-python cupy numpy scipy
```

The command above is the original official-recipe-based specification.
The execution and resolved-lock results below supersede its pending status.
Record the exact resolved package list after solving, then verify the device,
CuPy allocation and a cuQuantum contraction against the CPU result before
running a larger simulation. No remote/cloud paid service is involved.
Never use the copied macOS binaries as a Linux environment.

Primary setup reference:
https://docs.nvidia.com/cuda/cuquantum/26.03.1/getting-started/index.html

The implementation uses existing torch CUDA without changing that environment.
The separate approved cuQuantum prefix is now exercised by actual GPU runs.


## Executed state, 2026-11-04

Resolved: Python3.11.18, cuQuantum26.09.0, CuPy14.2.0, NumPy2.4.6,
CUDA12.9, RTX4090 driver580.178.04. The complete explicit resolved record is
examples/learned_frontier/envs/grh-cuda12-linux-64.lock; the initial solved
record before supplemental development headers is preserved separately as
grh-cuda12-initial-linux-64.lock.
The supplemental install in the same approved prefix added cccl2.8.2,
cuda-cccl12.9.27 and cuda-nvrtc-dev12.9.86 with freeze-installed. Base conda
and every earlier environment were left unchanged; its upgrade warning
was not followed.

Invoke the environment through conda activation or conda run, so CuPy can
find the existing headers under targets/x86_64-linux/include. Calling only
the prefix's Python binary without activation failed header discovery.
The first simulation attempt preserves that error; the second executed
all circuits but its package-metadata spelling lookup failed at final JSON
assembly. The third completed and wrote the verified record. No failed
output was overwritten or deleted.

```sh
/home/iska/miniconda3/bin/conda run --no-capture-output --prefix /home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104/.tools/grh-cuda12 python examples/learned_frontier/cuquantum_surface.py --output outputs/experiments/learned-frontier/cuquantum-new-run.json
```

The verified v3 record includes real cuTensorNet contraction and cuStateVec
7/11/23qubit circuits. NumPy references cover7/11qubits;23qubits has
normalization and inverse-echo checks only. Runtime measures a GPU gate
segment, not end-to-end or comparative speedup.
