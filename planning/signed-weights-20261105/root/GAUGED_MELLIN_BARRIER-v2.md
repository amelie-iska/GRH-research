# The gauged coefficient series still has a central reciprocal

5 November 2026. A new exact calculation for the actual squarefree cutoff coefficients, to be reviewed independently. It is an auxiliary coefficient-series calculation after the accepted two-pivot column gauge; it is NOT the original row remainder and does not estimate the q-dependent joint Fourier weight. The published unsigned7/6 bound and every target/scope obligation remain open.

## Actual coefficients and the fixed character

Use O=Z[omega] and delta=1+2omega. The reviewed TWO_PIVOT_APPLICATION-v3 constructs the unique generator Psi(a)=1mod(2delta) for each ideal prime to2delta, proving its exact finite conductor(2delta), norm12, with principal convention Psi((alpha))=alpha for alpha=1mod(2delta) (infinity type(1,0)). Write lambda(a)=Psi(a)/sqrt(Na), a unitary character of infinite order. It is not one of the original finite-order twists. The defining condition and normalization are explicit; no elliptic modularity or zero theorem is assumed here.

For good prime ideals let j(p)=J_p(chi_p,chi_p²), and extend j multiplicatively. On SQUAREFREE columns ONLY, mu(m)j(m)=Psi(m), so rho(m)=j(m)/sqrt(Nm)=mu(m)lambda(m). The actual gauged A coefficient is

    rho(m)A_U(m)=lambda(m)B_U(m),
    B_U(m)=mu(m)A_U(m)
          =sum_(abc=m;Na,Nb<=U) mu(c).                    (1)

All factors in(1) are squarefree and pairwise coprime. For each term,
mu(m)mu(a)mu(b)=mu(c); this proves(1) without changing A_U or replacing overlapping divisor supports by a square. If Nm<=U then B_U(m)=1. In the accepted high window and active annulus it is r_U(m)−1. That last annular formula must not be used for every coefficient of a global Dirichlet series. The Mobius identity itself must not be applied to arbitrary nonsquarefree row factors.

Fix nonzero literal z, the original finite nu and S, and let T contain the FULL deleted set S union supp(z), including conductor-drop zeros. On ideals outside T write Xi=unitary primitive(lambda*nu*kappa_z), with the literal fixed-ray comparison included just as in the original source. Equivalently all formulas may be read for any actual multiplicative unitary ideal character Xi with these retained zeros. Its nonzero infinity type is fixed; the prior theorem stated only for finite-order twists is NOT silently extended. Put x_p=Xi(p)(Np)^(-s) outside T.

## Exact finite-cutoff central denominator

For Re(s)>1 absolute convergence gives

    Jsharp_U^T(s)=sum_(m sf,(m,T)=1) B_U(m)Xi(m)(Nm)^(-s)
                 =N_U^T(s)/L^T(s,Xi),                    (2)

where

    N_U^T(s)=sum_(a,b sf,(a,b)=1,(ab,T)=1;Na,Nb<=U)
           Xi(ab)(Nab)^(-s)
           product_(p|ab)(1−x_p)^(-1).                   (3)

Indeed after fixing a,b in(1), the c sum is
product_(p notin T, p notdividing ab)(1−x_p). Factoring the FULL deleted Euler product gives(2)–(3). The finite numerator is analytic in Re(s)>0: each local denominator in(3) is nonzero there because |Xi(p)|=1. No claim of nonvanishing of N_U is made. In particular U=1 gives EXACTLY

    Jsharp_1^T(s)=1/L^T(s,Xi).                            (4)

This is a legitimate boundary identity, not a high-window or asymptotic counterexample. For general finite U, one must prove any cancellation of central reciprocal poles by N_U; it is not supplied by mu(m)j(m)=Psi(m). In a meromorphic continuation domain the identity must retain both numerator and denominator. There is no assertion that a zero actually lies off the critical line. Nor is a central reciprocal moment identified with a proved numerator moment.

## The opposite-sign two-auxiliary Euler factor

Introduce independent auxiliary variables v,w. The untruncated three-placement generating product for(1) is

    G^T(s,v,w)=product_(p notin T)[1+x_p(alpha_p+beta_p−1)],
    alpha_p=(Np)^(-v), beta_p=(Np)^(-w).                  (5)

This is NOT the ungauged factor1+x_p(1−alpha_p−beta_p). Placement of p in a or b has sign+; placement in c has sign−. In the absolute domain (for example Re(s)>1 and Re(v),Re(w)>=0), exact multiplication gives

    G^T(s,v,w)=L^T(s+v,Xi)L^T(s+w,Xi)/L^T(s,Xi)
                   * H^T(s,v,w),                       (6)
    H_p=[1+x_p(alpha_p+beta_p−1)]
                    (1−x_p alpha_p)(1−x_p beta_p)/(1−x_p).

The first-order terms cancel, and

    H_p−1=[x_p²(alpha+beta−alpha²−beta²−alpha beta)
             +x_p³ alpha beta(alpha+beta−1)]/(1−x_p).     (7)

An explicit open normal domain has Re(s)>0 and EACH of

    2s+v, 2s+w, 2s+2v, 2s+2w, 2s+v+w,
    3s+2v+w, 3s+v+2w, 3s+v+w

with real part greater than1. The eight numerator monomials in(7) prove normal convergence there, locally uniformly. In particular it contains every point with Re(s)>=1/2+eta and Re(v),Re(w)>=0, for positive fixed eta. Indeed |alpha|,|beta|<=1, so |H_p−1|<=C_eta(Np)^(-1−2eta). The sum converges by elementary ideal counting; deleted primes only remove factors. Finite local H factors may vanish, so do not assert a zero-free correction product without examining them. Equation(6) is first an absolute-domain identity; use it meromorphically only where the stated functions are continued.

At v=w=0 one has H_p=1−x_p² and

    G^T(s,0,0)=L^T(s,Xi)/L^T(2s,Xi²).                   (8)

At v=0 it is L^T(s+w,Xi)/L^T(2s+2w,Xi²). These identities check the sign and normalization. The potential central reciprocal in(6) cancels in these PARTICULAR slices. That does not justify deleting it for general v,w or for the finite numerator in(2).

Thus the gauge trades the old auxiliary reciprocal factors for a central reciprocal family with fixed nonzero infinity type. Even if one moves positive auxiliary lines toward zero within the normal region of H, a uniform central reciprocal/zero-residue estimate is still required. A full sharp Perron inversion, endpoint/tail budget or critical-strip family bound is NOT proved here by rewriting the Euler product. Those completed old contour audits are not rerun.

## Why this still does not estimate the actual joint kernel

For a common actual two-pivot weight F and h=1, the reviewed exact identity is

    S_h1^{XY}=D^(-1) sum_q gamma(beta_q)/Q
             sum_(mn=q,(m,n)=1) b_X(m)conjugate(b_Y(n))
             theta_(m,n)(Z) T_(q,F)(theta_(m,n)),          (9)

with b_X=rho*X_U*nu*W and T the ACTUAL q-dependent, squarefree/ray/capacity/raw-masked Fourier sum. X,Y may be C,mu, or high-window A. All generator signs and common complex-W conjugation are retained. Multiplication by rho is a diagonal unitary gauge; in the corresponding kernel its inverse phases remain. It preserves the eigenvalues/operator norm even for an indefinite coprime-truncated matrix. A PSD inference for that h1 matrix is invalid.

A fixed-z coefficient series such as(2) cannot be inserted as a bound for(9) without controlling T_(q,F), the product-frequency lifts, the condition q=mn and all uniformities. Those weights do not form an independent fixed smooth Mellin profile. The pure A1 endpoint already sums the fixed second factor's Fourier transform back to tau(theta)/Q, undoing the extra Jacobi/central completion exactly. No new power follows by retaining only gamma's finite ray phase or treating lambda as an independently trained or arbitrary fixed label.

The concrete target remains the original fixed-profile signed joint sum in the A6=1 mixed/pure neighborhoods. At H=D^(3/4) the published unsigned envelope retains7/6; the desired3/4 still needs5/12 power cancellation with all masks and cutoffs. Equations(1)–(8) give a precise reciprocal bottleneck to retain in any proposed analytic use of the new character. They do not supply that cancellation, positivity, a determinant/zero-location comparison, a new Lean theorem or GRH.
