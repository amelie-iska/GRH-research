# Actual weighted cutoff: exact double Perron and its contour barrier

5 November 2026. New two-variable attempt, remote Linux only. This proves an Euler factorization, a normally convergent correction region uniform in vertical variables, and exact sharp-cutoff double Perron inversion. It does **not** improve the accepted U loss, establish BT_sigma, bound reciprocal L-functions in the critical strip, locate zeros, or prove new Lean/GRH statements. Production, queue and previous evidence are unchanged.

## 1. Same family and same initial series

Retain K=Q(omega), fixed finite-order nu, fixed S containing primes above 6 and conductor(nu), every literal nonzero element row u, psi=psi_u=prim(nu kappa_u), and the INDEPENDENTLY primitive psi_2=prim(psi_u^2). Let T0=S union supp(u). Incomplete L^T0 deletes all primes in T0, whether or not either primitive conductor retains them. Outside T0, psi is unramified and has modulus one, and psi_2(p)=psi(p)^2. This last assertion is only about surviving primes, not multiplication of zero-extended arrays.

The accepted exact initial identity, first on Re s>1, is

    J_U(s,u)=sum_d beta_U(d)nu(d)chi_d(u)(Nd)^(-s)F_(u,d)(s)
            =sum_(a,b,c pairwise coprime squarefree, avoiding T0;
                   Na,Nb<=U) mu(a)mu(b)psi(abc)N(abc)^(-s).

Here beta_U is the actual truncated convolution and chi is the original raw sextic symbol. The c,d coprimality in F_(u,d), as well as (a,b)=1, is essential. A prime of supp(u) never returns because of a primitive-conductor drop.

Put q_p=psi(p)(Np)^(-s) and t_p=q_p/(1+q_p) for p outside T0. The independently retained original base factor is

    F0(s)=F_(u,1)(s)=L^T0(s,psi)/L^T0(2s,psi_2).

For Re s>1/2 its denominator is controlled by the absolute Euler product. The only possible pole in this half-plane for our finite-order characters is the original principal-row pole at s=1. The equality below keeps this base factor; it does not replace it by an artificial raw-square denominator:

    J_U(s,u)=F0(s) B_U(s),
    B_U(s)=sum_(a,b squarefree,(a,b)=1,avoiding T0;
                  Na,Nb<=U) mu(a)mu(b) product_(p|ab)t_p.

B_U is finite and holomorphic for Re s>0, since |q_p|<1 there. This independently continues each finite-cutoff J_U to Re s>1/2 (meromorphically on principal rows).

## 2. The genuinely two-variable Euler series

Define initially in the absolute region

    F(s,z,w)=sum_(a,b,c pairwise coprime squarefree,avoiding T0)
       mu(a)mu(b)psi(abc)N(abc)^(-s)(Na)^(-z)(Nb)^(-w).

Writing sigma=Re s, x=Re z, y=Re w, an absolute-convergence region is

    sigma>1, sigma+x>1, sigma+y>1.                    (A)

Indeed the absolute local majorant is 1+(Np)^(-sigma)
+(Np)^(-sigma-x)+(Np)^(-sigma-y). Multiplying the four allowed placements of a prime gives exactly

    E_p=1+q_p-q_p alpha_p-q_p beta_p,
    alpha_p=(Np)^(-z), beta_p=(Np)^(-w).

There is no q_p^2 alpha_p beta_p term: a=b=p is forbidden. Algebra gives

    (1-q_p)E_p
      =(1-q_p alpha_p)(1-q_p beta_p)
          -q_p^2(1-alpha_p)(1-beta_p).

Consequently

    F(s,z,w)= L^T0(s,psi)
       /[L^T0(s+z,psi)L^T0(s+w,psi)] R(s,z,w),       (F)

    R_p=1-q_p^2(1-alpha_p)(1-beta_p)
                 /[(1-q_p alpha_p)(1-q_p beta_p)],
    R=product_(p outside T0)R_p.

This is the proposed exact factorization, with its correction retained.

## 3. Absolute correction region and all vertical variables

A useful open domain for the correction is

    sigma+x>0, sigma+y>0,
    kappa:=2sigma+min(x,0)+min(y,0)>1.               (Omega)

In particular sigma>1/2. On any set with sigma+x>=eta>0,
sigma+y>=eta>0 and kappa>=1+epsilon,

    |R_p-1| <= 4 (1-2^(-eta))^(-2) (Np)^(-1-epsilon).

Proof: |1-alpha_p|<=2(Np)^(-min(x,0)), and similarly for beta; the two denominators have modulus at least 1-(Np)^(-eta). The prime-ideal majorant is summable. The product is therefore normally convergent and holomorphic on Omega, with a uniform upper bound exp(C_eta sum_p(Np)^(-1-epsilon)). This bound is independent of Im s, Im z, Im w, the particular unitary phases and the deleted set. It permits finite local zeros of R; nonvanishing has not been asserted.

Together with the accepted primitive abelian Hecke continuation, (F) is a meromorphic continuation of F to Omega. Its possible singularities include the original numerator pole and reciprocal-L zero divisors s+z=rho or s+w=rho. Finite deleted factors have no zeros when Re(s+z),Re(s+w)>0, so in this region these zero divisors are exactly those of the corresponding primitive L-function. Formula (Omega) is a sufficient proven region, not a claim of the maximal domain or a natural boundary.

An alternative form is especially important for honest Perron inversion:

    F(s,z,w)=F0(s) G(s,z,w),
    G=product_(p outside T0)(1-t_p alpha_p-t_p beta_p)
      =sum_(a,b squarefree,(a,b)=1,avoiding T0)
             r_(a,b)(s)(Na)^(-z)(Nb)^(-w),
    r_(a,b)=mu(a)mu(b)product_(p|ab)t_p.              (G)

For sigma>1/2, this a,b series is absolutely convergent whenever

    sigma+x>1, sigma+y>1.                           (P)

To see this, |t_p|<=(Np)^(-sigma)/(1-(Np)^(-sigma)), so its absolute Euler product converges under (P). Uniformity on fixed positive margins holds in ALL three vertical variables, including varying u. This proves (G) beyond (A) without evaluating the original infinite c series in the critical strip. The identity with (F) follows from (A) and continuation (or directly by local algebra). The psi_2 denominator remains in F0: when alpha,beta tend to zero the correction becomes product(1-q_p^2)=1/L^T0(2s,psi_2), as required.

## 4. Exact sharp endpoints, including finite-height errors

Every ideal norm is an integer. For any real U>=1 set V=floor(U)+1/2. Then Na<=U is EXACTLY Na<V, and V is not an ideal norm. In particular integer U keeps the complete equality endpoint; it is not silently replaced by a half weight. Also V is comparable to U.

Fix 1/2<sigma<1, and c,d>1-sigma. For T1,T2>0 define

    I_(T1,T2)=1/(2 pi i)^2 int_(c-iT1)^(c+iT1)
               int_(d-iT2)^(d+iT2)
                  F(s,z,w) V^(z+w)/(zw) dw dz.

Then, for s away from an original principal pole,

    J_U(s,u)=lim_(T1,T2 -> infinity) I_(T1,T2),       (DP)

with independent heights tending to infinity. This is an oscillatory limit, not an absolutely integrable infinite vertical integral.

Here is a quantitative proof. Put

    K_(c,T)(v)=(1/(2 pi i))int_(c-iT)^(c+iT)v^z dz/z,
    h(v)=1_(v>1),
    Delta_V=inf_(n integer>=1)|log(V/n)|>0.

The classical one-variable Perron identity follows by closing the Fourier contour. Integration by parts in each omitted tail gives the elementary estimate

    |K_(c,T)(v)-h(v)| <= 2 v^c/(pi T |log v|), v!=1.

Indeed each half-tail is at most 2/(T|log v|) before its 1/(2 pi) normalization. Let

    A(s;c,d)=sum_(a,b)|r_(a,b)(s)|(Na)^(-c)(Nb)^(-d)<infinity.

Termwise integration of the ABSOLUTELY convergent series (G) is legitimate at finite heights, so I_(T1,T2)=F0 sum r K_(c,T1)(V/Na)K_(d,T2)(V/Nb). Since h(V/Na)<=(V/Na)^c, expanding the two kernel errors gives

    |I_(T1,T2)-J_U| <= |F0(s)| A(s;c,d) V^(c+d)
       [2/(pi T1 Delta_V)+2/(pi T2 Delta_V)
                    +4/(pi^2 T1 T2 Delta_V^2)].     (ERR)

This proves the exact endpoint formula on the intended critical-strip s line, not merely its Re s>1 ancestor. One may use Delta_V>=1/(2V+1), because V=N+1/2 and the nearest logarithmic integer distance is log((N+1)/V)>=1/(2N+2).

If one instead places the unshifted U directly in Perron, h at Na=U has value 1/2. The product yields 1/4 when both equal U. The inclusive coefficient requires the explicit correction obtained from

    1_(Na<=U)=h_half(U/Na)+(1/2)1_(Na=U)

in BOTH variables. The half-integer V convention avoids these boundary terms entirely.

## 5. What can actually be bounded without reciprocal-L input

In the positive-line region (P), both reciprocal incomplete L-factors in (F) satisfy the absolute Euler upper bound zeta_K(sigma+c), zeta_K(sigma+d). R is uniformly bounded by section 3. For a fixed positive line a,

    (1/(2 pi))int_(-T)^T |a+it|^(-1)dt
          =pi^(-1)asinh(T/a) <<_a log(2+T).

Taking T1=T2=V^2, using (ERR), the uniform absolute bound for A and the retained absolute denominator at 2sigma, gives

    |J_U(s,u)| <<_(sigma,c,d,nu,S,eta)
       (Nu)^eta |L(s,psi_u)| V^(c+d) log^2(2V).     (B)

The small row factor bounds the finite numerator-deletion factors, exactly as in the accepted masked transfer; R and reciprocal bounds themselves are phase/deletion-uniform. No average over an unrelated comparable-conductor family is inserted.

Taking c,d arbitrarily close to 1-sigma recovers only

    |J_U| << (Nu U)^eta |L(s,psi_u)| U^(2-2sigma+eta).

At sigma=1/2+delta, squaring gives the SAME U^(2-4delta+eta) loss as the accepted absolute-divisor AFM bound. Inserting the existing original-family numerator moment in the accepted common-W Mellin integral therefore supplies no new U saving. Unequal safe contours cannot help: each must satisfy c>1-sigma, d>1-sigma. The separate previously accepted U-independent sieve envelope is unaffected; no new lower bound is claimed.

## 6. Exact obstruction to moving the two contours

The correction alone allows c,d<0 provided sigma+c,sigma+d>0 and 2sigma+c+d>1; for c=d=-theta this allows theta<sigma-1/2. Thus convergence of R does NOT itself force the positive lines used above. The obstruction is the reciprocal L-factors, together with control of their residues and of the resulting boundary integrals.

For fixed s, any zero rho of L(v,psi) gives a potential auxiliary pole z=rho-s, with multiplicity inherited from the zero, and similarly w=rho-s. Shifting a z line from c>1-sigma toward 0 passes the zero divisors with Re rho>sigma (up to the chosen heights). A denominator pole at v=1 on a principal row instead gives a reciprocal ZERO, not an auxiliary pole. The kernels add poles z=0,w=0.

These reciprocal poles are not a fiction of the factorization: on the coordinate slice w=0 one has exactly

    R(s,z,0)=1, F(s,z,0)=1/L^T0(s+z,psi),

and symmetrically F(s,0,w)=1/L^T0(s+w,psi). Hence arbitrary global cancellation of reciprocal zero divisors by R cannot be assumed. Away from an s zero/pole, the double kernel residue at the origin, when a deformation is permitted, is

    F(s,0,0)=1/L^T0(s,psi).

Sequential contour shifting also has single-residue boundary integrals and any crossed zero residues; it does not equal this double residue alone. A simple zero at rho gives a z residue proportional to V^(rho-s)/(rho-s), with coefficient involving L^T0(s,psi)R(s,rho-s,w)/[L^T0-prime(rho,psi)L^T0(s+w,psi)] before the remaining w kernel. Higher zeros require higher residues. No bound on these coefficients, reciprocal moments, or zero locations is provided by the numerator AFM theorem.

The precise failed step would be to replace the safe lines by fixed lines at or left of zero, discard all s+z=rho and s+w=rho residues, and retain only the kernel residues while continuing to use numerator moments. That step needs a zero-free region and quantitative reciprocal bounds in the swept domain, OR a new signed treatment of the actual zero residues and reciprocal boundary integrals. None has been proved here. Even when a particular fixed character and a finite compact height region happen to admit a deformed path avoiding finitely many zeros, the constants depend on zero distances and conductor; this does not yield the required uniform original-u family estimate over unbounded auxiliary heights. No impossibility theorem for all alternative averaging arguments is asserted.

The auxiliary singularities are in z,w for a fixed chosen s. They are not zeros or poles of the finite-cutoff J_U as a function of s. The latter retains the finite B_U factor and the absolute 2s denominator. A universal pole-free shift to the origin for every sigma>1/2 would already require excluding primitive L zeros with Re rho>1/2, which is exactly the sort of zero-location input that this research must not presume. This contour diagnosis is distinct from merely repeating the older cutoff-limit implication.

## 7. Evidence and next exact obligation

The adjacent checker uses existing stdlib-only exact Eisenstein sextic arithmetic. It tests the local rational identity, global finite-support Euler series, two-cutoff coefficient extraction, raw third/sixth-power zeros, overlapping a=b negative controls, the R=1 slices and the sharp endpoint correction on actual distinct equal-norm prime ideals. The finite checks do not prove normal convergence, vertical bounds, Hecke continuation or zero locations; those derivations are given above with the already accepted classical Hecke input explicit.

Surviving result: the genuine double Perron packaging and uniform correction domain are valid for the ACTUAL beta_U-weighted family. No U improvement results from the available absolute reciprocal bounds. A productive next obligation must estimate the original-family mollified/reciprocal two-variable integral (including any actual zero residues) or the previously identified signed covariance. It must not replace fixed nu by a varying-twist uniformity, restore deleted conductor-drop primes, or relabel an unproved reciprocal estimate as a consequence of numerator AFM.

Read dependencies: README; planning/IMPLEMENTATION_LOOP_PROMPT.md and current continuation; planning/weighted-moment-20261105/frontier/CENTERING_AND_SIGNED_TARGET.md; final independent-acceptance-v2.json and CLARIFICATION_ACCEPTANCE_ADDENDUM.md; papers/masked-moment-core.tex and masked-moment-details.tex; papers/weighted-cutoff-core.tex and weighted-cutoff-details.tex; prior UNIFORM_CUTOFF_MOMENT.md; existing arithmetic-cutoff scripts/README. No repository AGENTS.md or relevant Python lockfile was found. This note adds no new external analytic theorem beyond these inherited primitive abelian Hecke inputs. No installation, MCP, credential, GPU or publication operation was used.
