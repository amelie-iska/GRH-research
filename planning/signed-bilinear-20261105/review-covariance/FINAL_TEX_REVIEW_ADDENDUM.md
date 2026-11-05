# Final TeX review addendum

5 November 2026. I reviewed the final mathematical text in papers/signed-bilinear-core.tex and papers/signed-bilinear-details.tex, with the exact SHA256 values recorded in the adjacent final-tex-acceptance-v1.json receipt. This addendum extends, rather than rewrites, the earlier independent review.

The review covers the high-cutoff proposition, the squarefree coefficient count and its limitation, the legal factor-Cauchy estimate and exponents, and the complete finite covariance test. The double-Perron material is explicitly left to the separately assigned Perron reviewer.

**Accepted; no correction requested.** The TeX preserves the strict factor cutoffs, the fixed-profile nature of the coefficient lower bound, and the absence of a row-energy consequence. The derivation of the factor estimate and exponents agrees with the reviewed attempt. It claims only that the displayed estimates give no saving, without promoting that fact to a general impossibility theorem.

The smooth profile includes all four squarefree ideals at the selected norms. The complete 72-row B7 block has maximum norm 2197, and is distinguished from the 246 guaranteed nonprincipal rows below H=89. The latter is correctly described as a subset, with raw zeros retained. The real Gram eigenvalues 54 and 90 are correctly distinguished from eigenvalues of the full complex Gram matrix. Every normalization in the quoted covariance/energy equations agrees with the independent exact data.

Although the frozen author report labels its cross term as real covariance, an additional direct check of the complete complex cross term gives the unnormalized Eisenstein pair (-432,0) on B7 and (-552,0) on the H89 subset. Thus the full covariances really are the real numbers -27/25 and -69/50, and the TeX equalities for Q itself are valid in these examples. The cancellation of imaginary parts is consistent with the paired conjugate columns and conjugation-stable literal row sets.

The automatic-positive-covariance claim is refuted by a fixed finite example. The text correctly makes no BT_sigma refutation, asymptotic arithmetic energy lower bound, Lean or GRH claim. This review does not claim a TeX compilation or rendered-layout check; the parent owns integration/build verification.
