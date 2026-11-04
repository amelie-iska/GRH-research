# Additional complementary training datasets

These are two new auxiliary corpora. They replace no model, dataset, split,
checkpoint, vocabulary or training process. Both active model repositories are
read-only reference sources. Generation and uploads belong to the GRH project.
No GPU job, installation or model training is required for generation.

## 1. Aster: topological response and intervention atlas

The current HolonForge/Aster tokenizer supports nonchemical sites, Hamiltonian,
band, noise and observable tracks. Existing sources emphasize actual structures
and their computational properties. Add independently calculated effective-model
response pairs: SSH, Rice–Mele pumps, Kitaev wires, QWZ Chern insulators, Harper
photonic strips and finite high-genus dessin spin RG. Preserve conventions,
Hamiltonian parameters, meshes, spectra, open-boundary responses, invariants,
counterfactual perturbations and numerical checks. No fictitious atom species,
CIFs, synthesizability, experimentally realized phase or DFT label is inferred.

Forward tasks predict responses from model/boundary/noise conditions. Inverse
tasks condition on desired response with parameters as targets. Invariants and
target spectra must never enter a forward condition through text or metadata.
Gauge/size variants and intervention pairs share one parent split. Parameter-
group heldouts and separately labelled family OOD tests assess interpolation
versus family transfer. Gapless or unresolved topology remains unavailable.

## 2. Mora-3: conformer forces and geometric response

The current Mora-3 code has typed atom/bond graphs, conditional scalar fields,
ordered numeric axes and explicit condition/target/evaluation roles. Add a
chemically sanitized set of molecular building blocks and designed amides with
multiple stereochemistry-preserving conformers, local MMFF94 minima and bounded
displacements. Store atom order, bonds, coordinates, energies, analytic forces,
force-field partial charges and finite Vietoris–Rips persistence descriptors.
Tasks cover force/energy prediction, denoising toward the recorded local minimum,
and geometry/topology-conditioned conformation generation with known chemistry.

These are MMFF94 computational labels, not ab-initio energies, affinity, ADMET,
catalysis, clinical effects or experimental biomolecular ground truth. Preserve
protonation/stereochemical assumptions and unsupported/minimization failures.
All conformers and perturbations of a molecule stay together; scaffold and
fingerprint similarity components define additional conservative split groups.
Current Mora-3 ArrayTask permits only `observed` targets: do not relabel computed
targets to bypass this rule. Test its rejection and supply an explicit candidate
handoff requiring the owning model's future synthetic-source admission policy.

## Curation and release gates

Use existing pinned NumPy/SciPy and remote RDKit, one low-priority CPU thread.
Keep source code and parameters/seeds fixed; fresh immutable output directories.
Validate Hermiticity, eigensystem residuals, topology mesh convergence/gauge
invariance, exact reference cases, force finite differences, rigid invariance,
nonfinite/missing masks, group separation and target exclusion. Retain failures.
No fitted network is the physics oracle. Dataset construction is not model
admission or training, and neither dataset supplies the GRH arithmetic bridge.

Create two private Hugging Face dataset repositories with dataset cards,
checksummed manifests, splits, code and quality/limitation reports. Use only the
user-authorized protected copy of HolonForge's exact keys file; never display,
commit or upload it. Upload an explicit allowlist, not the whole project.
Verify private visibility and remote commit/hash correspondence. Add a contextual
interactive dataset laboratory and integrate the explanation into the book.

Primary implementation references: Fukui–Hatsugai–Suzuki,
arXiv:cond-mat/0503172v2; RDKit MMFF/ETKDG API documentation; PennyLane
differentiable quantum chemistry and Strawberry Fields Gaussian examples;
Hugging Face repository/upload documentation. Record exact fetched source
versions/hashes and actual review coverage in the evidence ledger.

## Large release acceptance and origin amendment

User minimum:10,000 actual static records per additional corpus; do not inflate
counts with time frames. Executed defaults16,384/22,951, with6144/517 parent
systems. Every default/dynamic/source row carries origin metadata; planned MP20
geometry, planned PubChem identity and new public PDB anchors are distinguished
from new synthetic labels. Neither source presence nor chemical design proves
novel identity relative to all prior corpora.

Additional gates resolved by release-v2: source geometry CIP/force checks,
explicit formal charges/isotopes/chiral tags/bond stereo and atom order; all
Mora anchors versus frozen default heldout constitution/scaffold/Morgan and
applicable all-conformer geometry; parent quarantine if conflict; diagnostics
outside forward conditions; zero assigned E/Z bonds in selected PubChem anchors.
Historical PDB1HRW actual HEADER and1LE0 replacement are recorded.

Source receipts and source/model scopes stay visible. Future material/biological
performance validation and native source admission are outside dataset delivery;
no active training or repository is altered. Full GRH and full-book Lean gates
remain unresolved.
