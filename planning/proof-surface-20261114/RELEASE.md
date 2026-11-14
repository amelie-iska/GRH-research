# Certified Surface Computation — version-two publication

Verified 14 November 2026 UTC. This records completed publication and execution,
not a promise of asynchronous work. The scientific source is
`435de07b50b2e88a63435a2cfa275a1b3abb6551`; this metadata receipt is its descendant.

## Published artifacts

- [61-page unified volume](https://huggingface.co/datasets/AmelieSchreiber/GRH-Physical-Graph-Workbench/resolve/49ace53ae5d70ac82490e1c76dbfa177cc73eead/documents/certified-surface-computation.pdf).
- [Interactive dessin / attention / quantum explorer](https://amelie-iska.github.io/GRH-research/workbench/surface.html).
- [Exact workbench](https://amelie-iska.github.io/GRH-research/workbench/).
- [Versioned data, proof archive and evidence](https://huggingface.co/datasets/AmelieSchreiber/GRH-Physical-Graph-Workbench/tree/49ace53ae5d70ac82490e1c76dbfa177cc73eead).
- [Exact source-proof archive](https://huggingface.co/datasets/AmelieSchreiber/GRH-Physical-Graph-Workbench/resolve/49ace53ae5d70ac82490e1c76dbfa177cc73eead/documents/source-proof-port.zip).
- [New measured-control results](https://huggingface.co/datasets/AmelieSchreiber/GRH-Physical-Graph-Workbench/blob/49ace53ae5d70ac82490e1c76dbfa177cc73eead/evidence/physical-controls/results.json).
- [Formal/regression audit](https://huggingface.co/datasets/AmelieSchreiber/GRH-Physical-Graph-Workbench/blob/49ace53ae5d70ac82490e1c76dbfa177cc73eead/evidence/surface-release/final/audit.json).
- [Independent dataset/score/codec audit](https://huggingface.co/datasets/AmelieSchreiber/GRH-Physical-Graph-Workbench/blob/49ace53ae5d70ac82490e1c76dbfa177cc73eead/evidence/surface-release/package-audit.json).

Hugging Face revision: `49ace53ae5d70ac82490e1c76dbfa177cc73eead`.
The previous revision `84aa1e7241e67c9b85e31d2e45400d3f285c001d` is preserved.
The new packet has 310 manifest-listed members plus the manifest, approximately
57.2 MB. Publication used an expected-parent lease; 195 new/changed members were
uploaded. The old 37-page PDF, original measured results and NOAA records remain
byte-for-byte unchanged. No third-party book scans, external paper PDFs, private
data, secrets or font files were introduced.

PDF SHA-256:
`73ba85cf7e8af2daa0b46da83fc78061f715bf9751f46b931e1faeabcbe58f54`.
Manifest SHA-256:
`4e06de4618cc4958a449027429f5952c3bff4ee5681215f140ff73a5b5cfae39`.

Pages commit: `00dc70e0168f91501c07fa90e1f3e58d38cbf2b8`.
[Deployment 43589186456](https://github.com/amelie-iska/GRH-research/actions/runs/43589186456)
completed successfully. The existing atlas was retained; only its workbench
subtree changed. The new volume is a separate integrated publication rather
than a silent overwrite of the original monograph or fluid book.

## The unifying constructions

The volume is organized as a calculus of explicit realizations. Dessin
permutations and cellular incidence lead to quivers, relations and complexes;
orders retain integral specialization; metrics, Hodge operators, Markov channels
and Pauli checks supply distinct analytic and physical realizations. Graph models
propose transformations while exact/formal/numerical tests verify the specified
property. The exposition leads with established results and their constructions.

Completed additions include:

1. A direct **uniform graph-to-graph approximation construction** using exact
   finite-temperature identifier gathering, compact-domain ReLU approximation,
   output slots and finite-group symmetrization. Encoding, masks, output action
   and resource growth are explicit; this is not an Lp theorem with its norm
   silently changed.
2. A **complete finite Boolean-circuit and graph-table formalization**. Lean proves
   agreement between Boolean and affine/ReLU interpretations for every circuit in
   the syntax, constructs every finite Boolean input indicator, and proves exact
   coordinatewise realization of every finite graph-output table. Its exponential
   construction cost is explicit.
3. An explicit **rank-four order with gentle special fiber**, its multiplication,
   generic matrix-algebra fiber, arrow relations and trace-pairing determinant.
4. The **exact finite toric-code spectrum**, ground-space multiplicity, gap
   `4 min(J_X,J_Z)` and energy-to-ground-space certificate on the checked torus.
5. A **Kraus realization of finite probability diffusion**, with actual matrix
   execution of completeness, trace preservation and the diagonal transport law.
6. A **complete energy-controlled nonlinear flow and unitary half-density lift**,
   with written change-of-variables/Stone-theorem proof, exact triad identities,
   Jacobian and inverse-flow tests, and unitary Cayley discretization.
7. Explicit **continuum gap and arithmetic determinant transport criteria**.
   Their analytic/arithmetic assumptions remain premises; a finite calculation
   does not manufacture them.
8. The integrated BGG/category-O, cluster/gentle/order, language/grammar,
   ConvexTok, GFlowNet, analogy/deduction and quantum/hybrid discussions from the
   earlier supplement, now connected to these additional realizations and tests.

The nonlinear half-density generator is a state-space transport operator and need
not be positive-energy. The finite spin gap is a completed finite-system theorem,
not the four-dimensional continuum Yang–Mills theorem. The determinant criterion
requires an independently established arithmetic identity. The released
Navier–Stokes result retains its original attribution and force/regularity
hypotheses. These distinctions specify the mathematical objects being studied.

## Exact source port and proof review

The accessible requested repositories were pinned and reopened:

| Repository | Commit |
|---|---|
| TropicalGT | f8ffc7150afdd83bace8078c86fde7c8eeb0e08e |
| ToricGT | a5199bc989a6fb170e21220e5e87bf95bc2fc0b4 |
| ToricGT-Program | f91ba1811b5a4f70d53c7120acf8ca2a0049f85b |
| Mora-3 | 75ac2d696f42da0a673fc43a20d84686a2ceed40 |
| Tropical_Quivers_of_Archs | 2b6ab79a685e2c6233fb8892e59589951feeddad |

The port includes all 17 TeX research documents and six Mora-3 paper Markdown
files in those pinned trees: **475 named claim occurrences, 248 distinct
statement hashes and 463 following proof occurrences**. Git blob identities,
SHA-256 hashes, original text and line locations are preserved. The dedicated
`TropicalGT/references/main.tex` graph-expressivity manuscript is included.

The literal `amelie-iska/TropicalGT-Program` name returned 404 through both public
API and selected GitHub connector access. It is not silently identified with a
different repository. TropicalGT's own Parts I–IV are included.

Twelve named source occurrences receive explicit review decisions; 463 remain
source-port-only. Preservation is not mislabeled as independent validation of
all 475 statements or a complete Lean port of every source proof. The review
records fixed-order IGN qualifications, uniform versus Lp metrics, decoding-TV
premises, a planar Minkowski counterexample, hard-routing discontinuity,
finite-temperature Hessian constants, bounded-grammar continuity, and the zero
conditional information of deterministic full-prefix summaries. Positive
constructive repairs and formal extensions are supplied alongside those findings.

## Final execution evidence

- **107 regression methods passed** under ordinary Python.
- **The same 107 passed under `python -O`.**
- **107 also passed from a fresh materialized publication layout**, after verifying
  its complete manifest. This is separate from tests run in the development tree.
- **48 new Lean declarations** passed the strict source-stable audit: 14
  ExpressivityContracts, 7 ConstructiveGraph, 7 FiniteGraphNetworks, 12
  OrderRealization, 3 InformationContracts and 5 HalfDensityContracts.
- The prior four measure-risk and six BGG declarations were freshly checked.
- Five canonical finite payloads were freshly kernel-replayed, axiom-free.
- Accepted formal logs have **zero warnings, no sorryAx and no unexpected
  foundational axioms**, and include every printed theorem type/dependency.
  Lean 4.24.0 and mathlib commit
  `f897ebcf72cd16f89ab4577d0c826cd14afaafc7` were verified.
- Nine 18-qubit controller configurations agree across independent NumPy,
  JavaScript Float64 and genuine cuStateVec complex128 executions. Maximum
  GPU/CPU amplitude error: **6.94e-18**. Maximum parameter-shift discrepancy:
  **3.61e-16**.
- Fifteen nonlinear triad flow/Jacobian/energy cases passed; maximum inverse-flow
  error: **1.50e-14**. Cayley temporal-refinement orders were **1.9983 and 1.9996**.
- Six four-qubit cuStateVec Cayley-matrix applications passed; maximum amplitude
  error: **1.12e-16**. This is a dense unitary backend check, not an unreported
  elementary-gate synthesis or quantum-hardware experiment.
- **30 local rendered-browser checks passed**, including all five kernel contract
  types, surface/circuit linkage, exact temperature state, keyboard operation,
  URL restoration, export, stale responses and mobile/landscape layouts.
- **11 published-browser checks passed**, with no page JavaScript exceptions.
  Static Pages explicitly declines remote kernel verification and provides the
  loopback instructions in its receipt panel.
- **26 pinned/public asset byte checks passed**: twelve Hugging Face objects and
  fourteen Pages/dependency objects. Public bytes matched the verified files.

The final three-pass 61-page PDF build has no undefined references or overfull
boxes. Two underfull paragraph advisories concern a long exact source path; the
rendered text is readable and unclipped. All pages were rendered and contact-sheet
inspected, with selected framework, proof, measured-codec and surface-chart pages
also inspected at full resolution. Layout inspection is separate from theorem
verification. A missing optional graphics package was removed from the build
requirements rather than installed into the user's environment.

## New measured controls and complete coding costs

The continuation adds actual GWOSC GW150914 H1/L1 strain and eighteen LibriSpeech
utterances from three speakers. Official GWOSC MD5 checks and independent SHA-256
hashes are retained. Speech remains native mono PCM16 at 16 kHz. The exact source
selection and archive-prefix hash are recorded; no complete-archive hash is claimed.

Speech has speaker-separated train/validation/test. The detector control fits H1
0–8/8–12 seconds and tests L1 24–28 seconds from GPS 1126259446, excluding the
known event from fitting. The strain code uses a declared 1e-24-unit fixed-point
view with measured quantization error. There are 2,400 graph windows per split
per new source: **14,400 new windows**, in addition to the unchanged 1,648 NOAA
windows. Raw support is disjoint across splits and target identities are unique.

Eight new native encoder fits completed: two sources, ordinary/tropical variants,
seeds 17/29 and 80 optimizer steps. The workbench now reports **24 component fits**
across six measured or observation-derived process sources, plus the original
English-text control. These are actual small pinned Mora-3 encoder runs, separate
from the full model, original campaign, full forest-analogy head, GFlowNet training
or quantum-hardware experiments.

Held-out bits per quantized symbol, averaging the two neural seeds:

| Control | Count | Ordinary | Tropical | Ordinary + retrieval | Tropical + retrieval |
|---|---:|---:|---:|---:|---:|
| Held-out speech speaker | 2.2405 | 2.6111 | 2.7917 | 2.4217 | 2.4720 |
| Held-out L1 strain interval | 3.9712 | 2.6296 | 2.6754 | 2.6106 | 2.7414 |

The count baseline wins on speech. Native models improve on the selected count
baseline in the detector interval, with substantial seed variation. Retrieval
can improve or worsen a run. All these outcomes are retained.

The new reference codec emits actual byte packets, including frozen model,
quantizer representatives, exact residuals, segment boundaries, initial samples
and termination. Independent decoding recovered every declared integer sample:

| Representation | Original bytes | Packet bytes | Actual BPB | zlib BPB | lzma BPB |
|---|---:|---:|---:|---:|---:|
| Speech PCM16 | 2,692,320 | 2,161,121 | 6.4216 | 5.8805 | 4.8748 |
| Strain fixed-point int32 | 65,536 | 62,367 | 7.6132 | 6.2821 | 4.7246 |

The reference codec does not beat those general-purpose baselines. Whole-stream
packet BPB and sampled-window neural likelihood have different exposure and
representation contracts and are not pooled into one leaderboard. Kolmogorov
complexity is not computed. A retrospective event correlation control reached
0.3953 at the known event, versus a maximum of 0.7177 across 52 off-source windows;
this statistic did not isolate the event. No event-discovery significance or
intentional-language claim is inferred.

An acquisition provenance issue was found and repaired: speaker-level transcript
storage could retain the wrong chapter. Chapter-specific files now match **all
18 audio identifiers**; audio, training runs and results were unchanged because
transcripts were never predictor inputs. The failed initial provenance state and
repair are recorded rather than hidden.

## Publication and machine state

The associated dataset was updated with an expected-parent lease. Its metadata
card passed validation. The previous scientific artifacts remain immutable,
and source-specific CC BY 4.0 attribution accompanies the new speech and strain.
The unchanged SILSO/ECG redistribution policy remains intact.

Both established clones were confirmed clean on `main` at the scientific source:

- Iska: `/home/iska/Documents/amelie/GRH-research`.
- Windows: `C:\Users\LIZ\Documents\GRH-research`.

Both matched selected source hashes and the same three submodule pins. No local
changes were discarded; no force push, restart, environment replacement or
unrelated training change was used. This metadata commit is synchronized after
creation and checked separately. The optional loopback test servers were stopped
by their test harnesses; the public site is static.

Earlier eight-agent attempts remain recorded as rejected by the account usage
limit before producing development output. None is credited with this work. No
paid API fallback or unobserved asynchronous continuation is part of the release.
