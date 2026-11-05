#!/usr/bin/env python3
"""Lossless read-only projection of NEW immutable complete-column records; no science rerun."""
from pathlib import Path
from itertools import combinations
import gzip,hashlib,json
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'web/data/signed-divisor'
CHECK=ROOT/'outputs/checks/2026-11-05-signed-divisor/ui'
PAIRS=('AA','AC','Amu','CA','CC','Cmu','muA','muC','mumu')
PINS={144:'b2db0dfb8f7b3f7ddc6cdd3c4fb3efd88b0e4bec6a805b341240b3722c075380',576:'ea68ea46eec092da39e3e6d282152f69e6c944cb6a15ae1e1efac439ef4a8675',60000:'fecbec83a4fadd301d7845daddcb7e31f216705a6b29c5ba98436642ae0b2e4f'}
sha=lambda b:hashlib.sha256(b).hexdigest()
def rawjson(v):return (json.dumps(v,separators=(',',':'),sort_keys=True)+'\n').encode()
def write(path,raw):
    with path.open('xb') as f:f.write(raw)
def read(p):return json.loads(p.read_bytes())
def lines(p):return [json.loads(s) for s in p.read_bytes().splitlines()]
def flatten(v):return [n for pair in v for n in pair]
def project(D):
    source=ROOT/f'outputs/experiments/2026-11-05-signed-divisor-D{D}-v1'
    assert sha((source/'manifest.json').read_bytes())==PINS[D]
    manifest=read(source/'manifest.json')
    for rel,p in manifest['files'].items():
        b=(source/rel).read_bytes();assert len(b)==p['bytes'] and sha(b)==p['sha256']
    primes=read(source/'prime-ideals.json');columns=read(source/'columns.json')
    ds=lines(source/'divisor-energies.jsonl');gs=lines(source/'gcd-classes.jsonl')
    index={tuple(d['prime_ids']):i for i,d in enumerate(ds)}
    incidents=[[] for d in ds]
    for c in columns:
        ids=c['prime_ids']
        for k in range(len(ids)+1):
            for subset in combinations(ids,k):incidents[index[subset]].append(c['id'])
    divisors=[]
    for i,(d,g) in enumerate(zip(ds,gs)):
        assert d['id']==i and d['prime_ids']==g['prime_ids'] and len(incidents[i])==d['incident_columns']
        divisors.append([d['prime_ids'],*d['generator'],d['norm'],d['mu'],d['incident_columns'],d['active_incident_columns'],d['row_allowed_active_column_counts'],list(map(int,d['row_raw_d_masks'])),flatten([v for r in d['F_omega'] for v in r]),flatten([d['Z_omega'][p] for p in PAIRS]),g['ordered_column_pair_count'],flatten([g['contribution_omega'][p] for p in PAIRS]),incidents[i]])
    payload=dict(schema='signed-divisor-display-case-v1',parameters=read(source/'parameters.json'),
      primes=[[*p['generator'],p['norm'],p['rational_prime'],int(p['kind']=='inert')] for p in primes],
      columns=[[*c['generator'],c['norm'],c['prime_ids'],c['A'],c['C'],c['mu'],c['r_U'],c['W']] for c in columns],
      rows=read(source/'rows.json'),phases=read(source/'raw-character-phases.json'),divisors=divisors,
      normLedger=lines(source/'norm-ledger.jsonl'),rowIdentities=read(source/'row-identities.json'),
      summary=read(source/'summary.json'),rawManifestSHA256=PINS[D],componentOrder=['A','C','mu'],pairOrder=list(PAIRS))
    expanded=rawjson(payload);compressed=gzip.compress(expanded,compresslevel=9,mtime=0)
    filename=f'D{D}-v1.json.gz';write(OUT/filename,compressed)
    return dict(D=D,U=payload['parameters']['U'],H=payload['parameters']['H'],A1=payload['parameters']['A1'],A2=payload['parameters']['A2'],file=filename,
      gzip_sha256=sha(compressed),gzip_bytes=len(compressed),json_sha256=sha(expanded),json_bytes=len(expanded),raw_manifest_sha256=PINS[D],
      columns=len(columns),rows=len(payload['rows']),divisors=len(ds),incidences=sum(map(len,incidents)),
      AA=payload['summary']['normalized_h1']['AA'],source=str(source.relative_to(ROOT)))

def main():
    OUT.mkdir(parents=True,exist_ok=False);CHECK.mkdir(parents=True,exist_ok=True)
    cases=[project(D) for D in PINS]
    index=dict(schema='signed-divisor-display-index-v1',cases=cases,
      fixedProfile='NEW W_delta; delta1/240000, fixed once for integerD<=60000; derivative costO_k(240000^k); globally different from old broad plateau',
      scope='Complete annular columns, declared different nonprincipal row blocks; nu1/unitclass1/Sabove2,3. No growthfit, asymptotic saving, GRH or training claim.',
      actual_source_v1_sha256='0e3539b5d6b0efc723f37fbc067c88297edb5556eff9314b2d8b79b88f25b95e',
      compatible_private_unit_fix_v2_sha256='9977e3cfea4b785089d52e1ded4490774818e0e13ac54d0922a65734671517a8',
      independent_small_acceptance_sha256='90b93e8e9b99c6d733fd359a1541d34072dab8b7f05109b2cc1d02983b68c9d2',
      unit_fix_compatibility_sha256='51e0888826bdba55e06df33f827e1daf5bc463dbdf47d1a5d236278a6ddc8a85')
    raw=rawjson(index);write(OUT/'index-v1.json',raw)
    result=dict(passed=True,projection_only=True,no_raw_science_run=True,index_sha256=sha(raw),
      projector_sha256=sha(Path(__file__).read_bytes()),cases=cases,total_gzip_bytes=sum(c['gzip_bytes'] for c in cases))
    assert result['total_gzip_bytes']<5_000_000
    write(CHECK/'projection-v1.json',rawjson(result))
    print(json.dumps(result,sort_keys=True))
if __name__=='__main__':main()
