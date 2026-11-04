# Actual finite renormalization

The primary [RG lab](http://127.0.0.1:8765/rg.html) and
[gate/tensor/surface inspector](http://127.0.0.1:8765/architecture.html?collection=rg)
carry effective actions, constants, generated couplings, partition functions
and retained observables through a specified elimination. The old QCNN
compression, covariance alignment and selected-coupling regressors remain
preserved as distinct auxiliary tasks.

`rg_math.py` defines all finite RG maps. Physical spins occupy the2black+mwhite
vertices of the actual clean dessin y²=x^m−1,beta=x^m, m5/9 (genera2/4).
Its incidence graph is K2,m with2m edges; the infinite gentle algebra has
m quiver vertices and completed order rank2m². This is a chosen physical
Hamiltonian on the incidence graph, not a faithful representation of that
order. The ribbon permutations, not graph adjacency alone, encode genus.
The two black spins are summed out exactly. Every coarse logweight and its
Walsh coefficient, including the constant and higher-body terms, is kept.
Subsequent RG marginalizes nested retained white-spin sets. Pair truncation
is separately measured by partition and distribution errors.

The quantum calculation uses the same energy coefficients plus a transverse
field on7physical qubits. Raw W'=Tr_black exp(−betaH) is positive, and
H_eff=−log(W')/beta includes all1024five-qubit Pauli terms and its identity.
General beta scales ALL classical energy coefficients, including fixed
whitefields. Three finite saved cases have nested5→3→2→1-spin traces.
They preserve partition functions and equal-time retained observables, not
all original real-time dynamics or a local thermodynamic fixed point.

The separate even64-site Ising transfer benchmark squares T and carries
K,h,C. Spacing doubles, N halves, and the homogeneous-extension eigenvalue-
ratio correlation length halves in blocked units. The browser transports
log(r)→2log(r) to avoid falsely rounding the tiny late-scale eigenvalue to0.
The chain benchmark has its own physical lattice; it is not the odd dessin.

`train_rg.py` executes PennyLane3qubit analytic feature training against ALL32
coarse logweights, using120training/40heldout/40OOD inputs, seed20261103.
A training-only ridge head warm start precedes120jointAdam updates. Twelve
nominal circuit angles+256head parameters are stored; three finalRZ angles
commute with theZ readout and are structurally inactive for this loss, as
shown by `evaluate_rg.py`. The qubits are coupling-feature registers, not
physical spins or quiver vertices. Classical quadratic features have the
same256readout parameters and outperform several heldout/OOD metrics.
Per-example sup-logweight errors contract through later EXACT RG; finite
MSE or KL does not prove parameter-uniform accuracy. `evaluation.json`
adds constant/higher-body diagnostics without changing trained checkpoints.

`generative_rg.py` prepares sqrt(p(s)) on5qubits from the learned full action,
checks Born probabilities, applies explicit projector-Kraus dephasing to
obtain diag(p), and draws4096samples with a fixed seed. The coherent pure
state is not itself a mixed Gibbs state. All32 amplitudes are classically
computed; this is a finite generation example with no efficiency/advantage
claim. The simultaneous95% Hoeffding bound is over five magnetizations of
the learned distribution, distinct from model error relative to the teacher.

Run with the existing approved environment, from the project root:

```
.tools/book-quantum-cpu/bin/python examples/rg/check_rg.py
.tools/book-quantum-cpu/bin/python examples/rg/train_rg.py
.tools/book-quantum-cpu/bin/python examples/rg/evaluate_rg.py
.tools/book-quantum-cpu/bin/python examples/rg/generative_rg.py
.tools/book-quantum-cpu/bin/python examples/rg/export_rg.py
node examples/rg/check_web_model.mjs
```

Training data/parameters are immutable evidence under outputs/experiments/
actual-rg/. The dataset generator refuses a differing existing dataset.
Do not reinstall dependencies or rerun training as routine checking; use
saved-record/model checks. Exported numerical traces are content-addressed,
separate from the original22architecture records. `FiniteRG.lean` checks9
actual finite scalar marginal/action/partition/observable/error/trace
identities at pinned Lean4.24/mathlib. The quantum spectral-log theorem,
whole training pipeline, continuum physics and arithmetic bridge are not
thereby fully Lean formalized. No claim here proves GRH.
