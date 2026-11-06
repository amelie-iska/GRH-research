# New exact formal HB checks — PASS

This is synthetic formal squarefree-ideal Dirichlet algebra, not original character/Gauss/family data, interval arithmetic or Lean. Eight DISTINCT symbols have norms7,7,13,13,19,25,31,37. Equal rational norms never merge ideal symbols; in particular the two norm7 symbols give a squarefree formal target of norm49.

Nine material choices of 2D are4,22,94,1042,8194,1000000,7^5,13^5,2^65. Membership in the truncated Mobius function is the exact integer comparison (Na)^5<=2D, with no floating root; the two odd fifth-power cases exercise an exact closed cutoff tie. All256 SF subset coefficients were checked for each case,2304 case-coefficient equalities in total. The847 entries whose target norm is<=2D also satisfy the J5 truncation WITHOUT the remainder.

The omitted remainder is checked by support rather than cancellation alone: every nonzero mu-M factor has norm at least n0 with n0^5>2D. Five such factors therefore already have product>2D; the four extra constant-one factors cannot reduce it. Nonzero remainders outside the target are retained in the saved ledger.

A meaningful negative control replaces J5 by J4 with THE SAME fifth-root cutoff. At D500000, each of19,25,31,37 is above that cutoff, while their product544825<=1000000. The true target coefficient is+1, the wrongly truncated coefficient is-23, and the omitted four-factor remainder is+24. Three target entries fail if that remainder is discarded. This is an expected synthetic support failure, not a failure of the accepted J5 proof.

A separate exact scale check covers2184 synthetic lower-scale boxes at D=2^64,2^72,2^80 and HB j=2,3,4,5, with the corresponding at-most-nine factor flags. A fixed-index scale-only greedy/midsize grouping agrees with an independent exhaustive subset search in every box:1786 balanced and398 unbalanced. Every unbalanced long factor is unrestricted, under the explicit D>=2^64 validation domain. A smaller-D call is rejected by that domain guard; no theorem of failure at all smaller D is asserted.

All comparisons against cube-root thresholds use integer cubes. After grouping,4368 independently selected per-coordinate norm samples preserve the group and obey the exact macro cubed bounds. Samples need not satisfy the original common-profile support and are not actual ideal samples; their purpose is to ensure the grouping never consults actual factor norms. Seed2026110609 and all scale-generation parameters are saved.

Executed once using stdlib Python at nice15, exit0. No dependency/environment change, old control replay, production source/index change or numerical arithmetic-family claim. These checks support the new algebra/grouping derivation; the independent mathematical proof review remains its separate authority. The long TypeI remainder and complete small-cutoff model remain unestimated.
