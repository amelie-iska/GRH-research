# Entire AR components, the theta/node categories and the wind-wheel tile

Read-only primary-source and mathematical review, 2026-11-03. No shared manuscript, source, script or output was changed. This report gives complete drawable components in specified categories; it does not claim a classification of every AR component of every completed dessin order.

## 1. The HLS example is an entire grid, not just nine modules

The pinned primary source is [Huang–Lin–Su, arXiv:2110.02777v2](https://arxiv.org/pdf/2110.02777v2), 16November2021,21pp. Its algebra H_n has an arbitrarily oriented A_n chain, square-zero loops at its two endpoints and no other relations; use n>=3. Lemma3.10 and Proposition3.12 pp11–12 prove infinite hook/cohook rays and the component attached to a minimal type(2,2) string. Theorem3.14 pp12–13 gives the full component inventory: one component containing projectives and injectives, one exceptional tube of rank n-1, homogeneous band tubes, and ZA_infinity^infinity components indexed by those minimal strings. These are finite-dimensional module categories of that exact quotient algebra.

Our concrete infinite clean dessin Lambda_n has the genuine H_n quotient: retain one direction on each doubled chain edge and kill the opposite directions. The Chebyshev Belyi map and the killed-arrow ideal were proved in the preceding reviews. Inflation identifies mod(H_n) with its full quotient-annihilator subcategory of mod(Lambda_n). AR sequences below are intrinsic to that subcategory. It is not extension closed in all modules of the completed order, so neither full faithfulness nor an exact inclusion transfers its almost-split factorization property automatically.

For H_3 with1-a->2-b->3 and endpoint loops l,r, let w=ab in travel convention. It is the minimal type(2,2) string. The entire component can be indexed by (p,q) in Z^2. Put

M(p,q)=M(X_p w Y_q),

where X_p denotes p repeated left-hook operations if p>=0 and -p repeated left-cohook operations if p<0; Y_q denotes q right-hook operations if q>=0 and -q right-cohook operations if q<0. These are operations, not literal letters concatenated to a path. Use the HLS conventions, translated by reversing travel order as in the existing nine-word table. Lemma3.10 and the four-region induction in Proposition3.12 ensure that all these operations continue and cover this component.

There are arrows

M(p,q)->M(p+1,q), M(p,q)->M(p,q+1),

and tau M(p,q)=M(p-1,q-1). Every mesh is the almost-split sequence

0 -> M(p-1,q-1)
  -> M(p,q-1) plus M(p-1,q)
  -> M(p,q) -> 0.

Choose the standard projection/embedding maps with one sign so the two length-two composites add to zero. The previous exact checker verifies the concrete central four meshes; the infinite almost-split extension is the cited hook/cohook theorem, not a finite-test inference.

The already verified nine labels are exactly the window p,q=-1,0,1:

```
(-1,-1) A  -> (0,-1) B  -> (1,-1) C
    |             |             |
(-1, 0) D  -> (0, 0) E  -> (1, 0) F
    |             |             |
(-1, 1) G  -> (0, 1) H  -> (1, 1) I
```

The grid continues indefinitely in all four directions. The axes through E consist of two irreducible monomorphism rays going outward and two epimorphism corays going inward. Rows and columns are not generally short exact. Only the mesh diamonds have the displayed exactness. The source's Figure3/4 pages14–15 describe the projective-injective component, not this ZA_infinity^infinity component; mixing those figures would merge distinct components of the same AR quiver.

## 2. Genuine homogeneous tubes in the infinite polynomial dessin category

Here is a complete ambient example that needs no finite-dimensional replacement algebra. Let A=k[x,y]/xy, with k algebraically closed, and fix lambda!=0. At the smooth maximal ideal(x-lambda,y), all finite-length modules have y=0 and x invertible. The whole finite-dimensional support block is the finite-length category for k[t] at t=0, with x=lambda+t. Its indecomposables are

T_r=k[t]/t^r, r>=1.

Their endomorphism rings are local. They form one entire homogeneous tube, tau T_r=T_r, with irreducible inclusions t:T_r->T_(r+1) and quotients pi:T_(r+1)->T_r. With T_0=0 the meshes are

0 -> T_r --(pi,t)--> T_(r-1) plus T_(r+1)
  --(t,-pi)--> T_r -> 0.

These formulas are exact, including r=1. The right map is almost split: a non-surjective map into T_r lands in tT_r and factors through T_(r-1); a surjective non-retraction from T_s has s>r and factors through T_(r+1). Decompose general source modules into their cyclic indecomposables. Duality gives the left property. Other primary support blocks have zero maps to this one, so the component is ambient in mod_fd(A), not merely an artificially isolated subcategory.

For the actual polynomial elliptic-theta algebra, invert its central u. The normalization is the product of two3-by-3 matrix algebras over k[u,u^-1]. Each nonzero central eigenvalue lambda consequently gives two smooth support blocks and two such ambient tube components. In a selected branch the dimension vector of the length-r object is(r,r,r); choose two arrow maps as identities and the remaining full-turn map J_r(lambda). This describes a family of entire components in the original infinite-dimensional polynomial algebra. They do not extend to continuous finite-dimensional modules over the arrow-adic order, because their central u is not nilpotent.

At the **singular** completed-node point, pure-x Jordan chains do not constitute ambient tubes. They have the intrinsic branch-quotient tube, but even its first candidate right almost-split map fails in the full node finite-length category: let T_2^x have x=J_2,y=0 and T_2^y have x=0,y=J_2. The augmentation T_2^y->k is nonzero, whereas every node-module map T_2^y->T_2^x lands in ann(x)=soc(T_2^x), killed by T_2^x->k. It cannot factor through that map. Thus drawing two pure-branch tubes as the whole completed-node AR quiver is unjustified.

## 3. Full and stable AR quivers of the actual node lattice category

For Lambda=k[[x,y]]/xy, u=x+y, let X=(x),Y=(y). The independently proved classification is Lambda^r plus X^a plus Y^b for all finite R-free lattices. Thus its entire lattice AR quiver has only three vertices Lambda,X,Y. Its arrows are

Y -> Lambda -> X, and X -> Lambda -> Y,

with tau X=Y,tau Y=X. The corresponding two sequences are0->Y->Lambda->X->0 and0->X->Lambda->Y->0, with inclusions and multiplication by x or y. The mesh composites between opposite branches vanish. Lambda is projective and there is no nonsplit AR sequence ending there. The known multiplication-by-u three-by-three diagram is an exact specialization of one of these rows; it is not a nine-object fragment of a missing infinite lattice grid.

The **stable** lattice quiver is smaller still. This exact category is Frobenius: Ext1(X,Lambda)=Ext1(Y,Lambda)=0 follows from the alternating annihilator resolutions, Lambda is projective, and the two displayed embeddings provide enough injectives and projectives. They are exactly the finite free Lambda-sums. Factoring them out leaves X,Y, with

stable End(X)=stable End(Y)=k,
stable Hom(X,Y)=stable Hom(Y,X)=0.

For instance maps X->Lambda->X give exactly xk[[x]] inside End(X)=k[[x]]. Suspension exchanges X and Y, by the two exact rows. Both stable AR triangles have middle term zero:

Y -> 0 -> X -> Sigma Y,
X -> 0 -> Y -> Sigma X,

with the final maps isomorphisms. Therefore its ordinary stable-quiver arrows are absent: it is two isolated vertices with tau exchanging them. It is not a homogeneous tube or a surviving three-vertex AR component. This is an actual small triangulated model; identifying it with the singularity category is the separate classical Gorenstein comparison, not an identification with Perf(Lambda) or all D^b modules.

## 4. Derived AR needs its own category and endpoints

A short exact AR sequence always gives a distinguished triangle, but its triangle need not be almost split in the bounded derived category. For a finite-dimensional algebra the endpoint of a derived AR triangle must be perfect; the appropriate translate uses the derived Nakayama functor shifted by-1. See the directly checked primary [OPS, arXiv:1801.09659v7](https://arxiv.org/pdf/1801.09659v7), Section5.1 pp38–39, which states the perfect-endpoint criterion and gives the graded-arc rotation theorem. Its main algebra is finite-dimensional graded gentle; it does not silently cover arbitrary completed orders.

This distinction is visible in our H_3 grid. In the travel/right-projective convention, P1 has basis

e1,l,a,la,ab,lab,abr,labr.

The projective cover P1->E=M(ab) retains e1,a,ab. Its kernel is lP1 plus abrP3, a direct sum. Multiplication by l:P1->P1 has kernel lP1, so that summand has an endless minimal projective tail. The terminal simple abrP3 repeats through the r loop as well. Hence E has infinite projective dimension. Its HLS module AR sequence is valid, but it does not become a derived AR triangle ending in E. An entire module grid cannot be relabeled as a derived component without checking perfectness and derived translation object by object.

There is a positive derived tube model at the smooth polynomial-node supports above. The block is hereditary, every T_r has the length-one free A-resolution by multiplication with(x-lambda)^r, and its bounded derived category has indecomposables T_r[n]. For each fixed n their meshes form the same homogeneous tube; the connecting arrows in the AR triangles land in T_r[n+1]. This describes the bounded derived category of that finite-length support block, and through the support decomposition the corresponding components of D^b(mod_fd A). It is not a claim equating this with the entire completed-order derived category.

## 5. Ringel's T(45): read the tile as a quilt, with its limits

The primary source is [Ringel, author tokyo.pdf](https://www.math.uni-bielefeld.de/~ringel/opus/tokyo.pdf),57pp, unversioned ICRA Tokyo2010 proceedings text. Section12.5 p30 specifies the five-bar wind wheel; Section13.3 pp38–40 draws T(45). The tile has four finite-word quarters. Its center is the unique nonperiodic two-sided word r(b); its diagonals contain nonperiodic one-sided words. Northwest–southeast circles denote contracting tails; northeast–southwest bullets expanding tails. Contracting objects use ordinary strings, expanding ones require completion, and the mixed central word requires partial completion. Arrow labels distinguish adding hooks from deleting cohooks on either side. Section13.4 p41 glues the five tiles into a torus with five holes; deleting infinite-word points gives the five nonregular string components. Section13.5 notes omitted generic, Pruefer and adic objects. Thus the quilt is not the ordinary finite-module AR quiver, nor a list of all pure-injectives.

For a faithful redraw use four labelled quarters I left,II bottom,III right,IV top. The p38 screen directions are: adding left hooks southeast; deleting left cohooks southeast; adding right hooks northeast; deleting right cohooks northeast. Preserve the circular/bullet diagonals and black-square center. Deleting the diagonals separates the four finite-word quarters of **one tile**; it does not create a single HLS stable grid. The surrounding border and neighboring-tile identifications are needed to recover its finite AR components. Section13.2's corner sequence is tied to its specified quotient W/I; do not promote it to an arbitrary AR sequence of the entire wind wheel without the source's factorization setup.

This is a finite-dimensional special-biserial wind-wheel algebra, not already the completed node or our H_n quotient. No exact presentation/functor identifying T(45)'s category with an actual quotient of the present closed dessin has been supplied. It remains a precise comparison resource. A future import must exhibit that algebra map/category and verify the relevant almost-split or definable-category hypotheses. Its quilt genus is a category construction; it is not automatically the genus of our Belyi curve.

## 6. Semi-invariants and arithmetic scope

The full grids and tubes supply genuine module parameters, irreducible maps and mesh relations. A presentation determinant Hom(f,N) can be computed on these families, but its Ext interpretation still needs the correct projective presentation. For example Y->Lambda->X in the lattice AR row does not make Y projective or X perfect. Applying Hom gives a long exact sequence with Ext terms; it cannot be replaced by a square two-projective determinant on the strength of being an AR mesh.

The tube parameter lambda is an arbitrary central/local-system parameter, not a prime Frobenius eigenvalue. Tau-periodicity or a pictured surface does not construct the arithmetic endomorphism, conductor/gamma factors, a convergent determinant or a positive global spectral comparison. The existing Jacobi theta carrier is a separate locally arithmetic benchmark; the projective multiplicity and full-deck coefficient obstructions remain relevant when trying to turn it into an order functor. None of these AR calculations proves GRH.

## 7. Visual artifacts and exact coverage

Read HLS relevant definitions and proofs pp1–13 and16 in the earlier review, and reread Lemma3.10/Proposition3.12/Theorem3.14 and their proofs pp11–13 here. Reinspected the actual p12 grid image. Its p14/p15 component figures remain available from the prior rendered review. Read Ringel Section12.5 p30, Sections13.1–13.7 pp35–43 including the Euler/orientability proof; visually rendered and inspected every page38–40, plus the p30 source page. This is not a full57-page proof audit; Ringel itself leaves some PartII combinatorics to the reader. Read OPS Section5.1 pp38–39 and the current node/grid manuscript passages. All smooth-tube and stable-node calculations above have explicit independent proofs.

Screenshots suitable for the user's requested illustration:

- /tmp/grh-diamond-v2-page12.png: actual HLS minimal-string diamond and four-region component.
- /tmp/grh-diamond-v2-page14.png and page15.png: the distinct projective-injective component figures.
- /tmp/grh-ringel-ar-scope-38.png: T(45), arrows, finite quarters and infinite limits.
- /tmp/grh-ringel-ar-scope-39.png: its border and neighboring ray/coray pieces.
- /tmp/grh-ringel-ar-scope-40.png: tile neighbors and precise completion conventions.
- /tmp/grh-ringel-windwheel-source-30.png: the actual five-bar source algebra.

All are generated temporary reading artifacts; source PDFs remained unchanged. No new checker or Lean compilation was requested or run in this pass. The earlier exact nine-module checker is corroboration of its finite window, not a replacement for the full component theorem.

Source artifact hashes:
- `/tmp/grh-diamond-2110.02777v2-20261103.pdf`: 320270bytes, SHA-256 `e12063a50ca7e97aa1931bae0abe2b02757f35725b94b515b55ff04cc411004d`.
- `/Users/amelieschreiber/Documents/LaTeX-projects/GRH/research/literature/dessin-extension-20261103/added-resources/ringel-tokyo.pdf`: 616701bytes, SHA-256 `604cea239cfeacd2e2a04fa47ebcceb43423d7120c14492b9e5759d8b4bf15c2`.
