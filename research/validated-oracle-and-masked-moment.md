# Validated analytic targets and the original-family masked moment

4 November 2026. All production, review, computation and TeX work in this milestone was executed on iska-linux-vscode. Two different mathematical gaps were attempted. Neither implies zero location or completes GRH.

## 1. Fixed, validated completed Dirichlet approximation

For the primitive quadratic characters chi3=(0,1,-1), chi4=(0,1,0,-1), chi5=(0,1,-1,-1,1), define Lambda_q(s)=(q/pi)^((s+a)/2) Gamma((s+a)/2)L(s,chi_q), with a=1,1,0. The primitive theta/Mellin identity with root number 1 is an explicit classical input. Exact Gauss sums fix its normalization; no Artin-holomorphy or zero-location assumption is made.

The new producer encloses the true 64 nodes on the radius-6/5 circle centered at 1/2, for all three targets (192 samples). Integer-only 224-bit outward dyadic rectangles enclose Machin pi, range-reduced logarithms, complex exponentials and degree-24 panel integrals. There are 28 panels, retained n=1..11 and time cutoff 128. Separate exact nonnegative terms account for the omitted-n tail, time tail, Cauchy remainder and every safely discarded complete panel contribution. Domain/type guards apply before discarding; typed caches cannot bypass float rejection. The implementation and derivation are in examples/analytic_oracle and papers/validated-oracle-{core,details}.tex.

A normalized Fourier polynomial P_q(s)=sum c_n ((s-1/2)/(6/5))^n, n=0..28, uses exact rational midpoint coefficients. The specified optimizer value is the closed-form exact 180-step GD iterate with step 1/4 and zero initialization, not an executed optimizer training trace. The sum of five individually upward-rounded terms controls optimization, sample-oracle perturbations, Fourier aliasing, analytic Taylor truncation and coefficient arithmetic. Exact compact-uniform bounds on |s-1/2|<=7/10 are below these upward displays:

| q | Maximum sample radius | Uniform polynomial bound |
|---|---|---|
| 3 | 3.026e-17 | 1.786e-15 |
| 4 | 7.206e-17 | 4.455e-15 |
| 5 | 1.404e-16 | 2.906e-15 |

All three exact uniform bounds are strictly below 5e-15. Growth constants M<4/10/6 are recomputed from exact rational theta bounds, not supplied as guessed floating premises. The immutable evidence is outputs/experiments/2026-11-04-validated-oracle-final-v5/oracle-certificates.json, SHA256 85e3bed76ad4067084ab5f8413b7159e4c5169e5d7cef0469d36164e82dfbca8. Producer source copies and their hashes are included. Earlier pilots and failures remain preserved.

Independent review accepted 843 primitive cases, 1160 exact recurrence identities, 24 negative controls, 192 node/target comparisons, 1536 component checks, 87 coefficient enclosures and 144 compact-boundary diagnostics. The high-precision special-function comparisons are diagnostics. The analytic inclusion argument and exact endpoint/budget arithmetic, not those comparisons, establish the finite certificate. See planning/analytic-oracle/validation-review/VALIDATED_ORACLE_REVIEW.md and outputs/checks/2026-11-04-validated-oracle/review/final-acceptance.json.

Limits: fixed q, precision, n/time cutoffs and degree; not an arbitrary requested tolerance API or all-conductor rate. No new Lean theorem, real-rooted approximation, positive arithmetic operator or GRH result. General infinite-width/readout theorems keep their separate source/initialization hypotheses.

## 2. Original-family AFM input: proved in prose with classical inputs

Let K=Q(omega), O=Z[omega], S fixed, and nu a fixed finite-order Hecke character. Let psi_u be the primitive character of nu times the sextic Kummer character of the actual nonzero element u in O. For H>=1, real t, fixed 0<delta<1/2 and epsilon>0, the independently reviewed derivation gives

    sum_{0<Nu<=H} |L(1/2+delta+it,psi_u)|^2
      <<_{delta,epsilon,nu,S} H^(1+epsilon)(1+|t|)^(1+epsilon).

The sum retains literal element multiplicities, units, S-supported powers, conductor drops and principal rows. Fixed nu is inserted into squarefree column coefficients of the Blomer–Goldmakher–Louvel large sieve, preserving their l2 norm; it is not assumed to belong to the theorem's finite ray-class parameter set. A fixed global S-unit comparison, primitive-character uniqueness, a primitive AFE with dz/z and the fixed-field 2pi normalization, squarefull/sixth-power bookkeeping and a same-family Poisson transfer supply the argument. Principal rows and their pole are separated.

Exact proof and dependencies: planning/analytic-oracle/arithmetic-review/afm-20261104-fixed-twist-final.md; independent adversarial-afm-review-20261104.md. Primary input: Blomer–Goldmakher–Louvel, arXiv:1112.1650v1, Theorem 1.3, Lemma 2.1, Appendix II and the Section 5 method, adapted explicitly. This is not a claim that its corollary directly states arbitrary fixed-twist uniformity. A separately reviewed fixed-unitary extension records the common infinity type and norm twist, including a shifted principal pole; constants depend on the fixed nu and no infinity-type/conductor uniformity in nu is asserted. The extension is not silently folded into the finite-order statement.

Finite consistency checks cover 96 valuation/support decompositions, 94 squarefull coordinates, 7 exponent and 15 Poisson envelope comparisons plus S-smooth summation; independent additional controls are recorded. These are not proofs of the analytic external inputs or new Lean declarations.

## 3. Consequence, surviving loss and next load-bearing claim

For the exact E_u, complete d-dependent masks, independently primitive denominator and actual beta_U in weighted-mellin-transfer-20261104.md, AFM discharges that note's numerator-moment assumption. With U^2<=D the residue-subtracted remainder obeys

    sum_{0<Nu<=H} |E_u|^2
      << M4(W)^2 D^(2delta) U^(2-4delta) H (HD)^epsilon,

with the explicitly stated fixed-character/S/delta dependencies. This is an improved averaged remainder bound, not the complete original signed short-row estimate. The principal residue, short Vaughan term and signed II-I covariance remain unbounded by this theorem. For U=D^a at any fixed a>0, the excess exponent 2delta+(2-4delta)a tends to 2a as delta decreases to zero. Thus repeating AFM or choosing delta small does not close the fixed-positive-power cutoff gap.

Next concrete claim: bound the full original d-weighted numerator moment before Minkowski/absolute summation over d, retaining beta_U, nu(d), chi_d(u), primitive conductor drops and the independently squared denominator/deleted factors; alternatively obtain sufficient signed II-I covariance. Keep all height/profile/scale and conductor uniformities explicit. No new zero-free region, positive determinant identity, Artin holomorphy or GRH scope is established.

## 4. Delivery and formalization boundary

Concise and extended technical-note sources share the reviewed oracle and moment fragments. Their PDF builds use existing pdflatex and existing packages only. Existing full book, native-MathML HTML, source volumes and four historical article PDFs are preserved. Their next integrated rebuild needs the pinned remote book prerequisites; make4ht/latexmk/tikz-cd and Lean4.24 are not currently available on Linux. No package/toolchain installation or fallback axioms were introduced. This milestone does not claim the existing 212-page book or live public web bundle already includes the new interval-oracle/AFM content.

The previously queued exact growth-constant public assets are now verified live (all three q cases, zero browser exceptions). That older publication is distinct from this new interval-oracle experiment. Portfolio pages/hub are completed drafts, still waiting for authorized remote GitHub authentication; no Mac-authenticated publication was performed, no active model data or credentials were read/copied, and no existing project page was modified.

Both project completion gates remain false. Preserve every prior artifact and resume from the actual unresolved d-weighted moment and analytic/categorical Lean interfaces.
