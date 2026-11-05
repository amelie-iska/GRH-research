"""Read-only finite Frobenius/incidence coefficient-tail budgets from frozen counts."""
from pathlib import Path
from itertools import combinations
from math import isqrt
from fractions import Fraction
import json,hashlib
R=Path(__file__).resolve().parents[3];O=R/'outputs/checks/2026-11-05-signed-divisor/review-design';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source=R/'planning/signed-divisor-20261105/root/DIVISOR_INCIDENCE_LIFT-v2.md';assert sha(source)=='a062a9b85603c0e7b300c219db10724c4b33f57c060eb51e6a5b5f201faa3732'
results=[]
for D,manifest_hash in [(144,'b2db0dfb8f7b3f7ddc6cdd3c4fb3efd88b0e4bec6a805b341240b3722c075380'),(576,'ea68ea46eec092da39e3e6d282152f69e6c944cb6a15ae1e1efac439ef4a8675'),(60000,'fecbec83a4fadd301d7845daddcb7e31f216705a6b29c5ba98436642ae0b2e4f')]:
 base=R/f'outputs/experiments/2026-11-05-signed-divisor-D{D}-v1';assert sha(base/'manifest.json')==manifest_hash;manifest=json.loads((base/'manifest.json').read_text());names=['columns.json','divisor-energies.jsonl','parameters.json','summary.json']
 for name in names:assert sha(base/name)==manifest['files'][name]['sha256']
 cols=json.loads((base/'columns.json').read_text());pars=json.loads((base/'parameters.json').read_text());summary=json.loads((base/'summary.json').read_text());Ed={}
 with (base/'divisor-energies.jsonl').open()as f:
  for line in f:
   row=json.loads(line);key=tuple(sorted(row['prime_ids']));assert key not in Ed and len(key)==len(set(key));Ed[key]=sum(row['row_allowed_active_column_counts'])
 B=[]
 for c in cols:
  fs=tuple(sorted(c['prime_ids']));assert len(fs)==len(set(fs));ds=[sub for k in range(len(fs)+1)for sub in combinations(fs,k)];assert all(d in Ed for d in ds);B.append(sum(Ed[d]for d in ds))
 budgets=[]
 for X in ['A','C','mu']:
  total=sum(b*c[X]*c[X]for b,c in zip(B,cols));actual=summary['divisor_budget'][X+X]['signed_numerator_omega'];assert actual[1]==0 and abs(actual[0])<=total
  for cutoff in range(0,max(len(c['prime_ids'])for c in cols)+1):
   E=sum(b*c[X]*c[X]for b,c in zip(B,cols)if len(c['prime_ids'])>cutoff);T=total-E;rad=4*T*E;ceil=isqrt(rad);ceil+=ceil*ceil<rad
   budgets.append({'channel':X,'keep_ideal_omega_at_most':cutoff,'tail_columns':sum(len(c['prime_ids'])>cutoff for c in cols),'T_integer':T,'E_integer':E,'exact_error_bound_before_D':f'{E}+sqrt({rad})','safe_rational_error_bound':str(Fraction(E+ceil,D))})
 for name in names:assert sha(base/name)==manifest['files'][name]['sha256']
 results.append({'D':D,'manifest_sha256':manifest_hash,'rows':summary['counts']['rows'],'columns':len(cols),'divisors':len(Ed),'lambda_definition':'E_d=sum saved actual nonzero-row/incident-column counts','sum_Ed':sum(Ed.values()),'min_B':min(B),'max_B':max(B),'B_weighted_norms':{X:sum(b*c[X]*c[X]for b,c in zip(B,cols))for X in ['A','C','mu']},'tail_certificates':budgets})
result={'passed':True,'source_path':str(source.relative_to(R)),'source_sha256':sha(source),'cases':results,'exact_arithmetic':'Integer coefficient/Frobenius counts, exact radical or rational ceiling bound; no floats.','method':'O(sum column ideal-divisors) incidence norm derivation after streaming saved E_d counts; no character/factor/bucket/direct-pair experiment rerun.','scope':'Finite coefficient-tail error certificates for these exact phase tables, conditional on each table/count being the actual frozen family. Smalltables independently accepted; large count validation is A separate audit, not claimed here. Bounds may be very loose and prove no signed/asymptotic saving.','checker_sha256':sha(Path(__file__))}
p=O/'finite-incidence-budgets-v1.json'
with p.open('x')as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({'passed':True,'receipt':str(p.relative_to(R)),'sha256':sha(p),'case_norms':[{k:v for k,v in r.items()if k in['D','sum_Ed','min_B','max_B','B_weighted_norms']}for r in results]},indent=2))
