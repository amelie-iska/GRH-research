# Independent adversarial mathematical review

Date: 5 November 2026. Reviewer: family_obstruction subagent. Verdict: PASS for the new ordinary-conductor block estimate and the combined unsigned envelope, as prose mathematics with classical elementary Gaussian Poisson and finite character facts. No Lean or GRH result is established. This review does not authorize production integration or publication.

I derived the ordinary conductor large-sieve route and the face improvement independently before receiving the parent's candidate formula. I then read the complete draft and directly reread GL Definition 1 and BGL Lemma 2.1 in the pinned remote text sources. The following are adversarial checks of the actual new argument, not an endorsement inferred from its finite checker.

## Character and zero-mask audit

BGL Lemma 2.1 states that the canonical character of a sixth-power-free ideal has trivial infinity type and primitive conductor between its squarefree kernel q and c q for a fixed c. Its fixed-S comparison with the literal Kummer character preserves this conductor bound. For v=product(r_j^j), 1<=j<=5, all outside-S valuations belong to {1,...,5}; hence every outside-S prime in q occurs in the primitive conductor. On good column ideals, the primitive value therefore equals the literal symbol even at collisions: both are zero. The sixth-power factor is excluded from v and its original mask 1_(m,r6)=1 remains in the coefficients. This is essential and is correctly done; allowing r6 to overlap the other factors causes no problem. No row-dependent phase is silently put into a common coefficient sequence.

The safe bound 5^omega(q) for tuple multiplicity is valid without proving injectivity. A primitive character determines its outside-S conductor q. Each prime in q can be assigned to exactly one of the first five factors, with at most five choices. The finite-small-prime divisor argument bounds this multiplicity by C_eta (Nq)^eta. All fixed-S wild conductor types lie among conductors dividing c_S q; their norms are therefore uniformly bounded by C_S Nq. They need no distinct ad hoc large-sieve treatment. On the three-factor face, inertia orders6,3,2 do identify the three factors, although the general proof correctly does not need this stronger observation.

## Ordinary multiplicative large-sieve audit

The class-number-one assumption is used legitimately. A chosen generator alpha_m of each ideal column has |alpha_m|^2=Nm, giving an injective element support in a fixed lattice disk of radius O(sqrt D). Nonsquarefree rational norms of squarefree ideals are allowed. Finite-order Hecke characters have trivial infinity type here. On this class-number-one field, primitive such characters form a unit-trivial subset of primitive multiplicative characters of O/f. If the finite residue character descended to a proper divisor of f, its unit-triviality would descend as well, contradicting primitive Hecke conductor minimality.

For every primitive character modulo f, the Gauss expansion is valid for all alpha, including nonunits, and its Gauss sum has squared magnitude Nf. After dividing squared expansions by Nf, enlarging from primitive characters to all characters of (O/f)^* gives exactly the factor phi(f)/Nf, which is at most one. There is no missing factor phi(f), Nf, or square root in the claimed normalization. Including all multiplicative characters at this intermediate step is legitimate even though some are not unit-trivial, since the sum is positive. The unit ideal contributes its primitive principal character and the single frequency0.

Reduced fractions x/f modulo O have an intrinsic denominator ideal. Equal reduced fractions force the same denominator ideal and the same residue numerator. Different fractions with conductor norms at most Q have a nonzero Eisenstein numerator after subtraction and denominator modulus at most Q, so their torus separation is at least c/Q. Fixed different/codifferent factors only change constants. This remains true for prime powers in wild fixed-S conductors, since reducedness means x is a unit modulo the full conductor ideal, not merely modulo its radical.

The additive inequality has a complete proof: majorize the lattice box by a Gaussian, expand the dual quadratic form, apply two-dimensional Gaussian Poisson, and bound the absolute kernel row sums by packing lifted separated frequencies. The row sum is O(N^2+delta0^(-2)); Schur and finite-dimensional duality yield the displayed additive bound. With N comparable to sqrt D and delta0 comparable to Q^(-1), the constant is O(D+Q^2), independent of the number of moduli or frequencies. This validates the ordinary all-primitive-character bound without any higher-order-family reciprocity assumption.

## Block, global envelope, and remaining gap

For fixed r6 and fixed literal unit/S factor the coefficient sequence is independent of all five variable factors and its squared norm is at most the original coefficient norm. Applying the all-character inequality with Q=A1 A2 A3 A4 A5 and paying the subpower tuple multiplicity gives D+Q^2. Ideal counting over the arbitrary r6 gives the stated D A6+R^2/A6 block bound. Enlarging the positive outer row sum discards only restrictions; it does not discard a coefficient mask.

I independently checked the universal interpolation. Let S=R/M. The exact capacity gives R S=R^2/M<=H: if M=A1 the logarithmic slack is x3+2x4+3x5+4x6; if M=A2 add x2-x1. Also R<=H, A6<=H^(1/6), and the accepted cross term T<= (DH)^(2/3). The elementary inequality

    min(R+DS+T, D A6+R^2/A6)
      <= R+T+D A6+min(DS,R^2/A6)

is valid. The last minimum is at most min(DS,H^2/S^2), hence at most (DH)^(2/3). Therefore the all-row envelope H+D H^(1/6)+(DH)^(2/3), up to a fixed multiplicative constant and arbitrarily small powers, follows. Dyadic summation and the fixed-S factor sum use convergent geometric powers1,1/6,2/3. For the actual normalized coefficients, the existing uniform divisor norm and principal-residue estimate are sufficient; the latter matches D H^(1/6), so the same envelope for E follows with smaller internal epsilons.

At H=D^(3/4), the new upper exponent is7/6. The old balanced saturation face has Q<=D^(1/2), hence raw energy O(D^(1+eps)) on its entirety. The new envelope witness (5/12,1/6,0,0,0,0) correctly gives both old middle term and ordinary-conductor square term exponent7/6, with cross term10/9. This is only saturation of available upper bounds. The remaining target gap is5/12 in the exponent; no signed cancellation, covariance, zero-location, or GRH conclusion follows.

## Direct BGL substitution boundary

The draft correctly distinguishes the proved ordinary conductor comparison from an unproved BGL-shaped mixed-family estimate. Radical q alone does not choose a unique mixed character. After the original fixed reciprocity phases, the proposed mixed reciprocity quotient is chi_b(a')/chi_a(b'), a variable outside-S factor. Thus the existing fixed S/ray partition does not verify GL Definition 1(2). This does not prove that no alternative sheet construction or stronger mixed large-sieve theorem can exist; the new result does not require either claim.

No mathematical correction is required before retaining this as a fresh research attempt. No production source, toolchain, dependency, protected history, or prior output was changed by this reviewer. Only this new review file was written through the remote SSH session.

Reviewed draft SHA256: 140a48e81f4ad00af99bd76afb71342311823f592833d784e60ac0e21378d0e1
