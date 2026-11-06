# Actual long TypeI: fixed twists, growing Gauss frequencies and full deletions

NEW research-only v2,6 November2026. This note gives an exact arithmetic reduction and a quantified SUFFICIENT missing input. It does NOT prove a new Gauss first-moment estimate or an improved bound for the remaining model. The proposed additive-completion step does not supply that input. No completed Euler kernel, generic-conductor sieve, scalar PIT, zero hypothesis or smooth-Gauss theorem is invoked.

## 1. Actual object and precise boundary

Use gauss-book HANDOFF-v1 (2dde46a2), accepted HB-v2 c28af64f, all-component phase package011b68a0 and direct-discrete-v2 4b42c006. We consider the ORIGINAL unweighted pure block v2=O and the other four good factors units, with fixednu/S/u0, ONE fixed possibly complex smooth column profile W supported[1,2] and zero at endpoints. B=||W||infty and M(W)=(2pi)^-1 integral|What(it)|dt. Keep the original complete goodSF annular columns, ordered(m,n)=1, optional ORIGINAL unequal-norm projection, exact source/ray/allrho/primitiveS roots and raw zeros.

The ACTUAL normalized top piece is the direct P_X, not its principal-density mean. V=X^(1/6)/2, X>=64, and

 T_X={(w,s):Nw<64,s good,V<Ns<=2V,Nw(Ns)^6<=X}.

s is arbitrary, w/s and k/s overlap remain legal. The pre-S finiteK=sqrt(b_cap), every e|P_S and primitive eta(e),bar eta(w) value remain. The j0 model L_X^K is still the ORIGINAL finite-k model, with allrho and this exact discrete s set; no kappa_S g(q), rho^6 projector or ray-count approximation occurs here.

Opening mu(m)A_Y(m), a,b are original short factors with coefficient1, Na,Nb<=Y<=D^(1/8). Put P=NaNb and L=D/P. In an unbalanced HB box, c=u*v is the long residual decomposition: v is ONE unrestricted coefficient1 factor, u groups the other HB factors and their signed divisor coefficients. For the exhaustive classification we retain D>=2^64. Its support has Nu<=C L^(1/3), Nv comparable to L/Nu, where C is fixed by at most nine factors. This is a coefficient expansion of the original model, not an extra selected-original-column filter.

Everything below is done at fixed original other column n,k,e,w,s and fixed finite source/ray component. It does not set means tozero or use positivity of a signed component.

## 2. The phase family is smaller than arbitrary lambda

After the accepted exact root formula, finite source-class Fourier expansion and modulo4 Gamma expansion, all long-v dependence can be written as

 psi(v) bar(G_v) chi_(3,v)(alpha_t)
       1_((v,Q)=1) W(Nv/T)/sqrt(Nv),                      (1)

with T=L/Nu and t=a*b*u*k as an IDEAL frequency. The original v dyad gives an additional exact interval indicator I contained in[T,2T]. All a,b,u phases and nonunit e/w primitive zeros stay outside. G_v is the same positive-cubic Gauss sum divided by sqrt(Nv), using the primary1mod3 section and inverse-different pairing.

Here psi belongs to a FINITE FIXED family of bounded multiplicative primary-residue functions. A typical factor list is

 vartheta(v) nu(v) chi_C([v]) chi_H(alpha_v)
 theta_S(alpha_v) product_j chi_(6,v)(z_j)^[sign_j].       (2)

The z_j come from fixedu0, the fixed S generator gamma_S, e and w; allw have norm<64. The notation [+] means the raw symbol and [-] means its CONJUGATE, not inversion atzero. The finite family includes needed conjugate/orientation branches. It is independent of the growing n,k,s,a,b,u. The Gamma Fourier COEFFICIENTS may depend on n, but their total mass is bounded bysqrt12; source coefficients have fixed mass. All primitive S conductor-drop states are included in the fixed finite component label. A zero at an e/w primitive S factor is still a scalar0.

We do not assert that every psi is finite order, nor import a finite-order theorem for it: vartheta has its actual nonzero infinity type. Formula(2), rather than a new conductor classification, defines the fixed functions required by the missing input below. Fixed-numerator residue symbols multiply on coprime denominator ideals including raw zeros, so every psi is bounded and multiplicative on the products actually used.

The full deletion ideal Q is the good-prime radical of a*b*u*n*k*s*w (with all actual fixed exclusions retained in psi/goodness). Q is a deletion ideal, NOT the primitive conductor q=m*n. Redundant primes are deliberately retained. In particular the original pair requires(a*b*u,n)=1 outside and(v,n)=1 inside; the analogous s,k and numerator masks remain. This is not a one-column-only replacement of the actual bilinear mask.

The only growing numerator phase in(1) is cubic:
the Gauss CRT crosses from a*b and u, combined with the original eta(k^2), give chi_(3,v)(alpha_(abuk)) by primary cubic reciprocity. Other-column n enters its scalar root/gauges, finite-selector coefficients and Q, not a new unproved fixed-n Gauss theorem.

On a NONZERO original branch, a,b,u are pairwiseSF/cop rime and(k,abu)=1; otherwise the original raw eta(k^2) kills the whole branch. Hence t=abuk is goodSF. This SF statement does not impose(k,s)=1: k and s may still share primes. A source-class formula off its original class is only an auxiliary coefficient extension; the finite Fourier sum restores the original class.

In the direct model no densityg is inserted. A historical principal-density model would have an extra fixed multiplicative g, and is a different object.

## 3. Exact deletion opening shifts both scale and frequency

For T>0, an exact interval I within[T,2T] with its chosen endpoint conventions, goodSF frequency t and finite good deletion Q, define

 F_psi(T;t;Q,I)
 =sum_(v SFgood,Nv in I,(v,Q)=1)
    psi(v)bar(G_v)chi_(3,v)(alpha_t)W(Nv/T)/sqrt(Nv).      (3)

No frequency unit or nonzero value is divided out. Let I/d mean that same real interval divided by Nd, with the SAME open/closed endpoints. Then EXACTLY

 F_psi(T;t;Q,I)
 =sum_(d|radQ,(d,t)=1)
    mu(d)psi(d)bar(G_d)chi_(3,d)(alpha_t)/sqrt(Nd)
           *F_psi(T/Nd;d*t;1,I/d).                      (4)

Only Nd<2T can be active, apart from zero profile endpoints. Every surviving d is coprime to t because the raw outer chi_(3,d)(t) otherwise vanishes; thus d*t is again SF. Full Q remains in(4), with no replacement by the primitive support of an induced character.

Proof: insert sum_(d|Q,d|v)mu(d), put v=d*z, and keep original squarefreeness as(d,z)=1. On that support,

 bar(G_(dz))=bar(G_d)bar(G_z)chi_(3,d)(alpha_z),
 chi_(3,dz)(alpha_t)=chi_(3,d)(alpha_t)chi_(3,z)(alpha_t).

Reciprocity combines chi_(3,d)(alpha_z) with the second factor into chi_(3,z)(alpha_(dt)). This RAW entry iszero when(z,d)>1, even if an exponent in a numerator happens to be divisible bythree. It therefore encodes the needed(d,z)=1 when the inner sum is written over allSFz. Multiplicativity of psi and the exact W rescaling prove(4). The argument includes the unit ideal and fixed-n masks. It does not complete an Euler series or average a frequency.

At T/Nd in(1/2,1), the only possible inner ideal is the unit; it has its literal W value. At T/Nd<=1/2 the sum iszero (including W(2)=0 at equality). Thus an input valid for lengths>=1 must explicitly be extended over the bounded subunit range by that unit calculation, not by pretending an empty column set.

An unconditional envelope consequence, with B_psi(L;t)=sup_I|F_psi(L;t;1,I)|, is

 |F_psi(T;t;Q,I)|
 <=sum_(d|radQ,(d,t)=1,Nd<2T)
        |psi(d)|/sqrt(Nd) * B_psi(T/Nd;dt).             (5)

This is a frequency/scale transfer, not a saving. In particular it is not a claim that growing deletions cost no conductor parameter for an unknown Gauss theorem.

## 4. A quantified sufficient base input, not an available theorem

Fix 1/2<=alpha<1 and 0<=beta<=alpha with beta<1. Consider the following EXPLICIT HYPOTHESIS H(alpha,beta), only for the finite fixed family(2), goodSF frequencies t and arbitrary exact intervals I in[T,2T]:

 |F_psi(T;t;1,I)|
  <<_(fixeddata,alpha,beta,epsilon)
   M(W)(2+T Nt)^epsilon T^(alpha-1/2)(Nt)^beta, T>=1.     (6)

This must hold also for the conjugated profile/orientation needed on the second column. A theorem only for a full smooth interval, a fixed frequency, an unrelated finite-order family or without uniformity in t DOES NOT supply(6). The sharp HB interval is part of the missing input, not a derivative-free consequence of smoothing. No such theorem is assumed available in this note.

The unit calculation extends(6) to T in[1/2,1) with an alpha-dependent constant. Substituting it in(4) gives

 |F_psi(T;t;Q,I)|
 <<M(W)(2+T Nt)^epsilon T^(alpha-1/2)(Nt)^beta
           sum_(d|radQ)(Nd)^(beta-alpha)
 <<M(W)(2+T Nt)^epsilon T^(alpha-1/2)(Nt)^beta
                                                   (NQ)^epsilon. (7)

Distribute epsilon among these factors as usual. The product of scale and frequency is EXACTLY invariant:
(T/Nd)*N(dt)=T Nt. The divisor weight is Nd^(beta-alpha), including the outer sqrt weight. Since beta<=alpha, its sum is at most tau(radQ)<<epsilon(NQ)^epsilon. This elementary divisor bound uses no Mobius cancellation: finitely many small primes are absorbed, and2<=P^epsilon beyond a fixed threshold.

This establishes a conditional deletion transfer with the precise exponent restriction. If a proposed input has beta>alpha, a Q-power can appear; dropping it would be an invalid uniformity claim.

## 5. Opening the actual HB and short factors: the sharp criterion

Put kappa=(2alpha+beta)/3-1/6. The signed coefficient of u is divisor-bounded, and u<=C L^(1/3). Applying(7) to each actual long-v factor, retaining every outer zero and exact interval, gives

 sum_u |H(u)|/sqrt(Nu) |F_psi(L/Nu;abuk;Q,I_u)|
 << M(W)(D A1 X)^epsilon (P Nk)^beta
                  L^(alpha-1/2) sum_(Nu<=C L^(1/3))
                                           (Nu)^(beta-alpha)
 << M(W)(D A1 X)^epsilon (P Nk)^beta L^kappa.              (8)

The constants depend on alpha,beta. Since beta-alpha>-1, the last step follows from elementary ideal counting and partial summation. The bound is not uniform as alpha->1,beta->0. Finite dyadic/HB logarithms are absorbed in the displayed epsilon.

For clarity, all deletion/frequency epsilon losses really have polynomial material parameters. Here P<=Y^2<=D^(1/4), Nu<=C(D/P)^(1/3), Nk<=sqrt(2A1), Nn<=2D, Ns<=X^(1/6), Nw<64. Therefore

 NQ <<fixed D^(3/2) A1^(1/2) X^(1/6),

and T Nt=(D/(P Nu))*(P Nu Nk)=D Nk in each actual long sum. Neither unknown conductor nor arbitrary ideal labels are substituted.

Now sum the original a,b weights1/sqrt(P) LAST. The bound for the one original column is

 C_I(k)
 <<M(W)(D A1 X)^epsilon (Nk)^beta D^kappa
                          Y^[(4/3)(1+beta-alpha)].       (9)

Indeed each a,b norm sum has exponent beta-kappa-1/2, whose integrated power1/2+beta-kappa=(2/3)(1+beta-alpha)>0. Equal rational norms still count distinct ideals; lattice ideal counting gives O(T) ideals<=T and hence sum_(Na<=Y)(Na)^gamma<<gamma Y^(gamma+1) for gamma>-1. The number of at-most-nine-factor decompositions is r^omega(u)<<epsilon D^epsilon onSFu. These are elementary coefficient/counting bounds, not a Mobius partial-sum estimate.

For each original finite k the other HB-expanded column has the pointwise divisor bound and l1<=B D^(1/2+epsilon). An optional ORIGINAL unequal-norm selector is handled by subtracting its fixed-n norm fibre O(D^epsilon), exactly as in the accepted column theorem; no arbitrary selected norm interval is put into a multiplicative function. Conjugation handles a tail on the other column with no Hermitian assumption.

The finite original k weights are not completed in the identity. Their positive MAJORANT is

 sum_(k SFgood,Nk<=K) (Nk)^(beta-2)
                   <=zeta_K(2-beta)<infinity, beta<1.     (10)

All k/s overlap remains allowed. The exact finite cutoffs and raw zero coefficient functions stay in the model; this inequality does not replace Q2 by an infinite Euler value.

Counting only the actual s band by O(V), with finite w/e/source/rho mass, yields the CONDITIONAL normalized one-TypeI-column leading component bound

 << B M(W)(D A1 X)^epsilon A1 V
              D^(kappa-1/2)Y^[(4/3)(1+beta-alpha)].       (11)

There is exactly one original1/D: it combines (9) with the other-column B sqrt(D). The original capacity and bounded g0 are not changed. The estimate includes BOTH-TypeI components by using the same bound on one of their columns, but it is conditional on the unavailable input(6), not an unconditional solution of those components.

At A1~D^(3/4), X=D^(3/8), V=.5D^(1/16), Y=D^(1/8), (9) has column power

 kappa+(1/6)(1+beta-alpha)=(alpha+beta)/2.

Consequently(11) has power

              5/16+(alpha+beta)/2.                     (12)

Thus alpha+beta<=7/8 is a SUFFICIENT criterion for this long-TypeI component to fit the normalized H=D^(3/4) budget. It is NOT necessary for the component, whole model or final signed target; cross-column/ray/root cancellation could do better. The illustrative choice alpha=5/6 would require beta<=1/24, giving35/48 if beta=0. This is ONLY arithmetic of hypothetical parameters; no5/6 Gauss theorem is invoked or attributed.

If U<D^(1/8), the accepted cutoff usesY=U and its coefficient-tail error is exactlyzero. This note does not replace that Y by a larger value or assert a uniform high-cutoff TypeI gain in that case.

## 6. The attempted additive completion and its exact failed step

The primitive finite identity, including collisions, is

 bar(G_v)chi_(3,v)(alpha_t)
 =1/sqrt(Nv) sum_(x modalpha_v)
     bar(chi_(3,v)(x))
       exp[-2pi i Tr(alpha_t*x/(delta*alpha_v))].          (13)

At units it follows from Gauss frequency change of variable; at a collision both sides arezero by the primitive local character sum. It includes the unit-conductor convention. Formula(13) is an EXACT representation for the long unrestricted coefficient1, not a new bound for its sum over v.

A proposed step was to swap v and x and treat x as one complete fixed-modulus frequency average, then infer cancellation of the v columns. That step is invalid as written: each x lives modulo a DIFFERENT alpha_v and the phase contains its reciprocal. A rigorous common lift does not flatten it.

Indeed for the finite set of relevant SFv let L0 be their ideal lcm and take its primary generator. Write beta_v=alpha_t*alpha_(L0/v). The exact lifted form of(3) is

 1/NL0 sum_(x modalpha_L0) sum_(v in the original support)
     psi(v)W(Nv/T) bar(chi_(3,v)(x))
       exp[-2pi i Tr(beta_v*x/(delta*alpha_L0))].          (14)

The lift of chi_v is defined through its original modulus v, not as a primitive character atL0 or with zeros at every prime ofL0. Each residue modulo v hasN(L0/v) lifts, so the factor in(14) is exactly1/NL0. The additive frequencies beta_v remain v-dependent. A primitive-conductor Gauss bound or common-frequency orthogonality cannot simply be inserted atL0. Original deletion masks are retained in the set of v; no root values at dropped conductors are invented.

Using only the exact magnitude of the primitive Gauss sum and ideal counting gives

                 |F_psi(T;t;Q,I)|<<B sqrt(T),             (15)

with bounded-unit endpoint constants. This is uniform and honest but is just the available trivial alpha1,beta0 certificate, not H(alpha,beta) with alpha<1. At that endpoint the u/a/b sums have logarithms, yielding the inherited O(M(W)D^(1/2+epsilon)) original-column budget and no required D^(-1/16) gain. Formula(14) does not prove that a better coupled method is impossible; it identifies the precise failed completion shortcut.

## 7. Surviving result and next arithmetic task

The proved survivor is the exact all-component fixed-twist/frequency/deletion package(1)-(5), the raw-SF frequency and scale transfer, and the conditional sufficient criterion(6)-(12). It is not a new unconditional target estimate or new sieve. The original allrho exact-discrete leading model, its finite k/e/w/s/source/root means and BOTH-TypeI arithmetic remain. The historical principal-density model and its separate37/48 certificate are not substituted for this actual object.

A genuine next estimate must control the sharply truncated fixed-twist cubic Gauss frequency family(6), uniformly in the SF frequency and the full coupled parameters, OR obtain cancellation in the original n/k/w/s/source pairing before the column triangles. A fixed smooth-frequency theorem without those hypotheses, dropping Q, or declaring the additive lift complete would not do. The already accepted TypeII/large-short/norm/density/scalar routes are not rerun as new progress.

Whole signed13/12/global unsigned9/8 and determinant/zero-location/Lean/GRH obligations remain unchanged. All work is SSH-Linux/new owned paths, no old numerical experiments, source/canonical/book/UI/queue/index/publication/auth/dependency/toolchain/MCP action.
