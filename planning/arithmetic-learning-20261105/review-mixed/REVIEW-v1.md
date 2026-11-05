# Independent review of the compact ordinary-conductor proposals

5 November 2026. Reviewer: arithmetic_readout_design subagent, separately assigned after the mixed-conductor author completed its proposal. Verdict: **PASS** for the exact mathematical assertions in the two compact TeX proposals, and PASS for the production files with the single reference-only amendment specified below. This accepts prose mathematics with the identified classical BGL input. It does not claim formal verification, a signed target estimate, or GRH.

I read the complete compact proposals, full draft, source-pin ledger, prior draft review, accepted uniform-cutoff fragments and the relevant pinned primary-source text. I independently reconstructed the Gauss normalization, additive lattice proof, raw-conductor transfer, tuple bound and global interpolation. Acceptance is based on those derivations, rather than on the prior review or the author's finite grid.

## Frozen objects and production amendment

Proposal core: `planning/arithmetic-learning-20261105/mixed-attempt/mixed-conductor-core-proposal.tex`, SHA256 `aebdea3c68f703a891f48dd481cfecd9bc5b734d50ecb3f8241643cb009a96ff`.

Proposal details: `planning/arithmetic-learning-20261105/mixed-attempt/mixed-conductor-details-proposal.tex`, SHA256 `2362bd5def75d9b9dedc9e64d719f8f98546fb6f8685670fc0cfee88fd79763c`.

Production core: `papers/mixed-conductor-core.tex`, SHA256 `fe3adf4b3e9c4ced71c1d9d341522c4f9ae05065ca1aac5469a84b051e339fe8`.

Production details: `papers/mixed-conductor-details.tex`, SHA256 `2362bd5def75d9b9dedc9e64d719f8f98546fb6f8685670fc0cfee88fd79763c`.

The production core replaces exactly `block bound~\eqref{wc:block}. With` by `block bound from Section~\ref{wc:core}. With`. This repairs a reference to a details-only equation in the concise edition and leaves every mathematical statement unchanged. The details file is byte-identical to its proposal. The review checker verifies these exact byte relations and the presence of wc:core in the common accepted core. This review does not attest rendering or PDF output.

## 1. Primitive Gauss identity, including every nonunit frequency

The primitive additive character e_f(x)=exp(2pi i Tr(x/(delta f))) uses the inverse different correctly. In the Eisenstein coordinates x=a+b omega, f=c+d omega, its exponent is (-ad+bc)/Nf modulo1. This supplies the nondegenerate full-modulus pairing. A primitive multiplicative character is extended by zero on the full nonunit set, rather than on just some retained radical support.

I checked the Ramanujan expansion by inserting the ideal Mobius unit indicator. For a divisor b of f the additive sum over x divisible by b has size N(f/b) precisely when f/b divides the additive argument; this gives c_f(y)=sum_(d|(f,(y))) Nd mu(f/d). Changing x=ay in the Gauss square is valid because the original nonzero terms have both variables units, and produces rho(a)c_f(a-1), with the displayed conjugation convention.

For each proper ideal divisor d of f, U(f)->U(d) is surjective. This follows locally for prime powers and globally by CRT, including wild primes. A primitive rho cannot be trivial on this kernel: triviality would factor rho through the surjective quotient and lower its modulus. Therefore the kernel sum vanishes for every proper d; d=f contributes exactly Nf. There is no squarefree assumption hidden in this argument.

Unit z gives the Fourier identity by an invertible substitution. Additive Parseval over ALL Nf frequencies gives Nf phi(f), and the phi(f) unit frequencies already contribute phi(f)|tau|^2=Nf phi(f). Every other frequency has nonnegative squared modulus and must vanish individually. This is a complete proof of the asserted raw zero extension at nonunits for arbitrary conductor ideals, including prime powers. The stated modulus-one convention also works: the zero ring has its single residue/character/frequency and tau1=1.

The proposal's new full-modulus proof therefore closes a real potential gap left by testing only prime-field Gauss sums. My fresh focused diagnostic additionally checks actual Eisenstein ideals(2),(3),(6), with norms4,9,36. It includes ramified-prime-power and composite wild moduli, all primitive local character choices in the chosen explicit families and all nonunit-frequency zeros. Those finite checks supplement this universal proof; they do not establish it by sampling.

## 2. The ordinary all-character sieve has the claimed normalization

For a primitive rho, the expansion with tau_f(conjugate rho)^-1 is correct for every alpha. Squared absolute values remove the orientation-dependent Gauss phase, leaving the common factor1/Nf. The positive sum over primitive characters can then be enlarged to every character of U(f). Full finite-character orthogonality gives phi(f)/Nf times the reduced additive-frequency sum, which is at most that sum. There is no missing phi(f), Nf or coefficient-norm factor.

I challenged the spacing across unequal moduli and repeated associates. One generator is fixed for each ideal, so generator associates are not multiple modulus entries. For a unit numerator x mod f, the denominator ideal of x/f is intrinsically f. Equality modulo O therefore cannot identify two different reduced modulus/numerator entries. For distinct fractions, subtracting any k in O gives a nonzero Eisenstein numerator divided by fg. Its absolute value is at least1/|fg|>=1/Q. Multiplication by the fixed inverse different only changes the torus/lattice comparison constants. This handles prime powers and modulus1 as well as squarefree moduli.

The additive proof is sound in dimension two. The support box has T comparable to max(1,sqrt D). Its indicator is bounded above by e^(2pi) times the stated Gaussian. On expanding the dual quadratic form and using Gaussian Poisson, each matrix entry is a positive periodized Gaussian with prefactor O(T^2). Lifted separated frequencies obey a disk count O(1+(L/rho0)^2). Gaussian integration of this count gives an absolute row-sum bound O(T^2+rho0^-2), uniformly in the number of frequencies. Schur and finite-dimensional duality yield the displayed additive inequality. With rho0 comparable to1/Q it is exactly O(D+Q^2).

The passage to ideal coefficients is also valid. Class number one allows an injective choice of generator alpha_m with |alpha_m|^2=Nm. Unit-trivial finite residue characters give the trivial-infinity-type Hecke characters on these ideal columns. If the residue character descended to a smaller modulus, its unit-triviality would descend too and contradict primitive Hecke conductor minimality. Thus the needed Hecke family is a subset of the primitive residue characters already bounded. Squarefree ideals with nonsquarefree rational norm are permitted. Neither a false rational-norm restriction nor an arbitrary higher-order-family sieve enters.

## 3. Literal Kummer transfer and tuple multiplicity preserve the masks

For fixed r6 and fixed literal unit/S factor, c_m=b_m chi_m(u0)1_((m,r6)=1) is independent of all five variable factors, and its squared norm is no larger than the original coefficient norm. This keeps the zero mask of every sixth-power factor, including allowed overlaps with the first five factors.

For v=product_(j<=5) r_j^j, every outside-S valuation lies in{1,...,5}. The Kummer character is tamely ramified at every such prime, with nontrivial inertia order6/gcd(6,j); conductor exponent is1 there. BGL Lemma2.1 in the pinned source states precisely the radical-to-fixed-multiple conductor bound for its canonical primitive character. The accepted finite S/unit comparison converts this to the literal Kummer character without changing the outside-S support and with uniformly bounded fixed-S conductor. This is the necessary external arithmetic interface; the new ordinary sieve itself is derived in the proposal.

Consequently the primitive literal value equals chi_m(v) on all good columns: at a collision with q both are zero. This is exactly the place where a sixth-power radicand would make primitive replacement unsafe; that factor was removed and retained in c_m before this step. No row-dependent comparison phase is absorbed into a common coefficient sequence.

A fixed primitive character determines q through its outside-S conductor. Each prime of q has at most five choices of the exponent-bearing factor r_j. With generators and literal unit fixed, this gives at most5^omega(q) tuples. The elementary finite-small-prime argument bounds it by C_eta(Nq)^eta, with no claim of uniform injectivity. All actual dyadic conductors have norm <=C_S Q, and counting the arbitrary frozen r6 costs O(A6). Thus the block bound is A6(D+Q^2) times the original squared coefficient norm and an arbitrarily small power. The TeX correctly defines Lambda as an operator norm WITHOUT an additional coefficient factor; an extra factor seen in the informal handoff's display is not present in the reviewed TeX theorem.

## 4. Global interpolation, coefficients and principal rows

I verified both maximum-pivot branches symbolically. Writing C=sum j*x_j, r=sum x_j and m=max(x1,x2), C-2r+m is x3+2x4+3x5+4x6 when m=x1, and gains x2-x1 when m=x2. Hence R*S_A=R^2/M<=H. Also 2C+m-3r=(m-x1)+x2+3x3+5x4+7x5+9x6>=0, proving T_A<=(DH)^(2/3). The elementary R<=H and A6<=H^(1/6) comparisons are valid.

For nonnegative terms the displayed splitting of the minimum is valid. Since R*S_A<=H and A6>=1 in the normalized dyadic convention, R^2/A6<=H^2/S_A^2. Splitting S_A at(H^2/D)^(1/3) proves min(D*S_A,H^2/S_A^2)<=(DH)^(2/3). This gives H+D H^(1/6)+2(DH)^(2/3) as stated, up to fixed constants and arbitrarily small powers. Logarithmically many dyadic blocks are absorbed by smaller internal exponents. Summation over the S-supported literal factor converges at all three positive powers1,1/6,2/3, while literal unit multiplicity is at most six.

The required powered-BGL block estimate is the accepted wc:block. I also checked its pinned source interface: BGL Section3.2 treats the powers simultaneously, with the j=n/2 case handled by its quadratic input and the j!=n/2 recursion involving j*ell. Thus the needed powers1 and2 at n6 are supported; the present theorem does not create a new BGL-shaped mixed family.

The coefficient norm bound uses the actual3^omega(m) divisor bound and ordinary ideal counting. Taking a smaller divisor exponent gives the stated uniform D^eta bound on the squared normalized coefficients, independently of U. The fixed finite-order nu is unitary on the good columns. Complex W causes no change: the bound uses the modulus of the original coefficients and one common profile, without choosing a row-dependent weight.

For principal psi_u, nu has no outside-S inertia, so each outside-S valuation of u must be0mod6. This is a necessary condition sufficient for the upper count O(H^(1/6)); no converse is claimed. The exact wc:principal expression has |rho_T| bounded uniformly, |W_hat(1)|<=||W||_infty and the actual beta sum bounded by log^2(2U). Hence the principal energy is O(D H^(1/6)||W||_infty^2 log^4(2U)), which the new envelope absorbs using U^2<=D and smaller internal exponents. The elementary E=I-P norm inequality proves the reviewed residue-subtracted theorem. This assembly does not claim the stronger principal/signed assembly needed at target size.

## 5. Exponents, old face and the exact remaining scope

At H=D^(3/4), the three envelope exponents are3/4,9/8,7/6, so7/6 dominates. Its improvement over5/4 is1/12 and its gap above3/4 is5/12. On the old face with AB=H^(1/3) and A,B>=1, Q=A^2B=A H^(1/3)<=H^(2/3), so Q^2<=D when H=D^(3/4). With A6=1 the new raw block bound is D^(1+epsilon) across that entire face, including B<=A. This face conclusion is understood in the H=D^(3/4) regime introduced in the same paragraph, not for arbitrary independent H,D.

The two stated new upper-envelope witnesses are correct. At(5/12,1/6,0,0,0,0), capacity is3/4 and both D*S_A and Q^2 have exponent7/6; the BGL cross term has10/9. At the pure x1=3/4 point the BGL cross term retains7/6. These certify saturation of the available upper bounds, not a lower bound for the actual arithmetic energy or a failure of signed cancellation.

Finally I expanded the mixed reciprocity quotient directly. After the fixed original reciprocity phases it is theta_b(a')/theta_a(b'), as written. Its outside-S variation prevents the suggested radical relabelling from automatically satisfying GL Definition1(2). The ordinary all-character estimate avoids needing that extra family axiom. The TeX correctly avoids a claim that every possible alternative mixed-family theorem is impossible.

No correction to the mathematical statements is required. The conclusions are an improved unsigned full-mask envelope and its application to the residue-subtracted remainder. The target signed moment/type-II covariance, a positive arithmetic determinant comparison, zero location, actual analytic/category Lean and GRH remain open. No quantum-learning or finite-trained-data generalization is involved in this analytic argument.

## Fresh reviewer evidence and boundaries

`check_review_v1.py` writes `outputs/checks/2026-11-05-arithmetic-learning/review-mixed/acceptance-v1.json`, binding these exact TeX, dependency, review and checker bytes. It performs fresh actual wild/full-modulus finite Gauss tests and symbolic capacity/witness controls. The author's accepted19725-point grid and old991 joint-Gauss checks are not rerun. The infinite large-sieve and global theorem acceptance comes from the derivations audited above. No production source, browser, build, dependency, credential, environment, Lean or publication action was performed by this reviewer.
