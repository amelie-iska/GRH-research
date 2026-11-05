# h=1 quadratic/Jacobi route: accepted exact result and open signed bound

The governing proof is TWO_PIVOT_APPLICATION-v3.md (SHA256 f1113869c23041e1f12b3d7869559e670234cec9a4b5188c33e0f030f7ff30d4). Independent review-phase/acceptance-v1.json is PASS (fe16ad0779ac43afe96158c8ff5e459b56ccd810ad9cb29fed48ac091c9d3f3a), with642 fresh exact Jacobi/CRT controls and58 fresh ray-extension controls. No old991/period/profile/learning tables were rerun.

The old inverse-different phase law is REUSED: tau_beta(x_q^3)=sqrt(Q)Gamma(beta), Gamma=[1+i^-b+i^a+i^(b-a)]/2. The central character is quadratic. For squarefree composite q the equality with a quadratic root sum needs the full product of local root counts and CRT annihilation, not the false composite identity1+xi_q. In the old FULLsix h1 formula the scalar is mu(q)Q^-7/2 xi_q(-1)Gamma(beta); fixed beta mod4 makes its Gaussian phase constant but leaves the actual signed weight.

The new application is the actual TWO-pivot completion, fixing the other factors and retaining all masks/capacity/rays/common fixed W. If j(p)=J_p(chi6,chi6^2), then(j(p))=p by the literal positive-character polynomial reduction. Moreover -j(p) is the unique generator congruent1 modulo f=(2delta), Nf=12. This constructs the fixed Hecke character Psi directly, with finite part alpha/u_f(alpha), principal value alpha on alpha=1modf, and exact conductor f by unit obstructions. It requires no assumed CM theorem. On squarefree columns mu(s)j(s)=Psi(s); never extend this Mobius identity to arbitrary ideals.

Thus the exact h1 slice is

    D^-1 sum_q Gamma(beta_q)/Q sum_(rt=q)
      b(r)conjugate(b(t))theta_(r,t)(Z) T_(q,F)(theta_(r,t)),
    b(s)=[Psi(s)/sqrt(Ns)]r_U(s)nu(s)W(Ns/D).

There is NO extra xi_q(-1) in this TWO-pivot scalar. C--mu replaces the second r_U by1; high-window A--A uses r_U-1 on both sides, under the existing window hypotheses. The fixed literal factors remain in theta(Z), including sixth-power raw collision zeros; arbitrary v6 is retained. The conductor12 is a COLUMN coefficient twist: the pair character still has growing conductor q, and original row conductors/principal residue subtraction are unchanged.

Surviving estimate: for fixed q, counting norms give sqrt(phi(q))/(DQ) times the orientation coefficient energy square root times||B2_q||_2. Absorbing the normalized Psi phase is diagonal unitary conjugation and cannot improve arbitrary-coefficient operator norms. At a literal length-one second pivot, its Fourier factor cancels the extra Jacobi/quadratic completion and returns the original one-pivot expression. No signed coupled inequality, exponent improvement, fixed-W counterexample, new Lean result or GRH conclusion follows. The original fixed-profile h,q,K estimate remains open; the mixed and pure A6=1 sectors are not settled.

Only the new owned planning/output directories were written. Source HEADdba37ff/index0ef1af and all12 pinned source files remain unchanged. No production/queue/compiler/dependency/authentication/publication action occurred. Governing author receipt is outputs/checks/2026-11-05-signed-weights/quadratic-phase/author-result-v2.json; independent acceptance and exact controls above supply the review evidence.
