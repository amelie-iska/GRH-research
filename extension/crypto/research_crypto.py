"""Library-backed artifact encryption, signatures and ML-KEM interfaces.

The implementation delegates every cryptographic primitive to cryptography.
It does not establish security of a new scheme, or depend on GRH. See README.md
for the format, trust boundaries and key/nonce lifecycle requirements.
"""
from __future__ import annotations

import base64
import binascii
import hmac
import json
import secrets
from typing import Literal

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey,
)
from cryptography.hazmat.primitives.asymmetric.mlkem import (
    MLKEM768PrivateKey,
    MLKEM768PublicKey,
    MLKEM1024PrivateKey,
    MLKEM1024PublicKey,
)
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, ChaCha20Poly1305

Algorithm = Literal["AES-256-GCM", "ChaCha20-Poly1305"]
ALGORITHMS = ("AES-256-GCM", "ChaCha20-Poly1305")
MAX_PLAINTEXT_BYTES = 16 * 1024 * 1024
MAX_ENVELOPE_BYTES = 24 * 1024 * 1024
MAX_CONTEXT_BYTES = 1024
_AEAD_DOMAIN = b"GRH-research/artifact-aead/v1\x00"
_SIGN_DOMAIN = b"GRH-research/artifact-ed25519/v1\x00"
_FIELDS = frozenset({"version", "algorithm", "context", "nonce", "ciphertext"})


class EnvelopeFormatError(ValueError):
    """The serialized envelope does not have the documented strict format."""


class AuthenticationError(ValueError):
    """The key, expected context, nonce or authenticated ciphertext is invalid."""


def _context_bytes(context: str) -> bytes:
    if type(context) is not str:
        raise TypeError("context must be a string")
    encoded = context.encode("utf-8")
    if not 1 <= len(encoded) <= MAX_CONTEXT_BYTES:
        raise ValueError("context must contain 1 to 1024 UTF-8 bytes")
    return encoded


def _data_bytes(data: bytes) -> bytes:
    if type(data) is not bytes:
        raise TypeError("data must be bytes")
    if len(data) > MAX_PLAINTEXT_BYTES:
        raise ValueError("artifact exceeds the 16 MiB single-message limit")
    return data


def _cipher(algorithm: str, key: bytes) -> AESGCM | ChaCha20Poly1305:
    if algorithm not in ALGORITHMS:
        raise ValueError("unsupported algorithm")
    if type(key) is not bytes or len(key) != 32:
        raise ValueError("an independently generated 32-byte key is required")
    return AESGCM(key) if algorithm == "AES-256-GCM" else ChaCha20Poly1305(key)


def _json_bytes(value: dict) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True, allow_nan=False).encode("ascii")


def _aad(algorithm: str, context: str) -> bytes:
    return _AEAD_DOMAIN + _json_bytes({"version": 1, "algorithm": algorithm,
                                      "context": context})


def generate_symmetric_key() -> bytes:
    """Generate one fresh key; use independent keys for distinct algorithms."""
    return secrets.token_bytes(32)


def encrypt_artifact(data: bytes, key: bytes, *, context: str,
                     algorithm: Algorithm = "AES-256-GCM") -> bytes:
    """Encrypt a bounded artifact; context is authenticated and public.

    A fresh random 96-bit nonce is generated internally. Random nonces are not
    a persistent uniqueness guarantee; see the per-key usage policy in README.
    No caller-supplied nonce is accepted.
    """
    _data_bytes(data)
    _context_bytes(context)
    cipher = _cipher(algorithm, key)
    nonce = secrets.token_bytes(12)
    ciphertext = cipher.encrypt(nonce, data, _aad(algorithm, context))
    return _json_bytes({"version": 1, "algorithm": algorithm, "context": context,
                        "nonce": base64.b64encode(nonce).decode("ascii"),
                        "ciphertext": base64.b64encode(ciphertext).decode("ascii")})


def _unique_fields(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise EnvelopeFormatError("duplicate JSON field")
        result[key] = value
    return result


def _base64_bytes(value: object, field: str) -> bytes:
    if type(value) is not str:
        raise EnvelopeFormatError(f"{field} must be a base64 string")
    try:
        raw = base64.b64decode(value, validate=True)
    except (ValueError, binascii.Error) as exc:
        raise EnvelopeFormatError(f"invalid {field} base64") from exc
    if base64.b64encode(raw).decode("ascii") != value:
        raise EnvelopeFormatError(f"noncanonical {field} base64")
    return raw


def decrypt_artifact(envelope: bytes, key: bytes, *, expected_context: str,
                     expected_algorithm: Algorithm = "AES-256-GCM") -> bytes:
    """Authenticate before returning plaintext; caller supplies trusted context.

    The algorithm is an independently supplied expectation, not negotiated from
    attacker-controlled envelope metadata. Valid replays remain valid: replay
    prevention requires application state and is outside this byte interface.
    """
    trusted_context = _context_bytes(expected_context)
    cipher = _cipher(expected_algorithm, key)
    if type(envelope) is not bytes:
        raise TypeError("envelope must be bytes")
    if len(envelope) > MAX_ENVELOPE_BYTES:
        raise EnvelopeFormatError("envelope exceeds size limit")
    try:
        parsed = json.loads(envelope, object_pairs_hook=_unique_fields)
    except (ValueError, UnicodeError, RecursionError) as exc:
        raise EnvelopeFormatError("invalid envelope JSON") from exc
    if type(parsed) is not dict or set(parsed) != _FIELDS:
        raise EnvelopeFormatError("unexpected envelope fields")
    if type(parsed["version"]) is not int or parsed["version"] != 1:
        raise EnvelopeFormatError("unsupported envelope version")
    if type(parsed["algorithm"]) is not str or parsed["algorithm"] not in ALGORITHMS:
        raise EnvelopeFormatError("unsupported envelope algorithm")
    try:
        actual_context = _context_bytes(parsed["context"])
    except (ValueError, TypeError, UnicodeError) as exc:
        raise EnvelopeFormatError("invalid envelope context") from exc
    if parsed["algorithm"] != expected_algorithm or not hmac.compare_digest(
            actual_context, trusted_context):
        raise AuthenticationError("artifact authentication failed")
    nonce = _base64_bytes(parsed["nonce"], "nonce")
    ciphertext = _base64_bytes(parsed["ciphertext"], "ciphertext")
    if len(nonce) != 12 or not 16 <= len(ciphertext) <= MAX_PLAINTEXT_BYTES + 16:
        raise EnvelopeFormatError("invalid nonce or ciphertext length")
    try:
        return cipher.decrypt(nonce, ciphertext, _aad(expected_algorithm, expected_context))
    except InvalidTag as exc:
        raise AuthenticationError("artifact authentication failed") from exc


def _signature_message(data: bytes, context: str) -> bytes:
    _data_bytes(data)
    encoded = _context_bytes(context)
    return _SIGN_DOMAIN + len(encoded).to_bytes(4, "big") + encoded + data


def sign_artifact(data: bytes, key: Ed25519PrivateKey, *, context: str) -> bytes:
    """Sign the context-framed bytes with a caller-managed Ed25519 private key."""
    return key.sign(_signature_message(data, context))


def verify_artifact(data: bytes, signature: bytes, key: Ed25519PublicKey, *,
                    expected_context: str) -> None:
    """Return None on success; raise cryptography's InvalidSignature on failure.

    Public-key ownership must be established out of band. This signature format
    is ordinary Ed25519 over framed bytes, not the separate Ed25519ctx variant.
    """
    key.verify(signature, _signature_message(data, expected_context))


def mlkem_encapsulate(public_key: MLKEM768PublicKey | MLKEM1024PublicKey
                      ) -> tuple[bytes, bytes]:
    """Return (shared_secret, ciphertext) using the standard backend API.

    This is key encapsulation only. It authenticates neither party and defines
    no transport or KEM/DEM protocol. Do not infer ciphertext validity from
    decapsulation returning a value: ML-KEM uses implicit rejection.
    """
    return public_key.encapsulate()


def mlkem_decapsulate(private_key: MLKEM768PrivateKey | MLKEM1024PrivateKey,
                      ciphertext: bytes) -> bytes:
    """Recover a shared secret; wrong-length ciphertext raises ValueError."""
    return private_key.decapsulate(ciphertext)
