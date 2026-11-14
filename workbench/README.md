# Certified Surface Computation

A unified executable research program connecting finite presentations, integral
orders, gentle relations, BGG structures, graph learning and quantum realizations.
The source belongs to [GRH-research](https://github.com/amelie-iska/GRH-research).
The exact workbench is joined by an interactive dessin / attention / quantum-state
explorer at `workbench/surface.html` on the public atlas.

## Mathematical constructions

The new volume gives a direct uniform graph-to-graph approximation construction
with exact finite-temperature identifier gathering, output slots and finite-group
symmetrization. A separate Lean module proves affine/ReLU correctness for every
finite Boolean circuit in its syntax and exact realization of every finite
Boolean graph table. Resource growth, encoding and symmetry actions are explicit.

An explicit rank-four order has a gentle radical-square-zero special fiber.
The checked toric-code Hamiltonian has its exact finite spectrum, gap and energy
certificate. A Kraus construction realizes finite probability diffusion as a
quantum channel. Written transport theorems state the precise analytic premises
for a continuum gap and an arithmetic spectral identity. Those premises remain
part of the theorem, not consequences inferred from a finite simulation.

`proof_port/` preserves the research documents from five accessible pinned
repositories, with exact source statements, following proofs and content hashes.
The requested `TropicalGT-Program` repository name returned 404. The source port
and its per-claim review register are distinct: preserved text is not automatically
promoted to a Lean theorem. The dedicated TropicalGT graph-expressivity manuscript
is explicitly included, and dependency repairs remain inspectable.

## Execute and inspect

```sh
# Standard library + Node; numerical/physical protocol tests also require NumPy.
python3 -m unittest discover -s workbench/tests -v
python3 -O -m unittest discover -s workbench/tests -v
python3 workbench/numerics.py
python3 workbench/bgg.py
python3 workbench/realization_bridges.py

# Local workbench and optional pinned kernel replay.
python3 workbench/bridge_host.py --lean /absolute/lean-4.24.0-linux/bin/lean
# Open http://127.0.0.1:8767/workbench/surface.html
```

The surface explorer uses the existing checked 18-qubit toric-code manifest.
It links physical edge selection to clean-dessin cycles, coordinatewise tropical
winners, circuit gates and actual state-vector readouts. Softmax, hard score
routing and coordinatewise max-plus remain distinct operators. The classical
controller sets quantum rotation angles; max-plus is not represented as a unitary.
Independent NumPy, browser Float64 and actual NVIDIA cuStateVec executions provide
separate computational checks. The simulation is not a quantum-hardware claim.

The five original exact contract types remain available: heat positivity,
weighted gain, Monte Carlo rank, family-wise budget and seed mutation. Receipt
hashes bind the exact input and fixed proof source. Input changes invalidate old
receipts. Static GitHub Pages performs arithmetic/export; the opt-in loopback
service supplies Lean execution without accepting uploaded code.

## Physical observations and code lengths

The first release's sixteen native encoder component runs on four measured or
observation-derived processes remain unchanged. The new controls add eight
fresh component runs on actual speech and gravitational-wave detector strain,
with speaker/detector-held-out intervals and validation-only selection. The full
Mora-3 training campaign, environments and checkpoints are separate and unchanged.

`experiments/exact_codec.py` emits actual frozen-model arithmetic-coded packets
with exact residuals, model metadata, segment boundaries and seeds. Its independent
decoder must recover all declared samples. These emitted bytes are distinguished
from ideal likelihood codelengths. A fixed-point strain view retains its measured
quantization error; it is not mislabeled as the original floating-point file.

Known speech supplies communicative provenance independent of compression.
Measured physical dependence, coding gain and intentional messages are different
hypotheses. Negative comparisons and failed controls remain in the evidence.

## Publication

The associated data and evidence repository is
[GRH-Physical-Graph-Workbench](https://huggingface.co/datasets/AmelieSchreiber/GRH-Physical-Graph-Workbench).
The versioned publication receipt records source, Pages, dataset and PDF hashes.
The earlier 37-page supplement and its historical evidence are preserved; the
expanded volume is published as `documents/certified-surface-computation.pdf`.
The main monograph and original fluid supplement remain separately reproducible.

Source-specific licenses and attribution accompany the physical controls. The
proof archive contains the user's authored research sources, not redistributed
third-party book scans or paper PDFs. Execution status, external theorems and
conditional research objectives are identified at their exact level of evidence.
