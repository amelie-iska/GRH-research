# Independent source and claim audit: fluid extension

Audit date: 13 November 2026. This is a targeted independent audit of the recovered project, current primary sources, and remaining verification gaps. It is not a second claim to have manually reread every source or rebuilt the upstream continuum formalization.

## Finding

The OpenAI release exists. Its scope is forced three-dimensional Navier–Stokes breakdown, addressing Clay alternatives C and D. The recovered project preserves that scope accurately. The inspected review documents do not present its finite algebraic Lean modules as a replacement for the complete continuum construction. No correction to those distinctions was needed in this pass.

The principal remaining gaps are reproducibility of the prior transcript inspection, six unavailable full texts, and completion of the separately tracked upstream Lean/Comparator verification. A new algebraic interpretation should be evaluated by the analytic estimates it preserves, not by whether its terminology resembles the continuum proof.

## 1. Current primary-source confirmations

The [OpenAI announcement](https://openai.com/index/navier-stokes-solution/), dated 8 September 2026, links an analytic paper and a formalization. [Clay's response](https://www.claymath.org/news/navier-stokes-announcement/), dated 11 September 2026, describes an apparent resolution and an ongoing evaluation process. This response does not establish that a prize has been awarded.

[Theorem 1.1 of the released paper](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf) specifies every positive viscosity, zero initial velocity, smooth compactly supported spacetime forcing, and smooth velocity and pressure before time one. Their spatial supports lie in one compact set. The velocity has bounded kinetic energy but unbounded supremum norm as time approaches one. A whole-space global smooth competitor with uniformly bounded energy is excluded; periodization gives the torus result. Its construction balances a concentrating core, oscillatory stress, and successive residual corrections.

The following are logically different propositions:

| Proposition | Status in the sources inspected |
|---|---|
| There exist permitted smooth forcing and initial data causing the stated breakdown | The released theorem's claim |
| Every smooth force causes breakdown | Not claimed |
| The unforced positive-viscosity equation has finite-time blowup | Not established by this release |
| The unforced positive-viscosity equation is always globally regular | Not established by this release |
| Finite-energy weak solutions cease to exist | Not the claim |
| A quantum or molecular model must develop the same singularity | No such conclusion follows |

These distinctions follow by comparing the quantifiers and force hypotheses in [Fefferman's official statement](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf). Alternatives A/B set the force to zero; alternatives C/D permit smooth forcing. Accordingly, a proof of C/D does not logically negate A/B.

The [Constantin–Ignatova–Vicol follow-up, arXiv:2609.20803v2](https://arxiv.org/abs/2609.20803v2), imposes specific anisotropic Type II bounds and exact axisymmetry in a collapsing core. In that setting, real-analytic forcing yields regularity at the putative singularity. Its obstruction to removing the forcing or making it locally uniformly spatially analytic must retain those structural hypotheses. This is not a general theorem settling unforced three-dimensional Navier–Stokes.

## 2. Transcript provenance: prior coverage and this pass

The recovered `extension/review/navier-stokes/microscopic-source-coverage.json` records a prior review of all **249 exposed English transcript segments**, from 00:00 through 32:36, through the public browser transcript interface. The companion `microscopic-source-review.md` contains a timestamped scientific review and explicitly distinguishes the transcript from the description. This prior coverage should be retained as an inspection record.

The cached source directory contains `video-page.html`, `video-description.txt`, and transcript extraction code. The extraction script alone is not evidence of successful extraction: no corresponding executor-local `transcript.json` or `transcript.txt` was found. The prior record states that an export existed in the browser environment but was not independently verified as an executor-local file.

In this pass, both the public watch-page fetch and timed-text endpoint failed through the research tool. Consequently:

1. The project's earlier complete transcript inspection is documented and should not be silently rewritten as description-only review.
2. A fresh independent transcript retrieval was **not** completed here.
3. The project should not advertise a retained, hashed transcript artifact.
4. The source record provides timestamps and review coverage, while the published extension contains authored analysis rather than a redistributed transcript.

The video is an introduction to successive reductions. A mathematical review should distinguish changes of representation, statistical marginalization, approximate closure, and asymptotic limits. None of those operations is interchangeable merely because it discards information.

## 3. Targeted checks on the microscopic references

### Electronic imaging

[Stodolna et al., PRL 110, 213001](https://doi.org/10.1103/PhysRevLett.110.213001), also available in the [AMOLF repository](https://ir.amolf.nl/pub/6240/15739OA.pdf), uses special separability of the hydrogen Stark Hamiltonian to connect measured photoelectron patterns with nodal structure. The experiment is not an informationally complete measurement of an arbitrary many-electron state. The project's distinction between a detector observable, a forward model, and reconstructed state information is appropriate.

[Itatani et al., Nature 432, 867–871](https://doi.org/10.1038/nature03183), with a recovered [author-hosted PDF](https://www.attoscience.ca/pdf/Itatani_Nature_2004.pdf), reconstructs molecular-orbital information from high harmonics in aligned nitrogen. The experimental reconstruction and a numerical time-dependent illustration should not be merged into a single experimental claim.

[Vozzi et al., Nature Physics 7, 822–826](https://doi.org/10.1038/nphys2029) addresses difficulties in the earlier orbital-tomography procedure, including phase information and the role of more complicated emission physics. The recovered PDF's title, authors, and DOI match the requested article, despite its unexpected download filename. Both papers support model-dependent inverse reconstruction; neither establishes a fluid closure or continuum regularity theorem.

### Molecular and kinetic reduction

[Van Dommelen's Born–Oppenheimer section](https://web1.eng.famu.fsu.edu/~dommelen/quantum/style_a/bo.html) concerns a separation within a molecular quantum model. Nuclear motion may still be quantum. Classical nuclei require a further approximation, and ground-state relaxation requires more than unitary evolution. The recovered extension makes these additional assumptions explicit.

[Allen's introduction](https://juser.fz-juelich.de/record/152581/files/FZJ-2014-02193.pdf) distinguishes model choice, numerical simulation, and comparison with physical experiments. A converged molecular-dynamics computation validates a numerical solution of the selected interaction model; it does not by itself validate that model for every thermodynamic regime.

[Golse–Saint-Raymond](https://arxiv.org/abs/0808.0039) proves a hydrodynamic-limit result for specified hard-cutoff collision kernels and asymptotically comparable small Mach and Knudsen numbers. Its limiting objects are Leray solutions. This does not upgrade the limit to universal smooth solutions, nor prove that arbitrary interacting quantum matter converges to the same continuum model. The project's prior review bounds its reading of this supplementary paper and does not claim complete independent proof checking.

[Volkov's DSMC chapter](https://volkov.eng.ua.edu/ME591_491_NEGD/2017-Spring-NEGD-06-DSMC.pdf) gives a kinetic simulation framework with particle weights, time splitting, collision sampling, and statistical observables. Simulation particles need not represent individual molecules one-for-one. Sample variance, finite-cell effects, and time-step error remain distinct from the validity of the kinetic model.

### Model reduction

The original Farhat filenames in the video's bibliography have been replaced. The [current course directory](https://web.stanford.edu/group/frg/course_work/CME345/) contains `CA-AA216-CME345-*` files. The [current Chapter 9](https://web.stanford.edu/group/frg/course_work/CME345/CA-AA216-CME345-Ch9.pdf) concerns hyperreduction. A review of these replacement decks is useful, but it must remain identified as review of the current replacement material, not a byte-identical recovery of the historical decks. The existing project does so.

### Full-text gaps retained

The recovered source ledger identifies these unresolved full-text reviews:

| Requested source | Retained status |
|---|---|
| Jönsson (1961), original German article | Abstract/metadata; the abridged 1974 translation is separately reviewed |
| Cerfon, *Mechanics (Classical and Quantum)* | Requested resource unavailable |
| Parker (1959), DOI 10.1063/1.1724417 | Abstract/metadata |
| Valentini et al. (2015), DOI 10.1063/1.4929394 | Abstract/metadata; subsequent related papers are not substitutes |
| Loudon (1959), DOI 10.1119/1.1934950 | Abstract/metadata |
| Loudon (2016), DOI 10.1098/rspa.2015.0534 | Abstract/metadata |

Fresh searches and publisher requests in this pass did not close these gaps. In particular, a similarly titled 2016 nitrogen-dissociation paper and later NASA reports do not complete review of the specified 2015 paper. The final completion statement should preserve this distinction.

## 4. Independent mathematical checks on proposed connections

The following checks are elementary reasoning, not additional claims extracted from the cited sources.

### Energy and information contraction cannot replace regularity bounds

Choose a nonzero smooth compactly supported divergence-free vector field `v` on three-dimensional space, and define

\[
u_\varepsilon(x)=\varepsilon^{-1}v(x/\varepsilon),\qquad 0<\varepsilon<1.
\]

The chain rule preserves the divergence constraint. Changing variables yields

\[
\|u_\varepsilon\|_2^2=\varepsilon\|v\|_2^2,
\qquad
\|u_\varepsilon\|_\infty=\varepsilon^{-1}\|v\|_\infty,
\qquad
\|\nabla u_\varepsilon\|_\infty
=\varepsilon^{-2}\|\nabla v\|_\infty.
\]

Thus even vanishing energy is compatible with unbounded amplitude and gradients. This family is not asserted to solve Navier–Stokes. Its role is to disprove an attempted implication from energy control alone to regularity.

Similarly, on the unit three-torus, `v_N(x)=(sin(2 pi N x_2),0,0)` is divergence-free. Its energy is bounded independently of `N`, but its maximum gradient grows like `N`. Projection onto any fixed finite Fourier cutoff annihilates this field for sufficiently large `N`. The same reduced observation therefore corresponds to increasingly large unresolved gradients. A quantum encoding or contractive channel that retains only those observations cannot reconstruct the lost bound without additional assumptions.

These counterexamples are consistent with the project's existing concentration and exact-reduction propositions. They do not challenge the usefulness of reduced models; they specify what an additional regularity certificate must actually control.

### Signed tropical data require an analytic realization

Valuations can organize scale exponents. They do not determine signs, amplitudes, phases, or derivative norms. For example, two order-one terms `tau` and `-tau + tau^(k+2)` can sum to a term of arbitrarily higher order. The recovered `ReductionContracts.lean` explicitly formalizes this obstruction for nonzero polynomials.

A valid route from such bookkeeping to a smooth residual is an all-orders estimate. Suppose a smooth residual `R(x,t)`, defined for `t<T`, satisfies on every compact spatial set, for all multi-indices `alpha`, time derivative orders `m`, and integers `N>=1`,

\[
\sup_{x\in K}|\partial_x^\alpha\partial_t^m R(x,t)|
\le C_{K,\alpha,m,N}(T-t)^N.
\]

Then extending `R` by zero at and after `T` gives a smooth function. Each derivative tends uniformly to zero on compact sets; induction using the fundamental theorem of calculus identifies the derivative of each extended derivative with the next extension. This is a sufficient flatness criterion, not an assertion that every residual has that property. Away from the singular location, matching nonzero terminal jets can require a different extension argument.

The universal quantifiers are essential: one finite-order calculation cannot establish all derivative bounds. The existing release chapter already distinguishes flat local residuals from controlled exterior terminal jets and retains differentiated cutoffs and nonlinear correction terms.

### Quantum, toric, and gentle-algebra semantics

A valid finite-dimensional quantum-channel theorem proves a statement about specified positive trace-one matrices and a specified channel. A finite quiver, path relation, or spectral gap proves a statement in its declared algebraic model. Transferring it to a continuum PDE requires a map preserving the relevant state space, domain, dynamics, and norm estimates. Transferring a finite gap to a continuum Yang–Mills mass gap additionally requires a controlled limiting construction. Transferring a finite spectral example to Hilbert–Pólya requires the asserted infinite spectral identity and domain properties. None is supplied merely by naming the finite operator after the desired continuum object.

The project's explicit separation of proved finite interfaces, conditional bridges, and open continuum obligations should remain visible in the site and theorem inventory.

## 5. Formal verification wording

The [upstream repository](https://github.com/openai/NavierStokesAndEuler) advertises Lean 4.34.0-rc2 with Mathlib and Lake. Its [Comparator instructions](https://raw.githubusercontent.com/openai/NavierStokesAndEuler/main/ComparatorChallenges/README.md) describe separate checking against challenge statements using Comparator and its required tools.

The recovered project's `release-build-verification.json` states that a fresh final upstream build had not completed. `final-pass-upstream-recheck.json` was marked `running` when inspected. This audit does not change either status. The root task must use the eventual process result, not this intermediate snapshot, when reporting completion.

Use separate evidence fields for:

- pinned source identity and dependency revisions;
- successful local compilation of the project's own finite modules;
- source screening for proof placeholders;
- successful compilation of the upstream target and its full dependency closure;
- independent statement comparison and exported-kernel checking.

A declaration count, clean grep, copied source tree, or successful finite-module build is not a substitute for the last two outcomes. Conversely, placeholder-bearing challenge files are not by themselves evidence that the submitted solution depends on those placeholders; the dependency closure and checked theorem type decide that question.

## Reviewed project records

- `extension/review/navier-stokes/microscopic-source-coverage.json`
- `extension/review/navier-stokes/microscopic-source-review.md`
- `extension/review/navier-stokes/microscopic-review-qa.json`
- `extension/review/navier-stokes/release-review.md`
- `extension/review/navier-stokes/reduction-contracts-review.md`
- `extension/review/navier-stokes/release-build-verification.json`
- `extension/review/navier-stokes/final-pass-upstream-recheck.json`

This independent pass confirms the project's principal scope distinctions and records the remaining limits of the evidence. It adds no claim to a new proof of unforced Navier–Stokes, GRH, or continuum Yang–Mills mass gap.
