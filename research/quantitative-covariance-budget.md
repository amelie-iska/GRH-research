# A lower covariance budget and the remaining coupled moment

5 November2026. On the actual raw-character Gram G of a literal row block,
with 0<=G<=Lambda_B I and C_U=mu*r_U, define
M_j=sum_m r_U(m)^j |W(Nm/D)|². Exact positive-contraction algebra proves

    Re Q_B(C_U,mu) >= -Lambda_B/(2D)*(sqrt(M0*M2)-M1).

This is sharp for general positive contractions with the fixed coefficient
vectors; arithmetic attainment is not claimed. It allows the accepted
negative-covariance example. It does not impose automatic positivity.

In the high-cutoff window2D/7<=U²<=D, actual balanced ideal factorizations
satisfy sum r_U<<D and sum r_U²<<Dlog(2D), uniformly in U. Counting two
factorizations ab=cd uses a=gh,c=gk,b=k*l,d=h*l and the INDIVIDUAL bounds
Ng,Nl<<sqrt(D)/max(Nh,Nk). Counting only their product would lose another
logarithm. For common possibly complex W this gives a lower budget of
order -||W||inf² Lambda_B sqrt(log(2D)).

The exact double commutator deletes equal-r levels. Complete six-unit row
blocks also delete Gram entries whose column norms differ mod36. These
are real restrictions with every raw zero and fixed column phase retained,
but the inherited sieve still costs DX on the surviving classes. There is
no new power saving: at H=D^(3/4), the relative D^(1/2) loss remains.

The full near-saturation face is A1=A2,A1*A3=H^(1/3),A4=A5=A6=1;
A3=1 is only an endpoint. Both neighboring wedges and the A3 direction
must be retained in any proposed gain. A small negative commutator budget
alone would also leave the within-level energies sum(k-1)²q_kk.

Shared proofs: papers/covariance-budget-{core,details}.tex.
Full attempt: planning/covariance-budget-20261105/attempt/QUANTITATIVE_COVARIANCE_BUDGET.md.
Independent review/checks: planning/covariance-budget-20261105/review/ and
outputs/checks/2026-11-05-covariance-budget/review/.
Finite exact reconstructions check the formulas and masks, not an
asymptotic saving. No new Lean theorem or GRH conclusion is claimed.

Next: estimate unequal-product character quadruples and their mixed Mobius
term BEFORE absolute Cauchy, retaining the union mask (including common
primes) and every near-saturating row block. The elementary multiplicative-
energy coefficient diagonal now has an explicit bound; the oscillatory
coupled row moment remains open. Short/principal assembly and an
independent positive determinant/zero-location bridge remain separate.
