# Reflected energy: exact arithmetic extraction and the common profile

Status: nine local character/unit-phase/Bochner statements are kernel-checked. The marked reflected block reduces to the explicit quadratic-cubic norm in prose CONDITIONAL ON the canonical completed-theta reflection formula and its cusp support/coefficient theorem. The common smooth-profile estimate is proved from its Mellin kernel and classical gamma estimates. The subsequent hybrid large sieve, global theta identification, outer rows and GRH are not certified by this reduction.

Pinned source: math commit4eaee87548250b2682affda7d05d947c05554bae, September build/paper.tex blob268c4e3206d460c617d3d2129742a72b831b3def. Read1660–2455,2540–2618,2888–3055,7318–7483 and7508–8238. The exact target is the passage7747–8005 to equation(4.6a), not another check of the exponent algebra already in research/low-energy.md. Sources and previous artifacts remain immutable.

## 1. Canonical data retained as an input

Retain the source reflected-block hypotheses: original slot coefficients have product form and are independent of the rows and dual variables; slot supports are disjoint; fixed row restrictions are independent of active tuples and dual variables except the explicit coprimality mask between P and R. These are hypotheses on the original coefficients, not assumptions that the desired reflected coefficients are independent. Arbitrary preexisting row-tuple weights would invalidate the conclusion.

Fix the original arithmetic modulus L and the source canonical branch of completed reflection. Its full sector modulus is M_ref², where M_ref=lambda^12 L^4. Freeze h0, the unit/ramified dual label, all nonresidual base primes, and the source's Ramanujan choices. In particular EVERY j=4 non-slot prime is frozen. Write F_act for the frozen active product, R for the residual j=1 row product and P for the active j=0 marked product. Primes in these three products are distinct on the remaining primal support. Primal collisions with a mark are removed before reflection and later kept as1_[gcd(P,R)=1] or fixed tuple restrictions.

The canonical denominator is c=c_F F_act R P, including nonunit h0. Fix SEPARATE classes of R and P modulo M_ref². Their product class then fixes the common cusp coefficient d, additive character vartheta and kappa_F. Fixing just an arbitrary product condition would impose a pair-dependent restriction and would not prove the coefficient independences used below. The source's cusp automorphy/expansion identification remains an external input, not a theorem established by the finite character checks.

The direct/reflected Bessel and Mellin normalizations in source2280–2406 yield the scalar−i/81 with angular factor conjugate(alpha(c))². Independent review rederived those numerical factors; no missing conductor or q_P power was found. This verifies their consistency assuming the theta expansions, rather than proving those expansions.

## 2. Local scalar and cross-prime phases

At an active good prime p put t=c/p. This is a UNIT modulo p; distinct active primes and the fixed denominator give this fact. The source has sigma_p=lambda²t and epsilon_p=−lambda^(-5)t^(-2). For j!=0,4 the local phase is, apart from its two normalized Gauss constants,

    chi_p(sigma_p)^(-2) chi_p(epsilon_p)^(-j−2).

Factoring the lambda-only term leaves chi_p(t)^(2j+2). For j=4, the epsilon phase is absent and the remaining t exponent is−2, equal to2j+2 modulo6. For j=0, the changed marked sign and Gauss constant are ONE-PRIME scalars; the same t exponent2 remains. Thus every local scalar has form

    xi_(p,j) chi_p(c/p)^(2j+2), |xi_(p,j)|=1,

where xi_(p,j) depends on p,j and the fixed datum but on no other active prime. The Lean unit theorem verifies the underlying integer-exponent identity without dividing any zero symbol.

For distinct primary primes p,q put a=chi_p(q), b=chi_q(p). Classical cubic reciprocity gives a²=b², while a^6=b^6=1. Hence

    a^(2j+2)b^(2k+2)=(a²)^(j+k+2).                (1)

For a residual row j=1 and mark k=0 this is1. For row j=1 and a moving k=4 factor, it is a² and need not be1. A genuine exact witness uses p=1+3omega (norm7), q=4+3omega (norm13):

    chi_p(q)=zeta6, chi_q(p)=zeta6^4,
    a^4 b²=1, but a^4 b^10=zeta6²=omega!=1.

Thus an attempted extension that leaves moving j=4 columns unseparated fails at an explicit pair. The SOURCE already freezes those primes; this is evidence that its restriction is necessary, not a refutation of its stated energy lemma. The pairwise row-mark factors cancel. Row-row, mark-mark and frozen interactions belong respectively to a row scalar, a tuple scalar, or fixed data. The angular alpha(c) factor separates multiplicatively as well.

## 3. Every zero and shared cube occurrence survives

On the extracted dual index

    mu=u lambda^h N_F n (B_F b)^3,

the two moving columns are exactly

    chi_R(nb³)^3=chi_R(nb)^3,
    chi_P(nb³)^(-2)=chi_P(n)^(-2)1_[gcd(P,b)=1].       (2)

Both identities hold at all nonunits. Formally we use actual MulChar powers/inverses: a sixth power is the principal ZERO-EXTENDED character, not the constant1 function. At b=0 in a field and n=1, the second left side is0, whereas deleting its mask gives1. This witness is kernel-checked for an arbitrary field character.

The j=4 divisibility term is split by

    1_(p|n0 b0³)=1_(p|n0)+1_(p not|n0)1_(p|b0).

In the first branch write n0=p n but extract NO occurrence from b0, even if p also divides b0. In the second branch write b0=p b and retain p not dividing n0; extract exactly one cube occurrence. This is a partition of the full support. The source dual n,b may contain allowed S-primes and may share primes. Adding an S-mask to these dual variables would invalidate the identity; for example a numerator−2 is a valid unit modulo a good row prime, despite its support at S. Only the displayed lambda valuation is separated.

To check the normalization, define

    delta(n,b)=d(mu)alpha(mu)vartheta(lambda^4 mu)
                       /[27·3^(h/6)|B_F b|].

The source coefficient theorem gives |delta|<=1, and its denominator is nonzero. From q_mu=3^h q_(N_F n) q_(B_F b)^3 one obtains the EXACT factor

    d(mu)alpha(mu)vartheta(lambda^4 mu)/sqrt(q_mu)
        =27 delta(n,b) q_(lambda^h)^(-1/3)
                       q_(N_F n)^(-1/2) q_(B_F b)^(-1).   (3)

A small Ramanujan or active base j=0 term supplies q_p^(-1/2). An assigned j=4 term supplies q_p^(1/2): assignment to N_F cancels its extracted squarefree inverse root; assignment to B_F leaves q_p^(-1/2). Shared cube occurrences stay inside q_b^(-1) and delta. The scalar27 combines with1/81 to give1/3, with no extra q_P factor.

## 4. Exact marked block and its norm argument

Put nu0=v/2+ell_b+e_lambda/3+(S0+B0)/2, with the source actual frozen log-norms. One may retain the marked root EXACTLY as q_P^(-1/2), rather than replacing it by its nominal scale. With cutoffs kept in one joint profile, the branch is of the form

    U(R)=(1/3) Z^(-nu0) rho(R)
        sum_tuple a(tuple)/sqrt(q_P) 1_[gcd(P,R)=1]
        sum_(n,b) beta(n,b) chi_R(nb)^3 chi_P(n)^(-2)
                           1_[gcd(P,b)=1] F_Y(y_R,y_n,y_b,(y_i)).   (4)

Here |rho|,|a|,|beta|<=1 after the explicit factors have been extracted. Inactive-mark weights q_p^(-1) may remain in the fixed outer scalar; their absolute masses are removed by Hilbert-space triangle before this block. All frozen dual restrictions are retained. The identities(2) put zeros at extracted frozen factors into a fixed row or tuple restriction. The coefficient beta depends on the full dual index but not R,P; a may be a general bounded tuple function but is independent of R,n,b. Original slot product form was needed before assigning inactive/active branches. It is not invented anew at the hybrid norm step.

Set y_R=q_R/Z^H, y_n=q_n/Z^v, y_b=q_b/Z^ell_b and y_i=q_(p_i)/Z^z_i. With

    T_d=2H+2A0+2z_a−N_*−N0−3B0,
    Y=q_(c_F)^(-2) Z^[v+3ell_b+e_lambda−T_d],

multiplicativity gives

    q_mu X/q_c²=Y y_n y_b³ y_R^(-2) product_i y_i^(-2).  (5)

This uses the ACTUAL row cutoff and all individual slot coordinates, including when N_F shares primes with b. It is not reevaluated at shorter rows later added by positivity. No equality H=M−O is needed.

## 5. Common profile estimate from the defined kernel

This analytic step can be proved independently of theta automorphy. Let V and all its Euler derivatives decrease faster than every real power at0 and infinity. Its Mellin transform is entire and rapidly decreasing on each fixed vertical strip, by integration by parts. Define

    R(t)=product_(±) Gamma(1+t±1/6)/Gamma(1−t±1/6),
    V#(x)=(1/2pi i) integral_(sigma) Vhat(−t) R(t) (Kx)^(-t) dt,
    K=(2pi)^4/27.

The first numerator pole is−5/6; reciprocal gamma is entire. On−1/4<=Re t<=A, the vertical Stirling formula gives |R(sigma+iu)|<<_A(1+|u|)^(4sigma), uniformly also for bounded u by continuity. The underlying primary facts are [DLMF5.2](https://dlmf.nist.gov/5.2) and [DLMF5.11.9](https://dlmf.nist.gov/5.11#E9). No L-function zero location is involved.

Rectangular contour shifts are valid by the rapid Mellin bounds. An Euler derivative in x inserts(−t)^j; shifting to−1/4,0,A respectively bounds it by x^(1/4),1,x^(-A), times the source finite Mellin seminorm M_(A,ceil(4A)+j+2)(V). The three bounds imply

    |D_x^j V#(x)| << min(x^(1/4),(1+x)^(-A)) M_(A,ceil(4A)+j+2)(V).

For a monomial h(y)=product y_i^a_i on a fixed compact log box and F_Y(y)=W(y)V#(Yh(y)), the chain rule gives D_i V#(Yh)=a_i D_x V#(Yh), with NO extra power of Y. The monomial h is bounded above/below there. Leibniz and integration by parts in logarithmic Fourier coordinates therefore give

    ||F_Y||_(J,sep)
      << m_A(Y) p_(J+d+2)(W) M_(A,ceil(4A)+J+d+4)(V),
    m_A(Y)=min(Y^(1/4),(1+Y)^(-A)).                  (6)

All constants are uniform in actual labels within the block. This is a homogeneous single-profile seminorm, not a statement that an inhomogeneous tuple norm is small. For a fixed annular block all row, tuple and dual index sets are finite, so Fourier inversion of this ONE joint profile can be interchanged with them. Its density is common to the whole finite row Hilbert space; norm powers have absolute value1 and preserve every arithmetic independence. The weighted Fourier norm is integrable by(6).

Taking m_ker=Z^[−(T_d−v−3ell_b−e_lambda)_+/4] from that linear vector and THEN applying Minkowski yields m_ker² only when the row norm is squared. The new Lean Bochner theorem verifies this order for an actual complete complex normed space and an explicitly integrable common density. It does not manufacture the arithmetic Fourier representation or prove gamma bounds formally. Positive row enlargement is allowed only after separation, with the kernel never evaluated on added rows.

The absolute tail uses the genuine unseparated sum, lattice lambda^(-4)O and the source coefficient bound |d(mu)|/sqrt(q_mu)<=27·3^(4/3). Kernel decay beyond actual argument Z^(tau_ref/2), with a fixed sufficiently large order, absorbs the polynomial row/tuple/lattice cost. This retains the source's whole-dyad removal before Fourier absolutization; no retained dual count is borrowed for the tail.

## 6. What has and has not closed

The arithmetic/normalization/common-profile part of the reduction to(4.6a) survives independent adversarial review; no valid source assertion was refuted. The full canonical theta reflection and cusp-family identification are still inputs. So is the hybrid quadratic-cubic large-sieve estimate: formal phase cancellation is not a mean-square theorem. The per-tuple coefficient exponent is−nu0−z_a/2; the previously checked real low-energy exponent and subset saving remain conditional on those analytic inputs. No new zero-free half-plane or GRH proof follows.

The9 new Lean statements use actual arbitrary-field MulChar objects, complex units/powers and an actual Bochner integral in a complete complex normed space. All110analytic declarations pass warnings-as-errors with standard foundations only. Exact diagnostics cover5058dual-column/partition cases in actual fields7,13,25,252actual local scalars,2592cross-prime phase pairs,50nontrivial moving-j4 pairs and90shared-cube normalization cases. Finite checks do not certify the external theta identity, Stirling analysis or the sieve. No new dependency, cache download, manifest or toolchain change was required.

Next concrete claim: independently verify the hybrid-energy estimate in source7484–7657, including the completed quadratic reduction in2672–2840, BOTH complete Mobius masks, squarefree S-parts of the dual columns, divisor-Cauchy weights and subunit quotient ranges. Check its invocation of the exact primary quadratic/cubic large-sieve theorems, without imposing squarefree rational norm or dropping source S-primes. Prove the bound or exhibit a precise failed step. Do not repeat the now-verified local phase and root-extraction accounting. The full theta/cusp identification and primary arithmetic self-adjoint determinant bridge remain open and distinct.
