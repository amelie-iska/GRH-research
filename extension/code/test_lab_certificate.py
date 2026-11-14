#!/usr/bin/env python3
"""Independent replay and fail-closed CLI regression for actual browser exports."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import verify_lab_certificate as V


class LabCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = json.loads(V.REGISTRY.read_text())
        script = r"""
const fs=require('fs'),B=require('./extension/site/certificate-bridge.js');
const registry=JSON.parse(fs.readFileSync('./extension/site/data/certificate-contracts.json','utf8'));
const samples=[['hodge-family-v1',{epsilon:'0/1'}],['hodge-family-v1',{epsilon:'1/3'}],['quadratic-cover-v1',{power:'3/1',x:'7/25',y:'63/100'}],...['5/8','3/5','2/1'].map(rate=>['weighted-gain-v1',{matrix:[['1/4','3/2'],['3/32','1/4']],weights:['4/1','1/1'],rate}])];
console.log(JSON.stringify(samples.map(([id,p])=>B.create(id,p,registry))));
"""
        cls.exports = json.loads(subprocess.check_output(["node", "-e", script], cwd=V.ROOT, text=True))

    def test_actual_browser_exports_replay_with_independent_exact_oracles(self):
        results = [V.replay(json.dumps(c), self.registry) for c in self.exports]
        self.assertEqual(results[0]["result"]["smallest_positive_eigenvalue"], "1/1")
        self.assertEqual(results[1]["result"]["least_eigenvalue"], "1/9")
        self.assertEqual(results[2]["result"]["determinant"], "2744/1")
        self.assertEqual(results[2]["result"]["target_mod_one"], ["7/50", "47/50"])
        self.assertEqual(results[3]["result"]["slacks"], ["0/1", "0/1"])
        self.assertEqual(results[4]["result"]["slacks"], ["-1/10", "-1/40"])
        self.assertTrue(results[5]["result"]["bound_holds"])
        self.assertFalse(results[5]["result"]["certifies_contraction_of_supplied_gain"])
        self.assertTrue(all(not r["lean_kernel_executed"] for r in results))

    def test_invalid_scalar_domain_is_not_silently_coerced(self):
        values = [0, 0.5, True, False, None, float("nan"), float("inf"), {}, "1", "01/2", "-0/1", "0/2", "2/6", "1/-2", "1/0", "1e-3", " 1/3", "1/" + "9" * 81]
        for value in values:
            with self.subTest(value=value), self.assertRaises(ValueError):
                V.rational(value)

    def test_duplicate_keys_numbers_and_nonfinite_json_are_rejected(self):
        for text in ['{"a":"1/1","a":"2/1"}', '{"a":1}', '{"a":1.0}', '{"a":1e2}', '{"a":NaN}', '{"a":Infinity}', '{"a":"1/1","\\u0061":"2/1"}']:
            with self.subTest(text=text), self.assertRaises(ValueError):
                V.parse_certificate(text)

    def test_bounded_utf8_and_nested_inputs_fail_before_replay(self):
        for text in ['"' + "λ" * 270000 + '"', "[" * 30 + "true" + "]" * 30, " " * (V.MAX_BYTES + 1)]:
            with self.assertRaises(ValueError):
                V.parse_certificate(text)

    def test_altered_conclusions_bindings_and_shapes_fail(self):
        original = self.exports[1]
        variants = []
        bad = deepcopy(original); bad["result"]["least_eigenvalue"] = "1/8"; variants.append(bad)
        bad = deepcopy(original); bad["result"]["positive_gap"] = False; variants.append(bad)
        bad = deepcopy(original); bad["binding"]["theorems"][0]["type_sha256"] = "0" * 64; variants.append(bad)
        bad = deepcopy(original); bad["binding"]["theorems"][0]["printed_type"] += " changed"; variants.append(bad)
        bad = deepcopy(original); bad["parameters"]["extra"] = "1/1"; variants.append(bad)
        bad = deepcopy(original); bad["lean"] = "axiom bad : False"; variants.append(bad)
        for variant in variants:
            with self.assertRaises(ValueError):
                V.replay(variant, self.registry)
        with self.assertRaises(ValueError):
            V.replay(original, self.registry, "weighted-gain-v1")

    def test_hodge_and_live_cover_domains_are_enforced(self):
        for epsilon in ["-1/3", "4/3"]:
            with self.assertRaises(ValueError):
                V.hodge({"epsilon": epsilon})
        for params in [{"power": "4/1", "x": "0/1", "y": "0/1"}, {"power": "1/1", "x": "1/3", "y": "0/1"}]:
            with self.assertRaises(ValueError):
                V.cover(params)

    def test_current_sources_and_compiled_types_are_bound(self):
        V.verify_registry_sources(self.registry)
        altered = deepcopy(self.registry)
        altered["contracts"]["hodge-family-v1"]["runtime_sources"]["extension/site/exact-rational.js"] = "0" * 64
        with self.assertRaises(ValueError):
            V.verify_registry_sources(altered)
        altered = deepcopy(self.registry)
        altered["contracts"]["hodge-family-v1"]["theorems"][0]["printed_type"] += " altered"
        with self.assertRaises(ValueError):
            V.verify_registry_sources(altered)

    def test_cli_valid_negative_and_malformed_records_work_with_optimization(self):
        with tempfile.TemporaryDirectory(prefix="grh-lab-certificate-") as directory:
            file = Path(directory) / "certificate.json"
            for optimized in (False, True):
                cmd = [sys.executable] + (["-O"] if optimized else []) + [str(Path(V.__file__)), str(file)]
                for sample in [self.exports[1], self.exports[4]]:
                    file.write_text(json.dumps(sample))
                    result = subprocess.run(cmd, text=True, capture_output=True, check=False)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    output = json.loads(result.stdout)
                    self.assertEqual(output["status"], "valid-instance")
                    self.assertEqual(output["result"], sample["result"])
                    self.assertTrue(output["local_source_bindings_checked"])
                bad = deepcopy(self.exports[1]); bad["result"]["least_eigenvalue"] = "1/8"; file.write_text(json.dumps(bad))
                result = subprocess.run(cmd, text=True, capture_output=True, check=False)
                self.assertEqual(result.returncode, 1)
                self.assertEqual(json.loads(result.stderr)["status"], "rejected")


if __name__ == "__main__":
    unittest.main(verbosity=2)
