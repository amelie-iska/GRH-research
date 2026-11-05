# Actual high-cutoff geometry and the signed covariance barrier

5 November 2026; exact original Eisenstein family, no new GRH theorem.

For2D/7<=U²<=D, the actual active coefficient is A_U(m)=mu(m)(r_U(m)-1),
where r_U counts ordered coprime factorizations ab=m with both norms>U.
The residual third ideal must be the unit, including the boundary7U²=2D.
The swap(a,b) is fixed-point-free, so every active coefficient is odd/nonzero.
Elementary Eisenstein lattice and squarefree-ideal counting show its normalized
coefficient norm stays bounded below for any fixed nonzero smoothW. This is
not a row-energy lower bound. Legal factor Cauchy+BGL leaves the sameDX
term; multiplying marginal operator norms does not control the coupled rows.

An actual smooth-profile finite counterexample refutes automatic nonnegative
signed covariance. WithD400,U17,nu=1,S above2/3, all72literal B7 rows and
the complete four columns of norms439,439,475,475, a nonnegative smoothW
with exact norm-values10/1 givesQ(C,mu)=-27/25, while pointwiseC_U*mu>=0
and the real Gram is positive definite. Its real eigenvalues54/90 are not
asserted as the full complex Gram eigenvalues. The second guaranteed
nonprincipal subsetNu<=89 has246rows and covariance-69/50, preserving60
raw zero entries. It is not called the whole nonprincipal family.

Implementation: examples/arithmetic_cutoff/signed_covariance.py. Both finite
complex Gram matrices and all1272character entries were independently
reconstructed by directF439/F19/F25 exponentiation, without author helpers.
The profile is a genuineC-infinity bump construction, not a claim that
arbitrary finite weights are smooth. These finite sign counterexamples do
not refuteBT_sigma, its lower covariance budget, or an asymptotic bound.

The exact two-cutoff Perron factorization also survives review. Its normal
correction region permits some negative auxiliary lines, but reciprocalL
zero divisors and crossed residues cannot simply be dropped. The exact
sharp cutoff, with half-integer endpoint and finite-height error, follows
from an absolutely convergent a,b series even onRe(s)>1/2. Safe contours
recover the oldU^(2-4delta)energy cost, retainingM4(W)^2,fixedmargins and
all conductor/deletion uniformities. The sliceF(s,z,0)=1/L^T0(s+z,psi)
is meromorphic; it does not supply an unconditional zero-free shift.

Shared complete exposition: papers/signed-bilinear-{core,details}.tex;
book chapter40 uses the same fragments. Full attempts and independent
proof/TeX reviews: planning/signed-bilinear-20261105/. Fixed finite exact
reports: outputs/checks/2026-11-05-signed-bilinear/. The priorU-independent
envelope remains the best proved global estimate here, withD^(1/2)relative
loss atH=D^(3/4). Signed covariance with a quantitative lower budget,
near-saturating neighboring blocks, reciprocal residue control, full actual
analytic Lean and the positive determinant/zero-location bridge remain open.
No new dependency, GPU/model job, Lean declaration or GRH completion.
