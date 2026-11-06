# The actual finite root-moment Schur map and its norm limitation

Research-only lane C, v1, 6 November 2026. This exposes the exact leading finite-w operator on the original signed coprime slice. Its bounded Schur norm recovers an inherited majorant and provides NO new signed power saving. The full coefficient/root vector is never replaced by an arbitrary phase-free vector. No projection-rank argument or actual-energy lower bound is made.

## 1. Scope and the leading moment

Use principal-mean HANDOFF2b923adf..., aggregatebbe4a216..., exact finite top mean in A5624e5bb..., mean4315f8d2..., sharpen972192ef..., and the current cbk primitive kernel/two-gauge normalization. Original columns are the COMPLETE good squarefree ideal annulus D<=Nm<=2D,D>1, with
c_m=A_U(m)nu(m)R_m(u0)W(Nm/D).
Keep original U, fixed nu/S/ray/source data, ONE common possibly complex W and every actual coefficient. Rows are ONLY the original unweighted two-pivot family, fixed literal unit/S-supported u0 without good support, with all original SF/coprime/literal/ray/capacity restrictions. R=A1A2. The original unequal-norm mask, if requested, is imposed before the representation.

At V=X^(1/6)/2, X>=64, the accepted unit plateau gives
M_top=sum_(outer,rho^6=1) kappa_S g(m)g(n) C_outer
 integral_V^(2V) sum_(Nw<=X/u^6)
                bar(eta(w))dotG(L_e Nw u^6/F)du.
All integral ideals w occur, including S-supported and prime-power ideals; different ideal orientations remain distinct. F=F_S NmNn is the ORIGINAL primitive conductor on coprime m,n. All finite k/ell/e masks and primitive S zeros remain. This is the retained mean, not the full original P_top.

Define J0 by replacing only dotG with
g0(v2)=dotG_v2(0)=C0^(-1/2) integral G_v2(t)dt.
No claim that this replacement is free is made. Its leading w weights are EXACT:
a_w=V^(-1) length{u in(V,2V]:Nw*u^6<=X}
    =(2(Nw)^(-1/6)-1)_+.
They vanish at Nw=64, are nonnegative and satisfy a_O=1. Thus J0 still includes every w of norm<=64 with its actual primitive value. No second unit averaging is applied.

## 2. Rectangular all-component formula

Fix one actual v2, class pair A,B, selected rho, ell|v2 with Nell<=b, and e|P_S. Keep
K_ell=sqrt(b/Nell), L_e=A1/[(Nk)^2 Nell Ne],
sigma=prim(rho psi_A bar(psi_B)), f_S=cond(sigma).
The proved root factors are TWO different column gauges:
u_m=beta_m xi_m(f_S)rho(m),
v_n=beta_n xi_n(f_S)bar(rho(n)),
epsilon(eta)=kappa_ABrho u_m bar(v_n).
Individual xi are unitary Hecke characters and may have fixed nonzero infinite type. Their legitimate primitive values at S are not raw forbidden symbols. Primitive sigma(e),sigma(w), including0, stay separately.

Let C_AB be the actual rectangular zero-pattern matrix
(C_AB)_(m,n)=1_((m,n)=1) 1_(Nm!=Nn)
for m in class A,n in class B; omit the last indicator only for the full mean. This coprime mask is applied FIRST. Off that support, formulas below are merely the accepted individual-column auxiliary extension, not primitive overlapping-conductor characters.

For any integral z put D_z^A=diag(xi_m(z):m in A), and similarly B. Entries are0 at primitive good collisions and otherwise have modulus1. Define
W_ABrho(T)=sum_(Nw<=64) a_w bar(sigma(w))
                               bar(D_w^A) T D_w^B,       (1)
Q_K,ABrho(T)=sum_(k original,Nk<=K)
        mu(k)sigma(k^2)/(Nk)^2 D_(k^2)^A T(D_(k^2)^B)*.   (2)
Original k is good SF and coprime to v2. The maps commute as Schur maps, but their separate raw-zero factors must NOT be simplified to a quotient k^2/w which might restore a collision.

Set
x_m=c_m g(m)u_m R_m(v2^2)xi_m(ell e)/sqrt(Nm),
y_n=c_n g(n)v_n R_n(v2^2)xi_n(ell e)/sqrt(Nn).
The convention is LINEAR FIRST:
Q_T(x,y)=sum_mn x_m bar(y_n)T_mn=x^T T bar(y).
The corresponding J0 component is exactly
kappa_S kappa_ABrho h_ABrho(v2)
 A1 V g0(v2)/sqrt(F_S)
 *mu(ell)mu(e)/(Nell Ne)*sigma(ell e)
 *Q_(Q_K,ABrho W_ABrho(C_AB))(x,y).                       (3)

This follows by multiplying the factors, not by a new root identity:
eta(k^2 ell e)=sigma(k^2)sigma(ell e)
 xi_m(k^2)xi_m(ell e)bar(xi_n(k^2)xi_n(ell e));
bar(eta(w))=bar(sigma(w))bar(xi_m(w))xi_n(w).
Every original sign, exact finite cutoff and S zero is present. If sigma(ell e)=0 the entire term is0; no division by it occurs. Empty capacity fibres/ell ranges have no attached leading term.

Equation(3) holds for arbitrary source pairs, not just a common-class shortcut. The finite sum over all actually selected rho^6=1 and source pairs reconstructs J0; other original rho branches belong to the quantified P-M error, not to a secretly discarded piece of the original kernel.

## 3. What a bounded Schur norm actually proves

For counting operator norms on each rectangular block,
||W_ABrho(T)|| <=A64 ||T||,
A64=sum_(Nw<=64) a_w,
because each diagonal is a contraction and |sigma(w)|<=1.
Likewise
||Q_K,ABrho(T)||<=zeta_K^S(2)||T||.
The latter is an inherited finite-k absolute majorant, not an Euler completion or new cancellation theorem. All fixed entrywise zero patterns commute with these maps; in particular they preserve the original coprime and unequal-norm restrictions.

The complete annulus has O(D) columns, so ||C_AB||=O(D). The actual vectors in(3) satisfy
||x||_2,||y||_2 << B D^epsilon,
using only |A_U|<=3^omega<<D^epsilon, their original phases,0<g<=1 and Nm>=D. After the original once-only normalization byD, finite class/rho/S sums, original ell divisor loss and unweighted v2 count, this yields
|J0|/D <<_(fixeddata,epsilon)
                    B^2(DXA2)^epsilon R V.              (4)
This is an ACTUAL leading-moment upper bound, but it has the same top-sector size as the inherited fixed-s comparison at X/V^6=64. At pure A1=R=H=D^(3/4),A2=1,X=D^(3/8), it is13/16, not target3/4.

For the full finite top mean, the previously accepted finite-mode Bessel--Euler hierarchy applies to arbitrary matrices with all roots and zero patterns retained. In the low-argument range T0=A1X/D^2<=1, its dimension-free Schur error from j0 is O(T0) times the same bounded-map majorant. Therefore the INHERITED consequence is
|M_top-J0|/D << B^2(DXA2)^epsilon R V (A1X/D^2),           (5)
and |M_top|/D has the same RV bound in that range.
At the declared pure top scale the right side of(5) has exponent-1/16. This is a useful quantitative orientation, but it is an old finite-hierarchy corollary, not new research output. B/root are independently retaining the exact matched endpoints; no endpoint completion is used here.

The separate lattice approximation P_top-M_top still has reviewed pure error37/48>3/4. Even a future target-size J0 estimate alone would not finish the whole signed assembly or automatically solve every original sector.

## 4. Positivity is confined to a different object

On a SAME-source-class, rho=1 component only, sigma=1 and A=B. The W map alone is
W(T)=sum_w a_w (D_w)* T D_w,
a completely positive map on COMPLETE matrices: if T>=0, each summand is positive. This statement concerns W only.

It says neither that Q_K is positive (its mu(k) coefficients are signed), nor that the ell/e sum is positive, nor that a general complex-sigma rectangular block is positive. Primitive S zeros in other branches do not change this distinction.

More basically, the original coprime unequal matrix C has diagonal0 for D>1. W(C) is Hermitian in this special component and still has diagonal0. If it is nonzero, it must be indefinite, since a nonzero Hermitian matrix of trace0 has eigenvalues of both signs. No assertion that it is nonzero in every actual branch is needed or proved. This is not a positive energy/Gram lower bound for J0.

The two different gauges u,v cannot be flattened across source pairs/rho. A fixed unitary/contractive change in a kernel is not a new estimate for the actual A_U vector. The actual roots remain in x,y in(3), not discarded from the physical problem.

## 5. The precise failed shortcut and remaining arithmetic

The finite number of w channels and the convergent finite-k absolute norm do NOT supply a factor D^(-delta). They supply the constant A64*zeta_K^S(2) in(4). Nor does unweighted finite-ray orthogonality remove kappa_ABrho, different f_S, primitive sigma(e/w), or the root gauges. All of those remain inside their actual weighted finite sum.

Existing bounded-inverse facts for a completed pure Euler multiplier are not invoked as an equivalence of actual fixed coefficient problems: an inverse acts on a kernel or on new diagonally modulated coefficient vectors, and need not preserve original A_U/W/capacity data. No lower bound, necessary scalar hypothesis, norm barrier or impossibility statement for the actual vector follows here.

The exact open requirement is a signed estimate for the fixed-vector expressions in(3), coherently over their actual k/w/class/rho/ell/e/v2 data, BEFORE replacing them by ||C|| and separate vector norms. Formula(3) isolates that requirement while preserving the full original coprime and unequal slice. Its source coefficient vector has not become arbitrary or generic-conductor data.

Comparison with the inherited baseline is mandatory: UB01Eq12 already bounds each fixed total sixth part, so summing the requested good-s band and finite-S logarithm gives (R/D)V F6(X/V^6,D). The top case of that bound is RV. Re-deriving(4)--(5) cannot be called a new actual-band gain or the next successful arithmetic step.

The surviving result of this lane is the explicit finite root-moment operator(1)--(3), its exact raw-zero/linearity/positivity scope, and the failed automatic-Schur-gain diagnosis. No new whole signed13/12/global9/8, positive determinant/zero-location, Lean or GRH claim is made.
