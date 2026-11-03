# An explicit dessin-order bridge to the affine-C diamond resource

Independent read-only review, 2026-11-03, by `surface_completion_audit`.

Verified resource: Huang–Lin–Su, arXiv:2110.02777v2, revised 16 November 2021, 21 pages. [Exact version](https://arxiv.org/abs/2110.02777v2), [PDF](https://arxiv.org/pdf/2110.02777v2).

The relevant model is the oriented A_n chain with endpoint loops epsilon_1,epsilon_n and relations epsilon_1²=epsilon_n²=0, in finite-dimensional **left** modules. The minimal symmetrizer is diag(2,1,...,1,2). The nine-object grid occurs in Proposition 3.12, p.12; its construction uses Propositions 2.6/2.9, pp.5–6, and Lemma 3.10, p.11. The global classification is Theorem 3.14, pp.12–13; Figures 3–4, pp.14–15, concern another component. They are AR meshes, not universally exact three-by-three rows and columns.

I found a positive bridge: the entire finite algebra in this resource is an explicit quotient of a closed infinite-dimensional locally gentle dessin algebra and its completed order. Moreover that infinite dessin has the explicit Chebyshev Belyi map below. Thus the resource supplies genuine intrinsic AR calculations in a specified quotient-annihilator subcategory of an infinite dessin order. It does not automatically identify the AR theory of the whole lattice category.

## 1. Construct the infinite dessin algebra first

Fix n>=3, to remain inside the ordinary affine-C Cartan range used for the paper's root-system/minimal-symmetrizer statements. Work initially over C; the quiver algebra itself can be defined over any field.

Vertices are 1,...,n. There are loops l at 1 and r at n, and two opposite arrows along every edge:

`a_i:i->i+1`, `b_i:i+1->i`, 1<=i<n.

Use travel-order path multiplication. Let A_n be the quotient by precisely

`l²`, `r²`, `a_i b_i`, `b_i a_i`.

The permitted successor is the single cycle

`l a_1 a_2 ... a_(n-1) r b_(n-1) ... b_2 b_1`.

Every vertex has exactly two incoming and two outgoing arrows, and every arrow has one permitted and one forbidden predecessor/successor. This is a closed locally gentle algebra. It is infinite-dimensional because the displayed permitted cycle can be repeated arbitrarily often.

Its forbidden cycles are the two loops l,r and the n-1 two-cycles a_i b_i. Therefore its clean-dessin permutation data has one permitted cycle of length 2n and face lengths

`2 repeated n-1 times, 1,1`.

There are n paired incidences/quiver vertices. The associated ribbon map has one black vertex, n white degree-two vertices and n+1 faces. Euler's equation gives genus zero. Its completed order Lambda_n is the closed split order obtained from the one hereditary cycle order of length 2n by pairing the positions corresponding to each original vertex. The established conductor comparison therefore applies; it is finite free of rank (2n)² over its common DVR.

## 2. An explicit Belyi map identifies that dessin

Let T_n,U_(n-1) be the Chebyshev polynomials and define

`beta_n(z)=1/[1-T_n(z)^2]=1/[(1-z²)U_(n-1)(z)^2]`.

The second equality follows from the polynomial identity obtained by substituting z=cos(theta), using cosine/sine multiple-angle formulas, and then using infinitely many values to identify the polynomials. This is a rational map over Q of degree 2n.

Its branch data can be checked directly:

- Infinity is its only point above zero, with multiplicity 2n.
- The n simple roots of T_n are the points above one; `beta_n-1=T_n²/(1-T_n²)` makes each multiplicity two.
- Its poles at z=1 and z=-1 are simple. The interior zeros `cos(k pi/n)`, 1<=k<n, of U_(n-1) are double poles.
- Differentiating gives `beta_n'=2T_n T_n'/(1-T_n²)^2`, and `T_n'=n U_(n-1)`. Thus there are no further finite critical values. Infinity has already been accounted for.

The passport is exactly

`(2n), (2^n), (2^(n-1),1,1)`.

Riemann–Hurwitz gives `(2n-1)+n+(n-1)=4n-2`, the full degree-2n genus-zero ramification count. Contracting the clean white vertices gives a connected one-vertex ribbon map. Its dual has n+1 vertices, n edges, and degrees 1,1,2,...,2; it is therefore a path. A path has a unique planar ribbon embedding up to the relevant labeling and orientation conventions. Dualizing identifies this clean dessin with the nested-loop dessin of A_n above, not merely one with the same unrestricted passport.

For a completely explicit first case, n=3 gives

`beta_3(z)=1/[1-(4z³-3z)^2]`.

It has passport `(6),(2,2,2),(2,2,1,1)`. The closed quiver has three vertices, six arrows and permitted cycle `l a_1 a_2 r b_2 b_1`.

The elementary algebra/quotient construction also makes sense for n=2, but I do not use that case to invoke an affine-C_1 minimal-symmetrizer statement: the rank-one affine labeling is degenerate and should be separately specified. No n=1 identification with the original two-permitted-loop node is claimed.

## 3. Obtain the resource's algebra by an exact quotient

Choose any orientation Omega of the chain. At each edge retain the arrow matching Omega and kill its opposite. Let I_Omega be the two-sided ideal generated by these killed arrows.

Then

`A_n/I_Omega = H_n(Omega)`.

To prove this, observe that a_i b_i and b_i a_i always contain a killed arrow. No additional relation among retained nonloop arrows survives. The two remaining relations are exactly l² and r². The retained quiver is the chosen oriented chain with its endpoint loops.

Every nonzero oriented path in H_n uses each chain edge at most once and each endpoint loop at most once. Its length is at most n+1. Thus I_Omega contains J^(n+2), is open in the arrow-adic topology, and

`Lambda_n / closure(I_Omega) = H_n(Omega)`

as actual algebras. Completion does not enlarge this finite quotient. For the linear orientation in the n=3 case its dimension is 13, from path counts 3,4,3,2,1 in lengths 0,...,4.

Inflation identifies H_n-mod with the full subcategory

`C_Omega={M in Lambda_n-mod : closure(I_Omega) M=0}`

in the left-module convention. This identification preserves objects, all Hom maps, exact short sequences with terms in the image, direct sums, and the intrinsic AR property when the test objects are restricted to C_Omega. For the project's right-module convention, use the opposite algebra/orientation; A_n is isomorphic to its opposite by exchanging the opposite edge arrows and fixing the loops.

This is a concrete import of the resource into actual modules of an infinite-dimensional dessin order. It is not an existential comparison with an unrelated finite algebra.

## 4. What this quotient bridge preserves, and what must still be proved

The category C_Omega is abelian and fully embedded, but it is generally **not extension-closed in all Lambda_n-mod**. For a killed arrow b_i, the two neighboring simples belong to C_Omega, whereas the two-dimensional representation with only b_i nonzero is an extension of them outside C_Omega. Therefore no extension-closed-subcategory transfer theorem may be applied without checking new hypotheses.

An intrinsic H_n AR sequence remains an exact Lambda_n sequence with the same matrices. Its factorization property is known among objects annihilated by I_Omega. It need not be almost split when all completed-order modules, or all finite-length modules, are allowed as test objects. In particular H_n-projectives are usually not Lambda_n-projective, and additional ambient maps can appear through the killed arrows.

These finite quotient modules have nilpotent common t and are not the nonzero R_0-free lattices of the order. The paper's endpoint-local freeness means freeness over k[l]/(l²) and k[r]/(r²); it is not freeness over k[[t]]. Its tau refers to the intrinsic finite quotient category. A lattice lift or an ambient AR comparison needs a separate exact functor and proof.

For a different fixed dessin order, the above construction is an explicit family-wide example, not a theorem that every order has this quotient. One must exhibit the retained chain, endpoint loops and exact killed-arrow ideal in that order. This is a realistic finite combinatorial acceptance test for importing the resource.

## 5. Nine actual modules for n=3, with words and dimensions

Take the linear orientation 1--a->2--b->3, endpoint loops l,r, with l²=r²=0. In the following table words are written in **travel order**, unlike the paper's compositional order. A minus sign on a letter means a formal inverse in a string word, not an inverse element of the algebra. Start at the indicated vertex; the associated basis has one vector at every successive visited position.

| Label | Travel-order word | Start | Dimension vector |
|---|---|---:|---|
| E=w | a b | 1 | (1,1,1) |
| F=hw | a b r^- | 1 | (1,1,2) |
| H=wh | r^- b^- a^- l a b | 3 | (2,2,3) |
| B=wc | l^- a b | 1 | (2,1,1) |
| D=cw | a b r b^- a^- l^- | 1 | (3,2,2) |
| C=hwc | l^- a b r^- | 1 | (2,1,2) |
| A=cwc | l^- a b r b^- a^- l^- | 1 | (4,2,2) |
| I=hwh | r^- b^- a^- l a b r^- | 3 | (2,2,4) |
| G=cwh | r^- b^- a^- l a b r b^- a^- l^- | 3 | (4,3,4) |

Here h and c in the labels refer to the hook/cohook operations; left/right position matters. For instance hw and wh are different modules, not two names for one symmetric extension. These are the nine modules around the minimal string w in the imported grid.

The basis action is explicit: a direct letter alpha sends its preceding position vector to its following one; an inverse alpha^- sends the following vector to the preceding one. Sum these position maps for repeated occurrences of the same arrow. All other arrow actions are zero. This gives genuine H_3 representations satisfying l²=r²=0. Inflate them to Lambda_3 by setting the killed b_1,b_2 of the closed quiver to zero (the letter b in this table denotes the retained forward arrow a_2, not a killed reverse arrow).

## 6. A redrawable grid, signs, exact meshes and tau

The signed arrows can be drawn as the following rectangular grid. All horizontal arrows point right and all vertical arrows point down:

```
 A=cwc  --p--> B=wc  --i--> C=hwc
   | -p          | p          | -p
 D=cw   --p--> E=w   --i--> F=hw
   | -i          | i          | -i
 G=cwh  --p--> H=wh  --i--> I=hwh
```

The maps p are the natural string-basis projections; i are the natural embeddings. Concretely, the horizontal projections retain the initial travel-word positions; the horizontal embeddings append the final r^- position. The upper vertical projections delete the initial l^- position, with the indicated signs. The lower vertical embeddings prepend the four-letter segment `r^- b^- a^- l`, hence shift each old basis-position index by four; their signs are as drawn.

Each small square is a mesh: the two length-two path composites **sum to zero**. This sign is essential. The four exact AR sequences in the intrinsic quotient category are

`0 -> A -> B directsum D -> E -> 0`,

`0 -> B -> C directsum E -> F -> 0`,

`0 -> D -> E directsum G -> H -> 0`,

`0 -> E -> F directsum H -> I -> 0`,

with components taken from the displayed signed arrows. Thus

`tau(E)=A`, `tau(F)=B`, `tau(H)=D`, `tau(I)=E`.

In integer grid coordinates increasing right/down, the translation is the northwest diagonal `(p,q)->(p-1,q-1)`. The two arrows out of each interior point increase one coordinate. This is the familiar repetitive-grid realization of Z A_infinity^infinity, after reindexing. It is a statement about this component, not a universal shape of an AR quiver.

Rows and columns of the nine-module grid are generally not short exact sequences, and their consecutive composites need not vanish. Therefore this grid must not be relabeled as an exact 3-by-3 diagram of rows and columns. The separate nodal multiplication-by-t diagram in the preceding report really does have that stronger exact-row/exact-column property.

I independently constructed all nine basis representations and twelve signed maps. Exact Fraction checks verified every arrow-intertwining identity, both loop relations, zero mesh composites, injectivity of each mesh's first map, surjectivity of its second map, and matching kernel/image dimensions for all four meshes. The AR rather than merely exact status is imported only after matching the actual string/hook hypotheses. Finite matrix/rank checks alone are not called a proof of the universal almost-split factorization property.

## 7. Proof review, small source cautions and coverage

The relevant induction and hook/cohook hypotheses support this import; I found no fatal gap for the specified H_n model. Two local cautions: Example 3.9(3), p.11, calls its displayed tube rank four although n=4 and only three distinct mouth modules are listed; the consistent rank is three. Also the general sentence on p.7 identifying every homogeneous-tube object as a band is too broad. The needed argument is that band components do not mix with string components; no such converse is required.

The latter caution has a concrete independent check: the Kronecker quotient of the closed four-arrow dessin has the regular modules `a=I_m, b=J_m(0)`. They are string modules, with word `(a b^-)^(m-1) a`, and form a rank-one tube. This does not refute the specialized affine-C classification or the imported grid; it prevents using an overbroad generic sentence as an ambient category theorem.

Read every relevant paragraph/proof on PDF pp.1–13 and 16, including the standing module conventions, the hook/cohook AR formulas, minimal-string criteria, the infinite-ray lemma, the full grid proof and component-classification proof. Visually rendered and inspected pp.12,14,15 at 1800-pixel scale to verify grid signs and distinguish the repeated-diamond component figures. The root-system proof on pp.17–21 was not audited and no new claim about it is made.

Local public-source artifacts: `/tmp/grh-diamond-2110.02777v2-20261103.pdf` (320270 bytes), its layout text, and page12/page14/page15 PNGs. They are new temporary review artifacts, not edits of the project sources. The positive result is an exact quotient/functor and a verified concrete mesh model. Arithmetic Frobenius, positive spectral realization, global L-determinant matching and GRH do not follow from it.
