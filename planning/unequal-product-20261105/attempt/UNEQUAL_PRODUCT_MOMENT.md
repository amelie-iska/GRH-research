# Unequal products: exact conductors, a small-conductor bound, and the failed local-completion step

5 November 2026. Original Eisenstein sextic family. This is a fresh, informal arithmetic attempt, confined to the present attempt/check directories. The accepted sources are byte-pinned in source-pins-v1.json. There is no production edit, new external theorem, dependency, build, Lean declaration, GPU work, authentication, publication, or GRH claim.

## 1. Exact objects and the new partial result

Let K=Q(omega), O=Z[omega]. Keep the original raw symbol

    x_m(u) = (u/m)_6,

zero when (u,m)>1, and multiplicative in the squarefree ideal m. Retain fixed S (including primes above 6 and conductor(nu)), fixed unitary finite-order nu, one possibly complex common W supported in [1,2], squarefree good columns, and the high window 2D/7<=U^2<=D. Put

    P_U = {(a,b): (a,b)=1, a,b squarefree good,
                      Na,Nb>U, D<=Na Nb<=2D},
    c_(a,b) = mu(a)mu(b)nu(ab)W(Nab/D),
    lambda_n = mu(n)nu(n)W(Nn/D).

Both factors in P_U have norm comparable to sqrt(D); all its hyperbolic restrictions remain. Define the unnormalized actual row polynomials

    C(u) = sum_(a,b in P_U) c_(a,b) x_a(u)x_b(u),
    M(u) = sum_n lambda_n x_n(u).

The normalized energies/covariance are D^-1 sum_B |C|^2 and D^-1 sum_B C conjugate(M). On this window the first polynomial is exactly the original C_U polynomial, not a separately chosen factor product.

For an accepted six-factor block retain literal units, fixed S-part, the unique row factorization

    u = epsilon * u_S * a1*a2^2*a3^3*a4^4*a5^5*a6^6,

pairwise-coprime squarefree a1,...,a5, arbitrary a6, all ray/class restrictions, and the actual row cutoff. Write

    R0 = product_(j=1)^6 A_j,  M0 = max(A1,A2),
    P = max(A1,...,A5),         product A_j^j <= H.

The symbol M0 in this note is a row scale, not a column moment. Fixed S-parts and finite classes affect constants only. There are O(R0) literal rows in this block.

For squarefree products m=ab and n=cd or n a single mixed column, let

    h=(m,n),  r=m/h,  t=n/h,
    q=r*t,    L=h*r*t.

All three ideals h,r,t are pairwise coprime. The new concrete partial bound is:

**Small-conductor unequal-product lemma.** For every epsilon>0 and Y>=1, the portions with m!=n and Nq<=Y of BOTH the actual C-versus-C energy and actual C-versus-mu mixed covariance have absolute value

    <<_(K,S,epsilon) ||W||_infinity^2 D^epsilon R0 sqrt(Y).       (SC)

Every coefficient, hyperbolic factor mask, row mask, and raw union zero is retained before this estimate. This is a bound for a specified portion of the exact expansion, not a lower covariance budget or the complete signed estimate.

At Y=P^2 the bound is O(D^epsilon R0 P). On the COMPLETE saturating face

    A1=A2=T, A3=C/T, A4=A5=A6=1,  C=H^(1/3),

one has

    R0 P = C*T*max(T,C/T) = max(C*T^2,C^2) <= C^3=H.           (FACE)

Here 1<=T<=C, including both A3=1 and T=1. At H=D^(3/4), this sector is therefore at the H scale, up to epsilon, everywhere on the face. If R0/M0 >= H^(1/3)D^(-eta), then the accepted slack identity gives A1/A2<=D^(3eta), hence

    R0 P <= H*max(1,A1/A2) <= H D^(3eta).                     (NEAR)

Thus (SC) is uniform on the full neighboring region, including A3 and small A4,A5,A6. The remaining sector Nq>P^2 is unestimated at the required strength. Local completion does not improve that sector by itself.

## 2. Proof of the small-conductor lemma; no coefficient-diagonal repetition

For Nm,Nn in [D,2D], m!=n, use the unique h,r,t above. Since Nr/Nt=Nm/Nn,

    1/2 <= Nr/Nt <= 2.

If Nr Nt<=Y and V=max(Nr,Nt), then V<=sqrt(2Y). Also Nh V<=2D. On one dyad V~V0 there are O_K(V0^2) pairs (r,t) by the elementary ideal count, and individually O_K(D/V0) possibilities for h. The latter is valid on every nonempty dyad: V<=2D, so its upper limit is at least a fixed positive constant. Dropping squarefreeness and coprimality is legitimate for this positive upper count. The dyad contributes O_K(D V0). Summing the GEOMETRIC series over V0<=sqrt(2Y) gives

    #{(m,n): m!=n, D<=Nm,Nn<=2D, Nq<=Y}
       <<_K D sqrt(Y).                                      (COUNT)

For Y above the possible range, the obvious O(D^2) alternative is available. No diagonal ab=cd multiplicative-energy estimate is used here.

Each fixed m has r_U(m)<=2^omega(m)<<_(K,delta)(Nm)^delta ordered long factorizations. For completeness, choose a fixed finite prime set so that 2<=(Np)^delta outside it; its finite number of remaining factors is absorbed into the constant. Thus r_U(m)r_U(n)<<D^epsilon after choosing delta small. The C-versus-C expansion gives this multiplicity; the mixed expansion gives only r_U(m). Since |nu|=1 and the raw row kernel has absolute value at most O(R0), multiply (COUNT) by these factors and ||W||_infinity^2 and divide by D. This proves (SC), retaining the original masks inside the exact expansion until this positive upper estimate.

For (NEAR), the accepted slack formula implies A1/A2<=D^(3eta) when A1>=A2; the reverse branch already has ratio<=1. For j>=2, every exponent in R0 A_j is at most its exponent in product A_i^i, so R0 A_j<=H. For j=1,

    R0 A1 / product A_i^i
      = A1/(A2*A3^2*A4^3*A5^4*A6^5) <= A1/A2.

Taking the maximum over j=1,...,5 proves (NEAR). This also proves (FACE) without setting A3=1.

This lemma does not rely on cancellation of Mobius signs. Its purpose is to remove the short-conductor sector from the load-bearing target, leaving a precise signed long-conductor problem.

## 3. What “symmetric-difference conductor” actually means for four columns

At one good prime ideal p, put

    alpha=1_(p|a), beta=1_(p|b),
    gamma=1_(p|c), delta=1_(p|d),
    e=alpha+beta-gamma-delta.

For arbitrary FOUR individually squarefree columns, e ranges over 0,+/-1,+/-2. For u not divisible by p, the local product is chi_p(u)^e. At p|u it remains ZERO whenever any of the four memberships is nonzero, even when e=0. Accordingly,

    L = radical(abcd),
    Q_1 = product_(p in L: e_p != 0 mod6) p,
    Z_1 = L/Q_1,

and the exact raw product is theta_(Q_1,e)(u) 1_((u,Z_1)=1). Its primitive conductor outside fixed S is Q_1, and L is the full zero-preserving period. At e=+/-1 the local primitive character is sextic; at e=+/-2 it is cubic. Both have tame conductor exponent one.

For the ORIGINAL C-versus-C expansion, however, (a,b)=(c,d)=1. Hence alpha+beta and gamma+delta are each 0 or 1. The exponents +/-2 are IMPOSSIBLE. Therefore

    Q_1 = support(ab) symmetric_difference support(cd)
        = ab*cd/(ab,cd)^2,

and Z_1=(ab,cd). This is exactly the two-SQUAREFREE-PRODUCT statement used in the accepted covariance note. It needs no correction on that original support. It would need qualification if “four-column conductor” were read as the symmetric difference of four arbitrary column supports.

Two explicit unrestricted warnings:

* Membership (1,1,0,0) has e=2 and a nontrivial CUBIC local character; the parity symmetric difference of four supports would delete p incorrectly.
* Membership (1,1,1,0) has e=1, although p lies in the supports of BOTH nonsquarefree products ab and cd; the symmetric difference of those product supports would again delete p incorrectly.

For the mixed C-versus-mu term the memberships are alpha,beta,gamma and e=alpha+beta-gamma. The original (a,b)=1 mask again forces e in {0,+/-1}. Its primitive conductor and canceled-prime deletion are the same q and h for m=ab,n.

The exact expansions BEFORE any absolute Cauchy are

    D^-1 sum_(a,b),(c,d) c_(a,b) conjugate(c_(c,d))
          sum_(u in B) x_a(u)x_b(u)conjugate(x_c(u)x_d(u)),

    D^-1 sum_(a,b),n c_(a,b) conjugate(lambda_n)
          sum_(u in B) x_a(u)x_b(u)conjugate(x_n(u)).

Replacing these by an unmasked product of four transforms changes the coefficient support; with signed coefficients there is no pointwise domination just from deleting (a,b)=1. The +/-2 channels are a feature of that relaxation, not of the original moment.

## 4. Every row direction, including the full A3 face

Fix the other row factors. In row direction j, the local exponent is k=j e mod6. For all four-column patterns the table is

    row power j     e=+/-1                 e=+/-2
      1 or 5        order6, conductor p    order3, conductor p
      2 or 4        order3, conductor p    order3, conductor p
      3             order2, conductor p    trivial, conductor1
      6             trivial, conductor1   trivial, conductor1.

At e=0 the primitive component is always trivial. EVERY entry retains a zero at p|a_j when p is in L. This includes j=6 and the e=+/-2,j=3 cells.

More formally define

    Q_j=product_(p in L: j*e_p !=0 mod6) p,
    Z_j=L/Q_j.

The exact pivot factor is theta_j(a_j)1_((a_j,Z_j)=1), not theta_j(a_j) alone. If a fixed other row factor meets L, the entire original summand is already zero and remains zero. The pairwise row masks on a1,...,a5 and the arbitrary a6 also remain.

On the ORIGINAL internal coprime support, e=+/-1 at every p|q. Therefore Q_j=q for j=1,...,5; only local orders differ. In particular j=3 is a genuine QUADRATIC primitive character with conductor q, and the whole A3 direction is nonprincipal. Its conductor has not become smaller merely because its order is two. At j=6 the oscillation disappears but the union deletion remains. No principal centering is changed.

In a RELAXED four-transform moment, e=+/-2 drops from Q_3 but remains in Z_3. A3-only rows can then have primitive-principal channels with unequal nonsquarefree products. Ignoring this is an additional reason not to identify the relaxed fourth moment with the original masked one.

## 5. Exact local complete sums and union-mask restoration

Let F_q be the residue field at p, rho its nontrivial additive character, and chi its order-six character. For any exponent k mod6 define the ZERO-EXTENDED complete sum

    G_k(t)=sum_(z in F_q^*) chi(z)^k rho(tz).

Its exact values/bounds are

    k!=0:  G_k(0)=0,  |G_k(t)|=sqrt(q) for t!=0;
    k=0:   G_0(0)=q-1,  G_0(t)=-1 for t!=0.                 (LOCAL)

Proof: for k!=0, the unit-character sum is zero, and substitution tz=y gives G_k(t)=conjugate(chi(t)^k)G_k(1). Expanding |G_k(t)|^2 and setting x=a y gives an inner additive sum q-1 at a=1 and -1 otherwise, hence q. For k=0 the assertion is the complete additive sum with its zero omitted. This proof works for both split prime fields and inert quadratic fields.

CRT now gives the full period-L additive transform as a product of Gauss factors at p|Q_j and Ramanujan factors at p|Z_j. Local additive twists introduced by CRT are units and only change phases. In particular its magnitude is

    (NQ_j)^(1/2) *
      product_(p|Z_j) | -1 + Np*1_(local frequency at p is zero) |,

provided every local frequency on Q_j is nonzero; otherwise it is zero. Thus a blanket sqrt(NQ_j) bound for ALL full-period transforms is false when Z_j is nonunit. A canceled common prime has not disappeared. The zero complete frequency vanishes when Q_j>1, but that says nothing by itself about the short row sum.

There is an exact way to restore the entire extra deletion without pretending it is an oscillatory conductor. For a fixed pivot use

    1_((r,Z_j)=1) = sum_(d|Z_j) mu(d) 1_(d|r).              (DELETE)

Consequently, with the original window, classes and remaining row restrictions denoted F,

    sum_r theta_j(r) F(r)1_((r,Z_j)=1)
      = sum_(d|Z_j) mu(d)theta_j(d) sum_z theta_j(z)F(dz).  (LIFT)

The inner F(dz) retains the actual support and all original row masks; (LIFT) has not made them independent. Literal elements are treated using fixed primary generators and all units; ideal multiplication rescales the norm by Nd. Fixed ray restrictions are carried to the corresponding scaled restriction, not omitted.

For a squarefree pivot one can also unfold its squarefreeness while retaining every fixed coprimality restriction. Let E be the radical of Z_j and the fixed excluded pivot primes (including the relevant other a_i, i<=5), with the primes of Q_j removed because theta_j already vanishes there. Then exactly

    mu(r)^2 1_((r,E)=1)
      = sum_(h^2|r,(h,E)=1) mu(h) *
        sum_(d|E,d|r) mu(d).

Here (d,h)=1. Therefore the pivot sum equals

    sum_(d|E) mu(d)theta_j(d)
      sum_((h,E)=1) mu(h)theta_j(h)^2
        sum_z theta_j(z) F(d*h^2*z).                       (SF-LIFT)

Terms with Nh>sqrt(O(A_j/Nd)) vanish. Since d,h are coprime the scaling is d h^2, not an incorrectly multiplied overlapping divisibility condition. For the arbitrary a6 pivot there is no squarefree expansion. Extra primary/ray factors remain inside F at their scaled arguments.

The divisor triangle cost is at most tau(E)<<(HD)^epsilon. At norm scale A_j the elementary bound on each inner sum is O(A_j/(Nd Nh^2)); the h sum has bounded reciprocal-norm-square sum. Hence the restoration returns O((HD)^epsilon A_j), not a power saving. This describes the arithmetic cost of keeping common-prime and row-prime deletion, rather than silently restoring a primitive nonzero at a raw zero.

## 6. A concrete Poisson attempt, with the original sharp boundary distinguished

For an UNMASKED smooth pivot trial define

    S_theta(Y)=sum_(z in O) theta(z) V(z/sqrt(Y)),

where theta is primitive of squarefree conductor Q>1, V is a fixed smooth compactly supported function on the Eisenstein plane, and fixed primary/ray restrictions are included by a finite fixed-modulus decomposition. Scaling a generator of Q identifies its lattice shape with the fixed Eisenstein lattice, up to rotation. Periodization and ordinary Fourier inversion give Poisson:

    S_theta(Y)= const_K * (Y/NQ) *
        sum_(dual frequencies xi) G_theta(xi) *
                  V_hat(sqrt(Y/NQ)*rot(xi)).

Normalization of the fixed dual lattice is absorbed in const_K and the rotation. The zero Gauss coefficient is zero; all other coefficients have modulus at most sqrt(NQ) by (LOCAL). Rapid Fourier decay and planar lattice counting imply

    |S_theta(Y)| <<_V min(Y,sqrt(NQ)).                     (POISSON)

For Y<=NQ, the frequency sum is O(NQ/Y), giving sqrt(NQ). For Y>=NQ, absence of the zero frequency and rapid decay give an even smaller bound. The elementary Y bound supplies the minimum. A fixed ray modulus only changes constants.

This smooth completion is an optimistic local test, not a substitution of a smooth row cutoff for the literal sharp cutoff. The exact Fourier-completion identity for a sharp window is still available, but its Fourier l1 norm must be retained; (POISSON)'s derivative constant may not be claimed uniform as an exact sharp boundary is approached. The unconditional bound for the ORIGINAL sharp masked kernel proved here is |K_B(m,n)|<<R0.

Insert (POISSON) into the exact lifted expressions (LIFT)/(SF-LIFT), with all their scaled masks still accounted for. Even this favorable trial cannot improve the long-conductor sector: for a pivot of norm scale A_j,

    Nq > P^2  implies sqrt(Nq)>P>=A_j.

All scaled lengths A_j/(Nd Nh^2) are smaller still. Thus every minimum in (POISSON) takes its elementary LENGTH term. After restoring the union and squarefree masks, the bound remains A_j times divisor losses; summing the other actual row factors returns R0. No sign information from the Mobius column coefficients has survived this per-conductor triangle.

On admissible coprime product pairs, Nq=Nm*Nn lies in [D^2,4D^2]. At H=D^(3/4) on the complete saturation face, every A1,A2,A3 is at most D^(1/4), whereas sqrt(Nq)>=D. Thus neither j=1 sextic, j=2 cubic, nor j=3 quadratic complete sums supply a short-row gain. Changing the local order does not shorten the conductor.

The exact failed inference would be:

    complete mean of a nonprincipal local character = 0
       therefore the original short masked row kernel is small.

The nonzero additive frequencies have not been bounded at a useful scale. The CRT Ramanujan factors and the lifted divisors cannot be omitted. Smoothing also cannot discard the original sharp boundary at a uniform derivative cost. This is an obstruction to THIS pointwise completion calculation, not an arithmetic lower bound or a disproof of the signed target.

## 7. Comparison to DX and the surviving next target

Using |K_B|<<R0 and the accepted balanced pair count O(D), the fully absolute unequal-product C-versus-C calculation gives only

    |offdiag E_C| << ||W||_infinity^2 D R0,

and the same bound for the unequal-product mixed covariance. At B_X, R0=X^2 and X=D^(1/4), this is D X^2=D^(3/2), worse than the accepted powered-BGL middle term DX=D^(5/4). The favorable local Poisson trial leaves precisely that absolute estimate on the long-conductor sector.

On the full face, set C=D^(1/4), A1=A2=T, A3=C/T. Then

    absolute full bound: D R0 = D*C*T,
    accepted middle:    D R0/M0 = D*C = D^(5/4),
    new small q sector: R0 P = max(C*T^2,C^2) <= D^(3/4).

The small-conductor exponent ranges from 1/2 to 3/4 across the face. The absolute full exponent ranges from 5/4 to 3/2. Neither statement is a lower bound on the actual signed sum. The accepted complete global envelope and its separate mixed monomial are unchanged.

The new load-bearing target can now be stated without an ambiguous four-column conductor:

    D^-1 sum_(m!=n, N(mn/(m,n)^2)>P^2)
      mu(m)mu(n)nu(m)conjugate(nu(n))
      W(Nm/D)conjugate(W(Nn/D))
      r_U(m)r_U(n) K_B(m,n),

jointly with the same expression having r_U(m) only. Keep the complete factor realization of each r_U and its hyperbolic restrictions when using the arithmetic; keep

    K_B(m,n)=sum_(actual u in B)
       1_((u,(m,n))=1) theta_(m/h,n/h)(u).

All other raw zeros from q are inside theta, all common-prime zeros remain in the displayed deletion, and every row factor/ray/capacity restriction stays. A useful improvement must sum the actual signed column correlations and nonzero dual frequencies together, before the per-conductor absolute estimate. Merely obtaining a complete local Gauss evaluation, replacing a four-transform product by an unmasked one, or iterating the inherited norm does not do that. No bound of the required strength for this long-conductor sum was obtained.

## 8. Verification and scope

The new standard-library checker imports no project arithmetic helpers. It independently implements Eisenstein multiplication, primary ideal factorization, split/inert residue fields, sextic symbols, and exact additive Gauss sums. Gauss norms are checked in Q(omega,zeta_p) by polynomial coefficient reduction modulo 1+X+...+X^(p-1), with p>3; no floating-point norm is used.

The v2 checker verifies all 16 four-column local membership patterns and all six row directions on residue fields of sizes 7,13,19,25,121; all six complete character exponents at every additive frequency; the full original D=128,U=7 annulus under nu=1 and nu(m)=x_m(2); 72 balanced literal rows and 24 nonprincipal cubic rows in each case; exact four-column and mixed expansions, including canceled-prime union zeros; independent Mobius deletion; exact small-conductor pair/triple decompositions at seven cutoffs; and the full A3 face plus neighboring exponent identities.

Finite profile values are rational/complex norm tables realizable by a COMMON smooth profile via disjoint bumps strictly inside (1,2); the values at the annulus endpoints are zero. No finite table or computed exponent grid proves an asymptotic theorem. Proofs above supply the asymptotic small-conductor count and its bound; the complete long-conductor estimate remains open.

Run only into a fresh output directory:

    PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 \
      planning/unequal-product-20261105/attempt/check_unequal_product_v2.py \
      --output outputs/checks/2026-11-05-unequal-product/attempt/exact-v2

The original v1 script and receipt are preserved. No production TeX compilation, Lean suite, GPU, queue update, dependency, MCP, authentication or public write was needed or run. The source-bound final manifest and HANDOFF.md record the actual passed counts and unchanged source hashes. This attempt does not establish BT_sigma, a complete covariance bound, an improved full analytic exponent, zero location, or GRH.
