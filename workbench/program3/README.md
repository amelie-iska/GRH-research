# Resource-certified arithmetic, coverings, learned RG and observed-sky controls

This continuation implements the program in the monograph's subsection titled
“Resource-certified elliptic-curve quantum arithmetic” (synthesis.tex 355–380
at fd57c525). Its numbering is edition-dependent. Original publications remain
historical artifacts; current source points to these implemented extensions.

`ecc.py` emits X/CX/CCX arithmetic circuits with exact affine/infinity encoding,
fixed invalid words, bounded field oracles and clean ancillary registers. Both
binary and coherent endomorphism paths are compiled and counted, including
signed decomposition and its uncomputation. The finite truth-table compiler has
explicit exponential cost and is not a cryptographic-size optimization claim.

`covers.py` implements gentle voltage covers, torus cell covers, local neural
intertwiners and replicated normalized attention. Its integral-order test exposes
when a cover of a zero-relation special fiber fails to preserve uv=pi e before
specialization. Cover degree, input size, parameter width and ramification are
different variables.

`qrg.py` trains a six-angle 4->2->1 quantum channel hierarchy plus a classical
readout. Its complete Kraus form is checked independently of Heisenberg and
partial-trace implementations. Coarse effective Hamiltonians use -log rho;
truncation back to a short Ising operator family has a recorded trace-distance
error. The independent-feature width study has an explicit RBF kernel and
concentration bound; it is not a blanket infinite-width claim for every QNN.

`cmb.py` acquires actual WMAP products through official NASA links and implements
broad-feature, annular and trained hierarchical-QNN searches. All locations,
scales and methods are included in phase-surrogate maxima. Null validation,
injections, source-product dependence, representation and observational limits
are explicit in CMB_PROTOCOL.md. The original synthetic experiment is retained.

`gpu.py` performs genuine cuStateVec execution of emitted p=7 circuits and the
trained hierarchical gates. It independently counts serialized gate streams.
Larger p=13 instances retain complete basis tests without a dense GPU assertion.

Run from the repository root with dependencies already available:

```
python -m workbench.program3.ecc --output /fresh/ecc
python -m workbench.program3.covers --output /fresh/covers.json
python -m workbench.program3.qrg --output /fresh/qrg
python -m workbench.program3.cmb --data /fresh/wmap --output /fresh/cmb --acquire
```

The CMB path additionally requires healpy and astropy. The recorded execution
uses an isolated tool directory, not replacements in a running training
environment. GPU execution uses the separately recorded cuQuantum environment.
Validation status is reported from actual logs, not inferred from file presence.
