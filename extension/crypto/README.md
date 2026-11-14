# Standard cryptography for research artifacts

This directory contains executable encryption, signature and post-quantum key
encapsulation interfaces. Every cryptographic primitive is implemented by the
maintained `cryptography` package and its native backend. Python handles bounded
artifact framing and strict parsing. No novel cipher, lattice problem or
unproved GRH/Hilbert–Pólya claim is used as a security assumption.

## What runs

| Interface | Standard primitive | Actual behavior |
|---|---|---|
| `encrypt_artifact` / `decrypt_artifact` | AES-256-GCM or ChaCha20-Poly1305 | Encrypts bytes and authenticates the selected algorithm, format version and public context; returns plaintext only after successful authentication |
| `sign_artifact` / `verify_artifact` | Ed25519 | Signs unambiguously framed artifact bytes and application context; verification requires a separately trusted public key |
| `mlkem_encapsulate` / `mlkem_decapsulate` | ML-KEM-768 or ML-KEM-1024 | Generates and recovers a shared secret using the backend's standard key encapsulation API |

The KEM functions are deliberately a separate interface. A KEM does not
authenticate either party, encrypt arbitrary files, prevent replay, or specify
an authenticated KEM/DEM transport protocol. ML-KEM's same-length invalid
ciphertexts normally produce a rejection secret rather than an exception;
returning a value is not a validity test. Ed25519 is a classical signature
algorithm and is **not** a post-quantum signature scheme. These distinctions
are retained even when the components appear in the same research project.

The recorded run used **Python 3.12.14, cryptography 50.0.0, and OpenSSL 4.0.1**.
Both ML-KEM parameter sets executed on that native backend. This is not a claim
that the local build is FIPS-validated; using a standardized algorithm and
possessing a cryptographic-module validation certificate are different facts.

## Reproduce

From the repository root, in an environment with the recorded dependency:

```sh
python extension/crypto/verify_crypto.py
```

To prepare a separate environment when needed:

```sh
python -m venv /path/to/research-crypto-venv
/path/to/research-crypto-venv/bin/python -m pip install -r extension/crypto/requirements.txt
/path/to/research-crypto-venv/bin/python extension/crypto/verify_crypto.py
```

`verification.json` records actual versions, source hashes and the outcome;
`verification.log` records every test name. The **31 test methods** include
additional parameterized cases and tamper checks. They cover empty/binary/Unicode
payloads, each byte of the tested ciphertext/tag and nonce, wrong keys and
contexts, algorithm substitution, malformed and duplicate JSON fields, signature
changes, context-framing ambiguity, both KEM parameter sets, implicit rejection
and malformed KEM lengths. Permanent boundary regressions also cover both AEADs
at the actual 16 MiB payload and 1024 UTF-8-byte context limits, one-byte-over
payloads, oversized envelopes, multibyte contexts, noncanonical base64 pad-bit
aliases and unpaired Unicode surrogates. No test is silently skipped when a
backend is absent.

All secret keys and shared secrets are created in memory for the run and are
never written to a result file. The test report contains neither private keys
nor key material. These are regression checks, not a proof of computational
security or an independent audit of the backend's implementation.

## Example

With this directory on the Python import path:

```python
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.asymmetric.mlkem import MLKEM768PrivateKey
from research_crypto import (
    generate_symmetric_key, encrypt_artifact, decrypt_artifact,
    sign_artifact, verify_artifact, mlkem_encapsulate, mlkem_decapsulate,
)

artifact = b"reviewed research output"
context = "GRH-research/review/release-2026-11-13"
key = generate_symmetric_key()
envelope = encrypt_artifact(artifact, key, context=context)
recovered = decrypt_artifact(envelope, key, expected_context=context)

signing_key = Ed25519PrivateKey.generate()
signature = sign_artifact(artifact, signing_key, context=context)
verify_artifact(artifact, signature, signing_key.public_key(), expected_context=context)

# A separate KEM demonstration; this is not an authenticated transport protocol.
recipient = MLKEM768PrivateKey.generate()
shared_secret, encapsulation = mlkem_encapsulate(recipient.public_key())
recovered_secret = mlkem_decapsulate(recipient, encapsulation)
```

Neither example prints or persists its secrets. Applications must provide key
storage, access control and authenticated public-key distribution separately.
Do not embed production keys in a static GitHub Pages site or a source archive.

## Format and trust boundaries

An encryption envelope is a JSON object with exactly five fields: `version`,
`algorithm`, `context`, `nonce`, and `ciphertext`. Version is the integer `1`;
algorithm must be one of the two explicit choices. Nonce and ciphertext use
canonical padded base64. Unknown fields, duplicates, malformed types, incorrect
lengths and oversized artifacts are rejected. The single-message plaintext
limit is 16 MiB. Context is 1–1024 UTF-8 bytes and is **public metadata**.

Associated data is the fixed domain string `GRH-research/artifact-aead/v1`, a
zero byte, and the compact, sorted-key ASCII JSON encoding of version,
algorithm and context. The receiver supplies the expected algorithm and context
independently. It must not simply copy these expectations from untrusted input.
AES-GCM and ChaCha20-Poly1305 retain the library's full 16-byte authentication
tag. The library receives the entire ciphertext before any plaintext is returned.

Every encryption generates a fresh random 96-bit nonce internally. There is no
caller-selected nonce API. Random sampling does not prove perpetual uniqueness:
for `m` independent samples the collision probability is at most
`m(m−1)/2^97`. For example, `m ≤ 2^20` gives a nonce-collision bound below `2^-57`;
this is only a nonce-collision calculation, not a total security bound. This
stateless library cannot enforce a distributed per-key quota or prevent key
reuse after a process restart. Use a fresh independent key for a one-off
artifact, or supply an application-controlled key lifecycle with explicit
usage limits and rotation. Use independent keys across algorithms and purposes.

Signature input is a separate fixed domain string, a four-byte big-endian
UTF-8 context length, the context bytes, and the artifact bytes. This removes
concatenation ambiguity. The underlying signature remains ordinary Ed25519
over that framed byte string; it is not an implementation of Ed25519ctx.
Byte-exact artifacts are signed, so a JSON document must be canonicalized by its
producer before signing if semantic equivalence is required.

Authenticated data can still be replayed. Incorporating an expected artifact ID
or release number in context binds that value, but replay rejection additionally
requires receiver state. Signing a manifest authenticates its bytes relative to
a trusted key; it does not prove the truth of its mathematical or scientific
claims. Python object lifetime does not guarantee secret-memory zeroization.

## Relationship to the formal mathematics

The Lean encryption lemmas in `BridgeTheorems.lean` establish finite algebraic
cancellation and an educational noise bound. They do not formalize this Python
implementation, the native cryptographic backend, IND-CCA security, signature
unforgeability, module-lattice hardness, key distribution or side-channel safety.
The exact finite algebra is useful for explanation; standard cryptographic
security rests on its own established definitions, analyses and implementation
assurance. No finite Hodge gap or fluid theorem substitutes for those obligations.

## Primary sources

- [cryptography 50.0.0: authenticated encryption](https://cryptography.io/en/50.0.0/hazmat/primitives/aead/).
- [cryptography 50.0.0: Ed25519](https://cryptography.io/en/50.0.0/hazmat/primitives/asymmetric/ed25519/).
- [cryptography 50.0.0: ML-KEM interfaces](https://cryptography.io/en/50.0.0/hazmat/primitives/asymmetric/mlkem/).
- [NIST FIPS 203: ML-KEM](https://csrc.nist.gov/pubs/fips/203/final).
- [NIST SP 800-38D: GCM](https://csrc.nist.gov/pubs/sp/800/38/d/final).
- [RFC 8439: ChaCha20 and Poly1305](https://www.rfc-editor.org/rfc/rfc8439).
- [RFC 8032: EdDSA](https://www.rfc-editor.org/rfc/rfc8032).

The versioned library references were checked on 13 November 2026. Algorithm
standardization, recorded functional execution, formal algebraic correctness,
and a proof of a complete deployed protocol remain separate evidence categories.
