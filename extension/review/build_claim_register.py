#!/usr/bin/env python3
"""Inventory manuscript claim environments; never modify the manuscript.

The manual annotations classify source evidence, not theorem truth.
Lean verification manifests remain authoritative; this script audits unchanged
sources and records only explicitly reviewed, partial type correspondences.
"""

from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import tomllib


PROJECT = Path(__file__).resolve().parents[2]
MANUSCRIPT = PROJECT / "extension/manuscript"
REVIEW = PROJECT / "extension/review"
LEAN = PROJECT / "extension/lean"
KINDS = ("theorem", "proposition", "lemma", "corollary", "conjecture", "problem")
CLAIM_RE = re.compile(
    r"\\begin\{(" + "|".join(KINDS) + r")\}(?:\[([^]]*)\])?"
)
CITE_RE = re.compile(r"\\cite[a-zA-Z]*(?:\[[^]]*\])*\{([^}]+)\}")

EXTERNAL = {
    "complexes.021": (
        ["v2BE1973"],
        "Buchsbaum--Eisenbud exactness criterion is cited, not proved locally.",
    ),
    "complexes.027": (
        ["v2AS1968I"],
        "Analytic/topological index equality is an external theorem.",
    ),
    "standard-monomials.005": (
        ["smtABW1982"],
        "The general integral Schur basis theorem is cited immediately before "
        "the environment; the elementary special cases have separate proofs.",
    ),
    "standard-monomials.013": (
        ["v2DEP1982", "v2DS1981"],
        "The general complex standard basis, reducedness, normality, and "
        "Cohen--Macaulay assertions are external results.",
    ),
    "standard-monomials.015": (
        ["v2DS1981", "smtCW2011"],
        "The general Schur filtration is external; the characteristic-zero "
        "representation splitting and convention checks are explained locally.",
    ),
    "gauge-theory.005": (
        ["AHS1978"],
        "The AHS index formula is external. The current statement explicitly "
        "assumes connectedness; a separate symbol calculation is proved locally.",
    ),
}

CONDITIONAL = {
    "foundations.003":
        "Proves a zero-location transfer assuming local uniform convergence "
        "and a nonzero holomorphic limit. It does not establish these "
        "hypotheses for an L-function; Rouche's theorem is named background.",
    "orders.011":
        "A metric transport criterion assuming two-sided quantitative norm "
        "bounds. It does not construct bounds uniform in an arithmetic family.",
    "orders.022":
        "Derives degree multiplicativity from explicitly assumed dual-isogeny "
        "identities. It is not a proof of those duality identities.",
    "gauge-theory.012":
        "Assumes the preceding strong semigroup/projector convergence and "
        "a common positive gap bound. It does not construct these data for "
        "the continuum Yang--Mills limit.",
    "synthesis.004":
        "Transports an already supplied coercivity bound through an isomorphism "
        "with an already supplied positive lower singular-value bound.",
}

NOTES = {
    "foundations.002":
        "The positive-pencil statement is proved. No identification with an "
        "arithmetic L-function is supplied by this proposition.",
    "orders.019":
        "The local argument uses the separately cited classification of "
        "ordinary elliptic-curve endomorphism algebras and standard Frobenius "
        "facts; it does not reprove that classification.",
    "complexes.004":
        "Both short exact sequences must be admissible in the chosen exact "
        "structure; membership of their objects alone is insufficient.",
    "complexes.011":
        "Two rank/exactness components have typed Lean support. The cohomology "
        "dimension identifications are not thereby formally certified.",
    "complexes.012":
        "The signed arithmetic after substituting the cohomology dimensions "
        "has typed Lean support; the geometric dimension calculation is separate.",
    "standard-monomials.007":
        "The statement explicitly assumes positive tensor degree d. The d=0 "
        "exception is discussed immediately afterward.",
    "cryptography.003":
        "An ideal finite Fourier-sampling distribution, not a new ECC resource "
        "improvement or a fault-tolerant hardware theorem.",
    "cryptography.006":
        "Lean verifies explicit integral shear identities and a squared-length "
        "formula. The operator-norm limit is not part of those declarations.",
    "cryptography.007":
        "The full statement includes two additional error terms and a "
        "decoding-radius conclusion. The simpler Lean cancellation identity "
        "is deliberately not equated with this whole statement.",
    "cryptography.008":
        "The general norm bound is not equated with the Lean theorem restricted "
        "to two coordinates and binary selector coefficients.",
    "cryptography.009":
        "The componentwise algebra is proved; existence or speed of the "
        "hypothetical recovery algorithms is not established.",
    "quantum-surfaces.001":
        "Uses the standard classification formula for connected closed oriented "
        "surfaces, in addition to the local subdivision count.",
    "quantum-surfaces.003":
        "The code-dimension and finite Pauli-group assertions are not fully "
        "formalized by the abstract Lean boundary/phase commutation identity.",
    "quantum-surfaces.004":
        "Only the final integer Euler/rank substitution is mapped to Lean; "
        "surface topology, incidence ranks, and CSS dimensions remain separate.",
    "quantum-surfaces.008":
        "The finite commuting-projector gap is proved in its stated normalization. "
        "It is not a continuum nonabelian Yang--Mills mass-gap claim.",
    "quantum-surfaces.009":
        "The exact finite correlator is proved. Its analytic product formula "
        "also supplies an efficient classical baseline.",
    "gauge-theory.010":
        "Uses the stated nonnegative self-adjoint Hamiltonian and vacuum "
        "hypotheses plus the spectral theorem. It does not assert that a "
        "Yang--Mills Hamiltonian has the required gap.",
    "gauge-theory.013":
        "An abstract numerical recurrence lemma; no Yang--Mills "
        "renormalization recurrence with these constants is established.",
    "source-concordance.001":
        "An independently proved finite-field correction to a source "
        "overstatement, including its explicit inverse formula.",
}

# Stable labels for the added fluid chapters; ordinary analytic hypotheses are
# recorded precisely, not automatically treated as unresolved research goals.
LABEL_NOTES = {
    "prop:micro-bornhuang":
        "A finite electronic-dimensional Born--Huang identity with the displayed "
        "smoothness assumptions; not an unbounded electronic Hamiltonian theorem.",
    "prop:micro-hellmann":
        "The differentiated finite-dimensional eigenvalue equation under the "
        "stated smooth normalized eigenvector hypotheses; not a general spectral "
        "perturbation theorem for unbounded operators.",
    "prop:micro-invariants":
        "The collision-invariant classification assumes C^2 regularity and d>=2. "
        "No measurable-only or one-dimensional classification is asserted.",
    "thm:micro-H":
        "The entropy calculation explicitly assumes differentiability, finite "
        "entropy, and justified interchanges of collision integrals. It does not "
        "construct solutions satisfying those hypotheses.",
    "prop:micro-pod":
        "Weighted snapshot-projection optimality with a positive definite mass "
        "matrix and the specified snapshot weights. It is not a trajectory-error, "
        "out-of-sample accuracy, or reduced-dynamics stability guarantee. The "
        "separate Euclidean projector lemmas are not equated with this full SVD theorem.",
    "prop:micro-deim":
        "Interpolation and error amplification require the sampled-basis inverse. "
        "The conclusion does not itself provide full-order-dimension-independent "
        "evaluation of an arbitrary dense nonlinear operator.",
    "prop:ns-force-energy":
        "The continuum energy argument assumes the stated smooth solution and "
        "support/integrability. It is not covered by the finite matrix derivative "
        "theorem and does not construct the released singular flow.",
    "prop:ns-sparse-volterra":
        "The local proof supplies the holomorphic Picard estimate under the "
        "displayed kernel, block, and parameter-neighborhood hypotheses. Lean "
        "checks only a strict-lower/diagonal/strict-lower zero composite, not the "
        "Cauchy estimates, word count, convergence, or uniqueness argument.",
    "prop:ns-residual-flatness":
        "A conditional realization interface with all required symbol, cutoff, "
        "and differential-polynomial bounds stated. It does not independently "
        "construct the full formal cascade supplied by the released paper.",
    "prop:fluid-order":
        "The formal declarations establish the exact integer matrix identities "
        "and injectivity on integer coefficient pairs. They do not bundle a "
        "Lean ring homomorphism from a separately constructed Z[sqrt(2)].",
    "prop:fluid-covering":
        "Only det(J^k)=14^k is formally mapped. The lattice quotient, Smith normal "
        "form, covering-space, and Haar-integration arguments remain the local "
        "mathematical proof.",
    "prop:fluid-no-complex":
        "The real 2-by-2 matrix obstruction is kernel checked. The subsequent "
        "geometric interpretation about holomorphic elliptic-curve endomorphisms "
        "is not a formalized Riemann-surface theorem.",
    "prop:fluid-discrete-hodge":
        "The mapped boundary lemma assumes its zero-composition relation. The "
        "metric adjoints, Hodge sum of squares, and derivation of that relation "
        "from the original cochain complex are separate parts of the proof.",
    "thm:fluid-finite-closure":
        "Only finite matrix work and the derivative identity are formally mapped, "
        "with explicit skewness and Gram-factorization hypotheses. The reduction "
        "from a general positive semidefinite L, state-dependent ODE well-posedness, "
        "Gronwall estimate, and global continuation are not formalized here.",
    "thm:fluid-memory":
        "The continuous matrix-exponential variation-of-constants formula is "
        "proved in prose. Discrete-memory declarations are intentionally not "
        "mapped to this continuous theorem.",
    "prop:fluid-discrete-memory":
        "Lean checks the hidden recurrence and resolved finite convolution. "
        "The resolvent determinant factorization is a separate unformalized "
        "component. The standalone Schur block-equation equivalence is not "
        "misidentified as a determinant theorem.",
    "prop:fluid-carleman-contractivity":
        "The truncation estimate assumes a bounded exact solution and a contractive "
        "linear semigroup in compatible tensor norms. It does not establish those "
        "properties uniformly over a fluid discretization or imply quantum advantage.",
    "prop:fluid-nonnormal-counterexample":
        "An explicit locally proved counterexample to a particular eigenvalue-only "
        "Euclidean norm inference in the reviewed Liu version 4. It is not a "
        "rejection of every algorithmic application or a Lean-checked calculation.",
    "prop:fluid-dissipative-ball":
        "A sufficient invariant-ball and finite-dimensional continuation argument "
        "under a bound on the Hermitian part in the stated metric. It does not "
        "replace that hypothesis with spectral stability alone and is not "
        "mapped to the finite energy derivative lemma as a whole theorem.",
    "prop:fluid-equality-partial-isometry":
        "A finite partial-isometry calculation and explicit norm-three "
        "counterexample to the reviewed equality-map formula. It does not "
        "invalidate the possibility of a correct equality block encoding.",
    "prop:fluid-equality-unitary":
        "An explicit reversible basis permutation and measured successful branch, "
        "including its state-dependent success probability. It does not "
        "deterministically copy an arbitrary unknown state or remove readout cost.",
    "prop:fluid-halmos-dilation":
        "A finite rectangular contraction dilation with alpha>=||A|| and the "
        "correct success probability. The proof does not derive the source's "
        "full collision-algorithm resource bound or repair its Carleman analysis.",
    "prop:fluid-postselection-instrument":
        "The two unnormalized branches are linear completely positive maps with "
        "total trace preservation. Conditional state normalization is not an "
        "unconditional deterministic nonlinear quantum channel.",
}

# Each item maps an actually typed declaration to a stated component, never
# to an entire composite environment. The names are checked against manifests.
FORMAL_COMPONENTS = {
    "complexes.011": [
        ("ResearchBridge.complex_rank_bound",
         "The adjacent-rank inequality rank(A)+rank(B)<=dim(V1), assuming BA=0."),
        ("ResearchBridge.middle_exact_iff_rank_sum",
         "Middle exactness iff equality in the adjacent-rank bound, assuming BA=0."),
    ],
    "complexes.012": [
        ("ResearchBridge.euler_rank_identity",
         "The integer identity (a-r)-(b-r-s)+(c-s)=a-b+c after dimension substitution."),
    ],
    "cryptography.006": [
        ("ResearchBridge.shear_determinant_one",
         "The displayed integer shear has determinant one."),
        ("ResearchBridge.shear_inverse",
         "The displayed shear multiplied by the opposite shear is the identity."),
        ("ResearchBridge.shear_e2_image",
         "The shear sends the second basis vector to (N,1)."),
        ("ResearchBridge.shear_e2_norm_squared",
         "The real squared-coordinate length of that image is N^2+1; "
         "the square-root and unbounded-operator-norm conclusion are not formalized here."),
    ],
    "quantum-surfaces.004": [
        ("ResearchQuantum.euler_surface_rank_substitution",
         "The integer substitution E-(V-1)-(F-1)=2g, assuming V-E+F=2-2g; "
         "the surface and stabilizer rank hypotheses are not proved by this declaration."),
    ],
    "complexes.025": [
        ("DiagramGrammar.homotopy_implies_exact",
         "The abstract implication from a zero composite and a middle contracting-homotopy "
         "identity to image=kernel. The exterior operations, their identity, and the full "
         "graded contracting homotopy are not formalized by this declaration."),
    ],
    "standard-monomials.004": [
        ("DiagramGrammar.homotopy_implies_exact",
         "The abstract middle exactness consequence once the contraction/creation "
         "homotopy and zero-composition equations have been supplied. The exterior "
         "algebra and its shuffle signs remain the manuscript's proof."),
    ],
}

# Labels keep new chapter mappings stable when unrelated claims are inserted.
FORMAL_LABEL_COMPONENTS = {
    "thm:typed-rewrite-soundness": [
        ("DiagramGrammar.context_sound",
         "Equality is preserved by typed one-hole sequential contexts. This syntax "
         "has identity, typed generators, and sequential composition; no tensor-context "
         "or density-operator syntax is formalized here."),
        ("DiagramGrammar.derivation_sound",
         "Every finite derivation of contextual sequential rewrites preserves the exact "
         "linear-map denotation, conditional on soundness of each basic rule."),
        ("DiagramGrammar.equiv_derivation_sound",
         "For the explicit linear-equivalence generator system, structural rules and "
         "inverse-pair cancellation are proved sound under finite contextual derivations. "
         "This is not completeness, confluence, or a certificate for floating-point code."),
    ],
    "thm:unitary-chain-transport": [
        ("DiagramGrammar.complex_transport",
         "The zero-composition equation is preserved under independent linear "
         "equivalences. Match A=d2, B=d1, e0=F2, e1=F1, e2=F0. "
         "The general homology-quotient isomorphism is not proved by this declaration."),
        ("DiagramGrammar.matrix_hodge_conjugacy",
         "The finite complex-matrix Hodge conjugacy identity, with A=d2, B=d1, "
         "U0=F2, U1=F1, U2=F0 and endpoint U-adjoint*U=I hypotheses. "
         "Choosing all changes unitary makes inverse equal adjoint as in the text. "
         "Infinite-dimensional spectral assertions and homology are outside this lemma."),
    ],
    "prop:ns-sparse-volterra": [
        ("FluidInterfaces.lower_diagonal_lower_zero",
         "The composition of a strict lower block, a block diagonal map, and "
         "another strict lower block is zero. The two lower blocks may differ, "
         "as needed when a derivative hits a coefficient. This is only the block "
         "algebra; no function-space, Volterra, holomorphic, or convergence theorem "
         "is formalized by this declaration."),
    ],
    "prop:fluid-order": [
        ("FluidInterfaces.quadratic_generator_square",
         "The displayed integer generator A satisfies A*A=2*I."),
        ("FluidInterfaces.renormalization_quadratic_identity",
         "The displayed matrix J satisfies J*J-8*J+14*I=0 over the integers."),
        ("FluidInterfaces.renormalization_determinant",
         "The exact integer determinant of J is 14."),
        ("FluidInterfaces.renormalization_power_determinant",
         "For every natural k, det(J^k)=14^k; no topological degree is included."),
        ("FluidInterfaces.renormalization_is_quadratic_order_element",
         "The displayed matrix J is the coefficient-pair matrix rho(4,1)."),
        ("FluidInterfaces.quadratic_order_one",
         "The integer coefficient-pair matrix rho(1,0) is the identity."),
        ("FluidInterfaces.quadratic_order_addition",
         "The coefficient-pair matrices obey rho(a,b)+rho(c,d)=rho(a+c,b+d)."),
        ("FluidInterfaces.quadratic_order_multiplication",
         "The coefficient-pair matrices obey rho(a,b)rho(c,d)="
         "rho(ac+2bd,ad+bc). A bundled ring homomorphism from an algebraic "
         "number-field order is not constructed by this identity."),
        ("FluidInterfaces.quadratic_order_determinant",
         "The exact norm determinant det(rho(a,b))=a^2-2b^2 over integer pairs."),
        ("FluidInterfaces.quadratic_order_representation_injective",
         "The map from integer pairs (a,b) to their displayed matrix is injective. "
         "Identification of these pairs with the order is the manuscript's argument."),
    ],
    "prop:fluid-covering": [
        ("FluidInterfaces.renormalization_power_determinant",
         "Only the arithmetic input det(J^k)=14^k. Neither the size of the lattice "
         "quotient, the covering degree, nor invariance of normalized Haar "
         "integration is proved by this Lean declaration."),
    ],
    "prop:fluid-no-complex": [
        ("FluidInterfaces.no_commuting_complex_structure",
         "For a real 2-by-2 matrix C commuting with the displayed J, C*C is not "
         "minus the identity. This exact linear-algebra statement does not "
         "formalize the subsequent geometry of elliptic curves."),
    ],
    "prop:fluid-discrete-hodge": [
        ("FluidInterfaces.boundary_flux_divergence_zero",
         "Given matrices B,C with BC=0, B(Cq)=0. With B=delta_1 and C=delta_2 "
         "this is the proposition's final divergence-free consequence once "
         "delta_1 delta_2=0 is supplied; mass-matrix adjoints and Hodge positivity "
         "are not proved by this declaration."),
    ],
    "thm:fluid-finite-closure": [
        ("FluidInterfaces.skew_transport_work",
         "A finite real skew-symmetric matrix has zero quadratic work; use "
         "J=-K(a) at the current state."),
        ("FluidInterfaces.factorized_viscosity_work",
         "The Euclidean Gram term has work u^T(L^T L)u=|Lu|^2. The manuscript's "
         "learned closure uses this factorized form; existence of a factorization "
         "of a general positive semidefinite physical viscosity matrix is separate."),
        ("FluidInterfaces.finite_fluid_work_identity",
         "The algebraic work balance for skew transport, factorized physical "
         "viscosity, factorized learned dissipation, and forcing."),
        ("FluidInterfaces.kinetic_energy_derivative",
         "Actual finite Euclidean kinetic-energy differentiation from coordinate "
         "HasDerivAt hypotheses; it neither constructs a trajectory nor proves "
         "an ODE existence theorem."),
        ("FluidInterfaces.finite_fluid_energy_derivative",
         "At a specified time with the displayed coordinate derivatives, the "
         "finite energy derivative equals forcing work minus the two Gram "
         "dissipations. State-dependent coefficients may be evaluated at this "
         "time, but local existence, Gronwall, continuation, and continuum "
         "regularity are not part of the declaration."),
    ],
    "prop:fluid-closure-obstruction": [
        ("FluidInterfaces.hidden_state_prevents_autonomous_closure",
         "For linear A and B with B(y) nonzero, no function F of the retained "
         "state alone agrees with Ax+Bz for all retained and hidden states. "
         "No assertion is made about a restricted invariant manifold or a "
         "probabilistic conditional-expectation closure."),
    ],
    "prop:fluid-discrete-memory": [
        ("FluidInterfaces.hidden_recurrence_expansion",
         "The all-natural-time expansion z_n=D^n z_0+sum_{k<n}D^(n-1-k)Cx_k "
         "from the exact hidden recurrence, including the empty sum at zero."),
        ("FluidInterfaces.resolved_memory_identity",
         "The resulting exact discrete convolution in the retained recurrence. "
         "No continuous matrix exponential, continuous-time memory integral, "
         "or block-resolvent determinant identity is included."),
    ],
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def uncomment_tex(s: str) -> str:
    """Remove unescaped line comments while retaining the number of lines."""
    result = []
    for line in s.splitlines(keepends=True):
        for match in re.finditer("%", line):
            backslashes = 0
            j = match.start() - 1
            while j >= 0 and line[j] == "\\":
                backslashes += 1
                j -= 1
            if backslashes % 2 == 0:
                line = line[:match.start()] + ("\n" if line.endswith("\n") else "")
                break
        result.append(line)
    return "".join(result)


def input_files() -> list[Path]:
    result, seen = [], set()

    def visit(path: Path) -> None:
        path = path.resolve()
        if path in seen:
            return
        if not path.is_relative_to(MANUSCRIPT.resolve()):
            raise ValueError(f"Input outside manuscript directory: {path}")
        seen.add(path)
        result.append(path)
        source = uncomment_tex(path.read_text())
        for name in re.findall(r"\\(?:input|include)\s*\{([^}]+)\}", source):
            candidate = MANUSCRIPT / (name if Path(name).suffix else name + ".tex")
            if candidate.exists():
                visit(candidate)
            else:
                raise FileNotFoundError(f"Included manuscript file is missing: {candidate}")

    visit(MANUSCRIPT / "main.tex")
    return result


def citations(text: str) -> list[str]:
    return sorted({key.strip() for item in CITE_RE.findall(text)
                   for key in item.split(",")})


def strip_lean_comments_and_strings(s: str) -> str:
    """Handle nested Lean block comments, line comments, and quoted strings."""
    result, i, depth = [], 0, 0
    while i < len(s):
        if depth:
            if s.startswith("/-", i):
                depth += 1
                result.extend("  ")
                i += 2
            elif s.startswith("-/", i):
                depth -= 1
                result.extend("  ")
                i += 2
            else:
                result.append("\n" if s[i] == "\n" else " ")
                i += 1
        elif s.startswith("/-", i):
            depth = 1
            result.extend("  ")
            i += 2
        elif s.startswith("--", i):
            j = s.find("\n", i)
            if j < 0:
                result.extend(" " * (len(s) - i))
                break
            result.extend(" " * (j - i))
            i = j
        elif s[i] == '"':
            result.append(" ")
            i += 1
            while i < len(s):
                if s[i] == "\\":
                    result.extend("  ")
                    i += 2
                elif s[i] == '"':
                    result.append(" ")
                    i += 1
                    break
                else:
                    result.append("\n" if s[i] == "\n" else " ")
                    i += 1
        else:
            result.append(s[i])
            i += 1
    if depth:
        raise ValueError("Unterminated Lean block comment")
    return "".join(result)


def lean_audit() -> tuple[dict, dict]:
    """Bind every current declaration to the current successful six-module run.

    This function does not run Lean. It validates the existing fresh run's
    source, checker, configuration, raw-log and per-declaration evidence.
    Older four-module manifests remain historical and are not relabeled.
    """
    reports, authoritative_names, signatures = [], set(), {}
    namespaces = {
        "BridgeTheorems": "ResearchBridge",
        "QuantumInterfaces": "ResearchQuantum",
        "DiagramGrammar": "DiagramGrammar",
        "FluidInterfaces": "FluidInterfaces",
        "ReductionContracts": "ReductionContracts",
        "TransportContracts": "TransportContracts",
    }
    manifest_path = LEAN / "final-verification/verification.json"
    fresh = json.loads(manifest_path.read_text())
    modules = fresh["modules"]
    by_module = {m["module"]: m for m in modules}
    config_path = LEAN / "lakefile.toml"
    config = tomllib.loads(config_path.read_text())
    if (fresh["status"] != "verified" or len(modules) != len(by_module)
            or fresh["module_count"] != len(namespaces)
            or set(by_module) != set(namespaces)
            or set(config["defaultTargets"]) != set(namespaces)
            or {m["name"] for m in config["lean_lib"]} != set(namespaces)):
        raise ValueError("Current Lean verification and Lake target scope mismatch")
    if (fresh["checker_sha256"] != sha((LEAN / "verify_all.py").read_bytes())
            or fresh["lakefile_sha256"] != sha(config_path.read_bytes())
            or fresh["mathlib_commit"] != config["require"][0]["rev"]
            or not fresh["mathlib_tracked_files_clean"]
            or (LEAN / "lean-toolchain").read_text().strip() != "leanprover/lean4:v4.24.0"
            or "version 4.24.0," not in fresh["lean_version"]):
        raise ValueError("Current Lean checker/toolchain/configuration provenance mismatch")
    standard_axioms = {"propext", "Classical.choice", "Quot.sound"}
    for module, namespace in namespaces.items():
        record = by_module[module]
        path = LEAN / (module + ".lean")
        if record["source"] != str(path.relative_to(PROJECT)):
            raise ValueError(f"Unexpected source path in verification: {module}")
        raw = path.read_text()
        code = strip_lean_comments_and_strings(raw)
        actual = {namespace + "." + name for name in
                  re.findall(r"(?m)^\s*theorem\s+([A-Za-z_][A-Za-z0-9_]*)", code)}
        names = set(record["declarations"])
        if len(names) != len(record["declarations"]) or names & authoritative_names:
            raise ValueError(f"Duplicate declaration in verification: {module}")
        authoritative_names |= names
        found = [{"token": m.group(), "line": code[:m.start()].count("\n") + 1}
                 for m in re.finditer(r"\b(?:axiom|sorry|admit|sorryAx|unsafe|native_decide)\b", code)]
        by_name = {name: set(values) for name, values in record["axioms_per_declaration"].items()}
        dependencies = set().union(*by_name.values()) if by_name else set()
        log_path = manifest_path.parent / record["log"]
        if not log_path.resolve().is_relative_to(manifest_path.parent.resolve()):
            raise ValueError("Verification log escapes its evidence directory")
        log = log_path.read_text()
        logged_axioms = {name: {x.strip() for x in values.split(",") if x.strip()}
                         for name, values in re.findall(
                             r"'([^']+)' depends on axioms: \[([^]]*)\]", log)}
        for name in re.findall(r"'([^']+)' does not depend on any axioms", log):
            logged_axioms[name] = set()
        if (record["status"] != "verified" or record["exit_code"] != 0
                or record["warning_count"] != 0 or "warning:" in log
                or not record["source_unchanged_during_check"]
                or record["unexpected_axioms"] or logged_axioms != by_name
                or set(by_name) != names or "sorryAx" in log
                or sha(log_path.read_bytes()) != record["log_sha256"]):
            raise ValueError(f"Current verification log/manifest mismatch: {module}")
        kernel_types, current = {}, None
        for line in log.splitlines():
            header = re.match(r"^(" + re.escape(namespace) + r"\.[A-Za-z_][A-Za-z0-9_]*)(?:\.\{|[ ({:])", line)
            if header:
                current = header.group(1)
                kernel_types[current] = line
            elif current and line.startswith(" "):
                kernel_types[current] += "\n" + line
            else:
                current = None
        digest = sha(path.read_bytes())
        if (digest != record["source_sha256"] or actual != names or found
                or len(names) != record["declaration_count"] or set(kernel_types) != names):
            raise ValueError(f"Source/declaration/printed-type mismatch: {module}")
        if dependencies - standard_axioms:
            raise ValueError(f"Unaccounted Lean dependencies: {dependencies - standard_axioms}")
        for name in sorted(actual):
            short = name.split(".")[-1]
            match = re.search(r"(?m)^\s*theorem\s+" + re.escape(short) + r"\b", raw)
            end = raw.index(":=", match.end())
            signatures[name] = {
                "name": name,
                "source_file": str(path.relative_to(PROJECT)),
                "source_sha256": digest,
                "type_signature_source": raw[match.start():end].strip(),
                "kernel_printed_type": kernel_types[name],
                "implicit_section_context_for_mapping": "",
                "verification_manifest": str(manifest_path.relative_to(PROJECT)),
                "verification_log": str(log_path.relative_to(PROJECT)),
                "reported_axioms": sorted(by_name[name]),
                "type_evidence": "kernel_printed_type",
            }
        reports.append({
            "source_file": str(path.relative_to(PROJECT)),
            "manifest_file": str(manifest_path.relative_to(PROJECT)),
            "source_sha256": digest,
            "manifest_source_hash_matches": True,
            "verification_log": str(log_path.relative_to(PROJECT)),
            "verification_log_sha256": record["log_sha256"],
            "verification_log_axioms_match_manifest": True,
            "declaration_count": len(actual),
            "source_declarations_match_manifest": True,
            "print_axioms_covers_every_declaration": True,
            "kernel_printed_types_cover_every_declaration": True,
            "audit_commands_provenance": "verify_all.py appends #check and #print axioms for every selected declaration",
            "forbidden_tokens_outside_comments_and_strings": found,
            "reported_dependencies": sorted(dependencies),
            "nonstandard_reported_dependencies": sorted(dependencies - standard_axioms),
        })
    if len(authoritative_names) != fresh["declaration_count"]:
        raise ValueError("Current Lean aggregate declaration count mismatch")
    other_files = []
    for path in sorted(LEAN.glob("*.lean")):
        if path.stem in namespaces:
            continue
        code = strip_lean_comments_and_strings(path.read_text())
        hits = re.findall(r"\b(?:axiom|sorry|admit|sorryAx|unsafe|native_decide)\b", code)
        if hits:
            raise ValueError(f"Forbidden tokens in Lean configuration: {path.name}: {hits}")
        other_files.append({"file": str(path.relative_to(PROJECT)),
                            "sha256": sha(path.read_bytes()), "forbidden_tokens": hits})
    fresh_record = {
        "path": str(manifest_path.relative_to(PROJECT)),
        "sha256": sha(manifest_path.read_bytes()),
        "status": fresh["status"],
        "checked_at_utc": fresh["checked_at_utc"],
        "module_count": fresh["module_count"],
        "declaration_count": fresh["declaration_count"],
        "scope": fresh["scope"],
        "upstream_continuum_kernel_verification_performed": False,
    }
    return {
        "method": "Source, configuration, checker, exact printed-type and raw-log audit against the current successful six-module verification manifest. This inventory generator does not invoke Lean.",
        "new_kernel_run_performed": False,
        "separate_fresh_local_kernel_verification": fresh_record,
        "authoritative_verified_declaration_count": len(authoritative_names),
        "project_axiom_or_admitted_placeholder_detected": False,
        "foundational_axioms_are_not_claimed_absent": sorted(standard_axioms),
        "verified_modules": reports,
        "other_lean_files": other_files,
        "all_authoritative_declaration_names": sorted(authoritative_names),
    }, signatures


def merge_new_component_mappings(signatures: dict) -> dict:
    """Validate and import the reviewed additions without replacing older maps."""
    path = LEAN / "new-declarations.json"
    additions = json.loads(path.read_text())
    entries = additions["declarations"]
    names = [item["declaration"] for item in entries]
    if len(entries) != additions["declaration_count"] or len(names) != len(set(names)):
        raise ValueError("New declaration-map count or uniqueness mismatch")
    existing = {name for groups in (FORMAL_COMPONENTS, FORMAL_LABEL_COMPONENTS)
                for values in groups.values() for name, _ in values}
    for item in entries:
        name = item["declaration"]
        if name not in signatures or name in existing:
            raise ValueError(f"New map references unknown or previously mapped declaration: {name}")
        signature = signatures[name]
        if (item["source"] != signature["source_file"]
                or item["source_sha256"] != signature["source_sha256"]
                or item["type_and_axiom_log"] != signature["verification_log"]
                or item["whole_manuscript_formalization_claim"] is not False
                or not item["scope"].strip() or not item["manuscript_anchor"].strip()):
            raise ValueError(f"Stale or overclaimed new declaration mapping: {name}")
        manuscript_path = PROJECT / item["manuscript_source"]
        if (not manuscript_path.resolve().is_relative_to(MANUSCRIPT.resolve())
                or not manuscript_path.exists()
                or "\\label{" + item["manuscript_anchor"] + "}" not in uncomment_tex(manuscript_path.read_text())):
            raise ValueError(f"New declaration mapping lacks its exact manuscript anchor: {name}")
        FORMAL_LABEL_COMPONENTS.setdefault(item["manuscript_anchor"], []).append((name, item["scope"]))
    return {"path": str(path.relative_to(PROJECT)), "sha256": sha(path.read_bytes()),
            "declaration_count": len(entries), "previous_precise_component_declarations_preserved": len(existing)}


def extract_claims(files: list[Path], signatures: dict) -> list[dict]:
    result = []
    for path in files:
        source = uncomment_tex(path.read_text())
        matches = list(CLAIM_RE.finditer(source))
        for index, match in enumerate(matches, 1):
            kind, title = match.group(1), match.group(2)
            claim_id = f"{path.stem}.{index:03d}"
            closing = "\\end{" + kind + "}"
            body_end = source.index(closing, match.end())
            end = body_end + len(closing)
            statement = source[match.end():body_end].strip()
            labels = re.findall(r"\\label\{([^}]+)\}", statement)
            following = source[end:]
            proof_match = re.match(r"\s*\\begin\{proof\}(?:\[[^]]*\])?", following)
            proof, proof_line, proof_end_line = "", None, None
            if proof_match:
                proof_end = following.index("\\end{proof}", proof_match.end())
                proof = following[proof_match.end():proof_end].strip()
                proof_begin = following.index("\\begin{proof}")
                proof_line = source[:end + proof_begin].count("\n") + 1
                proof_end_line = source[:end + proof_end].count("\n") + 1
            next_start = matches[index].start() if index < len(matches) else len(source)
            previous_end = matches[index - 2].end() if index > 1 else 0
            before = source[max(previous_end, match.start() - 1600):match.start()]
            after = source[end:min(next_start, end + 1600)]
            if claim_id in EXTERNAL:
                status, citation_keys, note = "external_cited", *EXTERNAL[claim_id]
                if proof_match:
                    raise ValueError(f"Unexpected local proof on external claim: {claim_id}")
            elif kind == "conjecture":
                status, citation_keys, note = "conjectural", [], "A conjecture is not recorded as proved."
            elif kind == "problem":
                status, citation_keys, note = "proposed_open_problem", [], "A proposed problem is not recorded as proved."
            elif claim_id in CONDITIONAL:
                status, citation_keys, note = "conditional_local_argument", [], CONDITIONAL[claim_id]
            elif proof_match:
                status, citation_keys, note = "local_argument_present", [], NOTES.get(claim_id, "")
            else:
                raise ValueError(f"Unreviewed claim without attached proof: {claim_id}")
            mappings = []
            label_notes = [LABEL_NOTES[label] for label in labels if label in LABEL_NOTES]
            if label_notes:
                note = " ".join(([note] if note else []) + label_notes)
            components = list(FORMAL_COMPONENTS.get(claim_id, []))
            for label in labels:
                components.extend(FORMAL_LABEL_COMPONENTS.get(label, []))
            for name, scope in components:
                mappings.append({**signatures[name], "matched_component": scope,
                                 "whole_statement_formalized": False})
            result.append({
                "id": claim_id,
                "environment": kind,
                "name_tex": title,
                "display_name": title or f"Untitled {kind}",
                "labels": labels,
                "source_file": str(path.relative_to(PROJECT)),
                "start_line": source[:match.start()].count("\n") + 1,
                "end_line": source[:end].count("\n") + 1,
                "statement_tex": statement,
                "status": status,
                "status_meaning": (
                    "Classification of evidence present in the manuscript, "
                    "not a claim of a complete independent proof audit."
                ),
                "review_note": note or NOTES.get(claim_id, ""),
                "local_proof_environment_present": bool(proof_match),
                "local_proof_start_line": proof_line,
                "local_proof_end_line": proof_end_line,
                "local_proof_whitespace_words": len(proof.split()),
                "local_proof_sha256": sha(proof.encode()) if proof else None,
                "local_proof_opening_tex": proof[:500] if proof else None,
                "citations_inside_statement": citations(statement),
                "citations_inside_local_proof": citations(proof),
                "reviewed_external_theorem_citations": citation_keys,
                "nearby_citations_not_automatically_dependencies": citations(before + after),
                "inherited_context_warning": (
                    "Notation and hypotheses may be established before the environment; "
                    "consult the cited source file and surrounding chapter."
                ),
                "formalization_status": "partial_components_only" if mappings else "not_mapped",
                "whole_statement_formalized": False,
                "formalized_declarations": [m["name"] for m in mappings],
                "formal_component_mappings": mappings,
            })
    expected = set(EXTERNAL) | set(CONDITIONAL) | set(FORMAL_COMPONENTS)
    missing = expected - {r["id"] for r in result}
    if missing:
        raise ValueError(f"Manual annotation IDs no longer present: {sorted(missing)}")
    expected_labels = set(LABEL_NOTES) | set(FORMAL_LABEL_COMPONENTS)
    missing_labels = expected_labels - {label for c in result for label in c["labels"]}
    if missing_labels:
        raise ValueError(f"Manual annotation labels no longer present: {sorted(missing_labels)}")
    return result


def external_prose_statements(files: list[Path]) -> list[dict]:
    """Manually delimited major external dependencies of the fluid extension.

    This is not an automated classification of every sentence or cited work.
    In particular a paper's reported theorem is not promoted to a new local proof.
    """
    records = [
        {
            "id": "fluid-external.released-forced-breakdown",
            "name": "Released forced whole-space and periodic Navier--Stokes breakdown",
            "file": "navier-stokes-release.tex",
            "anchor": "The source's main conclusion can be recorded",
            "status": "external_cited_not_locally_reproved",
            "citations": ["NSOpenAI2026"],
            "scope": "Positive viscosity, smooth compactly supported external force, "
                     "initial rest, bounded L2 energy, and finite-time unbounded L-infinity "
                     "velocity; whole-space and periodic conclusions under their exact "
                     "smoothness, support, and energy quantifiers. The analytic construction "
                     "is supplied by the released paper, not by the interface propositions.",
            "verification_boundary": "The complete 166-page paper was jointly read. "
                                     "Source review and dependency scan were completed, "
                                     "but the separate fresh upstream kernel and Comparator "
                                     "checks did not complete. The successful local Lean "
                                     "4.24 checks do not verify this continuum theorem.",
            "review_record": "extension/review/navier-stokes/release-source-manifest.json",
        },
        {
            "id": "fluid-external.clay-formulation",
            "name": "Clay alternatives and periodic-pressure requirement",
            "file": "navier-stokes-release.tex",
            "anchor": "In Fefferman's formulation",
            "status": "external_problem_statement",
            "citations": ["NSFefferman"],
            "scope": "Alternatives A and B impose zero force; C and D permit the "
                     "specified smooth decaying forcing. The periodic formulation "
                     "also requires periodic pressure, as clarified by the erratum. "
                     "These are authoritative problem definitions, not new existence theorems.",
            "verification_boundary": "Forced existential breakdown does not establish "
                                     "unforced positive-viscosity breakdown.",
            "review_record": "extension/review/navier-stokes/release-review.md",
        },
        {
            "id": "fluid-external.boltzmann-grad",
            "name": "Short-time hard-sphere Boltzmann--Grad convergence",
            "file": "microscopic-fluid-limits.tex",
            "anchor": r"\subsection{A rigorous classical-to-kinetic bridge and its time interval}",
            "status": "external_cited_not_locally_reproved",
            "citations": ["microGallagher2013"],
            "scope": "The referenced hard-sphere theorem requires admissible asymptotic "
                     "initial factorization and weighted hierarchy bounds, and gives "
                     "short-time convergence of the specified observables away from "
                     "positional diagonals. The full recollision proof is not reproduced.",
            "verification_boundary": "Only the source's introduction, main convergence "
                                     "statement and concluding scope were reviewed; the "
                                     "monograph was not read or independently verified in full. "
                                     "No arbitrary-data, arbitrary-potential, or long-time "
                                     "particle-to-fluid theorem is inferred.",
            "review_record": "extension/review/navier-stokes/microscopic-source-coverage.json",
        },
        {
            "id": "fluid-external.hydrodynamic-limit",
            "name": "Golse--Saint-Raymond incompressible Navier--Stokes--Fourier limit",
            "file": "microscopic-fluid-limits.tex",
            "anchor": r"\subsection{A precise historical hydrodynamic-limit theorem}",
            "status": "external_cited_not_locally_reproved",
            "citations": ["microGolseSaintRaymond2009"],
            "scope": "Theorem 2.4 is cited for the stated hard-cutoff collision kernels, "
                     "whole-space incompressible scaling, entropy-controlled initial data, "
                     "renormalized kinetic solutions and weak fluctuation topology. The "
                     "limit solves the specified Navier--Stokes--Fourier system with an "
                     "energy inequality; stronger initial-energy conclusions require the "
                     "additional preparation assumptions.",
            "verification_boundary": "An external weak-limit theorem, not a local "
                                     "regularity/uniqueness proof or a direct composition "
                                     "with the short-time particle limit. Source-reading "
                                     "coverage is bounded as recorded in the ledger.",
            "review_record": "extension/review/navier-stokes/microscopic-source-coverage.json",
        },
        {
            "id": "fluid-external.feec",
            "name": "Finite element exterior calculus stability requirements",
            "file": "fluid-structures.tex",
            "anchor": "Stable approximation requires additional commuting projection",
            "status": "external_framework_cited",
            "citations": ["NSFEEC2006", "NSFEEC2010"],
            "scope": "The cited framework supplies the role of compatible projections "
                     "and norm estimates in approximation stability. The local finite "
                     "boundary and Hodge identities do not establish those estimates "
                     "for a mesh family.",
            "verification_boundary": "No complete FEEC theorem, mesh-uniform convergence "
                                     "theorem, or continuum limit is locally formalized.",
        },
        {
            "id": "fluid-external.liu-nonlinear-algorithm",
            "name": "Dissipative quantum linearization and a source norm-gap correction",
            "file": "quantum-fluid.tex",
            "anchor": r"\citet{NSLiu2021} analyze",
            "status": "external_claim_with_local_counterexample",
            "citations": ["NSLiu2021"],
            "scope": "The reviewed version 4 reports a favorable R<1 regime with sparse "
                     "access, preparation, solution-norm and error assumptions, and the "
                     "added forcing-size condition. Its normalized quantum-state output "
                     "does not include cost-free classical full-field readout.",
            "verification_boundary": "The manuscript proves a specific counterexample "
                                     "to the source's eigenvalue-only Euclidean norm-decay "
                                     "inference, then uses an independently proved "
                                     "Hermitian-part condition. The unrepaired general "
                                     "norm-decay statement is not adopted as a dependency.",
        },
        {
            "id": "fluid-external.wu-nonresonance",
            "name": "Nonresonant Carleman estimate with an explicit resonance gap",
            "file": "quantum-fluid.tex",
            "anchor": "Non-dissipative extensions also need hypotheses.",
            "status": "external_claim_hypotheses_audited_not_locally_reproved",
            "citations": ["NSWu2025"],
            "scope": "The cited Theorem 1.1 assumes diagonalizability, nonpositive "
                     "spectral real parts, a uniform solution bound, and a strictly "
                     "positive infimum resonance gap. The displayed geometric-convergence "
                     "parameter must be less than one. Pointwise nonresonance alone "
                     "does not establish a positive gap.",
            "verification_boundary": "The source estimate is not a dependency of the "
                                     "singularity proof. The manuscript separately proves "
                                     "the real-spectrum obstruction and a short-time "
                                     "contractive-semigroup estimate, without claiming "
                                     "a theorem for arbitrary neutral real fluid systems.",
        },
        {
            "id": "fluid-external.quantum-fluid-cost-study",
            "name": "End-to-end quantum lattice-Boltzmann cost and truncation study",
            "file": "quantum-fluid.tex",
            "anchor": r"The September 2026 end-to-end study by \citet{NSJennings2026}",
            "status": "external_study_with_local_interface_corrections",
            "citations": ["NSJennings2026"],
            "scope": "The cited study analyzes specified observables, lifting and time "
                     "discretization, conditioning, unitary block construction, and "
                     "observable extraction. Its numerical scaling and convergence "
                     "reports are distinguished from its proved bounds.",
            "verification_boundary": "The report supplies no universal quantum "
                                     "advantage theorem or continuum Navier--Stokes "
                                     "singularity proof for this project. The separate "
                                     "fluid-circuit-repairs input proves corrections to "
                                     "two reviewed finite-interface formulas, without "
                                     "claiming complete algorithm repair.",
        },
        {
            "id": "fluid-external.collision-normalization",
            "name": "Reported normalization of the source collision matrix",
            "file": "fluid-circuit-repairs.tex",
            "anchor": "The reviewed paper's equation~(D58a)",
            "status": "external_formula_not_locally_rederived",
            "citations": ["NSJennings2026"],
            "scope": "The value alpha=6/bar(tau-star) is attributed to equation "
                     "D58a for that source's D=2 collision matrix and parameter "
                     "conventions. It is not rederived as a norm formula for an "
                     "arbitrary collision model.",
            "verification_boundary": "The local rectangular dilation theorem assumes "
                                     "alpha>0 and alpha>=||A|| explicitly. Its proof "
                                     "does not depend on treating this particular "
                                     "external numerical normalization as universal.",
        },
    ]
    included = set(files)
    for record in records:
        path = MANUSCRIPT / "chapters" / record.pop("file")
        if path not in included:
            raise ValueError(f"External statement source is not included: {path}")
        source = uncomment_tex(path.read_text())
        anchor = record["anchor"]
        if source.count(anchor) != 1:
            raise ValueError(f"External statement anchor changed: {record['id']}")
        if set(record["citations"]) - set(citations(source)):
            raise ValueError(f"External statement citations missing: {record['id']}")
        record.update({
            "source_file": str(path.relative_to(PROJECT)),
            "source_sha256": sha(path.read_bytes()),
            "anchor_line": source[:source.index(anchor)].count("\n") + 1,
            "local_full_proof_present": False,
            "local_lean_formalization_asserted": False,
            "inventory_scope": "Selected major external statements in the added fluid chapters; "
                               "not an inventory of every prose sentence or theorem in cited works.",
        })
    return records


def formal_type_map(register: dict, signatures: dict) -> dict:
    declarations = []
    for name, signature in sorted(signatures.items()):
        uses = []
        for claim in register["claims"]:
            for mapping in claim["formal_component_mappings"]:
                if mapping["name"] == name:
                    uses.append({
                        "claim_id": claim["id"],
                        "claim_labels": claim["labels"],
                        "claim_source": claim["source_file"],
                        "component": mapping["matched_component"],
                        "whole_statement_formalized": False,
                    })
        declarations.append({**signature,
                             "mapping_status": "partial_components_only" if uses else "not_mapped",
                             "manuscript_components": uses})
    return {
        "schema_version": 1,
        "generated_at_utc": register["generated_at_utc"],
        "purpose": "Exact declaration types and manually reviewed component correspondences, "
                   "not a claim that all manuscript environments are formalized.",
        "declaration_count": len(declarations),
        "declarations_with_manuscript_components": sum(bool(d["manuscript_components"]) for d in declarations),
        "whole_environments_marked_fully_formalized": 0,
        "claim_register": "extension/review/claim-register.json",
        "lean_source_audit": register["lean_source_audit"],
        "declarations": declarations,
        "type_reading_note": "Prefer kernel_printed_type when present: it includes elaborated "
                             "implicit parameters and typeclass hypotheses. Otherwise the "
                             "unchanged source signature and recorded section context are "
                             "provided, with the exact source hash. Local definitions in "
                             "the same module remain part of its interpretation.",
        "excluded_claims": [
            "Global ODE continuation from a finite energy derivative alone",
            "Continuous memory from a discrete recurrence theorem",
            "Covering-space degree or Haar averaging from a matrix determinant alone",
            "Analytic Volterra convergence from zero block composition alone",
            "Weighted POD/SVD optimality from a fixed Euclidean projector lemma alone",
            "Any fresh verification of the upstream continuum Navier--Stokes release",
        ],
    }


def formal_type_markdown(mapping: dict) -> str:
    lines = ["# Formal declaration and manuscript component map", "", mapping["purpose"], "",
             f"This snapshot records **{mapping['declaration_count']} verified declarations**; "
             f"{mapping['declarations_with_manuscript_components']} are mapped to precise "
             "manuscript components. No composite manuscript environment is marked "
             "fully formalized.", "", mapping["type_reading_note"], "",
             "Fresh local checks are recorded in "
             "`extension/lean/final-verification/verification.json` and its six raw logs. "
             "Those checks concern the local Lean 4.24 companion; the upstream "
             "continuum Lean 4.34 build has its separate incomplete status.", "",
             "## Boundaries", "",
             *["- This map does not assert: " + s + "." for s in mapping["excluded_claims"]], "",
             "## Declarations", ""]
    for declaration in mapping["declarations"]:
        lines.extend(["### " + declaration["name"], "",
                      "Source: `" + declaration["source_file"] + "`. Verification: `" +
                      declaration["verification_manifest"] + "`.", "",
                      "Reported foundational dependencies: " +
                      (", ".join("`" + a + "`" for a in declaration["reported_axioms"])
                       or "none") + ".", ""])
        printed = declaration["kernel_printed_type"]
        if printed:
            lines += ["Elaborated type:", "", "```lean", printed, "```", ""]
        else:
            context = declaration["implicit_section_context_for_mapping"]
            lines += ["Verified source signature (with reviewed section context where needed):",
                      "", "```lean", (context + "\n" if context else "") +
                      declaration["type_signature_source"], "```", ""]
        if declaration["manuscript_components"]:
            for use in declaration["manuscript_components"]:
                lines.append("- **" + use["claim_id"] + "** (" +
                             ", ".join(use["claim_labels"]) + "): " + use["component"])
        else:
            lines.append("No manuscript environment is assigned to this declaration. "
                         "Its own precise type remains verified; no broader claim is inferred.")
        lines.append("")
    return "\n".join(lines)


def refresh_fluid_component_map(mapping: dict) -> None:
    """Complete the earlier fluid-only review map; preserve its historical checks."""
    path = REVIEW / "navier-stokes/formalization-map.json"
    if not path.exists():
        return
    previous = json.loads(path.read_text())
    fluid = {d["name"]: d for d in mapping["declarations"]
             if d["source_file"] == "extension/lean/FluidInterfaces.lean"}
    recorded_names = {name for group in previous["groups"] for name in group["theorems"]}
    if (recorded_names != set(fluid)
            or any(d["source_sha256"] != previous["source_sha256"] for d in fluid.values())):
        raise ValueError("Fluid component-map source/group snapshot changed")
    for group in previous["groups"]:
        group["manuscript_mapping"] = (
            "Exact proper-component matches from extension/review/formal-type-map.json; "
            "an empty list deliberately leaves the declaration unassigned to a broader "
            "manuscript environment. No full environment is certified."
        )
        group["manuscript_components"] = [
            {"declaration": name, "components": fluid[name]["manuscript_components"]}
            for name in group["theorems"]
        ]
    previous.update({
        "component_map_updated_at_utc": mapping["generated_at_utc"],
        "complete_type_map": "extension/review/formal-type-map.json",
        "claim_register": "extension/review/claim-register.json",
        "current_total_verified_declarations": mapping["declaration_count"],
        "separate_fresh_local_kernel_verification":
            "extension/lean/final-verification/verification.json",
        "historical_verification_note":
            "The old_modules recompilation flags describe the original fluid-only "
            "subtask and are preserved. The current fresh check of all six local "
            "modules is recorded separately; it does not recheck the upstream continuum release.",
    })
    path.write_text(json.dumps(previous, indent=2, ensure_ascii=False) + "\n")


def markdown(register: dict) -> str:
    counts = register["counts"]
    external_count = counts["by_status"].get("external_cited", 0)
    conditional_count = counts["by_status"].get("conditional_local_argument", 0)
    verified_count = counts["authoritative_verified_declarations"]
    mapped_count = counts["verified_declarations_mapped_to_precise_components"]
    mapped_claims = counts["environments_with_partial_formal_components"]
    lines = [
        "# Manuscript claim register",
        "",
        "This register inventories every theorem, proposition, lemma, corollary, "
        "conjecture, and problem environment reachable from the current manuscript "
        "main file. It records what evidence is present; it is not a universal "
        "proof certificate.",
        "",
        f"The snapshot contains **{counts['claim_environments']} claim environments** "
        f"in **{counts['included_tex_files']} included TeX files**. "
        f"**{counts['attached_proof_environments']}** have attached local proof "
        f"environments. {external_count} general results are explicitly cited external theorems. "
        f"{conditional_count} local arguments are classified as conditional transfer or deduction "
        "criteria because their additional inputs are not established by those claims.",
        "",
        f"A separate list classifies {counts['selected_external_prose_statements']} major "
        "external statements from the new fluid chapters, including the released "
        "continuum theorem and the kinetic-limit and quantum-algorithm literature. "
        "These prose records are not added to the number of locally proved environments.",
        "",
        f"The {verified_count} verified Lean declarations are governed by their successful "
        f"verification manifests and raw logs. This register maps {mapped_count} declarations "
        f"to exact components of {mapped_claims} manuscript claims. **No complete composite environment "
        "is marked as fully formalized.** A partial map is never counted as a Lean "
        "proof of the entire proposition.",
        "",
        "## Meaning of the status labels",
        "",
        "- **Local argument present:** the manuscript supplies an attached proof. "
        "This label does not certify every inference or reprove all background results.",
        "- **Conditional local argument:** the implication is argued, but the "
        "specified quantitative, convergence, or duality inputs are assumptions.",
        "- **External cited:** the general theorem is attributed to the listed "
        "primary reference and is not proved in full here.",
        "- **Conjectural / proposed open problem:** reserved for such environments; "
        "they are not counted as proved. Additional research directions in prose "
        "are listed separately below.",
        "",
        "All statements inherit notation and hypotheses from their chapters. "
        "The JSON retains their exact statement text, labels, proof-source metadata, "
        "source hashes, and the precise types for the manually matched formal components.",
        "",
        "A separate mathematical reading, with per-claim findings and its own "
        "reviewed source snapshots, is recorded in second-pass-math-audit.json/md. "
        "Generating this inventory does not itself conduct that proof review.",
        "",
        "## Complete environment inventory",
        "",
        "| ID | Source | Environment and name | Evidence | Formal mapping |",
        "|---|---|---|---|---|",
    ]
    descriptions = {
        "local_argument_present": "Local argument",
        "conditional_local_argument": "Conditional local argument",
        "external_cited": "External cited theorem",
        "conjectural": "Conjectural",
        "proposed_open_problem": "Proposed open problem",
    }
    for claim in register["claims"]:
        title = claim["display_name"].replace("|", r"\|").replace("\n", " ")
        source = Path(claim["source_file"]).name
        mapping = ("Partial components: " + ", ".join(claim["formalized_declarations"])
                   if claim["formalized_declarations"] else "Not mapped")
        lines.append(
            f"| {claim['id']} | {source} | {claim['environment']}: {title} | "
            f"{descriptions[claim['status']]} | {mapping} |"
        )
    lines += ["", "## Conditional and external statements", ""]
    for claim in register["claims"]:
        if claim["status"] in {"conditional_local_argument", "external_cited"}:
            refs = claim["reviewed_external_theorem_citations"]
            suffix = f" Bibliography keys: {', '.join(refs)}." if refs else ""
            lines.append(f"- **{claim['id']} — {claim['display_name']}.** "
                         f"{claim['review_note']}{suffix}")
    lines += ["", "## Selected external statements in the fluid chapters", "",
              "These records classify source use and proof boundaries. They do not "
              "treat reported external results as newly proved local theorems.", ""]
    for record in register["external_prose_statements"]:
        lines += ["### " + record["name"], "",
                  "Status: `" + record["status"] + "`. Bibliography keys: " +
                  ", ".join(record["citations"]) + ".", "",
                  record["scope"], "", record["verification_boundary"], "",
                  "Source: `" + record["source_file"] + "`.", ""]
    lines += [
        "", "## Exact scope of the partial Lean correspondences", "",
    ]
    for claim in register["claims"]:
        if claim["formal_component_mappings"]:
            lines.append(f"### {claim['id']} — {claim['display_name']}")
            lines.append("")
            for mapping in claim["formal_component_mappings"]:
                lines.append(f"- **{mapping['name']}**: {mapping['matched_component']}")
            lines.append("")
    lines += [
        "The remaining verified declarations are not forced into a broader "
        "manuscript statement. They still have the scope and types recorded in "
        "their source files and verification manifests. Examples include scalar "
        "quadric expansions, abstract binary-character commutation, and a "
        "restricted binary-noise bound. Similar terminology alone does not "
        "establish a formal correspondence.",
        "",
        "## Proposed research and incomplete goals outside the environment list",
        "",
    ]
    for item in register["prose_research_directions"]:
        lines.append(f"- **{item['name']}** — {item['status_note']} "
                     f"Source: {item['source_file']}.")
    lines += [
        "", "## Lean source audit", "",
        "The source audit checked all registered theorem modules and the Lean configuration "
        "after stripping nested block comments, line comments, and strings. "
        "It found no project axiom declaration, sorry/admit/sorryAx placeholder, "
        "unsafe declaration, or native_decide invocation. The module hashes, "
        "declaration sets, and print-axioms inventories match the existing successful "
        "verification manifests. Their reported dependencies are limited to "
        "propext, Classical.choice, and Quot.sound; the audit does not claim "
        "that foundational axioms are absent.",
        "",
        "**The inventory generator itself does not run Lean.** Fresh second-pass "
        "kernel runs of all six modules are recorded in "
        "extension/lean/final-verification/verification.json and its six module logs. "
        f"All {verified_count} declaration-level dependency reports, printed types, source hashes "
        "and log hashes match the current successful record. The existing 35 precise "
        "component declarations remain mapped; validated additions are merged without "
        "reclassifying any composite manuscript statement as fully formalized. "
        "Earlier three-, four-, and 109-declaration six-module checks remain historical records.",
        "",
        "The local successful check does not complete the upstream continuum "
        "Navier--Stokes build, which used a different toolchain and stopped at "
        "missing dependency artifacts. That outcome remains in "
        "navier-stokes/release-build-verification.json.",
        "",
        "## Reproduction and limits", "",
        "From the project root, run python extension/review/build_claim_register.py "
        "(or invoke the script by absolute path from any directory). "
        "The script reads manuscript and Lean sources and writes the JSON "
        "and Markdown claim register and formal-type-map, and refreshes the fluid-only "
        "review map's component references. It does not modify original Lean sources, "
        "verification manifests, or logs. Manual status annotations and type matches are "
        "visible in the script. The script enforces matching Lean source hashes. "
        "If manuscript claims are reordered or substantively changed, review "
        "the manual annotations before regenerating.",
        "",
        "The inventory excludes unnumbered definitions, ordinary explanatory "
        "equations, prose results outside the explicitly selected external list, every theorem inside cited "
        "papers, and the inherited upstream project. It therefore does not "
        "constitute an assertion that all mathematical claims in all sources "
        "have been independently proved or formalized.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    files = input_files()
    initial_hashes = {path: sha(path.read_bytes()) for path in files}
    audit, signatures = lean_audit()
    additions = merge_new_component_mappings(signatures)
    audit["new_component_mapping_provenance"] = additions
    claims = extract_claims(files, signatures)
    external_prose = external_prose_statements(files)
    source_records = [{
        "path": str(path.relative_to(PROJECT)),
        "sha256": sha(path.read_bytes()),
        "bytes": path.stat().st_size,
        "lines": len(path.read_text().splitlines()),
    } for path in files]
    used_names = {name for claim in claims for name in claim["formalized_declarations"]}
    register = {
        "schema_version": 1,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "purpose": "Concrete manuscript claim/evidence inventory, not a universal proof or formalization certificate.",
        "entry_point": "extension/manuscript/main.tex",
        "source_files": source_records,
        "counts": {
            "included_tex_files": len(files),
            "claim_environments": len(claims),
            "by_environment": dict(Counter(c["environment"] for c in claims)),
            "by_status": dict(Counter(c["status"] for c in claims)),
            "attached_proof_environments": sum(c["local_proof_environment_present"] for c in claims),
            "whole_environments_marked_fully_formalized": 0,
            "environments_with_partial_formal_components": sum(bool(c["formalized_declarations"]) for c in claims),
            "verified_declarations_mapped_to_precise_components": len(used_names),
            "authoritative_verified_declarations": audit["authoritative_verified_declaration_count"],
            "selected_external_prose_statements": len(external_prose),
        },
        "interpretation": {
            "local_proof_presence_is_not_a_proof_audit": True,
            "ordinary_theorem_hypotheses_are_not_all_labeled_open_research": True,
            "conditional_label_scope": "Selected transfer/deduction criteria whose quantitative, convergence, or duality inputs are supplied as assumptions.",
            "formal_mapping_scope": "Only explicitly reviewed proper components, with actual source type signatures; no full composite statement mapping is asserted.",
            "reading_review": "Statement/status annotations and partial formal correspondences are manually reviewed. This inventory generator does not itself conduct mathematical proof review; separate source-specific coverage is recorded in second-pass-math-audit.json/md.",
            "separate_mathematical_review": "extension/review/second-pass-math-audit.json",
            "source_scope_exclusions": [
                "Definitions and explanatory equations outside requested environments",
                "External results stated only in prose, except the selected fluid statements explicitly registered",
                "Theorems in cited books and papers",
                "The inherited upstream repository's separate theorem inventory",
            ],
        },
        "claims": claims,
        "external_prose_statements": external_prose,
        "formal_type_map": "extension/review/formal-type-map.json",
        "prose_research_directions": [
            {
                "name": "Arithmetic zero-location/GRH bridge",
                "status": "unresolved_research_goal",
                "status_note": "No GRH theorem is asserted; arithmetic identification and analytic convergence inputs remain obligations.",
                "source_file": "extension/manuscript/chapters/foundations.tex",
            },
            {
                "name": "Uniform metric control for arithmetic modules",
                "status": "proposed_research",
                "status_note": "Construct and certify distortion bounds with explicit dependence on arithmetic input sizes.",
                "source_file": "extension/manuscript/chapters/synthesis.tex",
            },
            {
                "name": "Resource-certified improvements to ECC quantum arithmetic",
                "status": "proposed_research",
                "status_note": "A full reversible circuit, ancilla policy, success probability, and cost comparison are required; no general speedup is established.",
                "source_file": "extension/manuscript/chapters/synthesis.tex",
            },
            {
                "name": "New lattice-cryptographic security reduction",
                "status": "not_established",
                "status_note": "Module structure and correctness identities are not claimed to prove hardness or a new security reduction.",
                "source_file": "extension/manuscript/chapters/cryptography.tex",
            },
            {
                "name": "Uniform physical Yang--Mills mass gap",
                "status": "unresolved_research_goal",
                "status_note": "Requires an analytic infrared estimate surviving the stated limits and the correct reconstructed vacuum sector; no mass-gap theorem is asserted.",
                "source_file": "extension/manuscript/chapters/synthesis.tex",
            },
            {
                "name": "Complete Lean formalization and complete linked-source proof audit",
                "status": "not_completed",
                "status_note": f"The companion verifies {audit['authoritative_verified_declaration_count']} selected declarations and documents source coverage; it does not formalize all manuscript or source theorems or fully review every outbound linked work.",
                "source_file": "extension/manuscript/chapters/source-concordance.tex",
            },
            {
                "name": "Fresh upstream continuum Navier--Stokes kernel and Comparator verification",
                "status": "not_completed",
                "status_note": "Exact upstream tools and sources were pinned. The fresh build attempt stopped at dependency artifacts after rate-limited cache retrieval; source inspection and the successful local companion checks are not substituted for that verification.",
                "source_file": "extension/manuscript/chapters/navier-stokes-release.tex",
            },
            {
                "name": "New continuum conclusions from finite learned fluid models",
                "status": "not_established",
                "status_note": "Finite energy stability, exact recurrence identities and circuit simulations do not establish mesh-uniform regularity, a hydrodynamic joint limit, unforced positive-viscosity blowup, or an improved continuum existence theorem.",
                "source_file": "extension/manuscript/chapters/fluid-structures.tex",
            },
            {
                "name": "Trained quantum fluid ToricGT with demonstrated quantum advantage",
                "status": "not_completed",
                "status_note": "The new fluid companion supplies an explicit finite circuit and constrained model proposal, with classical simulation and structural checks. It does not claim a trained fluid model, quantum hardware execution of those new examples, or a proved end-to-end speedup.",
                "source_file": "extension/manuscript/chapters/quantum-fluid.tex",
            },
        ],
        "lean_source_audit": audit,
        "verified_declarations_not_mapped_to_environment_components":
            sorted(set(audit["all_authoritative_declaration_names"]) - used_names),
        "review_findings_resolved": [
            "The duplicate AHS index statement in gauge-theory.tex now explicitly assumes connectedness; the scalar 1 in its Betti-number term is therefore justified.",
            "The Schur-complex proposition explicitly requires d>0.",
            "The exact-category Euler statement explicitly requires both short exact sequences to be admissible.",
            "Fluid derivative, discrete-memory, determinant and zero-block declarations are mapped only to their precise mathematical components; no continuum or full ODE theorem is inferred.",
            "The source's eigenvalue-only Euclidean norm inference is isolated by an explicit counterexample and replaced in local arguments by a stated metric dissipativity condition.",
        ],
    }
    type_map = formal_type_map(register, signatures)
    if any(sha(path.read_bytes()) != digest for path, digest in initial_hashes.items()):
        raise ValueError("Manuscript changed during inventory generation; wait for stable sources")
    (REVIEW / "claim-register.json").write_text(
        json.dumps(register, indent=2, ensure_ascii=False) + "\n")
    (REVIEW / "claim-register.md").write_text(markdown(register))
    (REVIEW / "formal-type-map.json").write_text(
        json.dumps(type_map, indent=2, ensure_ascii=False) + "\n")
    (REVIEW / "formal-type-map.md").write_text(formal_type_markdown(type_map))
    refresh_fluid_component_map(type_map)
    print(json.dumps(register["counts"], indent=2))
    print("Lean source audit matched all registered verification manifests and raw logs.")


if __name__ == "__main__":
    main()
