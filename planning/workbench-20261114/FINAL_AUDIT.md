# Final correctness audit and publication handoff

Verified 14 November 2026 UTC. This receipt supplements, rather than rewrites,
`PUBLICATION.md`. Completed actions and outstanding research are separated below.

## Published identities

- Original integrated research/publication checkpoint:
  `e30d393420c05e66144b8fd8edbe979d38cd134d`.
- Tested analogy-boundary repair and current scientific source:
  `b01a5f5e1e301e8d1a111a84ff6052724e4c07ae`.
- Updated Hugging Face dataset revision:
  `84aa1e7241e67c9b85e31d2e45400d3f285c001d`.
- Prior reproducible dataset revision, preserved unchanged:
  `cf1e2c5690e6f7056ee507bf3143813facfdbce8`.
- Unchanged GitHub Pages commit:
  `9fad0d0f973a27bb75fc1fcb9cb4b6025028fded`.

[Live workbench](https://amelie-iska.github.io/GRH-research/workbench/)
— [fluid adapter](https://amelie-iska.github.io/GRH-research/workbench/laboratory.html?lab=fluids)
— [cosmology adapter](https://amelie-iska.github.io/GRH-research/workbench/laboratory.html?lab=cosmology).

[37-page research supplement](https://huggingface.co/datasets/AmelieSchreiber/GRH-Physical-Graph-Workbench/resolve/84aa1e7241e67c9b85e31d2e45400d3f285c001d/documents/graph-computation-category-o.pdf)
— [dataset and reproduction](https://huggingface.co/datasets/AmelieSchreiber/GRH-Physical-Graph-Workbench/tree/84aa1e7241e67c9b85e31d2e45400d3f285c001d)
— [measured results](https://huggingface.co/datasets/AmelieSchreiber/GRH-Physical-Graph-Workbench/blob/84aa1e7241e67c9b85e31d2e45400d3f285c001d/evidence/results.json)
— [independent final audit](https://huggingface.co/datasets/AmelieSchreiber/GRH-Physical-Graph-Workbench/blob/84aa1e7241e67c9b85e31d2e45400d3f285c001d/evidence/final-audit/integrity.json).

The supplement, original measured results, train/validation/test records and
executed experiment source are byte-for-byte unchanged by the final repair.
The original monograph and fluid book remain separate historical releases.

## Reproduced defects and correction

The previous standalone analogy checker accepted two invalid cases:

1. A source edge could map to a target path through a vertex absent from the
   declared target graph.
2. A retrieval record with an empty leakage-group set could enter the shortlist,
   despite lacking the provenance needed for group exclusion.

The repair validates every declared edge endpoint, bounded paths and relation
words, nonempty memory provenance, unique identities, finite numeric keys and
sequential ground-rule premises. Optional exact order witnesses must cover both
source and target graphs and increase along every edge. These are typed syntax
and declared-order conditions, not certificates of physical causation or
semantic equivalence. Retrieval remains a proposal, not a deduction.

Twenty new adversarial regression methods cover the reproduced errors and their
neighboring boundary cases. The measured experiment uses its separate frozen
embedding adapter; its predictions and training results were not changed.

## Freshly executed validation

- **52 regression methods passed under ordinary Python.**
- **The same 52 methods passed under `python -O`.**
- The original suite retains 375 matrix/seed/tropical involution cases and
  175 Python/JavaScript certificate comparisons.
- **Five finite certificates** were freshly replayed by the pinned Lean 4.24.0
  kernel, with no axiom dependencies.
- **Four measure-theoretic risk statements** freshly compiled without warnings;
  dependencies were limited to propext, Classical.choice and Quot.sound.
- **Six BGG coefficient identities** freshly compiled without warnings;
  dependencies were limited to propext and Quot.sound.
- The exact pinned mathlib commit was independently checked before compilation.
- All **103 historical manifest-listed files** matched their recorded bytes and
  SHA-256 values, with no missing or extra publication member.
- All **1,648 NOAA graph rows** were independently reconstructed from the pinned
  source files: values, differences, context, monthly continuity, units, scale,
  source identity, directed edges and quantizer labels matched.
- There were **zero duplicate record identities** and **zero cross-split raw
  temporal-support overlaps**. Counts remain 1,015 train / 316 validation /
  317 test. These are temporal holdouts within two series, not held-out systems.
- All **eight publicly included NOAA model runs** passed independent replay of
  probabilities, labels, symbol code lengths, exact integer residual lengths,
  BPB denominators and checkpoint hashes. Public per-record arrays are not
  included for SILSO/ECG, so this public-array replay does not claim to cover them.

The final audit's executed script, ordinary/optimized test logs, fresh kernel
receipts, formal logs and manifest checks are retained under
`evidence/final-audit/` in the updated dataset. The historical 32-test reports
remain explicitly historical rather than being silently overwritten.

Seven live Pages assets were requested again at 09:31 UTC: index.html, core.js,
app.js, bridge.js, laboratory.html, laboratory.js and styles.css. All returned
HTTP 200 and exactly matched the current source bytes. No UI code changed in
this audit. The earlier 17 local and six public browser checks remain the
rendered-interaction evidence; a static HTTP check is not represented as a new
browser test. Static Pages supports arithmetic/export, not remote Lean execution.
The loopback kernel service remains opt-in and was not deployed to the internet.

## Updated dataset publication

The new revision has **122 manifest-listed files plus the manifest**. It adds
the repaired reproduction source, tests and independent audit without changing
scientific observations. Publication used the previous revision as a parent
lease, so concurrent changes would have stopped the update.

Six pinned public targets were fetched after publication and matched local
bytes: README, manifest, repaired analogy source, new adversarial tests,
independent integrity report and research PDF.

- PDF: 556,705 bytes, 37 pages,
  SHA-256 `d6c420e11669241f247c37f44901ff5c56628dc289031ee083b9195626572f79`.
- Original measured results:
  `3eed1b691172b2b3aded5f8117e773594cb2804e59a5f1a2564bc7bcd7bdf630`.
- Repaired analogy source:
  `86894cc455c9109bae7b73aa8c663cd7b05b4229f61ece2273790084cf90aa29`.
- Independent row/score integrity report:
  `fbef610f3ac2081639a055596984bff61073cc588c924cc7a8ee63aebdd14468`.

No new raw SILSO or ECG data, third-party paper PDFs, private data or credentials
were introduced. Seven constructed exact fixtures remain a separate test-only
configuration and are not mislabeled measurements.

## Coverage and research limits

The published supplement includes the requested graph-language and circuit
semantics expansion, ConvexTok/GFlowNet/quantum-hybrid qualifications, analogical
transfer and deduction contracts, cluster/gentle/order connections and BGG
category O synthesis. Classical category O, Verma resolutions and the exterior
BGG correspondence are distinguished. Exact sl2 examples expose the cutoff
relation defect K(K-1-lambda); exterior identities, a rational contracting
homotopy and an integral torsion counterexample are executable.

Sixteen genuinely trained native Mora-3 encoder component runs remain reported:
four process sources, two attention variants and two seeds, with validation-only
checkpoint selection and all negative results retained. They are small CPU
component studies, not the approximately 80M model, the original campaign, a
trained GFlowNet, quantum hardware, a full native forest-analogy model or a BGG
training result. Predictive gains are mixed, and model/retrieval-inclusive costs
can overwhelm conditional gains on short streams. The separate known-English
control is actual text, not a speech experiment.

CMB, gravitational-wave, acoustic/animal communication, turbulence and additional
sensor extensions remain proposed studies, not executed results. No intentional
message was discovered. Compressibility and dependence do not establish intent.
Kolmogorov complexity is not computed; ideal code lengths and actual compressors
are explicitly labeled proxies. Full category-O formalization, a new
cryptographic security theorem, a continuum mass-gap result and the GRH/HP
arithmetic spectral identity are not claimed by this release.

## Machine synchronization and agent status

Before this metadata receipt, both established clones were confirmed clean on
main at the scientific source `b01a5f5e1e301e8d1a111a84ff6052724e4c07ae`:

- Iska: `/home/iska/Documents/amelie/GRH-research`.
- Windows: `C:\Users\LIZ\Documents\GRH-research`.

Windows was located, inspected and fast-forwarded from its older clean main;
its previous synchronization block is resolved. Both clones report the same
three recorded submodule pins. No local changes were discarded, no forced
update was used and no unrelated training environment or process was changed.
This final metadata commit is synchronized after creation and checked separately.

Eight isolated Codex workers were attempted earlier; all were rejected by the
account usage limit before producing development output. The reported work was
performed directly. No paid API fallback or unobserved asynchronous continuation
is part of this handoff.
