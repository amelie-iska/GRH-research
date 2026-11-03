# Inert-prime obstruction on the same real theta carrier

Independent read-only audit, 2026-11-03. No shared files or outputs were modified. This is an elementary restricted no-go theorem and an explicit complex replacement; it is not a no-go theorem for Hilbert–Polya constructions generally.

## Hypotheses and geometric reason for the intertwining relation

Retain the actual rational theta H1 basis b0=e0-e1,b1=e1-e2, with

C=[[0,-1],[1,-1]], C^2+C+I=0,
G=[[2,-1],[-1,2]]>0.

Here C is the order-three deck rotation. For a good odd prime power q with characteristic different from3, q congruent-1 modulo3, the q-power Frobenius conjugates that deck action to its inverse. On curve points F sigma=sigma^q F. The contravariant pullback relation is equivalent to the same inversion condition because inversion has order two. Thus any proposed Frobenius operator M on this carrier must satisfy

M C=C^2 M.

Cubing is bijective on F_q, so the elementary count on E_d:y^2=x^3-d, d nonzero, gives a_q(d)=-sum_x eta(x^3-d)=0. The genuine elliptic Frobenius therefore has characteristic polynomial X^2+q, and det(I-TF)=1+qT^2. The determinant is positive q, independent of any positivity argument for the chosen real model.

The restricted proposal under audit asks simultaneously for: (i) this same two-dimensional real carrier, (ii) the displayed real deck action, (iii) a real-linear M intertwining by inversion, and (iv) determinant q>0. These four requirements are incompatible.

## Complete elementary proof

Write M=[[a,b],[c,d]], with real coefficients. Direct multiplication gives

MC=[[b,-a-b],[d,-c-d]],
C^2M=[[-a+c,-b+d],[-a,-b]].

Equality forces c=a+b and d=-a, with no other restrictions. Therefore

M=[[a,b],[a+b,-a]],
trace(M)=0,
det(M)=-(a^2+ab+b^2)
      =-[(a+b/2)^2+3b^2/4] <= 0.

Equality holds only for M=0. Thus det(M) can never be q>0. Every nonzero real anti-CM map is orientation reversing, whereas the genuine weight-one Frobenius determinant is positive. This proof needs no cohomological conjecture, no classification of all elliptic endomorphisms and no metric hypothesis.

The same obstruction is basis independent: any irreducible real order-three action is real-conjugate to C or its inverse. Simultaneously changing the basis of C and M leaves determinants unchanged. Merely choosing a different real basis or real lattice does not repair it.

There is an even sharper metric identity:

M^t G M=(a^2+ab+b^2)G.

So positive real anti-CM similitudes of scale q certainly exist, but their determinant is **-q**, not q; their characteristic polynomial is X^2-q and their eigenvalues are real +/-sqrt(q). The positive metric alone does not supply the correct inert arithmetic polynomial. Conversely a real matrix with characteristic polynomial X^2+q exists, but it cannot satisfy this deck inversion relation. It is the conjunction of hypotheses that fails.

## Explicit complex replacement

Set K=[[1,-1],[0,-1]]. Exact multiplication gives

K^2=I, detK=-1, traceK=0,
KC=C^2K,
K^t G K=G.

On the complexification define F=i sqrt(q) K. Then

FC=C^2F,
F^2=-qI,
traceF=0, detF=q,
F^* G F=qG,
det(I-TF)=1+qT^2.

Here star is conjugate transpose. All these identities hold with the same fixed positive Hermitian form G; they are ordinary finite-dimensional linear algebra. F is sqrt(q) times a G-unitary and has eigenvalues +/-i sqrt(q). Its entries are not real, and this is not a rational, integral or canonically identified Tate-lattice construction. The two choices of the square-root sign are model choices; no canonical arithmetic comparison follows from checking the characteristic polynomial alone.

There cannot even be some alternative two-dimensional real structure commuting with both C and F: restricting to its fixed real plane would recreate the proved obstruction. However a quaternionic structure is available. Put J=2C+I. Then J^2=-3I, JC=CJ and JK=-KJ. The anti-linear operator

A=(J/sqrt(3)) composed with coefficient conjugation

satisfies A^2=-I, AC=CA and AF=FA. It is antiunitary for G, because J^t G J=3G. Thus the complex carrier naturally supports a quaternionic odd structure, which has no two-dimensional real fixed space. This is a concrete explanation for why complexification avoids the real obstruction.

Realifying this complex two-dimensional model gives four real dimensions, not the original two. Its real characteristic polynomial is (X^2+q)^2 and its real determinant is q^2. That operation alone doubles the desired local multiplicity; recovering one arithmetic factor would need another justified determinant construction.

## Relation to the primary literature and exact limitations

[Deninger, There is no Weil-cohomology theory with real coefficients for arithmetic curves, arXiv:2204.02714v2](https://arxiv.org/pdf/2204.02714v2), 27January2023, Section1 pp1–2, recalls Serre's supersingular finite-field obstruction: functorial real H1 of dimension two would require a quaternion algebra action through M2(R), which is impossible. It then describes an R-linear target with complex vector spaces and an anti-linear operator squaring to-1 in odd degree. The elementary matrix calculation here exhibits this mechanism using only the CM rotation and inert Frobenius relation; its quaternionic complex replacement is compatible with that discussion. The paper's separate arithmetic-curve argument is not needed or claimed as a corollary of this calculation. This was a focused read of Section1, not a fresh full eight-page proof audit.

The determinant-q and local polynomial identification are classical elliptic curve statements; the previous theta descent report cites the exact primary Milne endomorphism/Tate/zeta results. These statements concern good finite-field factors. They do not establish a number-field purity theorem, conductor calculation, global determinant or GRH.

This result does not contradict actual l-adic or crystalline cohomology: those coefficient fields do not carry the real positivity argument used to make a^2+ab+b^2 nonnegative. It does not rule out larger real spaces, complex or quaternionic targets, semilinear/crystalline structures, singular or completed categorical models, noncommutative determinants, or independently constructed infinite-dimensional Hilbert–Polya realizations. Each such replacement must state its comparison and multiplicity hypotheses. It specifically rules out extending the split-prime **same real two-dimensional deck-equivariant carrier** to the inert factors with the demanded determinant.

## Independent checks

No random seeds or numerical approximations were used. Exact integer checks for all361 pairs a,b in[-9,9] verified the anti-CM relation, negative norm determinant, and G-similitude formula. Separately checked K's inversion, involution and G-orthogonality. The displayed coefficient equations supply the universal proof beyond those diagnostics. The complex replacement follows symbolically from i^2=-1 and the checked K identities; no shared checker was edited.
