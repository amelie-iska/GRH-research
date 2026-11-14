# Quantum-tropical fluid realizations: source assessment and research design

Continuation date: **14 November 2026 (UTC)**. The filename retains the
13 November continuation identifier.

This note proposes a physical realization layer for the project's finite
quantum-ToricGT models. The proposal combines typed graph composition,
admissible quantum operations, a classical tropical controller, and a
substrate-specific input/output model. These components have different
mathematical meanings and different validation requirements.

The cited literature supplies individual physical and mathematical
ingredients. **None of the cited papers demonstrates the combined
ToricGT architecture.** A material's microscopic quantum description, a
nonlinear optical response, and a demonstrated quantum information
processor are also different claims. The seven-platform comparison below
keeps those distinctions explicit.

The companion chapter is
[quantum-tropical-realizations.tex](https://github.com/amelie-iska/GRH-research/blob/main/extension/manuscript/chapters/quantum-tropical-realizations.tex).
The separate bibliography is
[quantum-tropical-substrates.bib](https://github.com/amelie-iska/GRH-research/blob/main/extension/manuscript/quantum-tropical-substrates.bib).
The mathematical connections and experimental proposals in this note are
author-derived. Statements about the source papers have linked primary
evidence and a reading-scope record in Section 10. No full third-party
paper or transcript is redistributed here.

## 1. Repository meaning and provenance

The relevant starting point is the actual code and manuscripts, rather
than a loose association between the words “toric,” “quantum,” and
“fluid.”

| Source | Revision used | Material examined in this continuation |
| --- | --- | --- |
| [ToricGT implementation](https://github.com/amelie-iska/ToricGT/tree/a5199bc989a6fb170e21220e5e87bf95bc2fc0b4) | a5199bc989a6fb170e21220e5e87bf95bc2fc0b4 | Full finite toric-algebra module; selected tropical-attention definitions and aggregation; the existing reviewed source inventory. |
| [ToricGT-Program](https://github.com/amelie-iska/ToricGT-Program/tree/f91ba1811b5a4f70d53c7120acf8ca2a0049f85b) | f91ba1811b5a4f70d53c7120acf8ca2a0049f85b | README and selected Paper V definitions of primitive moves, gradings, trajectory counts, scalar features and toric relations. |
| [Tropical Quivers of Architectures](https://github.com/amelie-iska/Tropical_Quivers_of_Archs/tree/2b6ab79a685e2c6233fb8892e59589951feeddad) | 2b6ab79a685e2c6233fb8892e59589951feeddad | README; selected typed-quiver, operator-composition and weighted-gain passages. |

The Program and Tropical Quivers revisions were checked against their
cached Git HEADs. The selected ToricGT implementation files were checked
by SHA-256 against the
[existing source ledger](https://github.com/amelie-iska/GRH-research/blob/main/extension/review/quantum-toricgt/source-coverage.json).
That implementation revision is distinct from the Program's historical
ToricGT gitlink at 17960fc87; they must not be silently treated as the same
checkout. This continuation is a targeted reading, not a fresh full audit
of every upstream manuscript.

For reproducibility, the checked ToricGT review-text digests were as
follows. These identify the stored text copies, which can include a
terminal newline added during connector storage; the ledger separately
records the original Git blob identities.

| File in src/toricgt | SHA-256 |
| --- | --- |
| graph_tokenizer.py | 5c12e29a069f6c8b65830b0bc1028ad3463353ff92402f8a9136d947c6fec943 |
| tropical_attention.py | 22e2925bceca74dd60a1e55739f44781c3120140f817e973a71cb1b9f8e715d6 |
| toric_algebra.py | c1437e50eb783dd20d29eb83f522f769e18c3964d79feb95d93fd93e27b9f1f3 |
| soft_moe.py | cf6cf0e5b6d129da2ecbf19d5c547d22bba2e3037f37c3828cf5128a2b1b5d27 |

Three consequences matter for the new design.

First, the implementation's tropical attention forms ordinary
dot-product scores and then applies a max-plus aggregation. The
aggregation is piecewise affine in its supplied scores and values;
this does not make the whole trainable map piecewise affine in every
original input.

Second, the finite clock and shift matrices implement a root-of-unity
Weyl relation. Rational approximants to a parameter provide finite
matrix models; a finite matrix algebra is not a faithful representation
of an irrational noncommutative torus.

Third, Paper V's commutative semigroup grading forgets path order.
Its binomial relations constrain suitable scalar features. Two
operator sequences with the same primitive-move counts need not
implement the same quantum channel. The physical compiler must
independently check the relations it intends to preserve.

## 2. A realization contract

Specify a finite quiver Q, intended relations R, state spaces, allowed
controls, an encoding E, physical evolution P, and a readout D. A
realization claim should state the domain on which

\[
       D\circ P_\theta\circ E \simeq F_\theta
\]

approximates the desired graph operation, the metric used for this
comparison, and an explicit error budget. For a classical device this
may be a bounded error in observable trajectories. For a quantum device
it may be an operational distance between channels or a more restricted
and explicitly named set of measured observables.

| Project object | Proposed physical interpretation | Obligation before claiming realization |
| --- | --- | --- |
| Typed vertex and edge | State sector, local mode, allowed transition or control port | Define units, dimensions, accessible couplings and the encoding. |
| Finite Weyl feature | Calibrated operators or measured correlations in a finite subspace | Verify the intended commutation relation and account for leakage. |
| Tropical score | Classical route cost, log-probability or a bound on a positive gain | State what quantity is positive and what information is discarded. |
| Quiver relation | Equality or vanishing of a specified composition | Check it in the category actually used: linear maps, instruments, or channels. |
| Learned fluid feature | Observable of a discretized or reduced physical model | State conservation laws, closure assumptions and domain error. |
| Gain witness | Bound on changes in outputs under changes in inputs | Justify the gain on the claimed domain, then check the finite inequalities. |

A zero relation has a particularly useful diagnostic. The composition of
two trace-preserving channels on a nonzero state space cannot be the
zero map, because it preserves the trace of a normalized input. A
forbidden path can instead be absent from the routing graph or have a
zero trace-decreasing instrument branch. Thus a gentle-algebra
presentation cannot be copied verbatim into a category of unconditional
trace-preserving channels.

Likewise, equal channels and equal operator amplitudes are different
requirements. If two unitaries differ by a global phase they induce
the same conjugation channel. Their relative phase can still matter
when they are coherently controlled in different branches of a larger
interference experiment.

## 3. Incoherent and coherent graph transitions

### 3.1 Classical location with a quantum internal state

Let H_v be a finite-dimensional Hilbert space at vertex v and use the
direct-sum algebra

\[
  \mathcal A=\bigoplus_v\mathcal B(H_v),\qquad
  \rho=\bigoplus_v\rho_v,\quad
  \rho_v\succeq0,\quad \sum_v\operatorname{Tr}\rho_v=1.
\]

The location register is classical, while each nonzero block can retain
internal quantum coherence. A useful general transition specification
assigns edge Kraus operators

\[
 K_{e,a}:H_{s(e)}\longrightarrow H_{t(e)},\qquad
 \sum_{e:s(e)=v,a}K_{e,a}^\dagger K_{e,a}=I_v,
\]

and defines

\[
  (\mathcal T\rho)_w
    =\sum_{e:t(e)=w,a}K_{e,a}\rho_{s(e)}K_{e,a}^\dagger.
\]

Embedding each K as its source-to-target block in the full direct-sum
Hilbert space gives a Kraus representation. The displayed normalization
makes the sum of adjoint products the identity, proving complete
positivity and trace preservation. This finite construction follows
the open-quantum-walk pattern; Attal and colleagues formulate the
operator-valued outgoing normalization and block-state evolution in
Section 2 of their [author text](https://arxiv.org/html/1402.3253v1)
(qtsAttal2012).

The vertex masses are Tr rho_v. They need not form a closed classical
Markov chain in the general construction: the probability of an edge
can depend on the internal state. The companion chapter deliberately
uses the more restrictive form

\[
  (\mathcal T\rho)_i=\sum_jP_{ij}\Phi_{ij}(\rho_j),
  \qquad \sum_iP_{ij}=1,
\]

with each Phi_ij trace preserving. Under those additional assumptions,
and for a prescribed P, the masses do satisfy m'=Pm. This is a clear
starting model for conservative transport.

### 3.2 Coherent transitions require a larger algebra

Coherence between distinct locations belongs to
B(direct sum H_v), including its off-diagonal blocks. A graph Hamiltonian
can include local terms and Hermitian pairs of hopping operators. In a
finite Markovian open-system model, an admissible generator has the form

\[
 \mathcal L_u(\rho)=-i[H_u,\rho]
 +\sum_a\gamma_a(u)
 \left(L_a\rho L_a^\dagger
 -\tfrac12\{L_a^\dagger L_a,\rho\}\right),
 \qquad H_u^\dagger=H_u,\quad\gamma_a(u)\ge0.
\]

For fixed time-independent coefficients this generates a CPTP
semigroup. The historical primary source is
[Lindblad's generator paper](https://link.springer.com/article/10.1007/BF01608499)
(qtsLindblad1976); only its publisher abstract and bibliographic record
were available in this continuation. The finite channel claims in this
project have their own explicit arguments.

The direct-sum walker model is also different from a tensor product of
many local quantum systems or a bosonic Fock space. A physical fluid
may require those many-body descriptions. A finite truncation must
state its occupation cutoff, leakage estimate and the observables
whose errors it controls.

No discrete channel becomes a Navier--Stokes discretization merely
because it conserves total mass. A fluid interpretation additionally
requires momentum and energy variables, constitutive assumptions,
boundary conditions, relevant scale limits and consistency estimates.
Those are independent obligations in the project's existing
microscopic-to-fluid reduction framework.

## 4. Nonlinear dynamics and operator control

The term “nonlinear operator algebra” needs a precise interpretation.
The following mechanisms can coexist, but they should be recorded
separately.

| Mechanism | What is nonlinear? | What remains linear? |
| --- | --- | --- |
| Interacting Hamiltonian | The Hamiltonian can be a polynomial in creation, annihilation or other noncommuting operators. | For a prescribed Hamiltonian, the density-matrix equation and its channel are linear in the input density matrix. |
| Mean-field closure | An order parameter or state-dependent effective Hamiltonian can obey a nonlinear equation. | The underlying microscopic theory need not acquire nonlinear deterministic quantum channels. |
| Conditional measurement | Normalization by the outcome probability is nonlinear when that probability is nonzero. | Each unnormalized instrument branch, and the outcome-averaged channel, is linear and completely positive. |
| Classical feedback | Measured or estimated features select subsequent controls through a nonlinear law. | The operation for each fixed control setting can remain CPTP. |
| Koopman lifting | The original state dynamics can be nonlinear. | Composition acts linearly on scalar observable functions; a finite chosen dictionary need not close. |

For a measurement branch M_y, the normalized state is
M_y rho M_y-dagger divided by its trace, only when that trace is positive.
An unknown state's exact expectation values cannot be supplied to a
controller without a preparation and measurement protocol. An
ideal expectation-driven recursion is therefore an ensemble-level
model until its readout costs and errors are included.

Carusotto and Ciuti's selected mean-field and fluctuation passages
distinguish driven dissipative Gross--Pitaevskii descriptions from
regimes requiring quantum correlations. Amo and colleagues provide
an experimental polariton-flow example. They motivate a fluid
substrate, without equating a mean-field simulation with correlated
quantum processing.
See [the review](https://arxiv.org/html/1205.6500v3) and
[the experimental author abstract](https://arxiv.org/abs/0812.2748)
(qtsCarusottoCiuti2013; qtsAmo2009).

For finite closed-system control, accessible Hamiltonians generate
a Lie algebra that constrains reachable unitaries. Unitary
conjugation preserves a density matrix's spectrum; having all
unitaries available is not the same as having all CPTP maps.
Albertini and D'Alessandro make the operator, pure-state and
density-matrix reachability distinctions explicitly in
[Sections 2--3 of their author paper](https://www.math.unipd.it/~albertin/26.pdf)
(qtsAlbertiniDAlessandro2003).
An open-system design must additionally specify available jumps,
reset resources, measurements and admissible controls.

Koopman lifting offers a useful reduced-model interface, but it does
not remove closure error. If a finite dictionary satisfies

\[
 \psi(F(x))=K\psi(x)+r(x),
\]

then r is part of the model discrepancy unless it is proved to vanish
on the claimed domain. Brunton and colleagues discuss restrictions on
finite invariant subspaces that reconstruct the original state in
[their primary control study](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0150171)
(qtsBrunton2016). Fitting a small residual on training trajectories
does not establish a uniform domain bound.

## 5. Toric relations and tropical envelopes

### 5.1 Preserve the intended relation, not just its label

The implementation's finite Weyl matrices are a natural test case.
With its shift convention, S C = omega C S. The two conjugation
channels nevertheless commute, because a global scalar phase cancels
in A rho A-dagger. A channel-only test cannot identify that projective
phase. A phase-sensitive realization claim requires an appropriate
enlarged coherent protocol or an operator calibration.

For a general quiver relation expressed as a linear combination of
paths, an operator representation must make the corresponding ordered
composition vanish. A channel relation is instead an equality of
superoperators, which can be checked in finite dimensions through
their Choi representations. A commutative scalar grading alone
establishes neither condition.

This gives the project's order and surface-algebra language an
operational role: record legal compositions and explicitly retained
relations. The physical realization is a separate representation
problem. Topology, scalar toric relations and a quantum deformation
should be attached to named maps and hypotheses.

### 5.2 Positive sums admit controlled logarithmic reduction

For finitely many real scores and tau > 0, let

\[
 L_\tau(s)=\tau\log\sum_{j=1}^m e^{s_j/\tau},
 \qquad M=\max_js_j.
\]

Factoring out exp(M/tau) gives

\[
       M\le L_\tau(s)\le M+\tau\log m.
\]

This is an exact finite bound. The parameter tau is an algorithmic
scale unless a physical temperature interpretation has independently
been established. For positive route weights, products become sums
of logarithms and competing routes produce a log-sum-exp. An exact
max-plus limit drops a quantified multiplicity term.

General instrument branch probabilities may depend on the internal
state, so fixed edge scores require either a justified restriction
or a bound. For example,
Tr(K rho K-dagger) <= ||K||^2 Tr rho for positive rho.
This yields one-sided norm envelopes; it does not identify the
probability with a state-independent edge weight.

Coherent paths add amplitudes. The triangle inequality provides an
upper bound on the norm of their sum, followed by any desired
positive logarithmic envelope. It provides no comparable lower
bound in the presence of destructive interference. The pair I and
-I already has a vanishing coherent sum while both separate norms
are one. Entrywise maxima of complex amplitudes or density matrices
are not supplied by the CPTP formalism.

These distinctions also explain why largest-path growth alone
need not equal the norm growth of a graph update that sums paths.
The companion chapter's finite feedback example exposes that
gap without relying on a continuum approximation.

## 6. A control and measurement budget that can be checked

Suppose a driven update has nonnegative block gains g_vw on a
specified invariant domain:

\[
 \|F_v(x,u)-F_v(y,u)\|
 \le \sum_w g_{vw}\|x_w-y_w\|.
\]

Positive weights w and a number q < 1 satisfying G w <= q w
give contraction in the weighted maximum norm. With additive
weighted error bounded by delta, iteration gives

\[
 d_n\le q^n d_0+
       \delta\sum_{k=0}^{n-1}q^k.
\]

The eventual error budget is at most delta/(1-q). The certificate
checks a finite inequality; the independent scientific obligation
is to justify G and delta on the operating domain. Sampled
Jacobians or a good empirical prediction score do not by themselves
supply a global gain bound.

The companion chapter provides an exact two-qubit feedback model
whose weighted gain is 5/8 even though the largest unweighted row
sum is 7/4. The model uses nonlinear classical feedback around
fixed-control CPTP channels. Its finite calculations and
implementation receipts must be distinguished from any hardware
experiment.

A useful general fading-memory baseline is the channel

\[
 \Phi_u(X)=(1-\alpha)U_u XU_u^\dagger
                 +\alpha\sigma_u\operatorname{Tr}X,
 \qquad 0<\alpha\le1.
\]

For two states under the same prescribed u, the replacement terms
cancel and trace distance contracts by 1-alpha. CPTP evolution
without such a strict condition is merely nonexpansive in general;
unitary evolution preserves trace distance. If u is itself chosen
by feedback from the state, its dependence adds gain terms and the
fixed-control contraction is no longer the whole proof.

Likewise, the bound for ordinary damping,
(1-eta)I + eta F, is (1-eta)+eta L when F has Lipschitz
bound L and 0 <= eta <= 1. If L > 1, that estimate does not
certify contraction. Special cancellations can improve the actual
map, but they require a separate argument.

For measured observables, Hoeffding's original independent bounded
variable bound supplies a finite-shot component. The original
[scan](https://www.cs.rpi.edu/academics/courses/spring06/random/hoefding.pdf)
was visually checked at printed page 15, Theorem 1, equation (2.3)
and its interval-rescaling paragraph (qtsHoeffding1963).
For M settings fixed in advance, N independent shots per setting
with outcomes in [-1,1], and a common tolerance epsilon,
rescaling and a union bound give

\[
 \Pr\{\text{some error}>\varepsilon\}
   \le 2M e^{-N\varepsilon^2/2}.
\]

Thus N >= 2 log(2M/delta)/epsilon^2 suffices for simultaneous
confidence 1-delta. This bounds sampling error for the stated
experiment. It does not cover calibration bias, an unlimited
time horizon, arbitrary correlated reservoir samples, or repeated
adaptive reuse of a validation set without additional analysis.

Fujii and Nakajima's primary quantum-reservoir work supplies a
numerical learning precedent, rather than an experimental
quantum-speedup result. Its relevance here is the input, quantum
dynamics and trained-readout architecture.
[Author record](https://arxiv.org/abs/1602.08159)
(qtsFujiiNakajima2017).

## 7. Seven representative substrate families

This table is a design comparison, not a ranking of performance.
The proposal column is our connection to the project. It is not
attributed to the cited authors.

| Substrate | Established ingredient in the selected primary source | Proposed project role | Discriminating realization test |
| --- | --- | --- | --- |
| Exciton-polariton fluids | Driven interacting light-matter fluids; an experimental superfluid-flow example. [Carusotto--Ciuti](https://arxiv.org/abs/1205.6500), [Amo et al.](https://arxiv.org/abs/0812.2748). | Spatial modes as vertices; calibrated drive/loss and couplings as controls; fluid observables as features. | Compare a specified input/output operator with measured dynamics, then test whether the claimed regime needs correlations beyond mean field. |
| Ultracold atomic gases | Controlled localized loss affects open many-body condensate dynamics. [Barontini et al.](https://arxiv.org/abs/1212.4824). | A quantum-matter testbed for a small graph of modes with controlled dissipation. | Establish the actual accessible channel family, repeated preparation and finite readout budget; do not infer arbitrary programmability from controllable loss. |
| Superconducting cavity circuits | Engineered two-photon loss confined an oscillator to a quantum-state manifold. [Leghtas et al.](https://arxiv.org/abs/1412.4633). | Finite bosonic encodings, dissipative memory and calibrated graph couplings. | Bound cutoff leakage and decoherence; verify the chosen logical operations and measured observables. |
| Programmable integrated photonics | A configurable interferometer demonstrated transport using continuous-wave laser inputs and photodiode intensities. [Harris et al., Methods](https://arxiv.org/html/1507.03406v3). | Calibrated coherent wave routing, finite Weyl-style transformations and a classical controller. | Distinguish a wave analogue from a nonclassical-state experiment; quantify loss, drift, preparation and detection. |
| Magnonic networks | A YIG spin-wave device performed reservoir tasks with computer-based output processing. [Namiki et al.](https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/aisy.202300228). | A physical nonlinear-memory baseline and a candidate graph-coupled reservoir. | Measure memory, transfer response and total readout cost; a quantum-state claim requires separate nonclassical preparation and verification. |
| Soft bodies and fluid-structure systems | A soft silicone body's dynamics supported nonlinear computation with trained readout. [Nakajima et al.](https://www.nature.com/articles/srep10487). | A classical geometry-dependent reservoir, including a possible inverse-designed elastic/fluid interface. | Identify an operating-domain model and sensor/actuator error; distinguish bioinspiration from a demonstrated living information processor. |
| Natural pigment-protein excitation networks | Experimental and model studies limit broad claims of long-lived useful electronic coherence in the systems they examine. [Duan et al.](https://pubmed.ncbi.nlm.nih.gov/28743751/), [Zerah Harush--Dubi](https://pmc.ncbi.nlm.nih.gov/articles/PMC7888942/). | Natural coupling motifs and open-system transport models as constrained design priors. | Separate electronic and vibrational signals, transport function and controllability; neither efficient transport nor biological origin establishes a programmable quantum computer. |

The final row is deliberately narrower than a universal conclusion
about quantum biology. Duan and colleagues examine an identified
photosynthetic system and conditions; Zerah Harush and Dubi analyze
specified open-system models. Neither justifies a claim that all
biological quantum effects are absent. Conversely, those sources
do not support treating natural photosynthesis as an already
available general quantum learning substrate.

The practical first comparison should use one declared task,
input bandwidth, output tolerance, preparation/reset rule and
resource accounting. Include sensors, control electronics,
calibration and readout processing. A small platform-specific
experiment with a falsifiable operator target is more informative
than a claim of universal substrate equivalence.

## 8. De novo material and geometry design

There are at least two distinct generative tasks.

**Material proposal.** MatterGen conditions generation of inorganic
crystals on material attributes; the final publication includes
an experimentally tested candidate. It does not generate a
verified quantum channel from its matrix specification.
See the [final publisher record](https://www.nature.com/articles/s41586-025-08628-5)
and [author institution record](https://www.microsoft.com/en-us/research/publication/a-generative-model-for-inorganic-materials-design/)
(qtsZeni2025).

**Device geometry proposal.** Jiang and Fan use a physics-driven
generative network with forward and adjoint electromagnetic
calculations to search dielectric metasurface designs. The paper
explicitly distinguishes broad global search from a guarantee
of a globally optimal solution.
[Author PDF, introduction and Methods](https://fanlab.stanford.edu/wp-content/papercite-data/pdf/jiang2019global.pdf)
(qtsJiangFan2019).

These methods motivate different stages of our proposed pipeline;
they are not interchangeable solvers. A crystal generator does
not establish fabricated device geometry, coherence time or
control bandwidth. An electromagnetic geometry optimizer does
not establish a material's synthesizability or many-body quantum
state preparation.

### A proposed reproducible pipeline

1. **Declare the target.** Choose the quiver, retained relations,
   state space, task, input distribution, measured observables
   and acceptable error. State whether coherent quantum
   processing is necessary or a classical wave response suffices.
2. **Choose the representation and substrate.** Specify sectors,
   modes or tensor factors; accessible controls; losses; reset;
   and the encoding/readout maps. Check elementary feasibility
   before optimizing a large model.
3. **Generate candidates under explicit constraints.** Use
   composition and symmetry priors for a material, or geometric
   and connectivity constraints for a device. Preserve generator
   version, inputs and seeds.
4. **Evaluate with the correct forward model.** Use a solver
   appropriate to the claimed physical regime. Include boundary
   conditions, material dispersion or constitutive laws,
   discretization error and parameter uncertainty. A high
   learned surrogate score is only a proposal.
5. **Identify a reduced controlled model.** Fit and test its
   input/output map on held-out conditions. For a quantum model,
   preserve CP/trace constraints and track truncation. For a
   classical fluid or elastic model, preserve the applicable
   conservation and passivity constraints.
6. **Co-design the controller and error certificate.** Optimize
   task performance together with admissible controls and a
   justified gain envelope. Check positive-weight witnesses
   independently and propagate model, numerical and readout
   errors. A proposal is rejected when any required gate fails.
7. **Stress the candidate before a physical study.** Vary the
   declared uncertain parameters and operating conditions.
   Keep an untouched evaluation set. Record failures and
   sensitivity, including loss of a tropical routing margin.
8. **Measure a selected physical realization.** Under an actual
   experimental program, calibrate the prepared device,
   compare its operator or observable trajectories with the
   model, and repeat under drift and controlled perturbations.
   A simulation remains labeled simulation until that evidence
   exists.
9. **Compare resources fairly.** Use conventional numerical
   solvers, classical learned models and simpler physical
   baselines on the same task. Charge state preparation,
   measurement, reset, training and controller costs.

Natural systems can provide topology or material priors in step 3.
They do not bypass steps 4--9. For example, a branching transport
pattern can constrain a classical fluid graph; a pigment coupling
pattern can constrain an open-system model. The retained
structure must still be defined and measured.

## 9. Bounded implementation milestones and acceptance evidence

The following sequence separates established finite mathematics
from new scientific results.

| Milestone | Concrete artifact | Acceptance condition |
| --- | --- | --- |
| Finite quantum-control baseline | Rational small-state example, declared channel family and independent gain replay | Exact positivity/normalization construction, state invariance, specified gain inequalities and meaningful rejected controls. |
| Graph-fluid learning benchmark | Versioned discretization, training split, invariant-domain specification and held-out trajectories | Compare conservation, closure residual and propagated error with standard numerical and classical learning baselines. |
| Coherent versus incoherent comparison | Identical graph and task with separately typed coherent and instrument-based evolution | Resolve phase-sensitive observables, loss and measurement costs; show what the tropical envelope retains and discards. |
| One inverse-designed candidate | Generator/solver provenance, constrained design and uncertainty sweep | Reproduce predicted response and reject out-of-domain or physically inadmissible designs. |
| One measured substrate | Calibrated encoding, operations, readout and archived observations | Match the declared observable/channel target within the measured budget and report failures. |
| Broader application | A separately defined spectral, fluid or security claim | Supply that application's missing analytic limit, threat model or continuum argument; do not inherit it from the finite example. |

The first row is the scope of the companion chapter's exact
feedback example and its implementation receipts. This note
does not assert that the later rows have been completed.
Lean coverage must be read from the formal type map; an explicit
paper argument is not automatically a machine-checked theorem.

For Hilbert--Pólya research, finite operator experiments can test
features or proposed approximations, but cannot establish an
infinite-dimensional spectral identification by fitting finite
data. A finite device gap does not solve the continuum
Yang--Mills mass-gap problem. A physical response used in
cryptography needs a separate threat model and security
analysis. The proposed quantum-fluid layer similarly supplies
no new solution of the unforced three-dimensional
Navier--Stokes Millennium problem.

## 10. Exact primary-source coverage and bibliography key map

The following is the reading actually used for this addition.
“Selected” does not mean every equation, reference or
supplement was checked. Abstract-level entries support only
the limited claims attributed to them above.

| BibTeX key | Primary source | Reading in this continuation |
| --- | --- | --- |
| qtsCarusottoCiuti2013 | [DOI 10.1103/RevModPhys.85.299](https://doi.org/10.1103/RevModPhys.85.299); [author HTML](https://arxiv.org/html/1205.6500v3) | Abstract and selected mean-field, fluctuation, superfluid-flow and strongly correlated-regime passages, including the driven GPE and its stated regime. Not a full review of the long article. |
| qtsAmo2009 | [DOI 10.1038/nphys1364](https://doi.org/10.1038/nphys1364); [author record](https://arxiv.org/abs/0812.2748) | Author abstract and bibliographic metadata. Full experimental paper and supplements not reviewed in this continuation. |
| qtsBarontini2013 | [DOI 10.1103/PhysRevLett.110.035302](https://doi.org/10.1103/PhysRevLett.110.035302); [author record](https://arxiv.org/abs/1212.4824) | Author abstract and bibliographic metadata. |
| qtsLeghtas2015 | [DOI 10.1126/science.aaa2085](https://doi.org/10.1126/science.aaa2085); [author record](https://arxiv.org/abs/1412.4633) | Author abstract and bibliographic metadata. No complete experimental-protocol audit. |
| qtsHarris2017 | [DOI 10.1038/nphoton.2017.95](https://doi.org/10.1038/nphoton.2017.95); [author HTML](https://arxiv.org/html/1507.03406v3); [published PDF](https://ciqm.harvard.edu/uploads/2/3/3/4/23349210/harris2017.pdf) | Abstract, selected processor description and Methods measurement paragraph; published first-page author list. Continuous-wave illumination and intensity readout directly checked. |
| qtsNamiki2023 | [DOI/full text 10.1002/aisy.202300228](https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/aisy.202300228) | Abstract, selected introduction, conclusion and discussion of computer readout. No independent reconstruction of benchmark data. |
| qtsDuan2017 | [DOI 10.1073/pnas.1702261114](https://doi.org/10.1073/pnas.1702261114); [PubMed](https://pubmed.ncbi.nlm.nih.gov/28743751/); [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5559008/) | Abstract and metadata; full-text landing content was accessible, but a subsequent targeted fetch returned a browser-check page. No complete spectroscopy analysis is claimed. |
| qtsHarushDubi2021 | [DOI 10.1126/sciadv.abc4631](https://doi.org/10.1126/sciadv.abc4631); [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7888942/) | Abstract and selected opening discussion. A later targeted full-text fetch returned a browser-check page. Full methods were not audited. |
| qtsNakajima2015 | [DOI/publisher 10.1038/srep10487](https://www.nature.com/articles/srep10487); [PubMed](https://pubmed.ncbi.nlm.nih.gov/26014748/) | Publisher-indexed abstract and metadata, corroborated by the author's publication record. Direct publisher access encountered a cookie redirect and a PMC fetch encountered a browser-check page. |
| qtsAttal2012 | [DOI 10.1007/s10955-012-0491-0](https://doi.org/10.1007/s10955-012-0491-0); [author HTML](https://arxiv.org/html/1402.3253v1) | Abstract and selected Section 2 construction, block-state evolution and dilation passages. The journal year is 2012; the available arXiv record was deposited later. |
| qtsLindblad1976 | [DOI/publisher 10.1007/BF01608499](https://link.springer.com/article/10.1007/BF01608499) | Publisher abstract and metadata. Original full proof not independently reviewed here. |
| qtsAlbertiniDAlessandro2003 | [DOI 10.1109/TAC.2003.815027](https://doi.org/10.1109/TAC.2003.815027); [author PDF](https://www.math.unipd.it/~albertin/26.pdf) | Abstract, finite bilinear model, Section 2 reachability definitions and Section 3 Theorem 1/Corollary 3.1. Not every later controllability classification. |
| qtsFujiiNakajima2017 | [DOI 10.1103/PhysRevApplied.8.024030](https://doi.org/10.1103/PhysRevApplied.8.024030); [author record](https://arxiv.org/abs/1602.08159) | Author abstract and final journal metadata. Numerical results are attributed as such; not independently reproduced in this addition. |
| qtsBrunton2016 | [DOI/full text 10.1371/journal.pone.0150171](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0150171) | Abstract, introduction and selected finite-invariant-subspace/closure discussion. The paper's control examples were not rerun in this note. |
| qtsZeni2025 | [DOI/publisher 10.1038/s41586-025-08628-5](https://www.nature.com/articles/s41586-025-08628-5); [author institution](https://www.microsoft.com/en-us/research/publication/a-generative-model-for-inorganic-materials-design/) | Final-publication abstract, metadata and author list, corroborated by the author institution. Direct Nature fetch encountered a cookie redirect; no full synthesis or supplementary-data review. |
| qtsJiangFan2019 | [DOI 10.1021/acs.nanolett.9b01857](https://doi.org/10.1021/acs.nanolett.9b01857); [author PDF](https://fanlab.stanford.edu/wp-content/papercite-data/pdf/jiang2019global.pdf) | Abstract, introduction, Methods and selected optimization/results passages, including the explicit absence of a global-optimum guarantee. Supplements and numerical reproduction not reviewed. |
| qtsHoeffding1963 | [DOI 10.1080/01621459.1963.10500830](https://doi.org/10.1080/01621459.1963.10500830); [original scan](https://www.cs.rpi.edu/academics/courses/spring06/random/hoefding.pdf) | Original printed pages 14--15 visually read; independence setup, Theorem 1 equation (2.3), and interval rescaling checked. No claim to reread all later dependent-variable results. |

All 17 new entries are ASCII BibTeX with explicit LaTeX accent
commands where needed. A standalone BibTeX run resolved every
entry into a bibliography item without warnings or errors.
This syntax check does not extend the scientific reading scope.

The six unresolved original full-text gaps in the separate
[microscopic source review](https://github.com/amelie-iska/GRH-research/blob/main/extension/review/navier-stokes/microscopic-source-review.md)
remain unresolved. The new source assessment and private
transcript-provenance continuation do not convert those gaps
into completed full-paper reviews.
