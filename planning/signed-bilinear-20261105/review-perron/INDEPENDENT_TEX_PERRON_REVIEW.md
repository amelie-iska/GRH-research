# Independent TeX review: Perron portions of signed-bilinear shared sources

5 November 2026. Remote Linux only. **ACCEPTED for mathematical semantic faithfulness, at the exact hashes below.** No remaining correction is required in the reviewed Perron portions.

Scope is limited to the final core paragraph “The two-cutoff contour remains coupled” and the details subsection “Double Perron without a divergent critical-strip series”. Whole-file hashes bind the sources, but this receipt does not independently accept their high-window, factor-Cauchy or finite-covariance portions. Those belong to the separate reviewer. This is a mathematical/source review before compilation; it is not a compilation or rendered-layout receipt.

| Source | SHA256 |
|---|---|
| papers/signed-bilinear-core.tex | c5a181f3f457aad2d2a2010bdf48f0319493ce238003ed9586a1a91c6ff168d7 |
| papers/signed-bilinear-details.tex | 57c7fa845ae952fe5cbec91ad1b4a9227713e2f48c34e489a0d3ab718737f6f6 |
| accepted planning derivation DOUBLE_PERRON.md | e8549e3c576defc7a96b703240a9e51ad9daf6cc1e3ce8077ec37effbbce4e97 |

## Faithfulness findings

1. The inherited actual Eisenstein family, fixed finite-order nu and S, common smooth W and raw shared-prime zeros are retained. The full T0 remains S union support(u); psi_2 is formed independently as the primitive square character. F0 has the correct original incomplete ratio L^T0(s,psi)/L^T0(2s,psi_2). No primitive-conductor drop restores a forbidden original prime.

2. The local three-placement factor, the correction R and the identity used to derive it agree exactly with the accepted derivation. The G series retains squarefreeness, disjoint a,b support and T0 deletion. Its absolute region sigma+Re z>1 and sigma+Re w>1 for sigma>1/2 is correct. The text explicitly avoids evaluating the original infinite c series in the critical strip.

3. The correction’s Omega domain, local majorant and fixed positive eta/epsilon margins agree with the accepted normal-convergence proof. Its upper bound is uniform in all vertical parts and phase/deletion choices. Nonvanishing is explicitly unasserted. Nothing here supplies critical-strip reciprocal-L bounds.

4. Perron is restricted to fixed 1/2<sigma<1 and positive c,d>1-sigma. V=floor(U)+1/2 gives the exact inclusive sharp cutoff, including norm equality endpoints and distinct equal-norm ideals in the two variables. Delta_V now explicitly takes its infimum over integers n>=1; the bound 1/(2V+1) is valid. The Perron kernel K is now defined with c,T>0, v>0, v!=1 before its tail bound. Those two self-containment clarifications resolve the only requested source changes.

5. Equation sb:perron-error has exactly the accepted constants, V power and three finite-height error terms. The same coprime coefficient sum A is used. Finite-height integration is justified by the absolute G series. Both heights tend independently to infinity; the text identifies an oscillatory limit and retains the original principal-pole exclusion. It does not claim an absolutely integrable infinite vertical integral.

6. The safe contour bound retains (Nu)^eta |L(s,psi)|, fixed sigma/margin/nu/S dependencies and the logarithmic factors. The displayed amplitude and energy exponents agree with U^(2-2sigma+eta) and U^(2-4delta+eta). The common-profile Mellin insertion explicitly retains M_4(W)^2, height/conductor uniformities and the absence of a derivative-free improvement. “Fixed margins and sigma” means fixed delta in (0,1/2); this acceptance grants no uniformity as the principal pole line is approached at delta=1/2. The concise core reference to the previous U power is read with these small-loss and fixed-parameter details.

7. The reciprocal zero divisors z=rho-s and w=rho-s are preserved as an obstruction requiring new estimates. The coordinate-slice identity is explicitly meromorphic. The added numerator-zero caveat correctly forbids substituting a pointwise zero numerator before restricting to the slice. Single boundary integrals and crossed-zero residues remain present. The double kernel residue is stated only away from s zeros/poles. A principal L pole gives a reciprocal zero. No universal cancellation, new zero-free premise or consequence of numerator AFM is smuggled in.

The two numbered equation labels sb:perron-factor and sb:perron-error correctly attach to the factorization and finite-height error. The core/detail semantic linkage is faithful to the accepted proof.

## Evidence and limits

The original independent prose audit and exact finite controls remain the evidence for the unchanged mathematical content:
planning/signed-bilinear-20261105/review-perron/INDEPENDENT_ADVERSARIAL_REVIEW.md and
outputs/checks/2026-11-05-signed-bilinear/review-perron/independent-acceptance-v1.json.
Their source bindings were revalidated for this review. The unchanged finite checker was not rerun merely for prose TeX transcription; its existing 960 local identities, 192 global finite cases and endpoint/mask negative controls are not being presented as new analytic evidence.

No compilation or browser/layout test was performed by this reviewer. The parent’s staging build is a separate gate. This reviewer wrote only new assigned review artifacts, and made no production, wrapper, queue, auth, dependency, MCP or publication changes. No new analytic saving, BT_sigma, reciprocal/residue estimate, energy lower bound, Lean theorem or GRH result is accepted.

Disposition: the Perron portions are ready for the parent’s staging compilation and layout verification at the exact source hashes above.
