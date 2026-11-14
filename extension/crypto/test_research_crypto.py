"""Functional and adversarial regressions; all private keys are ephemeral."""
from __future__ import annotations

import base64
import json
import unittest

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.asymmetric.mlkem import (
    MLKEM768PrivateKey, MLKEM768PublicKey, MLKEM1024PrivateKey, MLKEM1024PublicKey,
)

import research_crypto as rc


CONTEXT = "GRH-research/artifact/source/2026-11-13"


def rewrite(envelope: bytes, **updates) -> bytes:
    value = json.loads(envelope)
    value.update(updates)
    return json.dumps(value).encode()


def flipped_field(envelope: bytes, field: str, position: int) -> bytes:
    value = json.loads(envelope)
    data = bytearray(base64.b64decode(value[field]))
    data[position] ^= 1
    return rewrite(envelope, **{field: base64.b64encode(data).decode()})


class ArtifactEncryptionTests(unittest.TestCase):
    def cases(self):
        for algorithm in rc.ALGORITHMS:
            key = rc.generate_symmetric_key()
            envelope = rc.encrypt_artifact(b"authenticated artifact", key,
                                            context=CONTEXT, algorithm=algorithm)
            yield algorithm, key, envelope

    def decrypt(self, envelope, key, algorithm, context=CONTEXT):
        return rc.decrypt_artifact(envelope, key, expected_context=context,
                                    expected_algorithm=algorithm)

    def test_roundtrip_empty_binary_unicode_and_large(self):
        for algorithm in rc.ALGORITHMS:
            key = rc.generate_symmetric_key()
            for data in [b"", bytes(range(256)), "tropical\u2192quantum".encode(), b"x" * 65537]:
                with self.subTest(algorithm=algorithm, size=len(data)):
                    envelope = rc.encrypt_artifact(data, key, context=CONTEXT, algorithm=algorithm)
                    self.assertEqual(self.decrypt(envelope, key, algorithm), data)

    def test_wrong_key_rejected(self):
        for algorithm, _, envelope in self.cases():
            with self.subTest(algorithm=algorithm), self.assertRaises(rc.AuthenticationError):
                self.decrypt(envelope, rc.generate_symmetric_key(), algorithm)

    def test_wrong_expected_context_rejected(self):
        for algorithm, key, envelope in self.cases():
            with self.subTest(algorithm=algorithm), self.assertRaises(rc.AuthenticationError):
                self.decrypt(envelope, key, algorithm, CONTEXT + "/different")

    def test_each_ciphertext_and_tag_byte_change_rejected(self):
        for algorithm, key, envelope in self.cases():
            count = len(base64.b64decode(json.loads(envelope)["ciphertext"]))
            for position in range(count):
                with self.subTest(algorithm=algorithm, position=position), self.assertRaises(rc.AuthenticationError):
                    self.decrypt(flipped_field(envelope, "ciphertext", position), key, algorithm)

    def test_each_nonce_byte_change_rejected(self):
        for algorithm, key, envelope in self.cases():
            for position in range(12):
                with self.subTest(algorithm=algorithm, position=position), self.assertRaises(rc.AuthenticationError):
                    self.decrypt(flipped_field(envelope, "nonce", position), key, algorithm)

    def test_changed_context_fails_even_if_new_context_expected(self):
        for algorithm, key, envelope in self.cases():
            changed = CONTEXT + "/altered"
            with self.subTest(algorithm=algorithm), self.assertRaises(rc.AuthenticationError):
                self.decrypt(rewrite(envelope, context=changed), key, algorithm, changed)

    def test_algorithm_cannot_be_selected_by_envelope(self):
        for algorithm, key, envelope in self.cases():
            other = next(a for a in rc.ALGORITHMS if a != algorithm)
            with self.subTest(algorithm=algorithm), self.assertRaises(rc.AuthenticationError):
                self.decrypt(envelope, key, other)

    def test_changed_algorithm_is_authenticated(self):
        for algorithm, key, envelope in self.cases():
            other = next(a for a in rc.ALGORITHMS if a != algorithm)
            with self.subTest(algorithm=algorithm), self.assertRaises(rc.AuthenticationError):
                self.decrypt(rewrite(envelope, algorithm=other), key, other)

    def test_fresh_random_nonce_sample(self):
        # This finite sample is not a proof that random nonces can never collide.
        for algorithm in rc.ALGORITHMS:
            key = rc.generate_symmetric_key()
            nonces = {json.loads(rc.encrypt_artifact(b"same", key, context=CONTEXT,
                                                     algorithm=algorithm))["nonce"] for _ in range(64)}
            self.assertEqual(len(nonces), 64)

    def test_duplicate_and_unknown_json_fields_rejected(self):
        for algorithm, key, envelope in self.cases():
            duplicate = envelope[:-1] + b',"version":1}'
            for altered in [duplicate, rewrite(envelope, extra="ignored?")]:
                with self.subTest(algorithm=algorithm), self.assertRaises(rc.EnvelopeFormatError):
                    self.decrypt(altered, key, algorithm)

    def test_strict_version_algorithm_and_base64(self):
        for algorithm, key, envelope in self.cases():
            for altered in [rewrite(envelope, version=True), rewrite(envelope, version=2),
                            rewrite(envelope, version=1.0), rewrite(envelope, algorithm="none"),
                            rewrite(envelope, nonce="!"), rewrite(envelope, nonce=""),
                            rewrite(envelope, ciphertext="AA=="), rewrite(envelope, context="")]:
                with self.subTest(algorithm=algorithm), self.assertRaises(rc.EnvelopeFormatError):
                    self.decrypt(altered, key, algorithm)

    def test_nonobject_and_malformed_json_rejected(self):
        for algorithm, key, _ in self.cases():
            for malformed in [b"[]", b"null", b"42", b'{"version":', b"\xff"]:
                with self.subTest(algorithm=algorithm), self.assertRaises(rc.EnvelopeFormatError):
                    self.decrypt(malformed, key, algorithm)

    def test_key_and_context_constraints(self):
        for bad_key in [b"", b"x" * 16, b"x" * 31, b"x" * 33]:
            with self.assertRaises(ValueError):
                rc.encrypt_artifact(b"data", bad_key, context=CONTEXT)
        for bad_context in ["", "x" * 1025]:
            with self.assertRaises(ValueError):
                rc.encrypt_artifact(b"data", rc.generate_symmetric_key(), context=bad_context)

    def test_unicode_context_roundtrip(self):
        key = rc.generate_symmetric_key()
        context = "\u00e9tude/\u03c1/\U0001f512"
        envelope = rc.encrypt_artifact(b"data", key, context=context)
        self.assertEqual(rc.decrypt_artifact(envelope, key, expected_context=context), b"data")

    def test_maximum_payload_and_context_roundtrip(self):
        # Exercise the actual advertised limits, not a reduced test constant.
        data = b"x" * rc.MAX_PLAINTEXT_BYTES
        context = "\u00e9" * (rc.MAX_CONTEXT_BYTES // 2)
        self.assertEqual(len(context.encode("utf-8")), rc.MAX_CONTEXT_BYTES)
        for algorithm in rc.ALGORITHMS:
            with self.subTest(algorithm=algorithm):
                key = rc.generate_symmetric_key()
                envelope = rc.encrypt_artifact(data, key, context=context, algorithm=algorithm)
                self.assertLessEqual(len(envelope), rc.MAX_ENVELOPE_BYTES)
                self.assertEqual(self.decrypt(envelope, key, algorithm, context), data)

    def test_oversized_payload_rejected(self):
        for algorithm in rc.ALGORITHMS:
            with self.subTest(algorithm=algorithm), self.assertRaises(ValueError):
                rc.encrypt_artifact(b"x" * (rc.MAX_PLAINTEXT_BYTES + 1),
                                    rc.generate_symmetric_key(), context=CONTEXT,
                                    algorithm=algorithm)

    def test_oversized_serialized_envelope_rejected(self):
        for algorithm in rc.ALGORITHMS:
            with self.subTest(algorithm=algorithm), self.assertRaises(rc.EnvelopeFormatError):
                self.decrypt(b" " * (rc.MAX_ENVELOPE_BYTES + 1),
                             rc.generate_symmetric_key(), algorithm)

    def test_utf8_byte_limit_is_not_character_limit(self):
        context = "\u00e9" * (rc.MAX_CONTEXT_BYTES // 2 + 1)
        self.assertLess(len(context), rc.MAX_CONTEXT_BYTES)
        self.assertGreater(len(context.encode("utf-8")), rc.MAX_CONTEXT_BYTES)
        for algorithm, key, envelope in self.cases():
            with self.subTest(algorithm=algorithm, operation="encrypt"), self.assertRaises(ValueError):
                rc.encrypt_artifact(b"data", key, context=context, algorithm=algorithm)
            with self.subTest(algorithm=algorithm, operation="parse"), self.assertRaises(rc.EnvelopeFormatError):
                self.decrypt(rewrite(envelope, context=context), key, algorithm)

    def test_noncanonical_base64_pad_bits_rejected(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        for algorithm in rc.ALGORITHMS:
            key = rc.generate_symmetric_key()
            # Empty plaintext gives a 16-byte tag ending in two base64 pad bytes.
            envelope = rc.encrypt_artifact(b"", key, context=CONTEXT, algorithm=algorithm)
            encoded = json.loads(envelope)["ciphertext"]
            self.assertTrue(encoded.endswith("=="))
            alias = encoded[:-3] + alphabet[alphabet.index(encoded[-3]) | 1] + "=="
            self.assertNotEqual(alias, encoded)
            self.assertEqual(base64.b64decode(alias, validate=True), base64.b64decode(encoded))
            with self.subTest(algorithm=algorithm), self.assertRaises(rc.EnvelopeFormatError):
                self.decrypt(rewrite(envelope, ciphertext=alias), key, algorithm)

    def test_unpaired_surrogate_context_rejected(self):
        for algorithm, key, envelope in self.cases():
            with self.subTest(algorithm=algorithm), self.assertRaises(rc.EnvelopeFormatError):
                self.decrypt(rewrite(envelope, context="\ud800"), key, algorithm)


class SignatureTests(unittest.TestCase):
    def setUp(self):
        self.key = Ed25519PrivateKey.generate()
        self.data = b"research evidence manifest"
        self.signature = rc.sign_artifact(self.data, self.key, context=CONTEXT)

    def verify(self, data, signature, context=CONTEXT):
        return rc.verify_artifact(data, signature, self.key.public_key(), expected_context=context)

    def test_roundtrip(self):
        self.assertIsNone(self.verify(self.data, self.signature))
        self.assertEqual(len(self.signature), 64)

    def test_empty_payload(self):
        signature = rc.sign_artifact(b"", self.key, context=CONTEXT)
        self.assertIsNone(self.verify(b"", signature))

    def test_changed_payload_rejected(self):
        with self.assertRaises(InvalidSignature):
            self.verify(self.data + b".", self.signature)

    def test_wrong_context_rejected(self):
        with self.assertRaises(InvalidSignature):
            self.verify(self.data, self.signature, CONTEXT + "/different")

    def test_wrong_public_key_rejected(self):
        with self.assertRaises(InvalidSignature):
            rc.verify_artifact(self.data, self.signature, Ed25519PrivateKey.generate().public_key(),
                                expected_context=CONTEXT)

    def test_signature_modification_rejected(self):
        for position in range(len(self.signature)):
            altered = bytearray(self.signature)
            altered[position] ^= 1
            with self.subTest(position=position), self.assertRaises(InvalidSignature):
                self.verify(self.data, bytes(altered))

    def test_context_message_framing_unambiguous(self):
        signature = rc.sign_artifact(b"bc", self.key, context="a")
        with self.assertRaises(InvalidSignature):
            self.verify(b"c", signature, "ab")


class MLKEMTests(unittest.TestCase):
    PARAMETERS = [(MLKEM768PrivateKey, MLKEM768PublicKey, 1184, 1088),
                  (MLKEM1024PrivateKey, MLKEM1024PublicKey, 1568, 1568)]

    def test_encapsulation_roundtrip_and_sizes(self):
        for private_type, public_type, public_size, cipher_size in self.PARAMETERS:
            with self.subTest(parameter_set=private_type.__name__):
                key = private_type.generate()
                public = key.public_key().public_bytes_raw()
                self.assertEqual(len(public), public_size)
                restored_public = public_type.from_public_bytes(public)
                secret, ciphertext = rc.mlkem_encapsulate(restored_public)
                self.assertEqual((len(secret), len(ciphertext)), (32, cipher_size))
                self.assertEqual(rc.mlkem_decapsulate(key, ciphertext), secret)

    def test_tampering_uses_implicit_rejection(self):
        for private_type, _, _, _ in self.PARAMETERS:
            with self.subTest(parameter_set=private_type.__name__):
                key = private_type.generate()
                secret, ciphertext = rc.mlkem_encapsulate(key.public_key())
                altered = bytes([ciphertext[0] ^ 1]) + ciphertext[1:]
                rejection_secret = rc.mlkem_decapsulate(key, altered)
                self.assertEqual(len(rejection_secret), 32)
                self.assertNotEqual(rejection_secret, secret)
                self.assertEqual(rc.mlkem_decapsulate(key, altered), rejection_secret)

    def test_wrong_private_key_does_not_recover_secret(self):
        for private_type, _, _, _ in self.PARAMETERS:
            key = private_type.generate()
            secret, ciphertext = rc.mlkem_encapsulate(key.public_key())
            self.assertNotEqual(rc.mlkem_decapsulate(private_type.generate(), ciphertext), secret)

    def test_invalid_lengths_rejected(self):
        for private_type, public_type, public_size, cipher_size in self.PARAMETERS:
            key = private_type.generate()
            with self.assertRaises(ValueError):
                rc.mlkem_decapsulate(key, bytes(cipher_size - 1))
            with self.assertRaises(ValueError):
                public_type.from_public_bytes(bytes(public_size - 1))


if __name__ == "__main__":
    unittest.main(verbosity=2)
