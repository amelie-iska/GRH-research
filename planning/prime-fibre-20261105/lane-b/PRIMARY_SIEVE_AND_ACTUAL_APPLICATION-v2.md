# A newly checked fixed-order sieve and the actual prime-fibre problem

NEW research-only literature/application note, 5 November 2026. This is submitted for independent review. It applies the stated unconditional Theorem 1.1 of Alexandre de Faveri's October 2026 PREPRINT, not a new sieve proved here. Its primary version is pinned below. The exact raw-family matching and resulting comparisons are derived here; no canonical/public file is changed. The target signed moment, K0-K_all cancellation, determinant/zero-location bridges and GRH remain open.

## 1. New primary input: its actual bound and its scope

Primary: A. de Faveri, *Optimal large sieve for fixed order characters*, arXiv:2610.04045v1, 2 October 2026, https://arxiv.org/abs/2610.04045v1. Theorem 1.1, printed page 2, states

    Theta_n(A,B) <<_(epsilon,fixed data) (AB)^epsilon
       [A+B+A^(1-1/n) B^(2/n)+A^(2/n) B^(1-1/n)].            (1)

Both index sets in Theta are n-th-POWER-FREE integral ideals prime to fixed S; coefficients on the inner ideal set are arbitrary complex numbers of squared norm one. K contains mu_n. S contains primes above n and its S-integer ring has class number one. The character family is constructed with fixed c,E,m_E in Section 2.3; constants may depend on this data. This is not the fully orthogonal A+B bound, not a prime-support theorem, and not a bound ordered only by radical conductor. Order DIVIDING n is included (Section 2.3). Theorem 1.4's extra mu_(2n) hypothesis is NOT a hypothesis of Theorem 1.1.

For n=6 the relevant upper expression is

    F6(A,B)=A+B+A^(5/6) B^(1/3)+A^(1/3) B^(5/6).           (2)

The larger sixth-power-free family is precisely what makes a physical a=v1*v2^2 admissible. It is not legitimate to replace its norm by N(v1*v2) and call that Theorem 1.1.

Local reading cache ONLY:

    primary/defaveri-optimal-v1.pdf
    SHA256 97720b3cacccbedb9c2014520ad4d128ae23afd0a781bdeff27dab4e86b7c726
    primary/defaveri-optimal-v1.txt
    SHA256 ef550aa4bca1659c6d98ebf69e2cbd42a2793b707f6171f53d1b2baeb8654a57

Do not redistribute these publisher/preprint snapshots in any release. Public citations and hashes suffice. The paper's proof is not replaced by its abstract or by the finite controls below.

## 2. Exact raw sextic family match over the Eisenstein PID

Fix K=Q(omega), O=Z[omega], the standing complex embedding, and fixed S containing the primes above 2,3 (and the original finite conductor exclusions). Every good ideal a has a unique generator alpha_a congruent to 1 modulo (3). Indeed O is a PID and the six units map bijectively onto (O/(3))^times. The primary generator map is multiplicative. The same argument applies to fractional ideals prime to 3, interpreting the congruence locally.

Choose the allowed Section 2.3 data as follows. Take c sufficiently divisible at S that the stipulated local sixth-power condition holds, and enlarge it to be divisible by (3). Choose the class representatives E0 as ordinary ideals prime to S and take m_E0=alpha_E0. Since K itself has class number one, these are allowed generators after S-localization as well. For the product representative E, the prescribed product m_E is exactly alpha_E, by multiplicativity of primary generators.

For coprime good a,b, the source construction writes

    a=(x) E g^6,   x=1 mod c,   (g,b)=1,
    chi_a(b)=(x*m_E / b)_6.

Choose an ordinary fractional generator gamma_g of g. Ideal equality gives

    alpha_a=eta*x*m_E*gamma_g^6,  eta in mu_6.

All factors are units at 3. The group (O/(3))^times has order six, so gamma_g^6=1 mod 3; also x,m_E,alpha_a are 1 mod 3. Thus eta=1 mod 3, which forces eta=1. Consequently

    chi_a(b)=(alpha_a / b)_6                                  (3)

EXACTLY, with the original positive sextic-symbol convention. On a common ideal prime both sides are zero by the source definition in Section 2.3.4 and the raw symbol definition. No primitive character is substituted with its omitted local factors, and no reciprocity quotient has been discarded. No extra column-ray restriction or coefficient split is required for this deliberately chosen family. Other allowed family choices need not be identical; we use this fixed one throughout.

This proof uses the physical ideal a, including valuations 2,3,4,5; the character may have order 3 or 2 in those cases, as permitted by the source. Its primitive conductor has the source's fixed-S part times the appropriate radical, but that does NOT change the norm indexing in (1). Reversing the fixed complex embedding conjugates the sextic symbols; it does not change the positive norm bound, and we choose the original embedding for (3).

## 3. Actual row decomposition and every retained mask

For an actual nonzero literal row, decompose its ideal outside S uniquely as

    (u)_outsideS = a*r6^6,
    a=r1*r2^2*r3^3*r4^4*r5^5,  a sixth-power-free.

Here each r_j (j<=5) is squarefree and the first five are pairwise coprime. The ideal r6 is ARBITRARY, may be nonsquarefree, and may overlap any r_j. With canonical primary generators,

    u=u0*alpha_a*alpha_r6^6,
    Nu=Nu0*Na*(Nr6)^6.

The literal unit and S-supported part are in u0. Freeze u0 and r6. For every original good squarefree column m,

    (u/m)_6=(u0/m)_6 * chi_a(m) * 1_{(m,r6)=1}.             (4)

If m also shares a prime with a, chi_a(m)=0, so all full-union/common-prime zeros remain. An overlap of a with r6 is not removed or counted twice: (4) is the product of the original raw zeros. The existing actual unit/ray/capacity/squarefree row filters can be enlarged only inside the ensuing positive operator estimate. Fixed nu and the ONE common complex W remain column coefficients.

For this frozen pair take

    c_m=A_U(m)nu(m)(u0/m)_6 W(Nm/D)1_{(m,r6)=1},
    I_u=D^(-1/2)sum_m c_m chi_a(m).

This is the original annular family, with zeros outside its good squarefree support. Both a and m are sixth-power-free, so (1) applies with A=H/(Nu0*(Nr6)^6), B=2D, up to harmless endpoint constants. If A<1 this row set is empty. Coefficients are independent of a, as REQUIRED. The uniform original assignment bound |A_U(m)|<=3^omega(m)<<_eta D^eta gives

    sum_m |c_m|^2 <<_eta B_W^2 D^(1+eta),  B_W=||W||infinity. (5)

The rough short-coefficient identity is NOT used for (5) or for K0. If a fixed unitary infinity-type-one Jacobi gauge vartheta is used, it too is just an allowed row-independent column multiplier. We do not assert that vartheta belongs to the finite-order row family, invoke a finite-order theorem for it, or claim that a unitary gauge improves an operator norm.

Unweighted actual rows (and the previously justified bounded natural literal multiplicities) are the scope. Arbitrary positive row weights require their own weight/operator control; they are not silently inserted into (1).

## 4. New positive comparison for A6=1 and the ACTUAL combined h=1 form

For A6=1, a physical two-pivot row a=v1*v2^2 obeys Na<=H/Nu0. Using (1)--(5) gives

    sum_(actual A6=1 rows) |I_u|^2
       <<_(nu,S,epsilon) B_W^2 (HD)^epsilon F6(H,D).         (6)

For fixed u0 this follows directly. If all S-supported u0 are summed in this A6=1 assertion, the D term costs O_S((log(2H))^|S|), absorbed into (HD)^epsilon; it is NOT summed as a convergent exponent-zero Euler product. The coefficient norm and theorem constants are uniform in the fixed column phases. This is a new LITERATURE-INPUT comparison, not a new signed saving. It can be combined by taking a minimum with the already established R,M-sensitive powered and ordinary-conductor bounds, where R=A1*A2, M=max(A1,A2). It retains neighboring blocks without identifying ab^2 with its radical.

There is also a direct consequence for the requested combined K0-K_all. Start from the accepted ORIGINAL divisor-energy identity for S1AA. For each squarefree d, L=D/Nd, keep A_U(da) UNFACTORED and retain its actual raw (d,u) row mask; enlarge that mask only inside a positive norm. The arbitrary-coefficient bound (1) and the assignment bound on A_U(da) give

    |S1AA| << B_W^2 (HD)^epsilon
                 sum_(Nd<=2D) (1/Nd) F6(H,D/Nd).

For 1/2<=L<1 only the unit residual can occur; use its direct row count, bounded by the same expression up to a constant. No length<1 sieve is invoked. The ideal sums at exponents 1,2,4/3,11/6 (the first logarithmic, the rest convergent) prove

    |S1AA| << B_W^2 (HD)^epsilon F6(H,D).                   (7)

This triangle is in the exact divisor identity, not separate absolute estimates of K0 and K_all. It is still a positive majorant and does not exploit mu(d) cancellation.

The accepted coherent-Mertens correction states

    S1AA=(K0-K_all)/D + E_corr,
    |E_corr|<=236800 B_W^2 R_w      at H<=D^(3/4),           (8)

with the original high-window/complete-support hypotheses. Its ordered rough-prime correction P2 has p=q allowed and only the stated asymmetric q-row mask; it is not conflated with Ctwo. We use that accepted correction intact. Therefore (7),(8) imply the SAME upper comparison F6(H,D) for the ACTUAL (K0-K_all)/D, plus its affordable correction. No new separate main-term cancellation is proved.

At H=D^(3/4), the four monomial powers in F6(H,D) are

    3/4, 1, 23/24, 13/12.

Thus both remaining pure and mixed witness neighborhoods admit the new candidate 13/12 comparison instead of the former 7/6 majorant, once the primary theorem/application are admitted. This is a gain of 1/12 in that positive A6=1 certificate, but it still exceeds the target 3/4 by 1/3. It is not an actual energy lower bound, a bound for a centered orientation variance, or a proof of the target.

## 5. Summing arbitrary overlapping sixth factors: a global corollary

For fixed u0, sum the positive bound (1) over all ideals r6, Nr6<=H^(1/6). The H term is weighted by (Nr6)^(-6), the H^(5/6)D^(1/3) term by (Nr6)^(-5), and the H^(1/3)D^(5/6) term by (Nr6)^(-2); these ideal sums converge. The D term counts O(H^(1/6)) possible r6. For S-supported u0, the resulting four global terms carry respectively powers (Nu0)^(-1), (Nu0)^(-1/6), (Nu0)^(-5/6), (Nu0)^(-1/3). Each sum converges over the fixed finite S-supported semigroup. Their fixed column phases have no effect on the coefficient norm or theorem constant. Consequently

    sum_(0<Nu<=H) |I_u|^2
       << B_W^2 (HD)^epsilon [
          H + D H^(1/6) + H^(5/6)D^(1/3)+H^(1/3)D^(5/6)].   (9)

This is valid for the original raw literal rows, including sixth factors with overlaps and repeated primes. It uses no conductor-dependent prime theorem. For the original fixed-nu residue-subtracted family E_u=I_u-P_u, use the already established principal-row count and residue bound

    sum_u |P_u|^2 << B_W^2 (HD)^epsilon D H^(1/6).

The inequality |I-P|^2<=2|I|^2+2|P|^2 preserves (9). This is the same principal assembly as the accepted old envelope, now dominated by an explicit term already in (9); no unproved Artin holomorphy, positivity or zero statement is inserted.

At H=D^(3/4), (9) has powers

    3/4, 9/8, 23/24, 13/12,

so the global positive candidate is 9/8, a gain of 1/24 from the old 7/6 envelope, still above the target by 3/8. The D H^(1/6) contribution includes coherent sixth-power rows; deleting their nonprincipal literal-unit phases or principalizing them would be invalid. Agreement of this SUPNORM-only exponent with the moving-profile obstruction is a consistency check, not a fixed-W lower bound or a signed target theorem. Current public metadata still describes the previously accepted result until independent review/integration.

## 6. What the prime-specific literature does and does not add

The primary search located two additional candidates, downloaded and read in their exact versions. Neither is used as an input to (6)--(9).

* H. Iwaniec, *The large sieve with prime moduli*, Rev. Mat. Iberoam.38(2022),2337--2354, DOI10.4171/RMI/1381, Theorem2/(1.5) under (1.4). It is an additive sieve at RATIONAL prime denominators q<=Q, with integer coefficients n<=N, (n,P)=1, N<=Q^2(log Q)^(-8), D0=Q/sqrt(N); its scale is (1+delta)Q^2/log D0, delta=(loglog Q)^(5/2)prod_(p|P,p<D0)(1-1/p)^(1/2). This is not a raw ideal-valued sextic row-family statement. Prime columns versus prime moduli, rational integers versus distinct Eisenstein ideals (including inert p^2), and the coefficient roughness/index restrictions cannot be interchanged. Even an analogous logarithmic gain would not supply the missing D-power.

* A. Dunn, *Metaplectic cusp forms and the large sieve*, arXiv:2403.13151v5 (22 October2026), Theorems1.2/1.5, printedpp4--5; journal DOI10.2140/ant.2025.19.1823 is the bibliographic publication pointer, not a claim that the journal PDF equals v5. The bilinear kernel is rho_f(lambda^(-3)ab) for a FIXED CUBIC METAPLECTIC CUSP form f, with squarefree alpha_a, arbitrary beta_b, X~AB, A,B>=10, congruence modulus v and a smoothness cost K. Theorem1.5 has factor K^8 N(v)^4 [(AB)^(1/2)+A^(3/2)B^(1/4)]||mu^2 alpha||infinity||beta||2, apart from epsilon factors depending on f. It does not identify rho_f with raw chi_p(u), a quadratic central Gauss phase, or the CM Jacobi generator vartheta. No fixed-f identity or uniform varying-level family matching those actual kernels has been proved. A prime theorem for rho_f is therefore not inserted into the actual combined form.

Restricting (1) to prime-ideal columns is legitimate by setting other coefficients to zero. It preserves the same F6 operator constant; prime sparsity may reduce a particular coefficient l2 norm, not automatically improve the operator by a D-power. For fixed residual a, the actual rough prime-column row sum has raw p|u zeros and fixed p∤a coefficient mask, so an appropriate prime-column norm could be used there. Recombining ALL residuals, ordered rough corrections and K0 coherently is still required. No theorem found in this bounded search proves the desired mean-retaining thin-family prime average for that recombination. No exhaustive literature nonexistence claim is made.

The present new useful input is therefore the full power-free fixed-order theorem, not a prime-specific signed estimate. The ordinary all-primitive comparison and the old BGL/powered-family audit are used only as prior baselines; they have not been rerun as new work.

## 7. Source and evidence limitations

All PDF/text snapshots are local reading cache, excluded from public closure; only citation/version/DOI/URL/hash metadata may be redistributed. Exact source theorem hypotheses and the chosen family data matter. Finite unit/decomposition/Fraction controls check this application's bookkeeping only; they do not prove the preprint theorem. No old actual table, character run, learning trace, publication/browser audit, dependency, auth, Lean compiler, production file, queue or protected index is changed.


## 8. Updated joint-PIT power accounting from this NEW norm input

This is a new corollary of (1), not a replay of the earlier Stieltjes attempt. On an actual two-pivot block with fixed u0, put H_b=min(H/Nu0,8*A1*A2^2), the physical outside-S row-norm cap; only nonempty blocks are considered. The now-available positive bound is the full neighboring-block formula

    lambda_now(L) << (HD)^epsilon min{
        R+L R/M+L^(2/3)R/M^(1/3), L+R^2, F6(H_b,L)}.      (10)

For L<1 keep the direct actual unit-column norm R_w as before. This is NOT a new estimate for arbitrary row weights. In the accepted exact joint-incidence/Abel identities one can insert lambda_now, retaining the signed mean, common W, endpoint E(U)Q(U), all raw zeros and the direct subunit endpoint. The sufficient pointwise discrepancy certificate becomes

    |EPIT|/D << (HD)^epsilon M1(W)^2 delta_S(U)
       [lambda_now,*(D/U)
                   +integral_(1/2)^(D/U)lambda_now,*(L)dL/L].

The minimum stays inside the integral; the two witness exponents are not a substitute for the neighboring-block statement. At H_b~H=D^(3/4), U~D^(1/2), the four new F6(H,D/U) powers are

    3/4, 1/2, 19/24, 2/3.

For the pure witness the former5/6 certificate improves to19/24; to fit H it would be sufficient to have an independent scalar discrepancy power U^(-1/12), still not supplied by the accepted fixed-field PIT. At the displayed mixed witness the OLD R,M-sensitive7/9 bound is smaller than the new generic19/24, so the minimum retains7/9 and the sufficient U^(-1/18) scalar power is unchanged. The earlier sufficient U^(-1/6) pure input belongs to the historical old operator bound.

By the independently accepted conditional zero-strip diagnostic (not an available prime-error theorem), an all-scale/all-epsilon mean-square power1/12 would entail a fixed strip Re(s)>11/12; power1/18 would entail Re(s)>17/18. These are independent sufficient INPUT diagnostics, not necessary conditions for the actual signed target, and no such powers/strips are asserted proved. The non-discardable pointwise lower endpoint needs compatible control as well. K0-J remains unestimated even with exact prime density.
