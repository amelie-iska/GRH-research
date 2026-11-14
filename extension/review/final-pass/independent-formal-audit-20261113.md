# Independent formal and mathematical review

**Review date:** 13 November 2026. **Disposition:** all 109 selected local Lean declarations freshly elaborated successfully; no Lean proof defect found in the inspected modules. The review also checks the new reduction, transport, and spin-lift arguments at their stated scope. It does not certify the entire monograph or the external continuum Navier–Stokes proof.

## Fresh executable result

The command was executed from the research repository, using the existing pinned tools and no dependency downloads:

```sh
python extension/lean/verify_all.py \
  --toolchain /workspace/scratch/70763186a94c/.tooling/lean-4.24.0-linux \
  --mathlib /workspace/scratch/70763186a94c/.tooling/mathlib4-v4.24.0 \
  --output-dir extension/lean/independent-verification-20261113
```

Exit status was **0**. The [machine-readable manifest](../../lean/independent-verification-20261113/verification.json) records completion at `2026-11-13T23:42:39.963034+00:00`, source hashes, actual declaration names, per-declaration axiom dependencies, log hashes, and source stability during elaboration. The local absolute paths above describe the actual execution environment; another machine must supply its own paths to the same toolchain and dependency revision.

| Module | Checked declarations | Exit status | Warnings |
|---|---:|---:|---:|
| [BridgeTheorems](../../lean/independent-verification-20261113/BridgeTheorems.log) | 25 | 0 | 0 |
| [QuantumInterfaces](../../lean/independent-verification-20261113/QuantumInterfaces.log) | 7 | 0 | 0 |
| [DiagramGrammar](../../lean/independent-verification-20261113/DiagramGrammar.log) | 16 | 0 | 0 |
| [FluidInterfaces](../../lean/independent-verification-20261113/FluidInterfaces.log) | 34 | 0 | 0 |
| [ReductionContracts](../../lean/independent-verification-20261113/ReductionContracts.log) | 16 | 0 | 0 |
| [TransportContracts](../../lean/independent-verification-20261113/TransportContracts.log) | 11 | 0 | 0 |
| **Total** | **109** | **all 0** | **0** |

Compiler: Lean **4.24.0**, commit `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`. The executable SHA-256 is `8fadc3ed92cc9decb94c96ee9c0876e91e03a3a5e69138f32114f02789e2766c`. The clean tracked mathlib checkout is pinned at `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`.

No declaration depends on `sorryAx` or a new project axiom. The union of reported dependencies is exactly the standard foundations `propext`, `Quot.sound`, and `Classical.choice`. The individual dependency counts are 104, 102, and 80, respectively; these overlap and are not disjoint theorem counts. The checker also rejects local `sorry`, `admit`, `axiom`, `unsafe`, and `native_decide` tokens outside comments and strings. Ordinary `decide` proofs of finite integer-matrix identities are kernel checked, not native-execution certificates.

This is a fresh elaboration of the project source against cached compiled imports. The compiler, operating system, and cached Lean/mathlib environment remain trusted. It is not an independent source rebuild of Lean and every dependency, and it is not a second proof-assistant implementation checking exported kernel terms.

## Material actually inspected

The reviewer read the six complete local `.lean` modules, their `lakefile.toml`, `lean-toolchain`, verification driver, current formalization README, and the new declaration map. The earlier 82-declaration map was consulted for the selected component correspondences and its explicit boundaries. The following new manuscript material was read in full:

- [Exact reduction contracts](../../manuscript/chapters/reduction-contracts.tex).
- [Corrected tropical-quiver transport and information contracts](../../manuscript/chapters/toric-transport-audit.tex).
- [Global spin-lift compatibility](../../manuscript/chapters/quantum-spin-scope.tex).

The existing final-pass tropical-source and microscopic-fluid reviews were also read. This preserves their source provenance without asserting a fresh complete reading of every source manuscript, every bibliography item, every earlier monograph proof, or all external analytic estimates.

## Statement-strength and non-vacuity review

The local formal statements concern actual mathematical objects: finite matrices, linear maps, linear equivalences, rational polynomials, seminormed groups, explicit typed syntax, and coordinate derivatives. They do not substitute an undefined `NavierStokes`, `GRH`, or `MassGap` predicate and then assume its conclusion.

Some results deliberately take structural hypotheses, such as `B.comp A = 0`, skew-symmetry, a recurrence equation, or the soundness of a generic rewrite rule. These are legitimate conditional interface theorems. They do not establish that an arbitrary learned model satisfies those hypotheses. Concrete structural rules are separately proved sound in `DiagramGrammar`; thus its generic contextual-soundness result is not the only evidence supplied for its implemented rule family.

Several easy declarations, including integer rank substitutions and scalar counterexamples, are useful exact components rather than difficult standalone research theorems. Counting 109 declarations does not turn them into 109 new continuum results or 109 fully formalized manuscript environments. The manuscript-to-declaration maps retain this distinction.

### Reduction and approximation

The factorization equivalence uses surjectivity to make the reduced space exactly the observation image and to prove uniqueness. Its set-theoretic construction uses choice; no continuity, computability, or measurable-selection conclusion is smuggled into the theorem. The discrete trajectory argument is a genuine induction. The continuous-time discussion correctly replaces `P(F(x))` by `DP(x)F(x)` unless `P` is linear.

The unresolved-fiber error bound is the triangle inequality in an actual seminormed group. It does not require an unstated probability distribution or claim an average-loss guarantee. The signed cancellation counterexample has nonzero summands and a nonzero residual for every natural parameter: `X + (-X + X^(k+2)) = X^(k+2)`. It therefore does not exploit the convention that the order of zero is infinity.

### Transport and Hodge structure

The chronological product places later maps on the left, and the residual recurrence transports old discrepancies through the next arrow. The finite telescope is correct without commutativity, invertibility, or flatness. The Lean statement uses one fixed module; the manuscript's varying-fiber version is proved in ordinary mathematics and is correctly identified as having a stronger typing scope. The scalar flat-cycle example genuinely refutes the wrong prefix convention.

The Hodge discussion correctly separates positivity of `D0 D0* + D1* D1` from the complex condition `D1 D0 = 0`. Orthogonality of exact and coexact components requires the latter condition. Neither positive finite matrices nor exact finite complexes supply a mesh-uniform continuum gap or an arithmetic identification of eigenvalues.

The finite fluid module proves both an algebraic work balance and an actual derivative statement from coordinate derivative hypotheses. It does not prove existence, uniqueness, time integration stability, or global continuation of the semidiscrete ODE. The pressure-work lemma is separate; the main displayed work-balance vector has no pressure term. These are appropriately scoped statements, not a hidden continuum Navier–Stokes proof.

### Quantum interpretations

The trace obstruction is stronger than a specifically quantum claim: normalized trace and two trace-preserving linear maps already rule out a zero composite. Positivity is unnecessary for this obstruction. It therefore applies to quantum channels, while the proposed instrument-branch alternative needs trace-nonincreasing branches and explicit success probabilities.

The manuscript's trace-norm contraction proof is valid for Hermitian discrepancies under positive trace-preserving maps, using the positive unital adjoint and the dual trace-norm formula. Complete positivity supplies the physical ancillary-system condition. This argument is ordinary mathematics; the Lean trace obstruction does not claim to formalize it.

`QuantumInterfaces` proves exact Pauli and binary-boundary algebra. Its Euler declaration is explicitly an arithmetic substitution after the topological facts have been supplied. It does not prove surface classification, a complete quantum error-correction theorem, training convergence, or an algorithmic quantum advantage.

### Information, relaxation, and the spin lift

The deterministic-certificate information argument conditions on the full prefix and correctly obtains zero extra Bayes information. Its lossy-state example and conditional-KL decomposition identify how a restricted predictor can nevertheless benefit. The distinction prevents an actual learned-predictor improvement from being incorrectly equated with an oracle conditional mutual information.

The damping obstruction is correctly restricted to the bound `(1-eta)+eta L` and is accompanied by an actual expanding scalar example. The sufficient relaxation criterion separately assumes two-trajectory strong dissipativity and a Lipschitz bound. Expanding the squared distance proves its stated contraction factor; one-trajectory energy dissipation alone is not used as a replacement hypothesis.

The periodic spin-lift obstruction is also sound under its explicitly global assumptions. Integration of `omega · grad(phi)` vanishes by periodicity and divergence-free vorticity. Cauchy–Schwarz gives the pointwise spinor-gradient lower bound. The example `exp(-nu t)(sin z, cos z, 0)` has zero advective derivative, Laplacian `-u`, and curl `u`; it is an exact smooth unforced solution whose positive helicity density contradicts the required integral compatibility. This excludes that global lift, not the velocity solution or every patchwise representation. These two propositions have written proofs and are not among the Lean declarations.

## Clarification identified during the review

The stochastic-limit paragraph initially wrote a Fokker–Planck equation with added `sigma_src - sigma_sink` terms immediately after deriving a conservative Markov generator only from conditional increments. Conditional first and second moments of a conservative transition process do not by themselves introduce sources or sinks. The recommended correction is to display the conservative equation for that derivation, then state separately that branching, killing, injection, or boundary fluxes require separately specified dynamics and their own terms. This is a scope correction in prose and does not change any Lean theorem. The coordinating reviewer was informed before publication.

The Taylor-remainder, tightness, and convergence assumptions are otherwise retained explicitly; the paragraph is not represented as a complete diffusion-limit theorem.

## Remaining proof obligations

The fresh local result does not close these larger obligations:

- A complete independent rebuild and definition/comparator audit of the external forced Navier–Stokes continuum formalization.
- A derivation of the unforced positive-viscosity problem from that forced result.
- Operator-domain control and the required arithmetic spectral/determinant identification for GRH or Hilbert–Pólya.
- A constructive quantum-field limit with a uniform positive Yang–Mills mass gap.
- Complete formal proofs of every manuscript environment and every external theorem used.
- Computational-security proofs or an independent implementation audit of the cryptographic backend.
- Training, statistical generalization, or quantum-complexity guarantees inferred only from algebraic expressivity.

No new Lean declarations were needed to repair the inspected statements. The raw source, printed types, axioms, and this review's limited coverage provide the evidence for the claims actually made.
