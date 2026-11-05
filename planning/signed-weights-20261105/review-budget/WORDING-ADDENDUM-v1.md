# Bounded current-byte and Perron wording addendum

PASS for ACTUAL_SIGNED_BUDGET-v3.md, SHA874d921be634a847f690dfbcae5f67728b6e0e63c749c868d76be3cf647d8199. I inspected the complete v2-to-v3 diff. The existing v2 proof of(6)--(9), including the L<1 endpoint, is unchanged and remains accepted. No52 diagnostics,700 phase checks or author fixture was rerun.

The centered definitions now explicitly require n_q>0 and omit empty orientation sets. This correctly avoids division by zero without changing any contributed term.

The Euler/Perron statement now uses successive positive-line Perron LIMITS with halfinteger cutoff, and explicitly denies finite-height exactness or any proved truncation/tail estimate. This correction is required: my original review checked the Euler algebra/normal domain and read inversion as limiting recovery, but should have qualified the earlier finite-height wording expressly. The new wording supplies that qualification; no finite-height theorem is accepted. Initial absolute-convergence lines and fixed noninteger cutoff justify successive limiting inversion, with constants allowed to depend on the fixed cutoff. No critical-strip or uniform-tail bound follows.

The appended variance arithmetic follows directly from the already frozen Gamma=(-4-2omega,-2+2omega) and a=(-1,-1): meanGamma=-3, centered values(-1,-2),(1,2), each Eisenstein norm3, squared-norm sum6 and average3. The uncentered pairing is6, squared modulus36, exceeding the proposed variance-only product2*6=12. The amplitude ratio is sqrt3. This is a nonzero-variance counterexample to dropping the mean; it is not mislabeled as the old zero-variance fixture. The selected-q signed value remains-6/60000, not a negative full energy.

Earlier review/acceptance and checker candidates remain preserved. This addendum supersedes the old target-byte/Perron qualification only. No new bound or scientific scope is claimed.
