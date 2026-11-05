# Independent mathematical review: original weighted cutoff

4 November 2026. Entirely on iska-linux-vscode; no production edits, dependency/environment changes, model/GPU jobs, credential access, publication or Mac writes.

## Accepted: uniform-cutoff all-original-row energy envelope

Read the complete author note UNIFORM_CUTOFF_MOMENT.md, including the actual coefficient recombination, powered/all-ideal BGL input, finite S-unit/ray partitions, literal element multiplicities and principal residue. Verdict: ACCEPTED as a prose application of the named classical large sieve and prior exact contour identity, not Lean or GRH.

The decisive improvement over the first rough proposal is the all-ideal max-first-two pivot. A fixed squarefull block argument gives D sqrt(H), whereas the complete norm factorization and BGL Section3 pivot give D H^(1/3). I independently derived the same bound, and checked the exact source text including its primitive-character warning, Section3 simultaneous powered recurrences and endpoint duality. The author correctly explains why power2 is available from that proof, rather than silently asserting it from a theorem header written for power1.

The proof correctly uses column-indexed primitive characters with squarefree column m, whose outside-S conductor contains every prime of m. Consequently the original sixth-power zero sentinel is retained at a shared prime. Primitive row-indexed characters would lose that zero; the note does not make that substitution. On coprime pairs, finite S-unit and ray-class partitions give fixed column phases, which do not increase coefficient norms. Summing S-supported literal ideals and six units preserves the stated powers; no arbitrary conductor-counting family replacement occurs.

The coefficient norm follows from the exact disjoint convolution and |A_U(m)|<=3^omega(m), uniformly U. Principal rows force every outside-S valuation to be divisible by6, giving O_(K,S)(H^(1/6)) rows, with a fixed-field counting constant retained. Their exact residue bound is O(sqrt(D)||W||infinity log^2(2U)), so P-energy is absorbed by D H^(1/3)(HD)^epsilon under U^2<=D. Taking E=I-P uses an upper triangle inequality; it is not covariance cancellation or a sharper residue theorem.

Accepted conclusion:

    sum_{0<Nu<=H}|E_u|^2
       << ||W||infinity^2 (HD)^epsilon
                       [H + D H^(1/3) + (HD)^(2/3)].

This is uniform in the actual finite U subject to U^2<=D and fixed finite-order nu/S. It combines with the prior AFM remainder envelope by taking their minimum. At H=D^(3/4) the new excess is1/2, improving the earlier small-delta cutoff loss2a only for a>1/4. That is a genuine upper-envelope improvement, not a lower bound, original signed MS3/4 estimate, all-scale supremum or GRH proof. W must be a common profile in the row family; an inside-row profile supremum cannot be inserted after the theorem. The explicit mask, short-term, principal and signed II-I boundaries are accurate.

## Accepted: root exact cutoff and inverse-L boundary propositions

Read the root's weighted-cutoff core/details and current research note. Verdict: ACCEPTED. Grouping squarefree coprime c,d preserves all original zeros and gives A_U=sum_{d|m}beta_U. Each prime has three disjoint placements; this proves the coefficient envelope. All divisors fit when Nm<=U, so A_U=mu(m) there. Rankin with eta=kappa-epsilon gives exactly the stated U^(-kappa+epsilon)[zeta_K(1+epsilon)^3+zeta_K(1+epsilon)] bound, uniform over deleted sets and unitary phases, only for Re s>=1+kappa. The divisor-series equality is over all integral ideals; the squarefree subset is bounded by it.

The Euler packaging with z=psi(p)Np^-s and t=z/(1+z) is correct. At the full untruncated coefficient limit, beta_infinity=mu(d)2^omega gives B=product(1-2t), and F B=1/L^T. The one-prime norm7 negative control is exact: B=3/4, naive square49/64, difference1/64; multiplying by F=8/7 gives6/7 versus7/8. It refutes only the forbidden-overlap simplification, not an infinite mean-square claim.

For fixed nonprincipal primitive psi, each actual J_U is holomorphic in Re>.5: classical nonprincipal Hecke continuation, nonvanishing absolute Euler denominator at2s, and finite1+z factors suffice. A locally uniform limit is holomorphic and agrees with1/L^T in Re>1, so L^T times that limit equals1 throughout the connected half-plane. The implication to zero-freeness is valid. The proposition does not assume or prove the locally uniform convergence, does not assert a converse, and does not derive it from an averaged energy bound. Principal rows are explicitly excluded; no general Artin holomorphy appears.

One nonblocking clarity request was sent to root: explicitly call the tau3 zeta^3 sum a sum over ALL integral ideals, so inherited squarefree notation cannot suggest equality on that subset. No load-bearing correction is needed.

## Evidence and exact limitations

Independent finite checker check_pivot_exact.py passed15625 six-variable dyadic exponent cases, the original H=D^(3/4) exponent comparison and sixth-power sentinel negative control. Its report and checker hash are under outputs/checks/2026-11-04-weighted-moment/review/pivot-exact-controls.json. These are bookkeeping checks, not a proof of BGL or analytic continuation. Primary BGL1112.1650v1 PDF hash1ab29e362c592b9f4078eb85e495ecce6a4665972e6427e7cc2ab0fb214e303b; precise reviewed ranges are recorded in ALL_IDEAL_PIVOT_DERIVATION.md.

The source-hashed acceptance receipt records the reviewed versions. If sources change substantively, this acceptance must be reconciled. No new Lean declaration, determinant positivity, complete original signed mean-square theorem or GRH proof is supported by this review.


## Literal TeX acceptance

Read both complete author TeX fragments (114+183 lines) after the Markdown proof, including every stated hypothesis, displayed estimate and mask statement. ACCEPTED without a load-bearing correction. Exact squared-norm coefficients, simultaneous powered endpoint/duality, max-first-two monomial inequalities, fixed-field/S-unit multiplicities, original column-conductor zero orientation, principal count and MIN exponent are consistent with the accepted derivation. The theorem explicitly has a single common smooth W, U^2<=D, fixed finite-order nu/S and no hidden locally uniform cutoff premise. Its quantitative conclusion remains a losing upper envelope, not the signed target or GRH. Existing theorem/amsmath/hyperref syntax suffices; no package/custom-macro or missing lemma/proposition environment is introduced. Parent will separately compile/inspect layout.

Reviewed source hashes are in outputs/checks/2026-11-04-weighted-moment/review/tex-acceptance.json. If copied byte-for-byte to production, this acceptance transfers to those identical bytes; substantive edits require reconciliation.
