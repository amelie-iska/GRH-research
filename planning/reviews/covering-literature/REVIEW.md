# Independent covering-literature review — 2026-11-03

Reviewer: `/root/covering_literature_review`. The review used the pinned local
primary PDF texts of Liu–Li–Xing–Chen, arXiv:2508.01563v5; Dong–Lin–Lu–Ruan,
arXiv:2609.26503v1; and Schroll's author preprint arXiv:2601.14396v1 of the
requested SIAM chapter, DOI 10.1137/25M1810647. The author preprint is not
claimed byte-identical to the published chapter. Relevant definitions,
covering/AR/derived theorem hypotheses and geometric-category boundaries were
checked; this is not a fresh independent proof of the papers' complete
classification theorems.

## Constructive theta quotient

The elliptic theta dessin with sigma=(012)(345), alpha=(03)(14)(25) gives
three quiver vertices and two parallel arrows a_i,b_i from i to i+1 modulo 3.
The mixed quadratic compositions vanish; same-family paths survive at every
length. Its polynomial algebra A is infinite-dimensional and locally gentle.
For L>=2, B_L=A/J^L is a legitimate finite-dimensional string quotient with
dimension 3(2L-1): at each starting vertex there is the trivial path and two
pure paths of each length 1,...,L-1. For L>2 it is generally not quadratic
gentle, so gentle/Fukaya theorems must not be applied directly to B_L.

The lifted quiver has integer vertices r, parallel arrows r->r+1, mixed
relations and length-L truncation, with deck generator r->r+3. The lift is
connected and locally bounded: each vertex has only 2L-1 surviving paths
starting at it, and likewise finitely many terminating paths. Removing the
truncation makes the reachable path-Hom sum infinite. The untruncated lift
therefore fails the locally bounded hypothesis, despite local finiteness of
each individual Hom space. The group action's orbit is the specified B_L
presentation. This is an algebra/quiver covering; extension to an unramified
cover of the cellular dessin surface is not automatic.

The finite-support push-down Hom decomposition is valid. With finite support
at both ends, only finitely many deck translates can contribute, and block
components of a base morphism split according to the unique deck difference.
The splitting respects every lifted arrow equation. Faithfulness is not
fullness, and an orbit sum is not Zwara's K0-bilinear numerical defect.

## Nine-dimensional non-lifting module

The column-basis vertex labels are

```
0,1,0,1,2,1,2,0,2.
```

X has entries 1 at (row,column)=(1,0),(3,2),(4,3),(6,5),(7,6),(0,8),
and Y has entries 1 at (1,2),(4,5),(7,8). Every listed action has the correct
base source and target. Direct exact multiplication gives XY=YX=0,
X^3=Y^3=0, so these matrices define a B_3-module. The cyclic word

```
a0 b0^-1 a0 a1 b1^-1 a1 a2 b2^-1 a2
```

has no cancellation; its powers never contain three consecutive same-family
forward or inverse arrows. It is primitive, since the possible proper period
three does not give a closed base walk. Thus it is legitimate band data.

The obstruction does not require assuming a diagonal Euler operator. For an
arbitrary 9-by-9 D, each nonzero X or Y position has a unique nonzero entry
in its row and column. The equation [D,X]=X yields the six corresponding
diagonal differences equal to 1; [D,Y]=Y yields three more differences equal
to 1. Summing the first six and subtracting the last three cancels all nine
diagonal coefficients and gives 0=3. This is impossible in characteristic
zero. Every finite-support lift supplies an integer-vertex Euler operator
with these degree-one commutator equations, so no such lift exists. The
characteristic-zero qualification matters: this particular contradiction
disappears in characteristic 3.

An independent exact SymPy computation additionally determines the
vertex-preserving commutant. Its dimension is 7 and it has basis I,r0,...,r5,
where Eij denotes the elementary matrix:

```
r0=E02+E13, r1=E15, r2=E35+E46,
r3=E48,     r4=E68+E70, r5=E72.
```

The only nonzero products among the six radical basis elements are
r0*r2=r1, r2*r4=r3, r4*r0=r5. All triple products vanish. Consequently the
endomorphism ring is kI plus a nilpotent ideal, hence local; the module is
indecomposable. The exact linear-system calculation used 27 vertex-preserving
unknowns and commutation with both matrices. This gives an elementary
indecomposability check separate from the standard band classification.

The matrices use covariant column representations (left-module convention).
The covering lecture uses contravariant/right modules; passing to opposite
categories reconciles the conventions without changing the support or
non-lifting conclusions.

## Precise use of the three sources

- Liu–Li–Xing–Chen, Definition 1.12, distinguish local finite-dimensionality
  from local boundedness. Theorem 4.23 gives a module **precovering** and,
  under torsion-free hypotheses, indecomposable/orbit properties. Theorem
  4.28 gives the corresponding bounded-derived precovering. The actual
  categorical Galois-covering hypotheses in Theorems 4.14/4.18 are needed
  before asserting the stated full AR-quiver covering. Density must not be
  inserted silently; the B_3 witness decisively disproves it for this cover.
- Dong–Lin–Lu–Ruan work over an algebraically closed field of characteristic
  zero with finite-dimensional GLS algebras. Their Theorem B lists a combined
  preprojective/preinjective component, ZD_infinity components, two-sided
  ZA_infinity components, one tube of rank n-1, rank-two tubes, and homogeneous
  tubes for the named minimal-symmetrizer family. This classification is not
  automatically a classification of our infinite gentle order. Theorem C
  concerns rank vectors of tau-locally-free modules, with two explicit
  non-root families in the CD family; it does not classify module isomorphism
  classes by vectors. Vertexwise freeness there is over truncated local
  vertex algebras, not central-DVR lattice freeness.
- Schroll's perfect-category/Fukaya correspondence requires the specified
  graded marked surface, stops/line field and admissible dissection. A
  compact Belyi Riemann surface alone is not that datum. In the infinite,
  nonproper polynomial situation, per(A) is not generally contained in the
  finite-total-cohomology category: the regular projective A already has
  infinite k-dimension. The smooth/proper assumptions in equivalence
  statements are essential. Formal completion to a surface order requires
  additional continuous/topological module and tensor considerations.

The branch involution exchanging a and b does preserve A and B_L. Forming a
skew group algebra in characteristic different from 2 is a valid possible
equivariant construction, but identification with a particular GLS algebra
needs an explicit quiver/triple or Morita comparison. Our witness has ranks
rank(X)=6 and rank(Y)=3, hence it is not fixed under branch swap. Its orbit
sum has the evident swap linearization; no fixed-object lift or stabilizer
character is being inferred.

## Acceptance boundary

The drafted `papers/covering-core.tex` and `papers/covering-details.tex` were
also read. The sign convention in the deck translation Hom formula is
consistent, and the bounded-projective Hom-complex argument correctly leaves
the general nonperfect source case to the cited precovering theorem. The new
actual-theta Hom-control example has cover End dimensions 5 and 1, pushed-down
End dimensions 9 and 2, hence defects 4 and 1 at a common K0 class. Restricting
to the finite convex interval [0,4] before zero-extension makes its source a
finite-dimensional algebra, as required by Zwara's literal definition. The
implementer made that finite convex restriction explicit in the revised core.

The new book chapter was read as well. It correctly labels its drawing as a
finite quiver window, not an AR component; retains the opposite-module
convention; separates infinite polynomial algebras, finite quotients and formal
completions; and keeps the arithmetic determinant/positivity problem open.
The higher-genus construction repeats the three-state pattern on 3m basis
vectors and yields 0=m. It is valid for the specified parallel-cycle dessin
family with sigma=(0...m-1)(m...2m-1), alpha pairing i with i+m. For odd m
that family has genus (m-1)/2. It must not be read as a statement about every
two-black-vertex dessin with arbitrary cyclic rotations and edge gluing.
The executable checks include m=3,5,9,19, dimensions 9,15,27,57.

The current Lean log prints three theorem types and dependencies. They state
actual mixed products and cubic nilpotence over an arbitrary commutative
ring, and absence of an Euler matrix over a characteristic-zero commutative
ring. Printed dependencies are precisely propext, Classical.choice and
Quot.sound. The statements do not silently assume desired gradability,
arithmetic positivity or zero locations.

For completeness, module non-density also implies bounded-derived
non-density here: if an exact push-down sent a bounded complex C to the
obstructed module M in degree zero, it would send the finite-support module
H0(C) to M. This contradicts the Euler obstruction. This strengthens the
scope explanation without contradicting the source's precovering theorem.

The final two shared TeX fragments and the new book chapter were reread after
revision. The explicit sigma/alpha family, finite convex source restriction
and H0 proof of derived non-density are now all present. These close the
review's outstanding mathematical wording requests. The new determinant
discussion correctly distinguishes a deck-wise Hom decomposition from an
invariant block decomposition of the actual differential; it does not infer
determinant factorization from the former. Equal source/target Hom dimensions
and fixed determinant lines are retained for the semi-invariant construction.
The elementary determinant 1-ab is an accurate warning about off-block terms,
not a claimed arithmetic example.

Independently rebuilding the general 3m-by-3m matrices for m=3,5,9,19 verified
their vertex labels, mixed products, cubes and vanishing diagonal-coefficient
sum, with Euler right sides 3,5,9,19. No unverified higher-m endomorphism-ring
or indecomposability classification is added.

The constructive category distinction, finite-support Hom splitting and
explicit non-dense cover are accepted as mathematically sound. They refine
the AR, semi-invariant and derived bookkeeping, not an arithmetic determinant
or zero-location theorem. Actual kernel checks in CoveringBand.lean verify
the matrix obstruction and relations only; the full module/cover/derived and
Fukaya results remain prose or explicitly cited external theorems unless
further formalized. No mathematical review finding remains open. Final
compilation, visual inspection and repository-integrity checks are the
implementer's separate acceptance work.
