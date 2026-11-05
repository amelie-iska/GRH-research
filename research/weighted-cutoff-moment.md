# Exact weighted-cutoff recombination and its convergence domain

4 November2026, remote-only continuation of the validated-oracle/AFM frontier. This note attempts the actual d-weighted expression before absolute summation. The unweighted numerator AFM theorem was already finished and is not repeated.

For T0=S union support(u), define J_u,U(s)=sum_sf d beta_U(d)nu(d)chi_d(u)Nd^-s F_u,d(s), with every original zero and independently primitive square denominator retained. On Re s>1, grouping m=dc gives J=sum_sf m,(m,T0)=1 A_U(m)psi_u(m)Nm^-s, where A_U(m)=sum_{d|m}beta_U(d)=sum_{ab|m,(a,b)=1,Na,Nb<=U}mu(a)mu(b). Thus |A_U|<=3^omega, and A_U(m)=mu(m) for Nm<=U. This is a disjoint-support convolution, not an unconstrained square.

For kappa>0 and0<epsilon<kappa, the uniform absolute-half-plane theorem is

    sup_{Re s>=1+kappa} |J_u,U(s)-1/L^T0(s,psi_u)|
      <= U^(-kappa+epsilon) [zeta_K(1+epsilon)^3+zeta_K(1+epsilon)].

Proof: all differences lie above normU; Rankin with exponentkappa-epsilon and the ideal triple-divisor series zeta^3 dominate them. Constants are uniform in the deleted finite set, original row and unitary character phases. This is actual cutoff convergence, but only in the absolute-convergence half-plane.

Equivalently, z_p=psi_u(p)Np^-s and t_p=z_p/(1+z_p) give J=F_u,1 sum_sf d,(d,T0)=1 beta_U(d) product_{p|d}t_p. At full cutoff beta_infty=mu(d)2^omega; the Euler product is product(1-2t), so F times that product is1/L^T0. A local norm7 counterexample shows why a naive square fails: B=1-2/8=3/4, while(1-1/8)^2=49/64 admits the forbidden overlapping paira=b=p. This is a local algebraic failure, not a new arithmetic energy lower bound.

For a fixed nonprincipal primitivepsi, locally uniform convergence of these actualJ_U on Re>.5 would imply zero-freeness there: allJ_U are holomorphic by the L(s)/L(2s) full-mask ratio and finite1+z denominators; a holomorphic limitG satisfies L^T G=1 on Re>1, hence by the identity theorem throughoutRe>.5. This is only an implication. It is not a proof of such convergence, not a converse and not a consequence of a family-average bound. Principal poles require separate treatment. This step cannot be smuggled into a learned-loss/convergence hypothesis.

The same regrouping gives the smoothed original polynomial I_u=D^-1/2 sum_sf m A_U(m)nu(m)chi_m(u)W(Nm/D), uniformly inU. It is the input to the new direct large-sieve attempt. Its direct large-sieve energy estimate, precise remaining loss and independent review are recorded below.

Shared proof fragments: papers/weighted-cutoff-{core,details}.tex. Exact diagnostics: examples/arithmetic_cutoff/exact_recombination.py, with a separate output namespace and actual Eisenstein split/inert prime ideals, raw row zeros and third/sixth-power cases. No new dependency, Lean declaration, model/GPU job or public release is inferred. Existing finite-carrier and scalar audits remain historical; the full d-weighted moment/II-I covariance and independent positive arithmetic determinant bridge are still the research frontier.


## The reviewed U-independent original-family envelope

The concrete cancellation attempt survives as a new application of the classical all-ideal large sieve, not the target all-epsilon signed estimate. For the actual E=I-P, fixed finite-order nu/S, H,D,U>=1, U^2<=D and a common smooth W supported[1,2], for every epsilon>0:

    sum_{0<Nu<=H}|E_u|^2
      <<_{nu,S,epsilon} ||W||_infinity^2 (HD)^epsilon
                       [H + D H^(1/3) + (HD)^(2/3)].

The constant is independent of U. Exact A_U recombination first gives a length-D polynomial with l2 coefficient norm <<||W||^2D^epsilon. A finite S-unit/ray-class partition and reciprocity convert the literal symbol to the COLUMN-indexed primitive character theta_m(a), whose conductor outsideS is exactly squarefree m. Therefore shared-prime zeros remain zeros even on sixth-power rows. Using the row-indexed primitive theta_a(m) on noncoprime pairs would be wrong and is not done.

Decompose a=a1 a2^2 a3^3 a4^4 a5^5 a6^6, a1..a5 pairwise-coprime squarefree, a6 arbitrary; dyadically set R=productAj and M=max(A1,A2). BGL's simultaneously proved power1/2 squarefree bounds yield block energy R+D R/M+D^(2/3)R/M^(1/3). The exact monomial inequalities R<=H, R^3<=H M^3, R^3<=H^2 M give the stated all-ideal envelope. All units and S-supported powers are summed, not quotiented away. Principal psi_u forces all outsideS valuations divisible by6, so at most C_SH^(1/6) literal rows; residue energy D H^(1/6)log^4(2U) is absorbed by D H^(1/3) with an arbitrarily small loss. This is an upper-triangle estimate, not signed covariance cancellation.

At H=D^(3/4), the new dominant D H^(1/3)=D^(5/4) exceeds H by D^(1/2). Combined with the accepted AFM bound, retain the minimum of this envelope and D^(2delta)U^(2-4delta)H. For U=D^a the new envelope improves the small-delta result only when a>1/4. The 1/2 loss is an upper-envelope limitation, not a lower bound for the true energy. The dyadic comparison is saturated at A1=A2=H^(1/3), but that does not rule out cancellation in the actual signed A_U.

Full author proof: planning/weighted-moment-20261104/attempt/UNIFORM_CUTOFF_MOMENT.md. Literal TeX: papers/uniform-cutoff-moment-{core,details}.tex, byte-identical to the accepted author fragments. Independent derivation/review: planning/weighted-moment-20261104/review/{ALL_IDEAL_PIVOT_DERIVATION,ADVERSARIAL_MATHEMATICAL_REVIEW}.md and the source-hashed mathematical/TeX acceptance receipts. Primary input BGL arXiv:1112.1650v1, Lemma2.1, Section3 definitions, Lemma3.4 and its power-j proof in Section3.2; cached PDF SHA256 1ab29e362c592b9f4078eb85e495ecce6a4665972e6427e7cc2ab0fb214e303b. A fetched quadratic background paper was not required by the final first-two-variable pivot and remains a local literature snapshot.

Finite evidence: author's208 coefficient/338 raw-symbol/46656 monomial/255 exponent controls; independent15625 dyadic controls; root2304 coefficient/792 seven-prime masked identities; independent504 sign-window cases. These counts are diagnostics and bookkeeping tests, not proofs of the external analytic sieve. No new Lean declaration, arbitrary-scope Artin theorem or GRH result follows.

The additional exact band A_U=-mu for U<Nm<=U² is proved by disjoint exclusion and separately checked; the original columns usually lie beyond that band. The genuine remaining input is cancellation using the signed actual A_U and its long-long complement inside the mixed moment, or the original signed II-I covariance, with all smaller-scale short terms/principal residues and required uniformities retained. Do not repeat the worst-case coefficient bound, old AFM, or completed finite-carrier audits as new complete solutions.
