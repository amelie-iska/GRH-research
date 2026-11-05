# Independent profile-uniformity implementation audit

Verdict: **PASS** for the frozen six-case v2 implementation and exact artifacts. No author arithmetic/test/case routine was called to establish this verdict. The code/proof interface in the canonical root proposals listed below also passes; the separate independent prose reviewer owns the full asymptotic/conductor proof review.

## Independent reconstruction

The accepted reviewer uses Eratosthenes primes followed by ordinary trial division, rather than the author's SPF. For every integer N in every strict annulus D<N<2D it reconstructs the rational factorization, rejection reason, allowed squarefree ideal norm group, actual prime-ideal norm multiset, ideal multiplicity, Mobius sign, DUPLICATED divisor norms, strict long-factor count r_U and original high-window A_U=mu(r_U−1). The complete partition, all group tables, profile exponents and histograms match.

The multiplicity calculation enumerates explicit ideal-support choices: one of two conjugate primes at split exponent1, BOTH at split exponent2, and the unique inert prime ideal at inert exponent2. It does not collapse ideals to rational norm. All30482 norm groups and1219280 allowed-multiplicity entries across all six D cases were independently reconstructed. A separate direct primary-ideal enumeration for D256/1024 reconstructs368 actual columns, the original ternary divisor-placement coefficient A_U and split/inert finite-field unit symbols. It matches every norm-fiber multiplicity, including the squarefree split products and inert prime ideals at nonsquarefree rational norms.

All40 canonical ideals v with Nv<=64 were independently enumerated by six-unit associate orbits and factored by exact Eisenstein division. Their literal epsilon*beta_v^6 elements, prime supports, exponents, squarefreeness flags, good-S flags and serialized coverage tables match. All14720 actual small-D tower symbols were independently computed in split residue fields and genuine inert F_(p^2) fields. Every raw zero and surviving aligned term matches the mask (m,v)=1. The two non-squarefree prime squares and the squarefree conjugate product at norm49 have distinct masks; using norm49 alone would be wrong.

Every T_v, allowed-column count and exact row energy T_v^2/D matches. All primary good-S cumulative caps, secondary [X/2,X) caps, empty blocks, and exact sum/energy statistics match for all six cases. The primary X64 family has19 rows; the diagnostic table has40 ideals. These counts are not interchangeable. The capacity-matched H=floor(D^(3/4)) gives X2,2,2,3,4,4 and contains only the good-S unit ideal at these modest finite scales. Fixed-X64 data are correctly labelled a different H=X64^6 range.

For both small cases all80 selected-row h1 ordered-pair numerators and their cumulative sums were recomputed using actual prime-ideal support disjointness and absolute A_U weights. They match the saved independent-small-checks table. This is a selected-row h1 calculation; it does not lower-bound the h1 component over other literal rows. The full nonnegative row energy may be lower-bounded by selected-row energies, exactly as the implementation states.

## Profiles, complex arithmetic and limits

The main common profile has node sign(A_U)*conjugate(chi_m(epsilon)); epsilon=1+omega is (1,1) in the omega basis. Independent exponentiation confirms the unit exponent(N−1)/6. Thus the surviving original coefficient is |A_U|; collisions remain zero. The real−1 witness is retained separately. The unsigned comparator ALSO varies with D. Integer centers strictly between D and2D and bump radius1/(4D) place disjoint supports strictly inside(1,2); endpoints vanish and derivatives have O_k(D^k) growth.

The exact unsigned order6 sums and energies were reconstructed in doubled rational/sqrt(−3) coordinates. This confirms a^2+ab+b^2, rather than a^2+b^2, for zeta6 coordinates. All six unit energies, coefficient-count lower bounds, comparator energies, manifest minima and summary histograms match. Minimum observed E/D is1311025/16777216, a finite observation rather than an asymptotic proof.

The primitive epsilon character has order6: a norm7 prime has value zeta6, so its proper powers1..5 are nonprincipal. Multiplying by an ideal sixth power preserves that primitive character while retaining the literal raw zeros. The experiment intentionally makes NO exact-conductor claim. The canonical prose supplies its own exact432/27/16 conductor proof; those numbers are not being inferred from these finite tables. Principal nu=1 and S above2,3 are the experimental scope. Finite table data do not extend that scope to arbitrary twists, fixed W, bounded derivatives or a GRH result.

One serialization contract is explicit: JSON object keys in split_prime_coverage are strings. The author's accepted generation works on fresh integer-key canonical objects, and all saved mask vectors are correct. A caller reusing the integer-key allowed_multiplicity helper on decoded JSON must first normalize these keys. This is documented in the frozen handoff; the independent audit did not call that helper or silently coerce away the issue.

## Negative controls and byte binding

Independent negative controls distinguish repeated ideal divisors from deduplicated rational divisors: at norm1369 and U32 the actual long-factor count is2; deduplication gives1 and an incorrect zero A_U. Norm49 prime squares versus conjugate product give different T_v. Raw collision restoration, false principal epsilon classification, and ordinary Euclidean coordinate norm are inconsistent with the reconstructed values.

The source freeze, all eight current source/helper files, all source snapshots, every input/summary/small-check artifact and the external manifest digest match before and after review. In-memory changes to a source, a norm-group input and a summary are rejected by the author's hash-verification contract; no protected bytes were mutated. Existing-output refusal passes. Author tests, compute_case and run were not used for the independent arithmetic audit. The only author functions invoked were read-only hash/output refusal contracts under memory patches.

The accepted exact reviewer reports1721320 grouped check units. No old15-column learning trace, old991 Gauss test, dependency, GPU, compiler/Lean, browser, authentication, publication or production write occurred.

## Canonical proof interface

The canonical root core/details bytes are bound in acceptance-v1.json. Their integer-D strict-interior profile removes the endpoint issue; U=sqrt D is exact in the theorem and sampled at square D in this implementation. The proof's cumulative Nv<=X family is the primary statistic. Its secondary half-open dyadic range may be empty at small X, as the code records. The exact row-conductor assertion is a separate analytic/algebraic proof, not a finite-code claim. The coprime-triple density and outer-row positivity argument keep selected h1 positivity distinct from the full signed h1 sum and require D,X to grow; finite experiments assert no asymptotic density theorem. The orientation-mean fixture and projection discussion are consistent with the accepted fresh joint note.

No code/proof interface correction is required. No fixed-profile target, adequate derivative-dependent estimate, new signed upper bound, determinant/zero-location bridge, Lean or GRH claim is refuted or proved by the implementation.
