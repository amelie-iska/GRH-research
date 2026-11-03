# Fixed reciprocity period with an explicit common modulus

Status: the exact Gram coefficient period is established in prose using classical cubic reciprocity and abelian class field theory, with those external dependencies named below. An explicit, deliberately nonminimal common defining modulus replaces a finite-family existence assertion. Thirteen Lean components check the actual Eisenstein algebra modulo4 and its phase table/period; they do not formalize cubic reciprocity, Kummer extensions, conductor-discriminant or lattice Gaussian integration. No GRH scope or new zero-free region is established.

Pinned source: math commit4eaee87548250b2682affda7d05d947c05554bae, September build/paper.tex blob268c4e3206d460c617d3d2129742a72b831b3def, lines570–694,761–1095,3320–3377,7090–7203 and8385–8465. Source clones remain immutable. The previous analytic argument is research/gram-poisson.md.

## 1. The fixed modulus, including higher bad-prime powers

Let F=Q(sqrt(-3)), O=Z[omega], lambda=1+2omega, and let S be the FIXED finite set of prime ideals from the source. It contains primes above2,3 and all primes of every complete fixed character presentation. Fix a generator pi_p for each p in S. Let m_pres be a common multiple of the FULL defining moduli of the fixed ray group T and fixed finite coefficient presentations. Include redundant zero primes, not only primitive conductors. Define integral ideals

    m0=(6)^6 product_(p in S) p^25,
    l_fixed=lcm((12), m_pres, m0).                       (1)

These depend only on the declared fixed arithmetic data. In particular they do NOT depend on C,d,k, the baseZ, or unbounded actual S-valuations of a row. Their prime support is contained in S. The first factor(12) includes the primary class and the period of the reciprocity phase; m0 includes all S unit masks, the auxiliary xi modulus b_* and the fixed symbol chi_·(b_*).

Here is a proof of the common numerator bound, rather than an assumption of conductor uniformity. For a=u product pi_p^e_p with a unit u and0<=e_p<=5, choose xi with xi^6=a. Since F contains mu6, E=F(xi) is cyclic over F of degree dividing6. The faithful character sigma↦sigma(xi)/xi is the power-residue character under ARITHMETIC Frobenius. Its conductor divides the relative discriminant D_(E/F), by conductor-discriminant. If g is the minimal polynomial of xi, integrality and normality give monic g,h in O[X] with X^6−a=gh. The root-difference identity gives

    disc(X^6−a)=disc(g) disc(h) Res(g,h)^2.

All factors are integral and nonzero (a!=0 and characteristic0). The field discriminant divides the power-basis order discriminant(disc(g)), locally also when an integral basis is chosen over a DVR. Finally the discriminant ideal of X^6−a is(6)^6(a)^5. Therefore

    f(chi_·(a)) | D_(E/F) | (disc(g)) | (6)^6(a)^5 | m0.   (2)

The argument includes degrees1,2,3 and reducible X^6−a; it never assumes that the polynomial is the minimal polynomial or that its power basis is an integral basis. At p, the upper conductor exponent is6 v_p(6)+25. For S consisting just of the primes above2,3, these bounds are31 at(2) and37 at(lambda), since v_(2)(6)=1 and v_(lambda)(6)=2. They are upper bounds, not computed exact conductors. Existing presentation moduli may require still larger fixed powers and are retained in m_pres.

Every fixed numerator zeta product pi_p^v_p reduces to e_p=v_p modulo6 on ideals outside S, because the discarded multiplier is a sixth power and no symbol vanishes there. Thus all kappa_(zeta,e) have conductor dividing m0. The case b_* has e_p=1, so its fixed symbol also fits. Negative signed rows use -zeta in the same finite family. This proves one actual common ideal without mistaking a growing good numerator for fixed data.

Classical inputs: [Milne, Class Field Theory v4.03](https://www.jmilne.org/math/CourseNotes/CFT.pdf), V Theorem3.27 and Remark3.28, printedp165 (PDF page174), supplies conductor-discriminant; VIII5.3–5.5, printedp245 (PDF page254), gives Frobenius orientation and ray factorization. The order/polynomial discriminant facts follow from the trace determinant and root-difference identity; compare [Milne, Algebraic Number Theory v3.08](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Proposition2.11, Lemma2.23 and Proposition2.34. These classical theorems are not new or kernel-checked here.

## 2. Why the phase has period4, but the whole coefficient need not have period12

For odd c=a+bomega put

    Gamma(c)=|c|^(-1) sum_(x mod c) e(x²/c),
    e(z)=exp(2 pi i Tr(z/lambda)).

The source four-term evaluation is

    Gamma(c)=[1+i^(-b)+i^a+i^(b-a)]/2.                  (3)

We independently checked its Gaussian derivation. With self-dual measure dmu=(2/sqrt3)dxdy and f_epsilon(z)=e(z²/c)exp(-pi epsilon|z|²), its Fourier transform is

    |c|/(2sqrt(r_epsilon))
       exp(-pi epsilon |c|²|y|²/(4r_epsilon)) e(-c y²/(4r_epsilon)),
    r_epsilon=1+3|c|² epsilon²/16.

The Gaussian determinant is epsilon²+16/(3|c|²), fixing both2 and the measure factor. Divide Poisson by I_epsilon=2/(sqrt3 epsilon). On the original side the class means modulo c give Gamma(c)/|c|. On the dual side replacement r_epsilon→1 costs O_c(1) in phase and O_c(epsilon) in amplitude/damping before that normalization, hence o(I_epsilon). Each of the four classes modulo2 has normalized damped mean1/|c|². The limiting equality gives(3). This is a fixed-c proof; no uniform limit in a moving modulus is being smuggled into it.

The12 units of O/(4) have square subgroup{1,omega,omega²}. Their square-class representatives1,-1,lambda,-lambda form C2×C2. Formula(3) gives values1,1,i,-i. Consequently

    R((-1)^e lambda^f,(-1)^g lambda^h)=(-1)^(eh+fg+fh),
    R(a,b)=Gamma(ab)/(Gamma(a)Gamma(b)).              (4)

This symmetric sign bicharacter is defined also at noncoprime PRIMARY odd pairs; no quotient of zero residue symbols is used. Its diagonal is multiplicative. The residue square class of the ELEMENT -1 must not be replaced by the trivial ideal ray class of(-1).

To connect(4) to actual sextic symbols, use unconditional cubic reciprocity for primary a,b≡1 modulo3: the square of chi_b(a)/chi_a(b) is1 on coprime pairs. For distinct good primes, CRT in the quadratic Gauss sums shows that R(p,q)=chi_p(q)^3 chi_q(p)^3. The sign quotient equals its cube, hence equals R. Multiplicativity extends this to all coprime primary pairs. This derives the needed sextic formula from cubic reciprocity and(3); it does not assume that sextic formula as the proof. The classical cubic law with precisely this primary convention is [Dunn–Radziwill v3, equation1.4](https://arxiv.org/pdf/2109.07463v3), p4. Their later GRH-conditional theorems are not used.

For completeness, the auxiliary G(c)=conjugate(chi_c(4))Gamma(c) also has a fixed phase modulus: cubic reciprocity with the primary element−2 gives chi_c(4)=(−2/c)_3=(c/−2)_3. Thus that factor depends only modulo2 and Gamma only modulo4. On primary ideals the modulus12 fixes the chosen generator's residues modulo3 and4; it therefore supplies a defining ray modulus for G and R. This does not cover the other S-numerators.

A useful exact diagnostic shows why modulus12 for R/G cannot replace the full l_fixed. The primary primes

    pi31=1+6omega, pi43=1−6omega

have norms31,43 and coincide modulo12. For the fixed numerator lambda, their sextic symbols are different. In the two residue fields, omega is5 modulo31 and36 modulo43. Thus

    11^5=6 modulo31=(1+omega),
    30^7=7 modulo43=(1+omega)^5.

It follows that chi_pi31(lambda)=zeta6 while chi_pi43(lambda)=zeta6^5, where zeta6=1+omega. This decisively refutes a proposed universal modulus12 for the kappa family. The SOURCE already explicitly allows higher S-powers; the witness supports that condition, rather than refuting its stated Gram proof.

## 3. Literal two-column coefficient ledger

For fixed primary good C,d and nonzero element k, ignoring a fixed scalar convention, the coefficient before the joint smooth profile is exactly

    a_(C,d,k)(m1,m2)=mu(d) c_sigma(Cd m1) conjugate(c_sigma(Cd m2))
      chi_(d m1)(k) conjugate(chi_(d m2)(−k))
      R(d m1,d m2) L_C(d m1,d m2;k).               (5)

The extension is zero off the primary class or S-units BEFORE inverse characters are evaluated. Here c_sigma(s)=1_(s in sigma) chi_s(b_*)/(tau xi(s)). Its full presentation depends modulo l_fixed, as just proved. Multiplication by the fixed C,d only changes the residue input; it introduces no new modulus. In particular no mask at a growing prime of C or d is fabricated by cancelling fixed finite coefficients.

The common kernel is the artificial bounded extension from the earlier audit, with period rad(C) in each residual column. It remains this extension inside every Mobius term. If d meets C it is identically zero. If d meets k an ORIGINAL zero-extended local symbol makes it zero, including valuations divisible by6. Thus nonzero terms have(d,Ck)=1, with no additional coprimality imposed on m1,m2.

Factor chi_(dm)(±k)=chi_d(±k)chi_m(±k). For k=zeta k_S k_good, reciprocity with zeros retained gives

    chi_m(k)=kappa_(zeta,e)(m) R(k_good,m)
                       product_(p|k_good) chi_p(m)^e_p.    (6)

The kappa factor has conductor dividing m0; R depends only modulo4. Every remaining good local factor depends only modulo p. The negative numerator uses the same finite family with -zeta. Also R(dm1,dm2) depends only on the residues modulo4 of the two columns and d. Combining these facts with(5) gives the actual additive period in EACH column

    r=lcm(l_fixed,rad(C),rad(k)),
    N(r)<=N(l_fixed) q_C q_k.                         (7)

Full defining moduli, primary/S masks and the zero branch are included. Congruence modulo a ray defining modulus implies equality of the ideal-character values on units: their quotient generates a principal ideal with local representative1 modulo that modulus. On nonunits the equal zero branch is taken first. This is the step that turns abstract ray factorization into an additive lattice period.

At a nonexceptional prime p outside C l_fixed with6 not dividing e_p, the only dependence on the m1 residue at p is the nonprincipal chi_p(m1)^e_p up to a unit scalar. All other factors in(5)–(6), including the second column, are independent of that residue by CRT. Since(d,k)=1, multiplication by d is a permutation there. Its field mean is0; complete joint mean0 follows. This supplies the period and zero mode used in the preceding Gram-Poisson lemma, with no dependence on a moving label hidden among the fixed constants.

## 4. Verification and remaining frontier

ReciprocityPeriod.lean uses the ACTUAL quadratic algebra QuadraticAlgebra(ZMod4)(-1)(-1), not coordinatewise multiplication on a pair. It checks omega²+omega+1=0, odd inverses/cardinality/closure, the square-class homomorphism and kernel, the four-term phase table and refinement, the sign bicharacter/diagonal, and period under x→x+4z in the integer Eisenstein quadratic algebra. Its finite proofs use kernel reduction, not native_decide. The full Gaussian formula, cubic law, actual number-field character construction and conductor ideal divisibility remain prose/classical dependencies. No target reciprocity or zero location is assumed in these formal finite statements.

The exact checker tests all12units modulo4, split/inert sextic symbols, repeated exponents and shared zeros, actual row conversions with arbitrary units and S-valuations, and the norms31/43 witness. It does not numerically compute the enormous m0 ray class group or pretend finite samples prove CFT. The selective QuadraticAlgebra cache was added at the unchanged mathlib/manifest pins; existing data/caches remain preserved.

Result: the previously open fixed-period/CRT independence input to Gram is closed IN PROSE under named classical theorems. The initial row/finite Fourier representation, full analytic reflection and arithmetic moment estimates still require their own independent certificates; the source7/8 theorem, perturbed final outer-row/common-signal assembly and GRH are not thereby proved. The formal layer still does not establish the full analytic argument.

Next: rotate to the exact arithmetic reflected-energy identity behind the conditional low bound. Start at September7747–7804 and8005–8238, tracing its use of completed reflection from the actual scalar coefficients, masks and normalized kernel. Establish the identity with its canonical branch conductor and common smooth density, or isolate a precise failure. Do not rerun the now-closed fixed-period/dyadic ledger. The primary spectral determinant/zero-location bridge for convergent approximants remains open; it must not be replaced by assuming universal Jensen positivity or by finite zero tests.
