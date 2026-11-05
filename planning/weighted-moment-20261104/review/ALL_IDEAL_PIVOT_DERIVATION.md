# Independent all-ideal pivot derivation for the weighted family

4 November 2026. Remote-only. This is an original-family application of the explicitly named classical BGL large sieve, not a proof of that external theorem, new Lean formalization or GRH. It refines the first D sqrt(H) direct envelope to D H^(1/3).

## Exact input and a warning about primitive conventions

Primary source: Blomer–Goldmakher–Louvel, arXiv:1112.1650v1, PDF SHA256 1ab29e362c592b9f4078eb85e495ecce6a4665972e6427e7cc2ab0fb214e303b. Read Theorem1.3, Lemma2.1, Section3 definitions of B1^j/B2^j, Lemma3.4 and its equations(3.6)–(3.9), Section3.2, and AppendixII. Cached primary text/PDF are preserved under planning/analytic-oracle/arithmetic-review/adversarial-sources/. No duplicate PDF needs publication.

BGL's Section3 proof establishes the squarefree large-sieve estimate for powers j=1,..,5 of the sextic family; j=3 uses its quoted quadratic result, and the other powers proceed through the recursive argument. The all-ideal pivot below only requires powers1 and2. It is not necessary to insert arbitrary primitive characters of comparable conductor into Theorem1.3.

Crucially, BGL's row-indexed chi_a is the underlying primitive character. If a is a sixth power, chi_a is trivial even at primes dividing a (explicit warning on p5). The original symbol (u/m)_6 remains zero if a column prime divides u. A proof must not silently identify those two arrays on noncoprime pairs.

Instead, use the COLUMN-indexed primitive character chi_m evaluated on the original outside-S row ideal a. The column m is squarefree, so its outside-S conductor is exactly m. Hence chi_m(a)=0 whenever (a,m)>1, including sixth-power rows. For coprime pairs, the already proved finite S-unit comparison followed by BGL reciprocity identifies the literal symbol with chi_m(a), multiplied by fixed column factors after a finite S-unit/ray-class partition. Both sides are zero on noncoprime pairs. Units and S-supported powers are then restored with their literal multiplicities. All fixed factors have modulus at most one; no desired positivity is used.

## All-ideal large sieve

Let lambda_m be any finite complex sequence on squarefree ideals m prime to S with Nm<=N. After a fixed finite class partition consider

    sum_{Na<=H, a prime to S} |sum_m lambda_m chi_m(a)|^2.

Decompose a uniquely as a1*a2^2*a3^3*a4^4*a5^5*a6^6, with a1,..,a5 pairwise coprime squarefree ideals and a6 arbitrary (overlap between a6 and other factors is permitted). Split the six norms into dyadic blocks A_j. Set R=prod A_j and M=max(A1,A2), and choose ell=1 or2 realizing M. For fixed other five row factors h, the inner polynomial is

    sum_m lambda_m chi_m(h) chi_m(a_ell)^ell.

Its coefficient squared norm is at most sum_m |lambda_m|^2. The exact chi_m(h) contains every original shared-prime sentinel, including chi_m(a6)^6=0 at a shared prime; never replace that expression by1. The required pairwise coprimality restriction on a_ell is a subset of the positive outer row sum and may be enlarged only in the inequality. Reciprocity, finite class partition and the squarefree power-ell large sieve bound the block by

    (HN)^epsilon * (R/M) * [M+N+(MN)^(2/3)] * sum |lambda|^2.

For A_j>=1 with prod A_j^j<=H, direct monomial comparison gives

    R<=H,
    R^3<=H M^3,
    R^3<=H^2 M.

For the second inequality, R^3/H=A1^2*A2/(A4*A5^2*A6^3)<=M^3. For the third, R^3/H^2=A1/(A2*A3^3*A4^5*A5^7*A6^9)<=M. Fixed factors2 from dyadic endpoints are harmless. Therefore the full all-ideal energy is bounded by

    (HN)^epsilon [H+N H^(1/3)+(HN)^(2/3)] * sum |lambda|^2.

There are only O(log(2H)^6) dyadic blocks; they are a disjoint positive outer row sum, and their count is absorbed in H^epsilon. This is also the explicit consequence of BGL Lemma3.4's max-first-two pivot. It is stronger than bounding each squarefull block with the same squarefree variable, which loses N sqrt(H).

For original rows, an S-supported ideal b and each unit/class choice contributes the same bound with H/Nb. The sums of (Nb)^(-1), (Nb)^(-1/3), (Nb)^(-2/3) over a FIXED finite S-supported monoid are convergent Euler products. Thus the same H exponents hold for all actual Eisenstein elements, with constants depending on S and the finite class choices. No row quotient or arbitrary conductor-counting replacement has occurred.

## Application to actual cutoff coefficients

For squarefree m define A_U(m)=sum_{d|m} beta_U(d), with the project's actual disjoint truncated Mobius convolution beta_U. The exact original smoothed type-I expression is

    I_u=D^(-1/2) sum_{m squarefree,(m,S)=1} A_U(m) nu(m) (u/m)_6 W(Nm/D).

This follows by combining c*d=m in the original full-mask series: c,d are squarefree and coprime, and original (u/m)_6 zeros retain all gcd deletions. It is not a replacement of the primitive square denominator by its zero-sentinel square. Every summand before recombination agrees in Re s>1, and smoothing is finite.

The combinatorial bound |A_U(m)|<=3^omega(m) is uniform U. Since tau3(m)=3^omega(m) for squarefree m, standard divisor bounds and the fixed-field ideal count give

    sum_m |D^(-1/2)A_U(m)nu(m)W(Nm/D)|^2
       <<_epsilon ||W||_infinity^2 D^epsilon.

Use N=2D in the all-ideal large sieve. The fixed nu is a coefficient multiplier on m prime to S and has modulus1. It follows that

    sum_{0<Nu<=H} |I_u|^2
      <<_{nu,S,epsilon} ||W||_infinity^2 (HD)^epsilon
                            [H+D H^(1/3)+(HD)^(2/3)].

For the residue P_u, a principal primitive nu*kappa_u forces every outside-S row valuation to be a multiple of6. Therefore the literal principal-row count is bounded by

    C_K H^(1/6) prod_{p in S}(1-(Np)^(-1/6))^(-1),

where C_K includes six units and the fixed-field ideal counting bound.

The retained residue formula gives |P_u|<<sqrt(D)||W||_infinity log^2(2U). For U^2<=D, its energy D H^(1/6)log^4(2U) is absorbed by the D H^(1/3) term with a small D loss. Consequently the same U-independent envelope applies to the exact residue-subtracted E=I-P. This uses an upper triangle inequality, not signed covariance cancellation.

## Surviving loss and review limits

At H=D^(3/4), the dominant new envelope is D H^(1/3)=D^(5/4), leaving excess D^(1/2) over H. It improves the previous small-delta H U^2 envelope only when U=D^a with fixed a>1/4; in other regimes one keeps the minimum of the two valid bounds. The exponent1/2 is an upper-envelope loss, not a lower bound or counterexample to a sharper true estimate. The all-epsilon original signed low-gcd bound, principal/short/type-II covariance and positive arithmetic determinant bridge remain open.

Finite exponent/sentinel checks: check_pivot_exact.py, report outputs/checks/2026-11-04-weighted-moment/review/pivot-exact-controls.json. 15625 six-variable dyadic exponent cases pass. These test bookkeeping only and do not prove BGL, reciprocity or the analytic moment theorem. No new Lean declaration is made.


## Explicit power-two endpoint of the cited proof

Theorem1.3's header uses the unpowered family, but Section3.2 proves its norm recurrence simultaneously for the finite powers j=1,..,5, as required because Lemma3.4 replaces j by j*ell modulo6. For j=3 the source invokes the stronger quadratic large sieve; all other j use the displayed recursion. The resulting E_(4/3) estimate, with arbitrarily small losses, and equation(3.10) give

    B1^j(M,N) << (MN)^epsilon [M+N^(5/3)M^(-1/3)+(MN)^(2/3)].

When M>=N, the middle term is at most (MN)^(2/3); when M<=N, reciprocity/duality equation(3.2) applies the same bound with M,N reversed. Thus B1^2 has the required M+N+(MN)^(2/3) bound too. This explicitly uses the proof's power-j statements; it does not misquote the theorem header as separately stating power-two canonical-family equivalence.
