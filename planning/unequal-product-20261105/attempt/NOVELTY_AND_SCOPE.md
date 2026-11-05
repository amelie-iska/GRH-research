# Novelty and scope correction for the unequal-product attempt

5 November 2026. This addendum governs how the preserved attempt is described. It corrects the novelty language in the frozen UNEQUAL_PRODUCT_MOMENT.md and HANDOFF.md; their bytes, their finite checks, and manifest-v1.json remain preserved. Their use of “new partial result” or “new concrete partial bound” must not be cited as a claim of a new analytic advance.

## Prior controlled sector

The earlier proof is research/short-row-high-gcd.md, independently reconstructed in planning/reviews/book/short-row-hybrid.md (§6) and planning/reviews/book/short-row-formal.md (§6). It keeps the exact common-prime zero mask and, for one fixed globally nonnegative radial Schwartz row profile Phi, proves the off-diagonal high-gcd estimate

    |tail with Nh>=G0| <<_(Phi,epsilon) ||W||_infinity^2 D^(2+epsilon)/G0^2.

On the annulus m=hr,n=ht,

    Nq=Nm*Nn/(Nh)^2,
    Nq<=Y implies Nh>=D/sqrt(Y),
    Nh>=2D/sqrt(Y) implies Nq<=Y.

Thus small conductor is high gcd up to fixed endpoint factors. The old proof gives O_(Phi,epsilon)(||W||^2 D^epsilon Y) on Nq<=Y in its fixed smooth scope. Its absolute pair estimate also absorbs r_U(m)r_U(n) or r_U(m) into D^epsilon; these factors are row independent and satisfy the standard divisor bound.

At Y=P^2, P=max(A1,...,A5), on the accepted H=D^(3/4) saturation face P<=D^(1/4), so Nh>=D^(3/4). This is inside the earlier controlled Nh>=D^(5/8) range. The fixed-radial estimate P^2 is stronger than the present R0*P elementary bound, since R0>=P.

## What the present argument does and does not add

The elementary annular pair count O(D sqrt(Y)) is the same high-gcd counting in conductor coordinates. With #B_A=O(R0) and actual factor multiplicities it yields O(||W||^2 D^epsilon R0 sqrt(Y)) directly for the present sharp literal factor block. This is a valid bookkeeping recovery in its stated scope; it is not a newly controlled arithmetic sector or an advance on the low-gcd/common-divisor-one frontier.

The fixed smooth estimate is not silently transferred to a selected sharp off-diagonal piece. That piece need not be positive, and a nonnegative majorant of the complete energy does not provide such a transfer. The elementary sharp-block proof and prior smooth proof have distinct profile hypotheses.

The complete A3 saturation face and near-face slack identity were already accepted in the covariance-budget sources. Local Gauss sums, CRT, Mobius deletion and squarefree lifting are elementary interface algebra; no novelty of those identities is asserted. The purpose of the present attempt is to make their application to the actual forthcoming fourth moment precise:

* The original C-versus-C energy expands in four factor ideals a,b,c,d with (a,b)=(c,d)=1, forcing local exponents 0,+/-1. The two SQUAREFREE products ab,cd have symmetric-difference conductor.
* A generic fourth moment of a length-D column transform has four individually squarefree columns without those internal masks and allows +/-2. The primitive row-j support is {p:j*e_p!=0 mod6}, while the full raw zero set is the whole union. In particular j=3 kills +/-2 oscillation but does not restore its zero.
* Exact DELETE/LIFT/SF-LIFT retain the canceled-prime deletion. Complete-period transforms have Ramanujan factors at those primes.
* On the original long-conductor sector Nq>P^2, every pivot j=1,...,5 and every lifted shorter length is below sqrt(Nq), so elementary favorable smooth completion takes its trivial length term. The original sharp boundary still requires its own Fourier control.

This is the substantive attempted-step analysis and scope correction, not a successful large-conductor bound. The hard target remains the original signed low-gcd sum (particularly h=1), with all factor, row, union and profile restrictions retained.

## Integration targets and preserved development evidence

The requested concise scope-correction proposals are:

    unequal-product-core-proposal.tex
    unequal-product-details-proposal.tex

They contain no SC proposition or purported new analytic book theorem. They state the original-versus-generic fourth-moment interface, full union mask, exact deletion formulas, and the failed completion/known-sector boundary.

The longer initial proposals are preserved in versions/*-long-v1.tex. The longer novelty-qualified v2 proposals are also preserved as *-proposal-v2.tex. They are development evidence, not the selected integration targets. The original Markdown attempt, HANDOFF.md, all v1/v2/v3 checker receipts and manifest-v1.json remain unchanged.

Manifest-v2.json pins this addendum, both selected proposals, the prior sources and the preserved versions. No production/book/web/queue/build/Lean/dependency/environment/cache/GPU/authentication/MCP/publication action was performed by this follow-up. No complete BT_sigma, new full analytic exponent, arithmetic energy lower bound, zero-location result or GRH claim follows.
