# Independent full review: Surface Algebras I and projective resolutions

Date: 2026-11-03. Read-only review of source repositories. This report and the explicitly authorized new literature downloads are generated artifacts. No shared manuscript, planning, Lean, lockfile, or source clone was edited.

## Identification and coverage

The current primary version is Amelie Schreiber, **Surface Algebras I: Dessins D'enfants, Surface Algebras, and Dessin Orders**, arXiv:1810.06750v5, submitted/revised 24 February 2023. This is not literally titled “Surface Algebras and Surface Orders I” in v5. The PDF has 54 pages; printed and physical page numbers agree. Its internal date is February 27, 2023. Primary version record: https://arxiv.org/abs/1810.06750v5 ; PDF: https://arxiv.org/pdf/1810.06750v5 .

Immutable downloaded originals are in:
`/Users/amelieschreiber/Documents/LaTeX-projects/GRH/research/literature/projective/surface-I-v5-independent-audit-20261103/`.

* `arxiv-1810.06750v5.pdf`, SHA256 `6fa9663600cc670e36b2504642989fe8a83420f9cc11cb2a3aadee3d72e7d43a`.
* `arxiv-1810.06750v5-source.tar`, SHA256 `1e52cc223ce3a8b036e69e53fbf833c9fa5e74101a2be9a0892a437dc01aebff`.

The source archive was listed before extracting its `main.tex` to `/tmp/grh-surface-I-v5-independent.tex`; the archive was not unpacked over any project. Local PDF text is `/tmp/grh-surface-I-v5-independent.txt` (3076 lines). I read the entire PDF text, all mathematical sections, all displayed proofs, and the examples, with source inspection for the center and resolution statements. Rendered physical pages 28–31 were inspected for formulas and conventions. This is full textual review, not verification of every cited external theorem, historical claim, or every arrow in every illustration. The external mathematical dependencies were not all independently reproved. Three newer primary PDFs were downloaded under distinct filenames in the same new directory; their review was focused, as specified below.

| Material | Pages | Review outcome |
|---|---:|---|
| Abstract, §1 | 1–3 | Program and announced consequences distinguished from proved algebra |
| §2.1–2.12 | 3–10 | All read; several universal representation-theoretic and arithmetic claims require correction |
| §3.1–3.4 | 10–15 | Permutation/ribbon-graph construction usable; convention and Euler-sign issues |
| §4 | 15 | Directed medial quiver construction read, including torus example |
| §5, Thm 5.4, examples | 15–18 | Closed locally gentle subclass; reconstruction needs equivalences and Galois-action qualification |
| §6, Prop 6.7 | 18–21 | Pullback construction usable with common residue fields and an explicit base; broad Dedekind scope not enough for later minimal covers |
| §7 | 21–22 | Nodal example supplies an exact resolution test and a special-fiber test |
| §8 | 22–27 | All examples read; projective arms correct in completed equicharacteristic setup; some radical/quotient notation slips |
| §9, Lem 9.2, Thm 9.1 | 27–29 | Center formula needs correction; normalization invariant is much weaker than orbit classification |
| §10, Thm 10.1, Cor 10.2 | 29–31 | Forbidden-arrow resolution mechanism valid after indexing repair; “periodic” and “exact lcm” require substantive qualification |
| §11 | 31–38 | All resolution/gluing examples read; ordered dart traces carry more information than periods alone |
| §12 | 38–39 | Background read; distinguish p-adic digits and the actual topology of the adelic quotient |
| §13.1–13.5 | 39–45 | Local order examples useful; geometric/arithmetic identifications include false steps |
| §14.1–14.3, Thms 14.2–14.3, Cor 14.4 | 45–51 | Artin induction quoted correctly before an unjustified integral strengthening; invariant/holomorphy conclusions do not follow |
| §15, references | 51–54 | Read; bibliography not comprehensively verified |

## Main conclusion

There is a concrete and worthwhile projective-resolution track here: compute forbidden-arrow chains, the associated syzygies, the graded Ext algebra, and the Cartan/Hilbert matrices, while preserving the completed-order and special-fiber distinction. It can replace ambiguous resolution formulas with actual exact complexes. It does not currently supply the arithmetic determinant identity, positive metric, self-adjoint realization, or analytic convergence needed for a Hilbert–Pólya argument.

The most important corrections are (1) eventual versus genuine periodicity, including a counterexample to the claimed exact minimal lcm period; (2) normalization does not determine a passport or Galois orbit; (3) a sign is applied twice in the original Hilbert–Pólya preprint's graded Cartan/Ext inversion; and (4) the surface-order and finite-dimensional special-fiber resolutions must not be identified by ordinary tensoring.

## 1. Exact corrected resolution, with conventions fixed

Work first with a finite quiver $Q$, a quadratic monomial ideal $I$, and $A=kQ/I$. Impose the closed gentle hypotheses of Definition 5.3: exactly two incoming/outgoing arrows at each vertex, and for each arrow a unique allowed and unique forbidden successor and predecessor. Write paths right to left, as the paper does. For an arrow $a:i\to j$, define $f(a):j\to k$ to be the unique arrow satisfying $f(a)a\in I$. The map $f:Q_1\to Q_1$ is a permutation. This avoids the paper's shifting uses of $\phi$, $\phi^{-1}$, vertices, and half-edges.

Use **left** projectives $P_i=Ae_i$. The map $P_j\to P_i$ associated to $a:i\to j$ is **right multiplication by $a$**, $u\mapsto ua$; this is left $A$-linear. Left multiplication by an arbitrary arrow is not a left $A$-module homomorphism. A right-module convention gives the transposed formulation.

Let $a_1,a_2$ be the outgoing arrows from $i$, and $a_{r,m}=f^{m-1}(a_r)$. Then

\[
P_0=Ae_i,\qquad
P_m=Ae_{h(a_{1,m})}\oplus Ae_{h(a_{2,m})}\quad(m\ge1).
\]

The first map is the row map
\[
d_1(u,v)=ua_1+va_2,
\]
and, for $m\ge2$, the maps are diagonal right-multiplication maps with entries $a_{1,m},a_{2,m}$. The augmentation is $Ae_i\twoheadrightarrow S_i$. In the graded case the generators of $P_m$ have internal degree $m$; explicitly write $P[m]_d=P_{d-m}$ if that is the chosen shift convention. Do not equate an internally shifted graded module with its unshifted version.

**Exactness proof.** The surviving paths form a basis. The two images $Aa_1,Aa_2\subset Ae_i$ have disjoint path supports, so their sum is direct and is the radical. The kernel of right multiplication by $a$ consists exactly of the surviving paths whose first arrow is (f(a)), hence is (Af(a)). Thus each kernel is the next image. Every differential is radical-valued, proving minimality. The same pathwise argument works with formal coefficients in the arrow-adic completion: the relevant subspaces are closed, and formal path coefficients still compare independently.

In particular
\[
\Omega^1 S_i=Aa_1\oplus Aa_2,\qquad
\Omega^m S_i\cong Aa_{1,m}\oplus Aa_{2,m}\quad(m\ge1).
\]

The uniserial summands are naturally projective modules for the appropriate hereditary normalization component, restricted to $A$; they are generally **not** projective over $A$. This recovers the useful content of Thm 10.1(1),(3),(4), but the augmentation and the first row map must be separated from the later diagonal maps. The paper's single diagonal display cannot literally describe the map to the single projective cover $P_0$.

The exact path argument also proves that the path-graded algebra is Koszul. With the appropriate opposite-algebra convention, the Yoneda Ext algebra of the vertex simples is the quadratic dual: its surviving paths are the forbidden chains of $A$. Thus Ext dimensions count forbidden chains with their endpoints, not arbitrary geometric intersections. One must still identify the precise surface model and grading before translating this to curves.

## 2. A decisive correction to Thm 10.1(2): the node

Take the paper's own §7 example
\[
\Lambda=k[[x,y]]/(xy),\quad \mathfrak m=(x,y),\quad S=\Lambda/\mathfrak m=k.
\]

Its minimal resolution is
\[
\cdots\xrightarrow{\operatorname{diag}(x,y)}\Lambda^2
\xrightarrow{\operatorname{diag}(y,x)}\Lambda^2
\xrightarrow{[x\ y]}\Lambda\longrightarrow k\longrightarrow0,
\]
with the two diagonal maps alternating. Exactness follows directly from
$\operatorname{ann}(x)=(y)$, $\operatorname{ann}(y)=(x)$, and $(x)\cap(y)=0$.

There are two different issues:

1. **The simple is not a periodic module.** With $t=x+y$, $\Lambda$ is free of rank two over $R=k[[t]]$. Every positive syzygy is a nonzero $R$-torsion-free module, while $k$ is $R$-torsion. Thus $\Omega^p k\not\cong k$ for every $p\ge1$. The resolution has an eventually periodic tail, not periodicity from the simple/augmentation.
2. **The lcm is not necessarily the least period of the unordered tail.** The nodal dessin has $\sigma=(1)(2),\alpha=(12),\phi=(12)$. The stated lcm is two. But
   \[
   \Omega k=(x)\oplus(y),\qquad
   \Omega^2k\cong(y)\oplus(x)\cong\Omega k.
   \]
   Its ungraded unordered syzygy tail therefore has period one. Ordered arm labels have period two. Interchanging the two summands accounts for the shorter period; the displayed alternating tail is correspondingly isomorphic to its one-step translate.

**Safe repair:** the ordered forbidden-arrow chains return after the lcm of their orbit lengths; this supplies a period of the positive-degree tail after forgetting the internal grading (or with a corresponding internal grading shift). A claim of the **least** period requires proving that no module isomorphisms, branch permutations, or other identifications shorten it. Call the simple eventually periodic, and define the category and meaning of period explicitly.

Thm 10.1 pp29–30 and Example 11.2 p37 need that distinction. The latter's visible projective labels do not themselves prove the least period of the syzygy modules. It may have the displayed ordered period; that is a different assertion.

## 3. Orders, normalization, completion, and special fiber

These are four different algebras/categories:

* $A=kQ/I$, a path-graded locally gentle algebra.
* $\widehat A$, its arrow-adic completion.
* The hereditary overorder $H=\prod_i H_i$, with $H_i\subset M_{n_i}(k[[x_i]])$.
* A central special fiber $\overline\Lambda=\Lambda/t\Lambda$, or another explicitly specified finite-dimensional quotient.

Hereditary $H_i$ has global dimension one. Its projective columns, restricted to $\Lambda$, may have infinite projective dimension. Thus its short resolutions do not replace the resolution over the glued order.

For the completed equicharacteristic case there is an explicit proof of the completion/pullback identification, which should be stated rather than treated as automatic. Send the arrows around each permitted cycle to successive matrix units, with the wrap-around arrow multiplied by $x_i$. Send a vertex idempotent to its two corresponding diagonal occurrences in $H$. Forbidden concatenations vanish and surviving positive paths have independent matrix/path coefficients. The image is exactly
\[
\{(h_i)\in\prod H_i:\text{the two diagonal residues paired by each edge agree}\}.
\]
Comparison of formal path coefficients proves injectivity and surjectivity after completion. This requires specifying the coefficient-field identifications. It is the appropriate setting for the pathwise resolution proof above.

With $t\mapsto(x_i I_{n_i})_i$, the pullback is a finite torsion-free, hence free, module over the common DVR (k[[t]]), of generic rank $\sum_i n_i^2$. Arrow-adic and $t$-adic filtrations are cofinal: sufficiently long permitted paths contain a full permitted cycle and a positive remaining path, hence are divisible by $t$. No equality of individual cycle lengths is needed.

The much broader Dedekind-domain choices in §6 require extra care. Local principal uniformizers, semiperfectness/minimal projective covers, common residue-field maps, and possible ideal-class twists cannot be silently imported from $k[[x_i]]$. Prop 6.7 is straightforward via primitive idempotents in the completed split situation; it is not a substitute for those hypotheses in all stated generality.

### Explicit special-fiber counterexample

For the node, writing $y=t-x$ gives
\[
\Lambda\cong R[x]/(x^2-tx),\qquad
\overline\Lambda\cong k[x]/(x^2).
\]
Over $\Lambda$, the simple has Betti numbers $1,2,2,2,\ldots$. Over the special fiber it has the minimal resolution
\[
\cdots\xrightarrow{x}\overline\Lambda\xrightarrow{x}\overline\Lambda
\xrightarrow{x}\overline\Lambda\to k\to0,
\]
with Betti numbers $1,1,1,\ldots$. Tensoring the order resolution with (R/(t)) does not yield an exact resolution of $k$: $\operatorname{Tor}_1^R(k,k)\cong k$ survives. Derived base change is legitimate, but ordinary base change on a non-$R$-flat simple does not preserve this resolution. Any extension to special-fiber modules must prove its own statement.

## 4. Center and classification corrections

### Lemma 9.2, pp27–28

The printed center expression includes $A_0\cdot k[[z_1,\ldots,z_r]]/(z_iz_j)_{i\ne j}$, where $A_0=kQ_0$. Literally including $A_0$ is wrong for a connected quiver with more than one vertex. For an arrow $a:i\to j$, $i\ne j$, one has $e_j a=a$ and $a e_j=0$; $e_j$ is not central. A central degree-zero element $\sum c_i e_i$ has $c_i=c_j$ along every arrow and hence is a common scalar.

In the closed case, the corrected completed center is
\[
Z(\Lambda)\cong k[[z_1,\ldots,z_r]]/(z_iz_j:i\ne j).
\]
The $z_i$ are sums of all cyclic rotations of the permitted cycle at graph vertex $i$. In the proof the termwise assertion $b\mathfrak c_k=\mathfrak c_kb$ is generally false: multiplication shifts the appropriate cyclic rotation. The **sum** commutes, by reindexing. This repairs the useful central-cycle argument without adding noncentral primitive idempotents. The polynomial version applies before completion. Ford–Oswald–Zhang Lemma 2.17 gives a carefully stated general locally gentle center theorem.

### Corollary 10.2, p31

The hereditary normalization records permitted-cycle lengths, not all three cycle types. An exact permutation example, computed independently, is
\[
\sigma=(123)(456).
\]
For $\alpha_1=(14)(25)(36)$, $\phi_1=\alpha_1\sigma^{-1}=(162435)$: there is one face and genus one. For $\alpha_2=(14)(26)(35)$, $\phi_2=(15)(24)(36)$: there are three faces and genus zero. Both graphs are connected and have the **same** normalization $H_3\times H_3$. They have different passports.

Thus classifying all orders with a fixed normalization cannot literally equal classifying constellations with a fixed full passport. Additional face data and the actual gluing are necessary. Nor does fixed normalization determine a Galois orbit: §11 p36 already explicitly distinguishes two orbits with the same center/normalization, contradicting the stronger language in the abstract if that language is interpreted as a converse.

The useful reconstruction result should retain actual labeled projective maps, their radical branches and incidence, or equivalently the quiver and quadratic relations recovered from Ext/Yoneda data. Betti numbers or period lengths alone are insufficient. For example, $k\langle x,y\rangle/(x^2,y^2)$ and (k[x,y]/(xy)) both have simple Betti numbers $1,2,2,\ldots$, but different relation maps/dessins.

### Galois action, Thm 5.4(7) and Thm 9.1

Galois preserves the passport; with uniform coefficient choices this gives invariance of the relevant abstract center/normalization types. It need not supply a canonical action by automorphisms on one fixed dessin algebra. Galois can move the dessin to a nonisomorphic dessin, and preserved dimensions only give noncanonical vector-space isomorphisms. An action on the family/groupoid and a linear representation on one chosen space are different constructions. Thm 9.1's one-way invariance can survive after the center correction; the stronger canonical-action/orbit conclusions need separate work.

## 5. Remaining mathematical sections: issues relevant to reuse

These findings do not undermine the corrected pathwise resolution, but prevent importing the paper's larger conclusions wholesale.

* **§§2.2–2.5, pp4–5:** Arbitrary modular group-algebra blocks are not Brauer graph/special biserial. For example $k[(C_2)^3]$ in characteristic two is local with $\dim\operatorname{rad}/\operatorname{rad}^2=3$, so its basic quiver has three loops and cannot be special biserial. Restrictions on defect/type are essential.
* **§3, pp11–15:** A ribbon graph determines a topological oriented embedding; the dessin/Belyi interpretation uses the corresponding bipartite map or clean subdivision. Keep these encoding choices explicit. The formula on p14 should be $\chi=2-2g$, not (2g-2); the genus-one example happens to give zero either way. The displayed permutation-product convention must be fixed throughout.
* **§5, p16:** The tensor algebra formula uses tensor powers of the arrow bimodule over $A_0$, not powers of the entire algebra $A$. This is a notation error with consequences if used literally. Definition 5.3 is a strict closed subclass of locally gentle algebras; general gentle algebras can have finite forbidden paths and terminating simple resolutions.
* **§6 and §8:** A maximal ideal is an ideal, not a chosen scalar entry in a matrix. Over a local DVR choose a uniformizer; over a general Dedekind domain use invertible-ideal modules, without pretending every ideal is principal. Several lines in §8 call semisimple quotients radicals, e.g. $\operatorname{rad}(k[[x]])=k$; literally the radical is ((x)), and the quotient is $k$.
* **§12:** P-adic digits should be chosen integer representatives $0,\ldots,p-1$, not interpreted as coefficient-field elements in characteristic zero. The adelic quotient $\mathbb A_{\mathbb Q}/\mathbb Q$ is a solenoid, not topologically the product $\widehat{\mathbb Z}\times(\mathbb R/\mathbb Z)$; the quotient identifies endpoint gluing. A set of representatives is not an isomorphism of topological groups.
* **§13.1/§13.5, pp39,43:** A finite number-field extension has transcendence degree zero over $\mathbb Q$. Its affine algebraic spectrum and projective closure do not become an algebraic curve. The curve construction in §13.1 requires a transcendence-degree-one function field, with the appropriate hypotheses on the base field for smoothness. Number fields and function fields are not interchangeable here.
* **§13.3, pp40–41:** Closed points with different residue degrees have different residue fields. The pullback of §6 requires specified isomorphisms to a common residue field; $\mathbb F_{p^a}\not\cong\mathbb F_{p^b}$ for $a\ne b$. A common scalar extension/descent construction would be an additional step.
* **§13.4, pp41–42:** Frobenius on a coordinate ring sends $f\mapsto f^p$, not merely coefficients to their $p$-th powers while fixing variables. Iteration changes a uniformizer to its (p^n)-th power, not its $n$-th power. Conjugation by the companion shift does not implement this: it fixes central scalars, whereas Frobenius sends a central local parameter $x$ to (x^p). The absolute/relative Frobenius and scalar-extension conventions also must be distinguished. The companion matrix can describe a lattice-chain shift, not automatically Frobenius.
* **§13.5, pp43–44, §14.3 p48:** $\mathbb F_{p^f}$ is not $\mathbb Z/p^f\mathbb Z$ for (f>1). The latter has characteristic (p^f) and is not a field. Inertia is not always cyclic; only the tame quotient is cyclic in general. Wild inertia can be noncyclic. Several subgroup indices are reversed. A shift with upper corner $\pi$ has $S_n(\pi)^n=\pi I$, so it is not a representation of the finite cyclic group of order $n$ in $GL_n$. Modulo $\pi$ it is not invertible. Its conjugation action/projective class is a separate matter.
* **§14.1, pp45–46:** An algebraic-group character $G\to\mathbb G_m$ is a one-dimensional multiplicative character. The trace of a general representation is an additive representation character and need not be multiplicative. These cannot be freely identified; this matters in the purported passage from torus weights to Artin characters.
* **§14.2, p46:** Trace invariants require cycles/powers with appropriate relations and dimensions. One simple-cycle trace is not generally a complete invariant ring. A single-loop quiver in dimension two already has independent trace and determinant invariants.
* **§14.3, p48:** For an Artin $L$-function over $\mathbb Q$, the unramified variable is (p^{-s}), not $N\mathfrak p^{-s}=p^{-fs}$ for a chosen prime upstairs; the Frobenius acts on inertia invariants. Extra residue-degree substitution needs a different explicitly defined base-field Euler product.

### Theorems 14.2–14.3 and Corollary 14.4

Artin induction as actually quoted in Thm 14.2 gives rational combinations of characters induced from cyclic subgroups. The proposed integral strengthening is false in that generality. For the quaternion group $Q_8$, every cyclic subgroup has even index. Every character induced from a cyclic subgroup therefore has even degree, as does every integral linear combination of them. The trivial character has degree one. This is a direct obstruction, independent of invariant-theoretic rhetoric. Brauer's integral theorem uses a different family of subgroups; it does not repair “cyclic” by renaming it.

Thm 14.3(2)'s claim about the entire representation variety being normal fails in the paper's own nodal algebra: its one-dimensional representation variety is $\operatorname{Spec}k[x,y]/(xy)$, whose node is not normal. Each irreducible component is a line and is normal; that is the materially different componentwise statement in the applicable special-biserial literature. Its dimension-one base-change group acts trivially, so this is also a warning against treating every invariant ring as an affine toric domain. Moreover, a product of projective spaces of arbitrary dimensions is not necessarily one projective line.

The actual theorem in Carroll–Chindris–Kinser–Weyman, https://arxiv.org/abs/1706.07022v3 , concerns irreducible components of moduli of semistable representations of finite-dimensional special biserial algebras, with their stated hypotheses. Neither componentwise normality nor rationality of a moduli space proves an analytic Artin holomorphy assertion. The required identification of the appropriate rings with the semigroup of functions holomorphic at a chosen complex point is an additional arithmetic-analytic theorem, absent here. Thm 14.3 and Cor 14.4 are announced without the required proof in this paper and cannot be used as established inputs to the Hilbert–Pólya construction.

## 6. Direct applications and corrections in the original Hilbert–Pólya preprint

Read-only target:
`Surface-Orders-Hilbert-Polya/emergent_cyclic_time_hilbert_polya_GRH_COMPLETED.tex`.

The new focused read covered lines 2398–2517 (resolution statements/proof), 2680–2900 (Cartan/Euler framework), and 5058–5085 (claimed surface-invariant holomorphy bridge), with a broader search for projective/resolution references. Earlier full textual coverage of this original source is separate from the present focused verification.

1. **Lines 2422–2424** repeat the exact lcm-period claim. Replace it by the precise positive-tail/ordered-chain statement above; retain maps and labels for reconstruction.
2. **Lines 2870–2889, `eq:q_euler_cartan_inverse`: a concrete sign error.** The source defines
   \[
   E_{ij}(q)=\sum_{m\ge0}(-1)^m\dim\operatorname{Ext}^m(S_i,S_j)q^m,
   \]
   but then writes $C(q)E(-q)^T=I$. It has applied the sign twice. With that definition the correct relation, subject to the chosen transpose convention, is
   \[
   C(q)E(q)^T=I.
   \]
   If instead (P(q)) denotes the **unsigned** Ext/Poincare series, write $C(q)P(-q)^T=I$. Do not combine the two conventions.

   The node checks this without any matrix-index ambiguity:
   \[
   C(q)=1+2q+2q^2+\cdots=\frac{1+q}{1-q},\quad
   E(q)=1-2q+2q^2-\cdots=\frac{1-q}{1+q}.
   \]
   Thus $C(q)E(q)=1$, whereas the printed identity gives $C(q)E(-q)=C(q)^2\ne1$.
3. **Ordinary Euler forms:** eventual periodicity does not make the infinite alternating Ext sum converge. For the node the unsigned dimensions are $1,2,2,\ldots$. Use a formal series, an explicit regularization with its own theorem, or a suitable perfect subcategory; do not substitute $q=1$ without justification.
4. **Lines 5073ff:** the asserted toric bridge imports the unproved/overstated Thm 14.3 discussed above. A resolution can define Schofield-type maps, but it does not identify their determinant with an Artin Euler factor or prove the holomorphy of the resulting global function.
5. **Self-adjointness:** a finite chain complex with a chosen positive Hermitian metric gives a positive Laplacian (dd^*+d^*d). That is a genuine construction, but its determinant depends on the complex and metric; equality with the desired arithmetic determinant must be proved. Infinite completed projectives are not automatically Hilbert spaces, and their algebraic arrow maps do not automatically have a compact-resolvent self-adjoint realization. Periodic resolution data by themselves do not supply prime weights, conductor terms, a Hilbert norm, domains, or trace-class estimates.

6. **Line 1331, checked after the root review identified it:** the DG algebra $k[\varepsilon]/(\varepsilon^2)$, $|\varepsilon|=-1$, $d\varepsilon=1$, is acyclic, not quasi-isomorphic to $k$. Every closed $z$ satisfies $z=d(\varepsilon z)$. Its unit is a boundary, so an augmentation to $k$ with its zero differential cannot be a DG-algebra map. It cannot serve as the claimed ground-field resolution. This is a separate elementary example error, not an obstruction to constructing the actual projective resolution above.

## 7. Recent primary literature and precise scope

The following is a focused literature review, not a full audit of these papers.

### Ford–Oswald–Zhang, 2026 version: the closest direct resolution reference

S. Ford, A. Oswald, J.J. Zhang, **Homological conditions on locally gentle algebras**, https://arxiv.org/abs/2409.08333v3 , revised 5 September 2026; related DOI https://doi.org/10.1016/j.jpaa.2026.108343 . Downloaded PDF SHA256 `4b71b4e12e0e02991bb2f8e50545d78535962be2446750bd27a91c12745c29c5`.

Focused reading: introduction; conventions p3; center §2.5, Lemma 2.17 pp7–8 and proof; §4.1 pp12–14, including Definition 4.2, resolution (4.3), Remark 4.4, Lemma 4.5 and proof, Example 4.6, Theorem 4.7 and proof. It supplies a clean graded right-module forbidden-path resolution and a precise homological-dimension statement. Its default characteristic is zero and it specifies its internal shift convention. This is a direct source for replacing ambiguous formulas, not a theorem about arbitrary mixed-characteristic completed orders. Its later injective-resolution/AS results were not independently audited here.

### Opper–Plamondon–Schroll, substantially revised 2025 version

**A geometric model for the derived category of gentle algebras**, https://arxiv.org/abs/1801.09659v7 , revised 10 July 2025. Downloaded PDF SHA256 `addd6fae0f373fd0508081c7617cc9d8be42afa0deedc3ebc4493bbfc4b40529`.

Focused review: abstract, introduction and conventions, theorem roadmap, and the actual statement of Theorem 3.3 and its intersection conventions. The current version distinguishes the triangulated category generated by simples, perfect objects, and objects with finite-dimensional cohomology. It treats **finite-dimensional graded gentle algebras** by default. Its Theorem 3.3 maps oriented graded intersections into a standard morphism basis. The map is bijective except for the same-closed-curve cases: equal gradings require the extra identity map; a grading shift by one requires the extra Auslander–Reiten connecting map. Section 3.1 describes a Schauder basis, so one must not silently turn every case into a finite naive intersection count. Band/local-system parameters, endpoint/puncture conventions, and category/object hypotheses must be preserved. This is not a blanket theorem that arbitrary ungraded intersection counts equal Hom/Ext for the infinite-dimensional surface order. The new v7 category scope is a reason to cite an exact version, rather than an old abstract alone.

### Li–Qiu–Zhou, geometric Koszul duality

**A geometric realization of Koszul duality for graded gentle algebras**, https://arxiv.org/abs/2403.15190v1 , 22 March 2024. Downloaded PDF SHA256 `dcf1d52a09c249fcacb69fb929be088d3e233a241f3cab7a760395d53d0c2dec`.

Focused reading: introduction and definitions roadmap, actual Lemma 3.5 and Theorems 3.6/3.9 with proofs, pp26–28. The relevant setup is **homologically smooth graded gentle algebras** with full formal arc systems and a grading/line field. In the actual body, Theorem 3.6 realizes the relevant Koszul functor/quasi-inverse via half rotation, and Theorem 3.9 gives the indexed intersection-dimension formula. The introduction's parenthetical theorem numbers are swapped; use body numbering. Those hypotheses are not automatic for closed surface orders having infinite simple resolutions. Algebraic quadratic duality survives more generally, but the stated geometric equivalence requires checking the actual category and hypotheses.

### Foundational module and locally gentle surface models

* Karin Baur and Raquel Coelho Simões, **A geometric model for the module category of a gentle algebra**, https://arxiv.org/abs/1803.05802v1 . Verified primary abstract/version; not a full proof review. Its tiling model concerns finite-dimensional gentle module categories. A curve must satisfy the appropriate permitted conditions; arbitrary curves are not all modules, and naive total intersection counts do not replace admissible-overlap morphism rules.
* Yann Palu, Vincent Pilaud, Pierre-Guy Plamondon, **Non-kissing and non-crossing complexes for locally gentle algebras**, https://arxiv.org/abs/1807.04730v2 , 13 July 2018, published 2019. Verified primary abstract/version. It gives the appropriate locally gentle surface/dissection dictionary and dual dissections. Its non-kissing complex theorem is not itself a universal Hom/Ext dimension formula.

### New resolving-subcategory papers: useful but narrower than this order problem

Benjamin Dequêne and Michaël Schoonheere:

* **Resolving subcategories for gentle algebras I: Monogeneous resolving subcategories for gentle trees**, https://arxiv.org/abs/2502.20994v3 , revised 9 September 2026.
* **Resolving subcategories for gentle algebras II: Resolving subcategories for gentle trees**, https://arxiv.org/abs/2509.10120v2 , revised 3 October 2025.

Verified primary versions/abstracts only. Their modified geometric model and resolving closures are relevant to organizing syzygy-closed subcategories; their finite-global-dimension/gentle-tree hypotheses prevent automatic application to closed surface orders with relation cycles. The second paper explicitly distinguishes the available join decomposition from a generally false semidistributivity expectation.

## 8. Concrete next research theorem

The strongest justified immediate target is a corrected, explicit **resolution–Ext–Cartan theorem** for the closed locally gentle algebra and its arrow-adic completion over a fixed coefficient field:

1. Construct the actual first row map and subsequent forbidden-arrow diagonal maps, with their left/right and grading conventions.
2. Prove exactness by independent path coefficients and minimality by radical-valued maps; prove the extension to formal paths separately.
3. Record ordered forbidden-chain periods and unordered syzygy periods separately; include the node as a required test.
4. Compute the endpoint-refined unsigned Ext series and quadratic dual, then apply exactly one sign substitution in Cartan inversion.
5. Prove the matrix pullback/completion isomorphism with a common base DVR and give a derived base-change statement that exposes the extra Tor groups at the special fiber.
6. Only after selecting the correct finite-dimensional or smooth graded surface model, identify graded intersections with the corresponding Hom spaces; do not omit local systems, endpoint rules, or grading indices.

This gives concrete algebraic input for an eventual chain/Hodge construction. The next genuinely new analytic/arithmetic obligation would be to construct a positive-metric operator whose determinant or trace is proved to equal the completed arithmetic function, with all ramified/archimedean factors and compact-uniform convergence. That bridge remains open. The present review does not establish RH or GRH.
