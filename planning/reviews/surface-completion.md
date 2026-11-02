# Surface-order completion and downstream hardware audit

Source: `/Users/amelieschreiber/Documents/LaTeX-projects/GRH/Surface-Orders-Hilbert-Polya/emergent_cyclic_time_hilbert_polya_GRH_COMPLETED.tex`.

## Scope and disposition

I read **every source line 10000–15376, inclusive (5377 lines)**. Bounded read ranges were 10000–10399, 10400–10799, 10800–11199, 11200–11599, 11600–11954, 11955–12204, 12205–12420, 12421–12700, 12701–12899, 12900–13399, 13400–13899, 13900–14399, 14400–14899, and 14900–15376. The requested completion block 11955–12420 was inspected especially closely. I did not read lines before 10000 in this assignment. No original source was modified. No MCP, installation, authentication, publication, or model/experiment execution was used. This generated report is the only file I wrote, at the parent's explicit request.

**Conclusion:** the claimed unconditional Dirichlet GRH, monomial Artin GRH, and Dedekind-zeta GRH proofs do not follow. Several of their essential intermediate propositions are explicitly false. This is more than an omitted estimate. In particular, the required equality between modular geodesic lengths and prime logarithms is impossible in the stated setting. The later hardware realization contains separate exact finite-dimensional counterexamples.

This is a source-grounded mathematical audit. References cited by the manuscript have not independently been fetched or bibliographically authenticated in this subtask. Assertions below with explicit computations/counterexamples do not depend on trusting those references. Experimental biology/software benchmark claims are distinguished from internally refutable mathematics.

## 1. What survives as a valid conditional implication

1. **Hilbert–Pólya implies GRH once the spectral correspondence is assumed.** Definition 10648–10657 and theorem/proof 10659–10668 are valid but encode the desired zero location in the definition. The caveat at 10670 correctly identifies the real obligation.
2. **Finite self-adjoint characteristic determinants have critical-line zeros.** Lemma 11138–11152 is correct: real eigenvalues of H give zeros 1/2+iλ. This gives no arithmetic identification by itself.
3. **Hurwitz closure under locally uniform holomorphic convergence is correct.** Theorem 11160–11179 and argument-principle discussion 11194–11225 are sound for a nonzero target. This theorem cannot supply the convergence hypothesis.
4. **Trace-norm continuity of Fredholm determinants is correct.** Theorem and standard estimate 11508–11533 are appropriate. They require actual locally uniform trace-norm convergence of specified holomorphic trace-class families.
5. **The determinantal closure theorem 11540–11571 is conditionally valid.** Its assumptions (c)–(d) expressly demand the determinant identity and trace-norm limit identifying the target L-function. They are substantive hypotheses, not consequences of total positivity.
6. **Weierstrass principle 11909–11921 is valid** because its matching open set lies inside the same connected domain. The later applications fail to establish precisely this overlap.
7. **Reversible strictly totally positive real matrices give self-adjoint logarithms.** Proposition 10898–10943 is valid under its explicit hypotheses. Detailed balance makes the diagonal similarity symmetric; strict total positivity gives positive principal minors, hence positive definiteness. Neither hypothesis has been proved for arbitrary arithmetic twists or for the later claimed matrices.
8. Newton identities/log-det identities 11729–11770 are ordinary sound algebraic identities over a Q-algebra. Being able to express Euler factors as polynomials in traces does not identify unrelated traces or control an infinite analytic limit.

Family-uniform convergence is useful for quantitative family estimates, but is not logically necessary to infer GRH separately for every member once locally uniform convergence is proved for each member. The manuscript repeatedly treats this useful strengthening as necessary for the universal quantifier.

## 2. Fatal arithmetic-geometric falsehood: geodesics are not primes

### F1. Proposition `prime_geodesic_correspondence`, especially line 12080, is false

The asymptotic prime geodesic theorem at 12073–12078 is an analogy with the prime number theorem. It does **not** imply the next assertion that every unramified p has a modular closed geodesic of length log p or k log p.

Here is an exact obstruction covering all p and k. For a hyperbolic γ in SL2(Z), choose its positive expanding eigenvalue u>1 after changing the sign of γ if needed. Then

- t=u+u^{-1}=|tr γ| is an integer at least 3;
- u is a quadratic algebraic unit, with conjugate u^{-1};
- the geodesic norm is N(γ)=u² and its conjugate is N(γ)^{-1}.

If N(γ)=p^k were rational, conjugation would fix it, forcing p^k=p^{-k}, impossible for p>1,k≥1. Equivalently, length log 2 would require integer trace sqrt(2)+1/sqrt(2)=3/sqrt(2), already impossible on Y0(1). The matrix [[2,1],[1,1]] has trace 3, norm (7+3sqrt(5))/2≈6.854101966 and length≈1.924847300, not the log of an integer prime power.

All Γ0(q) elements are integral matrices, so passing to a congruence subgroup cannot fix this obstruction. The norm convention is explicitly given at 12065–12069, so this is not a convention dispute.

Consequences: the objects γ_{p,k} in 12093 do not exist with the stated length property; the equality of exponential factors at 12238 is false; the proposed remainder cannot repair a sparse exceptional mismatch, because **none** of these exact integer-prime-power norms occurs.

### F2. `eichler_shimura_weights` (12090–12118) is not Eichler–Shimura

Lines 12109–12117 assert, without an actual correspondence, that geometric monodromy around a closed geodesic is Frobenius at a rational prime. The familiar Hecke/Frobenius relations concern arithmetic correspondences and suitable cohomology/Galois representations. They do not identify primitive hyperbolic conjugacy classes with rational primes, do not give their lengths log p, and do not identify arbitrary Artin representations with such geodesic holonomies.

Hecke correspondences at p use determinant-p double cosets, whereas Γ0(q) here consists of determinant-one matrices. Conflating these is a substantive category error. The d-entry congruence claimed at 12109 is not supplied by the mass formula or a proof in the source.

The same false identification is already asserted at 11014–11015, 11099–11100, and 11084. Reduction modulo q maps infinitely many geodesic classes into finitely many matrix conjugacy classes; for Γ(q), all elements even reduce to the identity. It cannot give the claimed bijection or length identification.

Jacquet–Langlands and the cited symmetric-power lifts are not general automorphy or GRH theorems for all higher-dimensional Artin representations. Lines 12117 and 12355–12358 materially overstate these correspondences.

### F3. The initial arithmetic local data are not constructed

At 12003–12007 a finite collection of dessin vertices is assigned Z_p “for the corresponding prime p,” but no such prime assignment is defined; finitely many complex geometric vertices do not come with all rational primes attached. A completed complex local ring of a modular curve is also not a p-adic DVR without an arithmetic model and a chosen prime/place. The holonomy/Frobenius statement at 12023–12024 is an additional assertion, not a consequence of defining χ(d).

## 3. Conditions (a) and (b) are not verified

### F4. Odd primitive characters do not define this weight-zero scalar twist

At 12013–12027 χ is arbitrary primitive, and ρ_χ(γ)=χ(d) is used as a flat scalar local system on Γ0(q)\H. But -I acts trivially on H. For odd χ, ρ_χ(-I)=χ(-1)=-1. A scalar automorphic section would obey f(z)=-f(z), hence vanish identically. The representation does not descend to the stated PSL2 quotient. The primitive character modulo 3 is an immediate counterexample. One can consider different weights/bundles, but that requires a different construction, not the claimed scalar Laplacian.

### F5. Valence and Belyi regularity do not give a totally positive arithmetic transfer

The proof at 12139–12144 only applies LGV after assuming an appropriate layered planar positive network exists. Valences dividing 3 and 2 do not construct that network on the exponentially larger microstate space or guarantee all required disjoint paths. “Maximal ramification at generic points” does not prove strict positivity of every minor. Perturbing entries may change the required arithmetic trace data, and no control of this change is provided.

Moreover, χ(p) may be -1 or nonreal. At complex s the factors exp(-sℓ) are nonreal. Strict total positivity is a condition on real matrices; it cannot hold for a nonconstant holomorphic matrix family throughout a complex domain while all its entries remain positive real. A holomorphic real-valued entry on an open complex domain is constant. The source needs distinct analytic transfer families and fixed self-adjoint approximants, with an actual bridge between them.

### F6. The Fricke involution is holomorphic and orientation preserving

Lines 12153–12159 call w_q(z)=-1/(qz) orientation reversing and infer a source/sink path reflection and detailed balance. This map is holomorphic on H, with derivative 1/(qz²), and preserves complex orientation. It is not a time-reversal reflection. Being a normalizer does not prove that it sends every geodesic to its inverse or preserves a positive weighted network. The asserted detailed-balance measure is also not specified as the finite-state vector π required by 10904–10912.

Doubling a complex twist (12162) may produce a real representation, but does not produce an entrywise positive, let alone totally positive, real matrix. For a negative real scalar -1, doubling still gives negative scalar blocks. For a nonreal phase, realification gives a rotation with signed entries.

### F7. Total nonnegativity is silently promoted to strict positivity

The corollary at 11339–11354 concludes symmetric *totally positive* and takes a finite logarithm from hypotheses that in general only give TN. A symmetric positive-entry TN matrix can be singular, e.g. [[1,1],[1,1]], whose logarithm has a zero-eigenvalue obstruction. The no-bottleneck strictness hypothesis must actually be imposed and proved; it does not follow from LGV alone.

## 4. Condition (c) has a false normalization claim and no dynamical content

At 12180 set B=1/2 I+iH and A(s)=I-(sI-B)/C, C>0. Its eigenvalues are 1+(1/2-s+iλ)/C. At s=1/4 their real parts are 1+1/(4C)>1, so ||A(s)||>1 for every C. At a zero s=1/2+iλ, A(s) has eigenvalue 1. Thus the claimed choice ||A(s)||<1 “on compact subsets” is impossible even on singleton compact sets.

The determinant identity after rescaling is otherwise a trivial way to represent any finite characteristic polynomial as det(I-A(s)). It does not connect A to the original transfer T. In the claimed condition-(d) proof the trace expansion is for T (12219), then the identity suddenly concerns A (12242), with no established relation. An affine repackaging of a characteristic polynomial is not a cycle-weight transfer identity.

## 5. Condition (d), lines 12194–12300, fails independently at several steps

### F8. Determinant versus reciprocal Euler product has the wrong sign

At 12219, log det(I-T)=-Σ Tr(T^k)/k. At 12235, log L_N=+Σ χ(p)^k p^{-ks}/k. Identical prime-cycle trace weights give det(I-T)=L_N^{-1}, not L_N. The code itself correctly states this at 12529–12530. No vanishing remainder can reverse this sign. Nor is the subsequently substituted A identified with T.

### F9. A linear exponential cannot by itself reproduce gamma factors

Lines 12251–12255 say exp(α_N+β_N s) absorbs/approximates the conductor and gamma factors. The conductor part is linear exponential, but Γ((s+a)/2) is not. A locally uniform nonzero limit of exp(α_N+β_N s), if it exists on a domain, has constant logarithmic derivative; gamma has nonconstant logarithmic derivative. No regularization construction replacing this statement is given. This observation addresses the claimed standalone prefactor approximation, not a claim that gamma factors can never enter more elaborate determinant constructions.

### F10. Convergence on two outside half-planes does not establish convergence inside

At 12261–12282 an approximate functional equation for finite Λ_N is asserted from Fricke symmetry without a formula or uniform error bound. The target's functional equation cannot be transferred to arbitrary finite approximants.

Phragmén–Lindelöf needs suitable **uniform in N** growth/boundary estimates, which are not provided. The polynomial degree d_N increases; exp(β_N s) may itself grow exponentially vertically. Stirling bounds for the target do not bound these unrelated approximants. Local convergence at fixed boundary points does not give the global supremum needed to pass to the limit.

The proposed g_N(s)=(Λ_N(s)-Λ(s))/(1+|s|²)^M (12275) is not holomorphic because of |s|², so the maximum modulus principle cannot be applied to it. For q=1 the wider strip -δ≤Re(s)≤1+δ additionally contains the completed zeta function's poles at 0 and 1; the claimed difference is not holomorphic there unless poles are explicitly cleared.

### F11. The remainder estimate is asserted, not proved, and its premises are false

At 12285–12297 the prime geodesic theorem is used to bound “non-prime geodesics” by O(N^{1/2}/log N). That theorem distinguishes primitive geodesics from their iterated powers; it does not distinguish rational-prime geodesics from all others. Here the asserted rational-prime geodesics do not exist at all (F1). Group-word factorization is not arithmetic factorization.

The global injectivity radius of Y0(q) is zero because of cusps, contrary to 12291. Increasing a closed-walk cutoff N does not refine a fixed dessin's geometric mesh. No approximation map, metric error, summable test norm, or bound proving C(K,q)N^{-η} is supplied. Exponential mixing does not magically establish such a bound for an unspecified discretization.

**Result:** theorem 12194–12300 is not proved. Therefore 12307–12324 (unconditional Dirichlet GRH) and the repeated “complete self-contained proof” 12367–12417 fail. The actual final Hurwitz step remains valid, but has no verified arithmetic convergence input.

## 6. Additional Artin and analytic issues

1. **Disjoint “overlap.”** In theorem 11574–11604 the limit F is constructed only on 0<Re(s)<1, while matching is demanded on U⊂{Re(s)>1}. These are disjoint; no connected holomorphy/convergence domain linking them is supplied. The identity theorem at 11600 cannot be applied. Corollary 11923–11939 repeats this mistake. If hypothesis (iv) were expressly strengthened to analytic continuation of F on a connected domain joining these regions, the conclusion would be conditional on that added hypothesis.
2. **Monomial induction is not reduction to Dirichlet GRH over Q.** Lines 12328–12336 need GRH for Hecke characters over arbitrary number fields. Artin induction identifies an induced one-dimensional character's L-function with a Hecke L-function over the intermediate field. This is not established by the claimed Q-Dirichlet theorem. “Identical argument on Hilbert modular surfaces” is neither supplied nor fixed by Jacquet–Langlands.
3. **Dedekind induction notation is wrong.** At 12345, for a general K/Q the group Gal(K/Q) need not have the claimed meaning, and induction has been written in an impossible direction. Correctly take a Galois closure L/Q, G=Gal(L/Q), H=Gal(L/K), and Ind_H^G 1. This correct formal identity does not prove its GRH.
4. **Functional-equation symmetry is misstated.** At 10675 the map s↦1-overline(s) is said to induce λ↦-λ on s=1/2+iλ. In fact it fixes every point of the critical line. The map s↦1-s reverses λ and typically relates the dual/conjugate twist. For a complex character one cannot impose within-twist ± pairing without justification.
5. **Gibbs/modular boundedness obstruction.** A faithful trace-one density operator has K=-logρ≥0. An affine rescaling with finite scalar shift is bounded on one side. A signed unbounded chiral spectrum cannot be such a normalized Gibbs generator. In infinite dimension, if H were bounded both below and above, exp(-βH) would not be trace class. The temporary bounded-below assumption at 10709 is explicit, but the later chiral identification cannot simply be declared automatic (10953–10958).
6. **Pole clearing only covers specified families.** At 11232–11235 m∈{0,1} does not cover arbitrary reducible Artin representations: 1⊕1 gives ζ(s)² with double boundary poles. Pole-clearing does not establish unproved Artin holomorphy inside the strip.
7. **Incorrect explicit formula.** Proposition 10816–10850 permits meromorphic test F without including its own residues, and discards the shifted vertical integral. Returning it by the functional equation produces another arithmetic contribution (the dual/transformed prime sum), not only archimedean/pole terms. The displayed one-sided formula is not justified for general F as stated.
8. **Incorrect heat Selberg formula.** Equation 10977 omits the identity contribution and all repetitions and uses exp(-t λ_γ), with no λ_γ defined by a geodesic. The heat orbital weights involve Gaussian exp(-(kℓ)²/(4t)) and the usual length/denominator factors, not an invented geodesic Laplace eigenvalue. The later more recognizable trace formula 12035–12047 still needs correct test hypotheses, exceptional spectral parameters, and cusp/scattering terms.
9. **L versus completed Λ derivative.** Equation 11001 writes the prime series as -Λ'/Λ but omits conductor and archimedean logarithmic derivatives. Those belong even away from ramification. It is the logarithmic derivative of L that has the bare prime series.

## 7. Positive semigroup transfer construction is false as written

At 11451–11471 the shifts S_γ on ℓ²(Γ) are declared finite rank after truncating the set of shifts, positive after symmetrization, and supplied with coefficients c_γ(ϖ)≥0 encoding Frobenius traces. All three assertions fail in elementary examples:

- Γ=N, γ=1 gives the unilateral shift S e_n=e_{n+1}, of infinite rank. A finite sum of shifts on this infinite Hilbert space need not be finite rank or compact. A compression to a finite skeleton would need an explicit projection and error control.
- (S+S*)/2 has quadratic form -1/2 on (e_0-e_1)/sqrt(2). Nonnegative matrix entries do not mean operator positivity. It also has trace-class problems, and the original shift has zero diagonal, so the proposed trace normalization can be undefined.
- The primitive real Dirichlet character modulo 5 has χ(2)=-1; complex characters have nonreal values. Toric degeneration cannot make their exact Frobenius traces nonnegative without changing them.

Furthermore, normalized positive density operators with the source's definition of “weak-*” convergence against **every bounded operator** (11489–11495) and a density-operator limit in fact already enjoy trace-norm convergence by finite-rank tightness/positivity. The nomenclature is wrong: T1 is the predual of B(H), while its weak-* duality is with K(H); pairing with all B(H) is its weak topology. More importantly, no such convergence to a normal trace-one limit is proved for the proposed construction. The genuine problem includes possible escape of mass.

## 8. Invariant theory does not supply the claimed pole restriction

At 11874–11882 rationality of an invariant field with a determinantal transcendence basis is used to conclude arbitrary rational invariants can have poles only on finitely many fixed determinant divisors/coordinate hyperplanes. This is false: k(t) is purely transcendental with coordinate t, but 1/(t-a) has a pole at every freely chosen a. A product of projective spaces is toric, but arbitrary divisors or rational functions are not restricted to its toric boundary. Knowing generators expresses denominators algebraically; it does not prove their vanishing loci are only a fixed collection of boundaries or prove analytic pole cancellation.

This does not refute the cited rationality theorems. It refutes the stronger pole-geometry/holomorphy consequence claimed in this manuscript.

## 9. The persistence toy calculation is topologically inconsistent

At 10213–10225 attaching the unique torus face is said to lower H1 from Z² to Z. A torus face attaches along the commutator aba^{-1}b^{-1}, whose cellular H1 boundary is zero. The closed torus still has H1=Z² and gains H2=Z. Hence the rank drop and presentation at 10311–10342 are not the homology of the stated torus.

At 10198–10205 the criterion v(χ)≥κ removes the face when κ increases, contrary to the claimed increasing bifiltration and the later discretization 10303. A 2-cell cannot be included before its boundary edges without violating the subcomplex condition. Connectedness of the graph is not the threshold for all its cycles to be present. Also, shortest-path distance between endpoints can be smaller than the direct edge length, so the equivalence at 10197 fails. The entropy-derived lengths require I≤I0 to avoid negative edges; without that condition an undirected negative edge can make shortest-path infima unbounded below.

## 10. Reference Python is not a numerical verification of the proof

I inspected every code line 12429–12838 but did not execute its dependencies or main routine.

1. `_primitive_characters` (12457–12484) returns a principal character (imprimitive for q>1) and at most one quadratic candidate, not all primitive characters. `mpmath.jacobi(k,q)` is not a justified Jacobi-symbol API; its actual installed-version interface needs checking rather than trusting the claimed “tested” statement.
2. The transfer is explicitly diagonal χ(p)p^{-s} (12529–12538), not a strictly totally positive network; negative/nonreal values are normal arithmetic data.
3. The routine called `symmetrise_transfer` does not implement its documented Hermitian part or modular logarithm. It simply sets eigenvalues to -arg(T_jj), in [-π,π] (12556–12570).
4. At the actual diagnostic call s=0.5 (12701–12702), for q=1 every diagonal entry is positive real. Therefore **H_N=0 exactly and F_N(s)=(s-1/2)^{d_N}**. It cannot approximate any nonzero zeta ordinates. This follows exactly from the code, without numerical error or installing any package.
5. `hp_approximant_normalized` (12589–12623) ignores its eigenvalues and returns gamma/conductor times a reciprocal finite Euler product. It is a different, generally meromorphic function, not the stated HP determinant.
6. The nonprincipal “zero finder” (12644–12663) merely samples a truncated 199-term Dirichlet sum at t=1,1.5,... and reports s0 when |sum|<0.1. It does not run Newton refinement or an argument principle; reported values are not certified zeros and may duplicate a root neighborhood.
7. Leading principal minors (12728–12737) are not a test of all minors. The critical-line test is guaranteed by building each reported number as 0.5+i times a real number and excludes zero eigenvalues, making q=1 vacuous.
8. `persistence_diagnostic` computes a parameter grid of these same tautological checks. It defines no persistence module, maps, or homology invariant.
9. “Numerical agreement” at 12847 is not established by the code and is contradicted by the q=1 calculation. The claim at 13718–13720 that 20 primes locate 14 zeta zeros to 0.01 is impossible for this diagnostic.

## 11. Downstream finite hardware theorem is independently false

### H1. Nonunitary complex-time gates and constant vacuum overlap

At 13664 let A=(XX+YY)/2, Hermitian with eigenvalues ±1 on the one-excitation space, and c=p^{-s}. Then U_p(s)=exp(-i c A) is unitary only when c is real (up to degenerate exceptional cases), not for all complex s. For example choose s=1/2+iπ/(2 log p), giving c=-i p^{-1/2}; then U=exp(-p^{-1/2}A), with positive eigenvalues exp(±p^{-1/2}) of unequal modulus. This directly disproves part (a), line 13691, of theorem 13682–13711.

More decisively, A|00>=0. Every stated U_p therefore leaves |0...0> unchanged, even at complex s. U_φ only multiplies this vector by exp(-i Σφ_p/2). Thus the displayed “state-overlap matrix” M(s)=<0...0|U_HP(s)|0...0> is a **scalar constant independent of s**, equal to 1 for trivial χ. It cannot have the claimed determinant, Euler-product, or L-function zeros. This refutes part (b) without any experimental assumptions.

A holomorphic unitary-valued matrix family on a connected complex domain is necessarily constant. Complex s cannot be encoded as arbitrary nonreal pulse durations/angles while retaining deterministic unitary gates; a dilation/block encoding/measurement construction would be a different, explicitly normalized scheme.

### H2. Different and incompatible transfer definitions

At 13639 the transfer becomes χ(p)^{1/2}p^{-(s-1/2)}, unlike the earlier χ(p)p^{-s}. H=(T-T*)/(2i) at 13643 differs from both -log S and the Python -arg(T) prescription. There is no proof these spectra or determinants agree.

At 13656–13658 a finite product Π(1-χ(p)p^{-s}) is called a degree-N polynomial in s whose zeros approximate L zeros. It is an exponential polynomial; for unramified |χ(p)|=1 every individual zero satisfies Re(s)=0, not 1/2. Its reciprocal is the partial L Euler product and has poles, not these zeros. No critical-strip local-uniform convergence follows.

The later arithmetic claims at 13744–13756, 13793, 13804–13809, 14675–14690, and 14705–14724 all inherit the already false geodesic/Frobenius matching and convergence statements.

### H3. Wrong exchange-gate identities and numerical units

The displayed Heisenberg matrix 13526–13539 correctly gives sqrt(SWAP), up to a global phase, at Jt=π/2. The next equation 13544–13545 falsely calls that gate iSWAP: its one-excitation diagonal entries are 1/sqrt(2), whereas iSWAP's are zero. Isotropic Heisenberg coupling is not pure XY coupling. iSWAP is not locally equivalent to a single CNOT, though either entangling gate plus arbitrary one-qubit gates is universal. The explicitly claimed CNOT synthesis needs direct matrix verification after gate definitions are repaired.

At 13561–13565 the units are inconsistent: 2 cm^{-1} corresponds to frequency ≈6×10^{10} Hz and angular frequency ≈3.77×10^{11} s^{-1}. Even using the text's 6×10^{10} s^{-1}, π/(2J)≈2.6×10^{-11} s=0.026 ns, not 26 ns. The discrepancy is at least a factor 1000, plus 2π/convention factors.

At 13390–13397, J0=25 cm^{-1}, κ=1 Å^{-1}, r=20 Å gives J≈25e^{-20}≈5.15×10^{-8} cm^{-1}, not 1–5 cm^{-1}. This directly invalidates the distance-to-gate-time estimate independent of any literature question.

The stated weak-field Gd S=7/2 model (13046–13050) does not have m=±1/2 as its two lowest Zeeman states for positive gB and weak crystal field; those are the central transition, whereas the lowest states are m=-7/2,-5/2 under the displayed sign convention. A usable central-transition encoding requires a revised selection/initialization/leakage model.

The pure T2-based fidelity lower bound 13130–13136 is not justified: a coherence time alone does not bound calibration, leakage, control, or SPAM errors. Observing Rabi cycles does not certify a fixed number of high-fidelity gates.

## 12. Dessin and hyperbolic-code mathematics contain further exact errors

### H4. Graphs, passports, and Galois actions are conflated

- At 13606–13617 an arbitrary planar graph need not be bipartite; subdividing its edges gives a *different* underlying graph that can be a dessin. Steinitz concerns convex polyhedra/3-connected planar graphs, not the stated general cellular-embedding claim.
- At 13620–13622 σ0=σ1=c and σ∞=c^{-1} have product c≠1 for n>1. They also act on n letters while the claimed map has degree 2n. The explicit rational Belyi map may be studied separately, but the displayed permutation triple is not its monodromy.
- A rectangular finite grid is not automatically a torus cellulation; periodic boundary identifications must be specified (13628–13630).
- Faithfulness of the absolute Galois action concerns the set of all dessins, not one fixed finite dessin or its finite sheets. Lines 14654–14656 cannot describe a faithful action of the infinite absolute Galois group on 168 sheets. The rational map β_n has rational coefficients and is fixed, not freely permuted as asserted at 13735–13742. Equal passports do not in general imply Galois conjugacy.
- The X0(5) index/Belyi degree is 6 by the source's own formula 11999, inconsistent with the asserted 12 edges. K_{3,4} has 7 vertices, 12 edges, and is nonplanar, contradicting the genus-0 and 6-site assertions at 13759–13767. There are 3 primitive characters modulo 5, not 4 (the principal character has conductor 1).

### H5. Every {7,3} count is off by a factor of two

For regular {p,q} polygons the interior angle is 2π/q and area is π(p-2-2p/q). Thus {7,3} face area is π/3, not 8π/3 (13871–13876).

From 3V=2E,7F=2E and V-E+F=2-2g:

E=42(g-1), V=28(g-1), F=12(g-1).

The source itself obtains coefficient -1/21 at 13885–13887, then solves the elementary equation incorrectly at 13889. Its displayed Klein-quartic counts E=84,V=56,F=24 at 13934 actually satisfy the corrected formulas for g=3, contradicting its general formulas.

The oriented triangle group Δ+(2,3,7) has area π/21; π/42 is the reflection triangle's area. Hence a torsion-free subgroup index is 84(g-1), not 168(g-1). A normal quotient of index168 gives genus3, not genus2 (13908–13929).

All architecture/code tables inherit the wrong counts. A genuine {7,3} cellulation with 1008 edge-qubits would have genus25 and 50 logical qubits, not genus13/26. The corrected asymptotic rate is 1/21, not 1/42. The {5,4} comparison at 14269 is also wrong: E=20(g-1), hence rate→1/10, not E=40(g-1),rate1/20.

### H6. The displayed curve is not the Klein quartic with automorphism group PSL2(7)

The equation at 13929 and 14637 is x³y+y³z+z⁴=0. It has projective automorphism diag(ζ9,ζ9^{-3},1) of order9 (all three monomials are fixed). A curve with automorphism group PSL2(7) of order168 cannot have an order9 automorphism. The standard cyclic Klein equation is x³y+y³z+z³x=0. Thus this is not a harmless missing citation.

### H7. The demanded global Euclidean isometry does not exist

At 14108–14110 the entire complete hyperbolic disk is asserted to have a smooth isometric embedding into R³, e.g. a gyroid. The complete constant-negative-curvature surface has the classical obstruction to such a smooth isometric immersion/embedding. A gyroid has varying Gaussian curvature and is not an isometric H² model. Schwarz–Pick (14053–14055) does not construct the claimed Euclidean embedding. Finite distorted patches or abstract graph embeddings are possible, but their distance/coupling errors and global compatibility must be specified rather than assumed away.

### H8. Surface-code distance and encoded dynamics are not proved

- The chain complex 14166–14174 is not a short exact sequence on a closed positive-genus surface: its homology is exactly what the code uses.
- The code space is not the literal intersection of F2-chain kernels inside a complex 2^n-dimensional Hilbert space (14217–14220). Correctly it is the simultaneous +1 eigenspace of commuting stabilizers. Its dimension is 2^{2g}; the rank argument gives k=E-(V-1)-(F-1)=2g.
- A universal lower bound systole≥c log n for every hyperbolic surface/unspecified {7,3} quotient (14228–14235) is not a general systolic inequality. Suitable towers can have logarithmic distance, but an explicit quotient/subgroup and both primal/dual shortest nontrivial cycles are needed. No GAP/Magma program or quotient presentation supports the claimed exact distance8.
- Physical code distance is the minimum primal/dual nontrivial cycle length, not just one real-geodesic systole. Error thresholds require a stated decoder and noise/measurement model; a gate-error threshold cannot be inferred by quoting a code-capacity X/Z noise number.
- The Heisenberg-plus-Z Hamiltonian does not commute with all stated stabilizers (14202,14206,14720). A face X product anticommutes with each nonzero onsite Z term on that face, so [S_f^X,Z_e]≠0 exactly. Pairwise exchange crossing a stabilizer's support likewise need not commute. Thus restricting dynamics to the code space is not justified.
- The physical/logical field spaces are conflated: F2^{2g} labels homology classes/logical Paulis, while the encoded Hilbert space has complex dimension 2^{2g}. They cannot simply be identified with HP eigenvector spaces (14673,14689–14690).
- The deck group Γ_g acts trivially on its quotient surface; its abelianization Z^{2g} is not automatically a finite edge-permutation symmetry group of the quotient (14671–14673).

## 13. Thermostability and oracle section: internal errors versus unverified empirical assertions

The literature-based claims about RFD3 architecture/CLI, coordination numbers, times, single-shot readout, model-supported metals, benchmark pass rates, and experimental gains require checking against the actual cited papers, models, and versioned software. I did not mark them proved from this manuscript. Their failures or successes cannot repair the arithmetic proof.

Several internal problems can already be demonstrated:

1. The supposed eight-oxygen cage lists donor multiplicities 2+1+1+1+2=7 (13013–13021); either a donor/water is omitted or the claim is inconsistent.
2. The heptagonal chunk has 7 separated LBT motifs, but 14030–14032 uses a ≤4-island benchmark to justify ≥60% pass rates. Earlier the text itself says 4–7 islands have much lower rates. Independently designed overlapping chunks do not become one consistent molecule merely because duplicated motifs were fixed in two separate coordinate systems.
3. At 14352–14364 scaffold rigidity is said to reduce Bose occupation nbar(ω,T) at fixed ω,T. That occupation depends only on ω,T; stiffness may change the spectral density/coupling, but not this fixed-frequency Bose factor.
4. The quantitative Tm→Debye→T2→fidelity forecasts (14367–14381,14545–14572) have no derived/calibrated transfer relation here. Dissociation-constant improvement is not evidence for nuclear-spin suppression or coherence improvement (13725–13729).
5. The reward at 14473–14488 has positive weights multiplying destabilization energy and the defined ΔG=-kBT log(pfold/punfold). With these definitions, more stable folded sequences have more negative ΔG, so the positive exponential weights reward *less* stable values. Signs require explicit consistent conventions.
6. Equation 14494–14502 is a full-trajectory balance residual, not a SubTB(λ) sum over subtrajectories. No λ appears. With a unique increasing-index construction path (14465–14467), a backward policy uniform over all possible un-edits must also be reconciled with which predecessors are actually legal.
7. The proof at 14595–14605 substitutes the high-temperature approximation nbar≈kBT/(hbarω) under a low-Debye-temperature condition. These are different conditions; the approximation cannot hold for all integration frequencies. Without specifying |V(ω)|² and energy-conservation/correlation structure, the integral does not force T⁴. For constant V and true Bose occupation, ∫ω² nbar dω scales as T³, not T⁴; additional powers require an explicit coupling law. Thus the displayed universal T2∝Θ_D³/T⁴ proposition is not proved.
8. Statements that a 20-prime circuit beats comparable classical computation (13718–13723), or that 5040 primes guarantee ~800 zeros of any moderate-conductor L-function to circuit precision (14750–14755), have no error/resource theorem and contradict the explicit finite-product/vacuum-overlap constructions above.

## 14. Recommended recoverable research program

1. Preserve the source as provenance; in a separately authorized revision remove/relabel all unconditional RH/GRH, exact Eichler–Shimura geodesic matching, and hardware-determinant claims. Keep the valid conditional Hurwitz/Fredholm theorem with every hypothesis plainly stated.
2. Choose one well-defined target: e.g. an ordinary Selberg zeta/dynamical transfer model with its actual hyperbolic lengths, or an arithmetic explicit-formula positivity criterion with its actual prime weights. Do not identify these zeta functions by analogy.
3. Construct a specified finite state space, network, weights, domains, and twist map. Check signed/complex arithmetic weights honestly. Prove positivity/reversibility only where they truly hold, or use self-adjoint block constructions without pretending those preserve the old determinant.
4. Separate the fixed self-adjoint H_N, the analytic transfer family T_N(s), and any Fredholm A_N(s). Prove the claimed determinant relationship before taking a limit. Fix determinant-versus-reciprocal orientation, pole clearing, gamma regularization, and a common connected matching domain.
5. For an actual convergence theorem give explicit compact-uniform error bounds, trace-class estimates or normal-family bounds, and a nonzero normalization. If these cannot be proved, record them as open research obligations. Hurwitz is a closure tool, not a substitute.
6. Replace the current Python diagnostics with independently checkable small counterexamples and meaningful convergence observables. In particular, q=1 must immediately report H_N=0 for the current algorithm; no root data should be manufactured from a near-zero finite Dirichlet sum.
7. Correct the torus boundary maps/bifiltration, {7,3} combinatorics, subgroup index, and CSS code ranks. Supply actual finite quotient permutations and compute both primal/dual distances before assigning a hardware genus/code parameter.
8. Treat molecular hardware as a separate empirical control proposal. First verify a single encoded spin manifold and coherent gate model, then a two-site coupling/entangling-gate experiment and nondestructive readout. Use a mathematically correct finite circuit amplitude before making compilation claims. Structural prediction, thermostability, quantum coherence, and number-theoretic convergence require different evidence.

## Verification performed

Besides complete source reading over the stated ranges, I ran a dependency-free standard-library Python calculation confirming the trace-3 element's norm/length, the impossible trace required by length log2, the failed condition-(c) normalization at s=1/4, and the negative quadratic form of the symmetrized unilateral shift. These numerical evaluations merely illustrate exact symbolic arguments given above. No full LaTeX build, original Python pipeline, external paper validation, experimental workflow, or model execution was run.
