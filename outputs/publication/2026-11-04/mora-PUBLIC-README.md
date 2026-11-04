---
pretty_name: Mora Complementary Conformer Response
language: en
license: other
task_categories:
- other
tags:
- synthetic
- physics
- parquet
- complementary-dataset
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*.parquet
  - split: validation
    path: data/validation-*.parquet
  - split: test
    path: data/test-*.parquet
- config_name: source_anchors
  data_files:
  - split: train
    path: source_anchors/train-*.parquet
- config_name: electronic_dynamics
  data_files:
  - split: train
    path: electronic_dynamics/train-*.parquet
  - split: validation
    path: electronic_dynamics/validation-*.parquet
  - split: test
    path: electronic_dynamics/test-*.parquet
- config_name: nuclear_md
  data_files:
  - split: train
    path: nuclear_md/train-*.parquet
  - split: validation
    path: nuclear_md/validation-*.parquet
  - split: test
    path: nuclear_md/test-*.parquet
---
# Mora Complementary Conformer Response

## Additional complementary scope
Atom/bond graphs, explicit-H coordinates, MMFF94 energies/forces/charges, recorded-reference denoising pairs and complete heavy-atom VR H0/H1.
This is an ADDITIONAL independent auxiliary corpus. It replaces no existing
training data, model, vocabulary or split. Both active model projects were
inspected read-only; no enrollment or neural optimizer update occurred.

## Data, format and intended tasks
22951 computed records; split counts: {'train': 22067, 'validation': 434, 'test': 450}.
Three Zstandard-compressed typed Parquet shards include native scalar/list/matrix
columns. `condition_*` fields are forward inputs, `target_*` are supervision,
and `evaluation_*` are excluded. The three JSON columns preserve the complete
lossless schema and task/provenance details; do not feed complete payloads or
record/group IDs into a model as a shortcut. Inverse tasks need an explicit
role swap and desired-condition contract, never hidden target access.

```python
from datasets import load_dataset
from huggingface_hub import dataset_info
# Public dataset: authentication is not required.
revision = dataset_info("AmelieSchreiber/GRH-Mora-ConformerResponse-20261104").sha
data = load_dataset("AmelieSchreiber/GRH-Mora-ConformerResponse-20261104", revision=revision)
print(data["train"].column_names)
```

## Generation and evidence
Seed20261104; Python3.11.6; NumPy2.4.6.
Exact source snapshots, parameter/units/evidence fields, `quality.json`,
`split-audit.json`, retained failure records where applicable, and SHA256
manifests accompany the shards. Deterministic simulations are independent of
the target neural models. Refer to validation and native-interface receipts
in the GRH project for actual checks and limitations.

## Splits and leakage
Whole-component greedy squared-deficit balance: row counts plus family/topology or molecular size/VR strata;80/10/10 targets; no component broken.
All parent/conformer/gauge/intervention and task descendants remain together.
Morgan radius2/2048bit Tanimoto>=.65, same nonempty Murcko scaffold and stereo-agnostic constitution form chemical components. A second all-conformer geometric closure joins identical heavy-element multisets at sorted pair-distance RMS<=.10angstrom.
Actual component-level family/topology (or size/VR) strata inform allocation.
Indivisible large components and rare strata prevent exact80/10/10 or complete
class coverage; distributions and cross-split nearest witnesses are reported.
These finite metric audits cannot prove all possible statistical independence
or prevent overfitting. Protein RMSD/TM-score or sequence-homology claims are
not made for these small-molecule/effective-model corpora.

## Limitations and native-model boundary
MMFF94 is an empirical molecular-mechanics method, not ab-initio or experimental biology. No affinity, ADMET, catalyst, therapeutic or clinical labels. Neutral/formal-charge graph states do not infer physiological protonation. Optimization convergence is not a proof of a unique/global minimum. Absolute MMFF energies are not cross-molecule atomization energies. Geometric persistence is a finite distance-filtration descriptor, not an electronic phase invariant.
Mora-3 scalar graphs can retain predicted/computed status. Its current ArrayTask rejects source_predicted targets for supervised projection. This is an explicit future admission-policy boundary; no label was changed to observed to bypass it.
Use as a method-labelled auxiliary/pretraining/fine-tuning source only after
the owning model's explicit source contract, normalization, task/mask and
evaluation review. No learned quality improvement has been measured.

## Rights and privacy
Public owner-controlled synthetic research release, published at the owner’s
request on 4 November 2026. No blanket redistribution license has been selected.
Public visibility does not replace the individual upstream source terms. No private model weights or credentials are included. Only the explicitly
authorized source-anchor excerpts/derivatives are included from prior training sources. Upstream software terms remain
separate from these computed outputs.

## References
- Fukui–Hatsugai–Suzuki, arXiv:cond-mat/0503172v2.
- RDKit MMFF94 and ETKDG documentation: https://www.rdkit.org/docs/
- Reproduction and contextual examples: GRH-research/examples/synthetic_training.

## Time-resolved configurations

`electronic_dynamics` adds occupations, charge modulation, bond currents,
connected density correlations and explicit pair sources on finite Hamiltonians.
Normal Slater dynamics conserves particle number; BdG mean-field dynamics has
a recorded condensate source. The Aster supplement also has an exact interacting
Hubbard dimer exchange/spin-swap benchmark, with coupling-ratio OOD splits.
The Mora pi-graph calculations use explicit **uncalibrated dimensionless**
parameters, not TDDFT or real molecular partial-charge predictions. Its separate
`nuclear_md` config uses0.05fs MMFF94 velocity Verlet,20fs trajectories, finite
energy/momentum checks and fixed charges. No solvent, redox, biological electron
transfer, equilibrium or experimental dynamics is asserted. All descendants
inherit parent groups; Hubbard coupling rescalings have ratio groups.

## Size and explicit data origin

The default configuration contains **22,951 static response/conformer
rows** before any time frames are counted. Separate source-anchor rows: 266.
Dynamics configurations count trajectories as rows, not each time step as an
independent system. Distinct parents and similarity components are reported.

`origin_class`, `planned_source_dataset`, `planned_source_record_id` and
`label_origin` distinguish reused planned-source identity/geometry, new public
structure anchors and newly computed/synthetic labels. The default source is
new simulations; novelty of chemical identity against all existing corpora is
not asserted. Source-linked variants are additional computed data, not newly
measured experimental or ab-initio labels.

`source_anchors` is **train only**. Existing Aster MP20 and Mora PubChem source
training assignments are respected. Public PDB coordinate anchors retain
CC0/DOI/hash and a qualified relation to the planned structural source family;
no PDBbind affinity or measured CISS label is copied. Quantum-transfer models
constructed on their graphs are uncalibrated effective models. Source structures
are not proofs of those quantum properties. A molecular source parent and all
its variants are excluded if they conflict with any frozen default validation/test
identity, scaffold, Morgan>=0.65 or applicable all-conformer heavy-distance
descriptor<=0.10angstrom. The source-cross-configuration audit records witnesses;
excluded data remain preserved in the parent packet, outside release shards.
Retained parent derivatives remain together. These anchors cannot establish blind model performance when their
parents may already have been seen. Global cross-corpus exposure and broader
chemical/protein similarity admission remain the owning model's evaluation
gates, separate from the within-release component audit.

## Final release audit

Exact configuration counts: `{"data":{"test":450,"train":22067,"validation":434},"electronic_dynamics":{"test":88,"train":84,"validation":69},"nuclear_md":{"test":4,"train":4,"validation":4},"source_anchors":{"train":266}}`.
Every configuration carries explicit origin fields. Source-anchor finite-difference
diagnostics are evaluation metadata, excluded from forward conditions. All emitted
assigned tetrahedral/CIP geometries were checked; selected PubChem anchors have
zero assigned double-bond E/Z tags. Historical PDB1HRW is explicitly obsolete and
superseded by1LE0; actual downloaded HEADER identity and source bytes are retained.
`validation/` retains all-row physics and source-boundary receipts. Final manifest
hashes pin the corrected row schema and all released evidence. No peptide-fold
blindness or full prior-model exposure audit is claimed.
