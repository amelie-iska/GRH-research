#!/usr/bin/env python3
"""Narrow unit-edge correction and frozen-data compatibility; no arithmetic table rerun."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import hashlib,json
import full_column_v1 as V1
import full_column_v2 as V2

HERE=Path(__file__).resolve().parent

def main():
    before=(HERE/'full_column_v1.py').read_bytes()
    after=(HERE/'full_column_v2.py').read_bytes()
    old=b'    if U*U<=N<=7*U*U:'
    new=b'    if N>U and U*U<=N<=7*U*U:'
    assert before.count(old)==1 and before.replace(old,new)==after
    assert hashlib.sha256(before).hexdigest()=='0e3539b5d6b0efc723f37fbc067c88297edb5556eff9314b2d8b79b88f25b95e'
    rejected=False
    try:V1.original_coefficients([],1,1)
    except AssertionError:rejected=True
    assert rejected,'The old unit-edge defect must be demonstrated, not merely presumed'
    assert V2.original_coefficients([],1,1)==(1,0,1,0)
    assert V2.original_coefficients([],1,2)==(1,0,1,0)
    cases=[]
    for name in ('D144-v1','D576-v1','D60000-v1'):
        out=V1.ROOT/('outputs/experiments/2026-11-05-signed-divisor-'+name)
        params=json.loads((out/'parameters.json').read_bytes())
        columns=json.loads((out/'columns.json').read_bytes())
        # The only added guard is true on EVERY frozen column; original executed branch/result is identical.
        assert all(c['norm']>params['U'] for c in columns)
        cases.append(dict(path=str(out.relative_to(V1.ROOT)),columns=len(columns),
          all_N_gt_U=True,manifest_sha256=hashlib.sha256((out/'manifest.json').read_bytes()).hexdigest()))
    result=dict(passed=True,v1_sha256=hashlib.sha256(before).hexdigest(),v2_sha256=hashlib.sha256(after).hexdigest(),
      literal_single_guard_diff=True,old_unit_edge_negative_control_rejected=True,
      corrected_unit_output=[1,0,1,0],frozen_case_compatibility=cases,
      frozen_tables_rerun=False,original_v1_provenance_preserved=True,
      scope='Only private high-window simplification at unit boundary; no actual run column affected')
    print(json.dumps(result,sort_keys=True))

if __name__=='__main__':main()
