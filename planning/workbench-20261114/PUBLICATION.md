# Published graph-computation and BGG workbench

Verified 14 November 2026, 06:14 UTC (13 November Pacific).
This receipt records completed actions, not a promise of subsequent execution.

## Publication identities

- Scientific and implementation source, including final dataset packaging:
  `e5d917a4c99c820a69075152d7163248d1d120a0`.
- GitHub Pages commit: `9fad0d0f973a27bb75fc1fcb9cb4b6025028fded`.
- Pages deployment: [run 43565249398](https://github.com/amelie-iska/GRH-research/actions/runs/43565249398), completed successfully.
- [Live exact workbench](https://amelie-iska.github.io/GRH-research/workbench/).
- [Live fluid adapter](https://amelie-iska.github.io/GRH-research/workbench/laboratory.html?lab=fluids).
- [Live cosmology adapter](https://amelie-iska.github.io/GRH-research/workbench/laboratory.html?lab=cosmology).
- [Hugging Face dataset](https://huggingface.co/datasets/AmelieSchreiber/GRH-Physical-Graph-Workbench), revision `cf1e2c5690e6f7056ee507bf3143813facfdbce8`.
- [37-page research supplement](https://huggingface.co/datasets/AmelieSchreiber/GRH-Physical-Graph-Workbench/resolve/cf1e2c5690e6f7056ee507bf3143813facfdbce8/documents/graph-computation-category-o.pdf).
- [Per-run measured results](https://huggingface.co/datasets/AmelieSchreiber/GRH-Physical-Graph-Workbench/blob/cf1e2c5690e6f7056ee507bf3143813facfdbce8/evidence/results.json).
- [Artifact manifest](https://huggingface.co/datasets/AmelieSchreiber/GRH-Physical-Graph-Workbench/blob/cf1e2c5690e6f7056ee507bf3143813facfdbce8/manifest.json).

The supplement is a separate publication. The original monograph, fluid book,
existing preview-workbench directory and historical release evidence were not
silently replaced. The new Pages tree adds only the workbench subtree.

## Artifact integrity

The PDF is 556,705 bytes, 37 pages, with SHA-256
`d6c420e11669241f247c37f44901ff5c56628dc289031ee083b9195626572f79`.
The final three-pass LaTeX build had no warnings, undefined references or overfull
boxes. Selected result, BGG and reference pages were rendered and visually
inspected; this is not a claim that every page received a separate visual audit.

The measured-study result SHA-256 is
`3eed1b691172b2b3aded5f8117e773594cb2804e59a5f1a2564bc7bcd7bdf630`.
The executed study source SHA-256 is
`d1ef909033581b85a874c3286ae2cf75774e9337aaff43973ba295636b0e4d98`.

Five pinned Hugging Face targets returned HTTP 200 with bytes identical to the
local publication packet: README, manifest, PDF, experiment results and test
JSONL. Seven public Pages assets also returned HTTP 200 with exact source-byte
matches: index.html, core.js, app.js, bridge.js, laboratory.html, laboratory.js
and styles.css. Initial pre-deployment Pages 404 responses were not counted as
successful publication; the final check occurred after the successful deployment.

## Verification results

- 32 Python regression methods passed under normal execution.
- The same 32 methods passed under `python -O`.
- The exact contract suite includes 375 matrix/seed/tropical mutation-involution
  cases and 175 Python/JavaScript certificate comparisons.
- Five accepted finite certificates passed Lean 4.24.0 kernel replay with no
  axiom dependencies. Five deliberately false witnesses, passed directly to
  Lean rather than rejected only by Python, all failed kernel checking.
- Four measure-theoretic finite-search bounds compiled without warnings. Their
  only printed foundational dependencies were propext, Classical.choice and
  Quot.sound. Event calibration and model-discrepancy bounds remain premises.
- Six BGG/sl2 coefficient identities compiled without warnings, with only
  propext and Quot.sound. This is not full formalization of category O or of an
  infinite BGG resolution.
- 17 local Chrome/Playwright checks passed, including all five kernel contract
  types, invalid-domain rejection, receipt invalidation, stale in-flight response
  rejection, mobile overflow, fluid/cosmology adapters and static wrapper paths.
  No page JavaScript exceptions were observed in that run.
- Six additional public-browser checks passed: page identity, explicit static
  kernel limitation, both live adapters and their static-host verification
  boundaries. No page exceptions were observed in that bounded public run.

The connected Browser integration was read-only. Interactive QA therefore used
already-installed Chrome through Playwright, without changing browser packages.
The loopback proof server was stopped after testing; no internet-facing kernel
service was deployed. GitHub Pages performs arithmetic/export, not Lean execution.

## Real measured-data experiments

Sixteen fresh, CPU-only native Mora-3 encoder component runs completed: four
sources, two attention variants and two seeds. Each attempted 80 optimizer
steps, selecting its checkpoint on validation only. The ordinary model/readout
has 2,744 parameters and the tropical-code variant has 2,104. These are not the
full approximately 80M Mora-3 model, a pretrained checkpoint, a quantum experiment,
a GFlowNet-training result or the original 24+2 campaign.

Held-out bits per quantized symbol (neural columns average seeds 17 and 29):

| Source | Test targets | Selected count model | Native ordinary | Native tropical | Ordinary + retrieval | Tropical + retrieval |
|---|---:|---:|---:|---:|---:|---:|
| NOAA CO2 | 146 | 2.6657 | 2.2118 | 2.1476 | 2.0616 | 2.0539 |
| SILSO sunspots | 406 | 2.8996 | 2.9120 | 2.9804 | 2.8768 | 2.9500 |
| NOAA Nino-3.4 | 171 | 2.9965 | 3.0051 | 3.0009 | 3.0090 | 2.9902 |
| MIT-BIH ECG MLII | 4,783 | 2.8046 | 2.8632 | 2.9473 | 2.7575 | 2.8696 |

These are symbol likelihoods, not original-byte compression figures. The report
separately adds exact signed integer residual codes and uses a canonical four-byte
fixed-point target denominator. Model-inclusive two-part costs also charge model
values, quantizer metadata, lag-context seeds and retrieval memory. On these short
streams, those costs can overwhelm the conditional predictive gain. The native
models improve CO2 prediction but do not consistently beat the count baseline
elsewhere. Retrieval worsened ordinary seed 29 on Nino-3.4 by about 0.0124 bits
per symbol. No architecture-wide superiority is claimed.

The independently sourced human-English control uses Gutenberg's Alice text.
Validation selected an order-two count model with smoothing 0.1, yielding
approximately 2.9601 held-out bits per UTF-8 byte. Actual zlib and lzma lengths
were approximately 3.0386 and 2.9087 bits per byte on that segment. These have
different conditioning/model costs. Human authorship is established by provenance,
not by the compression score. This is not an acoustic-language experiment.

The two corrected preflight defects occurred before optimizer updates and their
failure records remain included. A NOAA global-temperature endpoint returned
404 and is not represented as an executed fifth process dataset. The ongoing
Mora-3 campaign, its environments, checkpoints and running jobs were not changed.

## Dataset contents and rights

The published packet has 103 manifest-listed files plus its manifest. It contains
1,648 actual NOAA-derived directed lag-graph records: 1,015 training, 316 validation
and 317 test. The raw temporal supports of contexts and targets are disjoint
between splits; record identities are unique. These are temporal holdouts within
two series, not independent-system generalization. Target columns are separate
from the input graph.

Seven constructed exact mathematical fixtures are a separate test-only config,
not mislabeled measurements or admitted training examples. NOAA-only per-record
predictions and small component checkpoints are included. SILSO and ECG raw rows,
per-record predictions and checkpoints are source-linked rather than copied.
The source catalog distinguishes executed sources from proposed CMB, gravitational-
wave, turbulence, PDE simulation and activity-sensor extensions. No third-party
paper PDFs, private data, secrets or credentials are publication inputs.

## BGG and architecture synthesis

The final chapter distinguishes classical highest-weight category O, BGG Verma
resolutions and the exterior/symmetric BGG correspondence. It derives the sl2
short exact sequence, checks finite highest-weight quotients, exhibits the exact
cutoff defect K(K-1-lambda), and implements exterior anticommutation, d squared
zero and a rational contracting homotopy. Integral torsion and bad-prime examples
show why rational, integral and finite-field statements cannot be interchanged.

The synthesis connects these constructions to block algebras and Ext-quivers,
Koszul structures, graph-grammar relations, chain maps, analogy commutation,
GFlowNet object/history distinctions, dynamical residual bounds, hypertoric
category O and Gale duality, gentle surface algebras, orders and quantum encoding.
External theorem hypotheses and corrected source versions remain explicit.
A trained BGG head, full category-O implementation, physical message discovery,
continuum mass gap, cryptographic security theorem and GRH/HP spectral identity
are not claimed.

The expanded language treatment includes constructive uniform graph computation,
Turing and Boolean-circuit mechanisms, ConvexTok, GFlowNets, quantum/hybrid scope
and a source-sensitive response to categorical anti-neural claims. It explicitly
repairs the distinction between the cited Lp approximation result and a uniform
error claim, and between bounded approximation and a uniform unbounded machine.

## Machine and agent status

The main Iska clone at `/home/iska/Documents/amelie/GRH-research` was clean and
fast-forwarded to `e5d917a4c99c820a69075152d7163248d1d120a0` before this receipt.
The isolated release worktree is at the same source commit. Publication-receipt
synchronization is performed separately after committing this file.
Windows responded to a bounded inspection, but no current clone was established;
no Windows synchronization is claimed and no local files there were overwritten.

Eight isolated Codex workers were launched. All stopped at the account usage
limit before producing work. Their output is not counted as completed; the
coordinator performed the reported implementation, experiments and validation
subsequently. No paid API fallback, unrelated process termination, environment
change or asynchronous continuation is part of this receipt.
