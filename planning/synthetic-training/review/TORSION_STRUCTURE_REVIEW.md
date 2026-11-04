# Periodic chemistry learners and molecular ribbons: independent review

Reviewed2026-11-04: `train_torsion_flow.py` and its preserved v1 source,
`web/molecular-structure.mjs`, initial training log, and the revised source
while v2 CPU training/independent controls run. Only review files/evidence were
written. No remote host, credentials, model repository, training, dependency
installation or production edits were used by this reviewer.

Verdict: revised mathematical conventions and physical scope are accepted.
The initial positive-noise/reference/time-support mismatch and ribbon
connectivity issue were reported and source corrections independently inspected.
Final v2 circuit/gradient/oracle and browser-geometry receipts have now been
received and inspected (see the appended acceptance). This extension provides finite MMFF-based
torsion learning; it is not quantum chemistry, physical molecular-time evolution,
a model-admission action or an arithmetic/GRH result.

## The actual chemical target

Butane uses one carbon-chain dihedral on72 angular centers; pentane uses two
adjacent carbon-chain dihedrals on a24-by24 torus grid. Explicit hydrogens,
ETKDG seed, MMFF-minimized reference and all atom/bond/torsion indices are
recorded. Rotating the second pentane torsion leaves the first defining atoms
on its fixed side/rotation axis, so the sequential setters are compatible with
the two declared coordinates. Remaining bond lengths/angles are fixed by the
reference; these are not constrained free-energy surfaces after relaxing all
other molecular degrees of freedom.

For each grid point the code explicitly evaluates MMFF94 energy. Its finite
Gibbs weights are proportional to `exp(-(E-Emin)/kBT)` with300K and the stated
kcal/mol Boltzmann constant. The normalized finite mixture is then softened by
wrapped angular Gaussian noise with sigma `.05`rad. Thus the learned target is
a wrapped-Gaussian mixture of finite grid centers, not the exact continuous
`exp(-E(theta)/kBT)` density, solvent-dependent free energy, full conformer
equilibrium, molecular electronic density or experimental thermodynamics.
The source scope states these limits correctly.

## Periodic score DSM

Let `Y` be a draw from that softened target, `epsilon` standard normal and
`X_tau=wrap(Y+sqrt(2*tau)*epsilon)`. The source uses
`tau=.03+1.97*t`, target label `-epsilon/sqrt(2*tau)` and loss weight
`2*tau`. This is a valid denoising score-matching regression: conditional
expectation over the latent unwrapped displacement and all windings gives
`grad log q_tau` on the torus. Wrapping the noise label itself would generally
be wrong; the implementation correctly retains the latent real Gaussian noise.
Weighting by positive2tau changes relative time importance, not the conditional
population minimizer at any fixed time.

The forward heat generator is the torus Laplacian in tau. Descending heat time
by `d>0` gives reverse update `X <- wrap(X+2*d*score+sqrt(2*d)*z)`.
The source's factor two, variance and descending normalized time are consistent.
Starting with an actual target draw plus wrapped variance4 is the exact known
forward terminal law at tau2; it is a teacher-based initialization, not an
assumed exact uniform prior. Finite Euler sampling and learned-score errors
still require controls.

**Initial issue, resolved in v2 source:** reverse sampling stops at tau`.03`.
Even a perfect score therefore targets the softened mixture convolved with
additional wrapped variance`.06`, not the original `.05`rad-smoothed target.
Its total center variance is `.05^2+.06=.0625` (sigma`.25`). V2 now explicitly
records the positive-noise endpoint and uses its matching histogram reference.
The v1 source/output remains preserved. Score and flow endpoint TVs consequently
refer to different stated endpoint laws and must not be presented as a common
task performance ranking.

## Wrapped-geodesic flow matching

Independently sample uniform torus base `X0` and target `X1`; set
`V=wrap(X1-X0)` and `Xt=wrap(X0+t*V)`. Except for antipodal ties of probability
zero, this is the shortest product-torus geodesic with constant lifted tangent
velocity `V`. Conditional regression toward `V` is the corresponding flow
matching objective. Its population conditional velocity satisfies the marginal
continuity equation; finite neural fitting and128-step Heun integration do not
by themselves prove exact target sampling. Wrapping intermediate Heun positions
is consistent with periodic features and this torus chart convention.

**Initial issue, resolved in v2 source:** v1 trained both methods only at
normalized times `[.015,1]`, but flow generation evaluated smaller times near
the beginning and score generation evaluated smaller times near the end. V2
now draws training time over `[0,1]`; the positive score heat-time floor prevents
a zero-noise singularity. New output/source versions preserve the completed v1
experiment rather than silently rewriting it.

## Actual auxiliary quantum features and comparison scope

The hybrid starts in `|++>`, uses two layers of local input/time-dependent Rz,
trainable Ry and CZ, and evaluates eight exact Pauli expectations:
`Z0,Z1,X0,X1,Y0,Y1,Z0Z1,X0X1`. Tensor ordering and the `+2 Im` Y-readout
conventions are consistent. Every readout is periodic in each angle; Rz winding
global phases do not change expectations. The classical comparator instead
uses first/second sine/cosine harmonics. Both have64-tanh64-tanh heads, but
feature counts/parameter budgets are not identical in every dimension and
single-seed runs are not evidence of quantum advantage. These are classically
simulated auxiliary two-qubit feature circuits, not molecular electronic qubits,
coherent chemistry denoisers, ab-initio wavefunctions or hardware execution.
Generative time is distinct from femtosecond nuclear MD time.

Fresh local `check_torsion_math.py` AST-loads only the NumPy batch functions
with an array-returning tensor stub; no Torch/RDKit import is executed. It checks
10,000 actual source-generated batches for each method against independently
written displacement/noise equations, exact wrapped-mixture score finite
differences (max error `9.19e-11`), and literal two-qubit Pauli matrices against
all eight readout formulas (max error `1.67e-16`). Evidence:
`outputs/checks/2026-11-04-synthetic-training/review/torsion-math-review.json`.
This validates conventions; actual trained gate/gradient accuracy and sampler
refinement still need the root agent's separate executed controls.

## Peptide connectivity and ribbon boundaries

PDB parsing uses the first model, blank/A alternate policy, explicit atom/residue
mapping, TER segments and source HELIX/SHEET annotations. Standard residue
templates supply display connectivity; hydrogen/unknown-ligand proximity bonds
are expressly inferred display relations, not new chemical observations.
SDF uses explicit stored bonds and identifies peptide C-alpha/backbone motifs.
Its secondary structure remains unassigned rather than treating a synthetic
conformation as experimentally annotated helix/sheet. Ribbons are smoothed
cartoon geometry, not a new physical density or an inferred dynamics label.

**Initial issue, resolved:** a nearby disconnected SDF fragment could be joined
by a ribbon, and Catmull control points could reach across TER/segment breaks.
The revised `linked()` now requires actual peptide carbonyl-C to next-N
connectivity plus matching chain/segment and bounded CA separation. The same
predicate guards the spline's prior/next control points. The independent Node
`check_ribbon.mjs` confirms a connected-fragment positive control produces10
patches, nearby disconnected fragments produce zero, and a remote prior TER
segment contributes zero transverse excursion. Evidence: `ribbon-review.json`.
This is focused connectivity coverage, not exhaustive PDB/SDF format validation.

## Final evidence boundary

Before final numerical claims, inspect the v2 result/checkpoint/source hashes,
all eight actual run records, heldout-loss and finite-sampling qualifications,
independent circuit/autograd checks, exact periodic-score controls and sampler
refinement. Preserve poor metrics and differing endpoint laws. Current source
has no false quantum-chemistry, GRH, universal-convergence or quantum-advantage
claim. Existing private dataset release/loader receipts are separate from this
newly trained finite chemistry illustration and should retain their own hashes.

## Final v2 receipt acceptance

Inspected `torsion-verification-v2.json` and its independent checker source.
All eight trained models are covered. Independent Kronecker/Pauli discrepancies
are at most `6.67e-16`, quantum-parameter finite differences `3.53e-10`,
wrapped-mixture score finite differences `2.55e-8`, and oracle periodicity
`3.02e-14`. Learned-score MSE and zero-field baselines are retained, including
modest improvements and poorer cases; they do not imply quantum advantage.
The exact-score reverse controls use properly coupled nested64/128 Brownian
increments and correct positive-noise endpoint references. Their TVs include
finite256-sample error and discretization; no monotone-convergence theorem or
zero-noise recovery is claimed. Their sample count differs from the learned
2048-sample endpoint checks, so direct numerical ranking needs that distinction.

Inspected `torsion-browser-geometry.json`: intrinsic browser poses agree with
independent RDKit torsion assignments to `4.45e-15` angstrom and periodic torsion
values to `1.34e-15` radian. This supports bond-axis/downstream-atom geometry
implementation, not a claim of additional physical integration or equilibrium.
The focused ribbon regressions and all prior scope corrections remain accepted.
No required mathematical correction remains in the reviewed v2 implementation.
