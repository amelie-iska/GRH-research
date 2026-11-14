# Independent second-pass mathematical audit

The review read **all 125 original numbered statements**, their **119 attached proofs**, and the relevant inherited hypotheses. Six general results remain cited external theorems. It also read **55 new environments**: 54 arguments and 1 open problem, across the tensor, learning/language, cosmology, and quantum ToricGT chapters. No whole composite environment is represented as fully Lean-formalized.

The original inventory is tied to commit `5ad05c809358e1d945a7d2c9d4e4077aeb33ef22`. The JSON preserves original line/hash metadata and the reviewed post-correction snapshots. The accompanying assembler does not conduct mathematical review or run Lean; its notes record the manual reading, and its checks refresh provenance.

## Resolved corrections

| ID | Claim / location | Issue and correction |
|---|---|---|
| SP-001 | orders.011 | Shortest nonzero vectors are undefined for a zero-dimensional lattice. Added dim V>0 to the metric-transport proposition. |
| SP-002 | quantum-surfaces.008 | The earlier contracted one-vertex/one-face dessin has trivial checks and no positive eigenvalue; the upper-bound proof needs a nonloop edge. Required a connected closed oriented cellulation with an edge having distinct endpoints; explicitly retained the four simulated families. |
| SP-003 | gauge-theory.008 | A unitary-valued function need not be a representation, and its character need not be positive type. Changed unitary to unitary representation in the theorem. |
| SP-004 | gauge-theory.008 | A stray comma appeared inside the conjugate-character exponent. Removed the comma, leaving the intended integer power. |
| SP-005 | gauge-theory.tex | A stray plus sign interrupted the analytic continuation sentence. Changed continuation,+and to continuation, and. |
| SP-006 | standard-monomials.016 | The weight construction took a maximum over the finite poset, which is undefined when it is empty. Handled the empty poset by A=k and the trivial flat family k[t] before the nonempty construction. |
| SP-007 | cryptography.005 | The preceding first-minimum definition needs positive lattice dimension, although the dual-basis formula itself does not. Added n>=1 only to the first-minimum sentence. |
| SP-008 | synthesis.005 | A shrinking Rayleigh-quotient example needs a nonzero space and a positive sequence index. Specified V=W=R and j>=1. |

The exact six-file source patch is `second-pass-math-audit.patch`. The findings above were applied and rechecked. No further proof failure requiring redesign was found in this reviewed scope; that statement is a review outcome, not a formal completeness claim.

## Original per-claim coverage

| Claim | Review | Checked point / limit |
|---|---|---|
| foundations.001 | local argument | Checked the normalization embedding, product-ring integrality, and conductor calculation with the stated nodal congruence condition. |
| foundations.002 | local argument | Checked conjugation by the positive square root of the metric matrix. Positivity of the metric, rather than an arithmetic analogy, gives real generalized eigenvalues. |
| foundations.003 | conditional argument | Checked the conditional Rouche argument on a small disk. Local uniform convergence and a nonzero holomorphic limit remain explicit assumptions, not established L-function inputs. |
| orders.001 | local argument | Checked the common-denominator argument using finite generation and spanning over the fraction field. |
| orders.002 | local argument | Checked construction of the finite stable lattice from generators; the order is finite over the stated base ring. |
| orders.003 | local argument | Checked finite generation, integral containment, and rational spanning of the lattice endomorphism order. |
| orders.004 | local argument | Checked left/right multiplier closure and the denominator bound; sidedness of multiplication is retained. |
| orders.005 | local argument | Checked maximal-ideal localization detects a nonzero quotient class over the stated domain. |
| orders.006 | local argument | Checked that localized inclusions imply global inclusion using the preceding membership argument. |
| orders.007 | local argument | Checked that a lattice map commuting with the smaller order extends over the common rational algebra; no unjustified integral extension is used. |
| orders.008 | local argument | Checked the two matrix-unit constructions and their natural inverses in the displayed Morita equivalence. |
| orders.009 | local argument | Checked nondegeneracy of the specified trace pairing and the dual-lattice identification; this is not an arbitrary degenerate trace form. |
| orders.010 | local argument | Checked determinant scaling of the Gram matrix under the stated full-rank basis change. |
| orders.011 | conditional argument | Added positive dimension before referring to the shortest nonzero vector. Checked both directions of the quantitative norm/minimum bounds; uniform constants are assumptions. Resolved: SP-001. |
| orders.012 | local argument | Checked the involution reverses products and the reduced norm is central in the quaternion algebra before multiplying norms. |
| orders.013 | local argument | Checked that this section explicitly specializes to integer lattices and integral trace on all overorders. The finite quotient bound then follows from the trace dual. |
| orders.014 | local argument | Checked the averaging formula requires the group order to be invertible in the base; equivariance and the lifting property are separate substitutions. |
| orders.015 | local argument | Checked holomorphic group maps lift to complex-linear maps on universal covers and preserve the period lattice; the converse descends. |
| orders.016 | local argument | Checked the scalar stabilizer dichotomy in the two-dimensional rational lattice space; standard complex-torus background is used as stated. |
| orders.017 | local argument | Checked the quadratic-order conductor form and uniqueness under the fixed quadratic integer ring. |
| orders.018 | local argument | Checked the action is restricted to invertible ideal classes and the stated lattice class set; noninvertible ideals are not silently included in a torsor. |
| orders.019 | local argument | Checked the Frobenius order argument under ordinarity. The ordinary endomorphism-algebra classification and Frobenius facts remain cited background. |
| orders.020 | local argument | Checked prime-to-characteristic torsion faithfulness using the degree bound for a nonzero isogeny; characteristic-p torsion is not substituted. |
| orders.021 | local argument | Checked the extension of a right-ideal endomorphism to the rational quaternion algebra and its identification as left multiplication. |
| orders.022 | conditional argument | Checked the algebraic degree multiplication deduction from the explicitly supplied dual-isogeny identities; those identities are not proved by the deduction. |
| orders.023 | local argument | Checked the centralizer matrix equations over the stated ring and the resulting Gaussian-order form. |
| orders.024 | local argument | Checked the trace-pairing matrix and the dual basis for the Gaussian suborder; the conductor parameter is retained in the denominator. |
| complexes.001 | local argument | Checked torsion-freeness and finite generation of an extension with the stated module actions. |
| complexes.002 | local argument | Checked the split Grothendieck-group universal property against the required direct-sum relation. |
| complexes.003 | local argument | Checked the stabilization description of equality in the group completion; cancellation is not assumed without stabilization. |
| complexes.004 | local argument | Checked both short exact sequences are admissible in the chosen exact structure before the Euler relation is formed. |
| complexes.005 | local argument | Checked the bounded-end induction splitting an acyclic complex of projectives; boundedness is essential. |
| complexes.006 | local argument | Checked the pullback construction and two split projections used in Schanuel's lemma. |
| complexes.007 | local argument | Checked finite presentation by a free order module and that its kernel is a lattice under the chapter's ring hypotheses. |
| complexes.008 | local argument | Checked the denominator-cleared embedding in a free module; it uses the specified rational-algebra setting. |
| complexes.009 | local argument | Checked the corollary uses the two preceding lattice presentation/embedding statements with their inherited hypotheses. |
| complexes.010 | local argument | Checked positive definiteness of the weight matrices gives the Gram-kernel intersection and hence its rank formula. |
| complexes.011 | local argument | Checked image containment, rank-nullity, and the three cohomology dimensions; two exact rank components have separate Lean support. |
| complexes.012 | local argument | Checked cancellation of the adjacent ranks in the alternating dimension sum. The Lean arithmetic identity covers only the final substitution. |
| complexes.013 | local argument | Checked compatible bases splitting image, homology complement, and a preimage complement; this is a field argument. |
| complexes.014 | local argument | Checked the fixed-rank parameter count with the image-in-kernel condition and the rank-feasibility inequalities. |
| complexes.015 | local argument | Checked the derivative BA'+B'A and the kernel/rank calculation at the stated normal form. |
| complexes.016 | local argument | Checked the transverse block directions against the tangent equation, without identifying every first-order direction with an actual deformation. |
| complexes.017 | local argument | Checked the Jacobian of x dot y in four coordinates, smoothness away from the origin, and the singular origin. |
| complexes.018 | local argument | Checked graded signs in the endomorphism differential and d squared equals zero from the underlying complex relation. |
| complexes.019 | local argument | Checked the coefficient of the second-order deformation equation; the cohomology class is an obstruction rather than a universal existence theorem. |
| complexes.020 | local argument | Checked row and column elimination at a unit pivot and the induced smaller zero-composite relation over the stated ring. |
| complexes.021 | external statement | Reviewed the statement's rank and ideal-grade hypotheses and citation. The general Buchsbaum--Eisenbud proof is external, not independently reconstructed here. |
| complexes.022 | local argument | Checked the regular-sequence argument for the two-generator Koszul complex, including the use of each non-zero-divisor condition. |
| complexes.023 | local argument | Checked that tensoring preserves the exact sequences under flatness; arbitrary nonflat base change is excluded. |
| complexes.024 | local argument | Checked wedge/contraction expansion and signs on decomposable exterior tensors. |
| complexes.025 | local argument | Checked selection of a vector pairing to one with a nonzero covector and the resulting contracting homotopy. Lean covers the abstract middle-exactness consequence only. |
| complexes.026 | local argument | Checked the finite-dimensional orthogonal decompositions and harmonic/cohomology identification; no infinite-dimensional closed-range conclusion is inferred. |
| complexes.027 | external statement | Reviewed the elliptic-complex and compactness hypotheses and attribution. The Atiyah--Singer index theorem is external, not a local proof. |
| complexes.028 | local argument | Checked the curvature computation d_A squared equals bracket with curvature using the specified conventions. |
| complexes.029 | local argument | Checked the self-dual projection makes the composite vanish at an anti-self-dual connection. |
| complexes.030 | local argument | Checked injectivity and image/kernel equality of the nonzero-covector ASD symbol sequence; this does not supply a spectral lower bound. |
| standard-monomials.001 | local argument | Checked alternating relations give spanning and the determinant coefficient maps give independence over the stated commutative ring. |
| standard-monomials.002 | local argument | Checked row/column index conventions and the Cauchy--Binet expansion via exterior powers. |
| standard-monomials.003 | local argument | Checked shuffle signs and that the identities use no division, so they remain valid over the stated ring. |
| standard-monomials.004 | local argument | Checked the contraction/creation identity and the chosen unit pairing; abstract homotopy-to-exactness is now separately formalized. |
| standard-monomials.005 | external statement | Reviewed the integral Schur basis statement and its hypotheses. The general ABW basis theorem remains external; elementary cases are proved separately. |
| standard-monomials.006 | local argument | Checked the one-row, one-column, and elementary mixed Schur identifications with the chapter's convention. |
| standard-monomials.007 | local argument | Checked characteristic zero and positive tensor degree d, the averaging projector, and inherited contracting homotopy. The d=0 exception is excluded explicitly. |
| standard-monomials.008 | local argument | Checked rank-one straightening termination and independence by leading monomials in the specified polynomial parameterization. |
| standard-monomials.009 | local argument | Checked the three-term two-row minor relation by expansion, including the corrected cancellation monomials. |
| standard-monomials.010 | local argument | Checked the ordered straightening measure decreases and distinct standard tableaux have distinct diagonal leading monomials. |
| standard-monomials.011 | local argument | Checked the quadric relation, its basis, and the characteristic-zero representation calculation for the basic two-arrow complex. |
| standard-monomials.012 | local argument | Checked the complemented middle partition and dual-action convention in the bihomogeneous Schur decomposition. |
| standard-monomials.013 | external statement | Reviewed the general complex standard-basis/reducedness/normality/Cohen--Macaulay hypotheses and citations. These general source theorems are external. |
| standard-monomials.014 | local argument | Checked orbit classification by adjacent ranks, feasible degeneration to smaller ranks, and the stabilizer/parameter dimension calculation. |
| standard-monomials.015 | external statement | Reviewed the filtration and characteristic-zero splitting assumptions, endpoint zero-map conventions, and all-vertex Schur weights. The general filtration theorem is external. |
| standard-monomials.016 | local argument | Added the empty-poset case A=k with trivial family k[t]. Checked the positive weight separation and standard-monomial freeness argument for nonempty P. Resolved: SP-006. |
| standard-monomials.017 | local argument | Checked that diagonal leading terms of the two-row minors generate the initial algebra using the established standard basis. |
| standard-monomials.018 | local argument | Checked the prefix inequalities characterize the paired column semigroup and total-degree equality belongs to its lattice. |
| standard-monomials.019 | local argument | Checked normality is proved inside the common fraction field, with integral inequalities on the specified exponent lattice. |
| standard-monomials.020 | local argument | Checked the explicit monomial-basis flatness statement and distinct special fibers; flatness alone is not used to transfer every geometric property. |
| gentle-invariants.001 | local argument | Checked the rank-normal-form decomposition into the displayed indecomposable modules of the two-arrow relation. |
| gentle-invariants.002 | local argument | Checked the numerical consequence uses the complete decomposition and includes zero ranks/endpoints. |
| gentle-invariants.003 | local argument | Checked the extension complex, linearized relation, and infinitesimal base-change signs; its cohomology is not conflated with a nonlinear moduli space. |
| gentle-invariants.004 | local argument | Checked both character weights in the two-factor semi-invariant test under the fixed action convention. |
| gentle-invariants.005 | local argument | Checked the corrected explicit generator semigroup, relations, and exponent pairing; the cited source overstatement is not retained as a theorem. |
| gentle-invariants.006 | local argument | Checked the exterior-power trace expansion of det(I-tT), with finite-dimensional conventions. |
| gentle-invariants.007 | local argument | Checked determinant cancellation through invariant boundary and cycle subspaces; the cohomology factors are finite and the operator commutes with the differential. |
| cryptography.001 | local argument | Checked the cyclic hidden-kernel relation and exact coset fibers under the stated order assumption. |
| cryptography.002 | local argument | Checked character-sum cancellation by multiplication with a nontrivial character value. |
| cryptography.003 | local argument | Checked the Fourier amplitude normalization and uniform annihilator support; this is an ideal finite distribution, not a resource advantage claim. |
| cryptography.004 | local argument | Checked the displayed relation-lattice basis, determinant/covolume, and correspondence with the modular kernel. |
| cryptography.005 | local argument | Checked the transpose-inverse basis formula. Added n>=1 to the preceding shortest-vector definition; the basis formula itself also makes sense in dimension zero. Resolved: SP-007. |
| cryptography.006 | local argument | Checked integer unimodularity, inverse, and the growing norm of the second basis vector. Exact finite components have Lean proofs; the limiting operator-norm claim is prose mathematics. |
| cryptography.007 | local argument | Checked every error term in the noisy cancellation identity and the separate radius condition for decoding. |
| cryptography.008 | local argument | Checked the deterministic triangle/Cauchy bound with the stated selector coefficients; the narrower Lean binary-selector result is not identified with the whole bound. |
| cryptography.009 | local argument | Checked CRT/product decomposition componentwise. Existence, security, and cost of hypothetical recovery algorithms are not supplied by this algebra. |
| quantum-surfaces.001 | local argument | Checked permutation-cycle counts and subdivision/Euler characteristic; the closed oriented connected surface classification is background. |
| quantum-surfaces.002 | local argument | Checked the clean degree-four elliptic dessin and its genus; the contracted one-vertex example is not a positive-gap code example. |
| quantum-surfaces.003 | local argument | Checked binary incidence orthogonality gives Pauli stabilizer commutation; this uses mod-two phases rather than real incidence signs. |
| quantum-surfaces.004 | local argument | Checked connected primal and dual incidence ranks and the code-dimension count. Lean covers only the final integer Euler substitution. |
| quantum-surfaces.005 | local argument | Checked the primal/dual noncontractible cycle bounds for the rectangular periodic cellulation under its stated size conditions. |
| quantum-surfaces.006 | local argument | Checked the uniform rowspace state's star and face stabilizers and its selected logical sector. |
| quantum-surfaces.007 | local argument | Checked the RREF preparation circuit generates the stated independent-row superposition; column/pivot conventions are preserved. |
| quantum-surfaces.008 | local argument | Added a nonloop edge hypothesis to the connected closed oriented cellulation. Checked even excitation parity gives the lower bound two and the edge Pauli achieves it in the specified projector normalization. Resolved: SP-002. |
| quantum-surfaces.009 | local argument | Checked the exact star-correlator product identity and the defined four-parameter local ansatz; the formula supplies an efficient classical reference. |
| gauge-theory.001 | local argument | Checked curvature as the failure of the covariant differential to square to zero, with the same bracket/sign convention as the complex chapter. |
| gauge-theory.002 | local argument | Checked first and second variations under the stated smooth/compact assumptions and separation of the curvature and quadratic terms. |
| gauge-theory.003 | local argument | Checked the self-dual/anti-self-dual energy split and topological normalization for the classical bound; this is not a quantum mass-gap proof. |
| gauge-theory.004 | local argument | Checked the explicit nonzero-covector ASD symbol sequence and its dimension/rank calculation. |
| gauge-theory.005 | external statement | Reviewed the external AHS formula with connected closed oriented four-manifold and the bundle hypotheses. The full index theorem remains external. |
| gauge-theory.006 | local argument | Checked the finite exact family has arbitrarily small positive singular value while its exactness persists. |
| gauge-theory.007 | local argument | Checked normalized Haar integration on a finite lattice, positivity/finiteness of the partition function, and link gauge invariance. |
| gauge-theory.008 | local argument | Made rho explicitly a unitary representation, essential for positive-type closure; checked beta>=0, convergent exponential expansion, and positive tensor-power coefficients. Fixed a stray exponent comma. Resolved: SP-003, SP-004. |
| gauge-theory.009 | local argument | Checked Cauchy--Schwarz for a positive semidefinite form, null-vector orthogonality, and well-defined positive quotient. |
| gauge-theory.010 | local argument | Checked both directions of the spectral gap/Euclidean semigroup decay equivalence using the spectral theorem and the stated unique normalized vacuum. |
| gauge-theory.011 | local argument | Checked the elementary spectral models share the claimed ultraviolet leading behavior while differing at the low spectral edge. |
| gauge-theory.012 | conditional argument | Checked the norm limit argument assumes common positive gap and strong convergence of both semigroups and vacuum projectors; those uniform inputs are not built for Yang--Mills here. |
| gauge-theory.013 | local argument | Checked iteration of the nonnegative contractive recurrence and its explicit error bound; no physical renormalization recurrence is asserted. |
| gauge-theory.014 | local argument | Checked the opposite/dual action and pairing identity with the module's handedness fixed. |
| character-bridge.001 | local argument | Checked exactness after the specified localization and the exceptional fiber calculation; universal parameters are not substituted across excluded denominators. |
| character-bridge.002 | local argument | Checked the finite positive Laplacian and quantitative contracting homotopy on the stated complement; the norm bound uses the supplied positive eigenvalue. |
| character-bridge.003 | local argument | Checked pullback of the supplied character/representation along the specified algebraic map; no unconstructed analytic L-function bridge is inferred. |
| synthesis.001 | local argument | Checked the displayed periodic differentials compose to zero and their images equal the next kernels. |
| synthesis.002 | local argument | Checked the explicit derived obstruction and its nonvanishing in the stated cohomology class. |
| synthesis.003 | local argument | Checked the finite exactness and metric-gap computation for the explicitly displayed family. |
| synthesis.004 | conditional argument | Checked transport of coercivity requires a positive lower bound for the transport map; uniformity is an additional assumption. |
| synthesis.005 | local argument | Specified V=W=R and j>=1 in the shrinking transport counterexample, so the nonzero-space Rayleigh quotient and index range are explicit. Resolved: SP-008. |
| source-concordance.001 | local argument | Checked the F8/F2 counterexample to a pure-cubic claim, trace-zero depressed cubic, nonzero linear coefficient, and inverse formula using irreducibility. |

## New chapter mathematical review

The corrected tensor/learning snapshots explicitly add complex linearity to the Choi theorem, unitary scope to measurement probabilities, the identity-block eigenvalue multiplicity and nonzero-W condition, distinct-port separator gluing and erasure in the HR example, positive candidate/sample counts, and the correct lower-tail reduction. The cosmology review added a missing centering hypothesis to the conditional Gaussian formula and clarified the Stokes chain and quadratic-term wording; root applied all three and this review rechecked them. Empirical literature attribution is a separate review.

| Claim | Checked point / limit |
|---|---|
| tensor-grammars.001 | Checked finite sum definitions of composition, tensor product, contraction, and dagger with typed ports; this is a finite-dimensional interpretation. |
| tensor-grammars.002 | Checked the basis cup/cap contraction and closed-loop scalar dim H with the stated dual/conjugate conventions. |
| tensor-grammars.003 | Checked signed permutation averaging is an idempotent self-adjoint projector and its rank is the exterior dimension, including r above dim H. |
| tensor-grammars.004 | Checked exterior functoriality and the specified-index Cauchy--Binet coefficient identity. |
| tensor-grammars.005 | Checked the traceless-Hermitian normalization Tr(Ta Tb)=delta_ab/2, matrix-unit coefficient comparison, and Casimir contraction. |
| tensor-grammars.006 | Required and rechecked complex linearity. Checked Choi positivity, Kraus reconstruction, trace preservation, and the partial-trace transpose convention. |
| tensor-grammars.007 | Checked typed one-hole context induction and finite rewrite induction; probability consequences now explicitly apply to unitary circuit interpretations. Lean covers the sequential fragment only. |
| tensor-grammars.008 | Checked decreasing gate count and telescoping operator error, then the factor-two probability bound for normalized vectors. |
| tensor-grammars.009 | Checked zero composition, kernel/image quotient transport, and finite Hodge conjugacy under unitarity; invertibility alone does not imply spectral equality. |
| tensor-grammars.010 | Checked acyclic identity-block enlargement and added eigenvalue multiplicity dim W in each affected degree. The following gap-decrease example now requires W nonzero. |
| tensor-grammars.011 | Checked derivation-tree bags and vertex connectedness under distinct interfaces, fresh internal vertices, and no extra identifications. |
| tensor-grammars.012 | Rechecked the corrected six-port grammar with distinct attachments and separator edges. Its erased yield is a^n b^n c^n; the pumping and erasing-homomorphism arguments establish both non-context-free assertions. |
| tensor-grammars.013 | Checked a finite Turing transition table is simulated by local path rewrites and effective finite derivation enumeration gives the reverse recursively-enumerable inclusion. |
| tensor-grammars.014 | Checked bottom-up finite contraction cost O(m D^q) counts actual index variables/interfaces and a fixed grammar's bounded number of factors, not graph width alone. |
| learning-languages.001 | Checked exact integer balance, binary error-state recurrence, acceptance indicator, and O(log L) bit length. Temporary ReLU values need not be binary; wording now refers only to the other recurrent state variable. |
| learning-languages.002 | Checked distinguishable prefixes prove nonregularity for deterministic automata; the text now explicitly invokes finite-subset determinization for nondeterministic automata. |
| learning-languages.003 | Checked the ReLU pattern indicators on Boolean inputs and their disjoint sum represent any finite Boolean mechanism, without an efficiency claim. |
| learning-languages.004 | Checked acyclic composition and the Boolean intervention multiplexer. The same exogenous assignment is held fixed for the structural counterfactual; mechanisms are supplied, not identified from observations. |
| learning-languages.005 | Checked both observational distributions and their different do(X=0) laws. The impossibility is identification from the specified observational law, not inability of any architecture to compute a supplied mechanism. |
| learning-languages.006 | Checked soundness is pathwise for every finite accepted sequence of certified rewrites and independent of a possibly history-dependent rule-selection policy. |
| learning-languages.007 | Checked the exponentially tilted variance bound by 1/4 and Taylor integration for all real lambda, including negative lambda. |
| learning-languages.008 | Added and rechecked K,m>=1. Checked iid evaluation independent of fixed candidates, exponential Markov/union bounds, the 1-X lower-tail argument, and the empirical-minimizer 2-epsilon risk bound. |
| cyclic-cosmology.001 | Checked torsion-free metric compatibility gives the conformal connection formula, the null geodesic rescaling, and its converse. The conformal factor is smooth, finite, and strictly positive on the stated domain; the singular crossover is excluded. |
| cyclic-cosmology.002 | Checked p-form and volume scaling in arbitrary signature, wedge nondegeneracy, and source-free Maxwell invariance for n=4,p=2. Detector energy, charged matter, and boundary regularity are separate assumptions. |
| cyclic-cosmology.003 | Checked the four simple branch points, two unbranched points at infinity, connectedness, Euler characteristic, and nonvanishing differential in all charts. The real expanding branch and coefficient-field extension qualifications are explicit; a repeated-root quartic is excluded. |
| cyclic-cosmology.004 | Checked symmetric spinor contraction annihilates the symmetrized derivative, divergence plus complex self-duality implies closedness, and Stokes gives equality for the bounding oriented piecewise-smooth chain with smooth fields. This is conditional on the two displayed field equations. |
| cyclic-cosmology.005 | Checked nonnegative finite relative entropy, both mutual-information chain rules, and the conditional Markov version. No sender or end-to-end physical channel is constructed by the inequality. |
| cyclic-cosmology.006 | Checked the signed variation decomposition, stochastic-kernel contraction, and exact 1/K success bound for observationally identical equally likely messages, including abstention. |
| cyclic-cosmology.007 | Checked the finite alphabet entropy bound and conditional-error decomposition for Fano's inequality. Independent decoder randomization can be adjoined without changing message mutual information. |
| cyclic-cosmology.008 | Checked positive/negative parts of a Hermitian difference and trace preservation give trace-norm contraction; zero trace and 0<=E<=I give the measurement bound. Complete positivity is not needed for this particular conclusion. |
| cyclic-cosmology.009 | Checked the two-state trace-distance formula and strict increase under tensor squaring for overlap strictly between zero and one; deterministic channel contraction excludes the proposed cloning map. |
| cyclic-cosmology.010 | Checked the Kraus completeness relation, rectangular trace cycling, and equality against all observables imply equal reduced states after an unconditioned local operation. |
| cyclic-cosmology.011 | Checked Gaussian diagonalization, quadratic mean/variance, linear variance, and vanishing third-moment cross term. Replaced the misleading word centered for the noncentered chi-square sum. |
| cyclic-cosmology.012 | Checked nonzero fixed template and known positive covariance give a strictly convex scalar likelihood, inverse-information variance, and normalized score law. Data-driven template selection is treated separately. |
| cyclic-cosmology.013 | Checked exchangeability gives a uniform descending rank without ties and counting the entire tied block gives a conservative p-value. A fitted-parametric bootstrap is not asserted automatically exact. |
| cyclic-cosmology.014 | Checked isotropic harmonic covariance plus Gaussianity gives independent real coefficients and variance 2 C_l^2/(2l+1). The argument uses the standard irreducibility of a fixed-degree spherical-harmonic space; masked-sky estimators are excluded. |
| cyclic-cosmology.015 | Checked full-column-rank nuisance design, whitening, orthogonal projection, and the Schur-complement information. Vanishing exactly characterizes template confounding; the variance assertion requires positive remaining information. |
| cyclic-cosmology.016 | Reviewed as an explicitly open end-to-end physical/inference problem, not a proved theorem. Required crossover solutions, identifiable source laws, calibrated observables, and encoding comparisons remain tasks. |
| quantum-toricgt.001 | Checked finite backward induction, existence of outgoing choices, attainment, and termination on the ordered DAG. Negative edge costs do not invalidate the recursion because directed cycles are absent. |
| quantum-toricgt.002 | Checked the edge-potential inequalities telescope to a lower bound, equality certifies a legal path, and Bellman potentials attain it. Prediction accuracy and certification/repair success remain distinct. |
| quantum-toricgt.003 | Added and rechecked distinct source and target. Checked extraction of one positive integral path, subtraction, and absence of any remaining nonnegative zero-boundary DAG circulation. |
| quantum-toricgt.004 | Checked all weak-duality inequality signs: z<=0 reverses the H constraint, u<=0 uses x<=1, and x>=0 permits multiplication of the coordinate dual bound. Equality certifies only the specified feasible instance. |
| quantum-toricgt.005 | Checked the backward cyclic shift gives VU=omega UV, the nontrivial character sum vanishes, and q^2 nonzero orthogonal Weyl matrices form the matrix basis. Rational phase does not mean rational matrix entries. |
| quantum-toricgt.006 | Checked unitary gate normalization, Hermitian observables for real/imaginary Weyl expectations, feature range, and the two-term norm perturbation bound. Separate preparations can be needed for noncommuting observables; the reported model uses exact simulated expectations. |
| quantum-toricgt.007 | Checked the Pauli exponential expansion, real sinusoidal expectation, and plus/minus pi/2 shift rule for one gate occurrence. The full nonlinear loss is not assigned this two-evaluation rule. |
| quantum-toricgt.008 | Checked the multivariable chain rule with independently named occurrences, summation over shared offsets/tokens, and original-feature classical adjoints. Reused input angles need both occurrence contributions; max-plus ties do not have a unique derivative in general. |
| quantum-toricgt.009 | Checked finite maxima can be reordered and regrouped, with max(empty)=-infinity explicitly set. The conclusion applies to fixed score/value contractions, not to the whole nonlinear network. |
| quantum-toricgt.010 | Checked token permutation through feature maps, row operations, two-sided score permutation, soft/max attention, and separately normalized dispatch/combination. Endpoint renaming preserves equality data; byte attributes and padding masks must be transported. |
| quantum-toricgt.011 | Checked grouping by equal Laurent exponent gives the full binomial kernel and path incidence telescopes. The grading incidence convention is separated from the opposite flow convention before the following proof. |
| quantum-toricgt.012 | Checked zero-boundary integral rewrites plus explicit nonnegativity preserve the unit-flow constraint and hence a legal path only under the ordered-DAG hypotheses. Cost change is exactly the linear functional of the rewrite. |
| quantum-toricgt.013 | Checked the strict affine margin bound, its Cauchy--Schwarz sufficient condition, and constant-score case. A nonlinear encoder can have a disconnected/nonpolyhedral inverse image of a feature-space region. |
| quantum-toricgt.014 | Checked each independent offset occurs in one Pauli gate, whose derivative norm is 1/2; telescoping unitary products gives the l1 state bound and six expectation bounds give the sqrt(6) feature bound. Token inputs and the encoder are held fixed. |
| quantum-toricgt.015 | Checked the generated even-sum lattice, explicit even/odd nonnegative decompositions, and saturation relative to that lattice. The point (1,0) is outside the group and is not a saturation hole there. |
| quantum-toricgt.016 | Checked the triangle boundary matrix has rank two and kernel span(1,1,1); the filled triangle adds that image. The point/boundary/fill inclusions give first Betti numbers 0,1,0, disproving both unqualified monotonicity directions. |
| quantum-toricgt.017 | Checked nonempty feasible basis set, a normalized initial vector, and unitaries commuting with its projector imply subspace preservation and probability-one feasibility. The diagonal cost expectation is a convex average, and a positive nonoptimal cost gap gives the stated probability bound. This is a conditional future interface, explicitly not the trained three-qubit feature circuit. |

## Actual Lean verification

All three current modules were freshly passed to the Lean 4.24.0 kernel in the pinned mathlib environment. Each command exited zero. The raw output and command metadata are retained in `second-pass-math-audit-core-kernel.log` and `.json`.

| Module | Named declarations | Result |
|---|---:|---|
| BridgeTheorems.lean | 25 | Kernel exit 0; source hash retained |
| QuantumInterfaces.lean | 7 | Kernel exit 0; source hash retained |
| DiagramGrammar.lean | 16 | Kernel exit 0; source hash retained |

The new 16 declarations cover contextual soundness of a typed sequential syntax, structural/inverse-equivalence rewrite rules, tensor/trace identities as separate finite-matrix components, chain/exactness transport, contracting-homotopy exactness, and finite Hodge-matrix conjugacy. The dependency logs report only `propext`, `Quot.sound`, and, for some results, `Classical.choice`; no project axiom or admitted proof occurs. These foundational axioms are not described as absent.

`build_claim_register.py` now checks source hashes, declaration inventories, raw axiom logs, and exact label-based component mappings for the third module. Its inventory run does not itself invoke Lean. The new module prints its full kernel types, preserving implicit section parameters in the register.

## Remaining scope boundaries

- No claim that every assertion in prose, every theorem in a cited source, or all inherited upstream files has been independently proved.
- Six original general theorems remain cited external results; their statements and use were reviewed, not their full original source proofs reconstructed.
- Empirical/source-attribution assessment of the Chomsky and language-model literature belongs to the separate root research review.
- Experiment implementation audits, figure rendering, measured training results, and browser checks have separate records; this ledger records mathematical reading rather than independently rerunning those experiments.
- Cosmology source attribution and synthetic-code verification are separate from this mathematical review. The missing centered-Gaussian hypothesis in the conditional-polarization formula was corrected by root and independently rechecked.
- No complete composite manuscript environment is marked as kernel formalized. The claim register records narrowly typed partial components.
- The Lean syntax covers typed sequential composition and one-hole contexts. It does not implement a full symmetric monoidal/traced/dagger graph syntax, channels, graph isotopy, parser correctness, completeness, or confluence.
- No proof of GRH, a Yang--Mills mass gap, quantum computational advantage, or observational cosmological communication is asserted.

The review is reproducible as a provenance record by running `python3 extension/review/second-pass-math-audit.py`. Re-running that assembler does not replace human mathematical review after a substantive source change.
