# Audit of the October 2026 quasi-Riemann manuscript

## Artifact and coverage

I read **all 3988 lines** of `/tmp/grh-math-audit/quasi-oct.tex` (169005 bytes, 17135 words), including its full proofs and bibliography. I independently recomputed its Git blob ID as **2000faddbbebac5de0ecfe0b962534ea61a852d5**, matching the parent's specified artifact. SHA-256: `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.

Read ranges: 1–660 (with 327–350 separately reread to recover a truncated excerpt), 661–1000, 1001–1334, 1335–1685, 1686–2025, 2026–2350, 2351–2686, 2687–3020, 3021–3350, 3351–3650, 3651–3988. No lines were skipped. No source modifications, MCP use, installations, authentication, proof execution, or scientific runs occurred. This report is an explicitly requested generated artifact.

This is an independent source audit, **not a proof certification or a refutation**. I found no comparably elementary contradiction to the false modular-geodesic claims in the surface-order manuscript. I have not independently rederived every metaplectic-theta cusp formula from the cited external papers. The appropriate status is: a substantial claimed zero-free-region argument with clearly identifiable advanced inputs that require specialist verification.

## 1. What this paper actually claims

The abstract, lines 47–48, and main theorem, lines 73–75, claim:

> Every finite-order Hecke L-function over K=Q(sqrt(-3)) has no zeros in Re(s)>11/12; hence every Dirichlet L-function, including zeta, has no zeros there.

This is a **fixed-width zero-free half-plane**, independent of conductor and height. It is much stronger than the shrinking classical regions displayed at 136–157. It would rule out zeros arbitrarily close to 1 and the usual Landau–Siegel phenomenon. It is nevertheless **strictly weaker than RH/Dirichlet GRH**.

For primitive Dirichlet L-functions, functional-equation/conjugation symmetry would give nontrivial zeros only in the closed region

`1/12 ≤ Re(s) ≤ 11/12`.

It does not prove Re(s)=1/2. Zeros with, for example, Re(s)=3/4 are compatible with its conclusion. The strict inequality in the theorem does not exclude zeros on either 11/12 or 1/12.

Its general Hecke assertion is restricted to finite-order characters over the specific Eisenstein field. The Dirichlet deduction works by quadratic base change. It does not claim or supply GRH for all Hecke characters over arbitrary number fields, all Artin representations, or all automorphic representations.

Line 81 cites a separate September 30 manuscript claiming the stronger boundary 7/8, with bibliography entry 3875–3880. That reference is comparison/context: the October paper gives its own 11/12 argument and does not use the September theorem as an input in the displayed proof chain. Neither boundary is 1/2.

The iteration in Section 5 reduces auxiliary row/column parameters. It is not an iteration that repeatedly pushes the zero-free boundary toward 1/2. Treating the word “iteration” as a route from 11/12 to full GRH would misread the proof.

## 2. The logical dependency chain

The precise proof route is:

1. **Original sextic-twisted Möbius mean square:** Proposition `thm:ms`, lines 679–689, claims

   Σ_{0<N(u)≤D^{1+θ}} |A_u(D)|² ≲ D^{2+θ+ε}

   with a finite smooth-weight derivative norm and constants depending on the fixed Hecke character, excluded primes, support interval, θ and ε.

2. **Extraction using sixth powers of primes:** lines 694–724 isolate rows u=p^6. Since χ_n(p^6)=1_{p∤n}, these rows approximate the untwisted Möbius sum to O(D/Y), with Y=D^{(1+θ)/6}. The calculation gives exponent 11/12+5θ/12+ε, then θ is made sufficiently small for each requested loss.

3. **Mellin continuation of the reciprocal L-function:** lines 726–757 derive that a nonzero Mellin transform of a chosen test function divided by L_K^S is holomorphic in Re(s)>11/12; a zero of L there gives a contradiction.

4. **Quadratic base change:** lines 759–770 use

   L_K(s,χ∘N)=L(s,χ)L(s,χχ_{-3})

   up to harmless omitted Euler factors, and handle the possible pole at 1 using standard Dirichlet nonvanishing.

5. **Poisson reduction:** Proposition `prop:poisson-reduction`, lines 1000–1022 and proof 1024–1252, reduces the original mean square to an auxiliary cubic-Gauss-coefficient mean square E(H,X,F), defined at 938–953.

6. **Canonical mean-square estimate:** Proposition `prop:canonical`, lines 1261–1277, treats H≤XF D^{-κ}. It is proved using completed theta sums, cube inversion and a transfer inequality.

7. **Completed bound:** Proposition `prop:R`, lines 1317–1333, bounds the completed sums by H+H²N(f)/X. Its proof at 1632–2214 relies on the theta reflection formula and a quadratic large sieve.

8. **Cube removal:** Lemma `lem:cube-reduction`, lines 1341–1467, removes cube-completion terms by explicit Möbius inversion and weighted Cauchy–Schwarz.

9. **Transfer estimate:** Proposition `prop:transfer`, lines 1487–1509, is proved by two Poisson calculations in 2217–2683. Its output has H'≤HL/(ΣF), H'/Σ'≤H/Σ, Σ'≤L.

10. **Finite descent:** lines 1516–1609 prove the canonical estimate by induction on H≤D^{jκ}; lines 1613–1629 return to the original mean square.

This source makes the hard estimate an explicit mathematical proposition and supplies a real proof architecture for it. It does not silently declare arbitrary self-adjoint spectra to be L-function zeros. That distinction matters when comparing it with the surface-order completion.

## 3. Checks that survived source-level scrutiny

### 3.1 The 11/12 exponent arithmetic is coherent

The calculation at 711–723 is:

|A_1|² ≲ D^{2+θ+ε}/Y + D²/Y²
       = D^{11/6+5θ/6+ε} + D^{5/3-θ/3}.

Taking square roots and choosing θ small gives the stated D^{11/12+ε}. Constants may depend on θ; this is consistent with choosing a fixed θ separately for each desired exponent loss. No uniformity as θ→0 is needed for this deduction.

The pointwise comparison A_{p^6}=A_1+O(D/Y) and the use of prime-ideal counting are explicit. This is a conditional deduction from Proposition `thm:ms`, not a proof of that proposition by itself.

### 3.2 The Mellin contradiction uses a genuine common domain

At 729–745 the test W(y)=y^{-ρ}φ(y) has Mellin transform nonzero at ρ. The Möbius-saving estimate gives a holomorphic M_W on the connected half-plane Re(s)>11/12, and the reciprocal-L identity is first proved in its nonempty subdomain Re(s)>1. The identity theorem then has the connected overlap it needs. This is unlike the disjoint-overlap error in the surface-order manuscript.

The omitted finite Euler factors have no zeros for Re(s)>0 when their finite-order values have modulus at most one. A pole of L at 1 does not invalidate a contradiction at an assumed zero ρ; the meromorphic identity can be understood with the removable cancellation at the pole.

### 3.3 The descent scales do contract as stated

Combining H_c³=X²/H² in the nonempty remainder case with the transfer bounds gives, at 1568–1575,

H'≤H/(N(b)³F²)<H(H/Σ)²≤D^{-2κ}H,

while H'/Σ'≤D^{-κ}. This justifies the finite induction depth j=ceil(C0/κ), provided the completed and transfer propositions hold with their stated support/derivative control. The changing derivative order is explicitly budgeted at 1550–1595.

### 3.4 Möbius inversion is written with the required complete multiplicativity

The cube inverse, 1361–1374, is not obtained by discarding potentially cancelling cube terms. The source correctly groups the total cube index and uses Σ_{h|b} μ(h)=1_{b=1}. Short and long ranges are handled separately. The weight zero extensions at excluded primes are explicitly retained.

### 3.5 The elementary local finite-Fourier algebra is substantially specified

The finite Fourier coefficients at 2993–3000, and the local exponent change at 3233–3269, explicitly track inverse-variable changes and the special j=0,4 cases. In particular the advertised sextic-to-quadratic residual exponent is -1-2≡3 mod6, not an unexplained claim that sextic characters are quadratic.

I have not found an explicit false equation in these calculations during this pass. That is not equivalent to a full independent rederivation of the theta automorphy law or cusp normalization.

### 3.6 Smooth separation and recombination are actual estimates

Appendix B, lines 3491–3650, gives Mellin separation with derivative norms, a row-dependent kernel lemma proved by taking a common Fourier coefficient majorant, and weighted Cauchy–Schwarz recombination. The row-dependent nature of the weights has not simply been ignored. The exponent q=2m+4 in two Mellin variables is enough for the displayed integral to converge.

## 4. Load-bearing claims requiring independent specialist verification

These are **verification obligations**, not findings of falsehood. No mathematical counterexample is asserted here.

### 4.1 General fixed-ray theta reflection and its uniformity

Proposition `lem:reflection` (1805–1821), uniformity lemma (1847–1855), and their proof (2874–3478) are the crucial novel bridge. They extend cited theta formulas to arbitrary fixed ray-class twists and varying products of local sextic characters. The required conclusion is unusually strong and precise: after restricting the varying squarefree row to a fixed ray class, the cusp coefficient sequence, additive character and fixed denominator must be independent of that row.

The places to verify against the actual automorphic representation/cusp formulas are:

- normalization/support of c_theta(nb³), 361–366 and 1686–1717;
- reduction to exactly the three listed cusp expansions, 3027–3147;
- chosen CRT representatives and residues at the fixed primes, 3039–3073;
- multiplier identity and absence of untracked supplementary factors, 3150–3205;
- additive phase decomposition, 3207–3230;
- scalar and gamma-factor normalization, 3284–3449;
- whether the derivative indeed removes every relevant constant mode, including all reduced denominators and fixed twists, 3347–3369.

The source supplies computations for these steps. They need comparison with the precise Kubota/Patterson/Dunn–Radziwiłł normalizations, not acceptance merely because the cited work exists. If this uniformity fails, the quadratic-large-sieve application no longer has row-independent coefficients.

### 4.2 Quadratic large-sieve applicability

Lemma `lem:quadratic` (1886–1913) invokes Goldmakher–Louvel over the Eisenstein field with supplementary characters making the family trivial on units. The conductor and primitive-family conditions, supplementary factors at λ and 2, and removal of S-supported column factors must match that theorem exactly. The source discusses these points, but I did not fetch/reprove the cited external theorem in this subtask.

The proof of the completed bound needs the residual row character χ_{k0}(nb)^3 and every other k0-dependence to be contained in a bounded scalar or a uniformly separated smooth weight (1957–2033). This should be checked as one joint statement with the preceding uniformity lemma.

### 4.3 Exact preimage cancellation in the second Poisson calculation

The first Poisson transformation and enlargement of a nonnegative row sum are detailed at 2273–2349. The second transformation has a particularly important regrouping at 2550–2583: the signed sum over choices p|C,e,w is claimed to give

(1+1_{p|k'})-1_{p|k'}-1_{p∤k'}=1_{p|k'},

forcing f'|k'. That divisibility is then essential to the child column lower bound at 2593–2600 and hence to the induction.

The algebra of the displayed local cancellation checks, but a formal/computer-assisted audit should verify the **complete equivalence of the preimage ranges**, including squarefreeness, coprimality, primary generators, support restrictions and all signs/weights, before taking absolute values. Dropping a nonzero range condition at this step could invalidate the cancellation. I did not identify a specific dropped condition from the supplied text; the proof at 2555–2559 expressly argues that the preimages share a kernel and support.

### 4.4 Uniform estimates versus fixed-character constants

The main theorem proves a universal zero-location statement one character at a time; constants in Proposition `thm:ms` may depend on ν. It does not directly give a numerical uniform bound for the mean square as conductors vary. The arithmetic corollaries at 84–125 require their own stated standard consequences and effectivity checks. Their derivation should not be conflated with the fixed-character analytical constant in the Möbius estimate.

The prime-AP corollary is stated with an absolute effective constant and refers to an explicit-formula argument rather than supplying it in this source. I have not independently certified all the class-number, nonresidue, Miller-test, or idoneal-number corollaries. None is needed to prove the main theorem via the displayed dependency chain.

## 5. Lean status and dependencies

A full text search found **no Lean, Mathlib, formalization, axiom, sorry, or machine-checked-proof discussion** in this 3988-line source. The supplied directory contains only `quasi-oct.tex`, `quasi-sept.tex`, and `siegel.tex`; there are no Lean files or build manifests there.

Therefore this artifact alone does **not** substantiate any claim that the October theorem is machine checked or that it follows from a completed Lean development. A Git blob hash fixes the exact paper text; it does not certify its mathematics.

To audit a repository's formalization, obtain the exact repository commit/tree and inspect, read-only:

- `lean-toolchain`, `lakefile.lean`/`lakefile.toml`, `lake-manifest.json`, imports and Mathlib pin;
- the exact theorem statement and definitions of Hecke/Dirichlet L-functions and the half-plane;
- all assumptions/axioms on the main theorem, including custom axioms for mean-square estimates, theta reflection, large sieves, or analytic continuation;
- `#print axioms` for the exported theorem, every `sorry`/`admit`, and whether the theorem is conditional on a structure bundling the hard estimates;
- whether the checked result is a finite arithmetic identity, the conditional deduction from an estimate, or the entire claimed analytic theorem.

Even a genuinely checked finite descent or conditional nonvanishing deduction would not verify the external theta transformation unless its hypotheses are discharged. Conversely, standard Lean axioms such as classical choice/propositional extensionality should not be mislabeled as unproved number-theoretic conjectures. No such repository-level conclusion can be drawn from the current `.tex` artifact.

## 6. Implications for the user's RH/GRH research plan

1. Keep this fixed-width zero-free theorem distinct from full GRH. If independently validated, it is a substantial arithmetic input for exactly the stated families; it does not prove that all zeros have real part 1/2.
2. It cannot rescue the false equality of modular geodesic lengths with log p. Its proof works directly with arithmetic Möbius sums, residue characters, Gauss sums and theta coefficients; it does not establish the surface-order Fredholm determinant identity.
3. Use its explicit quantitative estimates and parameter ranges as hypotheses where justified. Do not turn “zero free to the right of 11/12” into a self-adjoint zero-spectrum realization.
4. Any improvement to the boundary requires a new quantitative estimate/extraction mechanism. The sixth-power amplifier used here and H=D^{1+θ} explain the 11/12 exponent; recursively applying the existing auxiliary descent does not produce a new zero-free exponent.
5. A rigorous audit priority is the fixed-ray theta reflection/uniformity and exact two-Poisson transfer, followed by the independent formalization dependency graph if one exists. These are concrete tasks, rather than trying to prove an unqualified RH/GRH statement from the paper title.

## Verification limits

Completed: full source coverage, exact blob verification, exponent/scale algebra, matching-domain check, proof-dependency mapping, and searches for formal-proof claims. Not completed: an independent reproof of every external theta/large-sieve result, external bibliographic/source validation, repository-level Lean audit/build, numerical tests, or general RH/GRH certification. No actual contradiction or fatal gap was established in this October manuscript during this pass.
