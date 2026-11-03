# Remaining mathematical obligations

No complete GRH proof has been established. A proof must discharge these, not assume them.

| ID | Obligation | Acceptance evidence | Status |
|---|---|---|---|
| O1 | Specify arithmetic Hilbert space and operator independently of unknown zeros | Complete domain, measure, action, closure, adjoint and convergence definitions | Open |
| O2 | Recover full completed L-function from that operator | Exact determinant/trace identity with conductor, gamma, ramified factors and multiplicities | Open for the intended positive spectral object; source identity refuted and separate elementary Abel rank-one Dirichlet identity proved |
| O3 | Preserve O2 under a self-adjoint realization | Explicit intertwining/determinant identity, not arbitrary Hermitian extraction | Open; unrestricted preservation refuted |
| O4 | Prove locally uniform convergence on a domain with overlap | Uniform trace-norm or normal-family estimates, all constants quantified | Open for intended positive spectral operators; the arithmetic Abel rank-one family has explicit trace-norm convergence in prose |
| O5 | Apply closure with nonzero holomorphic target | Rouché/Hurwitz argument after O1–O4 | Proved conditionally in prose |
| O6 | Extend from primitive Dirichlet to finite-order Hecke | Field/infinity type/conductor-specific construction and estimates | Open |
| O7 | Extend to general Artin with correct analytic scope | Holomorphy or meromorphic/pole analysis, valid induction and no hidden automorphy assumptions | Open |
| O8 | Formalize the actual proof | Pinned mathlib build, kernel-checked analytic definitions and complete dependency/axiom report | Open; finite obstructions and local analytic convergence lemmas checked |

A sequence of upper bounds β_n→1/2 on zero real parts could provide another route, but a fixed7/8 or11/12 region cannot. No mechanism producing such a sequence with valid constants has been established here. Numerical zeros up to a finite height cannot replace any of the universal obligations.

## Continuation findings

- Simply improving compact bounds on the existing finite Euler-product family cannot work: it is zero-free on Re>0 and cannot approximate a target zero locally uniformly. This proposed repair is rejected, not just unfinished.
- Nonprincipal Dirichlet partial sums and pole-subtracted zeta sums give convergent arithmetic approximants on Re>0, independently of unknown zeros. They do not have a proved critical-line zero divisor or self-adjoint realization.
- The separate mathlib layer now proves finite complex Euler-factor nonvanishing and a genuine boundary-uniform-limit nonvanishing theorem with explicit local assumptions. Root isolation and the entire GRH closure remain prose/unresolved as documented.
- The exponent report identifies a missing short-row mean square and explicitly conditional parameter extension; neither has been established as a new unconditional zero-free theorem.

- Holomorphic pointwise-Hermitian matrix rigidity is now kernel-checked. A nonconstant complex-holomorphic transfer cannot become a complex-holomorphic Hermitian family by ordinary pointwise extraction. A fixed H_N independent of spectral s remains permitted. Hermitian dilation loses phases/spectral imaginary parameter for the prime diagonal; real-axis Hermitian pencils require a separate zero-location theorem.

- A positive generalized-pencil criterion is now proved and formalized: fixed Hermitian A and positive-definite B yield only real z-zeros, hence centered s-zeros on the critical line. This supplies a valid sufficient mechanism for O3 but does not discharge the arithmetic construction/matching in O1–O2. A strict-imaginary-form nonvanishing criterion and an exact indefinite off-line witness are also checked. Next test a specified arithmetic candidate for a positive metric or the necessary Herglotz logarithmic-derivative sign, with normalization fixed independently of unknown zeros.

- A concrete arithmetic candidate was tested: S5(s,chi_mod3)=1−2^(−s)+4^(−s)−5^(−s) has exactly one simple zero within radius1e−4 of0.337261+11.027504i. Exact rational logarithm/exponential enclosures plus Rouche give the result; Lean checks only disk geometry and final margin. This refutes a direct nonvanishing-factor×positive-pencil identity for this particular finite approximant on that disk. It is not a zero of the full L-function or a GRH counterexample. Any replacement construction must change the finite-level approximants or establish a different arithmetic operator, rather than assuming partial sums inherit positive spectral structure.

- A different zeta-only family is now specified: scaled Jensen polynomials converge to Xi with explicit compact error T^4 F''(T^2)/(2d). Their coefficient-defined Newton-sum metric symmetrizes the companion. Strict metric positivity yields an exact self-adjoint block determinant; semidefinite metrics require separate treatment. Proving all-degree arithmetic PSD is the classical RH-equivalent Jensen condition, not a discharged obligation. Ordinary Fourier-kernel moment positivity cannot establish it: a strictly positive smooth Gaussian-mixture density gives a negative degree-two metric determinant. This counterexample concerns generic kernel reasoning, not the xi function. Dirichlet/Hecke/Artin interfaces remain separate.

- The September correction's local analytic extension is now proved from its displayed scalar factors: Re x>=3/4 with the original lower w and z boundaries, including all row valuations and holomorphy of the finite compensated tuple formula. This covers the local Euler part of the tiny exponent perturbation. Its earlier Gauss/reciprocity identification, quantitative compensated errors, common contour estimates and mean-square inputs remain uncertified. No new numerical zero-free half-plane is claimed.
- The principal factorization H_eta=A L^S(6s-3,theta), theta=alpha^(-6)eta^6, identifies an additional infinite-order angular character. A is holomorphic and nonzero on Re>1/2. Under the explicitly listed classical Hecke completion data, the unchanged H_eta has a zero with real part at least7/12; finite prime deletion cannot remove it. Hence its common-signal nonvanishing assumption cannot extend below7/12. This is a limitation of this correction and criterion, not a limitation on all approaches or a GRH counterexample.

- The compensated principal normalizer and principal-residue comparison have now been extended to the perturbed geometry from the displayed factors and the explicitly retained high/Mellin/reciprocal contracts. The uniform local saving37/50 gives mu=(7/10)ell_min; fixed-ray prime counting supplies eventual nonzero normalization, without a moving-conductor estimate or exceptional-zero exclusion. This closes the principal portion of that perturbation interface, not the general energy, frozen-capacity row count or remaining nonprincipal contour obligations.
- A distinct pointwise limitation occurs at3/5: for eta=1 and inert prime ideals, the real endpoint gives r=d and B_p=-1/Q exactly. The generic local asymptotic also rejects a negative-power error below that boundary. Such degree-two prime ideals have zero density in the prime-ideal average; no averaged obstruction is asserted. The separate unchanged-correction7/12 obstruction from the earlier run is retained.

- The frozen-kappa=3/4 counting interface is now reconstructed conditionally from the source moments, saturated witnesses and separate uncertified beta_*<=7/8 bound. The baseline plain capacity is exact, so no Delta/4 surcharge remains. Fixed-mesh quantifiers, masks, support, nonprincipal family, zero-capacity and height-ceiling requirements are explicit. This does not certify the moments or the earlier bound; floor rows remain separate. The next concrete task is the perturbed low reflected-energy application.

- The perturbed low application is now verified conditionally from the general reflected-energy/Gram estimates and exact arithmetic low/sector identities. The actual support mapping retains nonnegative dual ideal centers and negative unit-length offsets; a kernel-checked bound controls6epsilon_Z+2|theta|+tau. Tuple saving absorbs the possible row-norm loss for0<=t<=1/30. This verifies that application, not the deep source estimates; the nonprincipal shared contours and independent arithmetic certification remain open.

- The nonprincipal central-contour application now extends conditionally below7/8 using D1 only. Full-correction movement precedes dynamic division and pointwise partitions; the single conductor and cumulative height allowances are retained. The original-bin estimate keeps its additive deformation error until the late tail choice. Exact high identity, D1 local derivation, buffered L-bounds, trace contracts and arithmetic row moments remain inputs. Outer rows/final assembly are not certified. Next independently audit the finite prime-power Gauss/correlation arithmetic instead of repeating interface bookkeeping.

- A finite arithmetic input is now proved for actual arbitrary finite fields and complex multiplicative/additive characters: zero-preserving local kernels and finite Gauss identities. Prime-power lifting and CRT normalization/phase orientation have independent prose checks. The genuine F7 kernel36>7 off the coprime-residual locus proves the artificial-extension distinction is necessary; it is not a source counterexample. Full quotient-ring pairing, fixed reciprocity identification and quantitative Gram/reflection/moment estimates remain unverified, as do the outer-row/final assembly and spectral bridge.

- The quantitative Gram periodic-Poisson estimate now has a complete general annular proof in prose and a conditional source summation with all period volumes, Mobius masks, subunit scales and sixth-power exceptional counts tracked. Nine actual finite Fourier/dyadic Lean components pass. No extra period-square defect was found. The exact arithmetic representation, source trace pairing and fixed reciprocity/ray period remain explicit unverified inputs. Next verify that fixed modulus independently; the reflected identity, moments, outer rows, final common-signal assembly and spectral bridge are still open. A generic nonannular small-scale claim is false, but the source uses the required annuli.

- The exact fixed reciprocity/ray period feeding Gram is now established in prose using classical cubic reciprocity and abelian class field theory. A common defining modulus is lcm((12),m_presentations,(6)^6 product_(p in S)p^25), with all full presentations and zero masks. The norms31/43 lambda-symbol witness refutes replacing that whole modulus by12; the source already allows the needed higher powers. Thirteen actual Eisenstein quotient-ring/period Lean components do not formalize the Gaussian/CFT number-field arguments. The initial row representation, exact reflected-energy identity, moments, outer-row/final assembly and spectral determinant/zero-location bridge remain open.

- The arithmetic extraction from canonical completed reflection to the explicit quadratic-cubic norm is now independently checked conditional on that theta/cusp formula and the original block hypotheses. Exact1/3 normalization, shared cubes, row-mark phases, all zeros and dual S-primes are retained. A norms7/13 witness shows why moving j4 phases cannot simply be discarded; the source already freezes them. The common homogeneous profile is proved in prose from the defined gamma/Mellin kernel; nine actual character/phase/Bochner components pass. The full theta/cusp identification, hybrid sieve, outer rows/final closure and spectral bridge remain unresolved. Next verify the complete two-mask hybrid quadratic-cubic mean square.

## Projective-resolution arithmetic comparison (2026-11-03)

The four requested source reviews and corrected algebraic resolution/determinant proofs are complete in prose; sixteen actual Lean module/matrix components are checked. These do not close O1–O4 or the intended scope extensions. The new focused editions state these next construction obligations:

- PR-A: Specify the actual arithmetic realization of the selected surface/order derived category, with Galois/Frobenius, conductor, ramification and archimedean data. Prove its exactness/perfectness or justified analytic replacement, including conductor descent and Tor at singular fibers.
- PR-B: Prove its chain endomorphism commutes with the differential and its correctly normalized determinant equals the particular completed L-function, with multiplicities. Cartan Hilbert series and determinant lines are not already that scalar function.
- PR-C: Prove a positive Hermitian/polarized realization for that SAME determinant, or a determinant-preserving positive-pencil model of the existing convergent arithmetic approximants. Alternating duality and local Artin weight zero do not suffice; actual matrix counterexamples are given.
- PR-D: Prove compact-uniform or trace-norm/regularized determinant convergence and nonzero anchor, then exhaust the strip. Positive-length finite Cartan factors are zero-free on Re>0 and cannot locally uniformly approximate the required zeros under nonvanishing normalizations.
- PR-E: Extend actual Lean verification from dual numbers and matrix interfaces to general path projectives, categorical resolutions, Ext products and the eventual arithmetic comparison. The full surface/derived/Weil theory and original upstream graph are not claimed formalized.

A concrete intermediate acceptance target is the elliptic curve y²=x³−x overF5 with eight points and numerator1+2u+5u², using an actual arithmetic realization rather than a fitted polynomial. This is a finite-field benchmark, not evidence of a number-field GRH proof. Earlier hybrid-energy and short-row/contour frontiers remain preserved for alternative work.

## Hodge and boundary comparison update2026-11-03

The plain finite alternating determinant of Δ=(d+d*)² cancels every nonzero spectral factor; positivity from a resolution alone cannot preserve the missing arithmetic spectrum. Ordinary factors vary with metric, and a holomorphic d(s) need not give a holomorphic Δ(s). This is a failed repair attempt, not a refutation of independent arithmetic chain endomorphisms or degree-weighted torsion.

An explicit bounded ℓ² relative boundary model now realizes det(I−M), and hence the weighted Cartan ratio. This closes that algebraic/relative realization task in prose, not PR-B/PR-C. Its natural truncated shifts have an escaping terminal block: finite determinants stay1, the scalar M=1/2 limiting determinant is1/2, and trace-norm distance stays1 despite strong convergence. A changed boundary correction or different actual arithmetic approximants must supply the required determinant comparison and topology. The existing positive-length zero-free obstruction remains. Do not claim a universal infinite Hodge no-go: individual trace-class heat or a specified relative regularization matters.

## Arithmetic Abel family2026-11-03

An explicit elementary nonprincipal Dirichlet family on a fixed ℓ² space now has Fredholm determinant L(s,χ) for Re(s)>0, and explicit operators with determinants exactly the EXISTING raw partial sums converge locally uniformly in trace norm. Primitive gamma/conductor completion is included with the corrected functional normalization. This closes the analytic arithmetic encoding/convergence task for THIS rank-one family in prose; it does not identify a fixed self-adjoint height operator, a surface-order arithmetic realization or any general Hecke/Dedekind/Artin extension.

The direct common-positive-metric shortcut for this family is decisively rejected: symmetric fixed-range rank-one maps need proportional coefficient functionals, while two distinct critical-height functionals are not proportional. A different or enlarged positive spectral realization with a determinant-preserving comparison remains open. The mere existence of this elementary rank-one determinant is not a zero-location theorem. Ten formal components do not amount to formal verification of the full ℓ², Fredholm and asymptotic arguments.


## Dessin-specific arithmetic and categorical obligations (2026-11-03)

- **Arithmetic descent:** specify a rational/number-field Belyi model and compatible Galois/Frobenius actions. Same complex theta dessin gives different E1/E2 local factors at7; bare quiver/order/Fock invariants cannot distinguish them.
- **Determinant comparison:** construct an independent arithmetic endomorphism/correspondence on an actual determinant-admissible order/derived or analytic object and prove local/global determinant identities including conductors/gamma factors. The Abel family now lies in an actual dessin compact ideal, but no A-linearity or Frobenius functoriality is established.
- **Positive realization and limit:** independently prove positivity/self-adjointness for that SAME completed function, on specified domains with required compact/trace-norm or regularization control. The local Schur Cauchy PSD kernel and positive number operator do not equal the Weil form; recent NCG ground-state/core/arithmetic-limit hypotheses remain unverified here.
- **Derived/Schur compatibility:** nonempty Schur functors preserve monomial arrow relations on polynomial finite representations, but not termwise exactness or the fixed R central action on arbitrary lattices. Genuine mixed-degree replacements and an exact/dg functor require proof.
- **Geometric and AR scope:** general completed derived/geodesic Hom/Ext equivalence is not proved. HLS meshes are intrinsic to the specified quotient-annihilator subcategory, which is not ambient extension closed; no general AR transfer follows. Domestic CB/KG=2 is relative to Λ/J², not all Λ modules/lattices.
- **Full formalization:** actual nodal all-degree resolution components and matrix identities are Lean verified. General dessins, AR factorization, Schur/LR, C* exactness/K theory, Fredholm/descent and every complete GRH scope remain outside the kernel-checked layer.


## After the graph-pullback extension

The original-quiver CK1 collapse is now complemented by a proved graph presentation on arrow states plus vacuum sinks and a literal nodal AF pullback. This closes that operator-model identification, not arithmetic compatibility. The separate diagonal-fiber circle model has a proven polynomial embedding/generation with adjoints; extension to the entire formal order is impossible for this embedding, not a pending estimate. A valid continuous/topological order functor must state a smaller analytic domain or different realization.

The unrestricted completion/string and Perf/Fukaya identifications are false under the current hypotheses. The polynomial quotient annulus remains valid intrinsically; derived inflation fails. A precise singular/completed/geometric functor, compatible with the displayed Ext and center actions, remains necessary. No statement here supplies descent/Frobenius, global L determinants, positive comparison or GRH. Ten new generic matrix/pullback declarations do not formalize C* topology or the full category constructions.


## After the constructive arithmetic theta benchmark

Uniform Jacobi sums now compute the local coefficients and a split-prime rational cellular realization, with actual inherited positive Gram form and exact local-zeta cancellation. This supplies the recorded elementary good-prime benchmark; it is not a canonical integral/Tate/order comparison. Same-real2deck Frobenius at inert primes is IMPOSSIBLE by the proved determinant inequality, so that route requires a different coefficient or carrier category. The complex local repair needs independently proved extension-power compatibility if made a family.

Multiplicity-one arithmetic order determinant remains open: identity-tensor projective lifts have powers6/18, residue simples are nonperfect and not fullC6stable, and semilinear lifts differ from those linear tests. A determinant-line root is not authorized by the scalar factorization alone. Ramification, conductor/gamma normalization, Dirichlet versus global elliptic scope and a globally determinant-preserving positive spectral limit remain unresolved. Local curve purity does not prove GRH.


## After arbitrary-projective multiplicity and the branch functor (2026-11-03)

The ordinary underlying-R determinant route is now closed negatively for ALL finite projective Λ-linear chain actions on the theta order, not just identity-tensor insertions: specialization is a sixth power, and generically it is a cube. Bounded perfect cancellations do not recover either the single local quadratic or the full local curve zeta. This is not an obstruction to alternative determinant theories, semilinear maps or infinite analytic models.

There IS a true multiplicity-one repair: Φ+=−tensor^L_Λ W+ on PerfΛ→PerfR, with the actual branch column W+=R³. A basic projective maps to R. Its externally inserted Md gives P once, while the regular input still givesP³. W+ itself has infinite left projective dimension, consistent with the construction being derived on right perfect complexes. This closes the categorical multiplicity repair for a chosen branch, NOT the independent Frobenius action or required full symmetry.

The next unresolved construction must address full descent/equivariance. Chosen-branch determinant alpha-invariance is refuted by an explicit corner unit; a strict unramified central-fixed rankone-per-vertex branch sigma-lift is impossible. Ramification plus a NEW lattice gives a valid different rotation model; it does not automatically linearize the old base-changed lattice or supply arithmetic descent. Do not infer a universal determinant-level rotation no-go. Seek a specified equivariant family/twisted determinant/semilinear correspondence with an independently derived prime action and determinant comparison. Bad primes, integral/Tate/global normalization and the positive spectral limit remain open. All GRH scopes are unresolved.


## After tame descent and the full-deck coefficient theorem (2026-11-03)

The recorded balanced-column repair is now computed in full. Its invariants restore the old cut; S/R is faithfully flat but the semilinear group action fails effective integral descent at the ramified fixed point. Carrier End invariants genuinely recover the hereditary order and its projective rotation. The whole determinant line descends, while the natural comparison with det(invariants) is multiplication byu. These surviving constructions do not descend the earlier cellularH1, construct a prime action or recover the local factor.

A larger route is CLOSED NEGATIVELY: ANY finite R-free central coefficient kernel with invertible R-linear rotation and branch-swap intertwiners has vertexrank6m. For EVERY induced Λ-linear projective f its determinant reduces to H_top^(6m); all bounded perfect ratios retain this divisor obstruction, excluding localP and fullcurveZ. No left projectivity, flatness or integral branch splitting is assumed. Full cut/branch orbit equals the hereditary normalization and returns the original ordinary determinant exactly. This is not a no-go for all determinant lines, non-linearities or infinite analytic models.

The next work should rotate to the original short-row hybrid mean-square input, rather than repeat localcounts or the now-closed strict kernel search. Preserve original shared-cube/coprimality masks and distinguish the genuine finite kernel from artificial extensions. Any root-stack/twisted/infinite arithmetic alternative must supply its own determinant and center comparison, including coefficient extension k/Q (restriction squares rational factors). The independent arithmetic self-adjoint/global zero-location bridge, bad-prime/Tate comparisons and all GRH scopes remain open.


## Book, physics, learned interfaces and the surviving short-row task (2026-11-03)

Both complete source manuscripts are preserved and the critical book/on-page companion is implemented. This does not make the originals correct or the entire book Lean formal. General AR/derived/determinant interfaces, infinite operator/QFT domains, empirical hardware claims, and the global arithmetic positivity bridge remain subject to their exact hypotheses. Refuted source assertions cannot be made valid by formalization. See book/VERIFICATION.md for per-topic coverage and pending work.

Three PennyLane renormalization models, a larger genus-four nine-qubit QCNN, a Strawberry Fields Gaussian model and the ToricGT/PennyLane finite Harper surrogate have actual saved CPU training evidence. Low training loss does not imply exact physical RG, generalization, quantum advantage, arithmetic identification or GRH. The Harper benchmark has a known exact spectrum; exact rational principal-minor certificates, not the learner, establish its lower bounds. NVIDIA GPU adapters and Sage execution remain unpassed on this machine.

The analytic frontier now controls the fixed-radial-profile high-gcd part G>=D^(5/8) at H=D^(3/4), but not small gcd or moving-profile/supremum uniformity. Arbitrary-beta or arbitrary-column-weight strengthenings have coherent-row counterexamples; the specific arithmetic source family is not refuted. Next research must control that actual small-gcd kernel or construct a genuinely different independently positive arithmetic determinant family.


## Master-loop and persistence extension boundary

The governing plan/queue/hourly implementation loop is installed; three concrete checkpoints are complete. The new tensor/state architecture inspector, full persistence visualization tools, further chapterwise formalization, comprehensive matched training evaluations and the arithmetic GRH bridge remain pending. Four canonical tools replace repeated generic book panels. The new exact persistence/surface-coefficient construction is prose proved and independently reviewed, not fully Lean formal. Do not confuse a completed implementation checkpoint or scheduled heartbeat with completion of GRH.

The subsequent architecture-data checkpoint supplies 22 checked numerical
cases (836 DAG nodes) from existing trained parameters and fixed-weight
references. It closes the data-export task only. The step-through inspector,
upstream full-model training reproduction, larger matched evaluations and all
remaining mathematical/formal obligations above remain open. No new arithmetic
cancellation or determinant positivity is inferred from the trace exports.

The covering extension now supplies an actual locally bounded integer cover
of theta finite quotients and explicit non-lifting modules, including genus
4 and 9 examples. Thus the general module and bounded-derived push-down is
not dense; full AR coverage cannot be assumed. The parent infinite algebra
is not locally bounded, and a length-cutoff quotient need not be quadratic
gentle. GLS identification, equivariant linearizations for fixed objects,
completion/Fukaya/derived interfaces and determinant block compatibility all
require their own proofs. Three matrix lemmas do not formalize these entire
categories. The low-gcd estimate and positive arithmetic bridge remain open.


The P1 inspector is now implemented for the 22 saved cases and the computed
finite clock. Numerical masks, coordinates, routing, states and certificate
records have browser/reference checks; this closes the core inspector task,
not the optional upstream heads, larger trained campaigns, physical/GPU runs,
whole-book Lean coverage or arithmetic research gate. The next implementation
task is the exact persistence tool, followed by its genuine module formalization.
