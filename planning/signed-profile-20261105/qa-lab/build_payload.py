"""Compact, source-hash-bound display extraction; frozen experiment is read only."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,gzip,base64,sys,math
ROOT=Path(__file__).resolve().parents[3];RUN=ROOT/'outputs/experiments/2026-11-05-profile-uniformity-v2';OUT=ROOT/'outputs/checks/2026-11-05-signed-profile/lab';DEST=ROOT/'web/data/profile-uniformity.json'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
EXPECTED='a90d1c356c276b36430b58e342ea7aee6dfe6cb33c0d7db0a4ffcb5ab17bc460';assert sha(RUN/'manifest.json')==EXPECTED
m=json.loads((RUN/'manifest.json').read_text());pins={str((RUN/n).relative_to(ROOT)):h for n,h in m['artifact_sha256'].items()};pins.update(m['source_sha256']);pins[str((RUN/'manifest.json').relative_to(ROOT))]=EXPECTED
joint=ROOT/'outputs/checks/2026-11-05-signed-profile/joint-attempt/projection-profile-v1.json';pins[str(joint.relative_to(ROOT))]='7e2ecc51744098c2ae69b3632dce136d9d6499b3ec50fb06a2a12352c1392e0a'
review=ROOT/'planning/signed-profile-20261105/review-design/REVIEW-v1.md';pins[str(review.relative_to(ROOT))]='ae360ab1af288bd16b067254b58573ad01f26f6f779d0eaaff60a7f9b213dced'
for n,h in pins.items():assert sha(ROOT/n)==h,('Protected source changed',n)
counts=dict(groups=0,allowed_multiplicities=0,float_projections=0)
def projection(x):
 f=F(x);v=float(f);assert math.isfinite(v);assert abs(F.from_float(v)-f)<=max(abs(f),F(1,10**300))*F(1,10**14);counts['float_projections']+=1;return v
def stat(exact,D,X=1):return dict(exact=str(exact),value=projection(exact),over_DX_exact=str(F(exact)/(D*X)),over_DX=projection(F(exact)/(D*X)))
def packed(value):
 b=(json.dumps(value,separators=(',',':'),sort_keys=True)+'\n').encode();z=gzip.compress(b,compresslevel=9,mtime=0);assert json.loads(gzip.decompress(z))==value;return dict(encoding='gzip-base64 UTF8 JSON',sha256=hashlib.sha256(b).hexdigest(),data=base64.b64encode(z).decode())
payload=dict(schema='profile-uniformity-display-v1',manifest_sha256=EXPECTED,source_run=str(RUN.relative_to(ROOT)),source_sha256=pins,group_fields=['N','mu','r','A','multiplicity','chi_phase','W_phase','W_zeta6','ideal_prime_norms','divisor_norms','rational_prime_factors','real_minus_one_node'],scope=m['scope'],cases=[],joint=json.loads(joint.read_text()),conductors=dict(primitive=432,squared=27,cubed=16,proof_source=str(review.relative_to(ROOT)),proof_sha256=pins[str(review.relative_to(ROOT))],status='Reviewed prose result; not asserted by the finite experiment itself'))
common_rows=None
for D in m['D_values']:
 raw=json.loads((RUN/f'norm-groups-D{D}.json').read_text());summary=json.loads((RUN/f'summary-D{D}.json').read_text());groups=raw['active_norm_groups'];rows=raw['ideal_tower_family']['rows']
 metadata=[{k:v for k,v in row.items() if k not in ['T_v','allowed_ideal_columns','allowed_norm_group_multiplicities','row_energy']} for row in rows]
 if common_rows is None:common_rows=metadata;payload['ideal_rows']=metadata
 else:assert metadata==common_rows
 compact=[]
 for g in groups:
  record=[g[k] for k in ['norm','mu','r_U','A_U','ideal_multiplicity','chi_epsilon_exponent','order6_profile_node_exponent','order6_profile_node_zeta6','ideal_prime_norms','divisor_norms','rational_prime_factors','real_minus_one_profile_node']]
  assert all(isinstance(v,int) for v in record[:7]);assert record[6]==((-record[5])+(0 if record[3]>0 else 3))%6
  compact.append(record);counts['groups']+=1
 assert sum(g[4] for g in compact)==summary['active_squarefree_ideal_columns']
 row_values=[]
 for row in rows:
  allowed=row['allowed_norm_group_multiplicities'];assert len(allowed)==len(groups)
  assert all(isinstance(a,int) and 0<=a<=g[4] for a,g in zip(allowed,compact));counts['allowed_multiplicities']+=len(allowed)
  assert sum(allowed)==row['allowed_ideal_columns'];assert sum(a*abs(g[3]) for a,g in zip(allowed,compact))==row['T_v'];assert F(row['row_energy'])==F(row['T_v']**2,D)
  row_values.append(dict(allowed=allowed,T=row['T_v'],allowed_columns=row['allowed_ideal_columns'],energy=stat(row['row_energy'],D)))
 caps=[]
 for cap in summary['tower_cumulative_caps']:
  X=cap['X'];v=dict(X=X,H=cap['H'])
  for kind,field in [('ball','primary_goodS_cumulative'),('dyadic','secondary_goodS_dyadic')]:
   item=cap[field];selected=[i for i,row in enumerate(rows) if row['good_S'] and (row['norm']<=X if kind=='ball' else X/2<=row['norm']<X)];assert len(selected)==item['rows'];assert sum(F(rows[i]['row_energy']) for i in selected)==F(item['energy']);v[kind]=dict(rows=item['rows'],energy=stat(item['energy'],D,X),selected_rows=selected)
  caps.append(v)
 cap=summary['capacity_matched_tower'];X=cap['X_floor_H_1over6'];matched=dict(H=cap['H_floor_D_3over4'],X=X,rows=cap['selected_goodS_cumulative']['rows'],energy=stat(cap['selected_goodS_cumulative']['energy'],D,X))
 payload['cases'].append(dict(D=D,U=summary['U'],norm_groups=len(groups),columns=summary['active_squarefree_ideal_columns'],unit_T=summary['sum_abs_A_over_ideals'],unit_amplitude_exact=str(F(summary['sum_abs_A_over_ideals'],summary['U'])),unit_energy=stat(summary['main_order6_profile_energy'],D),unsigned_energy=stat(summary['unsigned_order6_nodal_comparator_energy'],D),groups=packed(compact),row_values=packed(row_values),caps=caps,capacity_matched=matched,source_file=str((RUN/f'norm-groups-D{D}.json').relative_to(ROOT))))
for n,h in pins.items():assert sha(ROOT/n)==h
b=(json.dumps(payload,separators=(',',':'),sort_keys=True)+'\n').encode()
if '--verify'in sys.argv:assert DEST.read_bytes()==b
else:assert not DEST.exists();DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_bytes(b)
report=dict(passed=True,payload=str(DEST.relative_to(ROOT)),bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),manifest_sha256=EXPECTED,checks=counts,exact_source_pins=pins,scope='All six complete norm-group lists and all40-row raw masks copied and checked; every float ratio checked against Fraction; packed decoded bytes hashed; frozen source/artifact hashes checked before/after. No new scientific run.')
(OUT/('payload-verified.json' if '--verify'in sys.argv else 'payload-built.json')).write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='exact_source_pins'}))
