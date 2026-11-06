# Review coverage

This file records textual coverage, not a guarantee that every background theorem, transform identity, or formal dependency is independently certified.

| Material | Coverage | Limitations |
|---|---|---|
| GRH PDF, commit0c77122d | All223physical pages, including appendices and bibliography; selected formula pages rendered and inspected | External theorems not all rederived; multiple decisive false steps identified |
| Surface TeX, commit212ff730 | Full textual reading1–15556: foundations reviewer1–9999 and15370–15556; completion reviewer10000–15376 | Selective derivation checks and exact counterexamples; not certification of all algebraic/hardware claims |
| Surface PDF in same repository | File inventoried and hashed; TeX audited in full | PDF is a distinct tracked artifact and has not been read end to end or proved identical to TeX |
| math September7/8 paper | All16677source lines read; exact blob verified; selected endpoint algebra and continuation checks | Lengthy theta/sieve/moment estimates and external inputs not independently certified in full |
| math October11/12 paper | All3988source lines read; exact blob verified | Main reflection/uniformity and Poisson regrouping require specialist verification |
| math Landau–Siegel paper | All773 source lines read; exact blob verified; determinant/interpolation stress checks | No decisive refutation established in this review; not a certification of the major claim |
| math Lean root/config | README, family003 docs, comparator instructions, lakefile, manifest/toolchain; actual two conclusion modules and comparator files inspected | Upstream Lean4.34.1/package graph not built |
| math formalization graph | Static transitive OAI graph of two actual solution modules:3125 modules, no missing local import and no sorry/admit/axiom token matches | No kernel verification; external packages not traversed; static token scans cannot certify semantics |
| Other math text matches | 27candidate TeX files triaged by matching contexts | GrH cohomology/macros/vendor-code false positives excluded; applications and historical RH mentions not full proof sources |
| New papers | Full core/details reviewed independently; PDFs compiled, representative pages rendered and inspected | Research drafts, not full GRH proofs or journal acceptance |
| New Lean | All7 standalone statements built and axiom reports inspected | Only finite/arithmetic obstructions; no analytic GRH formalization |

No repository AGENTS.md files were found in the three clones. Root user instructions governed preservation. No source clone was edited, updated, cleaned, migrated or rewritten. The large math clone contains174524tracked files; reviewing the selected RH family is not a claim to have reviewed the entire collection.

Continuation: the added main-text and extended-paper arguments were independently reviewed in full, as recorded in reviews/continuation-review.md. The separate analytic Lean file has six kernel-checked declarations using pinned mathlib4.24.0. The source-level exponent analysis is explicitly conditional; exact rational envelope calculations do not certify the character-moment estimates.

Heartbeat2026-11-02: independent read-only mathematical review of holomorphic Hermitian rigidity, dilation singular-value formulas and scope/source references. Three new actual-matrix/complex-analysis declarations in HermitianRigidity.lean pass pinned Lean/mathlib; analytic suite now has nine declarations. Both papers updated, rebuilt with resolved references/no overfull boxes, and changed pages visually inspected. No full spectral arithmetic bridge is verified.

Positive-pencil heartbeat2026-11-02: independently reviewed the generalized positive pencil, metric congruence, inverse estimate, indefinite off-line witness, strict Herglotz/reflection caveats and logarithmic-derivative sign. Seven new Lean matrix declarations independently compiled with warnings as errors; combined analytic suite16declarations passed with only standard foundational axioms. The quantitative inverse bound and log-derivative identity are prose proofs; no arithmetic realization or GRH conclusion is verified. Both paper editions were rebuilt with resolved references and no overfull boxes.

Arithmetic-zero heartbeat2026-11-02: exact Fraction program certifies finite inequalities for S5 modulo3, independently reproduced using a separate implementation; analytic enclosure estimates, second-derivative Taylor remainder and Rouche proof are explicit prose. Two new Lean statements check disk geometry and final rational margin; all18analytic/spectral/certificate statements pass. This is not a formalized root-existence theorem or a full-L/GRH counterexample. Source clones were not modified.

Final article verification: concise7pages and extended15pages; both compile with resolved references and no overfull boxes. The theorem page and two detailed-certificate pages were rendered and visually inspected.

Jensen-metric heartbeat2026-11-02: independently reviewed the explicit compact rate, unscaled companion convention, Newton-sum symmetrization, strict/semidefinite distinction, block-determinant normalization, and Gaussian smoothing counterexample. All7new Lean statements independently compile; combined analytic suite25uses only standard foundations. The exact model script was independently executed in memory. No actual xi coefficient enclosure, universal metric positivity or general GRH assertion is certified. Classical xi properties and Jensen/Hermite criteria remain external/prose dependencies.

Final Jensen editions:8and18pages, resolved references and no overfull boxes; four changed pages visually inspected. Romik1902.06330v3 kernel/factorial normalization independently checked; no factor-two defect found.

Euler-correction heartbeat2026-11-02: focused source rereading3845–4206,5480–5548and8645–8775. Independently reviewed all valuation exponents, explicit denominator constants, open neighborhoods, principal scalar simplification, normal convergence arguments, shifted angular character and the7/12 obstruction under explicit classical analytic inputs. Eight new Lean statements bring the analytic layer to33; ideal counting, arithmetic convergence, source Gauss identification and Hecke completion/zero existence remain prose/external. Exact Q(sqrt(-3)) local samples are not a full source proof audit. No quantitative compensated contour or mean-square input was certified.

Final Euler-correction editions:9and21pages, resolved references and no overfull boxes. New abstract and four proof pages were visually inspected. Classical order-one Hecke theory remains an explicit external input; the zero-transport formal statement does not prove existence of its Hecke zero.

Principal-residue heartbeat2026-11-02: focused rereading of September1531–1642,5570–5835,6173–6328,7004–7044,8775–8905,9050–9097,15548–15669and16270–16372. Independent review confirmed the principal interface extension under explicit inherited contracts, signs, fixed-height uniformity and pointwise/averaged distinction. Six new actual complex finite normalization declarations independently compile; suite39uses only standard foundations. The exact local samples and fraction allocations do not verify the PNT, full Gauss/high representation, contour integrals, or admissible nonprincipal slot counts.

Final principal-residue editions:10and25pages; resolved references and no overfull boxes. The main residue page and detailed normalizer, contour and boundary pages were visually inspected. No complete GRH formalization or new zero-free theorem was certified.

Frozen-capacity heartbeat2026-11-02: focused rereading of September4490–4585,6795–6840,9215–9325,12500–12595,14870–15491and15895–15995. The conditional counting reconstruction was independently reviewed, including capacity equality, minimax, physical supply, small-capacity handling, character presentations/masks, fixed-mesh quantifiers and height order. Seven new Lean declarations independently compile; combined suite46declarations uses standard foundations. Exact Python tests cover64rational crossing/cutoff cases and6finite complex-moment inequalities, not arithmetic moment estimates or detector certification. Both editions11and27pages compile cleanly; four changed proof pages rendered and inspected. No new zero-free theorem or GRH conclusion is established.

Low-energy heartbeat2026-11-02: focused rereading of September1288–1334,2460–2515,2940–3005,3435–3520,6850–6985,7450–7855,8005–8355and8505–8655. Independent review covered the actual conditional application, common profile/row range, all rescaled subsets, offset bound, scale/Gram margins and internal/external height order. Seven actual real-exponent/power statements independently compile; suite53uses standard foundations only. The15geometry cases and12357abstract dyad tests do not establish arithmetic moments or the underlying exact identities. Both editions12and29pages compile cleanly; four changed pages rendered and inspected. No new unconditional zero-free or GRH claim.

Central-contour heartbeat2026-11-02: focused source rereading4240–4282,5480–5640,5735–6174,6345–6395,6520–6583,8645–9052and15695–15928. Independent read-only review covered conditional D1 deformation below7/8, full correction before quotients, joint conductor credit, pointwise labels, exceptional/floor conditions and cumulative heights. Ten actual geometry/power/integral/exponent components independently compile; complete analytic suite63uses standard foundations. Finite rational tests do not certify the high identity, buffered estimates, trace contracts or moments. Both article editions13and32pages compile cleanly; five changed pages rendered and inspected. Outer-row/final closure and deep arithmetic certification remain open.

Finite-correlation heartbeat2026-11-02: source7038–7336 reread with independent audit of7055–7247. Universal actual finite-field/MulChar/Gauss statements are checked in16new declarations; suite79uses only standard foundations. Prime-power quotient lifting and CRT normalization/phase orientation have prose review; exact source pairing and fixed reciprocity-table identification remain outside formal scope. Deterministic actual Eisenstein diagnostics cover108990field cases,2058raw pairs,24prime-power lifts,12overlapping residuals and6CRT cases. No genuine source counterexample found. The artificial/genuine off-locus distinction is necessary and retained. Both editions14and35pages compile cleanly; five changed pages rendered and inspected. No Gram/moment, global zero-free or GRH theorem is certified.

Gram-Poisson heartbeat2026-11-02: focused reread of September8345–8560, with independent adversarial audit of the complete Mobius masks, fixed-period input, normalized dual sum, subunit annular scales, nonexceptional dyadic tail and sixth-power exceptional count. No source counterexample or period-square loss found. Nine actual finite Fourier/field-character and real finite/infinite sum declarations independently compile; combined suite88uses standard foundations. Exact finite diagnostics do not certify lattice Poisson or source reciprocity. The prose general lemma and conditional source application now appear in both editions,15and38pages, with clean builds and four final changed pages rendered/inspected. Exact arithmetic period, pairing/representation, reflection/moments and global zero-free/GRH claims remain uncertified. Next source target647–734 and761–1095.

Reciprocity-period heartbeat2026-11-03: focused rereading of September570–694,761–1095,3320–3377,7090–7203 and8385–8465. Independent adversarial review covered the Gaussian phase/table, cubic-to-sextic orientation, explicit conductor upper modulus and full column/mask/CRT ledger. Thirteen actual Eisenstein quotient-algebra declarations independently compile; full suite101uses standard foundations. CFT/cubic reciprocity/Gaussian integration remain named prose dependencies. Exact finite checks cover1728unit triples,1936sextic pairs/294zeros,26400row conversions and a norms31/43 counterexample to modulus12 for all fixed numerators. The source already allows higher S-powers. Both editions16and41pages compile cleanly; five changed proof pages rendered/inspected. This closes the fixed-period input in classical prose, not reflected moments or a global zero-free/GRH claim.

Reflected-identity heartbeat2026-11-03: focused reading1660–2455,2540–2618,2888–3055,7318–7483 and7508–8238, with independent audit through8005 of canonical branches/scalars, exact phase/root/zero and coefficient-independence ledger. The block reduction passes conditionally on theta/cusp formulas and stated original block hypotheses. The common-profile estimate is rederived in prose from the Mellin kernel; gamma background checked in DLMF5.2/5.11.9. Nine actual local character/phase/Bochner statements independently compile; primary full suite110passes. Actual finite fields and prime phases give5058columns/partitions,252scalars,2592phasecases,50nontrivialmovingj4pairs and90shared-cube cases. These are not theta or mean-square certificates. Both editions18and44pages compile cleanly; six changed pages rendered/inspected. Next audit: hybrid-energy with both complete masks and exact primary large-sieve scopes.

## Added2026-11-03: four projective-resolution sources

Full textual reviews cover all54pages of1810.06750v5,26pages of1812.00621v1,40pages of2210.11433v1 and24pages ofmath/0511610v1. Exact artifact hashes, page/section coverage, source inspections and external-review limits are in planning/reviews/projective. New focused articles develop corrected exact resolutions and determinants without modifying the source clones. Recent2023–2026 geometry/resolution/Koszul work and classical determinant/purity sources received focused primary theorem review, not a claim of full independent proof certification. The actual new formal layer has13 dual-number module declarations and3 matrix declarations; the universal quiver/derived/trace framework remains prose/external/open as declared.

## Added2026-11-03: Hodge and relative boundary determinant test

Complete new prose derivations cover finite parity cancellation, metric and holomorphic-family limitations, explicit unilateral-shift relative Fredholm realization of the weighted Cartan determinant and the escaping-terminal-block failure of trace-norm convergence. Independent review reconstructed those proofs, checked quotient domains, and compiled the new11 actual matrix/operator-ring declarations; full analytic suite137 passes. Fifteen finite-complex/positive-metric systems and24 boundary samples are exact diagnostics, not infinite proofs. The actual ℓ²/Fredholm/trace-norm theorems remain prose. Ray–Singer1971 §1 pp147–150 was inspected for the distinct degree-weighted torsion construction; no full66page review is claimed. Focused editions now11/23pages; seven changed pages were rendered and inspected. The arithmetic identity, positive realization and intended GRH scopes remain open.

## Added2026-11-03: arithmetic Abel boundary family

Complete new prose derivations cover bounded Dirichlet partial sums, dyadic ℓ² membership and holomorphy, exact Fredholm L/completed-L identities, every raw finite cutoff with its endpoint, finite arithmetic matrices and compact trace-norm convergence, and the critical-height common-metric obstruction. Independent review read the note, article sections, new Lean and exact checker in full, compiled10 declarations and reproduced216finite determinants/108Abel/42kernel-tail/36u-tail/36geometric tests. Formal coverage includes genuine continuous rank-one operators and an infinite geometric HasSum, not the full arithmetic lp/Fredholm construction. Focused primary review: DLMF2.10.9/25.15 and Bornemann0804.2543v1 §§3–5, not a full43page reading. General spectral positivity, surface/order arithmetic comparison and broader GRH scopes remain open.


## Signed divisor coverage — 5 November 2026

The new canonical papers/signed-divisor core/details and matching book chapter material received independent full derivation review: exact arbitrary-coefficient incidence lift/error certificate, nine-zeta local correction/finite-height cutoff recovery, finite eight-short-state numerator and fixed-common-profile coherent Mellin sum. Exact finite code coverage is separate: all three full-column manifests, small direct pair checks, complete large raw/F/Z/gcd-poset reconstruction and unit-edge-only v2 compatibility are pinned by outputs/checks/2026-11-05-signed-divisor/review-design/ and analytic/large-full-column-review-v1/acceptance-v1.json. The lossless inspector replays all three immutable v1 datasets, with no training. The separately reviewed v2 helper does not relabel old data provenance.

No Lean declaration was added or executed for these new analytic results; pinned Linux4.24 approval remains pending. The existing selected kernel-checked layer does not formalize this new coherent signed estimate, which is itself still open beyond the accepted exact reductions. No original-family asymptotic power gain, determinant/zero-location comparison, Artin holomorphy or GRH claim is made.


## Explicit rough-prime mask budget — 5 November 2026

A NEW quantitative A-A result replaces the rough-prime deletion by a defined
auxiliary kernel with an explicit correction. Work over the Eisenstein
ideals, with finite fixed S containing primes above2,3, original unitary nu,
ONE common complex W supported in[1,2], full original good squarefree annular
columns, and actual finite NONZERO literal rows1<=Nu<=H with weights w>=0.
Keep all internal row squarefree/coprime/unit/ray/capacity/sixth-factor masks.
The required window is U>=1,U²<=D,2D<=7U². It is not an all-cutoff theorem
or a theorem for arbitrary selected-column subsets/extra column filters.

Write d=f*e for the common IDEAL divisor, with f U-smooth/e U-rough; f is
NOT the original column-pair gcd h. Actual A_U(ez)=A_U(z), with NO mu(e)
inside A_U. Nonunit residual pair max(Na,Nb)>=7 permits at most one rough
prime; the unit pair a=b1 permits two DISTINCT rough prime IDEALS and
forces f1. The exact nonnegative C2 correction includes conjugate primes
of equal rational norm. It is not a lower bound for the whole signed slice.

Let K0 be the smooth-f signed completed norm, KT the original rough-prime
completed norm with full(p,abuS)=1, and KS its explicitly AUXILIARY S-only
rough-prime extension. All outer mu(f) signs, smooth masks and original
raw chi_a(u) zeros remain. With Rw=sum w, B=||W||infinity and kappa_U(u)
the number of distinct good rough prime ideals dividing u,

  D*S1AA = K0-KT+C2,
  Delta=(KS-KT)/D,
  |Delta| <= B²[229376 sum_u w_u kappa_U(u)+2048 Rw],
  0<=C2/D<=1792 B²Rw,
  S1AA=(K0-KS)/D+E,
  |E|<=B²[229376 sum_u w_u kappa_U(u)+3840 Rw].

If H<=D^(3/4), kappa_U(u)<=1 at EVERY scale, so
|E|<=233216 B²Rw<=2^18 B²Rw. For actual unweighted two-pivot rows with
bounded literal multiplicities, Rw<<A1*A2<=H; the correction is O(B²H),
without a divisor-power or profile-derivative factor. This bounds ONLY
the accounted correction, not the remaining signed main (K0-KS)/D.
The existing7/6 global envelope and missing5/12 saving are unchanged.
Principal/residue assembly and other coefficient channels remain separate.

The proof retains the exact disjoint row/residual prime union. Residual
prime deletion forces f1,a=p (and/or b=p) on support and gives exactly
2Re(T_1(P;u) conjugate(z_p(u)))-|z_p(u)|²; the last intersection term is
indispensable. The row term retains all raw zeros before any error triangle.
A support identity gives A_U(g)=mu(g)(2*1_(Ng<=U)-1) when good SF Ng<=7U,
including the unit. Active rough T terms have N(fa)<7U and therefore
|A_U(fa)|=1 exactly. This is not unrestricted multiplicativity, a proxy or
a shrinkage claim for the whole original annulus. Elementary ideal counting
and sum_f(Nf)^(-2)<=64 give the explicit constants; no prime theorem is
needed for the mask result. Both scaled comparisons are WEAK at B=0/Rw=0;
prior strict-product source/acceptance remains historical with a correction
addendum, never silently rewritten.

A separately reviewed coherent Stieltjes substitution retains Gf(t) as the
actual weighted row norm and mu(f) OUTSIDE, with exact lower boundary
-Gf(U)(pi_K^S(U)-Li(U)). Only the fixed-S prime measure is approximated;
growing deleted masks are already accounted by the correction. The analytic
Li/PIT subsection requires U>=7. Its operator variation budget retains
M1(W)^2 and a TRUE weighted norm input; the classical specialization is
ONLY the accepted unweighted/bounded-natural-multiplicity A6=1 two-pivot
family. At H=D^(3/4), U~sqrt(D), its inherited positive-operator majorant
has worst power5/6 times delta_S(U), not a new saving. The pinned fixed-field
Thorner--Zaman2019 Theorem1.1 supplies a subpower prime error after a fixed
threshold, retaining/absorbing any fixed exceptional zero. That upper budget
does not certify the3/4 target; actual signed errors may cancel and K0-J is
still unestimated. No actual-error lower bound, growing-conductor PIT,
pole-free contour shift, Artin holomorphy, positive determinant or GRH follows.
The DOI/publisher URL/cache hashes are in PUBLIC-CITATION-v1.json; full
publisher PDF/text/HTML caches remain local and excluded from publication.

Fresh deterministic controls use D200/U10/H53 with52columns5rows,
D512/U16/H107 with139columns7rows and D900/U30/H384 with250columns2rows.
The last is a declared noncritical capacity, NOT floor(D^(3/4)); its row
rough correction is exactly zero. A new fixed smooth W_delta,delta1/4096,
has exact flat strict norm nodes only on the stated integerD<=1024 scope
and explicit large derivative constants. It is not the previous profile.
All raw original/auxiliary masks, inert and conjugate primes, unit residual
states and non-squarefree auxiliary p² terms are retained. Raw
(K0,KS,KT,Erow,Eres,C2,D*S1AA) are respectively
(339,235,209,20,6,21,151),(366,781,711,48,22,89,-256),
(436,410,366,0,44,28,98). Normalized Delta values13/100,35/256,11/225
and actual-clean errors47/200,159/512,2/25 each divide by D ONCE.
These finite signs do not make Erow/Eres universally nonnegative.

Independent arithmetic reconstructs complete ideal universes/SF subsets,
3561 literal phase values (including auxiliary residual universes),3353
COMPLEX Fd transfers,199smooth/3154rough grid states INCLUDING exact-zero
placeholders,5119terms/39auxiliary nonSF terms and273767 ordered original
column-pair-row checks. All2510 active-profile reduced coefficients satisfy
the exact coupled short identity. A captured norm247=13*19 example rejects
its unrestricted use outside Ng<=7U. No old table/trajectory/evaluator was
rerun; fresh arithmetic/phase controls do not prove the analytic constants.
The compact exact summary web/data/rough-mask-controls.json SHA7596718f is
a projection of these immutable new inputs, with no browser training.

Governing canonical proposals f6de9534/a7d91548 match shared
papers/rough-mask-{core,details}.tex and book fragments. Independent gate
outputs/checks/2026-11-05-rough-mask/review/canonical-acceptance-v1.json
SHA89fa5333 binds analyticv5, zero/domain addendum, independent data/projection,
root PIT review and primary citation. Source/builds and all earlier failed
reviewer schema assumptions are preserved. Both originals, source clones,
all prior environments/outputs/cache/history and unrelated progress remain
untouched. No new Lean declaration, dependency, authentication or GPU work.
Pinned Linux4.24 compiler approval remains unanswered; do not install,
substitute, reinventory or repeat the question.

Next: estimate the ACTUAL clean mean-retaining signed main (K0-KS)/D, or the
coherent K0-J and signed prime-error cancellation, using the exact coupled
cutoff/Mobius coefficients and original row masks/conductors. Do not recast
this explicit correction bound, elementary unit-sector count or inherited
5/6 operator budget as the missing5/12 saving. Short/principal assembly,
independent positive arithmetic determinant/zero-location bridges and the
separate Dirichlet/Hecke/Dedekind/elliptic/generalArtin obligations remain
open. Actual analytic/category Lean and both completion gates remain false.
Keep the ONE existing heartbeat ACTIVE; no guaranteed proof schedule.


Final rough-mask promotion: outputs/checks/2026-11-05-rough-mask/promotion-v1/promotion-v1.json binds bookPDF/nativev1 and four focused/notev1 builds. Current edition288pages/40chapters/8552MathML; ALL8176previous literal math subtrees remain ordered/byte-identical, all386previous tables retained in388,13canonical iframes and29SVGrefs/assets unchanged. Focused67/183pages; notes25/74pages. Source-bound detailed proof, independent new ideal/phase/data checks, nativeQA at all widths and rootPDFvisual review pass; no new malformednode/overfull/unresolvedref/Lean declaration. Three inherited munder nodes and old amsmath/hyperref/underfull diagnostics remain disclosed. Exact zero/domain/full-column qualifiers supersede historical weaker/strict-scaled drafts without rewriting them. The explicit mask error has target size; the signed clean main, global5/12 saving, principal/determinant/zero-location bridges and full Lean remain open. Original sourceHEAD/index, all earlier releases/environments/cache/history and Macpreview remain preserved. Publication is a separate concrete gate.


## Physical-radicand sieve and coherent main — 5 November 2026

This substantive frontier supersedes older current7/6/global5/12 and
pure5/6-positive-certificate descriptions; their mathematical history stays.
NEW external input: Alexandre de Faveri, Optimal large sieve for fixed order
characters, arXiv2610.04045v1,2October2026, Theorem1.1. This is a pinned
submitted preprint theorem being invoked, NOT a new proof of that sieve,
a priority claim or complete Lean verification. PrimaryPDF SHA256:
97720b3cacccbedb9c2014520ad4d128ae23afd0a781bdeff27dab4e86b7c726.
Full primary reading caches remain LOCAL; public metadata pins the version.

The exact application uses K=Q(omega), containing mu6; mu12 is not needed
for Theorem1.1. Unique ideal generators alpha=1mod3 remove unit ambiguity
in the source's allowed fixed Section2.3 construction. BOTH indices are
sixth-power-free ideals. Physical radicand norm, valuations1..5, lower
character orders and all raw common-prime/union/ray/SF/capacity masks remain.
There is NO radical relabeling or arbitrary-family reciprocity premise.
Freeze arbitrary possibly nonsquarefree/overlapping r6 with its ACTUAL
coefficient collision mask. For original raw and residue-subtracted sums,

 Phi(H,D)=H+D H^(1/6)+H^(5/6)D^(1/3)+H^(1/3)D^(5/6),

 times B²(HD)^epsilon for fixed nu/S and ONE common complex W, B=supnorm.
The r6 sums use powers-6,-5,-2; the Dterm counts H^(1/6) ideals. All global
S-factor exponents are positive; principal residues/cutofflogs are retained.
For1<=H<=D every term is <=D H^(1/6). Critical9/8 improves previous7/6 by
1/24, still3/8 above target3/4. For fixed0<theta<1 and H=D^theta, the accepted moving-W_D obstruction matches
this unsigned SUPNORM-CLASS power ONLY when W may vary with D. It does not
prove fixed-W sharpness or refute suitable explicit-seminorm bounds/GRH.

For original UNWEIGHTED A6=1 two-pivot h1 rows, the exact gcd-Mobius
subsequence norms retain A_U(dn), every raw zero and direct subunit counts:

 |S1AA| << B²(HD)^epsilon [H+D+H^(5/6)D^(1/3)+H^(1/3)D^(5/6)].

Critical13/12 improves former7/6 by1/12, still1/3 above target. The Dterm's
S-factor exponentzero uses a finite polylog count, NOT a convergent sum.
Under inherited high-window/capacity hypotheses,
 |(K0-Kall)/D|<=|S1AA|+236800 B² actualrowmass.
This retains the combined mean; neither separate main is estimated at
target scale. Arbitrary positive weights require a TRUE weighted norm.

Previously reviewed research-only reductions are now integrated with full
proofs. KS=Kall+P2 has ORDERED(p,q),p=qallowed and onlyq's rowmask;
P2/D<=3584 B²rowmass differs from unordered DISTINCT C2/both masks.
Old233216 remains for the old main;236800 belongs to the new main.
Endpoint-exact two-jump Mertens summation keeps both closed-prefix terms,
fullT including common primes, and196608 M1²rowmass D/(UZ)m_(14DH)(Z).
Zcuts residual lengthX, NOT smoothf. Hypothetical scalar powers are not
proved; boundedX has unitf and marginal cancellation cannot bound the full
coherent outer sum. Euler deletion includes ALL supported prime powers;
only fixed-field subpower transfer follows, with fixed exceptional-zero
qualifications. The old sufficient smooth-f tail bound remains valid as a
coarse inherited localization, not current optimality or signed saving.

The joint Stieltjes operator keeps -E_S(U)Q(U), orientation means/equalnorm
fibres/rawzeros/fullsignedmatrix. Rough-prime positive compression is NOT
invariant and supplies no full energy lower bound. Radial Mellin Parseval
keeps equalnorm correlations. The current short positive input is the MINIMUM
with older valid bounds on1<=L<=D, directunitcount on1/2<=L<1. Pure budget
improves5/6 to19/24; mixed7/9 remains smaller. These are sufficient positive
MAJORANTS, not actual-error lower bounds. Keep the minimum INSIDE the
variation integral and the pointwise lowerendpoint.

CONDITIONAL diagnostic only: an all-scale/all-epsilon squarefunction
d2(T)<<T^(-alpha+epsilon) would imply zeta_K zero-free STRICTLY right of
max(1-alpha,1/2) by Mellin discrepancy continuation and primepowers.
Scalar inputs sufficient for pure/mixed majorants would be U^(-1/12),
U^(-1/18), yielding conditional strips11/12,17/18. NONE of these inputs or
strips is proved or asserted necessary for the actual signed target.

Canonical shared sources: papers/coherent-main-{core,details}.tex and
papers/physical-sieve-{core,details}.tex, exact book counterparts. Two
independent application reviews and one joint source-bound canonical review
keep the deep theorem external. The EXISTING quadratic-pivot inspector
shows currentglobal9/8/A6=1slice13/12, historical curves, suppressed unknown
constants/epsilon losses. The entire former cube face remains better
controlled at power1 by the old ordinary comparison. Displayed numbers are
bound expressions, not measured norms/energies/training/GRH.

Next: improve ACTUAL mean-retaining combinedK0-Kall or coherentK0-J PLUS
signedprimeerror/endpoint BEFORE per-f/per-conductor independent absolute
Cauchy, retaining exact generalA_U (NOTroughshortlemma onK0), fixedcommonW/
explicitseminorms, fullunion/commonprime/ray/SF/capacity masks, means/equalnorm
fibres and neighboring mixed/pure blocks. No target cancellation follows
from this new positive norm application. Short/principal target assembly,
independent positive determinant/zero-location bridges and separate
Dirichlet/Hecke/Dedekind/elliptic/generalArtin obligations remainOPEN. No
Artinholomorphy/GRH/desiredpositivity/zeros premise or new analytic/category
Lean. Linux4.24 permission stillUNANSWERED: no install/download/substitute/
reinventory/repeatedquestion. BothgatesFALSE; ONE heartbeatACTIVE. Preserve
sourceHEAD/index, all releaseworktrees/indices/originals/data/outputs/caches/
environments/history/Macworkspace/old8765preview/privateactive-modeldata.


Final physical-sieve promotion: outputs/checks/2026-11-05-physical-sieve/promotion-v1/promotion-v1.json binds valid bookPDF/nativev3, focused concisev1/extendedv2 and notes concisev1/extendedv2, plus inspected inspectorv3. Edition303pages/40chapters/9172MathML, focused71/200pages, notes29/89. ALL8552previous literal math subtrees remain ordered/byte-identical, all388oldtables remain in389,13canonical iframes/29SVGrefs/assets unchanged. Current external-preprint-based unsigned envelope has critical9/8 and original unweighted A6=1two-pivot signed comparison13/12; target3/4 is still open. Globalgap3/8/scopedsignedgap1/3 supersede former5/12. Newshortpositivecertificate19/24pure and min7/9mixed have only CONDITIONAL scalarinput/strictstrip diagnostics; no input or newzero-free strip is proved. Fixed0<theta<1 moving-profile supnorm sharpness is not fixed-W sharpness. Every original mask/commonprofile/mean/endpoint and arbitraryweightednorm qualification remains.

All6source-bound PDF/native builds, independent mathematical/application/integration reviews, focused exponent/model controls and UI/native desktop/mobile/night/keyboard/source/PDF/visual checks pass. No new malformedMathML/overfull/unresolvedreference/Lean declaration. Three inherited munder nodes and old amsmath/hyperref/underfull diagnostics remain; source-matched cachedPDF searchability/publicSVG limits unchanged. Failed hash-line/native-spacing/earlycapture candidates and all old outputs remain preserved. Both completiongatesFALSE; target signedassembly, independent determinant/zero-location and scope-specific GRH/analytic-categoryLean remainOPEN. Linux4.24approval stillunanswered; no newinstall/substitution/question. OriginalsourceHEAD/index, all releaseworktrees/indices/environments/caches/history/Macpreview/privateactive-data protected. Publication is separately gated; keepONEheartbeatACTIVE.
