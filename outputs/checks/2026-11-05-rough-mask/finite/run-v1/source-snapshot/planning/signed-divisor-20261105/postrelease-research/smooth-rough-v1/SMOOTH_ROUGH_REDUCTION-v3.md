# Exact U-smooth/rough reduction of the actual A–A signed divisor mean

This is a NEW post-candidate algebraic reduction, outside the frozen 233-path main selection and 604-file Pages bundle. It supplies no asymptotic saving, global lower bound, GRH consequence or new formalization. The result is explicitly for **A–A**. The other eight components do not inherit the same bracket: mu(ez)=mu(e)mu(z), while the original active-column relation gives C_U(ez)=A_U(z)+mu(e)mu(z) when e is U-rough and nonunit. No source, frozen data, index, bundle or canonical paper is changed here.

## 1. Actual finite slice and hypotheses

Work with ideals of O=Z[omega], using the original literal residue characters chi_m(u), extended by zero when (m,u)>1. Fix S containing all primes above 2 and 3, a unitary multiplicative character nu on good ideals, and one common complex W smooth and supported on [1,2], with its endpoint values zero. All nonunit good ideals have norm at least 7. Let

    1 <= U,    U^2 <= D,    2D <= 7U^2.                         (1)

U may be real; short cutoffs mean the original integer ideal norms <=U. Define exactly

    A_U(m) = sum_{xy|m, (x,y)=1, Nx<=U, Ny<=U} mu(x)mu(y),
    x_m = A_U(m) nu(m) W(Nm/D).                               (2)

Let R be an actual finite literal row family, with its original nonnegative multiplicities w_u and every raw mask retained. The original first-five squarefree/coprime conditions, literal unit/S-ray classes, capacity and any arbitrary sixth factor remain in R; no independent marginal row replacement is made. The algebra below is valid for any such R. In particular it applies to the A6=1 mixed and pure sectors. Grouping genuinely identical literal rows only adds their multiplicities.

Write the raw coprime slice as

    D S_AA^raw = sum_u w_u sum_{m,n good SF, (m,n)=1}
                   x_m conjugate(x_n) chi_m(u) conjugate(chi_n(u)).       (3)

If principal rows are allowed, (3) is still only the RAW slice: the original principal-residue assembly is separate. The intended A1>1 blocks, with the defining conductor of nu supported in S, consist of nonprincipal rows; that conductor hypothesis is used for this qualification, while the raw finite algebra only needs the stated unitary multiplicativity. No h1<=full-energy/PSD inference is used. The original pair-gcd h=1 sector has already been imposed in (3). The smooth factor f introduced below is a different variable: the Mobius expansion allows noncoprime original pairs in intermediate terms, and f=1 does not assert that pair-gcd condition termwise.

Insert the exact common-divisor identity and write m=da, n=db. Residual a,b are good squarefree ideals and MAY OVERLAP. Put

    T = S union supp(a b u),    M=max(Na,Nb), alpha=min(Na,Nb),
    F_ab(x)=W(x Na/D) conjugate(W(x Nb/D)),
    B_ab,u=sum_{d SF,(d,T)=1} mu(d) A_U(da)A_U(db) F_ab(Nd).    (4)

Then exactly

    D S_AA^raw = sum_{a,b good SF} nu(a)conjugate(nu(b))
                    sum_u w_u chi_a(u)conjugate(chi_b(u)) B_ab,u.         (5)

All sums with nonzero terms are finite. On (d,u)=1, the **original** d-dependent phases cancel as |nu(d)|^2 chi_d(u)conjugate(chi_d(u))=1. On (d,u)>1 their product is the raw zero, not 1. These facts, and (d,ab)=1 from squarefree original columns, produce the FULL deleted set T in (4), including common residual primes even if chi_a conjugate(chi_b) becomes imprimitive there. The literal S-ray/unit phases left in (5) are unchanged.

If F_ab(Nd) is nonzero, then

    D/alpha < Nd < 2D/M.                                    (6)

Using closed inequalities instead is harmless because W vanishes at both endpoints. When alpha<=M/2 the profile vanishes identically. The same common W appears in every term; there is no profile supremum or D-dependent phase alignment.

## 2. Rough invariance and the nonunit-residual formula

Factor each squarefree d uniquely as d=f e, where every prime of f has norm <=U and every prime of e has norm >U. Then f,e are coprime and squarefree. For any squarefree product e z, with all prime factors of e of norm >U,

    A_U(e z)=A_U(z).                                        (7)

Proof: neither of the two divisors in (2) can contain a prime ideal of e, since that alone has norm >U. Removing e is therefore a bijection of the original short-divisor assignments, preserving both cutoffs and both Mobius signs. In particular (7) has NO factor mu(e). It is not a factorization of A_U(fa) into a function of f times a function of a.

Suppose M>1. Since a,b are good, M>=7. Equations (1),(6) imply Nd<=2D/M<=U^2. Two rough primes would have product strictly >U^2, so e is either 1 or ONE prime ideal. Thus the exact signed reduction is

    B_ab,u = sum_{f good SF, U-smooth, (f,T)=1}
               mu(f) A_U(fa)A_U(fb)
               [ F_ab(Nf) - sum_{p notin T, Np>U} F_ab(Nf Np) ].         (8)

There is no omitted normalization or extra character/Gauss phase. The factor minus in the prime sum is mu(p). The condition p notin supp(f) is automatic from smoothness, while p notin T is essential. For a fixed f the prime sum has the exact support

    Np>U,    D/(Nf alpha)<Np<2D/(Nf M),    p notin T,           (9)

with endpoints understood through F. Restricting Nf<=2D/M makes (8) visibly finite. Both original coefficients A_U(fa),A_U(fb) remain intact, also when a and b share primes. The statement concerns the rough part of the COMMON divisor d; the full original columns may have additional rough primes in a or b.

## 3. The unit-residual sector has one extra semiprime term

M=1 means a=b=1. Now Nd<=2D, so two rough primes are possible. Three are impossible: two have norm product >U^2 and the third has norm >=7, giving Ne>7U^2>=2D. Moreover, if e contains two rough primes and f is nonunit, then Nf>=7 and Nd>7U^2>=2D. Therefore **the two-rough-prime case has f=1 only**. These strict inequalities also exclude boundary ambiguities.

With T_u=S union supp(u), F_11(x)=|W(x/D)|^2 and A_U(1)=1, one obtains

    B_11,u = sum_{f good SF,U-smooth,(f,T_u)=1} mu(f) A_U(f)^2
                  [ |W(Nf/D)|^2
                    - sum_{p notin T_u,Np>U}|W(Nf Np/D)|^2 ]
               + sum_{{p,q} distinct ideals, p,q notin T_u,
                        Np>U,Nq>U} |W(Np Nq/D)|^2.                       (10)

The last sum is over UNORDERED pairs of DISTINCT prime ideals. Conjugate split primes with the same rational norm are included. Their ideal product is squarefree even when its rational norm is a square. The coefficient is +1: mu(pq)=+1, and the original A_U(pq)=1 because neither rough prime can enter a short divisor.

Equations (8),(10) combine into the exact full identity (5) with the single additional actual-row correction

    C_two = sum_{{p,q} distinct good prime ideals,Np,Nq>U}
                   |W(Np Nq/D)|^2 sum_{u:(u,pq)=1} w_u.                (11)

It is a nonnegative component of the residual decomposition. It is NOT a lower bound for the full signed slice: the other residual sectors can cancel it. Every mask in the inner actual-row count is retained, including sixth-power factors and literal row multiplicities. Division by D occurs once, in (5), when passing to the normalized slice.

## 4. Fresh bounded control and the precise limit

Take D=100,U=7,S above2,3,nu=1 and one fixed profile
W_delta(t)=s((t-1)/delta)s((2-t)/delta), delta=1/20,
where s=0 below0 and s=1 above1 with the standard smooth transition. It equals1 on [21/20,39/20]. The primary literal row u=(-2,-3) has norm7 and lies in the pure first-factor A1=7,A2=...=A6=1 block with H=floor(100^(3/4))=31. Its character is nonprincipal, by valuation1 at the norm7 prime.

The two distinct primary primes p=(1,-3), q=(4,3) both have norm13; pq=(13,0) has norm169. Both primes are rough and coprime to u, so all raw masks survive. The original A_7(pq)=1 and W(169/100)=1. In fact this is the only unordered pair of distinct rough prime ideals whose norm product lies in [100,200]: the next available rough prime-ideal norm after13 is19, and13*19>200. Thus (10)'s indispensable extra term is exactly1 for this row. The selfpair m=n=pq nevertheless contributes zero to the full coprime kernel: across its four common-divisor sectors the coefficients are 1,-1,-1,+1. This explicitly prevents a global lower-bound reading of (11).

A separate coefficient control uses f=(-2,-3) of norm7 and p=(-5,-3) of norm19. Here f is smooth AT the cutoff, p is rough and N(fp)=133 lies in the annulus; directly A_7(fp)=A_7(f)=-1. A conjugate norm7 literal row (1,3) is coprime to fp, so rational-norm coprimality must not replace the ideal mask. These controls are new tiny exact computations; no accepted raw table or old trajectory is called.

What survives is a direct finite signed prime-weight reduction, with no Mellin/Perron interchange. It does not prove a smaller exponent. Triangle on (8) merely replaces its bracket by the absolute profile weights and the number of primes in (9), losing the sign again. A useful next estimate must control the coherent sum in (5) of these smooth-f coefficient weights and rough-prime brackets, together with (11). Pointwise cancellation in f, a generic Mertens assertion, free prime phases, or dropping the unit-residual correction has not been proved. The original 7/6 envelope and missing 5/12 saving are unchanged.
