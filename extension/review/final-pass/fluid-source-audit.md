# Independent final pass: microscopic limits and quantum fluid sources

Date: 13 November 2026. Baseline inspected: `c72fa33`. This is a second review of the recovered extension, with additional primary-source checks. It does not replace the earlier source-coverage manifest or certify that every cited paper was read anew.

## Outcome

The existing microscopic and quantum-fluid chapters already distinguish exact changes of variables, information-losing maps, constitutive closures, finite-dimensional results, and continuum theorems. The finite proofs inspected in this pass did not reveal a new contradiction requiring their removal. This is a bounded mathematical review, not an independent verification of every external theorem, every numerical result, or the continuum Navier–Stokes construction.

A useful addition is the narrowly scoped `quantum-spin-scope.tex`. It proves an explicit compatibility obstruction to a **global, smooth, periodic spinor lift with a global periodic auxiliary phase** for one spin representation. Its example is a smooth, decaying exact Navier–Stokes solution. The obstruction concerns those representation assumptions and makes no singularity claim.

## Material inspected

- `extension/review/navier-stokes/microscopic-source-review.md` and `microscopic-source-coverage.json`;
- `extension/review/navier-stokes/farhat-review.md`;
- `extension/review/navier-stokes/quantum-algorithms-review.md`;
- `extension/manuscript/chapters/microscopic-fluid-limits.tex`;
- `extension/manuscript/chapters/quantum-fluid.tex`;
- relevant bibliography entries and the stated formalization boundary in `fluid-verification.tex`.

The manifest contains 24 source groups. Its historical reading claims are evidence of that earlier review, not a substitute for new access. Full-text reading is also different from independent verification of the argument in a source.

## Transcript provenance

The historical record reports 249 exposed English transcript segments, from 00:00 to 32:36, read through the public YouTube transcript interface. It explicitly records unsuccessful caption/API retrieval and the absence of a verified executor-local transcript export or transcript-content hash. No full transcript is present in the checked-out repository.

This pass independently verified the [video identity and chapter description](https://www.youtube.com/watch?v=MXs_vkc8hpY), but could not retrieve the complete transcript through the available web routes. Therefore:

1. The repository has a detailed historical transcript-review record.
2. This pass did not independently reproduce that full transcript read.
3. The description alone is not being represented as a transcript.
4. No full visual/audio-frame review is claimed.

These statements preserve the earlier provenance without overstating its reproducibility.

## Source-access and interpretation checks

| Source | Evidence available in this pass | Required interpretation or remaining boundary |
|---|---|---|
| [Stodolna et al., PRL 110, 213001 (2013)](https://doi.org/10.1103/PhysRevLett.110.213001) | Publisher identity and author-hosted PDF located; historical five-page review retained. | Observed outgoing Stark-state nodal structure is not a measurement of arbitrary complex many-particle amplitudes or classical electron trajectories. |
| [Vozzi et al., Nature Physics 7, 822–826 (2011)](https://doi.org/10.1038/nphys2029) and [Itatani et al., Nature 432, 867–871 (2004)](https://doi.org/10.1038/nature03183) | Publisher identities and institutional/author copies located; historical main-text reviews retained. | Orbital reconstruction depends on an inverse model and experimental assumptions. Do not turn reconstruction into a general single-shot wavefunction-measurement claim. |
| [Jönsson 1961](https://doi.org/10.1007/BF01342460) and [Jönsson 1974](https://doi.org/10.1119/1.1987592) | Original metadata/abstract; abridged English translation located. | The 1974 article is an abridged translation, not an independent replication or complete substitute for the unavailable German original. |
| [Mathur's course](https://www.asc.ohio-state.edu/mathur.16/quantummechanics27-11-17/navigation.html) and [van Dommelen's Born–Oppenheimer section](https://web1.eng.famu.fsu.edu/~dommelen/quantum/style_a/bo.html) | Primary course pages accessible. | Historical scope is completed Mathur modules and selected van Dommelen sections; neither claim means every chapter, animation, or formula image was rechecked. |
| [Farhat's CME345 course](https://web.stanford.edu/group/frg/course_work/CME345.html) | Current nine replacement decks independently opened; PDF page counts agree: 58, 39, 96, 79, 43, 95, 58, 92, 67. | These total 627 PDF pages including overlays. Replacement filenames do not establish identity with the video-era `CA-CME345` files. |
| [Allen, Introduction to molecular dynamics simulation](https://juser.fz-juelich.de/record/152581/files/FZJ-2014-02193.pdf) | Official Jülich PDF accessible in this pass; it includes front matter in addition to the 28-page chapter. | This resolves that URL's transient access failure, not a scientific gap in the already-reviewed alternate copy. No external example code was executed. |
| [Parker 1959](https://doi.org/10.1063/1.1724417) and [Valentini et al. 2015](https://doi.org/10.1063/1.4929394) | Bibliographic/abstract evidence; the latter also has a primary University of Minnesota author record. | Full original texts were not retrieved. Abstract evidence cannot justify detailed claims about all assumptions or derivations. |
| [Loudon 1959](https://doi.org/10.1119/1.1934950) and [Loudon 2016](https://doi.org/10.1098/rspa.2015.0534) | Bibliographic records; additional Athens-hosted 1959 PDF candidate timed out. | Neither original full-text gap is closed. The separate domain-classification source must remain separately attributed. |
| [Cerfon's mechanics notes](https://math.nyu.edu/~cerfon/mechanics.html) | Original address attempted, unavailable. | Do not replace this item with another author's notes and mark it reviewed. |
| [Volkov's kinetic-theory deck](https://volkov.eng.ua.edu/ME591_491_NEGD/2017-Spring-NEGD-01-ElemKineticTheory.pdf), [Monte Carlo deck](https://volkov.eng.ua.edu/ME591_491_NEGD/2017-Spring-NEGD-05-MonteCarloMethod.pdf), and [DSMC deck](https://volkov.eng.ua.edu/ME591_491_NEGD/2017-Spring-NEGD-06-DSMC.pdf) | These primary files independently accessible; all-six-deck reading remains the historical record. | Mathematical-font extraction and selected rendered-page checks are narrower than visually checking every equation. |

The original-text gaps remain Jönsson 1961, Cerfon, Parker, Valentini, Loudon 1959, and Loudon 2016. Supplemental kinetic-limit sources also retain their explicitly bounded reading ranges. This audit does not change those items to complete review.

## Mathematical checks worth preserving

The chapter correctly retains several assumptions that can otherwise disappear in an ambitious unification:

- Born–Oppenheimer separation requires a controlled electronic subspace and gap; it is not the assertion that all nuclei are classical. Classical propagation and neglect of nonadiabatic couplings are separate decisions.
- Liouville evolution preserves fine-grained phase-space volume and entropy under the stated regularity and integrability conditions. Coarse-graining and a collision closure introduce additional structure.
- A one-particle marginal does not close the first BBGKY equation. The explicit pair-correlation counterexample is directly relevant to learned closures.
- Boltzmann–Grad limits require their scaling, admissible data, and time interval. The cited short-time result does not establish arbitrary-time fluid regularity.
- Collision invariants yield exact balance equations; Newtonian stress and Fourier heat flux require separate constitutive/limit arguments.
- Finite energy does not automatically imply the entropy integrability required by the stated H-theorem argument.
- Equal density, mean velocity, and temperature need not imply equal stress. A trained model cannot remove this information deficit without additional state or assumptions.
- Positive covariance requires a positive averaging measure. Sharp spectral truncation need not satisfy that hypothesis.
- POD minimizes a specified snapshot projection error; it does not itself guarantee stable reduced dynamics. Hyperreduction with state-dependent weights requires derivative terms.
- A scalar Madelung lift is local away from nodes and does not represent arbitrary smooth vorticity through a globally single-valued scalar phase.
- A nonlinear or non-Hermitian wave equation is not automatically a deterministic unitary quantum algorithm. State preparation, conditioning, approximation error, and observable readout retain costs.

The existing linear-memory and discrete Schur-complement proofs provide a precise project connection to [Mori's projection method](https://doi.org/10.1143/PTP.33.423). The finite cochain framework should continue to be compared with [Arnold–Falk–Winther's finite element exterior calculus](https://doi.org/10.1017/S0962492906210018) at the level of actual commuting maps and estimates, rather than inferred continuum regularity from topology alone.

## Quantum algorithm versions

The cited [Liu et al. arXiv v4](https://arxiv.org/abs/2011.03185v4) is dated 7 July 2026 and incorporates a correction. Distinguish that revision date from the publisher correction's date in bibliographic prose. The existing counterexamples and repaired sufficient conditions address specified algebraic/norm steps; they must not be expanded into a claim that every quantum algorithm in those articles has been disproved. Conversely, numerical agreement and finite circuits do not verify a complete quantum complexity theorem.

## Additional spin-representation source

[Meng and Yang, Physical Review Research 6, 043130 (2024)](https://doi.org/10.1103/PhysRevResearch.6.043130) supplies a pertinent two-component spin representation. This pass read the model, stated limitations, and selected appendix equations; it did not independently verify all 15 pages. Selected equations and qualifications on journal pages 7, 8, and 10 were also inspected visually. The source treats nonlinear, non-Hermitian evolution, acknowledges global auxiliary-field difficulties, and leaves an effective quantum algorithm open.

The amendment derives an independent necessary periodic compatibility condition from its Eq. (15). The proof is ordinary mathematics, not a Lean-certified result. It also records the generic Moore–Penrose obligation: `A A⁺ S = S` is needed for an exact solve. A pseudoinverse alone supplies a least-squares solution; boundedness requires separate singular-value control. This is an audit criterion, not an unverified accusation that the source's specially constructed right-hand side always violates compatibility.

## Integration guidance

Include `chapters/quantum-spin-scope` after `chapters/quantum-fluid` and add `ns-spin` to the bibliography list in both manuscript entry points. The amendment is self-contained and introduces no implementation claim. Preserve its explicit global-lift hypotheses and the distinction between an obstruction to a coordinate representation and a statement about existence of the represented fluid solution.
