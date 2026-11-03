# Independent persistence-tool review — 2026-11-03

Reviewer: `/root/persistence_tool_review`. The review uses the existing
persistence chapter, its earlier source/theorem review, and the proposed P2
tool. No source data, training weights, environments or Git state were changed.
This is not a claim that the broader GRH program or all categorical interfaces
are formalized.

## Mathematical design

For `m>=2`, require natural-number exponents with
`a0>...>a_(m-1)=0` and `b0=0<...<b_(m-1)`, with positive outer exponents.
These are minimal Artinian two-variable staircase generators. The adjacent
column has entries `-y^(b_(i+1)-b_i)` in row i and
`x^(a_i-a_(i+1))` in row i+1. Its grade is `(a_i,b_(i+1))`.

The proposed exactness proof is valid. In a relation, all terms except the
last are divisible by `x^a_(m-2)`. Coprimality with the last pure y-power
forces the last coefficient to contain that x-power. Subtract its multiple
of the final adjacent column, then factor the common x-power from the
remaining relation and apply induction. The first row of a zero adjacent
syzygy combination forces its first coefficient to vanish; the subsequent
rows force the rest. Positive exponent differences establish minimality over
the stated field-polynomial ring.

At a fixed grade, the active generators form one contiguous interval of
indices. Thus `c` active filling disks give H1 dimension one if c=0 and zero
otherwise, and H2 dimension `max(c-1,0)`, equal to the number of visible
adjacent syzygies. The CW model is not asserted to be a manifold or the
dessin surface. Its H2 must not be conflated with the unrelated quantum flag
complex's homology.

For the existing actual nodal coefficient `E=Lambda/u²`, the total free
`Lambda[x,y]` cone has ranks `(1,m+1,2m-1,m-1)`. The earlier regular-parameter
exactness proof applies once the staircase resolution has been established.
No unspecified minimality assertion is needed. Underlying field-vector-space
fibers have dimension four times those of M. These dimensions and the
parameter-ring Betti numbers are not the same as the cone's free ranks over
the surface-order coefficient ring; the interface must label their rings.

## Quantum bifiltration and transition maps

The designed equatorial/pole family is a new finite test input to one fixed
saved QCNN4 channel. It is not new training or a held-out benchmark. Reusing
the same vertex-population birth grades on both input and output is essential
to the claimed identity-on-labels inclusion.

For a positive trace-preserving finite linear map T and Hermitian A, the
Jordan decomposition and triangle inequality give
`||T(A)||_1 <= tr T(A_+) + tr T(A_-) = ||A||_1`. Applied to density-matrix
differences this proves trace-distance contractivity; complete positivity is
stronger than needed for this argument. It does not mean that an arbitrary
matrix norm, correlation graph or pair of unrelated channels is contractive
or commuting.

The actual floating-point distances are not interval-certified. Frozen
integer distance-derived graph labels nevertheless define an exact finite
combinatorial bifiltration. Verify the output-label inequality directly; do
not manufacture it by replacing output labels with their minimum with input
labels. The discrete inclusions are exact once these recorded labels and
fixed birth grades are chosen.

For an actual inclusion K_source into K_target, embed source one-cycles into
target edge coordinates. Then the proposed rank formula
`rank([B_target,Z_source])-rank(B_target)` equals the rank of the induced H1
map. Source boundaries already lie in target boundaries, so no additional
subtraction by source boundary rank is required. The H0 analogue with source
vertex generators is correct. Empty complexes, equal grades and genuine
comparable-grade constraints need implementation checks. A two-skeleton
computes H0/H1 of the full flag complex, but does not determine its H2.

## Independent exact/numerical design checks

Using the existing approved CPU environment in memory, five staircase examples
were checked: `(x,y)`, `(x,y)^2`, `(x,y)^3`, the 13-point staircase with
generators `(5,0),(3,1),(1,3),(0,5)`, and the 16-point staircase with generators
`(4,0),(3,2),(1,4),(0,6)`. All consecutive products, signed maximal minors,
Hilbert numerator identities, cone products and active-cell/syzygy counts
passed. The literal nodal E actions on `(1,xi,u,u xi)` satisfy
`xi*eta=eta*xi=0`, `u²=0` and `xi²=u*xi`.

An independent quantum calculation used the saved QCNN4 weights. Pure-input
trace distances were computed via `sqrt(1-|<psi_i,psi_j>|²)`, independently
of a density-matrix eigenvalue implementation. Input bins are
`{0,383,708,924,1000}`. Output eigenvalue trace-norm bins are
`{0,382,383,706,707,708,922,924,998,999,1000}`. Output distance never exceeds
input in this calculation. At radius bin383 and population threshold500,
the eight equator vertices and south pole have Betti numbers `(2,1)`, eight
edges and no triangles, in both input and output. This supplies a genuine
nontrivial H1 example.

## Actual implementation review

Reviewed `web/persistence-model.mjs`, `web/persistence.mjs`, the HTML/CSS,
`scripts/check_persistence_model.mjs`, both persistence exporter/checker Python
files, the shared propositions in `papers/dessin-core.tex`, and the appended
executable section of `book/chapters/persistence.tex`. No blocking mathematical
or implementation defect was found in this scope. The induction proves actual
polynomial exactness, not merely that consecutive differentials compose to
zero. The UI distinguishes parameter-ring Betti ranks, coefficient-cone free
ranks, CW homology and derived fiber homology. The quantum labels, common
channel, retained population births and two-skeleton limitations match the
implementation. The rank routine embeds source cycles in target edge
coordinates and quotients by target boundaries correctly.

The existing Node checker passed, reporting 72 comparable quantum map cases
and nontrivial H1 birth/persistence/death. To avoid relying only on another
implementation of the same rank formula, this reviewer independently tested
160 seeded random finite graph inclusions (seed1729, at most five vertices).
Every source cycle was exhaustively enumerated; its image was classified by
its coset modulo the exhaustively enumerated target-boundary space. The base-2
logarithm of the number of cosets agreed with the tool's induced H1 rank in
every case. An analogous quotient enumeration verified H0. This includes
empty source complexes. Sixty-four additional strict staircase patterns
passed active-cell/syzygy counts and all three nonorigin F2 fiber checks.
These independent checks ran in memory and wrote no additional artifacts.

The actual frozen record has SHA-256
`d5799c3784a93354312aaaa41b65bfbd7fe0aa0ed1360168828478174f2dbead`.
Its body hash, saved-training-checkpoint hash and exporter hash match.
Reconstruction of every stored output density by reshaping `U psi` as a 4x4
matrix and multiplying by its conjugate transpose gave maximum discrepancy
zero at machine precision. All ten fixed birth labels match the input
population, all 200 input/output labels equal ceilings of their stored
scaled numerical distances, and all output labels are at most input labels.
Pure-state overlap distances independently agree with the stored input
distances; eigenvalue trace distances agree with the stored output distances.
These are floating-point reproduction checks, not interval certificates.

The optional imported-channel provenance suggestion is resolved. The exporter
now records `examples/quantum/surface_models.py` and its SHA-256, alongside the
checkpoint and exporter hashes. The final record SHA-256 is
`22310cb4f01439463cd885cf257f266f5f0a491df4ab5ebc318e0b4a61b935b1`.
Independent comparison confirms that every field outside `provenance` is
identical to the reviewed d579 record, which remains present with its original
hash. Only `channel_implementation`, `channel_implementation_sha256` and the
exporter's necessarily updated `generator_sha256` differ. All final body,
checkpoint, exporter and imported-channel hashes match the current files.
The Node checker was rerun against the final manifest and again passed all
72 comparable map cases and the nontrivial cycle tests. The prior numerical
and exhaustive quotient checks therefore apply unchanged to the final data.

Acceptance is limited to the inspected mathematics and finite implementation.
Browser interaction, accessibility/visual inspection, complete PDF/HTML
builds, source-pin/integrity checks and private push are the integrating
worker's gates; this reviewer did not navigate its active browser or mutate
Git. General categorical/module/trace-norm Lean interfaces and the arithmetic
positive-determinant bridge remain explicitly open, as stated in the text.
