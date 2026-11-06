# Literal-ray Fourier recombination before the coherent band triangle

NEW v2 research attempt, 6 November 2026 (v1 preserved; S-supported dual ideal notation clarified). This does NOT reprove the accepted prefix/Mellin/all-j/root-normalization results. It changes the organization of the actual pure two-pivot kernel: work with the literal primary-generator lattice before any source-class/rho decomposition. The resulting finite CRT formula exactly recombines the ray/root components at a common additive modulus, including their induced-conductor frequency support. It exposes a surviving S-local Fourier-mean channel on actual equal-norm columns. No improved band bound is proved. The exact failed cancellation step is stated below.

Inputs are the just-closed intermediate run: HANDOFF-v1 bb9463e0, aggregate5470159d, RUN_CLOSED66473a6f, and the master/current ancestor instructions. Old numeric tables, controls, application audits and finished prefix arguments are inputs only, never rerun. All new files are confined to this new lane and its checks.

## 1. Actual pure family and a new representation-fixed band

Let O=Z[omega], delta=1+2omega=i sqrt(3), area(O)=A=sqrt(3)/2, C0=3/(4pi^2). Retain the ORIGINAL unweighted pure block v2=v3=v4=v5=v6=O, fixed literal u0 unit/S-supported with no good-prime support, S above2,3, the original good SF v1 interval and exact capacity Nu0 Nv1<=H. Thus a=ceil(A1), b=min(ceil(2A1)-1,floor(H/Nu0)), K=sqrt(b), with an empty interval giving0. Keep the accepted actual nodal interpolant G(x), not a uniformly smooth proxy: G(Nv1/A1) is exactly the original row indicator, support[1/2,5/2], amplitude<=1, growing derivatives retained. Here no Mellin/TV/prefix theorem is invoked.

Columns are the COMPLETE original good SF IDEAL annulus D<=Nm<=2D, D>1. Put

    c_m=A_U(m)nu(m)R_m(u0)W(Nm/D),
    A_U(m)=sum_{ab|m,(a,b)=1,Na,Nb<=U}mu(a)mu(b).

One common possibly complex fixed W, unfactored A_U, all distinct ideal/norm fibres, original signs and pair coprimality remain. There is no extra mu(mn). All individual S-values introduced below are explicitly AUXILIARY finite-field values; they do not restore an original forbidden raw row value.

For each coprime column pair m,n let q=mn, Q=Nq=Nm Nn. Define the FINITE residue character

    theta_q(x)=(x/m)_6 conjugate((x/n)_6), x in O/q,

zero at every nonunit modulo q. This is the literal finite-field character, not a claim that an individual source xi is finite order. Each good prime of q has one nontrivial local sextic factor, so theta_q is primitive at q. At this point its restriction to mu6 need not be trivial; it need not define a type0 ideal character.

Use the unique generator alpha(v)=1 mod(3) for every good ideal. The reduction mu6 -> (O/3)^times is a bijection, hence this generator section is multiplicative. Fix ONCE an S-supported ideal c=(gamma_c), divisible by(6), large enough for the actual literal row-ray congruences. Since(q,c)=1, CRT is available. Let gamma_q=alpha(m)alpha(n). For t=k^2, define P_t:O/c->{0,1} to contain ALL of:

* x=1 mod(3), selecting the primary generator of the residual ideal;
* x good at S;
* the actual original ray/literal restriction on alpha(t)x.

It is a finite periodic indicator, independent of m,n. There is no additional artificial row weight. Nonempty ray sets have r_t=sum_{x mod c}P_t(x)>0. An incompatible ray set gives r_t=0 and the entire residual term vanishes. In the pure case all ray dependence after square-divisor inversion is retained in this P_t, not discarded as a convenient constant component.

Before Poisson the exact numerator P_D=D S1AA is

    sum_{(m,n)=1} c_m conjugate(c_n)
       sum_{k good SF,Nk<=K} mu(k)theta_q(alpha(k)^2)
          sum_{x in O}P_{k^2}(x mod c)theta_q(x)G(Nx/L_k),  (1.1)
    L_k=A1/(Nk)^2.

Raw(k,q) collisions are zero in theta_q(alpha(k)^2); retaining the zero is equivalent to restricting(k,q)=1, not dropping the mask. The k cutoff is the ORIGINAL pre-S cutoff. Auxiliary x need not be SF, may share k, and S-nonunits are killed by P. This is precisely the row square-divisor expansion, expressed using literal generators; the original column support has not been changed.

We will Poisson-transform(1.1) at the common lattice modulus cq. The NEW literal additive band is Y<Nbeta<=2Y for beta in O. It is invariant under all six units. This is a representation-fixed actual band of the resulting exact expression. It is NOT declared identical to the old primitive-ideal band Ny in(Y,2Y]: inducing from f_S q to cq imposes frequency divisibilities and fixed S rescalings. The formula below keeps those, rather than transferring a bound between unmatched finite windows.

## 2. Exact CRT Fourier recombination

For gamma!=0 set e_gamma(z)=exp(2pi i Tr(z/(delta gamma))). Define

    P_hat_t(b)=sum_{x mod c}P_t(x)e_gamma_c(bx),
    tau_q=sum_{x mod q}theta_q(x)e_gamma_q(x).

The finite Fourier coefficient of F_t(x)=P_t(x mod c)theta_q(x mod q) modulo cq is

    F_hat_t(beta)=sum_{x mod cq}F_t(x)e_(gamma_c gamma_q)(beta x)
       =tau_q theta_q(gamma_c)conjugate(theta_q(beta))
                           P_hat_t(beta gamma_q^(-1) mod c).       (2.1)

Every term is defined at its actual finite modulus. In particular beta meeting q gives0. Proof: write the CRT residue as gamma_c(gamma_c^-1 x_q)+gamma_q(gamma_q^-1 x_c). The q additive frequency is beta gamma_c^-1, the c frequency beta gamma_q^-1. Primitive finite Gauss Fourier gives bar theta_q(beta gamma_c^-1)tau_q, including its ZERO at a nonunit frequency. At units it equals theta_q(gamma_c)bar theta_q(beta)tau_q. Thus(2.1) is exact for all beta, not just coprime frequencies. Parseval gives|tau_q|=sqrt Q; no unit-root assertion at an induced modulus cq is used.

This is a direct recombination of the source-class/rho/S-conductor bookkeeping. Expanding P_t into finite multiplicative ray characters, inducing each to cq, and re-summing their finite Fourier coefficients gives exactly(2.1), by finite Fourier linearity. Angular source representatives have disappeared because the ORIGINAL literal finite function is being transformed, not because their phases were silently replaced by1. Any primitive conductor drop is encoded by the actual support of P_hat_t(beta gamma_q^-1), with no lifted-Gauss square-root assumption. Class-dependent product norms are STILL Q, not a conductor radical or physical-row norm.

For every L>0, ordinary lattice Poisson gives

    sum_{x in O} F_t(x)G(Nx/L)
       = L/(Nc Q) sum_{beta in O}F_hat_t(beta)
                              dotG(L Nbeta/(Nc Q)),                (2.2)

where dotG(X)=C0^-1/2 integral_0^infinity G(u)J0(2sqrt(Xu/C0))du is the accepted field transform. To check the constant independently: (gamma_c gamma_q)O has covolume A Nc Q and dual vector w_beta=2bar beta/(bar delta bar gamma_c bar gamma_q). The Euclidean transform of G(|x|^2/L) is

    pi L integral G(u)J0(2pi sqrt(Lu)|w_beta|)du
       =A L dotG(L Nbeta/(Nc Q)).

Divide by the covolume to obtain(2.2). The same actual smooth G is used. Its derivative constants may grow; Poisson holds for each fixed D and its infinite dual sum. The new finite band is obtained by retaining only the displayed beta, without any assertion of a uniform finite tail.

Insert(2.1) into(2.2), and then into(1.1). The exact coherent literal band is

    B_Y = sum_{(m,n)=1}c_m bar c_n
       sum_{k good SF,Nk<=K} mu(k)theta_q(alpha(k)^2)
          [L_k tau_q theta_q(gamma_c)/(Nc Q)]
       *sum_{beta in O,Y<Nbeta<=2Y}bar theta_q(beta)
             P_hat_(k^2)(beta gamma_q^-1)
                    dotG(L_k Nbeta/(Nc Q)).                       (2.3)

ALL mu(k), original AU/nu/common W, finite ray means, raw collision zeros, complete columns/equal-norm fibres, nonseparable Q and exact capacity remain BEFORE ANY absolute value. No d inversion is necessary in this representation; in particular no mu(d) has been replaced by its absolute value. Formula(2.3) is valid also with any original coprime-pair restriction retained literally; it does not extend the primitive q character to overlapping columns.

## 3. A surviving S-local mean channel and exact unit cancellation

For beta=gamma_c zeta, equation(2.1) becomes

    F_hat_t(gamma_c zeta)=r_t tau_q bar theta_q(zeta).        (3.1)

The theta_q(gamma_c) factor cancels EXACTLY. This is the ZERO FOURIER FREQUENCY ON THE FIXED S/RAY RESIDUE RING, not the global beta=0 Poisson frequency. The latter is0 because q is nontrivial primitive. Nonzero zeta coprime to q need not be good at S; all these dual modes remain.

For any radial function H(Nzeta) and a unit-invariant finite band,

    sum_{zeta!=0}bar theta_q(zeta)H(Nzeta)
       =0                         if theta_q|mu6 is nontrivial,
       =6 sum_{zeta ideals}bar theta_q(zeta)H(Nzeta)
                                  if theta_q|mu6 is trivial.       (3.2)

Here the ideal sum includes ALL integral ideals, including S-supported ones, and raw q zeros. This is a six-element unit-orbit identity, not an unproved arithmetic cancellation estimate. In the second case theta_q(zeta) means the induced ideal value computed from ANY integral generator of zeta; unit-triviality makes it independent of that choice. NO primary1mod3 generator is asserted for an S-supported ideal. Theta_q is then a genuine angular0/radial0 primitive ideal character with conductor q, so epsilon_q=tau_q/sqrt Q in the accepted different normalization.

On good SF m,n, for epsilon=1+omega, local finite-field powers and multiplication of ideal norms give

    theta_q(epsilon)=epsilon^((Nm-Nn)/6).

Indeed each good prime ideal has norm1 mod6, and(product Np-1)/6 is congruent to sum_p(Np-1)/6 modulo6. Therefore

    theta_q|mu6=1 iff Nm=Nn mod36.                           (3.3)

Thus finite unit recombination cancels the S-mean branch for some actual pairs, but it KEEPS the entire equal-norm coprime fibre. No orientation mean or equal-norm fibre may be deleted on the basis of(3.2).

The contribution of beta divisible by gamma_c in the literal band is consequently EXACTLY

    B_Y^(Smean) = sum_{(m,n)=1,Nm=Nn mod36} c_m bar c_n
       sum_{k good SF,Nk<=K} mu(k)theta_q(alpha(k)^2)
            [6r_(k^2)/Nc] [L_k/sqrt Q]epsilon_q
       *sum_{zeta ideals,Y/Nc<Nzeta<=2Y/Nc}
                  bar theta_q(zeta)dotG(L_k Nzeta/Q).       (3.4)

This contains nonunit dual modes, not merely the already-studied dual UNIT. The finite k factor theta_q(k)^2 is cubic, not1; it remains inside the signed expression at the actual cutoff. There is no completed Euler product or inverse-L replacement here. The complement beta not divisible by gamma_c remains in(2.3). Neither(3.4) nor its real part bounds the whole band from below.

For the basic original ray selecting primary generators and S-goodness, with no further restriction, one may take c=(6), gamma_c=6, Nc=36. Exactly THREE residues modulo6 satisfy x=1 mod3 and x!=0 mod2: (1,0),(1,3),(4,3) in coordinates a+b omega. Hence r_(k^2)=3 for every good k (primary k^2=1 mod3), and

    6r/Nc=1/2.                                             (3.5)

This explicit nonzero coefficient is independent of D. Dropping the original2-adic coprimality condition would instead give4 residues and the WRONG coefficient2/3. Additional actual ray restrictions must use their own r_(k^2), not this unrestricted special value.

## 4. Does this give actual arithmetic cancellation at the pure witness?

It gives the exact cancellation(3.2) in the fixed S-local mean branch, and the genuine q/k-dependent arithmetic term(3.4) which survives it. It does not give the missing D-power. The finite CRT/primary/ray calculation cannot turn the remaining all-norm kernel into a small scalar or a positive Gram matrix.

This is a statement about the actual support, not an arbitrary gauge example: whenever a split rational prime p in(D,2D) has W(p/D)!=0, the complete annulus includes both conjugate prime ideals m=p_+, n=p_-; they are coprime IDEALS with equal normp and satisfy(3.3). In the high window p>U their ACTUAL A_U(m)=A_U(n)=1. At nu=1 the coefficient c_m bar c_n has magnitude|W(p/D)|^2 (and includes the fixed u0 phases); complex common W cannot remove this equal-norm fibre by opposite nodal phases. No assertion about existence/density of such primes in every interval, a real sign of epsilon_q, or noncancellation of the complete orientation sum is made. General nu/u0 phases remain as written. This pair example is a support check, not a whole-kernel lower bound or a fixed-W counterexample.

For the pure critical block A1~H~D^(3/4), a target-sized literal intermediate band would follow from the NEW signed inequality

    |the FULL right side of(2.3)|
         <<_(S,nu,W,eps) B_W^2 D A1 (DA1Y)^eps.             (CB)

This is a sufficient componentwise target, not necessary for the full kernel, where different bands can cancel. One must bound(2.3) with its full beta residue dependence, or establish a justified joint estimate of(3.4) TOGETHER with its other-residue complement. Bounding(3.4) alone is not asserted necessary. At fixed q,k the surviving phase is epsilon_q theta_q(k)^2 bar theta_q(zeta), coupled to dotG(A1 Nzeta/((Nk)^2 Q)), original c_m bar c_n, exact coprime columns and the finite cutoff. None is independent or an arbitrary free phase.

The precise failed step is: 'sum all source classes/rho, then the primitive roots or ray phases have mean zero in each radial band.' Equations(2.1),(3.1)--(3.5) refute that deduction as a finite-local algebraic inference. They do NOT refute(CB) or prove a positive error lower bound. Even in the zero S-local Fourier channel, primitive root numbers and cubic k phases survive, and all equal-norm column orientations remain. Replacing that actual coherent arithmetic moment by a finite unitary norm or a conductorwise square-root Gauss magnitude is exactly the unproved saving step. The previously accepted arbitrary-coefficient norm bounds would return the finished prefix budget; they are deliberately NOT reapplied as a new result here.

## 5. Scope, checks and next arithmetic request

The surviving new theorem is(2.1)--(2.3), the exact S-local mean/unit selection(3.1)--(3.4), and its original-family nonzero local coefficient(3.5). It reorganizes the FULL signed pure expression before any per-d/per-conductor absolute norm. It is not a new large-sieve theorem, a norm-only saving, an infinite-kernel bound, an all-u0/mixed/principal assembly result, PSD, an energy lower bound or GRH.

A NEW exact36-residue finite-S consistency check verifies the complete c=6 Fourier array in Z[omega], finite inversion, Parseval108, the3residue mask and wrong2-deletion control, and the six unit-character projections. It does not evaluate original q/m/n characters or rerun any accepted arithmetic table, phase/control suite, prefix/Mellin proof or exponent grid. Analytic derivation supplies the proof; finite checks only check these new S-local constants.

The next substantive arithmetic input would control the joint annular sextic Gauss-character band moment(2.3), retaining the prescribed A_U/nu/W coefficients, or use direct primal/dual reciprocity to estimate its S-mean term and complementary residues TOGETHER. It must supply a genuine cancellation statement in the actual q-orientation/k/zeta variables. Neither a finite class/ray identity nor epsilon_q being a unit supplies that statement. All existing13/12 whole-two-pivot and9/8 global bounds stay unchanged.
