# Read-only mathematical audit of the complete surface-order Artin manuscript

Source: `/Users/amelieschreiber/Documents/LaTeX-projects/GRH/GRH/surface_order_monomial_artin_grh_manuscript_complete.pdf`.

The PDF has 223 physical pages. Printed Arabic page n is physical page n+21. This report gives printed page numbers first and physical page numbers in parentheses. Front matter runs through roman page xx. Extraction and three representative page renderings are under `/tmp/grh-audit-MbyRod/`. The source PDF and repository were not edited.

## Bottom-line mathematical assessment

The manuscript does **not** prove RH, GRH for monomial Artin L-functions, or GRH/holomorphy for general Artin L-functions. Its sound central result is a conditional complex-analytic criterion: a nonzero holomorphic limit of finite-dimensional determinants whose zeros are all on the critical line also has all zeros on that line. The required arithmetic determinant families and convergence are not established. Several proposed bridges are explicitly false, including an elementary prime-sum convergence claim and two group-theoretic claims. Later purported proofs repeatedly apply conditional statements without proving their hypotheses.

The principal repairs are substantive research problems, not proofreading. The manuscript can be made mathematically honest as a conditional framework and research program. An unconditional proof requires a new argument for the missing analytic determinant identity and compact convergence, with a construction preserving the arithmetic function while obtaining self-adjointness.

## Coverage and limits

I read the entire extracted text in order: front matter, all Chapters 1–24 (printed pp.1–127), all Appendices A–Y (pp.129–196), and the complete bibliography (pp.197–202). There was one truncated chunk in Chapter 13; I reread the omitted construction explicitly. I rendered and visually inspected printed pp.63, 73, and 121 (physical pp.84, 94, 142), confirming the crucial displayed prime bound, fundamental-group map, and analytic denominator were extracted accurately. This is a full-document internal mathematical audit, not a claim to have independently checked every cited paper or every bibliographic detail. Some geometric assertions below are identified as unsupported or overgeneralized rather than fully classified as false in every possible revised formulation.

## 1. Fatal analytic error in Lemma 11.3

**Location:** §11.8, printed pp.61–63 (physical pp.82–84); especially Steps 3–4 on pp.62–63. Propagated into Remark 11.5 p.63, Theorems 11.1 and 9.2, Theorem 14.2, Appendix F, and the final global corollary.

The proof bounds a tail by `sum_{p>N} p^{-sigma_*}` and claims PNT/Abel summation makes this finite and tending to zero whenever `sigma_*>1/2`. This is false. For F=Q and the trivial character, that positive series diverges for **every** `sigma_* <= 1`. PNT makes the threshold 1, not 1/2. The integral displayed on p.62 behaves like `integral_N^infinity t^{-sigma_*}/log(t) dt`, which diverges for `sigma_*<=1`.

Additional errors on p.63:

- The displayed denominator `sigma_*-1` cannot be used for a convergent integral when `sigma_*<1`.
- The asserted bound `O(N^{1/2-epsilon/2}/log N)` generally grows for small positive epsilon; the next sentence says it tends to zero.
- Step 4 infers `||T||<1` from finiteness and a zeta bound. A finite bound does not imply a bound below one. Even for sigma>1, the prime sum becomes arbitrarily large as sigma approaches 1 from above.
- The assertion `zeta(sigma_*)-1<infinity` is being used as though zeta were its positive Dirichlet series for sigma between 1/2 and 1. Analytic continuation is not a bound for that divergent positive series.
- A determinant identity for pullbacks does not itself give the claimed operator-norm bound. The actual Hilbert space, embeddings, gluing maps, and norm estimates have not been specified.

For an actual block-diagonal operator `diag(chi(p)p^{-s})`, the operator norm is a supremum and can be <1 for sigma>0. That observation does **not** repair the determinant argument: the trace-class/logarithmic determinant sum still has absolute-convergence threshold sigma>1. Hilbert–Schmidt summability at sigma>1/2 could motivate a regularized determinant, but then the missing linear trace term and its arithmetic continuation must be controlled. Changing Schatten classes is not a proof of the required limit.

**Necessary change:** withdraw Lemma 11.3 as proved; preserve only an explicitly defined right-half-plane estimate. State the genuinely missing strip convergence or regularized determinant estimate as a hypothesis/open problem.

## 2. Conditional statements are promoted to unconditional proofs

**Locations:** Theorem 11.2 pp.60–61 (physical82); Appendix F pp.141–143 (physical162–164); Theorems 23.5 and 23.8 pp.120–122 (physical141–143); “Proof of Theorem 14.1” p.124 (physical145); Corollary 23.12 pp.124–125; Chapter24 pp.126–127; Appendix C p.132; theorem inventories pp.156–158 and173–177.

Theorem 11.2 assumes, among other things, the compact-uniform convergence needed in Theorem 11.1. It isolates a sufficient package; it does not construct its inputs. The proof of Theorem 11.1 on p.143 nevertheless says finite-place construction and gluing are “supplied by Theorem 11.2.” It also calls the strip-growth estimate an “input isolated” in Theorem F.2 and then applies the theorem without proving that input.

Theorem 23.5 explicitly assumes the relevant arithmetic surface, a complete prime/geodesic matching with Frobenius traces, and the correct scalar corrections. Theorem 23.8 explicitly assumes normalization, functional equations of approximants, and growth estimates. The proof on p.124 treats their conditional conclusions as established for every Artin representation. Their hypotheses have not been verified. Thus Theorem14.1 and Corollary23.12 do not follow.

**Necessary change:** rename the package statements conditional criteria/conjectural construction targets; produce a dependency table separating proved lemmas, correct external input, and unproved hypotheses. The conclusion should be “if Packages A–D are verified, then …”. The word “assembled” must not replace verification of a hypothesis.

## 3. False use of Belyi monodromy and fundamental groups

**Locations:** Theorem13.1 p.72 (physical93); §13.3 p.73 (physical94); Theorem13.2 pp.74–75 (physical95–96); Corollary13.5 pp.75–76 (physical96–97).

### 3a. Not every finite group is Belyi monodromy

Theorem13.1 claims every finite group G occurs as the monodromy group of a Belyi map. A Belyi map has two generating permutations `sigma_0,sigma_1`; its monodromy is a quotient of the free group F2, hence is two-generated. The group `(C2)^3` is an immediate counterexample. Belyi’s theorem about curves defined over number fields does not imply the displayed assertion. A group may occur in another role (for example as a subgroup or an automorphism group) without being the monodromy group asserted here.

### 3b. The pullback map is not defined as written and is not automatically surjective

Page73 uses a map from the fundamental group of the **compact** covering curve `Sigma_G=C_G(C)` to the fundamental group of `P1 minus {0,1,infinity}` induced by beta. But beta maps some points to those punctures, so it is not a map from that compact curve into the punctured target. One must remove the preimages of the branch points first.

After that correction, the subgroup corresponding to the covering does not give the claimed monodromy surjection by restriction. For a regular G-cover its subgroup is the kernel of the monodromy map, so the restriction is **trivial**, the opposite of the asserted surjectivity. The Riemann existence theorem does not justify the claim. Moreover an arbitrary Belyi covering need not be Galois with deck group equal to its permutation monodromy group, as p.74 assumes.

### 3c. Labelling loops is insufficient for a prime-cycle trace identity

Even if a suitable independent surjection from a chosen surface group to G were constructed, choosing a preimage of each Frobenius class establishes only a tautological trace equality for those chosen words. It does not establish:

- that the preimage is primitive;
- that distinct primes correspond to distinct primitive closed classes;
- that lengths equal log of prime norms;
- that **all** primitive cycles in the transfer determinant are accounted for exactly once;
- that there are no extra cycles, repetitions, or unwanted multiplicities;
- that ramified terms and conductors have the claimed contributions.

A finite group has finitely many conjugacy classes, whereas infinitely many primes share them. A transfer trace formula sums over all relevant cycles, not merely a conveniently labelled subset. These are precisely the missing arithmetic assertions Corollary13.5 needs.

Remark13.4 p.75 also incorrectly says Belyi maps of the same degree and monodromy group give isomorphic holonomy representations; branch cycles/Nielsen data and subgroup embeddings carry additional information. Faithful Galois action on all dessins does not canonically identify a selected dessin’s geometric monodromy with the arithmetic of an arbitrary given extension.

**Necessary change:** retain the arithmetic representation as input; correctly specify a base punctured surface, its covering, and the monodromy map. Treat prime-to-cycle and length/multiplicity matching as an independent unproved theorem, not as a consequence of Belyi labelling.

## 4. Taketa, solvable groups, and automorphy are misstated

**Location:** Theorem14.2 pp.79–81 (physical100–102), with related claims pp.78,88–89,169–170,177.

Step1 says “a solvable group G is monomial: by Taketa’s theorem, every irreducible representation of a solvable group is induced from a one-dimensional representation.” This reverses Taketa’s implication: monomial groups are solvable; solvable groups need not be monomial. The proof also treats an arbitrary possibly reducible rho as one induced irreducible piece.

Step3 overstates what a tower of cyclic base changes proves about arbitrary irreducible solvable-image Artin representations. A group being solvable does not ensure an arbitrary representation descends from degree one through the prescribed tower. A precise applicable automorphic induction/descent theorem and hypotheses are required. The Langlands–Tunnell discussion omits parity and other scope distinctions; the assertion about icosahedral cases on p.81 similarly lacks the needed qualifications.

Even granting automorphy in an individual case, Step4 does not follow: analytic continuation, a functional equation, and standard automorphic growth bounds do not yield self-adjoint approximants converging to the L-function. Automorphy does not itself prove GRH. The determinant-family bound required here is independent of a bound for the target L-function.

Step5 says T is self-adjoint on the critical line and then sets `H=-i(T-1/2 I)`, declaring H self-adjoint. If T is self-adjoint, this H is skew-adjoint (unless zero). The correct requirement for H would be `T=1/2 I+iH`, which is a different spectral statement. This is not proved.

**Necessary change:** withdraw Theorem14.2 as unconditional. State only precisely sourced automorphic families and retain the determinant convergence as an independent hypothesis. Correct Taketa’s direction and handle irreducible decompositions explicitly.

## 5. Brauer induction is not integral induction from cyclic subgroups

**Locations:** §4.2 p.25 (physical46), AppendixE.1 p.136 (physical157), Chapter22 p.114 (physical135), correspondence table p.167.

The manuscript repeatedly states every character is an **integer** combination of characters induced from one-dimensional characters of **cyclic** subgroups. Counterexample: G=C2 x C2. Every cyclic subgroup has order1 or2, so the degree of every character induced from one of them is4 or2. Every integer combination has even degree. The trivial character has degree1.

The appropriate integral Brauer induction theorem uses suitable elementary subgroups; rational Artin induction from cyclic subgroups is a different assertion. Also a monomial representation is induced from a one-dimensional character of an arbitrary subgroup, not necessarily a cyclic subgroup. Chapter22’s cyclic-Hj assumption excludes elementary examples, including the trivial representation of a noncyclic group.

The correct monomial reduction itself survives: `L_K(s,Ind_H^G psi)=L_{K^H}(s,psi)` with the base fields recorded. Its right-hand side is degree one **over the larger fixed field**, not a scalar Euler factor of degree one over the original field at every rational prime. See §9.2 pp.51–52 and E.3 p.137 for language that needs this clarification.

AppendixE.4 p.137 also overstates the zero-location obstruction of quotients: a meromorphic quotient of functions with zeros only on the line has neither zeros nor poles off that line, provided the factors are holomorphic and nonvanishing there. Negative exponents obstruct holomorphy/cancellation on the line; they do not create off-line zeros out of nowhere. Functional/completion factors must of course be tracked correctly.

## 6. Self-adjointness is not arithmetic determinant preservation

**Locations:** Proposition2.7 pp.10–11 (physical31–32), Example8.1 and Proposition8.3 pp.45–47 (physical66–68), §8.9 p.43, Corollary20.6 p.104 (physical125), §§21.7 and X.1–X.4 pp.110–111,193–195.

The claim that a represented normalizing twisted shift is unitary is false without an additional unitarity hypothesis and a specified involution. For the displayed shift `S_m(eta)`, its singular values in the standard complex representation are 1,...,1,|eta|, so it is unitary exactly when |eta|=1. Merely normalizing an order does not imply that condition. A uniformizer is not a complex unit phase. The manuscript never constructs compatible *-structures and representations for the heterogeneous DVR orders. Full unitary intertwiners between local representation spaces also require equal Hilbert dimensions; ranks3 and2 in the explicit example do not have these for their defining modules.

The unitary logarithm statement, **once unitarity is actually assumed**, is fine in finite dimensions with a real-valued eigenphase choice; a family-compatible branch is an extra issue.

Corollary20.6 defines `H=(T-T*)/(2i)` after saying reversible T is self-adjoint in its weighted Hilbert space. In that Hilbert space H=0. In an unrelated standard inner product the formula is always Hermitian but has no demonstrated relation to the arithmetic determinant. AppendixX’s `H=D^{1/2}TD^{-1/2}` is instead a valid Hermitian similarity under detailed balance, but it is a **different definition** of H. Neither formula establishes equality between `det(I-T(s))` and the centered polynomial in s used in Theorem6.1.

The worked example p.43 symmetrizes qS to `(qS+(qS)*)/2`. This changes the trace and determinant. For the 3-cycle warm-up, at q=1, `det(I-S)=0`, whereas the centered determinant of `(S+S*)/2`, evaluated at s=1, is nonzero: its roots are1/2+i,1/2-i/2,1/2-i/2. Introducing a second spectral variable zeta makes a finite polynomial with line zeros but does not identify it with the original Euler factor in s. For complex s, use of T(s)* also destroys holomorphic dependence unless a different construction is specified.

**Necessary change:** choose one precise Hilbert space, involution, Hamiltonian, and regularization. Prove a determinant-preserving identity between the arithmetic transfer family and the centered self-adjoint determinant. Do not infer this identity from the fact that one can symmetrize a matrix.

## 7. A sign error reverses the Euler determinant

**Locations:** Proposition2.8 pp.11–12 (physical32–33), Proposition12.1 p.65 (physical86), Corollary13.5 p.76 (physical97). Contrast the correct reciprocal convention in Corollary7.3 pp.34–35 and AppendixJ pp.151–152.

If `w(s)=a exp(-s ell)`, then `log det(I-T)=-sum w(C)^m/m`, and therefore `d/ds log det(I-T)=+sum ell(C)w(C)^m`. The manuscript instead puts a minus derivative on the left and a positive series on the right. With one scalar prime factor, `det(I-T)=1-chi(p)p^{-s}=L_p(s)^{-1}`. Thus `d log det = -L_p'/L_p`; the displayed `-d log det = -L'/L` has the opposite sign.

Proposition12.1’s assertion that unitarity and unramifiedness make a one-dimensional overlap determinant equal1 is also false: for scalar t, `det(I-t)=1-t`; |t|=1 does not make it1. A specific zero overlap operator or another mechanism must be given, consistently with earlier nonzero overlap weights.

**Necessary change:** fix one determinant/reciprocal convention throughout before any completion argument. The correction alone does not establish self-adjoint determinant convergence.

## 8. The analytic propagation theorem has proof defects and an unusable growth hypothesis

**Locations:** Proposition23.7 pp.121–122 (physical142–143), Theorem23.8 p.122, TheoremF.2 pp.141–143 (physical162–164), Remark11.5 p.63, AppendixD.4–D.5 p.135.

The quotient `(F_N-Lambda)/(1+s^2)^m` has potential poles at s=+i and s=-i, which lie **inside** the widened strip `-delta<Re(s)<1+delta`. It is not holomorphic as asserted. Use a denominator with zeros outside the domain, such as a sufficiently left-shifted linear factor, if that approach is used.

Locally uniform convergence on a whole boundary line is not uniform convergence on the unbounded line. To use a uniform maximum estimate one needs uniform tail control; a sufficiently strong common polynomial bound plus an extra decaying denominator could supply it, but this proof does not do so. The proposition also initially defines Lambda only on the critical strip but then evaluates it outside that strip; a connected holomorphic continuation domain has to be specified.

More fundamentally, the stated **common polynomial growth bound** is incompatible with a sequence of `e^{alpha_N+beta_N s}P_N(s)` having unbounded polynomial degrees d_N. Along a vertical line, if Im(beta_N) is nonzero, one tail grows exponentially; if Im(beta_N)=0, the asymptotic growth is a nonzero constant times |t|^{d_N}. A fixed bound `C(1+|t|)^M` therefore forces d_N<=M for every N. A sequence with uniformly bounded numbers of zeros cannot converge locally to a completed L-function with infinitely many critical-strip zeros, by the same zero-counting principle used in Theorem6.1. Theorem23.8 merely says individual polynomial growth, which does not imply Proposition23.7’s uniform-in-N bound.

A corrected abstract propagation criterion can use local boundedness of the actual family on a **connected open region bridging** the strip and a right half-plane, followed by Vitali/Montel and an identity theorem. Proving that local boundedness for arithmetic approximants remains the principal missing estimate. A target function’s functional equation alone supplies neither a functional equation for F_N nor uniform bounds for F_N.

AppendixD.4–D.5 invokes an identity theorem between a limit defined only in 0<Re(s)<1 and equality only on Re(s)>1; these are disjoint domains. A common connected continuation domain or a bridge neighborhood is required.

## 9. The finite-N exact identification hypotheses are impossible for the stated determinant form

**Locations:** Theorem23.8 condition1 p.122 (physical143), TheoremF.2 condition1 p.141 (physical162), and the normalization discussion pp.59,110,141–143.

For a finite-dimensional centered determinant, `F_N(s)=e^{alpha_N+beta_N s}P_N(s)`, so `F_N'/F_N=beta_N+P_N'/P_N` is a rational function plus a constant. A nontrivial truncated Euler product has logarithmic derivative containing terms of the form `chi(p)(log p)p^{-s}/(1-chi(p)p^{-s})`, with infinitely many periodic poles. These cannot agree on a right half-plane as meromorphic functions. The truncated Euler product itself is meromorphic with infinitely many periodic poles; it cannot equal an entire exp-times-polynomial function on an open half-plane. Adding gamma factors does not cure these exact finite-N mismatches.

An exponential prefactor has constant logarithmic derivative. It cannot directly encode the nonconstant gamma logarithmic derivative or its infinite pole structure. An infinite limiting determinant can reproduce gamma-type analytic data through a separately proved regularization, but that mechanism and normalization constants have not been supplied here.

**Necessary change:** replace exact finite-N agreement by a carefully stated asymptotic identity with quantified errors and a base-point normalization; prove it for the actual centered family. One cannot simply assume away the mismatch.

## 10. The degree-one theorem is overbroad even independently of GRH

**Location:** Theorem11.1 p.57 (physical78); related arbitrary-Hecke-character statements in AppendixF.

It says “a Hecke character,” without unitarity/finite-order restrictions. A nonunitary norm twist can have `L(s,chi)=zeta_F(s+1/4)`, whose completed function has a pole at s=3/4. It cannot be a compact-uniform limit of entire determinants on the open critical strip. More generally norm twists shift the natural center. Restrict the intended Artin reduction to finite-order characters and track contragredients in functional equations.

The trivial finite-order character has poles at the endpoints s=0,1 in its standard completion. That does not obstruct holomorphy on the **open** strip, but statements that its completed function is entire are wrong. The odd exception in Theorem14.2 p.79 (“trivial character of a quadratic field”) does not capture the general issue. Pole removal with xi-type factors must be stated explicitly if an entire completed object is needed.

## 11. Local algebra: useful facts mixed with incorrect generality

**Locations:** Proposition2.5 p.9 (physical30); Theorem2.11 and Corollary2.12 pp.13–15; Proposition12.2 pp.66–69; Theorems19.4 and19.7 pp.95–98; Theorem23.1 pp.117–118 (physical138–139).

- Definition2.3 gives maps **from** an overlap ring into the local centers; the fiber product in Proposition2.5 requires maps **to** the overlap ring. The proof moves between a ring pullback and a tensor-product formula for an affine scheme fiber product; those formulas express different variance and are not “equivalent” without a precise diagram. Under surjective quotient maps, center pullback statements can be proved, but those hypotheses must be supplied.
- The hereditary-order classification should be stated under the precise local-field/residue-field hypotheses of its source. A claim about finite unramified splitting over an arbitrary complete DVR needs justification beyond the local-field case. Corollary2.12’s unit-jump cyclic order is one special type; it does not make arbitrary hereditary-order types equivalent without loss of generality.
- Proposition12.2 identifies a cyclic hereditary DVR order with a cyclic quiver whose length-two compositions are zero. In the chain order, these products are not zero; a full cycle gives a uniformizer-type central element. A quotient may have relations, but it is a different algebra and must be specified. For valence1, the hereditary order R still has its uniformizer structure; the claim “no arrows” does not replace a definition of the completed order. Gentle local charts do not by themselves establish that arbitrary gluing is globally gentle/special biserial or that every cited invariant theorem applies to the resulting algebra.
- Theorem19.4 claims that for **any finite-dimensional algebra A**, the quotient near a semisimple representation is étale equivalent to a representation space of an ordinary local quiver, with no relations. This ignores obstructions/relations. Counterexample: A=C[epsilon]/(epsilon^2), dimension1 representation, simple M. The representation variety has x^2=0 (reduced underlying point), while Ext^1(M,M) has dimension1 and the ordinary one-loop local quiver has representation space A1. These are not étale locally equivalent. Local quivers with relations or stronger smooth/hereditary hypotheses are needed. Luna slices give slices, not unrestricted deletion of relations. Semi-invariants also live in character-weighted data and do not automatically descend as regular functions on an affine invariant quotient.
- Theorem23.1 takes the companion matrix **of P_v(T)=det(I-TA)** and asserts `det(I-TC_v)=P_v(T)`. A standard companion matrix has characteristic polynomial P_v after monic normalization; here one needs the reversed polynomial `t^r P_v(1/t)`. Rank1 with A=i gives P_v=1-iT; the companion of its monic normalization is [-i], yielding 1+iT, not 1-iT.
- The same theorem wants X in `End_{A_v}(M_v)` but exhibits a generic matrix in `M_r(O_v)` without specifying a module for which that matrix is A_v-linear. On the natural left module O_v^r for A_v=M_r(O_v), the commuting endomorphisms are scalars. A simple valid local realization is A_v=O_v, M_v=O_v^r, X the integral Frobenius matrix, or a correctly formulated Morita construction with determinant conventions. The local polynomial identity is elementary; its stated module construction is incomplete.

## 12. Exact descent must be proved; arbitrary overlaps cannot be chosen freely

**Locations:** Theorem20.3 p.102 (physical123), Theorem23.3 pp.118–119 (physical139–140), explicit models pp.108–112.

Theorem20.3 is a valid finite-dimensional determinant identity **assuming** its augmented Cech complex is acyclic in positive degrees. Theorem23.3 purports to obtain the needed determinant descent from pairwise surjectivity and cocycle compatibility alone. Those do not imply global acyclicity. For a triangle-shaped cover with no triple overlap, put C on each vertex and each edge with identity restriction maps and scalar operator t. The difference map C^3 -> C^3 has rank2, so H^1=C. The global equalizer is C. The naive alternating chart/edge determinant product is1, whereas its global determinant is1-ut. The missing H^1 term is essential.

Likewise the two-chart formulas cannot be used to manufacture an arbitrary conductor/ramified polynomial on the overlap. Exactness and intertwining force the overlap characteristic polynomial to divide that of the direct sum. In a one-dimensional local chart an arbitrary unrelated overlap eigenvalue is not an allowed quotient. The examples on pp.109–110 write down desired factors without constructing compatible quotient maps realizing them. Finite determinant descent identities do not establish convergence or exactness for the countably infinite family of arithmetic places.

## 13. Geodesics, curves, and graph closures need narrower statements

**Locations:** Chapter12 p.64; Theorem23.5 and Remark23.6 p.120; AppendicesU,V,W pp.182–192.

- Classical modular primitive closed geodesics are not simply rational primes of length log p. Hyperbolic modular eigenvalues are quadratic units. If e^ell=p for a prime, an integral trace would be `(p+1)/sqrt(p)`, impossible. Selberg products also carry the extra product over nonnegative integers, not just one factor per prime. Invoking Selberg/Eichler–Shimura does not prove the asserted ordinary GL1 Euler-product matching.
- CorollaryV.2 p.186 says every relevant nontrivial class on a complete finite-area punctured hyperbolic surface has a closed geodesic representative. Peripheral/parabolic classes about cusps do not; face loops are exactly a class requiring scrutiny. Contractible classes also have no nonconstant geodesic. Low-complexity surfaces may not support the stated hyperbolic metric at all. Band/string curve classifications also include grading/local-system data and should not be identified with all determinant face cycles without a map.
- PropositionW.2 appropriately describes a **formal** resemblance to Selberg and Weil. Its comparison does not imply the arithmetic determinant identity, as its own text admits. The inventories should retain that limited status.
- CorollaryW.5 p.191 claims canonical graph-C*, Leavitt-path and von Neumann completions with faithful trace packages for all local charts. A graph encoding alone does not produce those compatible functors. Graph C*-algebras can have no faithful traces (a vertex with two loops gives the standard obstruction), so a theorem relating traces when they exist cannot prove existence here. Conditions on graphs, ideals, and actual representations are needed.

## 14. Sound material to preserve

- The finite-dimensional companion characteristic polynomial in Proposition2.13 is correct for the displayed matrix.
- Pullback short exact sequence and compatible determinant multiplicativity in Lemma2.15/Proposition2.16 are correct, interpreting quotient formulas away from zeros or as a cross-multiplied polynomial identity.
- Lemma7.1, trace-as-closed-walk counts, and the reciprocal primitive-cycle product in §7.5–7.6 are standard correct finite-dimensional facts under their convergence assumptions.
- The 3-cycle example and permutation/genus computation for the theta-graph torus are correct elementary calculations. The later choice of a plain oriented6-cycle is a substituted model, not a proved medial-quiver equivalence of the original dessin.
- The monomial induction reduction is valid with correct subgroup/base-field formulations, independently of the invalid claimed rank-one GRH theorem.
- Conjugacy invariance, block-triangular determinant factorization, closed determinantal rank loci, and the elementary exact-complex determinant identities are correct in their stated finite-dimensional situations.
- Detailed-balance Hermitian similarity (Proposition20.5 and PropositionX.1) and restriction of a Hermitian operator to an invariant finite-dimensional subspace (Proposition21.7) are correct. Their arithmetic relevance needs a separate identity.
- Theorem6.1 is the right short conditional closure statement after adding `Lambda not identically zero`. Without this, a vanishing sequence such as `e^{-N}(s-1/2)` gives the identically zero limit, for which the zero-location assertion has no intended meaning. Its proof should cite Rouche/argument-principle zero counts or the corresponding strengthened Hurwitz statement explicitly. AppendixD already includes the nonzero-limit condition.

## 15. Concrete revision and research plan

1. **Correct theorem status first.** Present the work as a conditional surface-order Hilbert–Polya program. Withdraw unconditional Theorems9.2,11.1,14.1,14.2,C.1 and Corollary23.12 until hypotheses are verified. Preserve a correctly stated abstract conditional theorem.
2. **Choose the smallest actual arithmetic case.** For example fix the primitive finite-order character chi_-4, and define all finite spaces, graph maps, operators, inner products, and normalizations explicitly. Record the trivial-character xi normalization separately.
3. **Separate three analytic objects.** Distinguish the reciprocal Euler transfer determinant, the regularized completed determinant, and the centered self-adjoint spectral determinant. Prove an identity relating them rather than switching notation from one to another.
4. **Repair local statements.** Use correct Brauer induction, arbitrary inducing subgroups, corrected companion polynomials and A-linear modules, and local quivers with relations where required. Prove actual acyclicity and compatible quotient maps for any asserted gluing.
5. **Address prime/cycle multiplicities directly.** Produce a full bijection or an explicit trace identity including lengths, repetitions, extra cycles, ramified and archimedean terms. Labelling selected loops is not enough.
6. **Prove the missing analytic estimate.** Work first on Re(s)>1, then specify a legitimate regularization and a connected-domain normal-family/remainder criterion. Replace the false prime-tail bound. If the critical-strip convergence cannot be proved, leave it as the named central conjecture.
7. **Only then extend the arithmetic scope.** A validated rank-one construction can be transported through correct induction identities. Globally automorphic comparison cases need an additional explicit determinant theorem; automorphy itself must not be called a GRH theorem.

None of these recommendations supplies a proof of the unresolved RH/GRH assertions. They identify what can be rigorously retained, what must be corrected, and the exact new mathematics needed for an unconditional claim.
