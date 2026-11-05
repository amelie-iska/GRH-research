#!/usr/bin/env python3
"""Pin the sole root terminology clarification without rewriting old evidence."""
from pathlib import Path
import argparse,hashlib,json
ROOT=Path(__file__).resolve().parents[3]
OLD='cedc1e68b983dc86e63a2596d535d985a6e0a829906859df71fd97164e36613c'
NEW='7dc97b2e61a8d3bc286356bf9eae28fb986d29978582a97f9bfbfd7e329ab9c1'
old_sentence='Since nu is unramified outside S, a prime of a1 or a2 has a nonzero exponent 1 or 2 modulo 6 in the outside-S tame Kummer conductor.'
new_sentence='Since nu is unramified outside S, a prime of a1 or a2 has radicand valuation 1 or 2 modulo 6. At this prime outside S the tame Kummer character is nontrivial, with conductor exponent 1.'
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main(output):
 if output.exists():raise FileExistsError('Preserve prior evidence')
 old=ROOT/'planning/weighted-moment-20261105/review/author-derivation-before-clarification.md'
 new=ROOT/'planning/weighted-moment-20261105/frontier/CENTERING_AND_SIGNED_TARGET.md'
 manifest=ROOT/'planning/weighted-moment-20261105/frontier/manifest.json'
 snapshot=ROOT/'planning/weighted-moment-20261105/review/author-manifest-before-clarification-update.json'
 assert h(old)==OLD and h(new)==NEW
 before=old.read_text();after=new.read_text()
 assert before.count(old_sentence)==1
 assert before.replace(old_sentence,new_sentence)==after
 data=json.loads(manifest.read_text())
 assert data['paths_sha256'][str(new.relative_to(ROOT))]==OLD
 assert h(manifest)=='c970869469e6d011a8ba87870a1b32beab1e82d7da203651c23eba8a60cacd9a'
 with snapshot.open('xb') as f:f.write(manifest.read_bytes())
 unchanged=[]
 for name,digest in data['paths_sha256'].items():
  actual=old if name==str(new.relative_to(ROOT)) else ROOT/name
  assert h(actual)==digest
  unchanged.append(name)
 diag=ROOT/'outputs/checks/2026-11-05-weighted-moment/review/independent-negative-edge-controls-v1.json'
 diagnostics=json.loads(diag.read_text());assert diagnostics['passed']
 assert diagnostics['source_sha256'][str(new.relative_to(ROOT))]==OLD
 result=dict(passed=True,old_derivation_sha256=OLD,current_derivation_sha256=NEW,
 only_change='One terminology clarification: radicand valuations 1/2 modulo6; nontrivial tame conductor exponent1.',
 load_bearing_identity_changed=False,author_manifest_is_historical=True,
 original_author_manifest_sha256=h(snapshot),historical_manifest_paths_verified=unchanged,
 prior_finite_diagnostics_still_applicable=True,
 v1_receipt_superseded='The v1 prose review and reviewed_derivation_sha256 refer to OLD; its paths_sha256 captured NEW concurrently with root clarification. V2 is authoritative after explicit one-change reconciliation.',
 source_sha256={str(p.relative_to(ROOT)):h(p) for p in [old,new,snapshot,diag,Path(__file__)]})
 with output.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();main(a.output)
