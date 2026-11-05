# A quantitative rough-prime-mask restoration theorem for the actual A–A slice

This is a NEW quantitative mask-error proof, building on the independently accepted exact smooth/rough identity. The exact coefficient lemma below strengthens the earlier epsilon-loss proof only on the restricted rough-prime support. It does not repeat an old data audit. It proves a target-sized bound for the error in restoring the ROUGH PRIME mask only. A secondary bookkeeping corollary also budgets the exact positive unit-residual correction. The mean-retaining signed clean main kernel remains unestimated; no new global exponent, GRH consequence or formalization is asserted. The statement is A–A only. Other coefficient components require their own formulas.

## 1. Hypotheses and exact definitions

Work in O=Z[omega], omega²+omega+1=0. Ideals are nonzero. A good ideal is coprime to fixed S, which contains every prime above2 and3. Thus every nonunit good ideal has norm at least7. Fix a unitary multiplicative nu on good ideals, with defining conductor supported in S in the intended original setup. Fix ONE common complex W, smooth and supported on [1,2], with W(1)=W(2)=0. No profile is chosen separately for a row, prime or divisor. Set B=||W||infinity and assume

    1 <= U,    U² <= D,    2D <= 7U²,    H >= 1.               (1)

Let R be the ACTUAL finite family of nonzero literal rows u, with original weights w_u>=0, Nu<=H, and total weight R_w=sum_u w_u. All internal first-five squarefree/coprime conditions, literal unit and S-ray choices, capacity and any sixth-factor masks stay in this family. Grouping identical literal rows only sums their multiplicities. The original residue characters chi_a(u) are zero on (a,u)>1; these raw zeros remain in every sum below. The theorem does not assume that R is a family of arbitrary primitive characters.

For squarefree g define the ORIGINAL short-divisor coefficient

    A_U(g)=sum_{xy|g,(x,y)=1,Nx<=U,Ny<=U} mu(x)mu(y).          (2)

Let f range over good squarefree U-smooth ideals (every prime norm <=U). The symbol f is separate from the original column-pair gcd sector h=1. Write F=Nf. For a good prime ideal p write P=Np. Define

    T_f(P;u)=sum_{a good SF,(a,f)=1}
                  A_U(fa) nu(a) chi_a(u) W(F P Na/D),
    T_f^(p)(P;u)=the same sum with (a,p)=1.                   (3)

The coprimality (f,u)=1 is imposed outside T; (a,u)>1 remains an ORIGINAL raw zero. The coefficients A_U(fa) are kept unfactored. The S-only extension T_f is an explicitly ARTIFICIAL residual expression when p|a or p|u. In particular, if p|a then fpa is not squarefree, and T_f does NOT claim that A_U(fpa), or an original non-squarefree column, has been inserted into the arithmetic family. When p|u the original common-prime raw phase is zero; its deletion is recorded exactly by the error below.

The following K's are UNNORMALIZED, with every mu(f) sign retained:

    K_T=sum_u w_u sum_{f SF good,U-smooth,(f,u)=1} mu(f)
                   sum_{p good,P>U,p not|u}|T_f^(p)(P;u)|²,
    K_S=sum_u w_u sum_{f SF good,U-smooth,(f,u)=1} mu(f)
                   sum_{p good,P>U}|T_f(P;u)|².              (4)

Neither K is declared positive: its f-weights are signed. Originally the rough common prime had the FULL mask (p,a b u S)=1. The first expression in (4) is exactly that kernel after completing the two residual sums into a square. The second restores ONLY that rough-prime deletion to p notin S. The smooth-f mask (f,a b u S)=1 and all original residual characters remain intact.

For context, define K_0 by replacing P in (3) by1 and summing its square over the same u,f,mu(f). Define the unchanged exact unit-residual correction

    C_two=sum_{{p,q} unordered DISTINCT good prime ideals,
                 Np>U,Nq>U} |W(Np Nq/D)|² sum_{u:(u,pq)=1}w_u.          (5)

The accepted smooth/rough identity gives the original raw coprime A–A slice

    S_AA^raw = (K_0-K_T+C_two)/D.                            (6)

Principal-row residue assembly, if needed, is separate from this raw identity. The intended A1>1 blocks with nu supported in S are nonprincipal. In the S-only expression replace K_T by K_S, retaining K_0 and C_two exactly. Thus the NORMALIZED correction is

    Delta=(K_S-K_T)/D,
    S_AA^raw=(K_0-K_S+C_two)/D+Delta.                        (7)

## 2. The explicit theorem

Put kappa_U(u)=#{good prime ideals p|u:Np>U}. Under (1)-(4),

    |Delta| <= B²[229376 sum_u w_u kappa_U(u)+2048 R_w],
    0 <= C_two/D <=1792 B² R_w.                             (8a)

Consequently the exact clean-main reduction is

    S_AA^raw=(K_0-K_S)/D+E_clean,
    E_clean=Delta+C_two/D,
    |E_clean| <= B²[229376 sum_u w_u kappa_U(u)+3840 R_w]
               <=2^18 B² sum_u w_u[1+kappa_U(u)].           (8b)

The constants are elementary and deliberately crude; no fitted or unknown C_epsilon is assigned a numerical value. In fact the proof requires no D^epsilon loss at all. For general H,

    kappa_U(u)<=2log(Nu)/log(2U)<=2log(2H)/log(2U),          (8c)

so (8b) implies the originally requested epsilon-loss/logarithmic bound with an absolute fixed-field constant. More strongly, if H<=D^(3/4), then kappa_U(u)<=1 for every row, and

    |E_clean| <=233216 B²R_w <2^18 B²R_w.                   (8d)

These constants are uniform in U,D,H,nu,S,R and the common profile apart from B²; no derivative of W is used. The estimate does not remove the smooth-f mask, replace the original row family, estimate the signed main K_S or bound the whole original remainder by its target. It is explicitly A–A only.

## 3. Exact disjoint correction and residual support rigidity

Use the exact disjoint partition of the deleted-prime union:

    1_{p|a b u}=1_{p|u}+1_{p not|u}1_{p|a or p|b}.           (9)

Consequently K_S-K_T=E_row+E_res, where

    E_row=sum_u w_u sum_{f,(f,u)=1}mu(f)
                         sum_{p good,P>U,p|u}|T_f(P;u)|²,
    E_res=sum_u w_u sum_{f,(f,u)=1}mu(f)
              sum_{p good,P>U,p not|u}
                   (|T_f(P;u)|²-|T_f^(p)(P;u)|²).           (10)

At p|u the original chi_a(u) already vanishes whenever p|a; this is consistent with the full-square row term and does not justify deleting the p|u term itself. Equation (9) retains the full union without double counting.

For a nonzero omitted residual summand p|a, write a=p c. Its support implies

    F P² Nc < 2D.                                         (11)

If f c is nonunit, N(fc)>=7 and P>U gives F P² Nc>7U²>=2D, a contradiction. Hence necessarily

    f=1,    c=1,    a=p.                                  (12)

This concerns the artificially extended residual sum, not a new permitted non-squarefree original column. Since P>U, directly A_U(p)=1. Put

    z_p(u)=nu(p)chi_p(u)W(P²/D),    T_p(u)=T_1(P;u).         (13)

It follows that T_f-T_f^(p) is zero unless f=1, where it equals z_p. Therefore the residual correction is EXACTLY

    E_res=sum_u w_u sum_{p good,P>U,p not|u}
                       [2Re(T_p(u)conjugate(z_p(u)))-|z_p(u)|²].        (14)

The term -|z|² is indispensable. It is exactly the intersection p|a AND p|b in the residual union. These identities hold for complex W and all literal character phases. No absolute value or Cauchy has yet been applied to the main K_S.

If z_p is nonzero, then

    sqrt(D)<P<sqrt(2D).                                   (15)

Because U²<=D, the rough condition P>U is automatic on this support. All endpoint equalities have zero profile value.

## 4. Elementary ideal counts and an EXACT restricted coefficient lemma

The counting input needs no prime ideal theorem or Mertens estimate. Every Eisenstein ideal is principal: after rounding both real coordinates of a complex quotient in the basis1,omega, the residual s+t omega has |s|,|t|<=1/2 and norm<=3/4<1. A least-norm nonzero ideal element generates the ideal by Euclidean division. Multiplication by a+b omega has determinant a²-ab+b², so that generator's norm equals the ideal norm. Since a²-ab+b²>=(a²+b²)/2, counting possible generators, with harmless unit overcounting, gives for X>=1

    #{ideals a:Na<=X} <=(2sqrt(2X)+1)²<16X.                (16)

An annulus L<Na<2L contains at most32L ideals when2L>1; if2L<=1, W(Na/L) vanishes, including the unit endpoint. Thus this estimate also covers the genuine unit states when1/2<L<1.

The following exact coefficient identity is stronger than a divisor bound on the support needed here:

    A_U(g)=mu(g)[2·1_(Ng<=U)-1]
                for every good SF g with Ng<=7U.          (17)

The unit ideal is included. To prove (17), every PROPER divisor b of a nonunit good ideal g has Nb<=Ng/7<=U. If Ng<=U, every divisor fits and the unrestricted ternary assignment sum is product_{p|g}(1-1-1)=mu(g). If Ng>U, the only omitted assignments are x=g,y=1 and x=1,y=g; each has sign mu(g). Subtracting these two gives -mu(g). For g=1 the unrestricted sum is1. This proves (17) for every U>=1 without approximating the coefficient.

Now a nonzero term of T_f(P;u), with P>U, has g=fa squarefree and

    Ng<2D/P<2D/U<=7U.                                   (18)

Therefore |A_U(fa)|=1 EXACTLY at every active term. This is a restricted-support identity, not a shrinkage, approximation or proxy for the entire original A_U column family. The signed coefficient in T and in the clean main is unchanged.

Set L=D/(F P). Using (16), (18), |nu(a)|=1 and |chi_a(u)|<=1 yields the loss-free bound

    |T_f(P;u)|<=32 B D/(F P).                             (19)

The sum is zero for L<=1/2; the unit states for1/2<L<1 were counted above. A dyadic application of (16) also gives

    sum_{all ideals f}1/(Nf)²
       <=sum_{j>=0}16·2^(j+1)·2^(-2j)=64.                (20)

The restricted smooth squarefree f-sum is smaller.

## 5. Explicit normalized row-mask budget

Triangle is applied only to the error E_row in (10). Squaring (19), summing f by (20) and dividing by D once gives

    |E_row|/D <=65536 B² sum_u w_u
                         sum_{p|u,good,P>U}D/P².          (21)

The raw square contributed D²/P²; the single normalization leaves D/P². By the high window,

    D/P² <=D/U²<=7/2.                                    (22)

It follows that

    |E_row|/D <=229376 B² sum_u w_u kappa_U(u).             (23)

Each good rough prime norm P is>=7 and>U, hence P²>7U>=2U. The product of distinct such prime norms dividing u is at most Nu. Consequently

    kappa_U(u)<=2log(Nu)/log(2U)
               <=2log(2H)/log(2U).                       (24)

The denominator remains positive at U=1; unit rows have kappa_U=0. All arbitrary sixth-factor primes remain counted, and ideal coprimality is never replaced by rational-norm coprimality.

## 6. Explicit residual intersection budget

Use the exact identity (14), |z_p|<=B and (19) at f=1. The SINGLE division by D gives

    |E_res|/D <=B² R_w sum_{sqrt(D)<P<sqrt(2D)}
                                 [64/P+1/D].             (25)

This is only an absolute correction bound; the exact cross term still has its original phase. Since D>=1 and P<=sqrt(2D)<=2D, one has1/D<=2/P. Also (16) gives

    sum_{sqrt(D)<P<sqrt(2D)}1/P<=16sqrt(2).                (26)

Thus

    |E_res|/D<=1056sqrt(2) B²R_w<2048 B²R_w.               (27)

Combining (23),(27) proves the first part of (8a), with no divisor-power loss.

## 7. Secondary bookkeeping: the EXACT unit-residual correction

This is positive counting, not an oscillatory saving. Each contributing rough pair has P,Q>U and P Q<=2D; hence both norms are<2D/U. By (16), there are at most32D/U such prime ideals, and thus at most

    (1/2)(32D/U)²=512D²/U²                               (28)

unordered DISTINCT pairs. Only INSIDE the nonnegative C_two in (5), enlarge its masked row count to R_w and its profile to B². Then

    0<=C_two/D<=512(D/U²)B²R_w<=1792 B²R_w.                (29)

Distinct conjugate primes of equal rational norm remain included. There is no rational-squarefree restriction, no new diagonal exclusion and no claim of a lower bound for the full signed slice; other residual sectors can cancel this component. The correction remains exactly (5), with (29) merely budgeting its controlled omission. Together with (7),(23),(27), this proves (8a),(8b).

## 8. Target-capacity simplification and the surviving obligation

For H<=D^(3/4), the stronger kappa_U(u)<=1 holds at EVERY scale, not only asymptotically. If two distinct good rough prime ideals divided a row, then H>=Nu>=P Q>=49 and simultaneously H>=Nu>=P Q>U²>=2D/7. Combined with H<=D^(3/4), this gives D^(1/4)<7/2 and hence

    H<=(D)^(3/4)<(7/2)^3=343/8<49,                      (30)

a contradiction. In the preceding strict comparison use directly H>=Nu>=P Q>U²>=2D/7; no approximation of the cutoff endpoints is involved. It follows from (8b) that

    |E_clean|<=[229376+3840]B²R_w
              =233216 B²R_w<2^18 B²R_w.                 (31)

If an actual two-pivot block has R_w<<A1A2<=H, then this is a uniform O(B²H) mask-and-unit-correction budget with no epsilon loss or profile-derivative cost. Its tuple count follows from (16) for the two dyadic ideal variables, with only fixed unit classes and bounded original multiplicities; internal coprimality and capacity reduce the count, while grouping fibers preserves total multiplicity. The general logarithmic estimate (8c) remains available for declared finite capacities H>D^(3/4).

The result is a target-budget equivalence between the ACTUAL raw A–A coprime slice and the clean signed main (K_0-K_S)/D. That main still retains mu(f), the exact A_U(fa), common fixed W, nu, raw residual characters and actual literal row family. It has NOT been bounded here. The complete remainder's old7/6 envelope and missing5/12 saving remain unchanged. This restricted coefficient lemma, correction estimate and positive bookkeeping bound do not furnish a new global exponent, moving-profile counterexample, determinant bridge or GRH proof.
