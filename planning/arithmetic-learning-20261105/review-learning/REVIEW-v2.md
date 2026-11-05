# Independent arithmetic-learning code and mathematics review — accepted v2

**Verdict: PASS** for the exact finite supervised learner, its frozen v2 run, and the final shared paper bytes listed below. This is an independent audit of the learner, not a review of my own mixed-conductor argument. No correction to the frozen learner or artifact bytes is required. The optional request to justify the guaranteed nonprincipal subset is now implemented in the final details and has been reread and accepted.

## Mathematical and source audit

The objective is the full sum L=sum_i lambda_i |g_i−Gamma_i|^2 with lambda_i=1+|d_i^CC|^2+|d_i^CM|^2. It is a positive **spectral/Fourier-coordinate metric**, as explicitly stated in the final paper. Plain unweighted phase L2 Parseval would give sum|g_i−Gamma_i|^2; it would not by itself insert lambda. The final exposition makes the needed weighted norm explicit.

In zeta6 coordinates, |a+b zeta6|^2=a^2+ab+b^2 and M=[[1,1/2],[1/2,1]]. The ordinary real-coordinate gradient of L/2 is lambda_i M error_i. Preconditioning with the declared block metric lambda_i M makes the gradient equal to error_i, so the executed half step is exactly (g+Gamma)/2 and L_t=4^(−t)L_0. This is metric GD, not ordinary Euclidean-coordinate GD. The ordinary step eta=2/(3lambda_max) has nonnegative eigenfactors 1−lambda_i/lambda_max and 1−lambda_i/(3lambda_max); both are at most rho=1−lambda_min/(3lambda_max), proving the stated weighted-loss contraction. The ordinary trajectories are correctly untied and budget limited.

The raw target identity is exact: chi_m(u) conjugate(chi_n(u))=chi_r(u) conjugate(chi_t(u)) 1_((u,h)=1), with every q collision still zero. The sparse histograms use precisely these admissible literal rows. Distinct sign vectors differ by ±2 modulo6, so finite geometric summation proves orthogonality and exact coefficient readout for the restricted active orientation set. No full-cube kernel is substituted for a restricted set.

The common four-bump profile is genuinely smooth and supported inside (1,2). Its norm-coordinate bump radius is1/4, so every integer node except the four centers is exactly zero. Independent primary-generator enumeration and ideal division confirm that all15 active squarefree good ideal columns are included, with counts2,4,1,8 and actual r_U0,2,4,2. Norm-only ideal keys would collapse15 ideals to4 keys and are rejected by the independent support check.

All2262 literal rows, six units, S powers, and4530 raw column zeros are retained in the full case. The2148-row subset is correctly labelled guaranteed nonprincipal, not the entire nonprincipal family: outside S every prime norm is at least7, and7^4>625 forces each nonzero valuation into{1,2,3}; its nonzero class modulo6 gives nontrivial local Kummer inertia. No classification of the omitted114 outside-S-unit rows is asserted.

The CC/CM assembly keeps mu(q), actual r_U, W_m conjugate(W_n), and the exact diagonal. Weighted complex Cauchy–Schwarz yields the saved observable squared bounds; positivity of each summand yields the full-coordinate uniform bound L/lambda_min. All210 ordered coordinates are supervised, including zero-observable-weight coordinates. The same common exact Gamma labels drive training, so the finite learner claims no asymptotic advantage over exact label evaluation.

## Independent execution and negative controls

The accepted reviewer uses its own doubled Q(sqrt(−3)) arithmetic, lattice row/primary ideal enumeration, ideal division, modular finite-field exponentiation, Gram reconstruction, sparse histograms, signed readouts and eigencoordinate trajectory formulas. It does not import author arithmetic helpers. The sole author function invoked is verify_run, under an in-memory read patch for stale-byte refusal. No protected source or output bytes were altered.

Executed independently:

- Reconstructed31668 local symbols, all450 Gram entries and186552 sparse histogram cells.
- Replayed every saved state:216 metric updates and200 ordinary updates. Verified all exact losses, metric quarter contraction, ordinary eigencoordinate recurrence and contraction, signed predictions, actual errors, CC/CM certificate constants and values, coordinate bounds, first accepted iterate and selected finite feature predictions.
- Verified all four requested1e−12 runs;53/55/53/55 metric updates. Ordinary50-step runs remain explicitly uncertified for the requested tolerance.
- Verified64 nonzero negative-mu(q) C-C orientations per case; changing all signs to plus changes the readout. Omitting complex-profile conjugation also changes the actual readout.
- Checked scalar-only cancellation with a nonzero error vector, the wrong Euclidean(a,b) norm, norm-only keys, literal-unit removal and actual common-prime restoration. A concrete common-zero control is pair31,row(−9,−8): h=(1,9) deletes both raw column values while the q phases are units.
- In-memory tampering of learn.py, input.json and all_literal-complex.json is refused by the frozen hash verifier. A clean verification passes after each patch is removed. All source and artifact hashes match before and after the independent execution.

The reviewer receipt reports12868 grouped exact check units. This is a reproducible finite check, not a proof of an expanding-family analytic inequality. The first reviewer script has a preserved one-character syntax typo; independent_review_v2.py corrects only that reviewer typo and is the sole accepted executed reviewer. No author source was changed.

## Accepted exact targets and limits

The independent direct-amplitude reconstruction gives real-profile CC/CM targets2393/125,431/50 (full rows) and4293/250,771/100 (guaranteed subset), matching the paper. Complex-profile targets are also reproduced exactly in the receipt. Their aggregate CM happens to be real in these fixtures; complex intermediate targets and the conjugation control are still nontrivial.

The arbitrary positive rational request termination argument is correct for each fixed exact finite instance with unrestricted resources. The implementation's10000-update guard may refuse an extreme request without certifying it. No all-conductor/range/profile/runtime uniformity, unseen-data generalization, new analytic saving, positive covariance, PSD, determinant bridge, zero location, Lean result, quantum advantage or GRH conclusion is established.

verify_run checks hash binding against the manifest; it is not itself a mathematical replay or an authentication signature. This independent acceptance additionally pins the externally supplied immutable manifest digest. It does not claim protection against coordinated replacement of that trust anchor and all contents.

## Frozen bytes

Run manifest SHA256: 1eb22dfdadaf4a92e6b6231b7edd2fbfab0e68e0751237ce45e7a11bdb6dc3b4

Input SHA256: 61a43821bdba19b5ca353042e216b2107977e60211e959cd1d2e65cf1acb2ed6

Final paper bytes:

- papers/arithmetic-learning-core.tex: `1843bf4dc55f66d705336cf48a644133e3e272da2e5a054b5194953771974846` (3487 bytes).
- papers/arithmetic-learning-details.tex: `264954599ae10cbe4af708ba120453d82b5091dd91a6d0b20425eb4f568e5cd3` (6353 bytes).

Frozen source bytes:

- examples/arithmetic_learning/README.md: `f3cb62eab1c19d05f061af90f8289dc0f8ed3b8015d5e202243892f1293fd24f`.
- examples/arithmetic_learning/learn.py: `5c53724df205e017533c20229fe981ce70cde615eeefb7077e73be401dbbdd2e`.
- examples/arithmetic_learning/test_learning.py: `e8c777a86a840a3d223423d235fbbc4b2adb0d0918d9126ce8f785dcd1c95cdf`.
- scripts/check_finite_correlation.py: `5f8da7467f93071fc19b4a1a1e8c415a880a95305d847cce9a42c386d1f3d3e8`.
- scripts/check_mobius_split.py: `a3f1d3d89acafc187d6ca6851f370712b2544c92802b4d95dc5187e18a770638`.
- scripts/check_reciprocity_period.py: `34eef99b491f6b8d64b55b39c3a42400c6df3d0e1ddf5ba8494bc01f300e8925`.

Frozen artifacts:

- all_literal-complex.json: `cecf3f758ae65bc74ebc8c6be7680136f45b7edfc21b1e3d21b4f9ef414766fd`.
- all_literal-real.json: `fb51af890b64c0c09749fe6498d956d1c46a4811fa672ce4c45aa43686e26b95`.
- guaranteed_nonprincipal-complex.json: `5a9cafb8bacd908befbb1ecd52901622eff25cf457d786757286b23aa04c11a7`.
- guaranteed_nonprincipal-real.json: `dcd5a472d628322614a4e947fe9905e3f5211e5cb7a627ab00c6e1db3847fc96`.
- input.json: `61a43821bdba19b5ca353042e216b2107977e60211e959cd1d2e65cf1acb2ed6`.

Accepted reviewer SHA256: `9a8d2b6c861c6983ae56b24042ca5f3b4605b7fac3008758021cb96b347120e9`.

Evidence: outputs/checks/2026-11-05-arithmetic-learning/review-learning/independent-review-v1.json and acceptance-v2.json. No browser, production edit, protected-data mutation, dependency, GPU, authentication, Lean/compiler action or publication was performed by this reviewer.
