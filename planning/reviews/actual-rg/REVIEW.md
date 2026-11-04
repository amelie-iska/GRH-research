# Independent actual-RG and quantum TokenGT review — 2026-11-03

Reviewer: `/root/persistence_tool_review`. Reviewed the actual RG mathematics,
training/export code, browser model and shared TeX; also the subsequent
quantum-TokenGT model, training, saved-record checker, cellular CSS diagnostic
and exposition. Only this report and authorized reviewer artifacts were written.
No training, browser navigation, dependency/configuration change or Git mutation
was performed. Checkers were executed with output destinations redirected in
memory to `outputs/checks/2026-11-03-actual-rg/review/`, preserving prior outputs.

## Effective-action and quantum semantics

The redesigned K2,m teacher is actual finite decimation on the clean dessin's
incidence graph. Summing both black spins gives the two stated logcosh terms
and retains the white fields, every generated Walsh interaction and constant.
Nested marginalization preserves the raw partition and retained observables.
The matched order has m quiver vertices and DVR rank2m²; the spin model instead
has m+2 sites and2m incidence edges. The TeX correctly distinguishes these
objects and notes that the abstract incidence graph does not recover its
higher-genus ribbon embedding. The three varied controls tie the edge couplings;
the32 predicted actions are not32 independently varied input controls.

The homogeneous transfer-matrix formulas for K',h',C' solve all three matrix
entry equations correctly. The even64-site periodic benchmark preserves its
partition and doubles spacing. It is correctly separated from odd dessin
examples. Correlation length here means the transfer-eigenvalue-ratio length
of the homogeneous extension, rather than a fitted decay length on a final
one-site ring. The browser restricts K≥0; its log-eigenratio transport is
appropriate on that ferromagnetic domain and avoids late-scale underflow.

Quantum elimination uses the unnormalized partial trace of exp(−βH), followed
by the Hermitian spectral logarithm, retaining the identity coefficient.
Finite nonzero Hilbert spaces and β>0 give strictly positive reduced weight.
These dimension hypotheses are now explicit in the theorem text; this review
condition is resolved. The correlation-length homogeneous-extension qualifier
is also now explicit. Tensor ordering is consistent:
black0,black1,white0,…, with the first wire most significant. The complete
Pauli expansion, composition of partial traces, partition and retained static
observables have the right meaning. The effective Hamiltonian need not reproduce
fine real-time evolution or remain local or temperature independent.

At general β the commuting quantum limit is marginalization of βV, including
the fixed white fields, with H_eff=−V_coarse/β. The final TeX states this;
scaling only the three variable controls would have been incorrect.

The classical sup-action error proof is valid: finite logsumexp does not enlarge
the sup error, partition ratios lie in exp(±ε), and the stated bounded-observable
estimate follows from normalized likelihood ratios. A single learned initial
action retains the same bound through exact later steps; separately learned
step errors would add. This is a scalar statement, not an operator-monotonicity
claim for a noncommuting matrix exponential. Per-example finite-state maxima
are not parameter-uniform learning guarantees.

## Actual-RG checks and learned model

Independently compiled `FiniteRG.lean` with the existing pinned Lean4.24.0 /
mathlib environment and warnings treated as errors: exit0, nine printed types
and standard foundational axioms only. The file proves actual finite scalar
marginal, positivity, exp/log, partition, unnormalized observable, nesting,
error-sandwich and transfer-trace identities. It does not formalize the quantum
spectral logarithm, Pauli reconstruction or thermodynamic/critical RG.
Formal source SHA-256:
`65382a88cba24ca57ee1b17616b159042e4d3bdc75c8fe25470a19bcf768712b`.

The supplied physics checker passed to reviewer-owned paths. Independent
oracles additionally checked all16 partial-trace subsets and81 nested pairs
on a generic complex positive matrix; maximum errors were5.7e−14 and1.2e−13.
A full complex64-Pauli comparison matched explicit Kronecker matrices, with
reconstruction error1.8e−15. At β=.61 the zero-transverse-field model agrees
with independently enumerated classical weights, including white-field scaling.
A separately assembled tensor-product transverse Hamiltonian reproduces the
retained thermal weight within1.1e−14. The exact scalar-action error inequalities
also passed finite numerical checks. These are floating-point corroborations,
not interval certificates.

All160 saved teacher targets and training-only normalizations replay. The
120/40 split is disjoint; the dataset hash matches the checkpoint. Independent
complete-loss gradient checks for all12 nominal circuit angles at the final
checkpoint agree within9.3e−11. A useful structural finding was resolved in
the TeX: the last three RZ angles commute with all measured Z-products and
are inactive for this output loss. They change state phases, but12 nominal
angles are not12 effective expressive directions. This did not require retraining.

The model really predicts every coarse logweight, including its constant.
The separate evaluation artifact supplies interaction/constant errors without
altering trained weights. A full Walsh-character-matrix calculation independently
reproduces its constant MAE .04439, constant RMSE .06197 and higher-body
coefficient RMSE .009001. The classical baseline's better overall heldout action,
KL and partition errors are correctly reported; the quantum-feature fit has
a smaller higher-body coefficient RMSE in the separate diagnostic, which alone
does not establish advantage. OOD deterioration remains visible. Python/JS
replay agrees within1.8e−15 and the later sup-action errors do not grow.
The original trained checkpoint remains SHA-256
`7b905174236a468e3b39a63431790a7c2209537963c0eb6c3cdb9f50fa99727a`.

## Quantum TokenGT: independent critical checks

The active saved record is SHA-256
`5952ba0b9eeaba65c4dddd861cb7a86cbde660d09b3c6d89dd3fddd6c9d62c44`.
Its source and dataset hashes match. Its18 tokens correctly comprise seven
physical nodes, ten incidence edges and one masked pad. Three feature qubits
per token encode controls/metadata, not physical spins or an order representation.
Fixed quantum features feed classically trained attention and readout; no
coherent quantum attention or upstream full-model training is implied.

The saved checker passed to reviewer-owned paths:67 independent F2 radius
checks,61 exact-teacher forest rewards, density/bridge identities, permutation
transport and four trace records. A separate NumPy replay discarded padding
before attention, reconstructed each of the four softmax/tropical/hybrid
models and matched every saved heldout metric within2e−12. Each has1,076
trained classical parameters. The classical comparator is better on heldout
full-action RMSE; one-seed results establish neither significance nor advantage.
The analogy control is one specified clipped parameter transformation with a
train-derived mean latent displacement. Matching empty physical-observable H1
barcodes alone supplies no invariant or faithful analogy, as the exposition says.

The intervention-code MI functional has an explicit random six-valued C and
normalized classifier, so its variational interpretation is legitimate for
the specified distribution. The wording was corrected during review: the
heldout number is an empirical functional estimate, not a certified population
MI bound without uncertainty control. It measures recoverability of deliberately
injected codes; deterministic intervention differences can already distinguish
the codes and do not identify semantic factors. This condition is resolved in
the final exposition and README.

The continuous GFlowNet has a delta root, Lebesgue measures at times1,2,3,
full-support Gaussian forward transitions and a correctly normalized Gaussian
backward bridge at times2,3. The last backward move is a unit point mass at
the root, contributing zero log mass rather than a fictitious Gaussian density.
An independent arbitrary-path calculation reproduces the Brownian endpoint
identity within1.1e−14. The reward is integrable because its physical logZ
factor is bounded on the tanh-bounded control domain and it has Gaussian tails.
Exact trajectory balance everywhere would imply the terminal target law;
the recorded empirical residual, finite-box quadrature and histogram comparison
are diagnostics and do not prove that equality. The saved record reports zero
samples outside the histogram box; future nonzero outside mass must be included as an
additional bin for a complete binned-TV comparison. The current exposition
properly disclaims certified tails and sampling accuracy.

The executed repetition channel and cellular CSS example are both correct
and distinct. At p=.1 and .3, actual SDK output matches the independently
constructed logical Bell mixture within2.7e−14. Syndrome corrections give
logical X error3p²−2p³ and Bell entanglement fidelity1−3p²+2p³; no phase
protection or general fault tolerance follows.

An independent exhaustive cut/cycle enumeration on all1,024 edge masks confirms
the cellular code has rankHX6, rankHZ0, k4, dX1 and dZ4. The one-face
orientable cellulation has zero F2 face boundary, while K2,5 has girth4 and
no bridges. Thus a single-edge X is a nonstabilizer logical, and the smallest
nonzero Z cycle has weight4. The resulting [[10,4,1]] is correctly presented
as a bad-distance example, not topological protection supplied by genus.

## Evidence and acceptance

The final `book/chapters/quantum-tokengt.tex` was additionally read in full.
Its MI inequality, exact trajectory-balance integration argument and limits
of finite empirical residuals, CSS girth proof and numerical metric tables
agree with the reviewed objects. One concrete reporting error was identified
and fixed: the GFlowNet histogram comparator is20×20 cells of width0.5;
the separate normalizer quadrature is201×201 points at spacing0.05. These
must not be conflated, since histogram TV depends on the binning.

The separately checksummed QEC-memory sidecar was independently checked,
including its source hashes and preservation of the5952… trained record.
Its SHA-256 is
`9ab7dcea6143ccfce00b596a82642d17f10c3d22f5c89a5d6804eb7ec0266f30`.
All45 complete model/noise/level metric cases and75 explicit logical-density
cases pass; an independently density-replayed hybrid prediction agrees within
8.9e−16. The attenuation (1−2p_eff)^r follows from XZX=−Z and tensor products
of independent recovered channels, including entangled feature inputs.
Ideal concatenation composes p_eff=f(p), f(p)=3p²−2p³. The final book now
distinguishes logical-channel evaluation from a full9/27-wire noisy encoder/
recovery SDK run. Its3/9/27 per-token counts refer to encoded data qubits,
without a fault-tolerant gate/syndrome-ancilla resource analysis. The original
Bell-reference run supports the single-block channel; the larger layer uses
that proved channel rather than claiming unexecuted large gate simulations.

The new five-qubit generator was replayed only to reviewer-owned output.
Its4096 seeded shots reproduce the stored result exactly. StatePrep constructs
the coherent pure state sum_s sqrt(p_s)|s>; its Born distribution is p, but
its density is not the mixed Gibbs density. The explicit projector Kraus
dephasing gives diag(p). Probability and dephased-density errors are both
2.8e−17. The32 amplitudes are computed classically; there is no efficient
many-body thermal-preparation claim. The simultaneous five-magnetization
Hoeffding radius sqrt(2 log(10/.05)/4096)=.0508632 is correct for independent
Born shots with values in [−1,1]. The observed maximum shot error .0437665
is smaller. This bound is relative to the frozen learned distribution, not
the exact physical teacher; action approximation bias is a separate error.
The final book paragraph now explicitly describes this executed pure-state,
dephasing and sampling calculation, including the classical amplitude cost,
the union-bound formula and the distinction from physical-teacher bias.
The CSS proof's cut/coboundary terminology is corrected; its added independent
stabilizer-projector trace argument gives the expected16-dimensional code
space, equivalently four logical qubits.
No protected training/data/sampling artifact was overwritten.

Reviewer evidence includes `lean-focused.log`, `physics-checks.json`,
`independent-oracles.json`, `learner-checks.json`, `web-model.json`,
`quantum-tokengt/independent.json`, `qtoken-own-oracles.json`,
`quantum-tokengt/qec-layer.json`, `sampling-review.json` and
`qec-sampling-summary.json` under the
authorized reviewer output directory. No optimizer was rerun. Primary
Levin–Nave v2 context was checked
([primary text](https://arxiv.org/html/cond-mat/0611687v2)): its approximate factorization followed by
exact contraction is distinct from the full-action elimination executed here.
Wilson–Kogut's publisher/scanned endpoints were unavailable to this reviewer;
its full source was not independently audited. The finite identities above
were checked directly and do not depend on that reading claim.

No substantive mathematical or executed-program blocker remains in the
reviewed scope. Browser/visual and final integrated build/integrity gates
remain with the integrating worker. None of these checks establishes a
thermodynamic RG fixed point, full-book formalization or the GRH bridge.

## Constructive finite gentle cut for a future HMS interface

The final proposed m5 cut is accepted as an explicit finite quotient, not a
new primary infinite-order equivalence. Remove a0,b0 from the cyclic quiver.
The remaining arrows a_i,b_i:i→i−1 have i=1,…,4, and the surviving forbidden
pairs are a_i b_(i−1), b_i a_(i−1) for i=2,3,4. Positive nonzero paths remain
on one branch. Independent enumeration gives counts5,8,6,4,2,0 in lengths
0,…,5, hence dimension25. The bound quiver is finite, acyclic and gentle.

The forbidden indexing chains alternate branches and have length at most4;
they are labels of resolution summands, not nonzero algebra paths. The two
top chains are a4 b3 a2 b1 and b4 a3 b2 a1. The same minimal monomial-resolution
argument gives pd_B(S_i)=i and Ext4_B(S4,S0)=k². The standard finite-dimensional
split-algebra criterion then gives global dimension4. The split semisimple
quotient k^5 is important when invoking the usual homological-smoothness
criterion over a general coefficient field. Choosing an explicit grading is
still necessary for a graded Fukaya/HMS comparison; stops and a line field,
and the actual associated cut surface, have not been identified by this count.

There is a useful concrete limitation: every full permitted branch cycle
passes through one removed arrow. Thus the continuous quotient from the
completed order sends its diagonal DVR parameter u to zero. B is u-torsion,
not an order lattice. Its sink simple S0 is projective over B, whereas the
original completed m5 order has Ext5(S0,S0)=k² by its unending forbidden arms.
Consequently restriction along this quotient is not derived fully faithful.
Neither global dimension4 nor the existence of this finite gentle cut
identifies its derived surface with the original closed genus-two surface.
No Lean formalization of these added categorical/cut assertions is claimed.
