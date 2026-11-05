# Independent audit of the cube-factor quadratic pivot

Date: 2026-11-05. Verdict: **approved**, with the explicit scope below. This is a classical analytic consequence of the pinned Goldmakher--Louvel theorem and the previously established exact literal-to-canonical comparison. It is not a new large-sieve theorem, a complete signed covariance estimate, a Lean theorem, or a global exponent improvement.

## Precise statement

Fix K=Q(omega), a finite set S containing all primes above 6 and the fixed comparison moduli, and fixed finite-order nu. Let A_j,D,H >= 1, R0=product_{j=1}^6 A_j, and product A_j^j <= H. Columns m are squarefree integral ideals prime to S in D <= Nm <= 2D. Let (b_m) be any fixed complex coefficient sequence on those columns, independent of the variable row; it may contain the actual mu, nu, W and the cutoff/factor-count weights.

Use the unique valuation decomposition of the outside-S row ideal into r1 r2^2 r3^3 r4^4 r5^5 r6^6. Only r1,...,r5 are squarefree and pairwise coprime. The ideal r6 is arbitrary and may overlap any of them. Use primary generators for the good ideals. Retain every literal unit and S-supported factor, and retain all original residue-symbol zeros.

For the block with A_j <= Nr_j < 2A_j, first fix a literal unit and an S-supported factor. The unnormalized row energy satisfies

    sum_{admissible rows in this fixed block} |sum_m b_m chi_m(u)|^2
      <= C_(K,S,epsilon) (HD)^epsilon
         [R0 + D R0/A3] sum_m |b_m|^2.

Hence the actual raw Gram has operator norm

    Lambda_A <<_(nu,S,epsilon) (HD)^epsilon [R0 + D R0/A3].

The constant is uniform in the frozen row factors, the coefficients, H,D,A_j and the literal unit/S-factor. It depends on the fixed comparison modulus and finite partitions, and the displayed nu-dependence is harmless. All dyadic annular comparison constants are fixed. If the S-supported factor is subsequently summed, its contribution must be summed with the actual reduced capacity H/Nb as in the existing all-literal-row argument; the statement is not permission to multiply by the unweighted number of S-factors.

## Proof: the original zero extension is the correct orientation

Freeze all r_j except r3, and fix the literal unit and S-factor. Write u=F r3^3. Exact multiplicativity in the numerator of the raw symbol gives

    chi_m(u) = chi_m(F) chi_m(r3)^3.

This equality holds at collisions: if m meets F or r3, the appropriate factor is zero. Put c_m=b_m chi_m(F); then sum |c_m|^2 <= sum |b_m|^2. This is a coefficient sequence independent of r3. In particular the arbitrary sixth-power factor contributes

    chi_m(r6^6) = 1_{(m,r6)=1},

not the constant 1. If a prime divides both r3 and r6, this remains a fixed coefficient mask as well as a possible raw quadratic zero. **No restriction (r3,r6)=1 is introduced.**

The coprimality of r3 with r1,r2,r4,r5, the exact row capacity, and any original fixed row subset are restrictions on the outer pivot sum after the other factors are frozen. Its terms are nonnegative, so those restrictions may be removed at that point. The only variable row-column collision mask left is the one already in the raw character chi_m(r3)^3. No arbitrary simultaneous mask is discarded.

## Fixed S phases: why the finite family issue does not break the proof

Apply the already proved equation wc:literal-reciprocity to the primary generator of r3 itself, rather than to the whole powered row:

    chi_m(r3) = eta_(r3)(m) C([r3],[m]) vartheta_m(r3).

Here eta_(r3) ranges over the fixed finite S-unit Kummer twist set, and [r3] ranges over the fixed finite reciprocity group. Both m and r3 are good squarefree ideals. Cube the exact equality, including its collision zeros. Partition the pivot rows by the pair (eta_(r3),[r3]). For each part,

    chi_m(r3)^3 = d_m vartheta_m(r3)^3,
    d_m = eta(m)^3 C(g,[m])^3,

where d_m is a fixed modulus-one column multiplier. Thus the coefficient sequence c_m d_m is independent of the pivot row and has the same squared norm as c_m. Enlarge the nonnegative row sum in each part to all squarefree good ideals of norm <= 2A3. The number of parts is fixed independently of all scales and frozen factors. Sum the finitely many resulting estimates.

It would be invalid to absorb an arbitrary row-dependent phase into coefficients. The finite partition is the reason that step is valid here. Applying the comparison to r3 rather than the full row also avoids an unnecessary question about the varying class of F r3^3.

## The exact external input and its conductors

Pinned primary source: Goldmakher--Louvel, *A quadratic large sieve inequality over number fields*, arXiv:1112.1642v2, Definition 1, Remark 3, Theorem 1.1 and especially Corollary 1.2, PDF pages 1--2. The preserved PDF SHA256 is 5cc5f03388d3996b4333f07be51f989f60779fe172f8bd24c7aa6ddad64dd304.

Corollary 1.2 explicitly treats an n-th order Hecke family for even n and its n/2 power. Taking n=6 gives, in exactly the needed column-indexed orientation,

    sum_{a squarefree good, Na<=M}
      |sum_{m squarefree good, Nm<=N} z_m vartheta_m(a)^3|^2
      <<_(K,c,epsilon) (MN)^epsilon (M+N) sum_m |z_m|^2.

The family's characters are primitive of trivial infinite type; its finite reciprocity group and same-class primitive-product property are the hypotheses in Definition 1. These are those of the accepted canonical sixth-order family used in wc:literal-reciprocity. Remark 3 / Corollary 1.2 provide the quadratic family, so no inference from a count of arbitrary conductors is required.

More concretely, for squarefree m, at every p|m outside S, the local tame sextic character has order six. Its cube has order two, is nontrivial, and has conductor exponent one (residue characteristic is odd). Thus the primitive cubic power has outside-S conductor exactly m. Its S-part is among finitely many conductor types controlled by the fixed local comparison modulus. This is sufficient for the comparison's zero extension: if (m,a)>1, vartheta_m(a)^3 is zero, exactly as the original chi_m(a)^3. No global formula for the entire conductor, and no deletion of its fixed S-part, is needed. Fixed nu belongs to the coefficients and is not asserted to define a varying member of the GL family.

Both indices are squarefree **ideals**. There is no hypothesis that their rational norms are squarefree. Inert prime ideals of norm p^2 and squarefree ideals containing both split primes over p remain permitted. The unit ideal is permitted; bounded dyads use M,N>=1. Put M=2A3,N=2D to obtain (A3 D)^epsilon (A3+D), with fixed factors absorbed.

## Frozen count and normalization

For each frozen j != 3 there are O_K(A_j) ideals in its dyad, including arbitrary r6. Removing pairwise-coprimality constraints only enlarges this count, so there are O_K(R0/A3) frozen choices. Sum the pivot estimate, using the common coefficient-square bound each time:

    (A3 D)^epsilon (R0/A3)(A3+D) sum_m |b_m|^2.

Since A3<=H and D,H>=1, enlarge its small loss to (HD)^epsilon. This proves the stated block norm. The factor six for all literal units is fixed. There is no additional variable conductor factor or cardinality of ray classes depending on the frozen row.

This is an unnormalized Gram bound. When b_m includes D^(-1/2), that normalization belongs to sum |b_m|^2; it must not be counted twice. Since the theorem allows arbitrary fixed b_m, it applies separately to the actual mu, A_U, r or sqrt(r) coefficient vectors whenever their column norms are the ones used in the existing covariance proof.

## Comparison and the precise limitation

The previously accepted powered-BGL bound, with M=max(A1,A2), is

    (HD)^epsilon [R0 + D R0/M + D^(2/3) R0/M^(1/3)].

The new quadratic pivot can be combined with it by taking the minimum. On the old saturated face A1=A2=A, A3=B, A4=A5=A6=1, AB=H^(1/3), it gives

    R0 + D R0/B = A^2 B + D A^2,

whereas the old middle monomial is DAB=D H^(1/3). When B>A it improves that monomial by the factor B/A. A strict power gain needs B/A to grow as a fixed positive power of the asymptotic scale; B>A by a fixed constant is only a constant-factor gain. The common R0 term is unchanged, so an improvement of one monomial is not an unconditional power improvement of the total bound at arbitrary H,D.

At H=D^(3/4), write A=D^a and B=D^(1/4-a), 0<=a<=1/4. In the A3-dominant part 0<=a<1/8, the old leading exponent is 5/4 and the quadratic bound's leading exponent is 1+2a<5/4. It remains above the target exponent 3/4, even at a=0. At a=1/8 the leading exponent is still 5/4. For B<=A (a>=1/8), the old estimate remains available and the combined bound still has leading exponent 5/4. Thus **no global exponent improvement or BT_sigma conclusion follows**. A fixed-neighborhood gain around the complete former face is not supplied.

GL already states the sixth-family cube estimate explicitly. This application may refine the project's previous envelope, but it should not be called a new quadratic large sieve or assumed absent from the literature. This review makes no literature-priority claim.

## Verification and preserved state

Read in full: papers/{covariance-budget,uniform-cutoff-moment,masked-moment}-{core,details}.tex and planning/reviews/book/short-row-hybrid.md. Also checked the exact imported GL interface at the protected source paper's quadratic-norm subsection and its primary-generator/fixed-S conventions. Read the pinned GL PDF extraction through its family construction (PDF pages 1--5), including the exact theorem/corollary and conductor discussion. Source hashes and exact rational exponent-face comparisons are recorded in the sibling output JSON. These checks support bookkeeping and source binding; they do not reprove GL analytically.

All writes for this independent review are confined to new review-quadratic directories. No production source, dataset, environment, cache, publication, authentication or dependency configuration was changed. No Lean or production suite was run. The unrelated Lean feasibility result is in a separate note in this directory.
