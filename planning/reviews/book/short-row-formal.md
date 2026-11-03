# Short-row Gram/coherence and uniform primary count

Independent read-only mathematical review, 2026-11-03. No shared sources, scripts, papers, toolchains or outputs were changed. Initial coverage: September build/paper.tex lines590–632,694–722,2650–2845 and7484–7658, the MS_h target in research/exponent-frontier.md §5, and the independent short-row Gram/hybrid reports. This targets the current Gram/coherence implication and necessary term, not another audit of the old reflection phase identities. New formal/article/checker files were not yet present when this initial report was saved; their literal review will be appended.

## 1. Result and scope

The fixed-row arbitrary-coefficient example is valid and shows that the hybrid bound's NB term cannot be removed uniformly. A uniform, explicit lattice-count estimate below supplies its asymptotic without a prime ideal theorem or GRH. This is **not** a counterexample to the actual coefficient vector mu(n)nu(n), nor to the structured reflected cusp coefficients. It identifies the information an improvement must retain instead of discarding it in a positive coefficient-square bound.

The original squarefree Gram retains the common-factor coprimality indicator after phases cancel. Its oscillatory primitive conductor is ab, while a period of the full zero-extended function is hab. Complete off-diagonal orthogonality and positive semidefiniteness are true; neither supplies an upper bound for the short, incomplete off-diagonal quadratic form.

## 2. Uniform primary annular count with explicit constants

Let O=Z[omega], with complex covolume sqrt(3)/2 and norm N(x+y omega)=x²−xy+y². Let q be any squarefree integral ideal coprime to3. For B>0 put

    N_q(B)=#{b in O : b=1 mod3, B≤Nb<2B, (b,q)=1}.

Then

    N_q(B)=c0 B product_(p|q)(1−1/Np)+E_q(B),
    c0=2pi/(9sqrt(3)),

and an absolute, uniform bound is

    |E_q(B)| ≤ C1 sqrt(B) product_(p|q)(1+Np^(−1/2))
                   + C2 2^omega(q),
    C1=4pi(sqrt(2)+1)/(3sqrt(3)),
    C2=4pi/sqrt(3).

The bound is uniform in the actual ideal q, not just a fixed-modulus O(sqrt(B)). It does not claim uniform *relative* error when q grows so quickly that the error dominates its density main term.

Here is a proof of the constants. Complete Mobius insertion gives

    N_q(B)=sum_(d|q) mu(d) N(B;d),

where N(B;d) counts b=1 mod3 and b=0 mod d in the annulus. Since(d,3)=1, CRT specifies exactly one coset of the lattice3d. Eisenstein O is principal, so that lattice is a rotated/scaled copy of O, with covolume A_d=9Nd sqrt(3)/2. A centered fundamental parallelogram is contained in a disk of radius s_d=3sqrt(Nd). This is a conservative radius, sufficient uniformly in its rotation and translation.

For an arbitrary coset, let n_d(R) count its points in the open disk of radius R. The union of centered fundamental cells whose centers lie in that disk is contained in the disk of radius R+s_d and contains the disk of radius max(R−s_d,0), up to boundaries of area zero. Consequently

    |n_d(R)−pi R²/A_d|
       ≤ 4pi R/(3sqrt(3)sqrt(Nd))+2pi/sqrt(3).

Subtracting at R=sqrt(2B) and sqrt(B) gives

    |N(B;d)−c0 B/Nd|
       ≤ C1 sqrt(B/Nd)+C2.

The main divisor sum is product(1−1/Np); the absolute error sum factors into the stated product and divisor count. The open-disk convention produces exactly the half-open annulus B≤Nb<2B, so no boundary lattice points have been silently discarded. No character-sum cancellation or prime asymptotic enters.

For fixed q, its density is positive and its error is O_q(sqrt(B)+1), so N_q(B) is asymptotic to a positive constant times B. Additional fixed good-prime exclusions can be included in q. A fixed positive-angle sector or admissible fixed ray class has the same elementary boundary-cell argument, with its appropriate area/density; no such refinement is needed for the full-annulus obstruction.

For the concrete good prime ideal k0=(1+3omega), Nk0=7, the main term is

    N_k0(B)=4pi B/(21sqrt(3))+O(sqrt(B)+1).

Reduction modulo that prime sends omega to2 in F7, so the excluded residue is x+2y=0 mod7. The primary congruences are x=1 mod3,y=0 mod3. If the fixed excluded set S contains this prime, choose any other fixed good nonunit row; the same argument applies. The norm7 illustration is conditional on its being good, while the general obstruction is not.

## 3. Necessary NB contribution in the exact hybrid inequality

Use the source's allowed fixed row restriction to retain one squarefree good nonunit row k0. Put K=Nk0 and use the bounded annuli N=L=1 containing only n=P=1; a(1)=1. On the B-annulus set

    beta(1,b)=chi_k0(b)^3,

and zero elsewhere. The fixed k0 is part of the example, not a moving coefficient dependence. Thus beta is independent of the variable row k and of P, as required by the lemma. It is bounded by1. Since the quadratic power is real and zero extended, the selected row sum is exactly

    sum_b chi_k0(b)^6 = N_k0(B).

All P=1 masks are1. The energy is therefore asymptotic to a positive constant times B². The source's bound is compatible with this: at N=L=1 its scale is(K+B)B, up to the permitted small power. A K-only replacement would give O(B^(1+epsilon)) for fixed K, contradicted by every fixed epsilon<1. More generally a fixed-power reduction of B to B^(1−delta) fails for epsilon<delta.

The example is inside the source's arbitrary bounded-beta theorem, with a fixed nonunit row; deleting a unit/principal row does not repair that proposed strengthening. It is not the actual reflected beta, nor an allowable replacement for the particular original mu(n)nu(n) vector. The source's printed NB bound is not refuted. The necessary next input must exploit that structured vector or a different arithmetic decomposition.

## 4. Original Gram and the two conductor scales

For a fixed row-independent annular test W, the actual normalized family is

    M_u(D)=D^(−1/2) sum_n c_n chi_n(u),
    c_n=1_((n,S)=1) mu(n)nu(n)W(Nn/D).

Only squarefree columns survive. Expanding the energy over a retained row set U gives exactly

    E=D^(−1) sum_(n,m) c_n conjugate(c_m) G_U(n,m),
    G_U(n,m)=sum_(u in U) chi_n(u)conjugate(chi_m(u)).

If a weight/test varies with u, its two profile values must stay inside that row sum; it is not the same frozen-vector identity without a justified separation.

Write h=gcd(n,m), n=ha,m=hb. These three ideals are squarefree, pairwise coprime and good. At common primes the character phase cancels only on units. The exact function is

    chi_n(u)conjugate(chi_m(u))
      =1_((u,h)=1) chi_a(u)conjugate(chi_b(u)).

The coefficient factors at h cancel because mu(h)²=|nu(h)|²=1 on the specified good support. This does not remove the row mask. The remaining oscillatory character is primitive of conductor ab, since at every prime of a or b it has a nontrivial sextic local component. The complete zero-extended function, including its additional h zeros, has the valid periodic modulus hab=lcm(n,m). On Nh comparable to G and Nn,Nm comparable to D, these norms are D²/G² and D²/G respectively.

CRT gives complete row sum0 off the diagonal and phi(n) on the diagonal over O/lcm(n,m). The unit-column convention must be retained separately: the empty product chi_1 is1, including at zero. Over a larger common modulus Q, the diagonal acquires the repetition factor NQ/Nn. Thus the normalized diagonal mean is phi(n)/Nn, not automatically1.

These direct row-character statements need no reciprocity identity or artificial off-locus extension. They are distinct from the reflected higher-prime-power Gram lemma in the earlier Poisson note.

## 5. What complete mean zero and positivity do not establish

G_U is a genuine Hermitian Gram matrix and is positive semidefinite. This yields a lower bound for its off-diagonal contribution relative to the diagonal; it gives no upper bound of the desired short-row size. Replacing an incomplete ball by a complete period is not justified. For the coprime bulk the modulus norm is about D², while at H=D^(3/4) the row radius is only D^(3/8).

A coefficient vector aligned to one retained row can produce coherent amplitude on that row. This is exactly the mechanism in §3 and in the separate arbitrary-column examples. The arithmetic MS_(3/4) problem instead asks for cancellation of the particular Mobius/ray coefficient vector and all required profile/derivative variants. No new mean-square estimate for that vector has been proved or disproved here. The printed hybrid inequality and its unconditional classical-sieve inputs can remain valid while their arbitrary-beta form supplies no further short-row saving.

## 6. A proved smooth high-common-divisor reduction for the actual original Gram

Here is a positive reduction for the original family, rather than a strengthening of the arbitrary-beta hybrid theorem. Fix once and for all a nonnegative radial Schwartz function Phi on C which is at least1 on the closed unit disk. Assume the column test W is row independent, uniformly bounded and supported on a fixed compact annulus [c,C] in(0,infinity). Put H,D≥1. The actual coefficients satisfy |c_n|≤sup|W|; their support has cD≤Nn≤CD. Primary representatives and the good-prime support are retained. No cancellation of mu or nu is used in this reduction.

For any original retained rows of norm≤H, positivity gives

    sum_(retained u) |M_u(D)|²
       ≤ D^(−1) sum_(u in O) Phi(u/sqrt(H))
                         |sum_n c_n chi_n(u)|².

Dropping primary/good restrictions on the rows is legitimate at this point because the summands are nonnegative and chi_n(u) is defined for every u in O. The fixed row-independent profile assumption is essential. It is not a license to freeze a moving W_u. The right side has its exact weighted original Gram expansion.

For each off-diagonal pair write n=ha,m=hb and set q=ab,Q=Nq. Since representatives are uniquely primary, n≠m implies ab≠1. Let

    psi(u)=chi_a(u) conjugate(chi_b(u)).

This is a nonprincipal primitive multiplicative character of the squarefree ideal q; its local character at every prime dividing q is nontrivial. The primitive oscillatory conductor is q, even though the original zero-preserving pair has the additional h-mask and a period hq.

### 6.1 Primitive completion, including the normalization

For every X>0, the following uniform estimate holds:

    |sum_(v in O) psi(v) Phi(v/sqrt(X))| ≤ C_Phi sqrt(Q).

Here C_Phi depends only on the fixed Schwartz seminorms of Phi and on O, not on X,a,b. A proof with the genuine Gauss normalization is as follows. Poisson summation on each coset modulo q gives the Euclidean Fourier expression

    X/(covol(O) Q) sum_(xi in q*) G_psi(xi) Phihat(sqrt(X) xi),

where q* is the Euclidean dual lattice of q, and

    G_psi(xi)=sum_(r mod q) psi(r) exp(2pi i <xi,r>)

up to an immaterial Fourier-sign convention. The additive character is well defined on O/q. The zero mode vanishes: G_psi(0)=sum psi=0. Since O is principal, q is a rotated/scaled copy of O by a factor sqrt(Q), and q* is correspondingly a rotated/scaled copy of the fixed dual lattice O* by1/sqrt(Q).

CRT factors each finite Gauss sum into local finite-field Gauss sums, with unit CRT phase factors. At a prime of residue cardinality q_p, the multiplicative character is nontrivial. A trivial local additive character gives local sum0; a nontrivial local additive character gives magnitude sqrt(q_p). For completeness, if chi and e are the local multiplicative and additive characters, then substituting x=ty in |sum_x chi(x)e(x)|² gives

    sum_(t≠0) chi(t) sum_(y≠0) e((t−1)y)
      =(q_p−1)−sum_(t≠0,t≠1) chi(t)=q_p.

The inner additive sum is q_p−1 at t=1 and−1 otherwise, while the complete multiplicative sum is0. This proves the required local norm directly, with its zero extension. Therefore every G_psi(xi) has magnitude at most product sqrt(q_p)=sqrt(Q), with no factor from the full hq period. This argument works also for inert primes, whose residue fields have cardinality p²; it is not a model using F_p for every prime.

For A>2 and every r>0, the fixed two-dimensional dual lattice satisfies

    sum_(ell in O*,ell≠0) (1+sqrt(r)|ell|)^(−A) ≤ C_A/r.

For r≤1 this follows by lattice packing and integration over annuli, giving O(r^(−1)); for r≥1 it follows from |ell| bounded away from0 and the convergent sum of |ell|^(−A), giving O(r^(−A/2))≤O(r^(−1)). This bound is therefore valid on BOTH sides of X/Q=1; omitting the zero frequency is indispensable. Schwartz decay, radiality (or uniform rotated seminorms) and r=X/Q now give

    X/Q * sqrt(Q) * O(Q/X) = O(sqrt(Q)).

The covolume and the different only affect fixed lattice constants. This is a proof by actual finite Gauss sums and two-dimensional Poisson summation, not an assumption that arbitrary Fourier coefficients are1.

### 6.2 Removing the full common-factor mask, with every divisor scale

The exact original weighted pair correlation is

    S_H(ha,hb)=sum_u 1_((u,h)=1) psi(u) Phi(u/sqrt(H)).

Full Mobius insertion over ALL d|h, followed by u=dv, gives

    S_H(ha,hb)
      =sum_(d|h) mu(d) psi(d)
          sum_v psi(v) Phi(dv/sqrt(H)).

Each divisor is coprime to ab, so multiplicativity and the zero extensions are respected. A generator d is chosen for the ideal; its unit/rotation changes no bound. Since Phi is radial, the inner profile is exactly Phi(v/sqrt(H/Nd)). In particular the effective scale is H/Nd for EACH divisor; terms with H/Nd<1 are not deleted. The completion estimate just proved applies for every positive scale and yields

    |S_H(ha,hb)| ≤ C_Phi tau(h) sqrt(Nab).

On Nh comparable to G and Nn,Nm comparable to D,

    sqrt(Nab) = sqrt(Nn Nm)/Nh ≤ C D/G,

and the ordinary divisor bound in O gives tau(h)≪_epsilon D^epsilon. The full zero mask has been accounted for by this divisor sum; it has not been silently converted into a character of primitive conductor hab.

At u=0 every nonunit chi_n is0. The empty-product chi_1 is1, so its diagonal contribution must be isolated if the fixed annulus happens to contain n=1. It is D^(−1)|c_1|² Phi(0), and causes no high-divisor or off-diagonal exception. Every off-diagonal psi here is nonprincipal, so psi(0)=0. At u=0 the full divisor identity also holds, including the h=1 case. For large D the annular support excludes the unit column altogether.

### 6.3 Counting pairs and bounding the high-gcd tail

There are O(G) integral principal ideals/primary representatives with Nh in a fixed G-annulus. For each h, the permitted a and b lie in fixed annuli of scale D/G, and there are O(D/G) possibilities each. Here G is at most a fixed multiple of D; bounded ranges near scale1 are covered by the same fixed constants. Enforcing squarefreeness, pairwise coprimality, S exclusions and the two original W supports only decreases this count. Hence the number of pairs in a given h-dyad is

    O(G*(D/G)²)=O(D²/G).

After the original normalization D^(−1), its absolute off-diagonal contribution is at most

    D^(−1) * O(D²/G) * O_epsilon((D/G)D^epsilon)
       = O_epsilon(D² G^(−2) D^epsilon).

The coefficient factors have modulus bounded by a fixed constant. This is an absolute bound on the dyadic contribution and therefore controls it without assuming its sign. Summing the dyads G≥G0 gives the same order O_epsilon(D²/G0² D^epsilon), by a geometric series; a logarithm is not needed for this summation. The diagonal is separately O(H) for H≥1, since sum_u Phi(u/sqrt(H))=O(H) and the number of columns is O(D).

Taking G0=D/sqrt(H) proves that the complete high-common-divisor off-diagonal tail is O_epsilon(H D^epsilon). When H=D^(3/4), the threshold is G0=D^(5/8). This is a genuine reduction of the original smooth mean-square problem: the diagonal and the entire range Nh≥D^(5/8) meet the target scale. The smaller-common-divisor range, in particular h=1, is NOT controlled by this argument. The total target MS_(3/4), its required moving-profile variants, and any zero-free/RH/GRH conclusion remain unproved.

There is a precise profile extension, if needed: the same pairwise proof works with a profile Psi_(n,m)(u/sqrt(H)) depending on the two columns, provided its Schwartz seminorms are bounded uniformly in n,m and in the rotations arising from d. One may use, for example, enough uniform normalized-row derivatives to get Fourier decay exponent A=4. The divisor substitution then uses Psi_(n,m)(rotation_d(v)/sqrt(H/Nd)), whose seminorm bounds are unchanged by rotation up to fixed constants. No separation into a frozen coefficient vector is needed for this high-divisor bound. To apply it to a particular moving W_u, one must verify these derivatives for Phi(z)W_(sqrt(H)z)(Nn/D) conjugate(W_(sqrt(H)z)(Nm/D)); bounds only on column-log derivatives do not establish this hypothesis. This report has not certified that additional source-specific contract.

## 7. Literal formal verification status

The first available in-development ShortRowGram.lean snapshot (143lines) has been fully read. Its intended finite-field character masks, matched-row lower bound, complete finite-field Gram and generic finite Gram expansion have the correct mathematical directions and scopes. The first independent compilation failed while that snapshot was still under development: missing finite-field/unit-group and decidability assumptions, and proof-elaboration failures in the norm/real-part and mod7 calculations. The missing finiteness is substantive in the overgeneralized type: arbitrary characters on infinite fields need not have modulus1. The parent was notified immediately; this is not reported as a passing formal result. A corrected snapshot and the forthcoming article/checker will be independently rechecked before any final certification claim.
