# Covering, equivariant and geometric interfaces — 2026-11-03

Requested primary sources are pinned in
[the manifest](../planning/reviews/covering-literature/source-manifest.json).
The review examines the relevant definitions, theorem hypotheses and selected
proofs; it is not an independent reproof of all three external classifications.
The Schroll author preprint is recorded separately from the published chapter.

Liu–Li–Xing–Chen supply locally bounded covering and precovering machinery.
Dong–Lin–Lu–Ruan supply equivariant GLS/AR techniques and a corrected rank-root
correspondence. Schroll supplies the graded geometric/derived/Fukaya framework.
Their distinct categories and hypotheses are retained in the new book chapter.

## Constructive addition

The new results concern the actual infinite theta dessin algebra and its
specified finite string quotients. The shared articles contain full proofs:

- [Core](../papers/covering-core.tex): locally bounded integer cover and finite
  deck-Hom decomposition; actual theta Hom-control defects; indecomposable
  non-lifting module; specified higher-genus and derived non-density extension.
- [Calculations](../papers/covering-details.tex): full seven-parameter commutant,
  nilpotent radical multiplication, Euler obstruction, perfect-complex Hom
  transport and a valid induced branch-equivariant pair.
- [Book](../book/chapters/coverings.tex): categorical assumptions, precise
  literature applications, one original cover diagram, determinant and
  arithmetic boundaries.

The nine-dimensional carrier has X edges (1,0),(3,2),(4,3),(6,5),(7,6),(0,8)
and Y edges (1,2),(4,5),(7,8), acting on columns. Both mixed products and cubes
vanish. For arbitrary D, six X commutator equations minus three Y equations
force 0=3. The obstruction excludes every finite-support lift, even after
arbitrary basis changes; it is not merely a failed choice of diagonal grading.
Exactness also excludes a bounded-derived preimage of this module in degree
zero. The specified m-edge clean dessin family gives the same contradiction
0=m in dimension3m: genus4/dimension27 and genus9/dimension57 are concrete
larger cases. No general higher-genus endomorphism classification is asserted.

For L=5, the five simples and the five-step chain have identical cover K0
classes and Hom defects4 and1. Restriction to a finite convex source interval
and extension by zero gives a literal finite-algebra Hom-control counterexample.
This replaces any reliance on an unrelated generic finite algebra example.

## Evidence and limitations

Run the existing approved environment:

```sh
.tools/book-quantum-cpu/bin/python examples/coverings/theta_cover.py
```

It checks 36 Hom pairs by exact linear algebra, reconstructs every Hom basis
element from deck components, verifies the complete radical multiplication,
and checks the larger examples. The data are served in
`web/data/theta-cover.json`. The exact Sage counterpart is supplied but not
executed because the installed Sage launcher lacks its app.

`lean-analytic/CoveringBand.lean` checks mixed products and cubic nilpotence
over any commutative ring, and rules out an arbitrary Euler operator over a
characteristic-zero ring. All three printed axiom reports use standard Lean
foundations only. It does **not** formalize the complete covering category,
endomorphism-ring classification, general higher-genus family, derived
functors or external classification/equivalence theorems.

The infinite polynomial parent is not locally bounded, and the finite
length-L quotient for L>2 is not quadratic gentle. A graded-gentle Fukaya
equivalence is not silently transferred to that quotient or the completed
order. The finite modules extend continuously to the completion but are not
central-DVR-free lattices. An AR mesh, deck decomposition or GLS rank vector
does not prove determinant block factorization or positivity.

## Next dependent work

Use the explicit finite-support path/grade data in the canonical AR and
architecture tools without mislabelling a quiver-cover window as an AR
component. Implement the actual graded-quiver/module push-down interface in
Lean before calling the Hom theorem fully formal. Any proposed GLS/skew-group
identification must specify its triple, quiver, relations and functor.
The original low-gcd estimate and independent positive arithmetic determinant
remain unresolved; the new non-density result is not a GRH obstruction or proof.
