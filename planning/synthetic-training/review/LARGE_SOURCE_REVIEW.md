# Large release and source anchors: independent review

Reviewed 2026-11-04, read only. New scope: `source_anchors.py`,
`combine_sources.py`, the blocked material proposal, peptide-library expansion,
`package.py`, circuit/wavelet helpers in `visual_examples.py`, both
`papers/complementary-datasets-*.tex` manuscripts and new validation receipts.
No credentials, model repositories, remote host, PyArrow/RDKit installation,
production edit or upload was used by this reviewer.

Status after revised-source/receipt inspection: the mathematical/physical
interpretation is accepted within its stated effective-model scope. All three
initial source provenance/curation findings below are resolved. Final source and
large dynamics receipts now pass. A small forward-role cleanup and precise
tetrahedral-versus-bond-stereo wording were communicated below; private upload
verification remains separate release evidence.

## Concrete items sent to the root agent

1. **PubChem-anchor stereochemistry and label validation.** The first
   `pubchem()` implementation lacks the revised main generator's post-MMFF
   `graph_stereo_ok` reference check and any perturbed-geometry check at sigma
   `.02/.05`. Fully specified input SMILES and ETKDG enforcement alone do not
   verify minimized/noisy geometry. Apply the existing graph/CIP checks to all
   accepted anchor geometries, reject and retain failures, and validate finite
   energy/forces and force finite differences. This is an unverified condition,
   not a measured chirality failure in a downloaded row.

2. **Cross-configuration split claims.** Source anchors are train only, but the
   initial combine operation does not compare their chemistry with default
   validation/test components. The new `existing-mora:` group hashes do not
   automatically unify a reused source identity/scaffold with the same or
   sufficiently similar default heldout identity. Run same-constitution,
   scaffold and declared fingerprint/geometry comparisons and quarantine
   conflicts, or create explicit corrected combined assignments/exclusion masks
   in a fresh artifact. Until then, scope the no-crossing statement to the
   default corpus and each anchor lineage separately. Prior model exposure is
   an additional problem; disclosing that separate limitation does not itself
   prove within-release separation when configurations are combined for use.

3. **Historical PDB 1HRW.** Official RCSB records say
   [1HRW is obsolete](https://www.rcsb.org/structure/removed/1HRW) and
   [1LE0 supersedes it](https://www.rcsb.org/structure/1LE0). Verify the actual
   downloaded PDB HEADER identifier and any redirect. If historical bytes are
   retained, record obsolete/replacement metadata; if the endpoint supplies
   replacement bytes, name the actual entry/DOI and retain the requested legacy
   identifier and retrieval resolution separately. Preserve the original blob.
   The manuscript should say historical Trpzip1HRW, superseded by1LE0, rather
   than presenting it as an unqualified current entry.

## Accepted size and proposal interpretation

The generation/curation receipts report 16,384 default material rows from
1,024 parents per each of six families, and22,951 molecular rows from517
accepted molecular parents after adding designed peptides and requesting20
conformers. These counts exceed10,000 without counting individual time samples
as independent rows. The record count does not imply that every controlled
variant or nearby parameter draw is a statistically independent physical
system. The manuscripts state that distinction.

The blocked material proposal adds disclosed bounded jitter around separated
parameter blocks; it preserves the original Hamiltonian definitions and
corrected gap/BdG guards. It changes the proposal distribution, not the physical
theorems or a claim of uniform coverage. Peptides come from explicit RDKit
sequence-to-graph construction, not measured sequences/functions or a
physiological protonation inference. All designed dipeptides and the additional
short sequences have the same MMFF/finite-geometry scope as the small-molecule
corpus. The manuscript correctly discloses the dominant connected peptide
training component and consequent lack of broad heldout peptide coverage.

The received `mora-large-validation.log` reports all22,951 records passing
hash/projection, parent/component separation, exact energy/force recomputation
and geometry/graph stereochemistry checks, plus ten mirror controls and36
independent VR checks. It reports31 final components and split sizes
`22067/434/450`, Morgan maximum `.6470588235294118` and minimum sorted-distance
descriptor separation `.10036206843038423` angstrom. These are threshold-relative
within-default-corpus results, not global historical-exposure certificates.
The reviewer inspected the receipt rather than rerunning remote RDKit.

## Source provenance and physical scope

The MP20 anchors read48 existing Aster source-training structures without
changing their data. Source-row and source-file hashes and original assignments
are recorded. Strain, vacancy and synthetic link phases produce new explicitly
dimensionless finite neighbor-compression Hamiltonians, symmetrized as stated.
They are not new crystal measurements, Wannier/DFT fits, calibrated magnetic
fields, formation energies or material phase labels.

The32 PubChem anchors reuse admitted source-training identities but create new
ETKDG/MMFF geometries and force labels. A representation-source admission does
not imply force-array supervision admission or prior model exposure. Source
revision/payload/shard hashes remain distinct from new computed labels. Both
anchor families are visibly separate train-only configurations. The source
selection and display do not establish chemical novelty against all corpora.

Eight PDB snapshots retain raw bytes, URL, DOI, hash and residue/atom mapping.
The first model/first CA chain, capped32-residue subsystem, is a declared source
coordinate anchor. NMR model order is not time. A one-orbital spinless contact
Hamiltonian based on distances is uncalibrated and cannot produce measured
CISS spin polarization or biological electron-transfer rates. A pure mirror
preserves every distance and hence this Hamiltonian: the model is incapable of
chirality-dependent spin selectivity by construction. Mirror counterfactuals
are therefore controls, not CISS predictions. The manuscripts explicitly retain
this boundary.

The [official wwPDB policy](https://www.wwpdb.org/about/usage-policies) confirms
CC0 for archive data and encourages original-author attribution. Direct source
checks confirmed [Trp-cage1L2Y](https://www.rcsb.org/structure/1L2Y) and
[villin1VII](https://www.rcsb.org/structure/1VII) identities/method context.
The [CISS review v1](https://arxiv.org/abs/2108.09998v1) and
[chiral-bridge preprint v1](https://arxiv.org/abs/2205.05353v1) metadata and
abstract scope match the qualified manuscript citations. No independent
reproduction of those experiments is asserted.

## Dynamics, circuits and visualization mathematics

The existing independent normal/BdG/Hubbard Fock checks remain applicable.
`check_dynamics.py` now additionally second-quantizes every emitted adjacent
Givens and orbital-phase gate into a full16-state Fock circuit, independently
comparing with `exp(-it sum h_ij c†_i c_j)`. Maximum discrepancy is
`9.31e-16`. The manuscript Givens block, reconstruction order, vacuum/single/
double-occupation action and determinant factor are correct. This certifies
the tested finite normal compiler; the manuscript does not promote it to a
BdG or interacting Hubbard compiler. The latter has its own explicit
Jordan--Wigner/product-formula calculation.

Graph heat wavelets `s L exp(-sL) delta_i` have zero sum for the stated
symmetric combinatorial Laplacian; independent checks pass. Signed wavelet
values are not probabilities. Gaussian kernels displayed around atomic sites
are illustrative splats on discrete occupations, not electronic-structure
volumetric density. A time coordinate in a4D projection adds a display axis,
not a physical spatial dimension. These qualifications appear in the manuscripts.

The received cache-corrected MD probe gives drift ratios `3.9769..4.0018` on
halving steps `.1→.05→.025` across four systems, consistent with second-order
behavior for the tested setup. The small MD validation receipt reports12
trajectories, maximum drift `.0065795995380923955` kcal/mol and zero discrepancy
on recomputed energies/forces. Current large-source generation explicitly calls
`.05`fs for400 steps; its row metadata and final receipt must be used when
reporting that run. The reviewer did not rerun nuclear MD locally. Fixed-charge
MMFF nuclear motion remains separate from uncalibrated electronic-time pi
dynamics, not self-consistent coupled electronic/nuclear quantum dynamics.

## Remaining release evidence

Verify corrected source-anchor row counts and hashes, all accepted anchor
stereochemistry/force checks, cross-configuration conflict/exclusion report,
large material/dynamics all-row checks, final configuration schemas/actual MD
metadata, card/manifest correspondence and private remote upload hashes/commit.
This reviewer does not access credentials or authorize a new model admission.
Observed/predicted/computed evidence boundaries, read-only active repositories,
and the absence of new GRH/whole-book-formalization claims remain appropriate.

## Final source correction reinspection and receipts

Read the revised `source_anchors.py`, `combine_sources.py`, independent
`check_sources.py` and all four requested fresh source/large-dynamics logs.
No remote execution or credential access was performed by the reviewer.

The three initial source findings are resolved:

- PubChem references and every accepted perturbation now pass graph-assigned
  atom CIP/relative tetrahedral checks; invalid/nonfinite/high-energy cases are
  rejected, sampled finite-difference force checks are recorded, and full atom
  order/formal charges/isotopes/chiral tags/bond stereo data are retained.
  The independent checker reconstructs the graph in stored atom order, verifies
  canonical identity/CIP and recomputes every accepted MMFF energy and force.
- Combining packets now compares every molecular anchor variant with all
  default heldouts for constitution, nonempty scaffold, Morgan threshold and
  applicable heavy-element/sorted-distance descriptors. Any conflict quarantines
  the whole anchor source parent, leaving frozen heldouts unchanged. Independent
  final checks repeat the retained-row comparisons. The reported maximum
  Morgan similarity is `.32075471698113206`, with no applicable equal-element
  geometry pairs; `null` geometry is absence of such comparisons, not a measured
  separation distance. Zero crossings is substantiated for these declared
  within-release metrics, not global prior-model exposure.
- Actual historical `1HRW` bytes have HEADER `1HRW`; source metadata explicitly
  marks obsolete status and replacement `1LE0`, preserves requested/actual ids,
  DOI and file checksum. The independent checker verifies HEADER identity and
  replacement metadata. No silent replacement identity is asserted.

`mora-sources-validation.log` reports266 retained anchors over40 groups:74
accepted MMFF rows from32 reused source identities, plus192 CA-contact rows
from eight PDB sources. MMFF energy/force reconstruction errors are exactly zero;
all source anchors are train only and all file hashes pass. The lower molecular
row count correctly reflects rejection gates rather than inventing three valid
rows for every parent. `aster-sources-validation.log` reports576 anchors over24
inherited source groups from48 source structures, with all hashes and train-only
assignments checked. PDB/MP20 effective models are distinct from molecular-MMFF
geometry tasks; molecular-specific zero/error fields in the Aster receipt are
vacuous/N/A, not actual molecular tests.

The large dynamics receipts report241 molecular electronic trajectories with
723 independent exponential checks,12 MD trajectories with zero energy/force
reconstruction discrepancy and maximum drift `.0025390291324072223` kcal/mol;
and174 Aster trajectories with522 independent exponential checks. Aster has156
inherited-static trajectories plus18 separately grouped exact Hubbard controls.
Maximum density/pair-source errors are `4.56e-15` for Mora and `7.15e-14` for
Aster. Independent continuity residuals are below `1.65e-15`; all reported
manifests and no-native-model-change checks pass. These are inspected root-run
CPU receipts, supplemented by the reviewer's separate small-Fock tests.

Two narrow cleanups were communicated during this last read:

1. `gradient_finite_difference_error` is currently placed inside a PubChem
   anchor's conditions. Move this label-derived validation diagnostic into an
   evaluation/payload field, or explicitly exclude it in the forward reader.
   The physical force labels remain valid; this preserves the manuscript's
   input/target/evaluation role contract.
2. `graph_stereo_ok` validates atom CIP/tetrahedral geometry; stored bond E/Z
   tags are preserved but not independently assigned from coordinates by that
   function. If accepted source parents contain assigned E/Z bonds, check their
   geometry or qualify the all-stereochemistry receipt accordingly. A count
   of zero assigned E/Z bonds also settles this scope point.

Private repository creation, visibility, uploaded commit and remote file hash
correspondence remain outside this reviewer's permissions/execution scope and
must be reported from the root agent's final upload receipts.

## Root release cleanup evidence

The immutable release-v2 pass (`seal_release.py`) moves the finite-difference
validation diagnostic into `payload.evaluation`, outside scientific conditions.
The selected PubChem anchor rows have zero assigned E/Z bonds; source arrays
still preserve bond stereo for reconstruction. Final source validation freshly
reconstructs the corrected graph/condition schema and passes. This resolves the
two narrow role/scope cleanup items; it does not generalize the CIP check into
a geometric E/Z checker for future sources. Evidence:
`outputs/checks/2026-11-04-synthetic-training/review/release-cleanups.json` and
`mora-final-source-validation.json`. This paragraph is the root's integration
note, separate from the reviewer's independently executed checks above.
