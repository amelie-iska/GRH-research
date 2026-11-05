"""Independent field-by-field display transfer check; no raw arithmetic evaluator imports."""
from pathlib import Path
import json,gzip,hashlib
ROOT=Path(__file__).resolve().parents[3]
sha=lambda b:hashlib.sha256(b).hexdigest()
read=lambda p:json.loads(p.read_bytes())
lines=lambda p:[json.loads(s) for s in p.read_bytes().splitlines()]
index=read(ROOT/'web/data/signed-divisor/index-v1.json');results=[]
for e in index['cases']:
 source=ROOT/e['source'];blob=(ROOT/'web/data/signed-divisor'/e['file']).read_bytes();raw=gzip.decompress(blob);d=json.loads(raw)
 assert sha(blob)==e['gzip_sha256'] and sha(raw)==e['json_sha256'] and sha((source/'manifest.json').read_bytes())==e['raw_manifest_sha256']
 assert d['rows']==read(source/'rows.json') and d['phases']==read(source/'raw-character-phases.json')
 assert d['normLedger']==lines(source/'norm-ledger.jsonl') and d['rowIdentities']==read(source/'row-identities.json') and d['summary']==read(source/'summary.json') and d['parameters']==read(source/'parameters.json')
 for i,c in enumerate(read(source/'columns.json')):
  p=d['columns'][i];assert c['id']==i and p[:2]==c['generator'] and p[2]==c['norm'] and p[3]==c['prime_ids'] and p[4:]==[c[k] for k in ('A','C','mu','r_U','W')] and c['nu_omega']==[1,0]
 for i,p in enumerate(read(source/'prime-ideals.json')):
  assert d['primes'][i]==[*p['generator'],p['norm'],p['rational_prime'],int(p['kind']=='inert')]
 rawds=lines(source/'divisor-energies.jsonl');rawgs=lines(source/'gcd-classes.jsonl')
 for i,z in enumerate(rawds):
  v=d['divisors'][i];g=rawgs[i]
  assert v[:7]==[z['prime_ids'],*z['generator'],z['norm'],z['mu'],z['incident_columns'],z['active_incident_columns']]
  assert v[7]==z['row_allowed_active_column_counts'] and list(map(bool,v[8]))==z['row_raw_d_masks']
  for r in range(e['rows']):
   for ch in range(3):assert v[9][r*6+ch*2:r*6+ch*2+2]==z['F_omega'][r][ch]
  for j,key in enumerate(d['pairOrder']):assert v[10][j*2:j*2+2]==z['Z_omega'][key] and v[12][j*2:j*2+2]==g['contribution_omega'][key]
  assert v[11]==g['ordered_column_pair_count']
  assert len(v[13])==v[5] and all(set(v[0])<=set(d['columns'][ci][3]) for ci in v[13])
  assert all(v[13][j]<v[13][j+1] for j in range(len(v[13])-1))
 results.append(dict(D=e['D'],passed=True,columns=e['columns'],divisors=e['divisors'],all_F_and_Z_and_G_and_raw_phases_checked=True))
out=ROOT/'outputs/checks/2026-11-05-signed-divisor/ui/projection-check-v1.json'
with out.open('x') as f:json.dump(dict(passed=True,cases=results,index_sha256=sha((ROOT/'web/data/signed-divisor/index-v1.json').read_bytes()),checker_sha256=sha(Path(__file__).read_bytes()),no_raw_science_rerun=True),f,indent=2);f.write('\n')
print(out)
