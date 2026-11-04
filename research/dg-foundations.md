# Actual DG model, clock lift and corrected theta extensions

2026-11-03. P4 source-expansion slice; no arithmetic determinant constructed.
Original2053 lines1308–1478 were read in full and compared with the corrected
book, pinned Keller math/9910179v2 sections3.1/3.3/6.2, and Stacks tags0621,
062F. Exact immutable download hashes are in ../planning/DG_SOURCES.json.
Original manuscripts/source clones stay byte-identical.

## Decisive corrections and surviving constructions

1. An odd ε with dε=1 contracts the underlying k-complex of every unital DG
module, by left h(m)=εm or right h(m)=(-1)^degree mε. H*=0, not k.
The homotopy need not be graded B-linear for a general noncentral ε. On
C=(A→id A) over the actual infinite node, B=End_A(C) has a unit boundary;
even degree projections force every degree−1 graded B-linear endomorphism
of C to vanish. Thus acyclicity/derived zero is not DG-module homotopy zero.
2. The correct nodal model over R=k[ξ,η] is K=R⊕Rε, dε=ξη, ε²=0,
with ε degree−1. The full homogeneous Leibniz check, multiplication-by-f
homotopy, injective f boundary and ideal quotient give a DG quasi-isomorphism
to the actual infinite locally gentle node A=R/(ξη). Terms are R-free,
not asserted A-free. Its completion is proved coefficientwise using mixed
monomials and the actual equal-constant branch pullback, not an assumed
commutation of arbitrary cohomology with completion.
3. σq:ξ↦qξ,η↦q^-1η,ε↦ε is an actual continuous formal/polynomial DG
clock. It is coefficient-semilinear. It preserves diagonal k[[u]],u=ξ+η,
iff q²=1 and fixes it pointwise iff q=1. Declaring branches self-adjoint
further means nonreal phase is not a *-automorphism; unitary implementation
with that convention forces both branch images zero. Other adjoint/operator
constructions are not ruled out.
4. The original double3 example is spherical, not elliptic. Both primary
infinite theta algebras have self Ext1 zero. Elliptic positive Ext has two
summands ending at i−n mod3; spherical positive even self Ext has dimension2,
odd Ext reaches each other vertex once. Full proofs use the existing exact
forbidden-word resolution; exact dart and independent adjacency-matrix counts
agree. Outdegree cannot be substituted for self-Ext endpoint counting.
5. H0 isomorphism alone is not a DG quasi-isomorphism: the square-zero
negative thickening Λ⊕Λδ with d=0 has H−1=Λ. Minimal m2 is associative;
m3 is not its ordinary associator or a measured curvature. The nodal Koszul
model has cohomology only in degree0, so higher m_n vanish by degree. The
polynomial theta's diagonal Koszul grading also allows a weight-compatible
minimal model with higher operations zero. Complete/continuous/derived/HMS
interfaces are separate and cannot be inferred from an unlabelled enhancement.
6. For ordinary commutative node HH0=A. Neither universal trace classes nor
invariance chooses positivity: origin evaluation is positive/invariant and
its negative is an invariant nonpositive trace. The positive origin GNS
space is just C, so this choice supplies no nontrivial arithmetic spectrum.
7. F_(a,b)=ξ^aη^bK is a genuine decreasing DG-submodule filtration indexed
by (N²)^op. Increasing finite boxes in the viewer are only k-subcomplexes,
not R-submodules/DG subalgebras. Inverting both branches makes f a unit and
contracts K; this does not preserve the intended node.

## Implemented verification and boundary

NodalDG.lean checks20 actual exterior-line algebra/differential/Leibniz/
homotopy/augmentation/semilinear-clock/ambient nodal-resolution components.
Focused and full282-report pinned suites pass warnings-as-errors, standard
foundations only. This does not package a categorical Z-graded DGA, formal
completion, concrete q-substitution automorphism, theta Ext identification,
A-infinity transfer, GNS object, HH theory or any GRH proof in Lean.

Exact symbolic checks include64 normal forms,234 theta endpoint dimensions
through degree12, the Koszul identities and the even-projection counterexample.
The viewer's finite windows have independently checked exact finite-field
ranks; numerical phases are illustrative. Independent review checks27
allowed windows/135 inclusions, polynomial identities, adjacency-matrix
counts, source scope and final Lean types. No training/dependencies/GPU runs.

P4 remains in progress. Both project completion gates remain open. After this
source-development milestone, rotate one run to the actual P7 low-gcd kernel
with all original masks, conductors and uniformities; do not repeat the
finished high-gcd/finite-carrier audits. Further P4 work should replace the
next generic source-topic row (linear relations/functorial filtrations) with
actual definitions, proofs and primary infinite-order examples.
