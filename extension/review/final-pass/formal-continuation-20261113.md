# Formal verification continuation

**Review date:** 13 November 2026, Pacific. The final inherited-package check
completed at `2026-11-14T00:32:45.461719+00:00`.

**Result: 483 distinct project declarations in 43 source files passed fresh
Lean elaboration, with zero warnings and complete printed-type and
foundational-axiom evidence.** This comprises 115 selected extension
declarations, seven original arithmetic declarations, and 361 public
theorem/lemma declarations in the original analytic package. No mathematical
theorem source was changed in this continuation. The work strengthens the
verification process and establishes current evidence for existing proofs.

| Package | Source files | Verified declarations | Warnings | Current evidence |
|---|---:|---:|---:|---|
| Extension interfaces | 6 | 115 | 0 | [Extension manifest](../../lean/final-verification/verification.json) |
| Original arithmetic package | 1 | 7 | 0 | [Combined inherited manifest](../../lean/inherited-verification/all/verification.json) |
| Original analytic package | 36 | 361 | 0 | [Combined inherited manifest](../../lean/inherited-verification/all/verification.json) |
| **Distinct total** | **43** | **483** | **0** | Separate package scopes are preserved |

The extension manifest SHA-256 is
`0e22a8acbc9e9076a63af813d2f719cd64e27d30256f6f37c4950d77ac0868c8`.
The combined inherited manifest SHA-256 is
`36f8dab6e560e0c00be039081e7dc9ff060c0fa439a50c59bbf811f5eb6e0ce3`.
Each manifest records the individual source and raw-output hashes. Reported
axiom dependencies are subsets of `propext`, `Classical.choice` and `Quot.sound`;
none of the verified declarations depends on `sorryAx` or an additional
unproved project axiom.

## Fresh-check acceptance policy

The previous extension driver recorded warning counts but did not include a
zero-warning requirement in its own success condition. The downstream claim
register already rejected warnings, and the previous actual extension run had
zero warnings. The defect was therefore a disagreement between acceptance
policies, not evidence that a previously checked theorem had an admitted proof.

`verify_all.py` now passes `-DwarningAsError=true` to Lean and independently
requires warning-free output, a printed type for every selected declaration,
the complete expected axiom inventory, permitted foundational dependencies,
zero process exit status, and source stability. It snapshots the checker,
configuration, compiler and dependency-manifest hashes before checking and
requires those bytes to remain unchanged afterward. The final 115-declaration
run passed this stricter policy.

The [fresh-checker regression suite](../../lean/verify_verifier_gate.py) uses
actual compiler output from five temporary fixtures. Its nine checks cover
acceptance of a proved statement; rejection of a warning despite Lean's zero
exit status; compiler-level warning promotion; an admitted proof; an additional
project axiom; a missing printed type; a missing axiom report; a source-change
flag; and a nonzero exit status. The deliberately invalid fixtures are never
installed as project theorem sources.

Both the [ordinary regression record](../../lean/verifier-gate-verification/verification.json)
and [optimized record](../../lean/verifier-gate-optimized-verification/verification.json)
pass all nine checks. Explicit conditional failures remain active under
`python -O`. The existing claim-register gate separately passes all six of its
source/log/type/scope checks in both ordinary and optimized Python. These
regression counts are not additional theorem counts.

## Portable verification of the original packages

The original shell entrypoints assumed a local Darwin ARM toolchain. They now
delegate to [verify_inherited.py](../../lean/verify_inherited.py), accepting
explicit existing toolchain and mathlib paths, or the corresponding
`GRH_LEAN_TOOLCHAIN` and `GRH_MATHLIB` settings. The driver does not silently
invoke an installer or download dependencies.

```sh
sh scripts/check_lean.sh --toolchain /absolute/path/to/lean-4.24.0-linux
sh scripts/check_analytic.sh \
  --toolchain /absolute/path/to/lean-4.24.0-linux \
  --mathlib /absolute/path/to/mathlib4-v4.24.0

python extension/lean/verify_inherited.py \
  --toolchain /absolute/path/to/lean-4.24.0-linux \
  --mathlib /absolute/path/to/mathlib4-v4.24.0
```

The arithmetic shell entrypoint also passed an actual invocation on the Linux
toolchain. Both scripts pass shell syntax validation. The combined command
freshly checked all 37 original-package modules and all 368 inventoried public
declarations, with no dependency blocks remaining.

The new inventory resolves namespaces and sections, ignores comments and
strings, and includes attributed public declarations and public lemmas. The
analytic source has 361 such declarations. Its older 342-declaration README
count belonged to an earlier snapshot; a simple scan for lines beginning with
`theorem` also undercounts attributed declarations and the public helper lemma
`GRHResearch.ThetaTameDescent.cubic_fourth`. The new audit prints the type and
axiom dependencies of that helper as well. Private helpers are elaborated with
their containing files but are not separately added to the public count.

The compiler is Lean 4.24.0, revision
`797c613eb9b6d4ec95db23e3e00af9ac6657f24b`. Mathlib is the clean tracked checkout
at `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`, with its dependency manifest
matching the repository's pinned manifest. The actual commands used the
existing toolchain and checkout under
`/workspace/scratch/70763186a94c/.tooling/`.

## Dependency recovery and preserved failure evidence

The first inherited run checked 117 declarations in 16 modules but could not
elaborate 21 modules because required compiled mathlib imports were absent.
That [before-cache evidence](../../lean/inherited-verification/before-cache/verification.json)
remains historical. Missing imported objects were an environment limitation;
they were not treated as successful theorem checks or as mathematical
counterexamples.

Twelve missing import roots required 662 additional pinned compressed cache
artifacts. Existing compressed artifacts were reused in an isolated cache.
The initial unpack also fetched the `leantar` 0.1.15 utility there; its final
bytes match the existing local utility. No global configuration was modified.

The scoped download used sequential requests at two requests per second,
zero per-transfer retries, and an immediate stop condition for HTTP 429.
An initial 120-second cap was extended within a cumulative ten-minute/1 GiB
budget. One continuation's controller encountered a temporary-file
rename/stat race. The successful downloads were preserved, the controller was
made tolerant of disappeared temporary paths, and one bounded repair
continuation completed the same pinned targets. The receipts retain these
interruptions rather than assigning an unobserved successful exit to them.

The [final recovery receipt](../../lean/inherited-cache-recovery/cache-repaired-continuation.json)
records exit zero, no remaining missing roots, 29,519,276 new compressed-cache
bytes, and 471.2 seconds of cumulative recovery wall time. There was no HTTP
429 in this recovery. The final full inherited proof run was performed after
the required imports became available.

## External Navier–Stokes status remains separate

The upstream development uses Lean 4.34.0-rc2 and a different mathlib pin.
The successful Lean 4.24.0 recovery and local checks do not verify that external
development.

The [historical upstream attempt](../navier-stokes/final-pass-upstream-recheck.json)
is already closed with status `historical_attempt_closed_unverified` and
`terminal: true`. Its `original_status: running` field records historical
provenance; it is not a claim of a currently running build. The authoritative
[later upstream record](upstream-build-current.json) reports an HTTP 429 cache
block, process termination with exit `-15`, no completed full target build,
and no independent Comparator run.

This continuation re-inspected both cached upstream checkouts at
`f9e8bc5b38b6e212696e8a30e3e91517af887bbd`. Each still has zero compiled
`NavierStokes` module objects and no `ComparatorSolution.olean` endpoint. No
new upstream 4.34 build or network retry was launched.

## Interpretation and remaining mathematical obligations

These results establish that the listed formal declarations elaborate and have
the recorded types and axiom dependencies in the pinned environment. Cached
compiled imports and the named compiler remain trusted; this is not a rebuild
of the compiler or every dependency from source. Hashes bind records to bytes
and are not digital signatures.

The 483 count combines separate formal packages. It does not assert that all
manuscript environments are formalized, that each prose interpretation has been
independently justified by this automated audit, or that the project has proved
GRH, a continuum Yang–Mills mass gap, an unforced Navier–Stokes result, a quantum
speedup, or security of the implemented cryptographic protocols. Arithmetic
identification, continuum estimates and the separately documented external
build obligations remain explicit. No additional mathematical hypothesis was
silently introduced to make these checks pass.
