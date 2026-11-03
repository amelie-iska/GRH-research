# The square-zero quotient of the dessin node: primary-source review

Review date: 2026-11-03. This is a read-only mathematical review of the three supplied resources and the proposed quotient-stratum bridge. No shared manuscript, Lean, planning, protected source clone, dependency, or environment was changed. New downloaded literature was placed only in the authorized added-resources cache.

## Result and corrections

For the specified clean sphere example, take the actual completed node
\[
\Lambda=k[[x,y]]/(xy),\qquad J=(x,y),\qquad
B=\Lambda/J^2=k\langle x,y\rangle/(x^2,xy,yx,y^2).
\]
Then the ordinary algebraic module category annihilated by \(J^2\) is exactly \(B\)-Mod. The supplied finite-dimensional domestic-string results apply to this definable subcategory, including its infinite-dimensional modules. They do not classify all modules over the infinite-dimensional order, all its lattices, or continuous/pseudocompact modules.

The precise numerical conclusion is
\[
\operatorname{KG}(B)=\operatorname{CB}(\operatorname{Zg}B)=2
\]
with the papers' convention that isolated points have rank 0. It is not 3. The qualification “non-degenerate” in the introduction's dimension-3 statement for 1-domestic algebras matters here. The algebra B is string/special-biserial and 1-domestic, but is not gentle. Ringel's node resolution gives the Kronecker algebra, but is not a Morita equivalence or an equivalence of the full module categories.

## Exact primary-source pins and coverage

All page numbers below are the printed/PDF page numbers, which agree for these files.

1. Claus Michael Ringel, **The Minimal Representation-Infinite Algebras which are Special Biserial**, [author-hosted PDF](https://www.math.uni-bielefeld.de/~ringel/opus/tokyo.pdf), 57 pages. This URL is not versioned. Its introduction describes the text as written for the ICRA Tokyo 2010 workshop proceedings; that does not establish the PDF's revision date. The exact retrieved artifact, not an invented publication/version date, is pinned by SHA-256:
   `604cea239cfeacd2e2a04fa47ebcceb43423d7120c14492b9e5759d8b4bf15c2`.
   Coverage: introduction and definitions, §§1–6, pp.1–10; the complete node-resolution argument §7.1, p.10; cyclic-word and 4-vertex arguments §§7.2–7.3, p.11; the classification proof §8, pp.12–14; and the universal-cover argument §9, pp.14–16. Examples in §10 were inspected selectively. The later wind-wheel Auslander–Reiten/quilt discussion was not fully audited and is not needed for this bridge. Ringel explicitly says at p.4 that Part II leaves some combinatorial verifications to the reader; do not present the complete 57-page article as independently proof-certified by this review.

2. Gena Puninski and Mike Prest, **Ringel's conjecture for domestic string algebras**, [arXiv:1407.7470v2](https://arxiv.org/abs/1407.7470v2), revised 2015-09-13, 20 pages. SHA-256:
   `583d53dfde45fcdb9955684cae0e4e0ab9a140bf85fca8493b1abf4f326e813d`.
   Coverage: all sections and proofs, pp.1–19, and references through p.20. This includes the homogeneous-element argument, Theorem 5.1 and its reduction to the 1-domestic case, Theorem 5.6, and the domestic proof of Harland's theorem in §6. Imported theorems/references were identified, not recursively re-proved.

3. Rosanna Laking, Mike Prest and Gena Puninski, **Krull–Gabriel dimension of domestic string algebras**, [arXiv:1506.07703v2](https://arxiv.org/abs/1506.07703v2), revised 2015-06-29, 30 pages. SHA-256:
   `c1f432c5ac91920389b981551347fc46880177f244dbbf8c985875abe5aa0433`.
   Coverage: all §§1–10, definitions, examples and proofs through p.29, plus references through p.30. In particular, bridge-quiver definitions, construction of string/band pure-injectives, pp-neighbourhoods, isolation condition, individual ranks and Theorem 10.19 were read. External representation-theoretic and model-theoretic inputs remain external inputs.

Cache directory:
`/Users/amelieschreiber/Documents/LaTeX-projects/GRH/research/literature/dessin-extension-20261103/added-resources/`.
The PDF names are `ringel-tokyo.pdf`, `1407.7470v2.pdf`, and `1506.07703v2.pdf`; same-stem `.txt` files are extracted reading copies. Both arXiv version histories were checked against the primary abstract pages.

## Why B meets the hypotheses

The supplied papers work with finite-dimensional string algebras over an algebraically closed field. Puninski–Prest state this convention explicitly at p.2. Some elementary arguments below work over every field, but the classification and scalar parameterizations should retain the algebraically closed hypothesis unless a separate general-field result is supplied.

The quotient has basis \(1,x,y\), with radical \(kx\oplus ky\) and square-zero radical. It is a commutative local algebra, despite the free-algebra presentation. The quiver has one vertex and two loops; there are at most two incoming and outgoing arrows and every arrow has zero permitted successors/predecessors. Thus it is a monomial special-biserial/string algebra. It fails the additional gentle condition that an arrow have at most one forbidden successor and predecessor: each loop here has two of each. Quotients of locally gentle algebras need not remain locally gentle.

Every string alternates direct and inverse letters, because any two consecutive direct letters, or their inverses, would contain a relation. Immediate cancellation is forbidden. Consequently, after choosing an initial letter the continuation is forced: for example, \(x\) must be followed by \(y^{-1}\), then by \(x\), and so on. Up to cyclic permutation and inversion the unique primitive band is
\[
b=xy^{-1}.
\]
Hence B is 1-domestic. In the oriented bridge-quiver convention there are two vertices, b and its inverse, not two bands up to the equivalence used in counting domesticity. No finite bridge can switch between the two orientations: it would introduce a cancellation or forbidden length-two path. There is no nontrivial self-bridge either. The bridge quiver therefore consists of two isolated vertices, with maximal arrow-length 0.

B is also minimal representation-infinite. For infinitely many \(\lambda\in k\), the two-dimensional modules
\[
X=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad Y=\lambda X
\]
are pairwise nonisomorphic indecomposables. Their endomorphisms are \(\begin{psmallmatrix}a&c\\0&a\end{psmallmatrix}\), a local algebra. An isomorphism commuting with X can intertwine Y=\(\lambda X\) and Y=\(\mu X\) only when \(\lambda=\mu\). Every nonzero proper ideal I of B lies in its two-dimensional radical; the radical of B/I has dimension at most one. Such a factor is k or the dual numbers (or a further zero factor), hence representation-finite. This verifies minimality without relying on a blanket inheritance assertion about node orders.

## What Ringel's node resolution gives

Ringel p.2 defines a representation-theoretic node: a simple that is neither projective nor injective, equivalently a vertex that is neither source nor sink and at which all incoming/outgoing compositions are relations. His loop-counting convention counts each loop twice, so B's vertex is a 4-vertex and a node. Splitting it into a source \(a^-\) and sink \(a^+\) turns x,y into two parallel arrows \(a^-\rightrightarrows a^+\), with no composable pairs. The resulting algebra is the Kronecker path algebra.

Section 7.1, p.10, describes the functor on finite-dimensional modules and its bijection on indecomposables, omitting the source simple of the resolved algebra. Its lemma says that this resolution preserves minimal representation-infiniteness. The introduction, p.2, states the associated stable equivalence. Neither statement says that the original and resolved full module categories are equivalent: B has one simple isomorphism class, Kronecker has two. In particular, an arbitrary stable equivalence alone should not be used to transfer Ziegler topology, pp lattices, pure-injectivity or Krull–Gabriel dimension. The direct domestic-string results supply those conclusions here.

This “node” is a property of a simple module/quiver vertex. It is distinct from a singular point of a geometric nodal curve; the construction is not a geometric normalization or a proof identifying a curve's analytic spectrum.

## Actual pure-injective classification in this stratum

Puninski–Prest Theorem 5.1, p.11, with proof through p.16, says that every indecomposable pure-injective over a domestic string algebra is on Ringel's list. Theorem 5.6, p.16, excludes superdecomposable pure-injectives: every **nonzero** pure-injective has a nonzero indecomposable direct summand. The literal statement suppresses the harmless nonzero qualification; one should include it when restating the result. This does not classify all ordinary modules, nor assert a canonical product decomposition of every pure-injective.

For B the list simplifies to:

- All finite-dimensional indecomposable string modules and the finite-dimensional band modules \(M(b,\lambda,n)\), \(\lambda\in k^*\), \(n\ge1\).
- For each such nonzero scalar parameter, a Prüfer module (direct limit along the band ray) and an adic module (inverse limit along the coray).
- One generic module associated with the sole band.
- Four one-sided periodic-string pure-injectives, with direct-sum/product completion chosen as in the source's expanding/contracting prescription. They provide the two missing Prüfer and two missing adic endpoints, so the infinite list can also be organized as Prüfer and adic families indexed by \(\mathbf P^1(k)\), together with the generic.

There are no two-sided **nonperiodic** strings for B: all continuations are forced periodic. Thus there are no additional two-sided mixed-string points. Do not turn the completely periodic formal string \({}^{\infty}b^{\infty}\) itself into an extra indecomposable pure-injective. Laking–Prest–Puninski p.11, footnote 3, explicitly warns that it is the image of the regular Laurent-polynomial module, whose pure-injective hull is far from indecomposable.

A concrete matrix realization is useful. For a vector space V with endomorphism T, set
\[
F(V,T)=V\oplus V,\quad
X=\begin{pmatrix}0&I\\0&0\end{pmatrix},\quad
Y=\begin{pmatrix}0&T\\0&0\end{pmatrix}.
\]
All four radical products vanish. Endomorphisms have the form
\[
\begin{pmatrix}A&C\\0&A\end{pmatrix},\quad AT=TA,
\]
with arbitrary k-linear C. The ideal of C-matrices is square-zero; the quotient is the centralizer of T. Taking T a Jordan block gives the finite families. For \(\lambda\ne0\), this is the usual Laurent band construction. Taking T on the corresponding Prüfer, adic or rational-function module gives the infinite families; the other affine chart exchanges x and y. The exact band construction and its strong representation-embedding property, including preservation of pure-injectivity, are described in Laking–Prest–Puninski §5.3 and Theorem 5.2, pp.11–12. This is an explicit construction, not a consequence of the finite-dimensional node functor alone.

## Relative dimensions and an isolated-band base case

Laking–Prest–Puninski Theorem 10.19, p.29, gives KG equal to the maximum bridge-path length plus 2. Length means number of arrows, so an isolated vertex has length 0. Therefore KG(B)=2. The introduction, p.3, only attributes dimension 3 to 1-domestic **non-degenerate** string algebras. For comparison, allowing yx while killing \(x^2,y^2,xy\) creates a bridge between band orientations; killing yx too removes it. Applying the dimension-3 slogan to B would be an error.

The pointwise ranks specialize as follows:

| Points in Zg(B) | Relative CB rank | Source |
| --- | ---: | --- |
| Finite-dimensional indecomposables | 0 | Theorem 5.1, p.10 |
| One-sided periodic-string points | 1 | Theorem 10.4, p.20, with indent 0 |
| Band Prüfer points | 1 | Theorem 10.10, p.24, with both indents 0 |
| Band adic points | 1 | Theorem 10.14, p.26, with both indents 0 |
| Unique generic | 2 | Theorem 10.16, p.27, with both indents 0 |

Thus the first derivative removes finite points, the second contains just the generic, and the third is empty. Under §8.1's convention, p.16, the space has rank 2, not 3. Ordinary commutative Krull dimension of the Artin ring B is 0; this is a different invariant.

There is a small presentation omission worth recording if the generic-rank proof is reproduced: the printed proof of Theorem 10.16 at p.27 starts by choosing a band adjacent to b on a longest path, which is impossible for an isolated vertex. The isolated-band lower bound is instead supplied by the closed Laurent-band Ziegler embedding of §5.3: the generic of the PID Laurent ring has rank 2 in that subspace. The classified remaining points have rank at most 1, giving the matching upper bound here. No invalid adjacent-band choice is required. This does not invalidate the stated theorem or this specialization.

## Exact definable inflation, and limits of its scope

Let \(q:\Lambda\twoheadrightarrow B\). Restriction of scalars is an exact fully faithful equivalence
\[
B\text{-Mod}\ \simeq\ \mathcal D
=\{M\in\Lambda\text{-Mod}:J^2M=0\}.
\]
Endomorphism rings and direct decompositions are unchanged. The class D is axiomatized by the linear equations \(am=0\) for \(a\in J^2\), and is closed under products, directed colimits and pure submodules. It is therefore definable. A system of linear equations over Λ on an object of D is exactly the corresponding system with coefficients reduced in B; conversely B-coefficients lift to Λ. The solvability criterion for algebraic compactness consequently proves that pure-injectivity is equivalent in the two module categories.

The same reduction/lifting of coefficients identifies pp formulas on D. Hence
\[
\operatorname{Zg}B\longrightarrow\operatorname{Zg}\Lambda
\]
is a homeomorphism onto the closed subset consisting of indecomposable pure-injectives annihilated by J². The rank table and KG=2 concern this closed subspace and the corresponding relative pp/functor category. Ambient CB ranks can be larger; the ambient order's global KG dimension is not computed by these results.

D is not generally extension-closed inside Λ-Mod, despite being an abelian module category in its own right. In this actual example, \(\Lambda/(x^3,y)\) is an extension of \(\Lambda/(x^2,y)\) by k; the latter two are killed by J², whereas the middle module is not. Thus the bridge does not identify all ambient Ext groups, Auslander–Reiten sequences, or a full derived subcategory closed under arbitrary extensions.

There is also a concrete lattice restriction. The node is finite free of rank 2 over \(k[[t]]\), where t=x+y. On every module in D, \(t^2=x^2+y^2=0\). Consequently a nonzero torsion-free \(k[[t]]\)-lattice cannot lie in D. This stratum is a torsion boundary of the completed order, not a classification of its nonzero lattices. The primary papers use ordinary algebraic modules, so statements about continuous/pseudocompact modules require a separately specified category and topology.

## Why ordinary invariants miss the family, but pp formulas do not

For the displayed 2-dimensional family, conjugating by diag(t,1), t nonzero, scales both X and Y by t. Its orbit closure contains the zero pair, which represents k⊕k. Therefore every invariant regular function has the same value on all parameters λ.

More generally, for any B-representation \((X,Y)\), put \(R=\operatorname{im}X+\operatorname{im}Y\) and \(K=\ker X\cap\ker Y\). Radical-square-zero relations give \(R\subseteq K\). Choose a decomposition \(M=R\oplus S\oplus T\), where \(K=R\oplus S\). Both operators vanish on K and map T into R. Conjugation scaling R by t scales both operators by t, giving zero as a limit. Thus invariant regular functions on the **reduced** affine representation variety are constant over an algebraically closed field. This pointwise/reduced assertion should not silently be strengthened to a statement excluding nilpotents in the invariant ring of a nonreduced representation scheme.

The modules are nevertheless pairwise nonisomorphic, and pp geometry detects them explicitly. For a fixed λ, the pp formula
\[
\varphi_\lambda(z):\ \exists v\;(z=xv\ \wedge\ (y-\lambda x)v=0)
\]
has value im X, a one-dimensional space, on \(M_\lambda\). On \(M_\mu\) for \(\mu\ne\lambda\), the condition forces \(xv=0\), so its value is zero. The pp pair \(\varphi_\lambda/(z=0)\) therefore separates the corresponding Ziegler points. This is an explicit witness that a collapsed affine invariant quotient does not imply a trivial pp spectrum.

Semi-invariants/stability on the separated Kronecker quiver can recover projective parameters, but that is a different group action and moduli problem. A single-vertex fixed-dimension King's weight is forced to be zero; one should not identify it with the two-vertex Kronecker stability calculation without constructing the change of problem.

## Permitted next claim

A precise usable statement is: “For the clean spherical dessin β=4z(1−z), the radical-square quotient of its completed nodal order has a closed definable module stratum whose indecomposable pure-injectives are explicitly classified by domestic string theory; its relative pp/Krull–Gabriel and Cantor–Bendixson dimensions are 2, while the ordinary affine invariant quotient collapses the visible band family.”

This supplies a rigorous infinite-module boundary test for a specific infinite-dimensional dessin-derived order. It supplies neither a classification of all locally gentle completed orders nor an arithmetic determinant, purity theorem, trace formula identifying a completed L-function, or a proof of RH/GRH.
