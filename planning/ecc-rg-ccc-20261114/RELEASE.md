# Arithmetic, coverings, learned quantum renormalization and CCC controls

## Verified implementation

Scientific source: `e97aafb8c0757734d541460c70ed7e9d9a3743ee`.
Verified evidence commit: `d0067f8690f16d9355a768f7ef14e0fc7a840852`.
Independent successful run: [43603831191](https://github.com/amelie-iska/GRH-research/actions/runs/43603831191).

The exact subsection **Resource-certified elliptic-curve quantum arithmetic**
in `extension/manuscript/chapters/synthesis.tex` now points to its implemented
successor. Historical PDF editions remain unchanged. A new 21-page supplement,
full emitted circuits, assumption manifests, trained channels, CMB source records,
calibration and independent verification evidence are published in
[releases/program3-20261114](../../releases/program3-20261114).

PDF SHA-256: `a72ef99cf8caa8c257d01f2c8e3ffb1c1712e7e623b8b1087394a2d6086d4d69`.
The release manifest lists 98 files, all independently checked for size and
SHA-256 after downloading the Actions artifact. The final PDF has 21 pages and
no warnings, overfull content or unresolved references in its final build log.
Its pages and rendered browser panels were visually inspected. The publication
markup adds report links and an explicit final null-validation note; it changes
no circuit, learned parameter, observed map, null realization or numerical result.

## The original arithmetic program is now executable

The implementation provides an affine/infinity encoding, explicit invalid-word
behavior, field XOR oracles, a variable-point addition oracle, in-place fixed-base
translations, emitted X/CX/CCX gates, clean scratch, coherent signed decomposition,
and its uncomputation. Resource counts are reconstructed independently from the
serialized gate stream. Both scalar paths support every input point word, not
only a preselected initial infinity state.

| Field | Method | Logical qubits | X | CCX | All-to-all depth |
|---|---|---:|---:|---:|---:|
| 7 | binary | 16 | 2328 | 2904 | 3390 |
| 7 | endomorphism | 22 | 3808 | 4766 | 5608 |
| 13 | binary | 21 | 7040 | 8850 | 9832 |
| 13 | endomorphism | 27 | 9204 | 11768 | 13186 |

Complete clean-work data domains contain 2048 and 16384 words, respectively.
Invalid encodings are included. The general p=7 variable-point oracle checks
all 16384 input words and an additional 512 nonzero output-register cases.
A separate artifact-only affine implementation also replayed all four scalar
circuits and independently counted gates and depth.

The full endomorphism path costs more for this compiler and these curves. The
compiler uses an explicit finite lookup/Gray-transposition construction with
exponential width dependence. It is a complete small-instance reproducibility
baseline, not a polynomial-size cryptographic implementation or a demonstrated
fault-tolerant advantage. Public fixed-base phi(G) is recorded; it does not make
an unknown variable-point endomorphism costless. Physical error correction,
routing and T-gate lowering require additional declared compilation assumptions.

## Covers, integral orders and networks

Finite voltage covers preserve the specified gentle monomial relations through
local incoming/outgoing star bijections. Explicit cellular torus covers check
both pullback identities and the boundary composition. Tied local layers,
replicated normalized softmax and coordinatewise max-plus commute with the
specified feature pullback. Arbitrary sheet identifiers break that property.

The integral order relation uv=pi e requires compatible composite voltage.
Some connected gentle special-fiber covers fail this relation before reduction.
Fiber averaging requires an invertible cover degree; characteristic dividing
that degree supplies a counterexample. The normalized amplitude lift is a
single-state direct-sum isometry, not cloning into independent tensor copies.

Covers also create new modes: cycle-cover gaps decrease from 3 to approximately
0.06815 across the tested degrees 1,2,3,5,8, even though the base intertwiner is
exact. Thus local computational transport does not certify a size-uniform gap.
Cover degree, neural feature width and physical thermodynamic size are distinct.

## Learned hierarchy and infinite-width considerations

The trained quantum model has six gate angles and two classical readout
parameters. It is a 4-to-2-to-1 CPTP channel with explicit unitary blocks and
partial trace, without postselection. Training and independent implementations
agree across Heisenberg observables, pooled Kraus matrices, deferred-discard
state evolution and partial-trace calculations.

The model trains on 33 exact four-site periodic Ising Gibbs states at beta=1,
with held-out couplings and validation checkpoint selection. Effective coarse
Hamiltonians use the full -log(rho) and all Pauli coefficients. Truncation to
an Ising operator family has a measured trace-distance error rather than an
unjustified exact-closure claim.

| Seed | Learned-channel test MSE | Frozen initial channel + fitted readout | Constant baseline |
|---|---:|---:|---:|
| 17 | 0.0000614959 | 0.0001168692 | 0.02602927 |
| 29 | 0.0009693252 | 0.0000055542 | 0.02602927 |

Gate learning improves over the frozen-channel baseline for seed17 but not seed29.
The baseline is a post-initial-experiment diagnostic, fitted on training only;
no learned weights were retuned to make it favorable. The full-density-matrix
observable oracle is a different information-access contract.

The independent one-qubit feature construction has an explicit RBF kernel,
positive-semidefinite finite Gram matrices, almost-sure fixed-input convergence
and finite-set concentration. Nested independent channels and fully tied copies
are tested separately: repeating one tied feature does not create independent
width. A written bounded-dependency cumulant argument gives a sufficient Gaussian
limit when maximum dependence degree is o(M^(1/4)) and normalized covariances
converge. Its initialization/dependence assumptions are not silently transferred
to unrestricted jointly trained, deep entangled networks.

## Real WMAP controls and their interpretation

The acquisition resolves actual NASA WMAP DR5 ILC, foreground-reduced V/W maps
and KQ85 mask from official links, preserving FITS units, ordering and SHA-256
hashes. Native millikelvin are converted explicitly to microkelvin. Nside16,
lmax32, monopole/dipole removal, added five-degree smoothing and a fixed mask
are documented. The study uses broad widths12,18,24 degrees, respecting the
ILC documentation's large-scale qualification. It is not a degree-scale
Hawking-point replication or an exact common-beam deconvolution.

The frozen search covers 72 locations/scales and three methods: broad temperature,
low annular variance and an actually trained hierarchical QNN. The QNN is fitted
only to separate phase-surrogate realizations and declared injections, conditional
on observed harmonic magnitudes; observed phases do not select its weights.
Training, normalization, calibration and validation realization seeds are disjoint.
All 511 calibration draws repeat the whole search. Independent validation has
256 draws, and sensitivity tests retain all64 injection trials per amplitude.

| Product | Original full-search phase rank | Three-product union bound | Common-ILC-reference rank |
|---|---:|---:|---:|
| ILC | 0.9921875 | 1.0000000 | 0.99609375 |
| V | 0.005859375 | 0.017578125 | 0.818359375 |
| W | 0.23828125 | 0.71484375 | 0.9921875 |

The common-reference and V-W tests were designed after the initial disagreement
and are explicitly exploratory. V-W has phase rank0.03125. A separate common-phase
family test retains every inter-product harmonic cross-product and scans all
3 products x3 methods x72 templates. Its joint rank is0.017578125. In the final
verified artifact its independent null-validation result is **9/256** (3.515625%)
at nominal5%, with conditional Wilson interval[1.8604%,6.5453%]. Cross-product
invariance error is at most6.64e-16 in that run. The final source-bound result,
not an earlier conversational figure, is the publication authority.

These are conditional phase-surrogate ranks, not CCC posterior probabilities
or a full-instrument significance calculation. The large change under the common
reference is scientifically material. The maps share the sky and observations;
their ranks are not multiplied as independent discoveries. Anisotropic noise,
foreground processing, effective beams and reconstruction uncertainty are not
fully modeled. The current outputs support robustness investigations, not a
claim of a physical cross-aeon signal or an intentional message.

## Formal and software verification

- 142 regression methods passed in ordinary Python and the same142 under python -O.
- 22 new Lean declarations passed with no warnings, sorryAx or unexpected axioms:
  eleven reversible/cover/channel/rank contracts, five conformal/quartic/cubic
  identities, and six exact finite elliptic certificates.
- The arbitrary finite upper-rank theorem includes ties. Statistical
  exchangeability remains a separate physical/modeling premise.
- 320 independent JavaScript arithmetic replays, four invalid-word cases, four
  QNN replays and nine complete sky replays passed. Maximum JS/Python sky-score
  discrepancy:3.68594044175552e-14.
- 32 rendered browser checks passed, including independently compared mixed-state
  output, asset hashes, corrupted-data rejection, keyboard/mobile operation,
  URL restore, exported evidence and observed-versus-injected labeling.
- The original workstation also completed genuine cuStateVec p=7 arithmetic and
  six learned-channel checks before remote access paused. The CPU CI did not
  rerun those GPU tests. Their raw GPU receipt remains on the paused machine;
  it is not claimed as an independently downloaded member of this release.

## Operational scope and preservation

Desktop Commander reached its monthly limit and paused. No reconnect, retry or
alternate path into the paused machines was used. The independent standard
GitHub Actions CPU runner completed the final verification and publication.
Remote clones are not claimed synchronized after the pause; the ongoing Mora-3
campaign and environments were not changed. The earlier Hugging Face release
is unchanged; this continuation is published in the versioned GitHub directory
and downloadable artifacts. No secret, private input, external paper scan or
font file was published. Every ref promotion is fast-forward with an expected-head
check, not a force push.

The original source title was reopened before implementation. The new code and
written results extend that program; they do not silently replace its terminology
or retrofit the finite demonstrations into a large-scale quantum advantage claim.
