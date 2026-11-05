# Independent adversarial review: centering and the signed balanced-block target

5 November 2026. Executed only on `iska-linux-vscode` in `/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104`.

**Verdict: ACCEPTED as exact reductions and a shortcut obstruction, conditional on the expressly retained earlier analytic inputs.** No load-bearing gap was found in the reviewed version. This is not acceptance of BT_sigma, a new analytic saving, a D X energy lower bound, Lean formalization, determinant positivity or GRH.

The exact reviewed derivation SHA256 is `cedc1e68b983dc86e63a2596d535d985a6e0a829906859df71fd97164e36613c`. Its checker, report, handoff and manifest were read. Every hash listed in the author manifest matches the actual bytes. The final receipt pins the additional dependency and reviewer evidence bytes.

## Hypotheses retained by this acceptance

The field is K=Q(omega), with its actual Eisenstein elements and six literal units. The fixed finite-order Hecke character nu can have arbitrary fixed finite order; it is not required to have order dividing six. S is fixed and contains all primes above 6 and every conductor prime of nu. In particular nu is unramified at every prime outside S. All active columns and convolution ideals are squarefree and prime to S; disjoint placements are essential. The profile W is one common smooth function supported in [1,2]; it may be complex. D>1 and 1<=U<=sqrt(D). No row-dependent profile supremum is admitted.

The block B_X has outside-S radicand ideal a1*a2^2, with squarefree, coprime, nonunit a1,a2 and X<=Na1,Na2<2X. For the stated B_X the S-part is 1 and all six generators are retained. It is contained in Nu<8X^3. The target additionally restricts fixed 0<sigma<=1/12 and 2<=X comparable to D^(1/4), with fixed comparability constants. Neither constants uniform in varying nu/S nor arbitrary coefficient sequences are covered.

The primitive psi_u and independently primitive psi_(u,2) are those of the prior full-mask Mellin transfer. Their different primitive conductors must not be replaced by the larger deleted set or by a common raw-square zero sentinel. The retained residue is the original P_u, including its d-dependent rho_T and original zero-extended factors.

## Independent mathematical findings

1. **Residue-centered Gram and principal split.** Recombining the restored finite initial series gives I=sum_d beta_U(d)t_(u,d), and the displayed residue gives P=sum_d beta_U(d)r_(u,d). Subtracting gives E=sum_d beta_U(d)e_(u,d) before any inequality. Expanding the modulus gives CG, with conjugation on the second beta and second column. K_H is a Gram matrix and is positive semidefinite. No identity makes subtraction of the residue an orthogonal projection. The disjoint principal/nonprincipal split PS is exact, so there cannot be cross cancellation between those row sets.

2. **P=0 on the entire balanced block.** At a prime p outside S with radicand valuation r modulo 6, tame Kummer inertia has order 6/gcd(6,r). At primes of a1 and a2 these orders are respectively 6 and 3. Both are nontrivial, with tame conductor exponent one. The restriction of nu to inertia is trivial, so multiplication by nu cannot cancel them. Passing to the underlying primitive character does not erase nontrivial inertia. Consequently psi_u is nonprincipal for every displayed row, and P_u=0, E_u=I_u there. Units and S-supported multipliers do not change these outside-S valuations. If the assumption conductor(nu) subset S were removed, an inverse ramified twist could cancel inertia; that hypothesis is necessary.

   Nonblocking terminology clarification: in section 2 the words “exponent 1 or 2 modulo 6 in the outside-S tame Kummer conductor” should read “valuation 1 or 2 modulo 6 in the Kummer radicand.” The conductor exponent itself is one for either nontrivial tame inertia character. The argument and claimed nonprincipality use the correct underlying fact.

3. **Raw Gram conductor and union zeros.** For squarefree m,n and g=gcd(m,n), shared-prime nonzero sextic factors cancel against their complex conjugates. At primes in m/g and n/g the remaining exponents are +1 and -1, each nontrivial, so the primitive oscillatory conductor outside S is the squarefree symmetric difference. This describes the coprime locus only. If any prime of the union divides u, at least one original factor is zero and the product is zero. Thus diagonal G_B(m,m) is exactly the coprime row count, even though its remaining oscillation is trivial. The sixth-power example m=n=p, u=p^6 gives raw product zero and symmetric-difference oscillation one: replacing the former by the latter loses the mask. The accepted column-indexed primitive-character orientation retains that zero; the primitive row orientation can lose it.

4. **No unproved lower bound is smuggled into saturation.** The accepted BGL block bound with R comparable to X^2 and M comparable to X gives X^2+D X+D^(2/3)X^(5/3). At X comparable to D^(1/4) these exponents are 1/2, 5/4, 13/12. Since P=0, centering cannot change this block's actual energy, but that fact does not show the actual energy attains D X. The single-row aligned arbitrary-coefficient example certifies only its single-row norm statement. Distinct fixed-factor pivots change the coefficient phases, so their worst cases cannot be summed into a simultaneous lower bound. The note expressly rejects that invalid inference.

   Likewise, a prime column with Np>H cannot divide a nonzero row of norm at most H. If Np>U its actual A_U(p)=1. Under D>H and U<=sqrt(D), this holds throughout the active prime annulus, including its boundary. This proves the absence of an additional algebraic deletion for those columns; it does not prove a lower bound for their sum or for the full signed polynomial.

5. **LL and the full active annulus, with equality.** For squarefree m, the unrestricted disjoint three-placement sum is mu(m), prime by prime. In the exclusion Na>U, the inner sum over b|m/a is zero unless a=m, when it is one. Hence that exclusion is mu(m)1_(Nm>U), identically for b. Adding the overlap gives LL exactly. For every active column, Nm>=D>U because D>1 and U<=sqrt(D). Thus A_U=C_U-mu everywhere that W can contribute, including Nm=D and Nm=2D. At Nm=U^2, the strict conditions Na>U and Nb>U would force N(ab)>U^2, impossible when ab|m; therefore C_U=0 and A_U=-mu, including the equality endpoint. Conversely Nm=U lies outside this reduction and has A_U=mu. Nonsquarefree m would invalidate the unrestricted sum=mu argument and is excluded.

6. **Covariance signs and conjugates.** Defining L^c=L-P with the original P, without assigning new analytic residues to L or M, gives E=L^c-M. The expansion is ||L^c||^2+||M||^2-2 Re sum L^c overline(M). On B_X, P=0 and the exact Q_B has conjugation on g(n), nu(n), W(Nn/D), and x_n(u). Therefore Q_B(A,A)=Q_B(C,C)+Q_B(mu,mu)-2 Re Q_B(C,mu). The signs and complex conjugates in the note are correct. The diagonal is nonnegative and exact; no claimed off-diagonal sign follows from it.

7. **What BT_sigma would actually require.** With one common admissible uniform constant in R_sigma, the inequality Q_B(A,A)<=R_sigma is algebraically equivalent to 2 Re Q_B(C,mu)>=Q_B(C,C)+Q_B(mu,mu)-R_sigma. This is a lower bound on the real covariance. An upper bound on its absolute value does not establish it. The note labels this TARGET and supplies no proof; acceptance does not change that status. Uniform control of one balanced block alone also does not settle the near-saturating blocks of the full decomposition. At H=D^(3/4), the global mixed term remains D^(7/6), still larger than H even if the D^(5/4) term were removed.

## External and prior inputs

No new external analytic theorem is proved or newly verified by this review. The exact finite manipulations depend on the prior accepted full-mask Mellin transfer and its principal residue, as recorded in the masked-moment fragments. The nonprincipality/conductor statements use tame abelian Kummer reciprocity away from primes above 6, primitive-character uniqueness, and the elementary conductor behavior of a nontrivial tame one-dimensional character. The quoted upper envelope and block bound import the previously reviewed BGL sixth-order-family sieve, its powered first/second-variable form and the finite S-unit/ray-class comparison. The pinned primary source remains Blomer–Goldmakher–Louvel, arXiv:1112.1650v1, Lemma 2.1, section 3 definitions/Lemma 3.4/powered proof and Appendix II; the earlier accepted note records the PDF hash and precise ranges. This review did not rerun or re-present that finished sieve proof as new work.

## Focused independent execution

The new standalone reviewer checker imports no author checker. It implements Eisenstein ring multiplication, exact conjugation, split/inert finite-field sextic powers and Fraction arithmetic directly. The deterministic run on Python 3.12.3 passed:

- 224 LL cases, 198 active reductions, rational/integer cutoffs including U=1, and two exact Nm=U^2 endpoint cases;
- 25 local inertia-order diagnostics over split norms 7/13 and inert norm 25, including r=2 of order 3 and a negative ramified-inverse-twist control;
- 72 literal balanced rows and 75,776 exact raw products, including 69,888 union-mask zeros and 2,848 witnesses against omission of the inverse/conjugate;
- 1,296 rowwise covariance identities, 18 independent full Gram expansions with complex rational annular profiles and three fixed Kummer twists, and 54 inequality-equivalence checks including equality;
- 144 witnesses against incorrect covariance signs/conjugates and 18 against omission of the weight conjugate;
- a 74-row/four-column centered Gram calculation, five positive-semidefinite quadratic forms, exact PS and a nonzero witness against automatic projection orthogonality.

The centered test treats the common zeta-residue base as a formal constant set to one; it checks algebra, not the analytic value of that residue. Finite complex rational profiles are diagnostic arrays, not a replacement analytic smooth W. Local finite-field order checks do not prove the general Kummer conductor theorem. No numerical BT_sigma inequality or finite energy measurement is evidence of an infinite saving.

Command: `PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 planning/weighted-moment-20261105/review/check_independent_exact.py --output outputs/checks/2026-11-05-weighted-moment/review/independent-negative-edge-controls-v1.json`.

An initial reviewer-harness run aborted before output creation because a zero coefficient was multiplied by an undefined symbol at a prime absent from the symmetric difference. Restricting that sum to its nonzero terms corrected the harness; the final run above passed. No author artifact was changed and no prior report was overwritten.

Only new review planning/check files were written. Repository README, applicable working instructions, existing scripts and prior proof/review context were read. No repository AGENTS.md or relevant Python dependency lockfile was found; no environment or dependency was changed. No production file, queue, old output, data, model, credential, cache, publication or MCP setting was modified. No source theorem, Lean or GRH completion is asserted.
