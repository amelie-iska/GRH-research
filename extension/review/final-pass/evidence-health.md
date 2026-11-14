# Evidence integrity and the upstream verification boundary

This publication check binds the selected verification records to the current
source files and authentic retained execution logs. It performs no downloads and
does not rerun Lean. Its JSON output is deterministic for identical input files.

## Current outcome

The checked local record covers **115 declarations in six finite-interface Lean
modules**, and the cryptography record covers **25 functional and tamper-rejection
tests**. Their source, driver, configuration, and log hashes agree with the current
files. The Lean logs contain the exact recorded declaration-level axiom reports,
with no dependencies beyond `propext`, `Classical.choice`, and `Quot.sound`.

**The upstream continuum Navier–Stokes final kernel build remains unverified by
this project.** The separate current source audit and failed cache retrieval are
internally consistent with this explicit blocker. Passing this integrity check
does not promote a source audit into a successful proof build.

The machine-readable result is [evidence-health.json](evidence-health.json). It
records every checked input hash, the actual check count, and the outcomes of
eight in-memory negative controls. The controls reject a changed Lean source, a
changed Lean log, a wrong Mathlib pin, an unapproved axiom, a stale running status,
a source audit mislabeled as kernel success, a claimed endpoint build with no
endpoint log/axiom evidence, and a changed cryptography implementation.

## Reconciliation of the historical running record

`../navier-stokes/final-pass-upstream-recheck.json` previously contained only a
start record and still said `running`. It now has the terminal status
`historical_attempt_closed_unverified`. Its original start time, intended
configuration, dependency pins, and original-record hash remain recorded.

The record does not invent an exit code for that earlier attempt. Instead it
points, by path and SHA-256, to the later complete
[upstream-build-current.json](upstream-build-current.json), which records the
bounded retry's actual HTTP 429 diagnostics, termination, and incomplete build.
The two configurations are explicitly distinguished. The historical settings
must not be cited as the effective throttle of the later retry.

A read-only inspection of both existing upstream checkouts found no compiled
`NavierStokes` module artifacts or `ComparatorSolution.olean`. Therefore there is
no already compiled endpoint available for a cheap replay. No new network retry,
source modification, toolchain change, or full upstream build was attempted in
this reconciliation.

## Reproduce

From the repository root, with Python 3.11 or later:

```sh
python extension/review/final-pass/check_evidence_health.py \
  --self-test --output-dir extension/review/final-pass
```

Omit `--output-dir` for a read-only check. The negative controls override file
bytes in memory and never modify sources or evidence. All checks use explicit
conditions, so Python's `-O` option cannot disable the gate.

The gate checks the current aggregate Lean manifest and cryptography manifest.
Older per-module records are historical and are not silently promoted when a
later source changes. The separate claim-register gate handles correspondence
between manuscript components and formal declarations.

## Requirements before a future upstream success claim

A successful `NavierStokes.ComparatorSolution` build must supply exit code zero,
the actual retained build/axiom log and its SHA-256, and an
`axioms_per_declaration` map for both exact final declarations:

- `NavierStokes.Comparator.navier_stokes_breakdown_R3`;
- `NavierStokes.Comparator.navier_stokes_breakdown_periodic`.

The check parses the actual log and compares those declarations and dependencies
with the map. Both must remain tied to the explicit pinned source audit. An
upstream metadata report alone is insufficient. The corresponding aggregate
status is `fresh_source_audit_and_final_kernel_build_passed`; the historical
superseding-evidence hash must be updated when its referenced record changes.

Independent Comparator verification is a separate obligation. This checker
currently accepts only its honestly recorded `not_run` status. A future
Comparator success requires a dedicated certificate-validation schema and
checker before that separate claim can be accepted here.

Hashes establish consistency between retained files, not independent
authentication of who produced them. These checks do not certify the semantics
of the continuum theorem encoding, the entire manuscript, GRH, a Yang–Mills mass
gap, the cryptographic security of the wrappers, or their native dependencies.
