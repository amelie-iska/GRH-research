# Full-text mathematical audit of quasi-sept.tex (verification incomplete)

## Identity and honest scope

Audited immutable input: `/tmp/grh-math-audit/quasi-sept.tex`, 766,316 bytes, 16,677 lines. I independently recomputed its Git blob SHA-1 as `268c4e3206d460c617d3d2129742a72b831b3def`, matching the specified input. No source edits, installs, authentication, publishing, or MCP calls were made.

**Full textual coverage is complete: every line 1–16,677 was read.** The initial pass read 5,621 lines; the follow-up read all 11,056 remaining lines, including the complete reflection, unmarked energy, sextic sieve recursion, both complete moment inductions and initialization, all contour and tail arguments, and bibliography. A union-of-ranges check returned `Distinct lines read: 16677; Uncovered: []`. A truncated tool response near the reflection/preliminary boundary was reread explicitly (1350–1424 and1841–1905).

This is full **reading coverage**, not full independent proof certification. The external source formulas have not been checked against their cited papers, and the many local finite-transform identities, support extensions and recursive measure bounds have not all been independently recomputed. There is no justified finding here that the major claimed theorem is established, nor a decisive counterexample refuting it. I independently checked selected algebraic transitions as described below.

## What the manuscript actually claims

The title, abstract, and Theorem `thm:main` (lines29–43 and106–119) claim a zero-free half-plane `Re(s)>7/8` for **all finite-order Hecke L-functions over Q(sqrt(-3)) and all Dirichlet L-functions**, allowing the principal pole at s=1. Lines117–119 explicitly distinguish this from RH/GRH and say the critical-line assertions are not proved.

This is not a proof of RH: even if every estimate in the manuscript were correct, the conclusion allows nontrivial zeros with real parts between1/8 and7/8 (after using the functional equation). It says nothing here that would force all zeros to have real part1/2. The boundary7/8 is explicitly excluded from the strict zero-free assertion.

The claimed family-wide zero-free half-plane would nevertheless be a major result. It would uniformly exclude exceptional real zeros in (7/8,1), and the manuscript derives polylogarithmic least quadratic nonresidues and a deterministic polynomial-time square-root algorithm over prime fields (lines320–360), conditional in logical dependence on its main theorem. It is incorrect to dismiss this merely because it is weaker than RH, or to regard the algorithmic corollary as independent evidence for the main theorem.

This document differs materially from the surface-order PDF. It uses theta transformations, character moments, Mellin signals and a zero-detector, not a self-adjoint determinant construction. The elementary prime-series, Belyi, Taketa, and determinant-preservation failures identified in that PDF cannot simply be transferred to this manuscript.

## The top-level analytic criterion appears sound as a conditional lemma

The proposition “Continuation from a common signal” is at lines400–520. For a global supremum beta_* of real parts of zeros and a proposed boundary sigma_0, it requires:

1. A holomorphic Euler correction H_eta uniformly bounded away from zero on `Re(s)>sigma_0`;
2. A normalized physical sum J_eta(Z) with a power bound at the proposed boundary;
3. A power-saving bound for J_eta(Z) minus a Mellin integral f_eta(Z) containing the target reciprocal;
4. A strictly positive saving common to all target characters, although constants and thresholds may depend on the target.

The proof obtains a bound for f at infinity by the triangle inequality, rapid decay at zero by moving its defining contour right, and then a holomorphic Mellin transform to the left of beta_*. Fourier inversion identifies it with the reciprocal on a common right half-plane. Since H_eta is nonzero and the omitted Euler factors are nonzero in the right half-plane, a zero arbitrarily close to the global supremum supplies a contradiction.

I did not find a logical defect in that conditional argument on this reading. The exponent comparison is appropriately made relative to `C(beta_*)`, not `C(sigma_0)`, and the supremum need not be attained. Using a near-supremum zero is sufficient. A target-dependent lower threshold does not invalidate the argument because a single target is selected only after the common positive gap is fixed. This is an improvement over vague “analytic continuation by functional equation” assertions: the connected-domain identification and uniform exponent are explicit.

The criterion does **not** prove the required estimates. Verification of those estimates is the entire substantive task remaining for an audit.

## Main dependency chain

### First stage: Re(s)>11/12

The first-stage theorem is at lines532–555; its assembled proof is at6790–6805.

- **Completed cubic reflection** (`prop:completed-reflection`, starting1676). This supplies an exact transformed formula for a completed theta sum, retaining character zeros on nonunits, whole-index twists and the original coefficient masks. The manuscript gives a differentiated theta-integral and cusp-transformation argument for the entireness of T. I have now read the complete statement and proof, including the intermediate finite transforms1841–2279 and Mellin/continuation/kernel conclusion2280–2465. Its source coefficient/cusp formulas and complete multiplier ledger still require independent verification.
- **Unmarked completed-row energy** (`lem:unmarked-completed-moment`, starting3138). This gives the mean-square `Z^{1+epsilon}` input. I have now read its full proof, including the quadratic collision-mask reduction, common-profile separation, powerful-part count and actual residual annuli. Its bound remains an independently unverified deep dependency, rather than an omitted section.
- **Balanced low estimate** (`prop:balanced-low`, 3672–3722). Conditional on that completed-row moment, the Cauchy–Schwarz calculation is transparent: the additive moment is `(Q+Y^2)/Y`, the row moment is `Z^{1+epsilon}`, the outside normalization is `Q^{-1/2}`, and X=Y=Z^(1/2) yields `Z^{1/4+epsilon}`. I read the planar additive large-sieve proof and the reduced-fraction separation/coefficient-mass argument in full and found no immediate normalization error in this portion.
- **Exact Poisson representation and local Euler product** (`lem:local-euler`, 4010–4199). The claimed quotient is `zeta_F^S(6z)L^S(w,chi_bullet(u))/L^S(x,eta conjugate(chi_bullet(u)))` times a normally convergent correction. The `u=1` term contains the desired reciprocal. I read the complete Poisson derivation3724–3846, local table, phase-cancellation discussion and convergence estimates3847–4201. I have not independently recomputed the whole finite Gauss-sum table.
- **Buffered bins, pointwise bounds, saturated witnesses** (4201–4687). These assign row-dependent zero-free rectangles and produce large inverse and plain Dirichlet polynomials at one common row character/height. I read this whole section. Its use of known zero-free regions of individual buffered disks is logically different from assuming the desired global theorem. The proof carefully distinguishes primitive inducing characters from their zero-extended presentations.
- **Sextic large sieve and row envelope** (`lem:sextic-large-sieve`,4707; `prop:sextic-row-count`,5181). The desired sieve norm is `K+D+(KD)^(2/3)` up to epsilon factors. I have now read the full sieve proof4699–5180, including its paired Poisson, gcd, power-decomposition and near-monotonicity steps, and the full envelope proof5181–5460. Conditional on the sieve and detector, its powerful-part decomposition and final affine optimization appear coherent. The squarefree coefficient sequence is frozen before each residual row sum, as required.
- **Contour transformation, central estimate, principal extraction and outer rows** (5460–6492). I have now read this entire section, including the all-height integrated/trace tails, fixed-bin contour proof, central accounting, principal extraction and outer rows. These remain crucial analytic dependencies whose hypotheses must match the physical formula at every use.
- **Balanced high estimate and final choices** (6493–6700). The proposition claims a target-independent `1/4800` saving relative to `C_I(beta_*)`. It invokes the preceding detailed margins, chooses real losses before the target, then chooses a target-dependent height exponent and a larger external tail order. This assembly is valid only if the retained height orders truly do not grow with that final external order.

This first stage already claims a fixed zero-free half-plane. It should be independently audited and settled before investing in the longer second-stage amplification. Its proof does not require the later inverse/plain moment inductions.

### Transfer to all Dirichlet L-functions

The quadratic-transfer proposition is at6705–6780. I read its proof in full. It uses the norm character over F and, after deleting finitely many Euler factors, the identity

`L_F(s,chi o N) = L(s,chi)L(s,chi chi_-3)`.

The split/inert Euler-factor calculations are correct as written. Away from s=1, the Dirichlet factors are holomorphic in the relevant strip, so zeros cannot disappear through a pole. The proof treats the sole possible principal pole-zero cancellation at s=1 separately using `L(1,chi_-3)=pi/(3 sqrt(3))>0`. The paired series and integral give that value. I found no immediate flaw in this conditional transfer. It only transfers a proved Hecke zero-free half-plane; it cannot supply the Hecke theorem itself.

### Second stage: Re(s)>7/8

The bootstrap first assumes `7/8<beta_*<=11/12`. This sets `Delta=beta_*-7/8`, `kappa=2 beta_*-1=3/4+2Delta<=5/6`. The final geometry is h=13/16, ell=1/6, l_x=17/48, l_y=23/48, and `C_II(s)=s-11/16` (15495–15547).

The key new dependencies are:

- A compensated physical probe, with local tuple corrections whose holomorphy and exact Poisson identity must hold before pointwise divisions/amplitude partitions;
- A marked reflection and reflected-energy bound (sections7249–8060);
- The compensated low estimate (8061–8650);
- Dynamic local error bounds and actual conductor allocation (8651–9208);
- The marked inverse moment, stated9250–9281, and its canonical estimate9296–9347, proved through a long two-Poisson recursion and initialization9783–12342;
- The plain fourth moment with short prime factors, stated12531–12579, whose main induction spans12603–14984;
- Prime amplitude controls and refined row counts14985–15494;
- Principal normalizer and high-bin estimate15548–15852;
- Outer norms15853–15919, the endpoint inequality15920–16111, and quantified final choices16189–16466.

I have now read every statement and proof in this chain, including the complete canonical two-transform reduction9783–11600, inverse initialization11601–12342, and all plain-moment steps12603–14984. Reading has not independently verified every transform, support manipulation or recursive estimate. These are substantial new mathematical inputs, not routine citations or mere bookkeeping; they still need specialist proof checking before acceptance of the main theorem.

## Specific checks that passed at the level inspected

1. **Sixth-power amplification identity (12362–12476).** For squarefree Möbius columns, separating the part dividing rad(a) gives the displayed exact identity relating M_u(D) to M_{u a^6}(D/q_d). The map `(sixth-power-free u, primary a) -> u a^6` is injective by valuations modulo6 and the chosen primary generator. This would not be true without the sixth-power-free restriction; the proof uses it explicitly.
2. **Noncircular dynamic plain-moment hypothesis.** The plain estimate at12531–12579 assumes `beta_*<=(1+kappa)/2` when kappa<1. In the intended application kappa is *defined* to be2beta_*-1, so the hypothesis holds by equality. That equality is not itself circular reasoning. The difficult issue is the proof of the conditional moment estimate and its uniformity, not this substitution.
3. **Common exponents versus target-dependent constants.** The continuation criterion and late-height lemma carefully allow eta-dependent constants and thresholds while keeping an exponent common to all targets. This distinction is mathematically appropriate.
4. **Endpoint certificate (15994–16100).** I independently expanded the displayed polynomial identity with exact rational arithmetic using the Python standard library. The coefficient residual is identically zero. The numerical assertion `49/440640>1/10000` is also correct. The stated rational supply margins `8/39-7/37=23/1443`, `1/5-7/37=2/185`, and `1-h/4=51/64` are correct. This verifies the *algebraic certificate*, not the character-moment inputs supplying its R and q.
5. **Correct logical comparison in final exponent.** The final high estimate subtracts Delta to compare with `C(beta_*)`; it does not incorrectly demand every exponent be negative relative to the raw boundary scale. The calculation at16098–16111 makes this distinction explicit.

## Risks requiring full verification, not claimed refutations

### A. External theta/cusp input and finite phases

The exact reflection is extremely sensitive to cusp representatives, additive-character normalization, unit factors, original masks, and which coefficients are nonzero. The paper cites unconditional formulas from Dunn–Radziwill and says it does not use their conditional prime asymptotic. That separation must be checked directly against their formulas. A wrong scalar phase or dropped zero-on-nonunit factor can invalidate the shared physical/high expression even if later inequalities are right. The theorem statement is much more precise than the surface-order PDF’s analogies, but precision alone is not verification.

### B. The unmarked energy and sextic sieve recursion

These are the minimal deep checks needed even for11/12. A standard large-sieve shape cannot be substituted for the exact family, primary-generator convention, paired character, and coefficient restrictions. In particular every call must freeze all row-independent masks and coefficients before applying a positive norm inequality. The envelope proof appears to respect that at the inspected level; the recursion itself still needs checking.

### C. Moment induction closure

For each inverse/plain recursion edge, a reviewer must check: exact finite transform; conductor and puncture support; retained whole-product profile; the same family on the child; a strictly smaller declared width; treatment of exceptional inducing characters; no discarded main term; a coefficient measure of controlled mass; and uniform finite derivative/height orders. The abstract propagation lemma9348–9485 is a valid rule **conditional** on these bounds; it explicitly disclaims proving the arithmetic reductions. The late induction discussion14779–14984 explains how those requirements are meant to hold. The preceding several thousand lines have now all been read, but their many exact transform, fibre and support assertions have not all been independently recomputed.

### D. Centered main-term cancellation

The plain recursion describes a difference of two products with equal products of scales, claiming their exceptional-row main terms cancel. This cancellation is not a generic consequence of centering. It requires identical character, mask, norm powers, local extraction factors and lattice densities after both finite transforms. The manuscript expressly recognizes these requirements; the proof must still be checked term by term. The complete-common-support and masked-rectangle lemmas are especially important.

### E. Uniformity in a slot mesh chosen before the slot count

The final construction chooses a fine mesh independent of the number of slots, then chooses a large fixed even K and narrow disjoint prime windows (16196 onward). The plain lemma asserts this uniform mesh; the end of its proof explains aggregate support errors and derivative seminorms. A hidden loss proportional to K in the real exponent could break the parameter order. K-dependent constants and finite height orders are harmless only if they can be absorbed after the target as claimed, while real exponent margins and the mesh must have their specified earlier quantifier order.

### F. All-height tail bounds and late external orders

The late-height lemma6520–6581 is elementary and sound under its stated hypotheses: choose tau small after A_eta, then N large after tau. Its decisive hypothesis is that increasing the final external order changes only external test constants, not retained height exponents or real scale degrees. The long contour/moment machinery must verify that separation at every application. Merely asserting rapid decay without this quantifier discipline is insufficient. This is a verification target, not an identified failure in the inspected statement.

### G. Normalizing the actual same expression

The principal correction is asymptotically normalized by a nonzero `A_T(Z)` of size a fixed power of logZ (15548–15683), while the low and high representations must use the identical physical probe and excluded set. Fixed-ray prime counting is sufficient for that normalizer; a moving-conductor prime theorem would be a different and much stronger input. The inspected argument explicitly says it uses fixed ray counting and permits target-dependent thresholds. The compensated local identities and low estimate still need complete verification to confirm the same expression is being normalized on both sides.

## Recommended review order

1. Extract a self-contained first-stage paper ending with11/12. It already contains a major claim and avoids the new marked/plain recursions.
2. Independently verify the exact reflected identity and unmarked energy against the cited cusp expansions, with a ledger of every unit, mask and normalization.
3. Independently verify the sextic-sieve recursion and the all-height contour/principal/outer-row estimates. Confirm the final1/4800 margin for the actual normalized physical sum.
4. Only after that stage survives, audit every edge of the inverse and plain moment inductions, especially exceptional-row cancellation and uniform slot mesh.
5. Keep the endpoint certificate as a small reproducible exact-rational check; do not let a correct endpoint optimization stand in for the analytic inequalities feeding it.
6. Preserve the precise scope in the title and conclusion: a strict7/8 zero-free half-plane, not RH/GRH or critical-line zero placement.

## Assessment for the parent task

There is a credible, detailed **claimed strategy** here and some well-structured conditional analytic components. After full textual reading I found no justified decisive mathematical refutation, and I did not independently verify the main theorem. The appropriate status is **unverified claimed proof of a major zero-free-half-plane theorem; not a proof of RH/GRH even if correct**. A user-facing answer should not claim this audit establishes the breakthrough, and should not claim it disproves the manuscript merely because the conclusion is currently an open-type problem.

## Additional checks after completion of full textual coverage

The full follow-up included the new canonical-moment fibre measures, source-witness restrictions, fresh independent windows, and clipping gates; the plain induction's complete common-support extraction, off-coprime extensions, shared rectangle profiles, exceptional-row counts, and masked-lattice cancellation; and every remaining bibliography entry. No argument was rejected simply for invoking a global beta_* bound on a zero-free domain to its right, or for using a conditional moment hypothesis with kappa=2beta_*-1. Both are legitimate conditional devices if the stated estimates are correctly proved.

I independently checked six additional canonical-recursion **formal algebra identities** using exact rational coefficient dictionaries in the Python standard library. All residuals were identically zero:

- The F_c transition in `eq:canonical-transition`;
- The M_c transition in that display;
- The first invariant transition F_c−M_c;
- The second invariant transition4F_c−3M_c;
- The prefactor cancellation `kappa_i+lambda_c+C_c+2F_c=F`;
- The second-principal count `kappa_i+H_c+s_i+B+t+ell+R/2=F−B−j`.

These checks confirm selected exponent identities, not the arithmetic transformations producing them, the common-density hypotheses, or all admissibility inequalities. A complete independent verification still needs an explicit per-edge proof ledger and checks against the unconditional source cusp formulas and imported quadratic/cubic family theorems.

The companion review of the new paper sources is recorded in `/tmp/grh-new-papers-review.md`. Both new sources were read completely; they do not present the quasi-sept theorem as a proof of RH.
