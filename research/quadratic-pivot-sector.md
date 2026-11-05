# The cube-factor sector and a joint dual-frequency identity

5 November 2026. This refines a sector of the original arithmetic bound. It supplies neither a new large sieve nor the missing signed estimate or GRH.

[Interactive full-face inspector](https://amelie-iska.github.io/GRH-research/quadratic-pivot.html) · [book proof](https://amelie-iska.github.io/GRH-research/book/main.html#qp:core) · [joint completion](https://amelie-iska.github.io/GRH-research/book/main.html#jdq:core).

For the original outside-S ideal row r1 r2² r3³ r4⁴ r5⁵ r6⁶, only r1,…,r5 are pairwise-coprime squarefree. The arbitrary r6 may overlap them. Put R=product Aj, M=max(A1,A2), with Aj<=Nrj<2Aj and product Aj^j<=H. The columns are squarefree ideals of the Eisenstein field with D<=Nm<=2D, not necessarily of squarefree rational norm. Keep all literal units, fixed S factors, fixed finite-order nu, common possibly complex W, exact capacity and raw collision zeros.

Freeze all factors except r3. Exact numerator multiplicativity gives chi_m(u)=chi_m(F) chi_m(r3)^3; the frozen multiplier has modulus at most one. In particular chi_m(r6^6) is the indicator (m,r6)=1, never an unconditional one. The existing finite S-unit/ray comparison makes the remaining cube kernel a finite union of quadratic Hecke-family kernels with row-independent column coefficients. [Goldmakher–Louvel, arXiv:1112.1642v2, Corollary1.2](https://arxiv.org/pdf/1112.1642v2) therefore gives

    Lambda_A <= C_(nu,S,epsilon) (HD)^epsilon [R + D R/A3].

The PDF is pinned at SHA256 5cc5f03388d3996b4333f07be51f989f60779fe172f8bd24c7aa6ddad64dd304. This is an application of its classical sixth-family cube estimate. The full finite-partition, coefficient independence and conductor proof is in the shared quadratic-pivot sources; all external analytic dependencies are explicit. Normalization remains in the actual column l2 norm, and no arbitrary factor-count norm is replaced by one.

Combining with the existing powered-BGL bound gives R plus the minimum of [D R/M + D^(2/3) R/M^(1/3)] and D R/A3, up to the same declared type of constants/small losses. On the complete previous face A1=A2=A, A3=B, AB=H^(1/3), A4=A5=A6=1, put H=D^(3/4), A=D^a, B=D^(1/4-a). The refined leading exponent is min(5/4,1+2a), for the entire interval 0<=a<=1/4. It improves when a<1/8, while a>=1/8 still costs 5/4. Even the improved endpoint costs D, above the target D^(3/4). A power improvement requires B/A to grow by a power, not merely a constant separation. The inspector's numerical monomial sums omit the unknown analytic constants and epsilon factors; they are not measured Gram eigenvalues.

There is also an exact neighborhood refinement: if the middle monomial D R/max(M,A3) is at least D H^(1/3) D^(-eta), the previous full capacity/imbalance/high-power slack is at most 3 eta logD and A3<=M D^eta. These are necessary conditions for upper-bound monomials, not arithmetic energy lower bounds. They leave a smaller but nonempty hard near-face sector.

For the joint completion, write m=hr,n=ht with pairwise-coprime squarefree h,r,t and q=rt!=1, L=hq. Original internal masks give only local exponents0,+1,-1; generic four-column fourth moments are different. The primitive orientation theta=x_r conjugate(x_t) has theta³=xi_q independent of the orientation. With the explicitly specified inverse-different additive pairing and generators alpha of h, beta of q (alpha=1 for h=1), the full six-factor transform has the exact product

    product G_j(k_j) = (Nq)^2 xi_q(-alpha) tau_beta(xi_q)
                      conjugate(theta(product_{j=1}^5 k_j^j))
                      product_{j=1}^5 c_h(k_j) c_L(k6).

All canceled common primes remain in the Ramanujan factors; r6 retains the full raw deletion. The original mu(m)mu(n)=mu(q) stays as a signed conductor weight. Distinct orientations give an exact cubic-character Parseval diagonal, but their actual Fourier weight is not uniform. The coherent set has size phi(q)/3^omega(q), and at the pure r3 endpoint the actual row character is orientation-independent. Thus joint Gauss balance does not supply incomplete cancellation. The explicit finite-height/tail budget still requires a bound for its actual joint h,q,K weight.

Independent mathematical reviews are in planning/joint-dual-20261105/review-quadratic/. Exact cyclotomic split/inert/CRT/orientation checks pass991 assertions; the six-factor capacity/face checker passes3167 assertions over996 feasible states and1001 full-face positions. The inspector has1037 independent numeric cases and desktop/mobile/night/keyboard checks. Finite checks support the stated algebra/bookkeeping; they do not reprove GL or establish the missing analytic saving.

Reproduction uses existing stdlib/toolchains; all runs and outputs stay on Linux:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 planning/joint-dual-20261105/check_quadratic_envelopes.py --output outputs/checks/NEW-quadratic-envelopes
python3 planning/joint-dual-20261105/research/check_joint_gauss-v1.py --help
```

The original low-gcd/common-divisor1 joint signed estimate on the remaining face, short/principal assembly, independent positive determinant/zero-location bridge and actual analytic/category Lean remain open. A separate request to add the pinned Linux4.24 compiler is pending; the stored Mac binary is incompatible and no replacement toolchain has been installed. Earlier accepted readout certificates, datasets, active models, source clones, environments and release histories remain protected.
