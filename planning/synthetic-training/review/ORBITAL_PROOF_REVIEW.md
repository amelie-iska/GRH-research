# Orbital-flow proof and numerical review

Reviewed2026-11-04: `papers/orbital-flow-core.tex`,
`papers/orbital-flow-details.tex`, `orbital_transport.py`, browser orbital
formulae, torsion verification source/receipt and the five saved finite systems.
Only review files/evidence changed. No credentials, remote/GPU job, model
repository, training or dependency installation was used.

Verdict: the mathematical statements and scientific scope are accepted. No
required mathematical correction remains. Two stray literal prose plus signs
were reported to the root agent before final build. Source-generated finite
transport, analytic isolated hydrogen and learned finite-MMFF chemical torsions
retain their distinct meanings; neither quantum chemistry nor GRH is inferred.

## Smooth torus field: explicit proof

Let `B=[-pi,pi]^d` and `u=(2pi)^(-d)`. The independent uniform-base/target
coupling has joint density `u q0(x0+D)` in `(x0,D)`. Replacing
`x0=x-tD` gives

`rho_t(x)=u integral_B q0(x+(1-t)D) dD`,

`rho_t(x) v_t(x)=u integral_B D q0(x+(1-t)D) dD`.

Since the wrapped finite-mixture target is smooth and strictly positive,
`rho_t >= min q0 > 0`. Differentiation of these fixed bounded-domain integrals
is justified in space and time; all derivatives are continuous on the compact
torus times `[0,1]`. The quotient is therefore smooth and uniformly spatially
Lipschitz through both endpoints. At time zero the density is uniform; at time
one it is `q0`, and the symmetric D integral gives `v_1=0`. The bounded
geodesic displacement justifies differentiation under the smooth periodic
test-function expectation. This supplies the weak continuity equation. Its
smooth Lipschitz field has a unique flow, whose pushed uniform law is the
specified marginal by continuity-equation uniqueness. This is a statement about
the exact conditional field; trained approximations still require empirical
endpoint checks. The final manuscript now includes these integral formulas.

The score DSM and reverse heat-SDE derivations are also correct: the noise
label is the unwrapped latent Gaussian score averaged over winding
responsibilities, reverse drift is twice the score, and positive heat-time
stopping changes the endpoint law. V2 receipts explicitly verify the appropriate
reference. No hidden zero-noise theorem appears.

## Analytic hydrogen

The displayed1s,2s and Cartesian2p functions have the standard unit norms in
atomic units. Direct radial integrals reproduce one for each basis family.
The1s/2p-z overlap vanishes by parity. Removing common ground-state phase leaves
relative factor `exp(-3it/8)`, giving the stated cosine quantum beat; the2s
node at radius2 and2p-z plane at z0 are correct. The superposition remains
normalized on all of R3, independently of the finite ray-march display extent.

For `(phi_px+i phi_py)/sqrt2`, the explicit wavefunction is
`(x+iy) exp(-r/2)/(8 sqrt(pi))`. It has phase winding+1 and `Lz psi=psi`.
Its probability current is
`exp(-r)/(64pi) * (-y,x,0)`, with stationary density. This has the manuscript's
azimuthal orientation and does not represent a moving classical particle.
The shader implements these normalizations and relative phase consistently.
Rendering opacity, exposure, finite radius and optional isosurface do not
alter the analytic benchmark's meaning. These are nonrelativistic isolated
one-electron hydrogen functions, not ab-initio molecular or peptide density.

## Finite transport and topological controls

The finite-state spectral evolution and current/coherence conventions are
correct. Current is invariant under common phase, and source/browser data
share the same Hamiltonians, eigenvectors and initial vectors. Boundary weight
is a finite observable rather than a definition of bulk topology.

The61-site SSH domain-wall chain has two weak center bonds, strong end bonds,
31 even sites and30 odd sites. All off-diagonal entries are nonzero, so the
zero-energy recurrence fixes even amplitudes up to scale, with odd amplitudes
zero. It produces exactly one zero mode, with amplitude ratio magnitude1/3
away from the center. The48-site matched controls and the QWZ masses-1/-3
retain their explicit winding/link-product convention and physical scope.
The QWZ finite hopping blocks give the stated Bloch signs. No finite boundary
picture is silently promoted to an arithmetic spectrum or a bulk proof.

## Fresh independent local checks

Run:

```sh
OPENBLAS_NUM_THREADS=1 .tools/book-quantum-cpu/bin/python -B planning/synthetic-training/review/check_orbital_math.py
```

`orbital-math-review.json` records independent Krylov `expm_multiply` comparisons
for all five cases at three stored times (maximum state discrepancy
`4.74e-14`, current discrepancy `3.76e-14`, continuity residual `1.12e-16`).
It verifies source/web Hamiltonian/eigenvector/initial data equality and the
domain-wall nullity/recurrence. Hydrogen basis norms are one; finite differences
agree with the analytic vortex current to `2.16e-14` and Lz relation to
`5.32e-13`. A separate explicit conditional-torus-integral numerical continuity
test gives residual `1.53e-11`. The universal statements rest on the displayed
derivations, not these finite tests.

Inspected root-run orbital/torsion/browser receipts corroborate five finite
wavepacket cases, four hydrogen modes, eight chemical learners, intrinsic
RDKit pose agreement and mobile display checks. The reviewer's own checks do
not claim a fresh WebGL/remote execution. Existing private dataset/upload
receipts remain separate from the new analytical/generative demonstrations.
Full operator-domain formalization, new chapter Lean objects, quantum advantage,
and the independent arithmetic determinant/GRH bridge remain outside the
conclusions, as the manuscript states.
