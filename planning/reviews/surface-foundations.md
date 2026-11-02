# Read-only audit of surface/order foundations and their GRH relevance

Source: `/Users/amelieschreiber/Documents/LaTeX-projects/GRH/Surface-Orders-Hilbert-Polya/emergent_cyclic_time_hilbert_polya_GRH_COMPLETED.tex` (15,556 lines).

Source SHA-256 observed during audit: `08708269403c3095381c45eb4c82435a073aaca8819f427a232e8eba368e05dc`.

No source/repository files were modified. No MCP, installation, authentication, publishing, or remote service was used. The only generated artifact is this report. All counterexamples below are elementary and self-contained; external citations in the manuscript were not independently checked.

## Conclusion and scope

The sections examined do not establish RH or GRH. There are concrete false statements in the algebraic, representation-theoretic, topological, and arithmetic foundations, in addition to the missing proof of the prime/geodesic and spectral/zero identifications. Several problems admit local corrections, but correcting them does not supply that identification.

**Final textual coverage: every source line 1–9999 and 15370–15556 was read.** This is not a complete formal verification of every theorem or a complete audit of the entire manuscript. Source comments, preamble, diagrams, and tables were read for context rather than independently rendered/verified. Mathematical attention was concentrated on the foundations and GRH interfaces; the engineering, biomolecular, and literature claims were not experimentally or externally validated.

The first pass covered 1–2245, 3550–3975, 4780–5095, 5107–5318, 5475–5750, 6281–6668, 9150–9999, and 15370–15556. A second pass completed all gaps: 2246–3549, 3976–4779, 5096–5106, 5319–5474, 5751–6280, and 6669–9149. Two oversized reads were truncated; the omitted intervals were reread in smaller chunks, including 3255–3336.

I also scanned chapter/section/theorem headings across the manuscript. I did not read lines 10000–15369 in full and cannot exclude later qualifications or alternate arguments there. Such later material would need to replace the false statements identified here, rather than merely cite them.

The main outstanding foundation obligation is a defined, proved map from the arithmetic input to a self-adjoint operator with a trace/determinant identity that includes the correct prime weights, ramification, conductor, gamma factors, multiplicities, and limiting estimates. The first 9999 lines contain assertions of that identity, not its proof.

## Findings most directly affecting the claimed GRH chain

### F1. Integral cyclic induction theorem is false

**Source:** 4831–4843, used in 4803, 4850–4867, 4895–4899 and the later cyclic monomial package.

The theorem says every virtual character is an **integer** linear combination of characters induced from one-dimensional characters of **cyclic** subgroups.

**Counterexample:** let `G = C2 × C2`. Every cyclic subgroup has order 1 or 2, hence index 4 or 2. Every character induced from a one-dimensional character of such a subgroup has even degree. Every integer combination of these characters still has even degree. The trivial character of G has degree 1. Thus the claimed formula cannot hold.

**Correction:** distinguish rational Artin induction from integral Brauer induction. Integral Brauer induction requires a larger class of subgroups (elementary subgroups), not only cyclic ones. One-dimensional characters on the relevant subgroups still lead to abelian/Hecke L-functions over suitable intermediate fields, but the asserted cyclic-only integral framework does not follow.

**Dependencies affected:** the exact stated cyclic toric/monomial reduction, its claimed integral exponent control, and any holomorphy or positivity construction relying on that reduction. This does not itself disprove all possible Hecke factorizations; it disproves the theorem actually stated.

### F2. The toric holomorphy proof reverses a basic analytic fact

**Source:** proposition 5054–5063; proof 5065–5069; claimed relevance 5072–5087.

Line 5067 says negative exponents introduce poles because the generators are holomorphic and **nonvanishing** at the point. In fact, the inverse of a holomorphic nonvanishing germ is holomorphic there. If a generator vanishes, its inverse has a pole, with order determined by its valuation; products can cancel such valuations.

Freeness of an abstract multiplicative semigroup or a polynomial semigroup algebra does not, by itself, identify analytic orders of vanishing or prove nonnegative exponents for the particular Artin character under discussion. A rational function of toric coordinates can have poles on a smooth normal toric variety; for example, `1/x` on the affine line.

**Correction:** formulate a precise semigroup of actual characters/functions, prove its relation to all relevant irreducible L-functions, and establish the required valuation inequalities. The proof given is invalid. I have not established whether a suitably strengthened Artin-semigroup theorem could recover a related conclusion.

**Dependencies affected:** the alleged route from moduli toricity/polynomiality to analytic holomorphy. Meromorphy plus determinant coordinates does not establish Artin holomorphy in this argument.

### F3. Specializing a formal uniformizer to a unit phase is not an order representation in the stated generality

**Source:** the order definition assumes complete local domains at 1747; phase substitution 9612–9617; general local representations 9750–9752.

Take the explicitly permitted DVR `R = C[[t]]`. Suppose a unital C-algebra representation sends `t` to `λ I` with `λ ≠ 0`, as the phase prescription requires. The element `t − λ` is a unit in `C[[t]]` (its constant term is nonzero), but its image is zero. A unital ring homomorphism cannot send a unit to zero. Thus this representation does not exist, even without imposing continuity.

The distinction is between a formal/local order and a separately defined algebraic or analytic family of complex matrices. Substituting a phase into a finite matrix formula can produce a unitary matrix; that does not construct a representation of the original complete DVR/order.

**Correction:** define the appropriate algebraic/analytic parameter family and its fibers, or change the coefficient algebra and explicitly prove the required representation exists. Specify the involution as well; a general hereditary order over an arbitrary DVR has no given complex *-structure.

**Dependencies affected:** the advertised order-to-unitary-clock map, and hence the purported canonical Hilbert space/operator construction for arbitrary heterogeneous DVRs.

### F4. The general construction simply asserts a Selberg trace identity for the wrong kind of operator

**Source:** 9754–9790, especially 9768, 9778–9785.

The Hamiltonian is defined as the logarithm of a single monodromy operator along a chosen generator. Line 9779 then states a primitive-conjugacy-class trace formula for `Tr(exp(itH))`, saying it follows from Selberg. No theorem relating that monodromy logarithm to the Laplacian/automorphic spectral problem is constructed. The usual spectral distribution, identity term, test-function transform, and relevant continuous/parabolic contributions are absent.

For the finite clock realizations actually described, H is a finite matrix. Its wave trace is a finite oscillatory sum. It does not thereby acquire the spectral distribution of a hyperbolic Laplacian or the infinitely many zeros of an L-function. A separate limiting argument would be essential; this subsection supplies none.

Line 9783 also equates the logarithmic derivative of the **completed** L-function with a bare prime-power sum. The latter describes the uncompleted unramified Euler product in its half-plane of absolute convergence. Completion contributes gamma/conductor terms, and the general Artin case requires ramified corrections.

Finally, the equality of geometric norms/conjugacy traces with prime/Frobenius weights is asserted in 9780–9785, not proved. Having the same algebraic shape `trace of a matrix power` does not identify the two indexed distributions.

**Correction:** replace the assertions by precisely stated hypotheses/milestones, or construct a genuine operator and prove the complete trace/determinant identity, including analytic convergence and all correction terms. Specify the distinguished loop and branch canonically rather than assuming root numbers choose the entire logarithm.

**Dependencies affected:** the stated zero/spectrum equivalence 9787–9788 and the GRH conclusion 9790. Those conclusions do not follow from the preceding construction.

### F5. Outer automorphisms cannot be composed with an algebra representation as written

**Source:** 9285–9297, particularly 9292–9295; background 6357–6374.

The manuscript has a map `Hol: π1(X) → Out(Λ)` and an algebra representation `π: Λ → B(H)`, and says to compose them to obtain a unitary representation. These maps have incompatible source/target types: an outer automorphism is not an element of Λ.

**Correction:** prove the chosen representation is invariant under the relevant automorphisms, choose unitary intertwiners implementing them, and prove coherence. In general the implementers exist only under additional hypotheses and may define a projective representation with a nontrivial cocycle. Passing to outer automorphisms does not itself solve those issues.

**Dependencies affected:** the clock-induced local system and twisted Laplacian used in the GRH construction.

### F6. Square root of the shifted Laplacian is not self-adjoint on the stated full spectrum

**Source:** 9299–9304.

The candidate is `H = sqrt(Δρ − 1/4)` and is described as self-adjoint on the continuous/discrete decomposition. For the trivial twist on a connected finite-area surface, the constant L² function has Laplacian eigenvalue 0. Therefore `Δ − 1/4` has eigenvalue −1/4. No self-adjoint square root can have square equal to a negative operator on that subspace.

**Correction:** explicitly restrict to the spectral subspace `Δ ≥ 1/4`, or treat the exceptional spectrum separately and prove it does not invalidate the proposed zero correspondence. The caveat about cusps/thresholds does not provide this construction.

**Dependencies affected:** the first candidate family's advertised self-adjointness and full spectral correspondence.

### F7. Modular scattering coefficient uses the wrong completion

**Source:** 9325–9326.

The manuscript defines the entire xi function `ξ(s) = 1/2 s(s−1) Λζ(s)` and writes `φ(s)=ξ(2s−1)/ξ(2s)`. The standard coefficient uses `Λζ(2s−1)/Λζ(2s)`. With the manuscript's entire xi convention this is

`φ(s) = [s/(s−1)] ξ(2s−1)/ξ(2s)`.

For example, the actual modular scattering coefficient has a pole at s=1; the displayed entire-xi ratio is finite there.

**Correction:** use the non-entire completed zeta with the appropriate notation, or insert the missing rational factor and track its pole.

**Dependencies affected:** the concrete scattering testbed and its stated pole/zero bookkeeping. The elementary observation that scattering resonances are not automatically eigenvalues, explicitly acknowledged at 9334, remains sound.

## Concrete algebraic/geometric foundation failures

### F8. Twisted shift normalizes the opposite Iwahori orientation

**Source:** order matrix 1819–1826; shift 1836–1843; normalizer lemma/proof 1847–1864; reused in 2187–2195 and 9554.

For m=2 the order is `Λ = [[R,R],[πR,R]]` and `S = [[0,π],[1,0]]`. Then `E12 ∈ Λ`, but

`S E12 S^(-1) = π^(-1) E21 ∉ Λ`.

Thus the lemma is false for the displayed order. The earlier order matrix at 1757–1764 uses the opposite triangular orientation, for which this shift convention is compatible; the expanded insertion changed the orientation without changing the shift.

**Correction:** transpose/reverse either the order or shift consistently. For the displayed upper Iwahori order, the reverse cyclic shift with wrap factor π is the appropriate convention. Recheck all subsequent inverse/conjugacy/normalizer statements. Introducing an arbitrary exponent e does not automatically normalize the same order either.

**Dependencies affected:** local clock admissibility, normalizer classification, gluing, and every example citing this lemma.

### F9. Reversal does not force switching allowed cycles

**Source:** 1958–1967; proposition/proof 2056–2086; corollary 2088–2099; positivity inference 2101–2108.

For an allowed triangle `a1:x1→x2`, `a2:x2→x3`, `a3:x3→x1`, the inverse cyclic walk `a1^(-1) a3^(-1) a2^(-1)` is reduced and stays on the same allowed cycle. Its oriented inverse is the allowed a-cycle, so it contains no inverse of a forbidden relation.

The proof counts the two outgoing **arrows** at u but ignores inverse letters of arrows **incoming** to u. A string after `a^(-1)` can continue backward along the permitted predecessor, not only forward along the other outgoing arrow. Immediate backtracking is forbidden; arbitrary backward travel along an allowed cycle is not.

**Correction:** restrict the claim to the explicitly chosen forward-oriented continuation after an inverse letter, if that restricted move is desired; it is an additional rule, not a consequence for all strings. Prove the proposed operator transport separately.

**Dependencies affected:** the asserted forced adjacent-clock reversal and its use to justify planar positive transfer matrices/detailed balance.

### F10. The sphere 'corrigendum' has the wrong number of faces and its relations are not gentle

**Source:** 924–928, 955; quiver construction 959–979; relations 986–997.

Two vertices joined by three disjoint meridian edges on a sphere give `V=2,E=3,F=3`, since `V−E+F=2`. The three complementary regions are digons. They are not the two triangular faces described in the text. Consequently the stated face-based medial-quiver derivation does not follow from this dessin.

The displayed bound quiver also violates the gentle uniqueness condition: after `a2:v2→v3`, both outgoing arrows `a3:v3→v1` and `b2:v3→v2` are forbidden, because `a3a2=0` from 989 and `b2a2=0` from 995. Several other listed products are not composable and hence impose no path relation at all.

**Correction:** reconstruct the actual cellular embedding, distinguish vertex cycles from face cycles, and write a composable relation table satisfying the intended gentle conditions.

**Dependencies affected:** the claimed minimal geometric/time-orientation example and the DG example that explicitly cites this bound quiver.

### F11. Čech gluing data alone do not define π1 holonomy

**Source:** unrestricted sheaf/chart setup 6295–6306; formula/proposition 6346–6369.

An arbitrary cocycle of algebra-sheaf automorphisms defines a glued bundle/sheaf. It does not specify transport between different points of a chart. The displayed product of transition functions along overlaps is not even an unambiguous element of a single stalk without such transport. General transition functions can vary with position.

**Correction:** assume a locally constant local system (flat bundle), or construct a flat connection and parallel transport. Prove path/refinement independence and the relation to the chosen outer/projective quotient.

**Dependencies affected:** the claimed homotopy-invariant time-holonomy representation and its GRH twist construction. The standard correspondence invoked in 6367 applies to flat/locally constant data, not arbitrary Čech cocycles as stated.

### F12. Local unipotence does not imply a nilpotent-by-finite holonomy group or bounded exponent

**Source:** proposition 6456–6459.

Over characteristic zero, `U=[[1,1],[0,1]]` satisfies `(U−I)^2=0`, but `U^n=I+n(U−I)` has infinite order. This alone disproves the claimed bounded group exponent from a nilpotency index N.

Moreover, U and `L=[[1,0],[1,1]]` are both unipotent of index 2, but together generate `SL2(Z)`, which is not virtually nilpotent (it contains a nonabelian free subgroup). Their product already has non-unit eigenvalues `(3±sqrt(5))/2`.

**Correction:** simultaneous triangularity/common preserved filtration can yield a unipotent nilpotent group. Nilpotency class and element order must be distinguished; in characteristic zero nontrivial unipotent groups have infinite-order elements.

**Dependencies affected:** bounded-drift interpretations and any argument that promotes local truncations to controlled global holonomy.

### F13. The stated BFZ parametrization only produces symmetric matrices

**Source:** theorem 5626–5639, formula 5632.

The product is `U D U^T`, because the same parameters appear in the upper and reversed lower factors. Every resulting matrix is symmetric. It cannot parametrize an open dense subset of all totally positive matrices. For example, `[[1,2],[1,3]]` is totally positive and nonsymmetric.

**Correction:** use independent parameter sets for the upper and lower unipotent factors. The symmetric specialization is useful, but must be advertised as such. This local correction does not prove arithmetic transfer matrices are in that specialization.

**Dependencies affected:** the asserted all-matrix factorization and any claim that detailed balance/symmetry follows automatically from general total positivity.

### F14. Positive Grassmannian coordinates do not automatically make arbitrary transfer matrices totally nonnegative

**Source:** implication chain 3674–3692; 3713–3722; corollary 3904–3912; inference 2103–2108.

The positive part is an additional real semialgebraic restriction, not a consequence of having a Grassmannian/incidence presentation. A complex representation variety is not thereby contained in it. Even a matrix assembled from positive scalar coordinate functions need not be TN: `[[1,2],[2,1]]` has positive entries but determinant −3.

LGV supplies TN only for an actual compatible planar acyclic network/path matrix with the required boundary order. A ribbon graph on a torus or arbitrary surface, cycle reversal, and positive edge weights do not by themselves construct such a disk network or detailed balance. Also, the trace-generation theorem for GL invariants does not generate all SL semi-invariants by cycle traces: for the one-arrow quiver of dimensions (1,1), SL is trivial, so its invariant ring is k[a], whereas there are no oriented cycles and the cycle-trace ring is k.

**Correction:** specify the concrete matrices, prove every minor has a suitable positive network expression, prove the arithmetic data lie on the positive locus, and prove reflection symmetry/detailed balance. Separate GL trace invariants from SL semi-invariants.

**Dependencies affected:** the central geometry→positivity→self-adjointness interface. The finite-dimensional theorem 5656–5679 is essentially valid once a symmetric positive transfer matrix is actually supplied (the scalar-shift sign at 5677 needs correction).

### F15. Covering push-down does not make the stated representation-variety map smooth

**Source:** corollary/proof 5295–5316.

Take the oriented two-cycle with radical-square-zero relations, and its universal cover, the radical-square-zero infinite line. Give two adjacent covering vertices dimension 1 and every other covering vertex dimension 0. The upstairs representation variety is A¹, with coordinate x. Downstairs dimensions are (1,1), and the representation variety is `Spec k[x,y]/(xy)`. The push-down map is the inclusion of one coordinate axis, `x↦(x,0)`. At the origin its tangent map is `k→k²`, not surjective, so the map is not smooth.

If 'corresponding strata' is intended to mean a smaller target on which this example becomes an isomorphism, that target must be precisely defined; it is not the displayed full representation variety.

Line 5312 also conflates the tangent space of a representation scheme (derivations) with derivations modulo inner derivations (Ext¹, controlling deformations modulo basis changes). Obstructions are governed by Ext², not Ext¹.

**Correction:** state the correct covering/singularity theorem with its exact hypotheses and maps; do not infer smoothness of this bare push-down map from the Hom decomposition.

**Dependencies affected:** claimed geometric transport of smoothness and singularity types by covering functors.

### F16. Hochster–Eagon over arbitrary Noetherian base is overclaimed

**Source:** 3826–3834.

The theorem says `R[X]/I_t(X)` is CM for every Noetherian R and normal whenever R is a domain. For t=1 the quotient is R. Taking the nonnormal cusp domain `R=k[u²,u³]` contradicts normality. Taking any Noetherian non-CM R contradicts the CM claim.

**Correction:** impose the requisite CM/normal base hypotheses (or state the standard field version). Generic determinantal constructions cannot repair arbitrary singularities already in the coefficient ring.

**Dependencies affected:** claims of automatic good geometry under unrestricted base change. This does not refute valid characteristic-zero field results for individual circular-complex components.

### F17. The heterogeneous overlap-ring identity is false

**Source:** 9734.

The manuscript identifies `R_u ×_k R_v` with `k[x,y]/(xy)` for arbitrary DVRs. For `R_u=k[[x]]`, `R_v=k[[y]]`, the fiber product is the completed nodal ring `k[[x,y]]/(xy)`, not the affine polynomial node. For localized DVRs one gets the corresponding localized version. The affine polynomial rings k[x], k[y] are not DVRs.

**Correction:** keep the precise local/complete fiber product and residue maps. Gluing different local orders with different matrix sizes also requires explicit overlap/corner maps; it is not automatically conjugation of the entire orders inside one GL group.

**Dependencies affected:** the claimed arbitrary-DVR global order construction and its functoriality.

## Explicit torus and appendix counterexamples

### F18. The bipartite 'cellular chain complex' is not a chain complex

**Source:** edge boundaries 9942–9948; face word 9950–9959; H1 proposition/proof 9961–9975.

The word `e1 e6^(-1) e2 e4^(-1) e3 e5^(-1)` is not a composable graph walk: e1 ends at W14, while e6^(-1) starts at W36. Taking its claimed signed cellular boundary anyway yields

`∂1∂2(f) = 3(B2−B1) ≠ 0`.

The asserted cycle representatives are not cycles either:

`∂(e1−e2+e4−e5) = 2(W14−W25)`,

`∂(e1−e3+e4−e6) = 2(W14−W36)`.

Line 9972 explicitly computes two equal-sign summands and then declares their sum zero. The integer coefficient setting rules out a characteristic-two rescue. Subdividing each of the original three torus edges gives six edges; the unique face traverses each of those edges twice, hence a 12-incidence boundary, not the asserted six-edge word.

**Correction:** construct the actual attaching walk and chain map. Route-difference cycle representatives have the opposite signs on the B2 halves, for example `e1−e2−e4+e5` and `e1−e3−e4+e6`. The correct torus has H1≅Z², but the displayed proof does not compute it.

**Dependencies affected:** all persistence/homology calculations built on this explicit chain model and its proposed arithmetic toy validation.

### F19. The appendix's claimed 3-vertex→6-vertex algebra quotient cannot exist

**Source:** three quiver vertices/arrows 15411–15419; theorem/proof 15451–15465.

Let `B=k(C6)/J²`. Suppose a surjective unital k-algebra map `Λ→B` existed. Compose with `B→B/rad(B)≅k⁶`. Each arrow of Λ has distinct source and target among the three vertices. Its image in the commutative algebra k⁶ lies between orthogonal idempotents, hence is zero. Thus the image is generated by the images of only three mutually orthogonal vertex idempotents. Such an image has k-dimension at most 3, so cannot be all k⁶. This contradicts surjectivity.

This argument rules out any such surjection for this quiver, not only the stated arrow prescription. The six arrows do not generate the six vertex idempotents in B; line 15463 overlooks them. The face visits three original vertex spaces repeatedly; six independent B vertex spaces are different data.

**Correction:** use an unfolded face quiver and an explicitly defined restriction/pullback/push-down construction. A face traversal can yield a circular complex with repeated vector-space dimensions, but that is not the claimed quotient and fully faithful inflation of all B-modules.

**Dependencies affected:** appendix's Hom-controlled embedding, closed-face-stratum identification, and claimed full reduction to Λ6. The elementary fact that genuine algebra quotients give full restriction of scalars is valid; the required quotient here is impossible.

### F20. The appendix has additional bands beyond the two stated cycle words

**Source:** 15471–15485; arrows 15414–15418; relations 15427.

The word `a1 b3^(-1)` is a cyclic string: both a1 and b3 point x1→x2, so it runs x1→x2→x1. The arrows are distinct, so no immediate cancellation occurs. Every subword of every power alternates a direct and an inverse arrow, so none is a direct zero relation or its all-inverse inverse. It is primitive. This is a band different from either directed triangle or its inverse.

**Correction:** enumerate primitive cyclic strings properly and identify the resulting parameter families. Also, for a homogeneous tube, τ fixes each indecomposable up to isomorphism; it does not change quasi-length as claimed at 15484. Distinct λ values label distinct homogeneous tubes in the usual band setting, not quasi-simples of one single homogeneous tube.

**Dependencies affected:** the asserted exactly-two-band classification and AR diagrams justified from it.

### F21. Appendix projectives are infinite dimensional and not objects of the finite-dimensional module category being drawn

**Source:** 15506–15522; mixed relations 15424–15429.

The pure directed a-cycle has no relation killing any power. Hence `(a3 a2 a1)^n` survives for all n, and the vertex projectives have infinitely many independent paths. They are not finite-dimensional objects of the usual `mod Λ` category used for the band/string discussion. The text itself notes the algebra is infinite dimensional and usual AR techniques can fail at 1099.

Furthermore an indecomposable projective does not decompose as a sum of two branches as claimed at 15508; its radical may have a branch decomposition, while the projective has a common simple top.

**Correction:** choose and state a category supporting these projectives and appropriate almost-split sequences, or truncate the algebra and rederive the module classification. A truncation changes the algebra and cannot be implicit.

**Dependencies affected:** the appendix's projective boundary/preprojective component proposition and its finite-dimensional AR interpretation.

### F22. Appendix incidence resolution has incorrect Grassmannian dimensions

**Source:** 15537–15549, especially `dim R_i=d_i−r_(i−1)` at 15541 and `im D_(i−1)⊂R_i⊂ker D_i` at 15543.

Take all six dimensions d_i=1 and maximal ranks alternating `(1,0,1,0,1,0)`. These ranks satisfy all adjacent inequalities and are coordinatewise maximal. At any vertex where the incoming rank is 1, the stated formula demands `dim R_i=1−1=0`, but R_i must contain a one-dimensional image. Thus the asserted incidence variety has no points over the generic rank stratum it supposedly resolves. This is a direct counterexample to the proposition.

**Correction:** standard image-incidence uses `dim R_i=r_(i−1)`, or kernel-incidence uses `dim R_i=d_i−r_i`, with appropriate rank bounds and proof. These are not the dimension written in the appendix.

**Dependencies affected:** the explicit torus resolution, birationality claim, and any positive-chart argument relying on this formula.

## Further local errors and cautions

### Additional findings from completion of lines 1–9999

**F23 — The q-Euler inversion has a double sign error (2871–2888).** The definition already includes `(-1)^t`, but the claimed inversion inserts a further `-q`. For the Koszul algebra `A=k[x]/(x²)`, the scalar Cartan series is `C(q)=1+q`; Ext^t(k,k) has dimension 1 for every t≥0, hence the defined Euler series is `E(q)=1/(1+q)`. The displayed identity `C(q)E(-q)=1` instead gives `(1+q)/(1−q)`. With this signed Euler convention the inversion should use `C(q)E(q)^T=I` (with consistent left/right indexing), not `E(-q)`. This affects the claimed Ext-to-Cartan determinant bridge; it is locally repairable and does not supply arithmetic matching.

**F24 — The earlier incidence model is also empty over its claimed generic stratum (3515–3521).** Here `rank d2=e`, `rank d1=f−e` generically, so `dim ker d1=e`, while the proposed R has dimension e+1. Take e=1,f=2,g=1, `d2=(1,0)^T`, `d1=(0,1)`. This is a valid complex satisfying all displayed rank bounds, but no two-dimensional R can lie in its one-dimensional kernel. The proposed Grassmannian resolution therefore misses this generic point. Correct the rank/Grassmannian dimensions and reprove the vanishing/pushforward statements; this is the same kind of defect as F22, now in the foundational incidence input itself.

**F25 — A straightening law does not imply a toric associated graded, and the whole semi-invariant ring can be reducible (4491–4505, 4760–4779).** The standard monomial/term-order degeneration can have a monomial initial ideal and zero divisors. For example, `k[x,y]/(xy)` has the standard monomial basis `{1,x,x²,...,y,y²,...}` for the poset with x,y incomparable and straightening relation xy=0. Its associated graded is itself, a reducible ring, not the coordinate ring of an affine toric variety. Monomial relations cannot simply be identified with a cancellative affine-semigroup toric algebra at 4505. A genuine toric degeneration needs stronger valuation/SAGBI hypotheses and a suitable prime binomial initial algebra.

There is also a counterexample inside the manuscript's explicit family: take `A=A_(2,1)` from 4117–4122 with dimension vector (1,1). Since SL1×SL1 is trivial,

`SI(A,(1,1)) = k[a1,a2,b1,b2]/(a1a2,b1b2)`.

This ring has zero divisors and four irreducible components. It is not the coordinate ring of an irreducible affine toric variety, contrary to the whole-ring assertion at 4765. Restricting to specified components would change the theorem and requires a separate proof. Finally, even the existence of a toric degeneration of an original ring does not make the original ring toric. These errors directly affect the claimed invariant-theoretic input to Artin holomorphy and transfer positivity.

**F26 — The stated Plücker identity omits necessary ordering signs, and its 'equivalent' minors statement is false (4439–4455).** The coordinates were defined using sorted subsets at 4428–4430. With that convention, the insertion of b_r into A in 4445 has an extra ordering sign not included in `(-1)^(r−1)`. For k=2, A={3}, B={1,2,4}, take the point of Gr(2,4) represented by

`X = [[1,0,1,1],[0,1,1,2]]`.

The relevant minors are `p12=1,p13=1,p14=2,p23=−1,p24=−1,p34=1`. The displayed sum is `p13 p24−p23 p14+p34 p12 = 2`, not 0. Using alternating ordered-tuple coordinates instead of sorted-set coordinates repairs the sign convention. The further claim at 4447 that this sum is equivalent to all 2×2 minors of the displayed two-row array vanishing is independently false; a general three-term Plücker relation is not a rank-one condition on that array. This undercuts the advertised self-contained determinantal proof, while leaving the correctly stated standard Plücker relations available.

**F27 — The rational-clock refinement claims fail as written (5972, 6052–6055, 6073–6086).** The universal rational rotation C*-algebra A_(p/q) is infinite dimensional; the q-dimensional clock matrices are a quotient representation with fixed values for central U^q and V^q, not a faithful representation of that whole algebra. Consecutive continued-fraction denominators are coprime, and after they exceed 1 cannot satisfy `q_k | q_(k+1)`, contrary to 6054. For example the golden-ratio convergents have consecutive denominators 2,3,5,8. A separate divisible tower and a proof of coherent intertwiners are needed. The proposed phase calibration observable at 6085 is exactly `V U U† V†=I` for all unitaries; its expectation is 1 and cannot detect the commutation phase. Use the actual group commutator, e.g. `V U V† U†` with the appropriate sign convention. At 7036–7038 the two specified infinite-clock operators also coincide under Fourier transform (the shift is multiplication by e^(iθ)), so they commute, rather than obeying the claimed nontrivial Weyl relation. These are specific problems in the purported finite-to-infinite clock/trace bridge.

**F28 — Multiplying the real logarithm of a positive transfer matrix by i is not a self-adjoint generator (5774).** If T is symmetric positive definite, log T is self-adjoint; i log T is skew-adjoint, except in the trivial case log T=0. For example any nonidentity symmetric TP 2×2 matrix supplies a counterexample. It is not equivalent to `−(1/a)log T` with real a>0. Keep the Euclidean logarithm and Lorentzian unitary evolution distinct. This is a local sign/type error; the real-log theorem 5656–5679 remains available once the correct matrix is supplied.

**F29 — Several concrete quantum implementation propositions fail elementary checks (7200–7207, 7221–7225, 8080–8098, 8295–8315, 8350–8373, 8514–8538).** These are not needed for the negative GRH audit conclusion, but prevent treating the engineering layer as already established mathematics:

- There is no linear Hilbert-space isometry `C^(d²)→C^d` for finite d>1. A unitary followed by partial trace is a channel on density matrices, not that isometry. Partial trace is linear, so discarding alone does not create a nonlinear state map. The later correct channel formula does not repair the earlier isometry claim.
- The feature encoding `Z_d^floor(κx)|0>` is identically |0>, as is `exp(ix n̂)|0>` in the momentum-zero basis. Thus the worked micro-examples encode no x dependence at all (7221–7225, 7432–7435). Start from a suitable superposition, or use an actual nonconstant encoding.
- In the displayed star circuit, all final CZ gates commute with the central Z^m readout. Therefore the Z-population/Fourier readout is unchanged by those entanglers and cannot obtain the claimed neighbor-dependent convolution in 8350–8373. A basis-changing gate/readout or a different entangler is needed. The first identity in 8337–8348, Fourier transform of the diagonal, is valid.
- Rank-one projectors alone do not imply the sum of their overlap probabilities is ≤1 at 8303. The projectors must form a sub-POVM (for rank-one orthogonal projectors, an orthonormal set suffices). With U=I, templates |0> and |+>, and input |0>, the stated sum is 1+1/2. The frame/U notation in 8298–8302 also needs consistent conjugation.
- The Stinespring statement for arbitrary different input/output H,H' at 8082–8085 has a dimensional type mismatch: the displayed unitary is on H⊗K and tracing K leaves H, not H'. The isometric formulation `V:H→H'⊗K` in the proof is the appropriate general statement; its extension to a unitary requires compatible enlarged input/output spaces.
- A matching contraction removes one vertex per matched edge. Even a perfect matching reduces N to N/2, and a merely maximal matching may reduce by less; the proof's 'at least a factor 2' at 8533 is backwards. A three-vertex path contracts to two vertices. Bounded degree can yield a weaker constant-factor bound with more assumptions, but not the asserted universal Θ(N/2^ℓ). Neither generic pooling nor a feature count proves quantum error correction or holographic reconstruction.
- The exponential retrieval/capacity claim at 8425–8436 has no pattern-separation, normalization, or noise hypotheses. Identical keys cannot be distinguished at any hidden dimension. A modern Hopfield theorem cannot be transferred merely by substituting the Hilbert-space dimension into a capacity exponent.

The biomolecular and hardware literature assertions in 8797–8955 were read but not independently checked. The emergent-gravity chapter itself labels its Einstein limit assumptions and redshift relation as assumptions/postulates (6775–6778, 6903–6934). Neither those postulates nor implementing any finite circuit supplies an arithmetic zero/spectrum identity.

- **1331:** `A=k[ε]/(ε²)`, degree ε=−1 and `dε=1`, is acyclic, not a resolution with H*(A)=k. The differential from degree −1 to degree 0 is an isomorphism, and 1 is exact. Repair the example; this alone does not refute the general minimal-model theorem.
- **1400:** Ext¹(S_i,S_i) for a vertex simple is not spanned by the two arrows leaving/entering the vertex. In the displayed no-loop double-triangle quiver, self Ext¹ is zero; arrows describe Ext¹ between the appropriate distinct vertex simples. The 'informal' label does not make the self-Ext statement correct.
- **1234:** distinct strings do not invariably yield nonisomorphic modules: inversion gives isomorphic string modules. String modules are not all rigid; for instance a simple over the one-loop square-zero gentle algebra has nonzero self Ext¹. State the usual equivalences and the appropriate subclass if rigidity is intended.
- **1240:** excluding λ=1 from band parameters omits legitimate bands; there is no justification for that exclusion in the stated general setting.
- **1140,1151:** the graph of the nilpotent linear map f must also include the kernel pair `(e3,0)`; the graph of f² has dimension 3, not the single-dimensional subspace claimed. An endomorphism graph has the same dimension as its domain. Subsequent relation calculations should be rebuilt with the zero-image pairs included.
- **2141–2149:** 'all hereditary orders' requires general block lattice-chain types, not only the full rank-one successive quotient chains defined at 2134–2138. For example the maximal order M_m(R) is hereditary and has a one-step chain of period 1; it is not conjugate to the full Iwahori order with m rank-one steps. The proof also incorrectly speaks of a unique indecomposable projective for general hereditary orders.
- **6526–6538:** arbitrary dessins can have spherical or Euclidean triangle signatures; the manuscript's own (2,3,6) torus example at 9701–9706 is Euclidean. A uniform statement using H and a hyperbolic triangle group needs the hyperbolic inequality and the appropriate orbifold/uniformization qualifications. This does not negate Belyi correspondence.

## What remains usable and what a repaired argument would still need

Several standard ingredients are valid when stated with their actual hypotheses: finite-dimensional spectral calculus gives self-adjoint logarithms of unitaries; symmetric positive-definite transfer matrices have self-adjoint real logarithms; a genuine algebra quotient gives full restriction of scalars; Euler factors are determinants; a correctly constructed flat unitary local system gives a self-adjoint twisted Laplacian; and circle-complex rank loci have substantial independent geometric theory. These facts do not identify an arbitrary transfer spectrum with arithmetic zeros.

The text itself distinguishes numerical/test programs in 9390–9391 and expressly says the toy does not encode nontrivial L-function zeros in 9430–9433. Those are sensible limitations, but conflict with the completed-proof claims at 422 and 9153–9162 unless the missing arithmetic identification is separately proved. The general construction at 9778–9790 does not provide that proof.

After correcting local algebra/topology, a rigorous GRH argument would still require: (1) a well-defined arithmetic input-to-operator construction; (2) actual unitary/positive realization and domains; (3) exact trace or determinant matching, including completed/ramified terms; (4) zero multiplicity/completeness and continuous-spectrum treatment; and (5) the operator/determinant convergence estimates needed for a valid limiting theorem. Ordinary persistence stability, toric normality, finite-matrix positivity, or formal similarity of trace formulas cannot substitute for these obligations.

These are mathematical findings on the inspected source, not a claim to have refuted RH/GRH or every possible surface-order research program.
