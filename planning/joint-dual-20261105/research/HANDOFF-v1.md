# Joint Gauss research handoff — 5 November 2026

Selected artifacts: `JOINT_GAUSS_ORIENTATION_IDENTITY-v2.md` and `joint-gauss-{core,details}-proposal-v2.tex`. Version 1 notes/proposals are preserved development evidence; their h=1 specialization omitted the necessary alpha=1 convention. Governing v2 explicitly fixes the unit-ideal generator to 1. Do not integrate the long v1 drafts.

The surviving result is an exact joint full-mask phase identity, not a new analytic exponent. For m=hr,n=ht with q=rt, L=hq, Q=Nq, theta=x_r conjugate(x_t), xi=x_q^3, the simultaneous five-power Gauss product is orientation-independent. With generators alpha for h and beta for q and the inverse-different additive pairing, the full six-factor transform is

    product G_j(k_j) = Q^2 xi(-alpha) tau_beta(xi)
                      conjugate(theta(product_(j<=5) k_j^j))
                      product_(j<=5) c_h(k_j) c_L(k6),

with zero whenever any first-five frequency is a q-nonunit. All common-prime deletions remain. The exact joint conductor/frequency formula retains the outer mu(q) sign, actual r_U factors, fixed nu, common complex W and exact original row Fourier weight F. Orientations diagonalize over uniform unit K because their quotients are nontrivial cubic characters. This yields an exact finite Parseval norm budget and a computable truncated-frequency remainder; it does not bound the true nonuniform dual weight or give a power saving.

The entire A3 face/neighborhood is present in F. At the pure A3 endpoint the actual row character is quadratic and orientation-independent; fixed length-one variables can undo complete phase balance under inverse summation. The remaining task is a signed estimate for the actual h,q,K sum, particularly h=1. The old small-conductor/high-gcd sector is unchanged. There is no new BT_sigma, arithmetic energy lower bound, global exponent gain, Lean declaration, zero-location theorem, positive determinant bridge or GRH result.

Focused checks: `check_joint_gauss-v1.py` passes 991 exact stdlib assertions. They cover split fields F7/F13/F19 and inert F25; all 546 full-period transforms for actual Eisenstein q=(3+omega), h=(4+omega), L=(11+6omega); twelve mixed six-frequency products; all four orientation Gauss balances at conductor norm91; sixteen orientation orthogonality entries; exact nonconstant-complex-vector Parseval; the eight coherent cubic-diagonal residues; and all 7776 local five-frequency products. Receipt: `outputs/checks/2026-11-05-joint-dual/research/joint-gauss-check-v1.json`. The selected TeX proposals have balanced unescaped braces. Root owns final article/book TeX builds; this subtask did not run them.

Run:

    python3 planning/joint-dual-20261105/research/check_joint_gauss-v1.py \
      --output outputs/checks/2026-11-05-joint-dual/research/NEW-UNUSED-NAME.json

The checker refuses to overwrite outputs. Existing checker stdout/receipt is sufficient; no rerun is required without a changed formula or new concern.

Independent reviewer `/root/lean_frontier_feasibility` reported the full algebraic audit correct after the unit-generator correction: inverse-different pairing, CRT, zero frequencies, ell^-6 inversion, mu/nu cancellation, orientation orthogonality, fibers, coherent diagonal, finite height and tail Cauchy. Root retains final-byte acceptance separately.

All subtask writes are new files inside `planning/joint-dual-20261105/research/` and `outputs/checks/2026-11-05-joint-dual/research/`. No production/source-pin/history/dependency/environment/model/GPU/credential/authentication/MCP/publication action was performed. Root owns queue claims and integration.
