#!/usr/bin/env python3
"""Assemble a human mathematical review ledger; do not infer proof correctness.

The notes below record a completed reading of the specified statements, proofs,
and relevant inherited hypotheses. Running this file only refreshes line/hash
metadata and checks the explicitly recorded corrections and kernel artifacts.
It neither performs that reading nor invokes Lean.
"""
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
REVIEW = ROOT / "extension/review"
BASE = "5ad05c809358e1d945a7d2c9d4e4077aeb33ef22"
CLAIM_RE = re.compile(r"\\begin\{(theorem|proposition|lemma|corollary|conjecture|problem)\}(?:\[([^]]*)\])?")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def current_claims(path):
    text = path.read_text()
    result = {}
    for i, m in enumerate(CLAIM_RE.finditer(text), 1):
        end = text.index("\\end{" + m[1] + "}", m.end())
        end += len("\\end{" + m[1] + "}")
        after = text[end:]
        pm = re.match(r"\s*\\begin\{proof\}(?:\[[^]]*\])?", after)
        proof = ""
        proof_lines = None
        if pm:
            pe = after.index("\\end{proof}", pm.end())
            proof = after[pm.end():pe].strip()
            pb = after.index("\\begin{proof}")
            proof_lines = [text[:end + pb].count("\n") + 1,
                           text[:end + pe].count("\n") + 1]
        result[f"{path.stem}.{i:03d}"] = {
            "name": m[2] or "Untitled " + m[1],
            "statement_lines": [text[:m.start()].count("\n") + 1,
                                text[:end].count("\n") + 1],
            "statement_sha256": hashlib.sha256(text[m.start():end].encode()).hexdigest(),
            "proof_lines": proof_lines,
            "proof_sha256": hashlib.sha256(proof.encode()).hexdigest() if pm else None,
            "source_sha256": digest(path),
        }
    return result


# One note for every original claim, in its original environment order. These
# are manual observations; the script checks their inventory, not their truth.
NOTES = {
"foundations": [
    "Checked the normalization embedding, product-ring integrality, and conductor calculation with the stated nodal congruence condition.",
    "Checked conjugation by the positive square root of the metric matrix. Positivity of the metric, rather than an arithmetic analogy, gives real generalized eigenvalues.",
    "Checked the conditional Rouche argument on a small disk. Local uniform convergence and a nonzero holomorphic limit remain explicit assumptions, not established L-function inputs.",
],
"orders": [
    "Checked the common-denominator argument using finite generation and spanning over the fraction field.",
    "Checked construction of the finite stable lattice from generators; the order is finite over the stated base ring.",
    "Checked finite generation, integral containment, and rational spanning of the lattice endomorphism order.",
    "Checked left/right multiplier closure and the denominator bound; sidedness of multiplication is retained.",
    "Checked maximal-ideal localization detects a nonzero quotient class over the stated domain.",
    "Checked that localized inclusions imply global inclusion using the preceding membership argument.",
    "Checked that a lattice map commuting with the smaller order extends over the common rational algebra; no unjustified integral extension is used.",
    "Checked the two matrix-unit constructions and their natural inverses in the displayed Morita equivalence.",
    "Checked nondegeneracy of the specified trace pairing and the dual-lattice identification; this is not an arbitrary degenerate trace form.",
    "Checked determinant scaling of the Gram matrix under the stated full-rank basis change.",
    "Added positive dimension before referring to the shortest nonzero vector. Checked both directions of the quantitative norm/minimum bounds; uniform constants are assumptions.",
    "Checked the involution reverses products and the reduced norm is central in the quaternion algebra before multiplying norms.",
    "Checked that this section explicitly specializes to integer lattices and integral trace on all overorders. The finite quotient bound then follows from the trace dual.",
    "Checked the averaging formula requires the group order to be invertible in the base; equivariance and the lifting property are separate substitutions.",
    "Checked holomorphic group maps lift to complex-linear maps on universal covers and preserve the period lattice; the converse descends.",
    "Checked the scalar stabilizer dichotomy in the two-dimensional rational lattice space; standard complex-torus background is used as stated.",
    "Checked the quadratic-order conductor form and uniqueness under the fixed quadratic integer ring.",
    "Checked the action is restricted to invertible ideal classes and the stated lattice class set; noninvertible ideals are not silently included in a torsor.",
    "Checked the Frobenius order argument under ordinarity. The ordinary endomorphism-algebra classification and Frobenius facts remain cited background.",
    "Checked prime-to-characteristic torsion faithfulness using the degree bound for a nonzero isogeny; characteristic-p torsion is not substituted.",
    "Checked the extension of a right-ideal endomorphism to the rational quaternion algebra and its identification as left multiplication.",
    "Checked the algebraic degree multiplication deduction from the explicitly supplied dual-isogeny identities; those identities are not proved by the deduction.",
    "Checked the centralizer matrix equations over the stated ring and the resulting Gaussian-order form.",
    "Checked the trace-pairing matrix and the dual basis for the Gaussian suborder; the conductor parameter is retained in the denominator.",
],
"complexes": [
    "Checked torsion-freeness and finite generation of an extension with the stated module actions.",
    "Checked the split Grothendieck-group universal property against the required direct-sum relation.",
    "Checked the stabilization description of equality in the group completion; cancellation is not assumed without stabilization.",
    "Checked both short exact sequences are admissible in the chosen exact structure before the Euler relation is formed.",
    "Checked the bounded-end induction splitting an acyclic complex of projectives; boundedness is essential.",
    "Checked the pullback construction and two split projections used in Schanuel's lemma.",
    "Checked finite presentation by a free order module and that its kernel is a lattice under the chapter's ring hypotheses.",
    "Checked the denominator-cleared embedding in a free module; it uses the specified rational-algebra setting.",
    "Checked the corollary uses the two preceding lattice presentation/embedding statements with their inherited hypotheses.",
    "Checked positive definiteness of the weight matrices gives the Gram-kernel intersection and hence its rank formula.",
    "Checked image containment, rank-nullity, and the three cohomology dimensions; two exact rank components have separate Lean support.",
    "Checked cancellation of the adjacent ranks in the alternating dimension sum. The Lean arithmetic identity covers only the final substitution.",
    "Checked compatible bases splitting image, homology complement, and a preimage complement; this is a field argument.",
    "Checked the fixed-rank parameter count with the image-in-kernel condition and the rank-feasibility inequalities.",
    "Checked the derivative BA'+B'A and the kernel/rank calculation at the stated normal form.",
    "Checked the transverse block directions against the tangent equation, without identifying every first-order direction with an actual deformation.",
    "Checked the Jacobian of x dot y in four coordinates, smoothness away from the origin, and the singular origin.",
    "Checked graded signs in the endomorphism differential and d squared equals zero from the underlying complex relation.",
    "Checked the coefficient of the second-order deformation equation; the cohomology class is an obstruction rather than a universal existence theorem.",
    "Checked row and column elimination at a unit pivot and the induced smaller zero-composite relation over the stated ring.",
    "Reviewed the statement's rank and ideal-grade hypotheses and citation. The general Buchsbaum--Eisenbud proof is external, not independently reconstructed here.",
    "Checked the regular-sequence argument for the two-generator Koszul complex, including the use of each non-zero-divisor condition.",
    "Checked that tensoring preserves the exact sequences under flatness; arbitrary nonflat base change is excluded.",
    "Checked wedge/contraction expansion and signs on decomposable exterior tensors.",
    "Checked selection of a vector pairing to one with a nonzero covector and the resulting contracting homotopy. Lean covers the abstract middle-exactness consequence only.",
    "Checked the finite-dimensional orthogonal decompositions and harmonic/cohomology identification; no infinite-dimensional closed-range conclusion is inferred.",
    "Reviewed the elliptic-complex and compactness hypotheses and attribution. The Atiyah--Singer index theorem is external, not a local proof.",
    "Checked the curvature computation d_A squared equals bracket with curvature using the specified conventions.",
    "Checked the self-dual projection makes the composite vanish at an anti-self-dual connection.",
    "Checked injectivity and image/kernel equality of the nonzero-covector ASD symbol sequence; this does not supply a spectral lower bound.",
],
"standard-monomials": [
    "Checked alternating relations give spanning and the determinant coefficient maps give independence over the stated commutative ring.",
    "Checked row/column index conventions and the Cauchy--Binet expansion via exterior powers.",
    "Checked shuffle signs and that the identities use no division, so they remain valid over the stated ring.",
    "Checked the contraction/creation identity and the chosen unit pairing; abstract homotopy-to-exactness is now separately formalized.",
    "Reviewed the integral Schur basis statement and its hypotheses. The general ABW basis theorem remains external; elementary cases are proved separately.",
    "Checked the one-row, one-column, and elementary mixed Schur identifications with the chapter's convention.",
    "Checked characteristic zero and positive tensor degree d, the averaging projector, and inherited contracting homotopy. The d=0 exception is excluded explicitly.",
    "Checked rank-one straightening termination and independence by leading monomials in the specified polynomial parameterization.",
    "Checked the three-term two-row minor relation by expansion, including the corrected cancellation monomials.",
    "Checked the ordered straightening measure decreases and distinct standard tableaux have distinct diagonal leading monomials.",
    "Checked the quadric relation, its basis, and the characteristic-zero representation calculation for the basic two-arrow complex.",
    "Checked the complemented middle partition and dual-action convention in the bihomogeneous Schur decomposition.",
    "Reviewed the general complex standard-basis/reducedness/normality/Cohen--Macaulay hypotheses and citations. These general source theorems are external.",
    "Checked orbit classification by adjacent ranks, feasible degeneration to smaller ranks, and the stabilizer/parameter dimension calculation.",
    "Reviewed the filtration and characteristic-zero splitting assumptions, endpoint zero-map conventions, and all-vertex Schur weights. The general filtration theorem is external.",
    "Added the empty-poset case A=k with trivial family k[t]. Checked the positive weight separation and standard-monomial freeness argument for nonempty P.",
    "Checked that diagonal leading terms of the two-row minors generate the initial algebra using the established standard basis.",
    "Checked the prefix inequalities characterize the paired column semigroup and total-degree equality belongs to its lattice.",
    "Checked normality is proved inside the common fraction field, with integral inequalities on the specified exponent lattice.",
    "Checked the explicit monomial-basis flatness statement and distinct special fibers; flatness alone is not used to transfer every geometric property.",
],
"gentle-invariants": [
    "Checked the rank-normal-form decomposition into the displayed indecomposable modules of the two-arrow relation.",
    "Checked the numerical consequence uses the complete decomposition and includes zero ranks/endpoints.",
    "Checked the extension complex, linearized relation, and infinitesimal base-change signs; its cohomology is not conflated with a nonlinear moduli space.",
    "Checked both character weights in the two-factor semi-invariant test under the fixed action convention.",
    "Checked the corrected explicit generator semigroup, relations, and exponent pairing; the cited source overstatement is not retained as a theorem.",
    "Checked the exterior-power trace expansion of det(I-tT), with finite-dimensional conventions.",
    "Checked determinant cancellation through invariant boundary and cycle subspaces; the cohomology factors are finite and the operator commutes with the differential.",
],
"cryptography": [
    "Checked the cyclic hidden-kernel relation and exact coset fibers under the stated order assumption.",
    "Checked character-sum cancellation by multiplication with a nontrivial character value.",
    "Checked the Fourier amplitude normalization and uniform annihilator support; this is an ideal finite distribution, not a resource advantage claim.",
    "Checked the displayed relation-lattice basis, determinant/covolume, and correspondence with the modular kernel.",
    "Checked the transpose-inverse basis formula. Added n>=1 to the preceding shortest-vector definition; the basis formula itself also makes sense in dimension zero.",
    "Checked integer unimodularity, inverse, and the growing norm of the second basis vector. Exact finite components have Lean proofs; the limiting operator-norm claim is prose mathematics.",
    "Checked every error term in the noisy cancellation identity and the separate radius condition for decoding.",
    "Checked the deterministic triangle/Cauchy bound with the stated selector coefficients; the narrower Lean binary-selector result is not identified with the whole bound.",
    "Checked CRT/product decomposition componentwise. Existence, security, and cost of hypothetical recovery algorithms are not supplied by this algebra.",
],
"quantum-surfaces": [
    "Checked permutation-cycle counts and subdivision/Euler characteristic; the closed oriented connected surface classification is background.",
    "Checked the clean degree-four elliptic dessin and its genus; the contracted one-vertex example is not a positive-gap code example.",
    "Checked binary incidence orthogonality gives Pauli stabilizer commutation; this uses mod-two phases rather than real incidence signs.",
    "Checked connected primal and dual incidence ranks and the code-dimension count. Lean covers only the final integer Euler substitution.",
    "Checked the primal/dual noncontractible cycle bounds for the rectangular periodic cellulation under its stated size conditions.",
    "Checked the uniform rowspace state's star and face stabilizers and its selected logical sector.",
    "Checked the RREF preparation circuit generates the stated independent-row superposition; column/pivot conventions are preserved.",
    "Added a nonloop edge hypothesis to the connected closed oriented cellulation. Checked even excitation parity gives the lower bound two and the edge Pauli achieves it in the specified projector normalization.",
    "Checked the exact star-correlator product identity and the defined four-parameter local ansatz; the formula supplies an efficient classical reference.",
],
"gauge-theory": [
    "Checked curvature as the failure of the covariant differential to square to zero, with the same bracket/sign convention as the complex chapter.",
    "Checked first and second variations under the stated smooth/compact assumptions and separation of the curvature and quadratic terms.",
    "Checked the self-dual/anti-self-dual energy split and topological normalization for the classical bound; this is not a quantum mass-gap proof.",
    "Checked the explicit nonzero-covector ASD symbol sequence and its dimension/rank calculation.",
    "Reviewed the external AHS formula with connected closed oriented four-manifold and the bundle hypotheses. The full index theorem remains external.",
    "Checked the finite exact family has arbitrarily small positive singular value while its exactness persists.",
    "Checked normalized Haar integration on a finite lattice, positivity/finiteness of the partition function, and link gauge invariance.",
    "Made rho explicitly a unitary representation, essential for positive-type closure; checked beta>=0, convergent exponential expansion, and positive tensor-power coefficients. Fixed a stray exponent comma.",
    "Checked Cauchy--Schwarz for a positive semidefinite form, null-vector orthogonality, and well-defined positive quotient.",
    "Checked both directions of the spectral gap/Euclidean semigroup decay equivalence using the spectral theorem and the stated unique normalized vacuum.",
    "Checked the elementary spectral models share the claimed ultraviolet leading behavior while differing at the low spectral edge.",
    "Checked the norm limit argument assumes common positive gap and strong convergence of both semigroups and vacuum projectors; those uniform inputs are not built for Yang--Mills here.",
    "Checked iteration of the nonnegative contractive recurrence and its explicit error bound; no physical renormalization recurrence is asserted.",
    "Checked the opposite/dual action and pairing identity with the module's handedness fixed.",
],
"character-bridge": [
    "Checked exactness after the specified localization and the exceptional fiber calculation; universal parameters are not substituted across excluded denominators.",
    "Checked the finite positive Laplacian and quantitative contracting homotopy on the stated complement; the norm bound uses the supplied positive eigenvalue.",
    "Checked pullback of the supplied character/representation along the specified algebraic map; no unconstructed analytic L-function bridge is inferred.",
],
"synthesis": [
    "Checked the displayed periodic differentials compose to zero and their images equal the next kernels.",
    "Checked the explicit derived obstruction and its nonvanishing in the stated cohomology class.",
    "Checked the finite exactness and metric-gap computation for the explicitly displayed family.",
    "Checked transport of coercivity requires a positive lower bound for the transport map; uniformity is an additional assumption.",
    "Specified V=W=R and j>=1 in the shrinking transport counterexample, so the nonzero-space Rayleigh quotient and index range are explicit.",
],
"source-concordance": [
    "Checked the F8/F2 counterexample to a pure-cubic claim, trace-zero depressed cubic, nonzero linear coefficient, and inverse formula using irreducibility.",
],
}

FINDINGS = [
    ("SP-001", "orders.011", "orders.tex", "missing dimension hypothesis",
     "Shortest nonzero vectors are undefined for a zero-dimensional lattice.",
     "Added dim V>0 to the metric-transport proposition.", r"real inner-product spaces with $\dim V>0$"),
    ("SP-002", "quantum-surfaces.008", "quantum-surfaces.tex", "missing cellulation hypothesis",
     "The earlier contracted one-vertex/one-face dessin has trivial checks and no positive eigenvalue; the upper-bound proof needs a nonloop edge.",
     "Required a connected closed oriented cellulation with an edge having distinct endpoints; explicitly retained the four simulated families.", "with distinct endpoints, the smallest positive eigenvalue"),
    ("SP-003", "gauge-theory.008", "gauge-theory.tex", "representation type hypothesis",
     "A unitary-valued function need not be a representation, and its character need not be positive type.",
     "Changed unitary to unitary representation in the theorem.", r"be a unitary representation"),
    ("SP-004", "gauge-theory.008", "gauge-theory.tex", "formula typography",
     "A stray comma appeared inside the conjugate-character exponent.",
     "Removed the comma, leaving the intended integer power.", r"\overline{\chi(g)}^{b}"),
    ("SP-005", None, "gauge-theory.tex", "prose typography",
     "A stray plus sign interrupted the analytic continuation sentence.",
     "Changed continuation,+and to continuation, and.", "continuation, and"),
    ("SP-006", "standard-monomials.016", "standard-monomials.tex", "empty-object proof case",
     "The weight construction took a maximum over the finite poset, which is undefined when it is empty.",
     "Handled the empty poset by A=k and the trivial flat family k[t] before the nonempty construction.", r"If \(P\) is empty"),
    ("SP-007", "cryptography.005", "cryptography.tex", "definition domain precision",
     "The preceding first-minimum definition needs positive lattice dimension, although the dual-basis formula itself does not.",
     "Added n>=1 only to the first-minimum sentence.", r"and, for $n\ge1$, its first minimum is"),
    ("SP-008", "synthesis.005", "synthesis.tex", "counterexample domain precision",
     "A shrinking Rayleigh-quotient example needs a nonzero space and a positive sequence index.",
     "Specified V=W=R and j>=1.", r"On $V=W=\mathbb R$, with $j\ge1$"),
]

SUPPLEMENTAL = {
"tensor-grammars": [
    "Checked finite sum definitions of composition, tensor product, contraction, and dagger with typed ports; this is a finite-dimensional interpretation.",
    "Checked the basis cup/cap contraction and closed-loop scalar dim H with the stated dual/conjugate conventions.",
    "Checked signed permutation averaging is an idempotent self-adjoint projector and its rank is the exterior dimension, including r above dim H.",
    "Checked exterior functoriality and the specified-index Cauchy--Binet coefficient identity.",
    "Checked the traceless-Hermitian normalization Tr(Ta Tb)=delta_ab/2, matrix-unit coefficient comparison, and Casimir contraction.",
    "Required and rechecked complex linearity. Checked Choi positivity, Kraus reconstruction, trace preservation, and the partial-trace transpose convention.",
    "Checked typed one-hole context induction and finite rewrite induction; probability consequences now explicitly apply to unitary circuit interpretations. Lean covers the sequential fragment only.",
    "Checked decreasing gate count and telescoping operator error, then the factor-two probability bound for normalized vectors.",
    "Checked zero composition, kernel/image quotient transport, and finite Hodge conjugacy under unitarity; invertibility alone does not imply spectral equality.",
    "Checked acyclic identity-block enlargement and added eigenvalue multiplicity dim W in each affected degree. The following gap-decrease example now requires W nonzero.",
    "Checked derivation-tree bags and vertex connectedness under distinct interfaces, fresh internal vertices, and no extra identifications.",
    "Rechecked the corrected six-port grammar with distinct attachments and separator edges. Its erased yield is a^n b^n c^n; the pumping and erasing-homomorphism arguments establish both non-context-free assertions.",
    "Checked a finite Turing transition table is simulated by local path rewrites and effective finite derivation enumeration gives the reverse recursively-enumerable inclusion.",
    "Checked bottom-up finite contraction cost O(m D^q) counts actual index variables/interfaces and a fixed grammar's bounded number of factors, not graph width alone.",
],
"learning-languages": [
    "Checked exact integer balance, binary error-state recurrence, acceptance indicator, and O(log L) bit length. Temporary ReLU values need not be binary; wording now refers only to the other recurrent state variable.",
    "Checked distinguishable prefixes prove nonregularity for deterministic automata; the text now explicitly invokes finite-subset determinization for nondeterministic automata.",
    "Checked the ReLU pattern indicators on Boolean inputs and their disjoint sum represent any finite Boolean mechanism, without an efficiency claim.",
    "Checked acyclic composition and the Boolean intervention multiplexer. The same exogenous assignment is held fixed for the structural counterfactual; mechanisms are supplied, not identified from observations.",
    "Checked both observational distributions and their different do(X=0) laws. The impossibility is identification from the specified observational law, not inability of any architecture to compute a supplied mechanism.",
    "Checked soundness is pathwise for every finite accepted sequence of certified rewrites and independent of a possibly history-dependent rule-selection policy.",
    "Checked the exponentially tilted variance bound by 1/4 and Taylor integration for all real lambda, including negative lambda.",
    "Added and rechecked K,m>=1. Checked iid evaluation independent of fixed candidates, exponential Markov/union bounds, the 1-X lower-tail argument, and the empirical-minimizer 2-epsilon risk bound.",
],
"cyclic-cosmology": [
    "Checked torsion-free metric compatibility gives the conformal connection formula, the null geodesic rescaling, and its converse. The conformal factor is smooth, finite, and strictly positive on the stated domain; the singular crossover is excluded.",
    "Checked p-form and volume scaling in arbitrary signature, wedge nondegeneracy, and source-free Maxwell invariance for n=4,p=2. Detector energy, charged matter, and boundary regularity are separate assumptions.",
    "Checked the four simple branch points, two unbranched points at infinity, connectedness, Euler characteristic, and nonvanishing differential in all charts. The real expanding branch and coefficient-field extension qualifications are explicit; a repeated-root quartic is excluded.",
    "Checked symmetric spinor contraction annihilates the symmetrized derivative, divergence plus complex self-duality implies closedness, and Stokes gives equality for the bounding oriented piecewise-smooth chain with smooth fields. This is conditional on the two displayed field equations.",
    "Checked nonnegative finite relative entropy, both mutual-information chain rules, and the conditional Markov version. No sender or end-to-end physical channel is constructed by the inequality.",
    "Checked the signed variation decomposition, stochastic-kernel contraction, and exact 1/K success bound for observationally identical equally likely messages, including abstention.",
    "Checked the finite alphabet entropy bound and conditional-error decomposition for Fano's inequality. Independent decoder randomization can be adjoined without changing message mutual information.",
    "Checked positive/negative parts of a Hermitian difference and trace preservation give trace-norm contraction; zero trace and 0<=E<=I give the measurement bound. Complete positivity is not needed for this particular conclusion.",
    "Checked the two-state trace-distance formula and strict increase under tensor squaring for overlap strictly between zero and one; deterministic channel contraction excludes the proposed cloning map.",
    "Checked the Kraus completeness relation, rectangular trace cycling, and equality against all observables imply equal reduced states after an unconditioned local operation.",
    "Checked Gaussian diagonalization, quadratic mean/variance, linear variance, and vanishing third-moment cross term. Replaced the misleading word centered for the noncentered chi-square sum.",
    "Checked nonzero fixed template and known positive covariance give a strictly convex scalar likelihood, inverse-information variance, and normalized score law. Data-driven template selection is treated separately.",
    "Checked exchangeability gives a uniform descending rank without ties and counting the entire tied block gives a conservative p-value. A fitted-parametric bootstrap is not asserted automatically exact.",
    "Checked isotropic harmonic covariance plus Gaussianity gives independent real coefficients and variance 2 C_l^2/(2l+1). The argument uses the standard irreducibility of a fixed-degree spherical-harmonic space; masked-sky estimators are excluded.",
    "Checked full-column-rank nuisance design, whitening, orthogonal projection, and the Schur-complement information. Vanishing exactly characterizes template confounding; the variance assertion requires positive remaining information.",
    "Reviewed as an explicitly open end-to-end physical/inference problem, not a proved theorem. Required crossover solutions, identifiable source laws, calibrated observables, and encoding comparisons remain tasks.",
],
"quantum-toricgt": [
    "Checked finite backward induction, existence of outgoing choices, attainment, and termination on the ordered DAG. Negative edge costs do not invalidate the recursion because directed cycles are absent.",
    "Checked the edge-potential inequalities telescope to a lower bound, equality certifies a legal path, and Bellman potentials attain it. Prediction accuracy and certification/repair success remain distinct.",
    "Added and rechecked distinct source and target. Checked extraction of one positive integral path, subtraction, and absence of any remaining nonnegative zero-boundary DAG circulation.",
    "Checked all weak-duality inequality signs: z<=0 reverses the H constraint, u<=0 uses x<=1, and x>=0 permits multiplication of the coordinate dual bound. Equality certifies only the specified feasible instance.",
    "Checked the backward cyclic shift gives VU=omega UV, the nontrivial character sum vanishes, and q^2 nonzero orthogonal Weyl matrices form the matrix basis. Rational phase does not mean rational matrix entries.",
    "Checked unitary gate normalization, Hermitian observables for real/imaginary Weyl expectations, feature range, and the two-term norm perturbation bound. Separate preparations can be needed for noncommuting observables; the reported model uses exact simulated expectations.",
    "Checked the Pauli exponential expansion, real sinusoidal expectation, and plus/minus pi/2 shift rule for one gate occurrence. The full nonlinear loss is not assigned this two-evaluation rule.",
    "Checked the multivariable chain rule with independently named occurrences, summation over shared offsets/tokens, and original-feature classical adjoints. Reused input angles need both occurrence contributions; max-plus ties do not have a unique derivative in general.",
    "Checked finite maxima can be reordered and regrouped, with max(empty)=-infinity explicitly set. The conclusion applies to fixed score/value contractions, not to the whole nonlinear network.",
    "Checked token permutation through feature maps, row operations, two-sided score permutation, soft/max attention, and separately normalized dispatch/combination. Endpoint renaming preserves equality data; byte attributes and padding masks must be transported.",
    "Checked grouping by equal Laurent exponent gives the full binomial kernel and path incidence telescopes. The grading incidence convention is separated from the opposite flow convention before the following proof.",
    "Checked zero-boundary integral rewrites plus explicit nonnegativity preserve the unit-flow constraint and hence a legal path only under the ordered-DAG hypotheses. Cost change is exactly the linear functional of the rewrite.",
    "Checked the strict affine margin bound, its Cauchy--Schwarz sufficient condition, and constant-score case. A nonlinear encoder can have a disconnected/nonpolyhedral inverse image of a feature-space region.",
    "Checked each independent offset occurs in one Pauli gate, whose derivative norm is 1/2; telescoping unitary products gives the l1 state bound and six expectation bounds give the sqrt(6) feature bound. Token inputs and the encoder are held fixed.",
    "Checked the generated even-sum lattice, explicit even/odd nonnegative decompositions, and saturation relative to that lattice. The point (1,0) is outside the group and is not a saturation hole there.",
    "Checked the triangle boundary matrix has rank two and kernel span(1,1,1); the filled triangle adds that image. The point/boundary/fill inclusions give first Betti numbers 0,1,0, disproving both unqualified monotonicity directions.",
    "Checked nonempty feasible basis set, a normalized initial vector, and unitaries commuting with its projector imply subspace preservation and probability-one feasibility. The diagonal cost expectation is a convex average, and a positive nonoptimal cost gap gives the stated probability bound. This is a conditional future interface, explicitly not the trained three-qubit feature circuit.",
],
}


def main():
    baseline = json.loads(subprocess.check_output(
        ["git", "show", BASE + ":extension/review/claim-register.json"], cwd=ROOT))
    base_sources = {s["path"]: s["sha256"] for s in baseline["source_files"]}
    current = {}
    for source in {c["source_file"] for c in baseline["claims"]}:
        current.update(current_claims(ROOT / source))
    notes = {f"{chapter}.{i:03d}": note
             for chapter, values in NOTES.items() for i, note in enumerate(values, 1)}
    assert set(notes) == {c["id"] for c in baseline["claims"]}
    corrections = []
    by_claim = {}
    for fid, cid, name, severity, issue, fix, marker in FINDINGS:
        path = ROOT / "extension/manuscript/chapters" / name
        assert marker in path.read_text(), (fid, marker)
        corrections.append({"id": fid, "claim": cid,
            "source_file": str(path.relative_to(ROOT)), "category": severity,
            "issue": issue, "correction": fix,
            "status": "applied_and_rechecked", "post_correction_source_sha256": digest(path)})
        if cid:
            by_claim.setdefault(cid, []).append(fid)
    claims = []
    for old in baseline["claims"]:
        cid = old["id"]
        status = ("reviewed_external_statement" if old["status"] == "external_cited"
                  else "reviewed_conditional_argument" if old["status"] == "conditional_local_argument"
                  else "reviewed_local_argument")
        claims.append({"id": cid, "name": old["display_name"],
            "source_file": old["source_file"],
            "base_snapshot": {"commit": BASE,
                "source_sha256": base_sources[old["source_file"]],
                "statement_lines": [old["start_line"], old["end_line"]],
                "proof_lines": [old["local_proof_start_line"], old["local_proof_end_line"]]
                    if old["local_proof_environment_present"] else None},
            "reviewed_snapshot": current[cid],
            "status": status,
            "findings_resolved": by_claim.get(cid, []),
            "manual_review_note": notes[cid],
            "whole_statement_kernel_verified": False})
    supplementary = []
    for chapter, chapter_notes in SUPPLEMENTAL.items():
        path = ROOT / "extension/manuscript/chapters" / (chapter + ".tex")
        cc = current_claims(path)
        assert len(cc) == len(chapter_notes), chapter
        for i, note in enumerate(chapter_notes, 1):
            cid = f"{chapter}.{i:03d}"
            supplementary.append({"id": cid, "source_file": str(path.relative_to(ROOT)),
                **cc[cid], "status": "reviewed_local_argument" if cc[cid]["proof_lines"] else "reviewed_open_problem",
                "manual_review_note": note,
                "whole_statement_kernel_verified": False})
    cosmology = (ROOT / "extension/manuscript/chapters/cyclic-cosmology.tex").read_text()
    assert "For jointly centered Gaussian vectors" in cosmology
    assert "oriented piecewise-smooth three-chain" in cosmology
    assert "quadratic term arising from $z$" in cosmology
    kernel_path = REVIEW / "second-pass-math-audit-core-kernel.json"
    kernel = json.loads(kernel_path.read_text())
    assert sum(r["theorem_count"] for r in kernel["records"]) == 48
    for r in kernel["records"]:
        assert r["exit_code"] == 0
        assert digest(ROOT / "extension/lean" / r["source_file"]) == r["source_sha256"]
        assert all("sorryAx" not in axioms for axioms in r["axioms_per_theorem"].values())
    supplementary_counts = Counter(Path(c["source_file"]).stem for c in supplementary)
    supplementary_proofs = sum(c["proof_lines"] is not None for c in supplementary)
    supplementary_open = sum(c["status"] == "reviewed_open_problem" for c in supplementary)
    data = {
        "schema_version": 2,
        "assembled_at_utc": datetime.now(timezone.utc).isoformat(),
        "reviewer": "orders_volume_one independent mathematical second pass",
        "scope": f"Read all 125 original numbered statements, their 119 attached proofs, and relevant inherited hypotheses; separately reviewed {len(supplementary)} new environments ({supplementary_proofs} arguments and {supplementary_open} open problem). This is content and proof review, not universal correctness certification.",
        "base_commit": BASE,
        "method": "Manual mathematical reading; the assembler refreshes only source metadata and checks recorded correction markers and existing actual kernel records.",
        "counts": {"original_claims_reviewed": len(claims),
                   "original_attached_proofs": 119,
                   "original_external_statements": 6,
                   "by_original_review_status": dict(Counter(c["status"] for c in claims)),
                   "resolved_old_chapter_findings": len(corrections),
                   "supplemental_new_claims_reviewed": len(supplementary),
                   "supplemental_by_chapter": dict(supplementary_counts),
                   "freshly_kernel_checked_declarations": 48},
        "limits": [
            "No claim that every assertion in prose, every theorem in a cited source, or all inherited upstream files has been independently proved.",
            "Six original general theorems remain cited external results; their statements and use were reviewed, not their full original source proofs reconstructed.",
            "Empirical/source-attribution assessment of the Chomsky and language-model literature belongs to the separate root research review.",
            "Experiment implementation audits, figure rendering, measured training results, and browser checks have separate records; this ledger records mathematical reading rather than independently rerunning those experiments.",
            "Cosmology source attribution and synthetic-code verification are separate from this mathematical review. The missing centered-Gaussian hypothesis in the conditional-polarization formula was corrected by root and independently rechecked.",
            "No complete composite manuscript environment is marked as kernel formalized. The claim register records narrowly typed partial components.",
            "The Lean syntax covers typed sequential composition and one-hole contexts. It does not implement a full symmetric monoidal/traced/dagger graph syntax, channels, graph isotopy, parser correctness, completeness, or confluence.",
            "No proof of GRH, a Yang--Mills mass gap, quantum computational advantage, or observational cosmological communication is asserted.",
        ],
        "findings": corrections, "claims": claims,
        "supplemental_new_chapters": supplementary,
        "additional_prose_checks": [
            "Centered joint Gaussian hypothesis added to the conditional polarization formula; original formula would be false with arbitrary nonzero means.",
            "Predictive codelength gain checked as C0-C1=sum log2(q1/q0), with a separately subtracted artifact cost B. Positive observed-symbol probabilities and normalized distributions are explicit.",
            "The tiny graph binomial example eliminates z_c=z_a z_b and gives the stated unit-flow interval and affine cost wall. Abelianized boundary invariance does not preserve arbitrary extra trajectory semantics.",
        ],
        "kernel_verification": {"record_file": str(kernel_path.relative_to(ROOT)),
            "record_sha256": digest(kernel_path),
            "log_file": "extension/review/second-pass-math-audit-core-kernel.log",
            "log_sha256": digest(REVIEW / "second-pass-math-audit-core-kernel.log"),
            "lean_version": "4.24.0",
            "mathlib_commit": "f897ebcf72cd16f89ab4577d0c826cd14afaafc7",
            "modules": [{k: r[k] for k in ("source_file", "source_sha256", "exit_code", "theorem_count", "elapsed_seconds")}
                        for r in kernel["records"]],
            "project_axioms_or_admitted_proofs": False,
            "foundational_axioms": ["propext", "Quot.sound", "Classical.choice"],
            "new_module_manifest": "extension/lean/diagram-verification.json"},
    }
    (REVIEW / "second-pass-math-audit.json").write_text(json.dumps(data, indent=2) + "\n")
    patch_paths = sorted({r["source_file"] for r in corrections})
    diff = subprocess.check_output(["git", "diff", BASE, "--", *patch_paths], cwd=ROOT)
    (REVIEW / "second-pass-math-audit.patch").write_bytes(diff)
    lines = ["# Independent second-pass mathematical audit", "",
        "The review read **all 125 original numbered statements**, their **119 attached proofs**, and the relevant inherited hypotheses. Six general results remain cited external theorems. "
        + f"It also read **{len(supplementary)} new environments**: {supplementary_proofs} arguments and {supplementary_open} open problem, across the tensor, learning/language, cosmology, and quantum ToricGT chapters. No whole composite environment is represented as fully Lean-formalized.", "",
        "The original inventory is tied to commit `" + BASE + "`. The JSON preserves original line/hash metadata and the reviewed post-correction snapshots. The accompanying assembler does not conduct mathematical review or run Lean; its notes record the manual reading, and its checks refresh provenance.", "",
        "## Resolved corrections", "", "| ID | Claim / location | Issue and correction |", "|---|---|---|"]
    for f in corrections:
        lines.append(f"| {f['id']} | {f['claim'] or Path(f['source_file']).name} | {f['issue']} {f['correction']} |")
    lines += ["", "The exact six-file source patch is `second-pass-math-audit.patch`. The findings above were applied and rechecked. No further proof failure requiring redesign was found in this reviewed scope; that statement is a review outcome, not a formal completeness claim.", "",
        "## Original per-claim coverage", "", "| Claim | Review | Checked point / limit |", "|---|---|---|"]
    for c in claims:
        status = c["status"].replace("reviewed_", "").replace("_", " ")
        fixed = " Resolved: " + ", ".join(c["findings_resolved"]) + "." if c["findings_resolved"] else ""
        lines.append(f"| {c['id']} | {status} | {c['manual_review_note']}{fixed} |")
    lines += ["", "## New chapter mathematical review", "",
        "The corrected tensor/learning snapshots explicitly add complex linearity to the Choi theorem, unitary scope to measurement probabilities, the identity-block eigenvalue multiplicity and nonzero-W condition, distinct-port separator gluing and erasure in the HR example, positive candidate/sample counts, and the correct lower-tail reduction. The cosmology review added a missing centering hypothesis to the conditional Gaussian formula and clarified the Stokes chain and quadratic-term wording; root applied all three and this review rechecked them. Empirical literature attribution is a separate review.", "",
        "| Claim | Checked point / limit |", "|---|---|"]
    for c in supplementary:
        lines.append(f"| {c['id']} | {c['manual_review_note']} |")
    lines += ["", "## Actual Lean verification", "",
        "All three current modules were freshly passed to the Lean 4.24.0 kernel in the pinned mathlib environment. Each command exited zero. The raw output and command metadata are retained in `second-pass-math-audit-core-kernel.log` and `.json`.", "",
        "| Module | Named declarations | Result |", "|---|---:|---|"]
    for r in kernel["records"]:
        lines.append(f"| {r['source_file']} | {r['theorem_count']} | Kernel exit 0; source hash retained |")
    lines += ["", "The new 16 declarations cover contextual soundness of a typed sequential syntax, structural/inverse-equivalence rewrite rules, tensor/trace identities as separate finite-matrix components, chain/exactness transport, contracting-homotopy exactness, and finite Hodge-matrix conjugacy. The dependency logs report only `propext`, `Quot.sound`, and, for some results, `Classical.choice`; no project axiom or admitted proof occurs. These foundational axioms are not described as absent.", "",
        "`build_claim_register.py` now checks source hashes, declaration inventories, raw axiom logs, and exact label-based component mappings for the third module. Its inventory run does not itself invoke Lean. The new module prints its full kernel types, preserving implicit section parameters in the register.", "",
        "## Remaining scope boundaries", ""]
    lines.extend("- " + s for s in data["limits"])
    lines += ["", "The review is reproducible as a provenance record by running `python3 extension/review/second-pass-math-audit.py`. Re-running that assembler does not replace human mathematical review after a substantive source change.", ""]
    (REVIEW / "second-pass-math-audit.md").write_text("\n".join(lines))
    print(json.dumps(data["counts"], indent=2))


if __name__ == "__main__":
    main()
