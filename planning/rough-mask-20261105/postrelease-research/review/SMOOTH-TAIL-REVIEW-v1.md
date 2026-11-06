# Independent review of the smooth-divisor tail localization

Verdict: accepted as a derived positive-norm tail corollary. This review does not prove a new sieve, signed cancellation estimate, global exponent improvement, determinant bridge, or GRH statement.

The governing note is SMOOTH_TAIL_LOCALIZATION-v1.md, SHA92b5fbacf0fb9a066037da159875de5980ffcc9ab9545e83b3ce470b55e79c9e. The inherited input is the actual-coefficient positive norm in papers/signed-weights-details.tex, sw:divisor-budget, lines13–36; the definitions of T_f, K0 and KS are rma:T/rma:Kzero/rma:KS. No accepted experiment or checker was rerun.

## Exact identification and inherited hypotheses

For d=f, the inner AA norm in sw:mobius is precisely G_f: A_U(fa), coprimality(a,fS), nu(a), the raw symbol chi_a(u), the common profile W(FNa/D), the original literal two-pivot rows, and the raw(f,u) restriction all agree. Factors nu(f) and chi_f(u) disappear only through absolute square, leaving the latter mask. Nothing requires A_U(fa) to factor. The powered block sieve is invoked only for the original unweighted natural row multiplicity, or the already allowed fixed bounded multiplicities, after enlarging a subfamily inside a positive norm. This does not extend the classical operator input to arbitrary row weights. The fixed nu/S/literal conductor/ray conventions and capacity/internal masks remain those of the accepted input; intended nonprincipal rows retain the conductor-nu-supported-in-S qualification.

At L=D/F>=1, that input bounds G_f by (HD)^eta B^2(LR+L^2R/M+L^(5/3)R/M^(1/3)). Its coefficient square norm follows from the uniform divisor-assignment estimate on N(fa)<=2D and O(L) ideal counting, with sufficiently small internal exponents. For1/2<L<1 only a=1 can occur, giving O(RD^eta B^2), which the same expression absorbs since L>1/2. At L=1/2 the unit residual evaluates W(2)=0; below it no residual survives. Thus F>=2D contributes zero. Unit residuals are retained, and no subunit-length sieve is assumed. The degenerate B=0/empty-family cases satisfy the weak bounds directly.

## Independent tail derivation

Take the absolute triangle only in f after the positive norm estimate. Dropping squarefree, U-smooth and good-ideal restrictions increases these nonnegative upper sums. Ideal counting A_K(x)=O_K(x), by dyadic partial summation, gives sum_(Y<F<2D)1/F=O(log(2D)), sum_(F>Y)1/F^2=O(1/Y), and sum_(F>Y)1/F^(5/3)=O(Y^(-2/3)) for Y>=1. After division by D the three terms are Rlog(2D), DR/(MY), D^(2/3)R/(M^(1/3)Y^(2/3)). Absorb only logarithms and the original assignment/sieve subpowers into the requested epsilon. This proves(1) without any cancellation of mu(f).

For every actual or auxiliary KS term, the profile argument is F P Na/D, with P>U and Na>=1. If F>Y>=2D/U this exceeds2, so every term is exactly zero, independently of raw row/residual zeros. This proof does not declare fpa squarefree in auxiliary collision states. It proves(2) on the full accepted KS definition.

If R=O(H), the first term is target size. Solving DR/(MY)<=H yields Y>=DR/(MH). Solving the third inequality yields Y>=D R^(3/2)/(M^(1/2)H^(3/2)). Adding Y>=max(1,2D/U) proves the sufficient cutoff(3), including the vacuous Y>=2D case. The unit-semiprime correction is not lost: its smooth factor is f=1, while the reviewed tail is F>Y>=1. This is a split of the clean K0-KS expression, not a removal of C2 from the complete identity.

## Exponents and surviving obstruction

Independent Fraction arithmetic gives mixed r=7/12,m=5/12,y=13/24 and normalized tail exponents(7/12,5/8,3/4), and pure r=m=3/4,y=5/8 with(3/4,3/8,3/4). The rough support exponent is1/2, strictly below both chosen y. Fixed constants in U~sqrt(D) and feasible dyadic capacity windows are retained; the power notation is not an assertion that an entire dyadic box with lower endpoint exactly H fits a hard capacity H. The general cutoff is sufficient, not necessary or sharp. A fresh361-point rational feasible-triangle check verifies only this algebra and is not evidence for any energy estimate.

The f=1 powered bounds remain(7/12,7/6,10/9) and(3/4,1,7/6); comparison with the accepted ordinary branch still gives exponent7/6 at both displayed neighborhoods. These are inherited upper-bound exponents, not actual-energy lower bounds. The small-f coherent sum still retains all actual coefficients, prime supports, mu(f), row masks and one common W. No signed main estimate or missing5/12 saving follows.

## Local duplication/scope check

The recorded sw:divisor-budget already contains the needed positive bound; this note merely retains its divisor cutoff. Focused searches of existing papers/research/planning found no prior explicit13/24 smooth-f localization. The older research/short-row-high-gcd.md already records a5/8 cutoff for the original pair-gcd sector with a fixed smooth radial row profile. The intermediate smooth incidence divisor f is not the original column-pair gcd h, and the present literal two-pivot row family is not silently replaced by that radial family. The repeated5/8 endpoint does not establish a new high-gcd theorem or external priority claim. No old high-gcd or finite-data audit was replayed.

All review code and evidence are newly created postrelease files. No frozen153 release input,47 READY product/source guard, book/PDF, README, masterplan, queue, or protected HEAD/index was edited.
