# Joint five-power Gauss balance with every original mask

5 November 2026. Version 2 fixes the unit-ideal generator convention flagged by independent review; v1 bytes remain preserved. Research-only exact reduction, not an analytic exponent improvement. The Gauss and CRT ingredients are standard. The five-power balance and orientation Parseval below are the surviving algebraic application in this attempt. No production, pin, history, dependency, environment, model, credential or publication change is part of this directory.

## Original coefficient and literal row weight

Use the original good squarefree ideal columns, sextic symbols x_m(u)=(u/m)_6, fixed finite-order nu, fixed S containing the primes above 6 and the conductor of nu, and the actual common possibly complex smooth W supported in [1,2]. In the accepted cutoff window set

    lambda_m = mu(m) nu(m) W(Nm/D),  c_m = r_U(m) lambda_m.

The count r_U is the actual number of ordered internally coprime long-long factorizations of m. It is not replaced by an arbitrary or multiplicative coefficient. Expand the normalized C-C energy as

    D^-1 sum_(m,n) c_m conjugate(c_n)
                      sum_u x_m(u) conjugate(x_n(u)).

Fix one literal block's unit/S-supported factor u0 and write

    u = u0 v1 v2^2 v3^3 v4^4 v5^5 v6^6.

Let F(v1,...,v6) be the exact finite-support weight on O^6. Include every primary/ray condition, squarefree and inter-factor restriction, dyadic window, capacity restriction, original sharp boundary and declared common row profile. The first five squarefree factors and arbitrary sixth-power factor retain their exact original restrictions, including any permitted overlap with the latter. No product factorization, independence or smoothness of F is assumed. Sum all original u0 classes after the identity. An additional row restriction can be included in a common F only when it is independent of the column orientation. Otherwise partition it explicitly or retain an orientation-indexed transform and do not use the common-weight Parseval corollary below.

For m=h r,n=h t the ideals h,r,t are pairwise coprime squarefree. Set

    q=r t, L=h q, Q=Nq, ell=NL,
    theta_(r,t)=x_r conjugate(x_t), xi_q=x_q^3.

Exclude q=1, the coefficient diagonal. The exact raw character is

    x_m(u) conjugate(x_n(u))
      =theta_(r,t)(u0) product_(j=1..6) f_(j,r,t;h)(vj),
    f_j(v)=theta_(r,t)(v)^j 1_((v,h)=1)       (1<=j<=5),
    f_6(v)=1_((v,L)=1).

Theta has its primitive zero extension on q. Thus every f_j retains all primes of L. The separate definition of f_6 is essential: no raw zero is restored by taking a primitive character.

The original internal coprimality gives local exponents only 0,+1,-1. Every theta^j, 1<=j<=5, is primitive on the same q, and theta^3=xi_q is independent of the orientation r,t. These assertions are not made for generic four-column exponents +/-2. Also

    mu(h r) mu(h t)=mu(q).

The Mobius sign is constant among orientations of one q. It remains a signed outer conductor weight.

## Additive and CRT conventions

Take O=Z[omega], delta=1+2 omega, a generator of the different. Fix generators alpha of h and beta of q, choosing alpha=1 when h=1, and use alpha beta for L. Define

    e_beta(z)=exp(2 pi i Tr_(K/Q)(z/(delta beta))),
    tau_beta(eta)=sum_(z mod q) eta(z) e_beta(z).

The pairing is nondegenerate on O/q. Analogous definitions use alpha and alpha beta. Ideal residue characters are independent of this additive-generator choice. Changing a generator in a Gauss sum requires changing its additive character too; the formulas below are covariant under doing so consistently.

The Ramanujan sums are

    c_h(k)=sum_(z mod h,(z,h)=1) e_alpha(k z)
          =product_(p|h)(Np 1_(k in p)-1),

and similarly c_L. Unit scaling of k leaves c_h invariant, and c_1=1. For 1<=j<=5 let

    G_j(k)=sum_(v mod L) f_j(v) e_(alpha beta)(k v).

CRT, using alpha^-1 mod q and beta^-1 mod h, gives exactly

    G_j(k)=theta(alpha)^j tau_beta(theta^j)
              conjugate(theta(k)^j) c_h(k)   if (k,q)=1,
    G_j(k)=0                                otherwise.

The factor theta(alpha)^j is the explicit CRT phase, not a suppressed ray/root-number factor. For j=6, G_6(k)=c_L(k).

## Joint five-power phase balance

For a nontrivial primitive character eta the standard Gauss identity is

    tau_beta(eta) tau_beta(conjugate(eta))=eta(-1) Q.

Pairing powers 1 with 5 and 2 with 4 yields

    product_(j=1..5) tau_beta(theta^j)
      =Q^2 theta(-1)^3 tau_beta(theta^3)
      =Q^2 xi_q(-1) tau_beta(xi_q).

Thus the *orientation dependence of the complete five-power Gauss phase* cancels. For k1,...,k5 units modulo q define

    K(k)=product_(j=1..5) kj^j mod q.

Combining the five CRT phases gives the exact full-mask identity

    product_(j=1..6) G_j(kj)
      =Q^2 xi_q(-alpha) tau_beta(xi_q)
         conjugate(theta_(r,t)(K(k)))
         [product_(j=1..5) c_h(kj)] c_L(k6).                (GB)

If any of k1,...,k5 is nonunit mod q the left side vanishes. The modulus-one factor xi_q(-alpha) is the explicit remnant of the h-generator and Gauss pair signs. At h=1 our explicit convention alpha=1 makes it xi_q(-1). Every canceled common prime survives in all five c_h factors and in c_L; the sixth-power variable retains the full L deletion.

This phase cancellation is not a proof of cancellation in the original incomplete signed moment.

## Exact joint conductor/dual-frequency identity

Use the unnormalized transform of the exact literal row weight

    Fhat_L(k)=sum_(v in O^6) F(v)
                      e_(alpha beta)(-sum_j kj vj).

It is the transform of the periodization of F on (O/L)^6, so inversion has factor ell^-6. Put t=q/r and

    a_(h,q)(r;u0)=r_U(h r) r_U(h t)
                   nu(r) conjugate(nu(t))
                   W(Nh Nr/D) conjugate(W(Nh Nt/D))
                   theta_(r,t)(u0).

Set a=0 for all excluded orientations, including all original annular, squarefree, S and column restrictions. The common nu(h) factor cancels because nu is unitary on good ideals. Define

    A_(h,q)(K;u0)=sum_(r|q) a_(h,q)(r;u0)
                             conjugate(theta_(r,q/r)(K)),

    B_(h,q,F)(K)=sum_(k mod L, (k1...k5,q)=1, K(k)=K)
                  Fhat_L(k) [product_(j=1..5)c_h(kj)] c_L(k6).

Then for any selected set T of original off-diagonal pairs specified by h,q and permitted orientations, the normalized original contribution is exactly

    E_T=(1/D) sum_(h,q in T) mu(q) Q^2 xi_q(-alpha)
                 tau_beta(xi_q) ell^-6
                 sum_(K in (O/q)^x) B_(h,q,F)(K)
                                       A_(h,q)(K;u0).          (JD)

Sum the original u0 classes and blocks afterwards. This retains the outer signed conductor sum before taking absolute values. It applies to h=1 and to a low-gcd/large-conductor sector. It is a finite identity, with no smoothing or approximation. Selecting T does not permit dropping another signed piece by positivity.

For the mixed C-versus-mu term replace the second r_U(h t) by 1. The common possibly complex W and every other factor remain unchanged.

## Exact orientation diagonal and finite bound

Distinct orientations are orthogonal over the dual product K:

    sum_(K in (O/q)^x) conjugate(theta_(r,q/r)(K))
                              theta_(s,q/s)(K)
      =phi(q) 1_(r=s).

The quotient has exponent +/-2 at each flipped prime, so any nonempty flip gives a nontrivial cubic character. Hence

    sum_K |A_(h,q)(K)|^2=phi(q) sum_(r|q)|a_(h,q)(r)|^2.    (OP)

This is an exact CRT character diagonal, not marginal independence of the original row factors. One conductor term therefore satisfies

    |E_(h,q)| <= Q^(5/2)/(D ell^6)
                  [phi(q) sum_r |a_(h,q)(r)|^2]^(1/2)
                  ||B_(h,q,F)||_2.                          (OB)

This is an explicit finite norm reduction. No estimate for the remaining B sufficient to yield an analytic exponent improvement has been proved. Taking outer absolute values of (OB) would lose conductor signs; (JD) has not done that.

The product map from five q-unit frequencies to K has every fiber of cardinality phi(q)^4, since k1 is uniquely solvable after k2,...,k5 are fixed. Thus (OP) holds under uniform five-frequency averaging as well. The actual Fourier/Ramanujan weight is not uniform.

All orientations have the same value at K exactly when x_p(K)^2=1 for every p|q. This coherent cubic-residue diagonal has cardinality phi(q)/3^omega(q), and the common value is x_q(K) in {+1,-1}. Thus orthogonality gives no pointwise cancellation on this subset.

## Finite-height truncation

Choose one centered fundamental-parallelogram representative k of each residue modulo alpha beta. Since |omega|=1, each has |k|<=|alpha beta|=sqrt(ell), hence Nk<=ell. Thus (JD) is exact at finite height sqrt(ell) in each of six complex variables. This is conductor-sized finite completion, not an analytic short-height bound.

For any frequency subset Omega, let B_Omega restrict the sum defining B. The error in one normalized conductor term obeys the exact computable bound

    |E_(h,q)-E_(h,q;Omega)|
      <=Q^(5/2)/(D ell^6)
         [phi(q) sum_r |a_(h,q)(r)|^2]^(1/2)
         ||B-B_Omega||_2.                                  (FT)

For a height cutoff T>=sqrt(ell) the tail is zero. Below it no small tail follows from the smoothness of the column W: F still contains the original sharp row/capacity, squarefree and ray masks. Such a decay bound remains to be proved.

## The full A3 face and the exact surviving obstruction

No restriction on A3 occurred: the full face A1=A2=A, A*A3=H^(1/3), A4=A5=A6=1 and its accepted neighborhood are included in the exact F. Completing a literal length-one variable is legal, but its Fourier transform is spread across the full residue group; its inverse sum can undo the corresponding Gauss balance.

For example, at the endpoint v1=v2=v4=v5=v6=1, inversion in those five variables leaves exactly

    [sum_(r|q) a_(h,q)(r)] *
      sum_v F3(v) xi_q(v) 1_((v,h)=1).

The row character is orientation-independent there. An orientation gain would require an actual bound on the coefficient sum. On the general face retain theta(v1) theta(v2)^2 xi_q(v3), with every coupled restriction: v3 is quadratic but v1,v2 retain orientation dependence.

If only powers 1,2,3 are completed after v4,v5 are fixed, the product is

    tau(theta) tau(theta^2) tau(theta^3)
       =xi_q(-1) Q J(theta,theta^2),

where J(theta,theta^2)=sum_z theta(z) theta(1-z)^2 and |J|=sqrt(Q). Its phase generally depends on orientation. Thus (GB) must not be described as elimination of every actual near-face phase.

The unproved task is a quantitative signed estimate for the h,q,K sum in (JD), or a uniform bound for its actual B-weight paired with A, at Q~D^2/(Nh)^2, especially h=1. Cubic orientation orthogonality alone is insufficient: the true weight can concentrate on coherent fibers and depends on q. The old small-conductor/high-gcd sector is unchanged. No BT_sigma, global exponent gain, arithmetic energy lower bound, Lean, zero-location theorem, positive determinant bridge or GRH result follows.

## Diagnostic scope

The accompanying stdlib checker uses exact cyclotomic polynomial arithmetic at split fields F7,F13,F19 and the inert Eisenstein field F25, exact common-prime-deletion complete transforms at modulus 7*13, and exact orientation orthogonality/cubic diagonal/product-fiber counts. These are diagnostics of (GB)/(OP) and the CRT convention, not a uniform incomplete arithmetic estimate. No old covariance sign fixture is rerun.
