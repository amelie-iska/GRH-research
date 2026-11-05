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

P2 persistence tools are implemented and independently reviewed. Exact finite
staircase/CW/fiber/rank data and a fixed-channel quantum flag bifiltration
now have a single canonical laboratory. Universal staircase exactness and
channel contractivity have full elementary prose proofs; finite diagnostics
are not their full Lean formalization. P6 must connect actual multivariate
polynomial/module maps, prove the relevant exactness and inspect theorem
axioms. No new Lean result was claimed here. Sage remains supplied unexecuted;
quantum distance estimates remain non-interval-certified. The original-family
low-gcd estimate and independently positive arithmetic determinant remain open.

P6 persistence interface now closes the complete underlying ungraded worked
sequence for k[x,y]/(x²,xy,y²), including augmentation, projective terms and
both Hom boundaries for the actual residue action. Its general regular-pair
premise is discharged for the polynomial variables. Remaining obligations:
general staircase exactness in Lean; bigradings/minimality, Ext/Tor objects
and dimensions, CW/Schur equivariance, and the actual nodal E tensor cone.
The module quotient basis/Hilbert series and categorical ProjectiveResolution
wrapper are not formalized by these19 declarations. Entire-book coverage and
the original low-gcd/independent arithmetic positivity bridge remain open.

The DG foundations P4 slice now has a genuine infinite-node model, correct
completion/clock proofs and distinct spherical/elliptic endpoint Ext tables.
Its20 Lean components check algebra and ambient sequence identities, not all
graded/category/topological or derived constructions. Full q-substitution,
HH/GNS/A-infinity objects and general DG gluing remain separate. P4 overall
is still in progress; all source topics are not yet fully rewritten or
formalized. The low-gcd original arithmetic kernel and positive determinant
bridge remain unresolved; rotate an arithmetic run next rather than imply
that this source correction proves GRH.

## Arithmetic rotation: signed low-gcd structure remains essential

The absolute pair-square target B1(H,D)<<H²D^epsilon is now refuted for the
original sextic kernels at H=D^(3/4): actual prime columns force
B1>>D^(11/4)/(log D)². This was a proposed sufficient route, not a claim of
the source manuscripts. Four finite complex Gram inequalities are checked
in Lean. It supplies no lower bound on the original signed μνW quadratic
form and does not close its estimate, the determinant bridge or any GRH
scope. Do not repeat this disproved absolute route as progress. A next
arithmetic task is the exact truncated Möbius convolution with every
squarefree/coprimality/row-zero factor retained, followed by a genuine
coefficient-sensitive type-I/type-II estimate. The broad P4 linear-relations
construction can proceed on the next implementation rotation.

## Actual-RG and quantum-token implementation boundary

The physical implementation now carries full actions/constants/scale maps,
with genuine clean-dessin incidence models, quantum thermal effective
Hamiltonians and matched trained approximations. Nine finite scalarRG
identities are kernel checked; the whole quantum/log/operator/channel,
optimization, continuousGFN and categorical program is not. Original
auxiliary compression/covariance data remain preserved and correctly scoped.
No trained residual or finite spectrum provides an arithmetic positive
realization or proves GRH. Both original signed-low-gcd and determinant
bridges remain open.

QuantumTokenGT executes measured-feature hybrid attention, defined concept
MI, finite latent search/analogy/persistence and a continuous-state GFN.
General semantic emergence, population MI guarantees, exact GFN sampling,
coherent quantum attention, material discovery and quantum advantage are
not established. Ideal independent-X memory recovery has an actual tested
physical-prediction layer; realistic gates/syndromes, phase errors and
fault-tolerance need another code/noise/decoder treatment. The actual
one-face genus2CSS code hasdistance1, not useful topological protection.

A constructive finitegentle m5cut hasdimension25/gldim4 but killsu and is
not derived fullyfaithful in the completedorder. HMS comparisons require the
actual graded/stopped surface and appropriate category; the learned carriers
are not faithful order modules. Future categorical/materials extensions must
supply their stated Hamiltonian/data/functor before claiming applications.
Sage source is supplied unexecuted; no GPU/hardware or new dependency run.
Continue P4source construction and the coefficient-sensitive P7 arithmetic
rotation with the new implementation preserved.


## Linear relations: established slice and remaining interface

The actual finite A_m branch category, functorial Fitting decomposition,
Jordan filtration/Hom formula, nonsplit string extension and cyclic transport
determinant now have reviewed prose proofs. Eleven general relation/Fitting
statements are Lean checked. Whole categories, formal completion topology,
Jordan/Hom and Cantor/determinant arguments are not fully packaged in Lean.
The source's graph and rigidity assertions cannot be formalized as stated.
A monodromy band with arbitrary eigenvalue supplies no zero-location theorem;
finite torsion is not a nonzero completed-order lattice. All PR-B/PR-C,
positive arithmetic comparison and signed low-gcd obligations remain open.
Next arithmetic task retains the exact truncated Möbius identity before
estimating original masks, conductors and coefficient-sensitive type-I/II terms.


## Signed Vaughan split frontier

The exact good-ideal convolution/regrouping is established in prose, with8
actual Nat Dirichlet formal components. The proposed all-cutoff separate-piece
short-row bound is false at U1/principalnu; original signed MS3/4 and moving
cutoffs remain open. A U7/norm637 negative-coefficient control prevents
recycling the same positivity proof. The generic one-Cauchy envelope loses
powers even if an unproved optimistic slice estimate were supplied.

Next analytic construction: for the actual type-I squarefree inner sum,
derive its Euler ratio L(s,theta_u)/L(2s,theta_u²) with every removed local
factor from S,d and original row zeros. Distinguish primitive conductor from
full zero extension, including sixth-power rows. Establish exactly which
Mellin contour/residue and moving-d/profile uniformities follow without GRH
before summing the actual beta_U. No square-root Mobius cancellation, Artin
holomorphy or desired spectral positivity may be assumed.


## Frontier update: actual branch extension and certified path vocabulary

The specific N5(J1(0)) self-extension now has actual ambient-algebra maps,
exactness and no section verified in Lean over any coefficient field; the
polynomial generated algebra is proved infinite dimensional. The path-normal-
form quotient isomorphism, general branch/category equivalence, Yoneda Ext
packaging and universal almost-split factorization remain separate obligations.
This closes a selected formalization gap, not the arithmetic positive bridge.

ConvexTok supplies certified small finite vocabulary optimization. No trained
TokenGT checkpoint has been changed to consume compressed path tokens, and
no categorical/geometric equivalence or arithmetic positivity follows from
shorter word encodings. The original-family signed low-gcd mean square,
full-mask Mellin/contour uniformity and all GRH scope obligations are unchanged.


## Type-I scalar contour frontier (2026-11-03)

The selected primitive-factor restoration and scalar Mellin estimate are now
proved in prose using classical CFT/Hecke theory, with explicit good/wild
conductor and M4-profile dependence. Quadratic conductor drops and sixth-power
row zeros are restored before using primitive L-functions. Seven finite Euler
identities are Lean checked. Do not repeat this scalar derivation as a new
solution or report those finite identities as full Hecke formalization.

What remains is a useful ORIGINAL-family average before pointwise convexity:
the primitive numerators, independently squared primitive denominators,
d-dependent deletion factors, actual beta_U, principal/residual classes and
quantitative height/profile uniformities must stay inside the weighted moment.
The derived scalar envelope loses a power and supplies no short-row mean
square. Original scale suprema also require cutoff compatibility and restoration
of2a_U on small scales, plus signed covariance with typeII. No GRH scope or
independent positive arithmetic determinant comparison has been closed.


### Normal-path formalization frontier

Unbounded normal-image membership, independence, equality of the normal
span with the actual generated algebra, and bijective A-valued finite
expansion are now Lean checked over every field. Next: construct a separate
mixed-zero path quotient/normal concatenation algebra and package its
universal multiplicative comparison. The current linear equivalence alone
is not this separately defined algebra-map interface. Then construct the actual module-category sequence before
any assertion of universal almost-split factorization. Polynomial finite
sums, formal completions and lattices must remain distinct. The positive
arithmetic determinant/zero-location bridge and original signed low-gcd
mean square are unchanged and open.

## Learned-generative and GPU extension boundaries (2026-11-04)

The specific random-feature/readout RBF limit has a complete prose proof;
it is not the limit of the trained four-qubit feature-learning networks.
A learned Hermitian finite matrix or positive circuit supplies no independent
arithmetic determinant comparison or control of infinite domains. The
original-family signed low-gcd moment and every intended GRH scope remain
open. Next arithmetic rotation is the original weighted Mellin moment before
pointwise convexity, keeping all primitive numerator/denominator factors,
row zeros, beta_U, conductors and II-I/short-term covariance.

New homological, probabilistic and Frobenius constructions are prose/exact
checks, not newly packaged Lean theorems. General path-quotient/category/AR
interfaces, coefficient-field/valuation/HMS comparisons, continuum/CFT/string
sewing, anabelian field hypotheses and chemical/biochemical applications
remain open. The GPU simulations are classically executed finite circuits;
matched three-seed runs show no entanglement advantage. No physical quantum
processor, universal denoiser, fabricated ASIC, PPA or quantum speedup is
inferred. The23-qubit case lacks an independent large-state reference.

## Complementary datasets: downstream limits (2026-11-04)

The two additional corpora exceed10K default static rows each. Finite
component/threshold checks are not universal leakage or overfitting guarantees.
Existing-source anchors are train only; molecular anchors also face all default
heldouts under the declared chemical/geometric thresholds. Full historical
model-corpus overlap, protein sequence/fold splitting and native synthetic-label
admission remain separate future evaluation decisions. Neither active model was
modified or trained. Mora's observed-only scalar/array gate remains in force.

MMFF94 is empirical, and source-contact orbital models are dimensionless and
uncalibrated. No ab-initio density, CISS, affinity, efficacy, new physical phase
or measured training gain follows. The tested normal Givens compiler does not
cover BdG pairing. The dataset constructions have no new Lean declarations;
360 existing reports retain their previous scope. GRH's arithmetic bridge and
all original-family low-gcd uniformities remain open.

## Learned certificates and gluing (2026-11-04)

The finite holomorphic readout theorem proves arbitrary-accuracy compact
approximation under independently certified constants, oracle and arithmetic
error. The historical floating q3/4/5 training experiment does not implement a validated
interval oracle; the separately preserved final-v5 finite certificate now does
so for three specified conductors and a fixed compact/tolerance. The Szegő readout limit has an explicit source-condition
rate, with vanishing Gram eigenvalues; no general quantum-network or
all-conductor rate follows. Real-zero restricted approximation still needs
the independent arithmetic positivity/determinant bridge; the 7/16 Rouché
obstruction is retained. Game moment PSD and learned finite Bell violations
do not discharge O1–O8. Surface homotopy cell gluing does not automatically
supply an exact, Hom-controlled or determinant-preserving categorical functor.
New analytic/topological/game full Lean implementations remain open.


## Validated-oracle and AFM frontier (2026-11-04, remote)

Closed for the narrow supplied finite configuration: true circle-node/sample
inclusion, analytic tails, complex arithmetic, coefficient midpoint rounding
and a strict compact-uniform polynomial error below 5e-15 for q3/4/5. The
closed-form GD iterate is certified, not an executed optimizer trace. The
fixed n/time/precision interface does not implement arbitrary requested
accuracy. The original floating learners and observed errors retain their
historical semantics. No new analytic Lean declaration was added.

The previously conditional AFM numerator input is now proved in prose for
the fixed finite-order twist and literal Eisenstein element family, using
the named classical inputs. A separately reviewed fixed-unitary extension
retains dependence on the fixed twist and infinity type. The resulting exact
full-mask residue-subtracted remainder costs D^(2delta) U^(2-4delta).
For U=D^a, fixed a>0, delta->0 leaves the 2a exponent loss. Thus the complete
d-weighted moment before absolute summation, principal residue, short Vaughan
term and signed II-I covariance remain open; no original signed MS3/4 theorem
or positive arithmetic determinant bridge follows. Do not repeat the completed
unweighted numerator AFM proof as a solution to the remaining weighted gap.

Next: exploit cancellation in the actual d-weighted numerator sum, retaining
beta_U, nu(d), chi_d(u), primitive drops, the independently squared denominator
and deleted factors, or prove sufficient signed covariance. In parallel,
package actual analytic objects in the pinned Lean layer and integrate the
reviewed technical-note fragments into the book once the preserved remote
build prerequisites are available. Standalone paired PDFs do not count as
full book/HTML synchronization or whole-book formalization.


## Weighted-cutoff and integrated edition milestone (5 November 2026)

The reviewed original-family masked type-I remainder now has the U-independent
bound ||E||² <= C_(nu,S,epsilon) ||W||_infinity² (HD)^epsilon
[H + D H^(1/3) + (HD)^(2/3)], for U²<=D, fixed finite-order nu/S and
one common smooth profile. Recombination retains every original zero mask,
primitive drop, principal residue and literal element multiplicity. The proof
uses the pinned classical BGL powered large sieve and has independent
adversarial prose/TeX review; it is not a new Lean proof. At H=D^(3/4),
a relative D^(1/2) loss remains. It does not prove the original signed short-row
estimate, the needed II-I covariance or the arithmetic positive-determinant bridge.

The exact cutoff series has an explicit U^(-kappa+epsilon) convergence rate
on Re(s)>=1+kappa. Locally uniform convergence of the actual series on
Re(s)>1/2 would force zero-freeness for a fixed nonprincipal character;
that stronger convergence is an unproved hypothesis, not a GRH proof.
See research/weighted-cutoff-moment.md and papers/weighted-cutoff-*.tex /
uniform-cutoff-moment-*.tex. Exact recombination diagnostics preserve raw
sextic zeros and reject the naive unconstrained Mobius square.

Accepted staged artifacts are now promoted on Linux: book233pages/40chapters,
focused articles49/129pages, technical notes8/20pages; native HTML contains
6216MathML expressions and13unique laboratories. All5356oldMathML subtrees,
384oldtables, both source volumes and all13oldiframes are unchanged. Existing
vector assets were source-hash checked; the two article-only grids preserve
all nodes, arrows, hooks, signs and labels. The bounded remote builder uses
installed pdflatex/Poppler, Pandoc3.10 and librsvg/cairo, without installing tools.
Fresh reproduction and exact-source transformation audits pass.

Firefox layout checks at320/390/768/1440 preserve full18px equations in
focusable horizontal scroll containers, with no page overflow. This corrects
an inherited MathML overflow issue. Stable dark-mode contrast is14.54:1;
representative PDF/grid and desktop/mobile/night renders were inspected.
Three malformed old TeX4ht munder nodes remain explicitly inherited; the860new
expressions have zero such defects. Article logs retain existing atop/over
and seven underfull-box warnings per edition, with no overfull boxes or
unresolved references. No new Lean declarations; prior360reports retain
historical scopes and were not rerun with an unpinned Linux toolchain.

Evidence: outputs/checks/2026-11-05-weighted-moment/promotion/promotion.json;
outputs/checks/2026-11-04-weighted-moment/{review,native-browser-v9};
outputs/article-integration-20261104/audit-v1/source-preservation-audit.json;
planning/book-integration-20261104/MOBILE_QA.md and
planning/article-integration-20261104/HANDOFF.md. Earlier failed builds and
replaced aliases are preserved. Both completion gates remain false.


## Current weighted arithmetic frontier (5 November 2026)

The U-independent envelope closes the weighted-before-Minkowski subtask in
prose, not the original low-gcd short-row target. Keep the exact squarefree
A_U coefficient and column-indexed primitive characters with union-support
zeros. Combining the envelope with the earlier AFM bound gives the recorded
minimum; at H=D^(3/4) a positive exponent loss remains. Principal residue
control sufficient for this envelope is weaker than the final assembly needs.

Next concrete arithmetic task: signed actual-coefficient covariance on balanced
nonprincipal rows a1*a2², with both factors retained inside the column Gram
form. planning/weighted-moment-20261105/frontier isolates this target and the
failure of principal centering/shared-prime masks alone to improve it. Its
finite controls are diagnostics, not a new infinite energy bound. Neighboring
near-saturating dyadic blocks and the D^(7/6) mixed contribution must also be
handled; one block's success alone would not establish the global H-sized target.
The independent determinant/zero-location bridge, full intended L-function
scopes and actual analytic/category Lean formalization remain unresolved.

Publication authority now includes existing Mac gh for publishing only;
remote401 does not revoke this explicit user permission. No automatic login
or credential transfer is allowed. The Mac workspace/local8765 preview and
older research HEAD/index remain protected. New public release work uses
a narrow isolated remote worktree, never blanket staging this old dirty copy.

### Independent signed-frontier continuation (5 November 2026)

The next exact reduction is accepted at derivationSHA7dc97b2e61a8d3bc286356bf9eae28fb986d29978582a97f9bfbfd7e329ab9c1.
Principal subtraction vanishes on the balanced a1*a2² nonprincipal block.
The raw Gram retains symmetric-difference oscillation and the union zero mask.
On the full active annulus A_U=C_U-mu, exposing the precise signed covariance
lower bound BT_sigma; neither a saving nor an energy lower bound is proved.
Independent224coefficient,2endpoint,75776raw-product,1296complex-covariance,
18Gram and54signed-target controls pass. Radicand valuations1/2mod6 are
distinct from tame conductor exponent1; this wording correction is documented.
Source/review: planning/weighted-moment-20261105/{frontier,review}.
Both gates remain false. Do not repeat centering or mask exclusion as a new
analytic solution; attack the signed covariance with all required uniformities.


## Signed covariance and two-cutoff frontier (5 November 2026)

New shared proofs are papers/signed-bilinear-{core,details}.tex in chapter40,
with executable examples/arithmetic_cutoff/signed_covariance.py and
research/signed-cutoff-covariance.md. In the window2D/7<=U²<=D, every actual
active coefficient is mu(m)(r_U(m)-1), where r_U is an even ordered-factor
count. Thus it is odd/nonzero. Elementary lattice/squarefree counting gives
an explicit positive lower constant for its normalized coefficient norm,
for each fixed nonzero smooth profile. This is not a row-energy lower bound.

A finite example in the ORIGINAL sextic family, with D=400,U=17,nu=1,
all72literal B7 rows and the complete four columns of norms439/475, has
Q(C,mu)=-27/25 despite nonnegative pointwise coefficient overlap and a
positive-definite real Gram. A genuine common nonnegative smooth profile
has exact integer-norm values10/1. A second guaranteed nonprincipal246-row
subset atH89 preserves raw zeros and gives-69/50; it is not the full
nonprincipal family. Independent direct F439/F19/F25 exponentiation
reproduced1272raw characters, full complex Gram matrices and all12amplitude
cases. These are exact finite sign counterexamples, not asymptotic BT_sigma
or GRH counterexamples. No lower bound for arithmetic row energy is inferred.

The high-window bilinear attempt retainsDX after legal factor Cauchy/BGL;
the older regrouped estimate is stronger. The exact two-variable Perron
factorization, normal correction domain, half-integer sharp cutoff and
finite-height error are proved. Safe reciprocal-L contours reproduce the
oldU^(2-4delta)energy cost, with M4(W)^2 and fixed margins retained. Moving
the contours requires actual reciprocal/zero-residue control; numerator
moments do not justify dropping those terms. The coordinate slice is a
meromorphic identity, including the stated numerator-zero caveat.

Independent proof and final-byte TeX acceptance is under
planning/signed-bilinear-20261105/{review-covariance,review-perron}; exact
reports are outputs/checks/2026-11-05-signed-bilinear/. The new book is
237pages/40chapters/6412nativeMathML, with13unique laboratories. Focused
articles51/133pages and paired notes9/24pages are synchronized. Three-pass
builds, source audits, XML/numbered-reference checks and320/390/768/1440px
browser checks pass. Paragraph headings now match the unnumbered PDF style.
Old source volumes, diagrams, data and environments are preserved. Earlier
overfull/undefined-proposition staging failures are retained; valid outputs
alone are promoted. Inherited amsmath/underfull and3old munder warnings stay
explicit. No new dependency, training/GPU job, Lean declaration or GRH proof.

Next: prove a QUANTITATIVE lower covariance budget or coupled arithmetic
fourth moment that permits the observed negative covariance, uniformly in
the original masks, conductors, cutoffs and common profile; cover neighboring
near-saturating blocks. Alternatively control the actual two-variable
reciprocal integrals and all crossed residues. Do not retry automatic
covariance positivity, coefficient shrinkage, marginal independence or a
pole-free contour shift as if these missing inputs had been established.
The best global envelope here still losesD^(1/2) atH=D^(3/4); short/principal
assembly, analytic/category Lean and the positive determinant bridge remain
open. Both completion gates remainfalse; the existing heartbeat stays active.

## Frontier after requested-error readouts and lower covariance budget

- The readout API has fixed-label certificate floors. Fully adaptive positive
  tolerances require proved N/T/quadrature/discard/primitive-series/precision
  rules and new validated labels. Ideal-root LS is not the saved surrogate GD.
- The high-window coefficient moment sum r²<<DlogD and negative covariance
  budget do not save an arithmetic power. Estimate the unequal-product
  row-coupled fourth moment plus mixed Mobius term with union masks and the
  full A1=A2,A1*A3=H^(1/3) face; also retain within-level energies.
- No new analytic/categorical Lean theorem was added. Short/principal
  assembly, scope-specific positive determinant/zero-location comparison and
  every complete GRH scope remain unresolved. Both completion gates false.

## Frontier after adaptive sampling

Fixed q = 3, 4, 5 requested-error sampling/readout construction is implemented
and proved in prose; all-conductor/height extensions, efficient extreme-
request complexity, analytic/category Lean and physical/quantum architecture
comparisons remain separate. Preserved fixed-label APIs still have floors.
The new arbitrary-request theorem does not constrain output zeros or identify
an arithmetic determinant. Positive scope-specific determinant/zero-location
comparisons, short/principal assembly and GRH remain open.

Do not repackage small-conductor/high-gcd recovery as a fresh saving. The
next hard arithmetic input is the joint signed large-conductor/dual-frequency
sum on original common-divisor1 and neighboring A3 face blocks, with original
union masks. Generic±2 fourth-column cancellations and original ±1 factor
expansions must not be conflated. Both completion gates remain false.

## After the quadratic pivot and joint completion

The classical quadratic pivot improves only the A3-dominant part. At H=D^(3/4), the remaining face a>=1/8 still has5/4; a necessary neighboring condition is A3<=max(A1,A2) D^eta with the previous small slack. The exact complete Gauss-phase balance and orientation Parseval do not prove actual weighted incomplete cancellation. Estimate the original joint signed h,q,K weight, especially h=1, retaining coherent cubic-residue fibers, fixed length-one factors and all masks. GL is an explicit classical dependency, not a newly proved sieve.

No short/principal assembly, independent arithmetic positive determinant/zero-location bridge or full analytic/category Lean has been supplied. Compiler approval remains pending; do not install/substitute automatically or rerun the completed inventory. Both completion gates remain false.

## Ordinary conductor refinement and finite arithmetic learning — 5 November 2026

This accepted frontier supersedes earlier descriptions of5/4 as the best
available global unsigned exponent. A classical ordinary all-primitive-character
comparison gives Lambda_A << (HD)^epsilon A6[D+(A1 A2 A3 A4 A5)^2],
with the arbitrary overlapping r6 retained as its actual coefficient mask.
Combining with the powered-family bound and exact capacity yields
H + D H^(1/6) + (DH)^(2/3) for the original residue-subtracted energy,
with fixed nu/S and one common possibly complex W. At H=D^(3/4), power7/6
improves5/4 by1/12 but still exceeds the target3/4 by5/12.
The whole old A1=A2=A,A3=B,AB=H^(1/3) face now costsD; it is no longer
the worst upper-bound face. New upper-envelope witnesses are
(log_D A1,log_D A2)=(5/12,1/6) and pure log_D A1=3/4.
They are not actual-energy lower bounds. The proof includes all-modulus
primitive Gauss completion, nonunit vanishing, reduced Eisenstein fractions,
a lattice large sieve, raw conductor/zero transfer and principal assembly.
It is a refined application of classical sieves, not a new classical sieve.
Independent exact-production proof receipt: outputs/checks/2026-11-05-arithmetic-learning/review-mixed/acceptance-v1.json.

A separate finite Fourier-feature learner targets all210 actual original
coupled correlation coordinates,95(h,q) blocks including65 h1 blocks.
D6000/U60/H625 and one stated common smooth four-bump profile activate all15
squarefree ideal columns; principal nu,2262 literal rows and a separately
labelled2148 guaranteed nonprincipal subset retain4530 raw column zeros.
Four tau1e-12 runs execute216 metric-gradient updates and200 budget-limited
ordinary updates, saving every exact rational state. Both signed observables
and the full-vector tolerance are certified; weighted spectral loss and
metric/ordinary gradient conventions are distinct. Exact labels are supplied
before training, so no speedup, unseen-conductor generalization or uniform
analytic saving is asserted. Immutable v2 manifest binds source/input/output.
Independent acceptance-v2 in outputs/checks/2026-11-05-arithmetic-learning/review-learning/
reconstructs31668 symbols/450 Gram targets/186552 histogram cells and every
saved update/certificate. The failed logging-only v1 remains preserved.

Next substantive arithmetic research must estimate the actual signed joint
conductor/dual-frequency weights before per-conductor absolute Cauchy,
including h1 and the new remaining upper-envelope neighborhoods, with all
coherent fibers, raw common-prime zeros, ray/squarefree/capacity restrictions,
fixed profiles and conductor uniformities. A finite learned Gamma certificate
is not this varying-family saving. Short/principal target assembly, independent
positive arithmetic determinant/zero-location comparisons and scope-specific
Dirichlet/Hecke/Dedekind/elliptic/Artin obligations remain open.
No new analytic/category Lean declaration, PSD or GRH proof is supplied.
Pinned Linux4.24 compiler approval remains pending; do not install/substitute
or repeat the completed inventory without an explicit reply/changed state.
Keep both completion gates false and the existing heartbeat ACTIVE.

Evidence and reproduction: research/mixed-conductor-and-learning.md;
shared papers/mixed-conductor-{core,details}.tex and
arithmetic-learning-{core,details}.tex; examples/arithmetic_learning/README.md.
Do not rerun accepted author/reviewer grids or frozen216/200 traces as new
research. Preserve all earlier sources/runs/releases and original HEAD/index.


## Moving-profile and coherent-mean boundary — 5 November 2026

For principal nu=1, fixed S above2,3 (or a fixed larger S), and U²=D,
the actual norm-radial A_U and literal epsilon=1+omega phase admit ONE
common complex smooth profile W_D with supnorm1. It varies with D, has
derivatives O_k(D^k), and vanishes at the annulus endpoints. On actual
nonprincipal rows epsilon*beta_v^6 the primitive conductor is432, with
power conductors432/27/16/27/432; every original S/v collision remains
deleted. The ideal v is arbitrary, including repeated/overlapping primes.
An elementary positive-density coprime-triple proof gives full original
E-energy >=(c_S+o(1))D H^(1/6), H=D^theta,0<theta<1. This uses outer
row-energy positivity and a SELECTED literal class's h1 A-A contribution;
it does not lower-bound the signed h1 sum over unselected rows.
At theta3/4 lower power9/8 is below the current upper7/6. No new unsigned
upper saving, fixed-W counterexample, positive determinant or GRH follows.
The DH^(1/6) term is necessary in the varying-profile supnorm class for
theta<2/3. A target uniform through M_k(W)^alpha for every epsilon would
need k*alpha>=1−5theta/6; this does not refute existing derivative costs.

The actual orientation projection exactly returns the coupled Gamma norm;
rank supplies no conductor saving. Coherent restriction has compression
3^(-omega(q))*11* and leakage lambda(1−lambda), so it cannot commute with
projection for free. An exact original D4000/U63/q-five-prime fixture has
four active orientations, Gamma=3 and variance0, but selected h1AA=3/1000.
Omitting the literal unit phase incorrectly gives−3/4000. This rules out a
variance-only centering rule without its mean term on nonprincipal rows.
The A6=1 mixed/pure upper-envelope sectors remain open.

Sources: papers/profile-uniformity-{core,details}.tex;
research/profile-uniformity-and-coherent-means.md; examples/profile_uniformity/.
Design review and exact joint note: planning/signed-profile-20261105/.
Independent implementation acceptance-v1 reconstructs all30482 norm groups,
1219280 raw-mask entries,40 distinct arbitrary ideals through norm64, and
14720 direct literal symbols across the six frozen scales. The governing
v2 manifest is a90d1c356c276b36430b58e342ea7aee6dfe6cb33c0d7db0a4ffcb5ab17bc460.
The fixed-X64 good-S family has19 rows; the separate capacity-matched small
caps2..4 contain only the good-S unit. Finite ratios do not prove the
asymptotic theorem. The new standalone profile-uniformity.html inspector
is a hash-bound exact-data view, not browser training. Preserve failed v1
manifests/builds, all earlier sources/outputs/releases and the fixed-profile
frontier. No new Lean declaration or compiler/dependency change occurred.

Next: bound actual signed h,q,K weights BEFORE per-conductor absolute Cauchy,
retaining coherent means, fixed common profiles, full union/common-prime
masks and conductor/ray/squarefree/capacity uniformities, especially h=1
and the A6=1 remaining neighborhoods. Short/principal target assembly,
independent positive determinant/zero-location and scope-specific GRH
obligations remain open. Pinned Linux4.24 approval remains pending; do not
install/substitute/reinventory without explicit reply or changed state.
Both completion gates remain false; keep this existing heartbeat ACTIVE.
