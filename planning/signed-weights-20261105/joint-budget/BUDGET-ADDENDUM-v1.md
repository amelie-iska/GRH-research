# Unit-column endpoint and the gauged coprime-pair central denominator

This supplements ACTUAL_SIGNED_BUDGET-v1.md without altering its frozen bytes. It adds an explicit small-length proof and a new finite-cutoff two-column coefficient identity. Neither assertion bounds the actual joint Fourier kernel or changes the unsigned7/6 exponent.

## Unit-column endpoint in the proved gcd budget

In equations(7)–(8), L=D/Nd is at least1/2 whenever a column survives. If1/2<=L<1, the residual column a has1<=Na<=2L<2, so only the unit ideal occurs. Hence

    |G_d^XY| << D^eta ||W||infinity² R,

using the actual X_U(d),Y_U(d) bounds and the actual(d,u) mask. Since R>=1 and

    L min{R+LR/M+L^(2/3)R/M^(1/3), L+R²} >= R/2,

equation(8) extends to these d with an absolute constant. No theorem stated only for column length>=1 is applied outside its range. The coefficients X_U(da) remain unfactored throughout; for complex common W and finite nu, the shared nu(d) and chi_d(u) conjugate exactly as in the main proof.

## Independent review of the root's single-column gauged identity

PASS for exact `root/GAUGED_MELLIN_BARRIER-v1.md`, SHA256 `a8c57a59be200633d3edeae3e799ce1901aaa3c0a40318fec4aba84e223812df`. The input Jacobi gauge is independently accepted in `review-phase/REVIEW-v1.md`, which binds TWO_PIVOT_APPLICATION-v3.md. Here lambda=Psi/sqrt(N) is the type-one unitary character, distinct from the raw normalized Jacobi factor rho=mu*lambda on squarefree columns.

For the actual coefficient B_U=mu*A_U, the three placements a,b,c have signs +,+,-, since mu(abc)mu(a)mu(b)=mu(c). Therefore the new local factor is1+x(alpha+beta-1), with the opposite signs to the original A_U factor. Factoring its c-sum yields exactly the finite numerator divided by L^T(s,Xi). Every finite numerator denominator1-x is nonzero for Re(s)>0. The H_p formula and its displayed x²/x³ expansion in the root note multiply correctly, and at the stated margins their deviations are O((Np)^(-1-2eta)). The slices v=w=0 and v=0 are respectively L(s,Xi)/L(2s,Xi²) and L(s+w,Xi)/L(2s+2w,Xi²). These are sign/normalization checks, not permission to discard a central reciprocal for finite U. U=1 is exactly1/L^T(s,Xi). No zero-free statement, Perron tail bound, extension of a finite-order AFM theorem, or actual Fourier-kernel estimate is inferred. Thus the root note's exact algebra and stated analytic boundary pass independently.

## A new JOINT finite-cutoff identity, retaining the coprime column mask

Fix a unitary multiplicative ideal character Xi, for example the fixed-z lambda*nu*Kummer character on its full retained set T. Put

    x_p=Xi(p)(Np)^(-s), y_p=overline(Xi(p))(Np)^(-t),
    M_T(s,t)=product_(p notin T)(1-x_p-y_p).

For Re(s),Re(t)>1 define the actual finite-cutoff, squarefree COPRIME-pair coefficient series

    Jsharp_U,cp(s,t)=sum_(m,n sf,(m,n)=1,(mn,T)=1)
           B_U(m)B_U(n)Xi(m)overline(Xi(n))(Nm)^(-s)(Nn)^(-t).

Write m=abe,n=cdf, with Na,Nb,Nc,Nd<=U. The six ideals a,b,e,c,d,f are globally pairwise coprime, and the coefficient is mu(e)mu(f). Fixing a,b,c,d leaves the two remaining placements e,f with local factor1-x_p-y_p. Consequently EXACTLY

    Jsharp_U,cp(s,t)=M_T(s,t) N_U,cp(s,t),                            (A)

where the FINITE numerator is

    N_U,cp=sum_(a,b,c,d sf pairwise coprime, (abcd,T)=1;
                       Na,Nb,Nc,Nd<=U)
        Xi(ab)overline(Xi(cd))(Nab)^(-s)(Ncd)^(-t)
               product_(p|abcd)(1-x_p-y_p)^(-1).                     (B)

The product divides out each short-placement prime once, rather than treating the two columns as independent. This is the exact shared-prime correction missing from a product of two marginal formulas.

Further,

    M_T=C_T(s,t)/{L^T(s,Xi)L^T(t,overline(Xi))},
    C_T=product_(p notin T)[1-x_p y_p/((1-x_p)(1-y_p))].               (C)

The last product converges normally when Re(s),Re(t)>0 and Re(s+t)>1. In the smaller domain Re(s),Re(t)>1/2, the full deleted set contains the primes above2,3, so every remaining prime norm is>=7 and

    |x_p+y_p| < 2/sqrt(7) < 1.

Thus every denominator in the FINITE(B) is nonzero there, N_U,cp is holomorphic there, and C_T is nonzero there (normal convergence and nonzero local factors). No nonvanishing is claimed for N_U,cp. For U=1, N_U,cp=1 exactly. Therefore the joint gauged finite-cutoff series retains TWO central reciprocal L factors, with a precise coprimality correction. Cancellation at possible zeros for a general finite U cannot be assumed.

The opposite-sign FOUR-auxiliary generating factor for(A) is

    1+x_p(alpha_p+beta_p-1)+y_p(gamma_p+delta_p-1).

There is again no x_p y_p term, since both columns cannot contain p. At all four auxiliaries zero the local factor becomes1+x_p+y_p, the untruncated B_infinity=1 series. This does not license taking U to infinity in the critical strip or replacing finite(B) by that limit.

Equations(A)–(C) are an exact new coprime-pair coefficient identity. They are NOT an identity for the original ungauged row polynomial: its actual two-pivot q-dependent T must still be controlled, as in the main note. A reciprocal estimate for fixed Xi cannot simply be inserted under those frequency/conductor sums. The unchanged concrete sufficient target is(SW), a D^(5/12) signed gain over the proved h1 baseline at the remaining mixed and pure neighborhoods. No such gain is proved here.
