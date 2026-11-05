# High cutoff bilinear attempt handoff

5 November 2026. Remote-only; root owns queue and any integration.

The derivation is HIGH_WINDOW_BILINEAR_ATTEMPT.md. It proves the elementary
window \(2D/7\le U^2\le D\): every active long-long summand has complementary
ideal \(c=1\), so \(A_U(m)=\mu(m)(r_U(m)-1)\), with the full strict endpoints.
The ordered split count is even, hence every active coefficient has
\(|A_U(m)|\ge1\). An Eisenstein lattice/Möbius count proves the corresponding
positive coefficient-norm lower bound for fixed nonzero \(W\). This gives no
row-energy lower bound and no counterexample to the signed target.

The exact bilinear polynomial retains the original \(x_{ab}=x_ax_b\),
coprimality, zero masks, full hyperbola, fixed \(\nu/S\), common complex \(W\),
and primitive column orientation. On \(B_X\) alone \(P=0\); the original
principal residue elsewhere is retained.

A legitimate factorwise Cauchy plus power-one/two BGL application proves
\[
 Q_B(C_U,C_U)\ll (DX)^\epsilon\|W\|_\infty^2
 [\sqrt D X^2+DX+D^{5/6}X^{5/3}].
\]
At \(X\asymp D^{1/4}\) its exponents are \(1,5/4,5/4\).
The old recombined envelope has \(1/2,5/4,13/12\) and remains stronger.
No \(BT_\sigma\) saving follows. The exact unsupported step in the proposed
improvement is treating the two column factors on the same \(r,s\) as
independent BGL transforms. An explicit cyclic Fourier-array calculation
refutes that generic norm inference, without asserting an arithmetic
sextic counterexample.

Independent narrow sanity check by child bilinear_independent_check agreed
with the window, parity, coefficient density and factor-Cauchy derivation.
This is not a substitute for the root's independent review of the final bytes.

Focused command passed on Linux:
PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 planning/signed-bilinear-20261105/attempt/check_high_window_exact.py --output outputs/checks/2026-11-05-signed-bilinear/attempt/high-window-exact-v1.json

Exact deterministic evidence: 2,688 coefficient cases; 753 high-window
cases, including 291 with nonzero long complement; 148 equality-window
cases; seven strict-cutoff controls; one outside-window negative control;
157,464 raw multiplicativity cases with 139,968 zero-mask cases;
720 actual 72-row bilinear and complex-covariance identities;
three exact Fourier marginal counterexamples; 64 rational exponent checks.
Finite annular profiles test algebra, not a smooth-profile analytic theorem.
No seed, stochastic input, new dependency or analytic test claim.

Next mathematical input: prove a coupled fourth-moment/signed covariance
estimate for the actual Möbius and coprime hyperbolic factors. An upper
absolute covariance estimate has the wrong direction for \(BT_\sigma\).
The high window covers only comparable-to-\(\sqrt D\) cutoffs, so a proof
there would still need the other cutoffs and near-saturating row blocks.
No repetition of finished centering/sieve audits is proposed.

Only the exclusive planning/signed-bilinear-20261105/attempt and
outputs/checks/2026-11-05-signed-bilinear/attempt namespaces were written.
No queue, production, old-output, source, environment/cache, MCP/auth,
model/GPU, promotion or publication action. BT_sigma, full signed energy,
arithmetic positive determinant and GRH remain open.
