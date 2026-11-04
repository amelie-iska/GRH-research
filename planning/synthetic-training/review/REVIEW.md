# Independent synthetic-dataset review, 2026-11-04

Status after source reinspection: the five requested corrections below are
implemented in the revised source. Focused local regressions confirm corrected
QWZ null decisions and all three Kitaev variants' particle-hole symmetry. Final
static all-row/native execution logs are now received and pass; final combined
dynamics/upload receipts remain a release gate. The initial v1 data and
scientific counterexamples stay preserved. This is an
additional-data review, not authorization to alter either active model repository.

## Scope and execution boundary

Read `DESIGN.md`, `common.py`, `materials.py`, `biomolecules.py`, the first
`curate.py` implementation, both v1 manifests/quality/split audits and their
example JSON files. Verified all thirteen manifest-listed local file SHA256 and
size values. Local NumPy/SciPy checks used the existing Mac scientific environment.
No remote host, GPU, credentials, model repository, MCP server or package install
was used. Local PyArrow and RDKit are absent: no independent all-row Parquet or
MMFF execution is claimed.

Reproduction:

```sh
.tools/book-quantum-cpu/bin/python -B planning/synthetic-training/review/check_math.py
```

Evidence is `outputs/checks/2026-11-04-synthetic-training/review/math-review.json`.
The script verifies accepted cases and records the actual failing scientific
counterexamples; `completed=true` does not mean the dataset release passed.

## Required corrections communicated

1. **Kitaev boundary defects violate the declared BdG symmetry.** The original
   finite basis is particles followed by holes. With `C=[[0,I],[I,0]]`, its
   correct constraint is `C H.conj() C = -H`. The base matrix passes. The initial
   defect adds `.15` to particle site zero and subtracts `.1` from the final
   hole site, without their matching particle/hole partners. Its residual is
   `.15`. A physical onsite defect must have opposite diagonal entries at the
   same particle/hole site. Preserve initial v1, and either create corrected
   rows in a fresh version or explicitly exclude the unconstrained-Hermitian
   diagnostic rows from physical Kitaev training. Hermiticity alone is
   insufficient here.

2. **Odd Chern meshes miss true QWZ gap closures.** At mass zero, the 17/33
   meshes report Chern `+1` on both meshes and gaps `.3691/.1903`, so the initial
   guard accepts a gapped phase although the continuum bulk closes at `(pi,0)`
   and `(0,pi)`. At mass two it accepts Chern zero with mesh gaps `.5242/.2695`
   despite closure at `(pi,pi)`. For this exact QWZ model use the analytic gap
   `2 min(|mass+2|, |mass|, |mass-2|)` for the gap/availability policy; retain
   mesh gaps as separately named finite-grid diagnostics. Agreement of two
   mesh integers is not a bulk-gap certificate.

   Following the initial generator's deterministic random-number consumption,
   parent 58 has mass `.03269341357763622`, true gap `.06538682715527244` and
   mesh-33 gap `.20416748772758664`; parent 82 has mass
   `.03026983176640119`, true gap `.06053966353280238` and mesh-33 gap
   `.20245044680487076`. Both are incorrectly available under the stated
   `gap > .08` robustness rule. Their three descendant rows each require the
   corrected null policy in any revised dataset.

3. **Stratum counts do not implement stratification.** Initial
   `assign_components` balances total rows only. Initial curation computes
   `stratum_counts` after allocation but does not use them to choose splits.
   The requested stratification needs a component-level multi-stratum
   allocation that considers family/topological class, plus honest reporting
   when rare labels or oversized indivisible components make coverage
   impossible. Otherwise describe the output as component-heldout with a
   stratum audit, not stratified.

4. **Recompute split-dependent audit values after geometry curation.** Initial
   curation updates `final_component_allocation` but retains the old top-level
   component count, row counts, largest-component count and exact
   `cross_split_max_Morgan_Tanimoto`. Since it reallocates merged components,
   these can become stale. Namespace the parent audit or update all final
   values and recompute the Morgan cross-split maximum. The `<.65` guarantee
   survives indivisible chemical components; the exact old maximum need not.

5. **Check minimized reference stereochemistry against the specified graph.**
   Initial `chirality_ok` tests perturbed coordinates only against the already
   minimized reference. ETKDG enforces input chirality during embedding, but
   the stated stereochemistry-preserving dataset also needs validation after
   MMFF minimization. Compare geometry-assigned stereochemistry to the input
   chiral graph or compare against pre-minimization tetrahedral orientation.
   Reject/retain failures explicitly. This is a missing validation, not an
   observed chirality flip in the inspected example JSON.

## Revised-source reinspection

The initial generator sources were preserved under
`examples/synthetic_training/archive/initial-v1/`. The revised material source
pairs each Kitaev onsite defect and canonical gauge phase with its hole partner
and asserts particle-hole symmetry. Fresh in-memory generation/reinspection
finds zero PHS residual for base, gauge and defect. It uses analytic QWZ and
Rice--Mele gaps, even 32/64 meshes and a conservative Harper mesh Lipschitz gap
lower bound. All twelve QWZ descendants in the four critical/small-gap regression
cases now carry `chern=null` as required. The Harper bound subtracts
`2*pi/n*(hopping+2*onsite)`: nearest-grid distances are at most `pi/n` per
coordinate, matrix derivative norms are bounded by `hopping,2*onsite`, and the
eigenvalue gap changes by at most twice the matrix norm change. It is correctly
qualified as floating numerical evidence rather than an interval certificate.

`assign_components` now evaluates a squared-deficit objective for total rows and
family/topology or molecular-size/VR strata, retaining entire connected
components and explicit rare/large-component limitations. Initial curation's
stale values are now namespaced in `parent_audit`; final allocation values and
cross-split Morgan maximum are updated/recomputed. `graph_stereo_ok` reconstructs
geometry-assigned CIP labels and compares them with graph CIP labels before
accepting minimized molecular references. These source changes address the five
findings; final all-row results and graph-stereochemistry positive/negative
runtime controls must still substantiate the produced new-version release.

## Accepted mathematics and limited claims

The complete edge/triangle boundary reduction computes finite Euclidean
Vietoris--Rips H0/H1 over F2 with face-before-coface ordering. The unit square
gives three H0 bars `[0,1]`, one essential H0 class and H1 `[1,sqrt(2)]`.
Fresh tests verify rotation, translation and point-permutation invariance;
all three saved biomolecule examples' heavy-atom persistence records reproduce.
Zero-length bars are intentionally omitted. No higher homology, protein-fold
classification or physical topological phase is inferred from these descriptors.

The Chern link orientation is explicit. For the lowest QWZ band the code returns
zero at masses `-3,+3`, minus one at `-1`, plus one at `+1`, with random-gauge
errors below `7e-16` in the tested cases. Fourier reconstruction of both QWZ
and Rice--Mele strip onsite/hopping matrices agrees with the stated bulk Bloch
Hamiltonians. The strip uses fixed `ky=.37`; the saved bulk curve is a separate
`ky=0` slice and should have that axis/slice metadata made explicit. The
independently derived QWZ analytic gap exposes the critical-point issue above.

The finite dessin RG marginal uses exact summation/logsumexp over two eliminated
black spins; normalization and dimensionless effective-model scope are
consistent. The physical models are synthetic effective Hamiltonians, not DFT,
experimental realizations, CIFs, calibrated material response or a GRH result.

Molecular labels are MMFF94 finite force-field calculations. Forces correctly
use minus the analytic coordinate gradient; reference minimization convergence,
finite-difference samples, rigid energy/force covariance and rejected cases are
recorded. Absolute energies are explicitly not cross-molecule atomization
energies. Charges are force-field charges, not measured charge transfer. Local
basin-paired denoising targets are not claimed unique global minima or thermal
conformer samples. Scientific validity still depends on the missing
post-minimization stereochemistry check and final all-row remote evidence.

Transitive similarity closure correctly keeps all accepted edges within a
component; a fresh toy test confirms transitivity and indivisible assignment.
All molecular descendants are initially grouped by parent, stereo-agnostic
constitution, nonempty Murcko scaffold and Morgan radius-two similarity at
`.65`. Additional all-emitted-conformer sorted-distance grouping is invariant
to rotation/translation/permutation and conservative as stated. It is not a
complete congruence invariant, an optimized element-aware RMSD, a protein
TM-score or universal independence guarantee. Chemistry/physics family and
declared thresholds must remain visible in leakage claims.

The current conditions/targets JSON roles are separate and evidence remains
`synthetic_computed`. The Mora native `observed`-only boundary must not be
bypassed by relabeling. Native-reader tests, private Hugging Face visibility,
upload commit/hash checks and final all-row split witnesses are root-agent
release gates, outside this initial local check.

Primary source spot checks used the pinned [Fukui--Hatsugai--Suzuki v2](https://arxiv.org/abs/cond-mat/0503172v2)
metadata/abstract and official [RDKit force-field](https://www.rdkit.org/docs/source/rdkit.Chem.rdForceFieldHelpers.html)
and [distance-geometry](https://www.rdkit.org/docs/source/rdkit.Chem.rdDistGeom.html)
API documentation. These support API/method context; they do not certify
generated labels, unseen-chemistry performance or learning outcomes. Live
documentation is newer than the dataset's recorded RDKit 2026.03.1; the saved
engine/version and exact sources remain the reproduction authority.

## Received final static validation evidence

Inspected `materials-validation-final.log`, `biomolecules-validation-final.log`
and `native-interfaces-final.log` under the check directory. These are root-run
remote CPU receipts, not independent remote reruns by this reviewer. They report
1,536 materials rows, 288 particle-hole checks and 18 near-critical QWZ null
rows; 1,495 molecular rows with exactly reproduced MMFF energy/forces, all
geometry/graph stereochemistry checks, ten mirrored negative controls and
36 independent VR rank checks. Both report manifest/projection and whole-parent/
component split checks passing. Final molecular Morgan maximum is `.625` and
minimum cross-split sorted heavy-distance descriptor separation is
`.10334350577838568` angstrom, exceeding the declared `.10` threshold.

The native-interface receipt confirms Aster condition-only target-poison
invariance for all six families and Mora rejection of computed scalar/array
targets, with evidence labels retained and inspected model-source hashes
unchanged. This substantiates compatibility/admission boundaries rather than
model enrollment, optimizer changes or performance gains. Final observed static
split sizes are Aster `1138/198/200` and Mora `1172/149/174` for
train/validation/test; exact80/10/10 ratios are not claimed.

## Electronic/BdG/Hubbard dynamics extension

Independently inspected `dynamics.py` and wrote `check_dynamics.py`. Because
PyArrow/RDKit are absent locally, the checker AST-loads only the pure NumPy
`electronic` and `hubbard` functions. It constructs annihilation/creation
operators and full16-state Fock Hamiltonians independently. Normal Slater and
complex-pairing BdG trajectories agree on occupations, direct bond-current
expectations, connected density correlations and independently evaluated pairing
sources to below `3.8e-15`. Exact Hubbard tests at `U/t=2,8,16` agree on the
N=2 Hamiltonian, occupations, current operators, correlations and spin-swap
probabilities to below `1.1e-14`. Evidence is `dynamics-review.json`.

The conventions are consistent: `P_ij=<c†_j c_i>`, `Psi=(c,c†)`,
`R=<Psi Psi†>`, `R0=diag(I-P0,P0.T)`, `P=I-R11` and
`F=R12=<c c>`. Current leaving site i is
`J_i->j=-2 Im(h_ij P_ji)`. Off-diagonal Gaussian number covariance is
`|F_ij|^2-|P_ij|^2`; its diagonal is `n_i(1-n_i)`.
The BdG pairing source is independently
`-2 Im diag(Delta F†)`, with `Delta=H12`. The initial source/residual was
defined tautologically from continuity. **Resolved:** source now uses this
independent formula and compares to the actual commutator-derived time
derivative. Hubbard currents now also use independent number-operator
commutators and are compared against probability derivatives.

The Hubbard exchange gap matches the singlet/triplet gap
`(sqrt(U^2+16t^2)-U)/2`; the finite interacting dimer is separate from Gaussian
Wick exchange and from Coulomb exchange-energy calculations. Scale variants
share a coupling-ratio group and high-ratio validation/test are expressly OOD
coupling holdouts. Idealized molecular pi-orbital dynamics use uncalibrated,
dimensionless parameters, half filling and spinless fermions. The text excludes
TDDFT, real molecular charge transfer, redox and biological efficacy; those
exclusions are material to interpreting the result.

No nuclear MD trajectory is certified by this reviewer. Initial failed drift
records remain preserved, and the root agent identified a stale RDKit distance
cache when calling gradients without refreshing energy at each position. The
source was corrected to refresh energy before force evaluation. Final refined
energy/momentum trajectories, new combined dataset manifests and private upload
receipts still need their own passing evidence. The model repositories and
synthetic-admission boundaries remain unchanged.
