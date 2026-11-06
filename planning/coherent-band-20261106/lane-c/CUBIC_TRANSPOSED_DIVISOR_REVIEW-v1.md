# Independent review of the actual cubic transposed divisor bands

Verdict: PASS for the exact scoped theorem in planning/coherent-band-20261106/lane-a/CUBIC_TRANSPOSED_DIVISOR_BANDS-v2.md, SHA256 1fcf324837d2d8560b53aa548b916be6488d936af4dcf7001fdc00e68c152e67. This is an independent analytic derivation, not an author checker call or a control/table rerun. The external de Faveri arXiv2610.04045v1 Theorem1.1 remains an explicit submitted-preprint dependency, not a new proved or formalized sieve in this project.

Accepted scope is precisely: original good SF annular IDEAL columns, original ternary AU at1<=U<=sqrt(D), fixed common complex W supported[1,2], fixed nu/S/literal/ray data, original unweighted two-pivot rows and capacity, ONE common source class C/rho=1, and the representation-fixed auxiliary divisor band E<Nd<=2E in the IDENTITY source class,1<=E<=D/2. The theorem is not broadened to other divisor classes, all original source/rho components, arbitrary row weights, principal assembly or the full d sum.

## 1. Primitive identity-class d splitting, with all unitary types

For[d]=1, compare d to the unit in the accepted source conductor lemma: tilde_chi_d is primitive of conductor d, with trivial infinity type. The same fixed psi_C represents a and da because their source class is C. Exact family index multiplicativity therefore gives, as primitive characters,

 xi_da=tilde_chi_d xi_a, cond(xi_a)=a.

This remains true at the legitimate primitive S values; it is not merely a raw equality after deleting S. Since(d,a)=1, the conductors are coprime. The proved global unitary root law has arch correction i^(|0|+|k_C|-|k_C|)=1 and retains the radial cross factors. Multiplying its result by psi_C(da), I independently obtain

 beta_da=epsilon(tilde_chi_d)beta_a
                 tilde_chi_d(a)tilde_chi_a(d).

In particular xi_a(d)psi_C(d)=tilde_chi_a(d); no missing d-dependent radial or angular phase remains. The exact source reciprocity convention gives tilde_chi_d(a)=alpha(1,C)tilde_chi_a(d), so the displayed(3) with SQUARE tilde_chi_a(d)^2 is correct. Unit residual a=O is covered by the already proved unit-conductor root convention; no artificial principal Poisson residue is created by this column-phase identity.

For a,b in the same residual class, the common epsilon(tilde_chi_d) and alpha factors cancel against their complex conjugates. This gives exactly

 beta_da bar beta_db=beta_a bar beta_b
                         (tilde_chi_a bar tilde_chi_b)^2(d).

The character on d is cubic, not sextic or a generic conductor label. If g=(a,b), its primitive good conductor is(a/g)(b/g): at the remaining good primes the local exponents are+2 or-2 mod6 and have exact order3. The residual quotient ideals a/g,b/g have the SAME source class and are coprime, so there is no S conductor. If a=b the primitive character is principal. In every case the raw(d,a*b)=1 mask persists, including common primes g that disappeared from that primitive conductor. It is not restored from the conductor-reduced character.

Common nu(d), raw u0/k/ell/v2 and primitive tilde_chi_d(e/h) factors are unit phases on their allowed support and cancel in the paired expression; zeros remain the full original row mask(d,S a b k v2 z)=1. Ell is supported in v2; e,h and u0 are S-supported, so no missing good frozen factor is hidden. The complex Mellin radial factors do NOT need to cancel: their paired weight is Nd^(2s-1), retained explicitly in(15), and their modulus is what the Cauchy estimate uses.

## 2. Actual cubic family, physical norm parameters and contractions

The already accepted positive primary-generator match is EXACT on good coprime ideals:

 tilde_chi_a(d)=(alpha_a/d)_6,
 tilde_chi_a(d)^2=(alpha_a/d)_3.

At collisions both are zero. Here alpha_a is the original unique generator1mod3; it is not a newly selected conductor generator or an ideal radical. The square maps the fixed positive mu6 embedding to the same mu3 embedding. This identity covers inert prime ideals as well as split ones and does not impose rational-norm squarefreeness.

I checked the pinned primary Section2.3 and Example2.2: its cubic family is precisely(alpha_a/alpha_d)_3 for these primary generators. The d-by-a matrix is that norm matrix or its ordinary transpose; transpose has the same operator norm. Theorem1.1 with n=3 is symmetric up to fixed constants and gives

 ||K||op^2 <<(EL)^eta [E+L+(EL)^(2/3)].

Both indices d and a are SF, hence cube-free, and their PHYSICAL norms are O(E) and O(L). There is no replacement by a conductor parameter Nq_ab~L^2. The extra deletion of2/original S and the fixed sixth-source class selectors are row/column support restrictions inside this cubic positive comparison. The common(d,a) zero is ALREADY the raw cubic family zero, not an arbitrary entry deletion asserted to reduce a norm. The(d,k v2 z) mask is a genuine row projection and bar R_a(z) a column contraction. All other residual phases are column modulations of modulus<=1. Thus there is no generic primitive-family or unproved weighted-row theorem in(10).

## 3. Why the finite Schur repair is substantive and valid

Without the repair, AU(da)W(NdNa/D) would depend on BOTH row and column and could not be fed to a fixed coefficient-vector cubic sieve. The note explicitly identifies and repairs that failed shortcut.

For supported coprime SF d,a the finite polynomial H_da(v,w)=H_d(v,w)H_a(v,w) is exact. With V=floor(U)+1/2, every divisor norm is an integer and the Perron indicator1_(Nr<V) equals the ORIGINAL1_(Nr<=U), including integer endpoint U. For every integer n>=1, |log(V/n)|>=1/(2V+1). Truncated vertical Perron tails obtained by integration by parts therefore give the stated O((V/n)^c U/T) error uniformly for the chosen small c and large finite T. Expanding TWO approximate indicators and summing the3^omega(m) assignments gives(6), including its quadratic(U/T)^2 term.

The rectangle has O(E) rows, O(L) columns and product O(D), while every supported NdNa is<=4D. Noncoprime entries of K are already zero, so H_dH_a is never incorrectly used as AU of a nonsquarefree product. A uniform entry error delta gives Schur-operator error<=delta sqrt(#rows*#cols)||K||, using the Frobenius/max-entry comparison; this is a valid conservative bound. Taking a fixed sufficiently large polynomial T makes that error arbitrarily small relative to||K||. It is not silently discarded.

The finite diagonal Perron integral has row/column maxima bounded by3^omega(d),3^omega(a), and scalar integral O(log(2T/c)^2). Because U<=sqrt(D), V^(2c)=O(1). The resulting Schur norm is D^eta after the usual arbitrary-small exponent relabelling. No infinite-height absolute Perron integral, inverse-zeta continuation, endpoint half-weight, or multiplicativity AU(da)=AU(d)AU(a) is assumed. I also checked compatibility with the independently gated explicit root lemma f07d6228; X=4D covers this rectangle and its support.

For the ORIGINAL complex W, Mellin inversion is absolutely convergent in norm with multiplier bound M(W). It is an integral of two unitary norm diagonals and a unit scalar, not a claim that W factors pointwise. M(W)>=||W||infinity. Its dependence on the actual W or a varying profile's actual seminorm remains explicit.

A one-sided matrix therefore costs M(W)D^eta. The bilinear form uses TWO such vectors: its norm costs M(W)^2 and the SQUARE of the AU multiplier bound, with the arbitrary-small exponent renamed. The displayed theorem does this correctly. A B_W-only assertion uniform over moving profiles has not been substituted.

## 4. Quantitative d vector and coupled inner bounds

On the actual annulus with E<Nd<=2E, possible Na satisfy L/2<=Na<=2L, L=D/E>=2. A bounded number of dyadic subranges has lower endpoint>=1; unit residuals at L/2=1 are allowed by the positive cubic input. W itself restores the original annulus exactly inside the rectangle.

At source s=sigma+i tau, the row magnitude Nd^(sigma-1/2) contributes at most E^(sigma-1/2), while the input column vector has squared norm

 sum_{Na in[L/2,2L]}Na^(2sigma-1)<<L^(2sigma).

Every remaining coefficient factor is a contraction or the controlled AU/W multiplier. Thus the SQUARED norm of each d vector is

 <<M(W)^2D^eta E^(2sigma-1)Theta3(E,L)L^(2sigma)
  =M(W)^2D^(2sigma+eta)Theta3(E,L)/E.

This verifies(11), including the denominator E. The actual second vector is evaluated at conjugate(s) before complex conjugation; it need not give a PSD form. Cauchy in d with|mu(d)|<=1 is legitimate and yields that same bound for their bilinear pairing. This step deliberately does NOT establish Mobius sign cancellation.

A final triangle over O(Z) good dual ideals proves the new inner branch (Z/E)Theta3. Independently, the old positive-d method on this same restricted band has O(E) divisors, coefficient norm O(M(W)^2D^(2sigma+eta)/E) per divisor and residual Phi(Z,L), giving the old Phi branch. Both bound the SAME representation-fixed component, so taking their minimum is valid. No union of unproved estimates or positivity ordering is needed.

## 5. The actual total-dual band and once-only normalization

For Y<NhNz<=2Y the weight has magnitude at mostY^(-sigma); complex phases remain harmless in Cauchy. The legal good-row prefix is Z_h=2Y/Nh>=1 for every Nh<=2Y, keeping a possible good unit row. For the new branch sum_h Z_h<=2Y product_{p in S}(1-1/Np)^(-1). The old branch has the four positive Phi exponents and the accepted fixed-S geometric sum. Proving the two total h estimates separately and then taking their minimum gives exactly the theorem's min{Phi(Y,L),(Y/E)Theta3(E,L)}. No flat S-volume count or missing S mode is introduced.

The ORIGINAL finite pre-S K_ell, e/ell signs and sharp b(v2) remain exact before the bound. Their magnitudes contribute A1^(1-sigma), a finite k majorant zeta_K^S(2-2sigma) for fixed0<sigma<1/2, a fixed finite e sum and tau(v2) for ell. Actual unweighted v2 counting gives A2 with its divisor epsilon loss. The accepted actual-G BV/Gamma L1 constant is uniform at this fixed sigma, independent of its growing higher derivatives. Finally there is ONCE1/D. I obtain exactly(1), including D^(2sigma-1) and Y^(-sigma).

For E~D^(2/3), Theta3/E=O(1), and the old Phi comparator exceeds Y by a positive power for every fixed0<gamma<2/3 when Y=D^gamma. For E~D^(1/2), the new comparator is YD^(1/6), improving the old one for0<gamma<2/5. These monomial comparisons check, but provide no density or actual lower construction. The identity source-class restriction and the unresolved small-d/other-class sectors remain.

## 6. Rough-prime specialization and honest failed step

When d=p is a prime IDEAL with Np>U and p avoids the full union, AU(pa)=AU(a) exactly: no short divisor can include p. This includes inert ideals with nonsquarefree rational norm and uses ideal primeness. Under the ADDITIONAL high-window2D/7<=U^2, active Na<2D/U<=7U, so the previously accepted short lemma gives|AU(a)|=1, including the unit edge. It is correctly used only on this rough auxiliary support, not globally on AU(m).

After the fixed a,b,z modulations are factored outside, the remaining prime sum has the displayed varying-conductor cubic lambda_ab, full T deletion, radial factor Np^(2s-1) and ORIGINAL W product. Since mu(p)=-1 is constant on this prime sector, scalar Mobius cancellation is not supplied. The primitive conductor drop at(a,b) does not shrink T. A principal a=b auxiliary component is not a full-slice obstruction or a legitimate new original diagonal energy: it can cancel against other d components in the exact inversion.

No fixed-field PIT can be imported uniformly over q_ab up to norm4L^2 merely from this identity. The finite-Perron/Schur repair supplies the honest positive cubic norm, but the final d Cauchy and z triangle still lose the sought signed coherence. This is the correct surviving limitation; full signed13/12/global9/8, principal/short/varying-u0 assembly and GRH/determinant/Lean remain unchanged.

No controls, fresh or old numerical matrices/phase tables, builds, browsers, dependency/environment changes, auth/publication actions or source/index mutations were run in this independent review. Exact source and protection pins are recorded in the acceptance receipt.
