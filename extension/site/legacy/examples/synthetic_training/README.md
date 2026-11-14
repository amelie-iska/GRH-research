# Additional complementary physical training corpora

These datasets add capabilities; they replace no existing corpus, model,
vocabulary, split, checkpoint or training process. Both remote model repositories
are read-only references. All generation uses existing environments, low-priority
single-thread CPU processes and new output namespaces in the GRH project. No
GPU training job, model enrollment, install or environment upgrade is performed.

The larger default corpora contain **16,384 materials response records** and
**22,951 molecular/conformer records**. Dynamics and source-anchor rows are
separate; time frames are not counted as independent systems. Private HF links,
commit hashes and actual final configuration counts appear in the release
receipts and the [interactive explorer](http://127.0.0.1:8765/datasets.html).

## Two methods and intended contribution

**Aster:** explicit effective-Hamiltonian families, bulk/topological guards,
finite open-boundary/gauge/defect responses and exact classical dessin RG.
Dimensionless normal/BdG transport and interacting Hubbard exchange add dynamics
and circuit tasks. Existing MP20 training geometries supply separately labelled
strain/vacancy/effective-link variants. Those computed Hamiltonians are not
DFT/Wannier fits, validated quantum materials or proven GRH operators.

**Mora-3:** sanitized chemical building blocks, designed amides and peptides,
multiple conformers, empirical MMFF94 energies/forces/charges, reference-basin
denoising pairs and complete finite heavy-atom VR H0/H1. Separate short NVE
trajectories and uncalibrated pi-orbital dynamics keep their units/evidence
distinct. Planned PubChem identities and public PDB peptide/protein subsystems
anchor further method-labelled calculations. No affinity/ADMET/clinical/CISS or
ab-initio label is invented. Source NMR model order is not physical time.

## Actual row counts and explicit origin labels

| Model / configuration | Rows | Origin |
| --- | ---: | --- |
| Aster default |16,384| New effective-material simulations |
| Aster source anchors |576|48 existing MP20 training-source structures; new computed strain/vacancy/link responses |
| Aster electronic dynamics |174| New simulated trajectories, including18 exact Hubbard cases |
| Mora default |22,951| New MMFF conformer/force simulations of517 chemical parents |
| Mora source anchors |74|32 existing PubChem training-source identities; new checked3D/MMFF responses |
| Mora source anchors |192|8 new public PDB anchors related to the planned structural family; new effective-model variants |
| Mora electronic dynamics |241| New uncalibrated electronic trajectories |
| Mora nuclear MD |12| New20fs MMFF trajectories at .05fs steps |

Default counts exclude all additional configurations and do not count frames as
independent rows. Source-linked examples are train only. “New simulation” does
not claim chemical-identity novelty or prior-model blindness.

## Data organization and origin

- `default`: typed Parquet train/validation/test; `condition_*`, `target_*` and
  `evaluation_*` columns plus lossless scientific JSON.
- `electronic_dynamics`: time-dependent occupations, currents, charge modulation,
  exchange/pair correlations and independently checked continuity/source terms.
- `nuclear_md` (Mora): empirical MMFF94 positions, velocities, forces and energies.
- `source_anchors`: TRAIN ONLY reuse/derived examples with exact source IDs,
  revisions/hashes, original assignments and evidence. These cannot be blind
  evaluation for a model that may have seen the parent.
- Cards, manifests, quality/failure/similarity reports and source snapshots.

`origin_class`, `planned_source_dataset`, `planned_source_record_id` and
`label_origin` distinguish new simulations, existing planned-source reuse with
new labels, and new public PDB anchors related to the planned structural family.
New simulations do not imply new chemical identities absent from all earlier
training data. Global cross-corpus exposure remains a separate evaluation gate.

## Similarity-aware partitions

All descendants of a parent stay together. Material parameter/spectrum edges
include conservative symmetry folding; chemistry edges include constitution,
nonempty Murcko scaffold and radius2/2048bit Morgan Tanimoto>=0.65. A second
all-conformer geometric closure uses identical heavy-element multisets and
sorted pair-distance RMS<=0.10angstrom. Components are allocated using actual
family/topology or molecular-size/VR strata. Large components remain intact;
the large peptide component makes the train fraction exceed80%, and held-out
peptide coverage can be missing. Reports show actual counts and nearest pairs.

This proves no crossing for the finite declared relation, not universal
independence or prevention of overfitting. Small-molecule descriptors are not
protein TM-align or homology certificates. Molecular source anchors are also checked
against all default heldouts under the same chemical and applicable all-conformer
geometric thresholds; any conflicting parent is quarantined in full. The current
selected anchors have no such crossings. Global prior-model exposure is separate.
Do not fit vocabularies/scalers on validation/test or feed payloads/identifiers
and targets back as forward conditions.

## Reproduction on Linux

Working root: `/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104`.
Use the existing `/home/iska/miniconda3/envs/tokengt/bin/python`; PyArrow and
RDKit are already present. No additional packages are required. Prefix commands
with `PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
MKL_NUM_THREADS=1 nice -n 15` and use a new immutable output directory each time.

```sh
python examples/synthetic_training/materials.py --parents 1024 --blocked-design --output outputs/datasets/new-aster-raw
python examples/synthetic_training/biomolecules.py --conformers 20 --include-peptides --output outputs/datasets/new-mora-raw
python examples/synthetic_training/curate.py --source outputs/datasets/new-aster-raw --output outputs/datasets/new-aster-curated
python examples/synthetic_training/package.py --source outputs/datasets/new-aster-curated --output outputs/datasets/new-aster-parquet
python examples/synthetic_training/dynamics.py --source outputs/datasets/new-aster-parquet --output outputs/datasets/new-aster-dynamics
python examples/synthetic_training/source_anchors.py --model aster --output outputs/datasets/new-aster-anchors
python examples/synthetic_training/combine_sources.py --source outputs/datasets/new-aster-dynamics --anchors outputs/datasets/new-aster-anchors --output outputs/datasets/new-aster-release
```

Apply the same curation/packaging/dynamics steps to Mora and select `--model mora`
for its anchors. `source_anchors.py` reads only the bounded existing source
packets and explicit public PDB downloads. It does not modify either model.
Use frozen `generation_source`, `parent_generation_source`, `dynamics_source`
and `anchor_source` snapshots for exact historical revision reproduction.

Checks:

```sh
python examples/synthetic_training/check_physics.py
python examples/synthetic_training/validate.py --dataset outputs/datasets/new-aster-release --output outputs/checks/new-aster.json
python examples/synthetic_training/check_dynamics_data.py --dataset outputs/datasets/new-aster-release --output outputs/checks/new-aster-dynamics.json
python examples/synthetic_training/check_native_interfaces.py --materials outputs/datasets/new-aster-release --bio outputs/datasets/new-mora-release --output outputs/checks/new-native.json
```

Native reader checks preserve computed-label status. Mora's current observed-only
scalar/array supervision gate rejects these computed targets; no relabeling or
production admission is performed. Aster condition-only tokenization is checked
with target-poison controls. Reader compatibility is not model training readiness.

## Upload and visualization

`upload_private.py` uses only the exact user-authorized HolonForge keys-file copy
under ignored `.private-credentials`, protected0700/0600. It never displays a
token, logs in globally or uploads a whole project folder. Explicit manifest
members/card are scanned, a NEW PRIVATE dataset repo is created, and remote
Git/LFS hashes, sizes, commit and private visibility are verified. Existing repo
collisions are refused. No original model/source secret is changed.

The explorer uses actual geometry/dynamics, CPK colors, SDF/XYZ exports, graph
wavelets, numerical Givens replay and checked Hubbard product-formula diagrams.
The larger release also displays MP20 CIF geometry and PDB1L2Y/1AZU/historical1HRW
residue contact subsystems, with full source-file downloads and scope labels.
Site-density splats are illustrative kernels, not ab-initio volumetric density.
Nuclear femtoseconds, dimensionless electronic time and circuit steps are separate
processes. Missing Bogoliubov compilation is explicit. No hardware/quantum
advantage or complete new Lean formalization is claimed.

The final `seal_release.py` pass adds origins to every dynamic configuration,
moves force diagnostics out of conditions and records zero assigned E/Z anchor
bonds. Source chemistry preserves formal charges, isotopes, chiral tags and
bond-stereo arrays in source atom order. Tetrahedral/CIP checks do not imply a
general E/Z geometry implementation for future data.

The initial failed drafts are preserved: independent review caught a BdG defect
breaking particle-hole symmetry and an odd-mesh gap guard; corrected versions
are the release candidates. A stale RDKit force-distance cache was identified
by NVE failure and corrected with same-coordinate energy/gradient refresh and
second-order step-refinement evidence. Failed artifacts are never substituted
for verified data. GRH and its independent positive arithmetic bridge remain open.

Verified private Aster release:
[GRH-Aster-TopoResponse-20261104](https://huggingface.co/datasets/AmelieSchreiber/GRH-Aster-TopoResponse-20261104)
at commit `2b8ce36571298a3517b8c88bb23269341d9b8908`. All configurations load through the official
`datasets` library with matching counts and origin columns. Other release
links and full remote Git/LFS receipts appear on the explorer after verification.

Verified private Mora release:
[Mora complementary conformer response](https://huggingface.co/datasets/AmelieSchreiber/GRH-Mora-ConformerResponse-20261104)
at commit `53a6b66acaa69ef79584648f3f6dc068363c4837`. Its complete remote file manifest is
verified; official-loader receipts are retained beside the release receipts.


## Spatial clouds, trained chemistry, games and analytic learning

The fixed private releases above remain unchanged. Additional reproducible
laboratories use separate `outputs/experiments/2026-11-04-*` namespaces:

- `orbital_transport.py`: five exact finite SSH/QWZ wave packets, full phases,
  currents, matched quenches and independently checked invariants.
- `train_torsion_flow.py`: eight actual MMFF periodic-chemistry readout/hybrid
  models. Final data are torsion-flow-v2; v1 remains preserved. Reverse DSM
  stops at positive heat time and is compared with that smoothed endpoint,
  not the unsmoothed flow target. No entanglement advantage is established.
- `electron_clouds.py`: coherent finite-Gaussian Coulomb H2plus and separately
  labelled effective Trp-cage fields. Full-space charge is proved; voxel,
  atlas quantization and saved-frame interpolation errors are explicit.
- `holomorphic_learning.py`: twelve actual q3/4/5 primitive-Dirichlet complex
  readouts, with conditional analytic budgets. High precision is not interval
  certification. The infinite-feature theorem concerns a specified readout,
  not every quantum architecture and not the GRH zero-location bridge.
- `train_quantum_games.py`: twelve finite CHSH/tilted/magic-square runs across
  three seeds. A stalled classical tilted optimum is retained. MIP*=RE is
  cited externally; these finite tensor strategies do not separate Cqa/Cqc.

`web/molecular-structure.mjs` parses local PDB/SDF connectivity, deposited
HELIX/SHEET records and explicit peptide links. Full-source atoms and modeled
contact subsystems are different modes; synthetic backbones do not acquire
invented secondary-structure labels. The cartoon avoids disconnected chain
bridges, including its spline controls.

Focused checks include `check_molecular_view.mjs`, `check_torsion_geometry.mjs`,
`check_orbital_transport.py`, `check_torsion_flow.py`, `check_electron_clouds.py`,
`check_game_models.mjs` and `check_hubs_spokes.mjs`; browser checks use the
existing isolated CDP9242 browser, sequentially. They write reports beneath
`outputs/checks/2026-11-04-synthetic-training`. Exact commands/arguments are in
these scripts and their preserved run logs. No new dependencies or active
HolonForge/Mora model changes were made.

Live views: `/datasets.html#electron-density-clouds`,
`/datasets.html#torsion-generative`, `/learned.html#certified-learning`,
`/learned.html#learned-games` and `/learned.html#hubs-spokes`.
The last tool illustrates disk/punctured-disk gluing with pinned HoTT
references and exact genus1/2/4 dessin permutations, not a new Lean4 HIT axiom.

Publication update: both dataset repositories and the GRH research repo/site
are now public at the owner's explicit request. Original private receipts
are historical; card-only public commits are in outputs/publication/2026-11-04.
All Parquet data remain frozen. No blanket source redistribution license is
implied by visibility. New certify_learning_constants.py provides deterministic
Fraction growth/tail certificates; latest output is rational-learning-v4.
Full interval sample and coefficient-rounding certification remain unfinished.
