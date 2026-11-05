#!/usr/bin/env python3
"""Tamper only the in-memory reader; leave all protected input bytes immutable."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from unittest.mock import patch
import json,hashlib
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'examples/arithmetic_learning'))
import learn
RUN=ROOT/'outputs/experiments/2026-11-05-arithmetic-learning-v2'
OUT=ROOT/'outputs/checks/2026-11-05-arithmetic-learning/implementation/stale-artifact-controls-v2.json'
if OUT.exists():raise FileExistsError(OUT)
original=Path.read_bytes
results=[]
for name in ('input.json','all_literal-real.json'):
    target=(RUN/name).resolve()
    def reader(path):
        data=original(path)
        return data+b' altered in memory only' if path.resolve()==target else data
    with patch.object(Path,'read_bytes',reader):
        try:learn.verify_run(RUN)
        except RuntimeError as error:
            message=str(error)
            assert 'Stale artifact bytes: '+name in message,(name,message)
        else:raise AssertionError('tampering accepted: '+name)
    results.append(dict(artifact=name,in_memory_tamper_refused=True,reason=message))
assert learn.verify_run(RUN)
receipt=dict(passed=True,checks=results,actual_file_bytes_changed=False,source_sha256=hashlib.sha256(original(Path(__file__))).hexdigest(),run_manifest_sha256=hashlib.sha256(original(RUN/'manifest.json')).hexdigest())
with OUT.open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps(receipt,indent=2))
