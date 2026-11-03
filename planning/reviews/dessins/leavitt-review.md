# Infinite dessin algebras: Leavitt obstruction and a concrete Fock extension

Independent mathematical review, 2026-11-03. Only infinite-dimensional closed locally gentle algebras and their completed surface orders are considered. No finite-dimensional gentle quotient is substituted. Shared sources, scripts, manuscripts and environments were not edited. Exact exploratory computations ran in memory, without invoking existing report writers.

## Results

1. The proposed nodal, elliptic and spherical Belyi examples, permutations, Cartan determinants and order ranks are consistent.
2. Imposing the original forbidden products on the ordinary Leavitt algebra, graph C* algebra, or ordinary graph-Toeplitz algebra of the original quiver forces the algebra to be zero. CK2 is not needed for this obstruction.
3. The permitted-arrow transition graph gives valid matrix Laurent/circle algebras, but forgets the alpha gluing. The displayed torus and sphere have the same such algebras.
4. The faithful allowed-path Fock algebra has the proposed nonzero extension by terminal-sector compacts. The connecting map is minus the unsigned incidence matrix of the original cellular graph. A necessary correction to the explicit unitary lift is given below.
5. All three proposed K-group computations are correct. They distinguish the interval and loop examples but not the torus and sphere theta dessins. No arithmetic determinant identity or RH/GRH conclusion follows.

No novelty claim is made: the subproduct/monomial operator-algebra literature is a relevant setting for this construction.

## 1. Fixed conventions

Let H be a finite nonempty dart set, alpha a fixed-point-free involution, and sigma a rotation permutation; assume the group they generate is transitive. Set

\[
\phi=\alpha\sigma^{-1}.
\]

Graph vertices are sigma-orbits, edges are alpha-orbits, and faces are phi-orbits. Thus

\[
2-2g=\#\mathrm{cyc}(\sigma)-|H|/2+\#\mathrm{cyc}(\phi).
\]

Let [h] denote the alpha-orbit of h. The gentle quiver has vertices [h] and arrows

\[
a_h:[h]\longrightarrow[\sigma^{-1}h].
\]

Words here are in travel order: ab means traverse a then b. This is the convention in the primary Leavitt definitions below; sources writing paths right to left need their displayed relations reversed.

The allowed successor of a_h is a_(sigma^-1 h); the forbidden successor is a_(phi h). Both begin at the head of a_h since [phi h]=[sigma^-1 h], and they are distinct since alpha has no fixed points. They are permutations of all arrows. Consequently the algebra A=kQ/I is infinite-dimensional: every allowed cycle repeats indefinitely.

Write Lambda for its arrow-adic completion. Use q for path length and u for the common DVR parameter of an order. A permitted 3-cycle has path degree three but can represent one power of a normalization uniformizer. These variables must not be identified.

## 2. Exact geometric examples

### Nodal interval

The degree-two map beta(z)=4z(1-z) on P1 has two simple points over zero, a double point at z=1/2 over one, and a double pole at infinity. Its clean triple is

\[
\sigma=(0)(1),\quad\alpha=(01),\quad\phi=(01).
\]

The graph has two vertices, one edge, one face, and genus zero. The quiver has one vertex and loops x,y, with

\[
A=k\langle x,y\rangle/(xy,yx)=k[x,y]/(xy),\quad
\Lambda=k[[x,y]]/(xy).
\]

Its permitted cycles have lengths 1,1; the forbidden cycle has length two:

\[
\det C_A(q)=\frac{1-q^2}{(1-q)^2}=\frac{1+q}{1-q}.
\]

The normalization is k[[x]] x k[[y]]. With u=x+y, the order is k[[u]][x]/(x^2-ux), of rank two over k[[u]]. The ordered forbidden-arm period is two, while the unordered positive syzygy tail has period one, by exchanging its two summands.

### Elliptic theta dessin

On the smooth projective cubic E:y^2=x^3-1, beta=x^3 has degree six. Over zero there are x=0,y=+/-i, each with zero order three. Over one, y=0 at the three cube roots of one, and beta-1=y^2, giving three indices two. At the unique point at infinity x has pole order two, so beta has pole order six. Total ramification is 4+3+5=12, consistent with genus one.

Use

\[
\sigma=(012)(345),\quad \alpha=(03)(14)(25),\quad
\phi=(051324).
\]

With v0={0,3}, v1={1,4}, v2={2,5}, the arrows are

\[
a_0,a_3:v0\to v2,\quad
a_2,a_5:v2\to v1,\quad
a_1,a_4:v1\to v0.
\]

The allowed cycles are (a0,a2,a1), (a3,a5,a4); the forbidden cycle is (a0,a5,a1,a3,a2,a4). Therefore

\[
\det C_A(q)=\frac{1-q^6}{(1-q^3)^2}
=\frac{1+q^3}{1-q^3}.
\]

The normalization is H3 x H3, with H3 the standard hereditary tiled 3-by-3 order. Mapping a common u to u_i I3 gives rank 9+9=18. Gluing the diagonal residues changes finite-length data, not generic rank.

For the simple at v0, positive syzygy top pairs are (v2,v2),(v1,v1),(v0,v0), repeated. Three forbidden steps exchange the two initial arrows. Thus the unordered ungraded positive syzygy tail has least period three; individually labelled forbidden chains have period six. The distinct top pairs exclude periods one and two.

### Spherical theta dessin

For beta(z)=4z^3/(1+z^3)^2 on P1, the zeros at zero and infinity have order three; the three roots of z^3=1 have index two over one; the three roots of z^3=-1 are double poles. Total ramification is 4+3+3=10, as required for degree six and genus zero.

Use

\[
\sigma=(012)(345),\quad \alpha=(03)(15)(24),\quad
\phi=(04)(13)(25).
\]

With v0={0,3}, v1={1,5}, v2={2,4}, its arrows are

\[
a_0:v0\to v2,\ a_2:v2\to v1,\ a_1:v1\to v0;
\quad
a_3:v0\to v1,\ a_5:v1\to v2,\ a_4:v2\to v0.
\]

Its allowed cycles are again (a0,a2,a1), (a3,a5,a4); forbidden cycles are (a0,a4),(a1,a3),(a2,a5). Hence

\[
\det C_A(q)=\frac{(1-q^2)^3}{(1-q^3)^2}.
\]

The normalization is again H3 x H3 and its common-DVR rank is 18. Positive syzygy top pairs at v0 are (v2,v1),(v0,v0), repeated, giving least unordered tail period two.

The torus and sphere have the same abstract center and normalization types but different face/forbidden data.

### A concrete single-loop dessin for the torsion example

The degree-two clean Belyi map beta(z)=(z+1)^2/(4z) on P1 has a double zero at -1, a double point over one at 1, and simple poles at zero and infinity. It realizes

\[
\sigma=(01),\quad\alpha=(01),\quad\phi=(0)(1).
\]

The underlying cellular graph has one vertex and one loop. Its infinite algebra is k<x,y>/(x^2,y^2), with one allowed 2-cycle and two forbidden 1-cycles. Its completion has normalization H2 and common-DVR rank four. This is distinct from the nodal interval even though both scalar Cartan determinants simplify to (1+q)/(1-q).

### Independent checks

In-memory exact enumeration checked the arrows, allowed/forbidden cycles, Euler characteristics, normalization ranks and syzygy top sequences. Fraction evaluations at q=1/2,1/3,-1/2 checked the proposed determinant ratios. For sigma=(012)(345), enumeration of all 15 clean involutions and its 18-element centralizer shows that the three involutions with phi type (6) form one simultaneous-conjugacy orbit, and likewise the three with phi type (2,2,2). Thus these passports identify the displayed triples up to relabelling; no specific analytic path-lifting labelling is asserted.

## 3. Why the Cartan determinant retains more than the permitted graph

For arrow weights w_a, let T_ab=w_b for allowed adjacency and U_ab=w_b for forbidden adjacency. Let S_va=w_a when s(a)=v, and R_av=1 when r(a)=v. Then RS=T+U and the weighted path matrix is

\[
C=I+S(I-T)^{-1}R.
\]

Sylvester's determinant identity gives

\[
\det C=\frac{\det(I-T+RS)}{\det(I-T)}
=\frac{\det(I+U)}{\det(I-T)}.
\]

The two successor permutations decompose into cycles, giving numerator factors 1-(-1)^l w(c) and denominator factors 1-w(c). This proves the displayed rational formulas, rather than merely checking sample values. The forbidden numerator is precisely what separates the sphere and torus Cartan determinants. Removing U changes the invariant.

## 4. Ordinary CK1 is incompatible with these gentle relations

Primary definitions checked:

* Abrams–Aranda Pino, The Leavitt path algebra of a graph, arXiv:math/0509494v1, Definition 1.3, printed/physical p3: https://arxiv.org/pdf/math/0509494v1 .
* Bates–Pask–Raeburn–Szymanski, The C*-Algebras of Row-Finite Graphs, NYJM 6 (2000), section 1, printed p309/physical p3: https://nyjm.albany.edu/j/2000/6-14.pdf .

If ab=0 is a composable forbidden product, the ordinary relation a*a=p_r(a) implies

\[
0=a^*(ab)=p_{r(a)}b=p_{s(b)}b=b.
\]

Every arrow is a forbidden successor, so all arrows vanish. Every quiver vertex is the range of an arrow, so b*b=p_r(b) then kills every vertex. The finite unit is zero.

Thus the Leavitt quotient and the graph-C* closed-ideal quotient are zero. The same applies to the ordinary Cohn/graph-Toeplitz setting: CK2 was never used. The required coverage hypotheses hold for these closed dessins; this is not a claim about every graph with one extra monomial relation.

For example, on the original nodal one-vertex two-loop graph, x*x=y*y=1 and xy=0 already give y=0, then 1=0. The original gentle algebra is not the two-loop Leavitt/Cuntz algebra.

## 5. Valid permitted-state Leavitt and circle algebras

The graph G_per has vertices H and arrows h -> sigma^-1 h. It is a disjoint union of directed cycles, with lengths the sigma-cycle lengths. For one length-l cycle, the assignments

\[
p_i=E_{ii},\quad e_i=E_{i,i+1}\ (i<l-1),\quad
e_{l-1}=zE_{l-1,0}
\]

and the reversed matrix units for ghosts, with z^-1 at the wrap, give

\[
L_k(C_l)\cong M_l(k[z,z^{-1}]).
\]

Paths/ghosts supply the matrix units and full-cycle Laurent parameter, and path normal forms give the inverse identification. Over C, z as the circle coordinate gives

\[
C^*(C_l)\cong M_l(C(\mathbb T)).
\]

The nonzero matrix projections and the gauge action prove faithfulness by Bates et al., Theorem 2.1, printed p311/physical p5. The gauge action is explicit: z -> w^l z combined with conjugation by diag(1,w^-1,...,w^{-(l-1)}).

Consequently the permitted-state construction gives the direct sums of these algebras over sigma-cycles. It gives two Laurent/circle components for the node and two M3 Laurent/circle components for both theta dessins. Alpha has disappeared.

The polynomial cycle path algebra, its hereditary formal completion, its Laurent localization and its C* circle completion are distinct. Completing gives H_l over k[[u]], then localization gives M_l(k((u))); inverting before formal completion gives the Laurent polynomial algebra. Original diagonal residue maps at u=0 cannot extend to a Laurent variable that has become invertible. Reattaching alpha as extra structure is possible, but the unmarked direct sum alone has not retained the original glued order.

## 6. Ordinary graph Toeplitz versus a chosen matrix Toeplitz cover

For l=1 the graph Toeplitz algebra is the classical Toeplitz algebra T. For l>1 it is not M_l(T). Indeed K0 of the graph Toeplitz algebra of a finite graph is free on its vertices, so

\[
K_0(\mathcal T(C_l))=\mathbb Z^l,\quad K_0(M_l(\mathcal T))=\mathbb Z.
\]

The primary location checked is Brownlowe–Laca–Robertson–Sims, Reconstructing directed graphs from generalised gauge actions on their Toeplitz algebras, arXiv:1812.08903v1, Remark 4, physical/printed p3: https://www.aidansims.com/papers/BLRS2018.pdf .

The graph Fock defects generate l independent compact-operator ideals. The matrix Toeplitz extension has one simple compact ideal M_l(K), although both quotients are M_l(C(T)). Thus a matrix Toeplitz cover is a chosen different extension, not the graph Toeplitz algebra. Stabilization does not remove the K0-rank discrepancy.

Fowler–Raeburn, The Toeplitz algebra of a Hilbert bimodule, arXiv:math/9806093v3, https://arxiv.org/abs/math/9806093v3 , supplies the correspondence/Fock framework; its uniqueness hypotheses must be checked for the actual construction.

## 7. A faithful infinite Fock algebra retaining every zero relation

Let F=ell^2(permitted finite paths), including one vacuum delta_v per original quiver vertex. Let P_v project onto paths starting at v. Prefix creators are

\[
L_a\delta_w=
\begin{cases}\delta_{aw},&aw\text{ survives and is composable},\\0,&\text{otherwise}.\end{cases}
\]

Let Q_a=L_aL_a*. Write g(a) for the allowed successor and f(a) for the forbidden successor. Then exactly

\[
L_aL_{f(a)}=0,\qquad
L_a^*L_a=P_{r(a)}-Q_{f(a)}
=\mathrm{vac}_{r(a)}+Q_{g(a)},
\]
\[
P_v-\sum_{s(a)=v}Q_a=\mathrm{vac}_v.
\]

These follow on path basis vectors. The missing forbidden continuations make L_a*L_a a proper subprojection of P_r(a), which avoids the CK1 collapse.

The polynomial representation of A over C is faithful: a finite linear combination of distinct paths, applied to the sum of all vertex vacua, produces that same combination of distinct orthogonal path vectors. Let T_A=C*(P_v,L_a). This is a concrete nonzero C* algebra with all the original quadratic zero relations, but it is not the ordinary graph C* algebra of Q.

The scalar monomial analogue is explicitly described in Kakariadis–Shalit, On operator algebras associated with monomial ideals in noncommuting variables, arXiv:1501.06495v3, section 4.1/Lemma 4.2, printed p15/physical p16: https://arxiv.org/abs/1501.06495v3 . The multi-vertex assertions here are proved directly using path vectors, not obtained by silently treating all vacua as one.

## 8. The compact ideal and cycle quotient: proof

For an original quiver vertex v, let F_v be the terminal sector spanned by paths ending at v. Prefix operators and adjoints preserve terminal sectors.

For paths p,q ending at v,

\[
L_p\,\mathrm{vac}_v\,L_q^*=|\delta_p\rangle\langle\delta_q|.
\]

Therefore the closed ideal J generated by the vacua contains every K(F_v). Conversely their finite direct sum is an ideal for all block-diagonal prefix operators and contains the vacua. Hence exactly

\[
J=\bigoplus_{v\in Q_0}\mathcal K(F_v).
\]

It is generally not the full compact algebra K(F), since cross-terminal matrix units are absent.

Modulo J, the operators q(L_a) have initial projection q(Q_g(a)) and range projection q(Q_a). Thus they are a CK family for the allowed arrow-state graph G_per. They generate T_A/J because q(P_v)=sum_out q(Q_a).

Each q(Q_a) is nonzero: Q_a has infinite rank in some terminal sector, from repeated allowed-cycle prefixes, and therefore does not belong to J. The length gauge action U_z delta_p=z^|p| delta_p preserves J and induces the usual graph gauge action on the quotient. Gauge-invariant uniqueness now proves the surjection is faithful. Thus there is an exact sequence

\[
0\longrightarrow\bigoplus_{v\in Q_0}\mathcal K(F_v)
\longrightarrow T_A
\longrightarrow\bigoplus_{c\in\mathrm{cyc}(\sigma)}
M_{|c|}(C(\mathbb T))
\longrightarrow0.
\]

This establishes the proposed quotient without identifying T_A with a graph-Toeplitz algebra.

## 9. The connecting map: explicit lift and its defect

Choose an allowed cycle c=(a,g(a),...,g^{l-1}(a)). A generator of its quotient K1 is the corner loop unitary plus the complementary identity. A subtlety is important:

\[
L_c^*L_c=Q_a+\mathrm{vac}_{s(a)}.
\]

Thus L_c+(1-Q_a) is not an isometry: its initial pieces overlap at the vacuum. The correct lift is

\[
W=L_cQ_a+(1-Q_a).
\]

Then W*W=1. Its range defect is

\[
D=1-WW^*=Q_a-L_cQ_aL_c^*.
\]

On path basis vectors, D projects onto the l permitted paths starting with a whose lengths are 1,...,l. All longer such paths have a full c prefix followed by another a, so belong to the range of L_cQ_a. The terminal vertices of these l defect vectors count the darts in the sigma-cycle, with their alpha-edge labels.

With the convention delta[u]=[1-W*W]-[1-WW*], this proves

\[
\delta(c)=-\sum_{h\in c}e_{[h]}.
\]

This is minus the unsigned edge-by-vertex incidence matrix of the original cellular graph. A loop has two darts at the same vertex and contributes 2. Choosing the opposite boundary-sign convention changes the global sign, not the kernels, cokernels or K-group conclusions.

## 10. K-groups and what they cannot detect

Write B for that unsigned incidence map Z^(sigma-cycles) -> Z^(alpha-edges). Since K1(J)=0 and quotient K0 is free, the six-term sequence yields

\[
K_1(T_A)\cong\ker B,\quad
0\to\mathrm{coker}B\to K_0(T_A)\to
\mathbb Z^{\#\mathrm{cyc}(\sigma)}\to0.
\]

The last sequence splits abstractly, noncanonically.

* Nodal interval: B(m,n)=m+n. Thus K0=Z^2 and K1=Z.
* Single-loop graph: B(n)=2n. Thus K0=Z plus Z/2 and K1=0.
* Either theta dessin: B(m,n)=(m+n)(1,1,1). Thus K0=Z^4 and K1=Z.

More generally, for a connected original graph with E edges and V vertices, spanning-tree integer elimination gives: in the bipartite case, rank B=V-1 and coker B is free of rank E-V+1; in the nonbipartite case, rank B=V and coker B is Z^(E-V) plus Z/2. The obstruction in the latter case is the odd-cycle parity, with loops included. Consequently

\[
\begin{array}{c|cc}
&K_0(T_A)&K_1(T_A)\\\hline
\text{bipartite}&\mathbb Z^{E+1}&\mathbb Z\\
\text{nonbipartite}&\mathbb Z^E\oplus\mathbb Z/2&0
\end{array}
\]

for this closed connected setup. These coarse groups depend on the underlying incidence graph, not its cyclic embedding. In particular they do not recover genus, distinguish the two theta examples, or replace the forbidden numerator of the Cartan determinant. No unmarked-C*-algebra reconstruction theorem for the full dessin is asserted.

## 11. Formal completion, literature scope, and the next analytic obligation

The allowed-path Hilbert space is infinite in every example here. Nevertheless arbitrary formal series in Lambda need not converge in the Fock operator norm. A one-branch series sum(n! x^n) is a simple example with no norm-convergent meaning under an isometric branch shift. The polynomial faithful representation and its chosen operator norm completion must be distinguished from the full adic completed order.

Shalit–Solel, Subproduct systems, arXiv:0901.1422v3, https://arxiv.org/abs/0901.1422v3 , is a general starting point. Its v3 version record explicitly withdraws an unrestricted product-system embedding/dilation assertion from v2. Kakariadis–Shalit likewise distinguish tensor, generated C*, compact-quotient and boundary/C*-envelope constructions; they must not be identified without their stated hypotheses.

A concrete next theorem can work with the full labelled prefix/defect data and a specified analytic summability algebra. It must construct an actual positive-metric or self-adjoint operator and prove that its determinant or trace equals the target arithmetic expression, retaining the forbidden/gluing data and all conductor and archimedean terms. Domains, trace-class or compact-resolvent properties and analytic convergence remain separate obligations. The exact Fock extension above is an infinite dessin-focused operator result, not an arithmetic RH/GRH proof.

Additional in-memory checks passed 1360 basis initial-projection/forbidden-product equalities on paths of lengths 0 through 8 in the four infinite examples, using untruncated prefix operations. The corrected cycle lifts were injective on all tested basis vectors; their finite defects had exactly the predicted terminal incidence counts, including the loop count two. These bounded checks supplement the infinite path-basis proofs; they do not replace them.

Coverage: the cited primary definitions/results were inspected at the stated locations; the examples, collapse proof, matrix models, Fock extension, connecting map and K-group calculations were independently derived. This is a focused literature review, not a full audit of all the cited operator-algebra papers.
