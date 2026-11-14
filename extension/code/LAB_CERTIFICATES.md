# Live laboratory certificates

The live bridge exports exact input parameters, independently recomputable
results, and bindings to the source and compiler-printed types of named Lean
interfaces. It supports export from the current controls and validated import
back into those controls. It does **not** execute Lean in the browser.

## Supported contracts

| Contract | Exact input | What is checked | Boundary |
|---|---|---|---|
| `hodge-family-v1` | `epsilon` in `[0,1]` | The diagonal family, its scalar coercivity constant, zero/positive boundary, and finite kernel data | The original logarithmic control generally produces an irrational parameter and is not exported as a rational theorem instance. Use the separate exact input, or select exact zero. The canvas renders that rational state numerically. |
| `quadratic-cover-v1` | `power` in `{0,1,2,3}`, `x,y` on the hundredth grid in `[0,1]` | Integer powers of `J`, nonzero determinant `14^power`, exact point image modulo one | The generated Lean instance proves the determinant identity and positivity. Topological covering claims and numerical trigonometric/fibre drawing are separate. Off-grid imports are rejected instead of rounded to a slider step. |
| `weighted-gain-v1` | Nonnegative 2×2 `matrix`, positive `weights`, nonnegative `rate` | Every product, row bound, slack, row ratio, and the contraction flag | This verifies the supplied gain envelope. Proving that it dominates an actual update on an invariant domain is another obligation. A failed bound is a valid negative replay; `q >= 1` can give a holding bound without contraction. |
| `cosmology-calibration-v1` | `alpha`, `threshold`, `snr`, and exact natural `center`, `width`, `order` | Exact score/rank arithmetic on stored binary64 constants and the conditional even-moment family bound | The finite rank has no probability law asserted here. The measure theorem retains measurable-score, integrability and true-moment premises. The Gaussian law/moment identity, generator law and observational model remain separate obligations. |

Rational parameters use reduced strings `n/d`, including `/1`, with a positive
denominator and no redundant leading zeros. Cosmology's three discrete indices
use canonical natural strings. No JSON numeric literals are accepted. Input
components are bounded to 80 decimal digits. Derived rational results can be
larger; they are recomputed exactly, rather than accepted as assertions.

The browser parser also rejects duplicate keys, missing/unknown fields,
nonfinite tokens, noncanonical fractions, excessive nesting and oversized
documents. The overall UTF-8 document limit is 512 KiB. An imported certificate
cannot contain Lean source, executable code or arbitrary control identifiers.

## Import and provenance

The trusted registry is `extension/site/data/certificate-contracts.json`.
The certificate must match its theorem names, compiler-printed types, source
hashes, runtime/model hashes and toolchain identity. Source and type bindings
identify the reviewed interface; they are **not signatures or proof
authentication**. The source links point to the current repository branch and
must not be mistaken for immutable content identifiers.

Import performs all protocol, domain, binding and exact-result checks before
preparing a control mutation. The adapter then commits a reversible state
transaction, reads the controls again and compares their canonical parameters.
Failure to restore them exactly rolls the transaction back. Hodge imports select
the exact rational mode. Cover imports obey the actual slider grid. Weighted
gain inputs remain exact text, including after restoration.

## Independent replay

From the repository root, replay a downloaded JSON certificate with:

```sh
python3 extension/code/verify_lab_certificate.py certificate.json
```

This tool uses independent Python integer/Fraction arithmetic; it does not import
the JavaScript producer. For cosmology it uses the separately implemented
`cosmology_certificate.py`. The CLI also compares the trusted local source files
and recorded compiler types with the registry. It fails on stale source
bindings. A valid negative gain instance exits successfully with
`bound_holds=false`; this must not be interpreted as a holding inequality.
Malformed, stale and altered records exit nonzero. The checks remain active
under Python optimization.

## Actual Lean return path

The panel can also download `LaboratoryInstance.lean`. Save it in
`extension/lean`, use the pinned Lean/Mathlib project, and run:

```sh
cd extension/lean
lake build
lake env lean -DwarningAsError=true LaboratoryInstance.lean
```

The source is generated from fixed templates and already validated literals.
It applies the named interfaces to the current instance. Failed gain proposals
produce a theorem about an exactly violated row, rather than a false bound.
Cosmology exports instantiate the **actual measure-theoretic finite-scan theorem**
for 288 scores with all its probability assumptions explicit; they do not prove
a probability statement merely by checking scalar arithmetic. A capped bound of
one uses the uniform-bound theorem when the stronger uncapped budget premise
fails.

The selected emitted instances and negative controls are checked by
`extension/lean/verify_laboratory_contracts.py`; its evidence is kept separate
from arithmetic replay and from the aggregate formal declaration count.

## Rebuilding the registry and focused tests

After the runtime sources are frozen and the complete Lean verifier has checked
the same theorem sources, regenerate the registry:

```sh
python3 extension/code/build_lab_contract_registry.py
node --test extension/site/verify-certificate-bridge.cjs
python3 extension/code/test_lab_certificate.py
```

With the separate frozen Lean-instance audit completed, the combined evidence
runner reproduces both test suites, all eleven bound example exports and their
independent replay, then compares their emitted Lean bytes with the checked
instances:

```sh
python3 extension/code/verify_lab_bridge.py
```

Its report is `extension/verification/lab-certificate-bridge.json`; the replayable
examples and logs are in `extension/review/final-pass/lab-certificates/`.

The registry builder refuses changed Lean sources or missing compiler-printed
types. It does not compile Lean itself. Regenerating a binding after a material
source change intentionally makes old certificates fail the current-release
binding check; their original release remains the appropriate replay context.
