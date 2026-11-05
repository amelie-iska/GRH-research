# Centering, raw masks, and the remaining signed Gram target

5 November 2026. Bounded remote-only continuation. This note proves exact algebraic reductions and a precise obstruction to a proposed shortcut. It does **not** improve the accepted analytic envelope or prove an arithmetic energy lower bound. No new source theorem, Lean declaration, GRH conclusion, promotion or publication is claimed.

## Objects and retained hypotheses

Keep K=Q(omega), the literal nonzero element rows 0<N(u)<=H, fixed finite-order nu, fixed S containing primes above 6 and conductor(nu), a single common smooth W supported [1,2], D>1, and 1<=U<=sqrt(D). All column ideals m and convolution ideals a,b,c,d below are squarefree and prime to S unless otherwise stated. Write

    x_m(u)=(u/m)_6,
    I_u = D^(-1/2) sum_m A_U(m) nu(m) W(Nm/D) x_m(u),
    E_u=I_u-P_u,
    A_U(m)=sum_{ab|m,(a,b)=1,Na,Nb<=U} mu(a)mu(b).

The x_m are the ORIGINAL zero-extended symbols: x_m(u)=0 if ((u),m)>1. The independently primitive psi_u and psi_(u,2), their distinct conductors, and the full T(u,d)=S union supp(u) union supp(d) remain those of the accepted Mellin transfer. Recombination of that full-mask initial series, rather than any replacement of a primitive square denominator by a raw-square sentinel, gives the finite I above.

The exact principal residue is retained:

    P_u=1_(psi_u=1) sqrt(D) W_hat(1)
        sum_d beta_U(d) nu(d)x_d(u) rho_T(u,d)/Nd,
    rho_T = (res_(s=1) zeta_K(s))/zeta_K(2)
            product_(p in T)(1+Np^(-1))^(-1),
    beta_U(d)=sum_{ab=d,Na,Nb<=U}mu(a)mu(b).

The accepted bound is ||E||_2^2 << ||W||_infinity^2 (HD)^epsilon [H+D H^(1/3)+(HD)^(2/3)], uniformly U. At H=D^(3/4) its leading exponent is 5/4. Every new analytic inequality below is labelled TARGET, not proved.

## 1. Exact centered Gram form, before inequalities

For each d in beta_U's finite support define

    t_(u,d)=D^(-1/2)nu(d)x_d(u)
       sum_(c squarefree,(c,T(u,d))=1) nu(c)x_c(u)W(Ncd/D),
    r_(u,d)=1_(psi_u=1) sqrt(D) W_hat(1)
            nu(d)x_d(u)rho_T(u,d)/Nd,
    e_(u,d)=t_(u,d)-r_(u,d).

All sums in t are finite. Then exactly

    E_u=sum_d beta_U(d)e_(u,d),
    ||E||_2^2=sum_(d,e) beta_U(d)overline(beta_U(e)) K_H(d,e),
    K_H(d,e)=sum_(0<Nu<=H) e_(u,d)overline(e_(u,e)).       (CG)

K_H is positive semidefinite, since it is the Gram matrix of these actual centered column vectors. This positivity does not give the required small quadratic form at the signed beta_U. In particular, subtracting r_(u,d) is not asserted to be orthogonal projection, row averaging, or column centering: those would require an additional identity which is absent here. Absolute values on beta_U or K_H remove precisely the signed covariance one seeks.

There is a simpler exact split by principal status:

    ||E||_2^2 = sum_(psi_u!=1)|I_u|^2
                +sum_(psi_u=1)|I_u-P_u|^2.              (PS)

No cross cancellation between those two disjoint row sets is possible. Thus principal centering can only change the second term.

## 2. The saturated a1*a2^2 block is wholly nonprincipal

Fix a dyadic X>1 and literal rows whose outside-S ideals are

    (u)_S=a1*a2^2,
    X<=Na1,Na2<2X,  a1,a2 squarefree, (a1,a2)=1,

with a1,a2 nonunit. Fixed S-supported factors and all literal units may be retained; for definiteness the block B_X below has S-part 1 and includes the six generators of each displayed principal ideal. It lies in N(u)<=8X^3. Since nu is unramified outside S, a prime of a1 or a2 has a nonzero exponent 1 or 2 modulo 6 in the outside-S tame Kummer conductor. Therefore primitive psi_u is nonprincipal for EVERY such row. In particular

    P_u=0 and E_u=I_u on B_X.                            (NP)

The accepted max-first-two BGL argument yields for this block

    sum_(u in B_X)|E_u|^2
      << ||W||_infinity^2 (DX)^epsilon
           [X^2 + D X + D^(2/3)X^(5/3)].                (BB)

Indeed R~X^2 and M~X in the accepted block bound. At X~H^(1/3) and H~D^(3/4), the three exponents are 1/2, 5/4, 13/12. The D X term is exactly the saturated D H^(1/3) monomial. Equation (NP) proves that principal residue subtraction does not alter the energy on this block. It does NOT prove that its true energy has size D X. The bound (BB) can be very non-sharp at the actual signed coefficients.

## 3. The shared-prime mask is already present, not an additional saving

For any row subset B define the exact raw Gram kernel

    G_B(m,n)=sum_(u in B) x_m(u)overline(x_n(u)).

Writing g=gcd(m,n), the product inside this sum is exactly zero on ((u),mn)>1. On its coprime locus it is the product of the sextic symbols at primes of m/g and inverse symbols at primes of n/g. Thus the oscillatory primitive conductor outside S is the squarefree symmetric difference (m/g)(n/g), while the zero mask remains the UNION support supp(mn), including primes of g. On the diagonal

    G_B(m,m)=#{u in B : ((u),m)=1}.                      (DZ)

The finite S-unit/ray-class partition and reciprocity identify these same raw symbols with column-indexed primitive theta_m((u)_S), multiplied by the fixed class phases. Their outside-S conductor is exactly squarefree m. A primitive row character with sixth-power primes removed is NOT substituted. This preserves the independently primitive psi_(u,2) convention through the initial exact transfer and never identifies its conductor with that of psi_u.

Consequently, deleting shared primes a second time cannot supply a new gain. In particular, if m=p is a prime ideal with Np>H, then x_p(u) is nonzero for EVERY 0<Nu<=H. If also Np>U, then the actual coefficient is A_U(p)=1, because only a=b=1 meets the cutoff. At the boundary D>H and U<=sqrt(D), this applies to every prime column p in the length-D annulus. There is no algebraic annihilation or small power of D in that mask. This observation concerns an unaffected column subfamily, not a lower bound for the sum with all actual columns.

For an arbitrary coefficient norm estimate the single-pivot D term is natural: on any collection of N columns coprime to one fixed row u0, coefficients proportional to overline(x_m(u0)) make that row's unnormalized amplitude N and have squared norm N. Hence the operator norm is at least N. But the accepted proof applies a separate norm bound after each other row factor is fixed. Those coefficient vectors differ by theta_m(h). Maximizers for distinct h need not coincide. Summing the worst-case D term over all h does NOT prove an operator-norm lower bound of D*(R/M), still less an energy lower bound at A_U. This is the exact failed inference between monomial saturation and true arithmetic obstruction.

## 4. A signed identity exposing what would actually improve the block

Define the genuine long-long complement

    C_U(m)=sum_(ab|m,(a,b)=1,Na>U,Nb>U)mu(a)mu(b).

Inclusion-exclusion in the disjoint three-placement sum gives, for every squarefree m,

    A_U(m)=mu(m)-2 mu(m)1_(Nm>U)+C_U(m).                (LL)

Proof: the unrestricted sum is mu(m). In the exclusion Na>U, summing mu(b) over all b|m/a vanishes unless a=m; thus this exclusion equals mu(m)1_(Nm>U), and likewise for b. Their overlap is C_U. All sums are finite. This also recovers the previously accepted middle sign window when C_U=0.

Because active columns satisfy Nm>=D>U, one has A_U=C_U-mu on the ENTIRE active annulus, with the exact same symbols, nu, W and zeros. Put

    L_u=D^(-1/2)sum_m C_U(m)nu(m)W(Nm/D)x_m(u),
    M_u=D^(-1/2)sum_m mu(m)nu(m)W(Nm/D)x_m(u),
    L_u^c=L_u-P_u.

Then exactly E=L^c-M and

    ||E||_2^2=||L^c||_2^2+||M||_2^2
               -2 Re sum_u L_u^c overline(M_u).         (CV)

No separate analytic residue theorem for L or M is needed to define this identity: P is the ORIGINAL residue above. On B_X it simplifies to L^c=L. In terms of the retained G_B, define Q_B(f,g) by

    Q_B(f,g)=D^(-1)sum_(m,n) f(m)overline(g(n))
          nu(m)overline(nu(n))W(Nm/D)overline(W(Nn/D))G_B(m,n).

Then sum_B |E|^2=Q_B(C_U,C_U)+Q_B(mu,mu)-2Re Q_B(C_U,mu). Each displayed term uses the union mask in section 3. The diagonal alone is Q_B(A_U,A_U)'s exact nonnegative sum of |A_U(m)W|^2 times the count (DZ); the unexplained positive coherence is in the signed off-diagonal sum.

For a fixed 0<sigma<=1/12, a concrete next claim is the following ACTUAL-COEFFICIENT TARGET, uniformly 1<=U<=sqrt(D), fixed nu/S, common W, and 2<=X~D^(1/4):

    Q_(B_X)(A_U,A_U)
      <<_(nu,S,epsilon,sigma) ||W||_infinity^2(DX)^epsilon
           [X^2 + D^(1-sigma) X + D^(2/3)X^(5/3)].       (BT_sigma)

This would save D^sigma in the offending D X contribution of the balanced block. It is not asserted for arbitrary coefficient sequences. It is equivalent to the signed lower bound

    2Re Q_B(C_U,mu) >= Q_B(C_U,C_U)+Q_B(mu,mu)-R_sigma,

where R_sigma is the proposed right side with one fixed admissible constant. No sign or cancellation of that covariance has been proved. A Cauchy upper bound on its absolute value points in the wrong direction and does not establish this lower bound.

BT_sigma for one balanced block alone does not improve the whole all-ideal envelope: neighboring dyadic blocks with R/M near H^(1/3) must be controlled uniformly too. An exact follow-up is to prove BT_sigma first for these actual nonprincipal a1*a2^2 rows while keeping both squarefree factors inside the signed column quadratic form, then extend it to the near-saturating blocks of the full six-factor decomposition. Principal centering and shared-prime exclusion, by themselves, have no remaining step that supplies it. The competing global mixed term is D^(7/6) at H=D^(3/4), so even eliminating the D^(5/4) term would not establish the desired H-sized energy.

## Evidence and limits

The adjacent stdlib checker verifies (LL), exact raw masked Gram products, the L-M covariance identity on actual nonprincipal a1*a2^2 Eisenstein rows, principal sixth-power zero sentinels, and a prime-column example with every row coprime. Finite profiles in that checker are rational annular polynomials, not a claimed analytic replacement of the common smooth W. No numerical estimate of BT_sigma is used as evidence of an infinite theorem. There is no seed and no stochastic input.

Source dependencies are the already accepted full-mask Mellin transfer and the already reviewed BGL envelope; this note adds no external analytic source. Previous exact sign-window and sieve audits remain completed rather than being re-reported as a new improved moment. Only the assigned frontier planning/check directories were written; all previous files, queue, production documents and output histories are preserved.
