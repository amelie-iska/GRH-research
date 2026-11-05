#!/usr/bin/env python3
"""Saved-record implementation consistency/CLI controls, no author routine import."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import hashlib,json,subprocess,os
ROOT=Path(__file__).resolve().parents[3]
RUN=ROOT/'outputs/experiments/2026-11-05-profile-uniformity-v2'
OUT=ROOT/'outputs/checks/2026-11-05-signed-profile/implementation/saved-consistency-v2.json'
if OUT.exists():raise FileExistsError(OUT)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((RUN/'manifest.json').read_text())
assert sha(RUN/'manifest.json')=='a90d1c356c276b36430b58e342ea7aee6dfe6cb33c0d7db0a4ffcb5ab17bc460'
for name,h in m['artifact_sha256'].items():assert sha(RUN/name)==h,name
for name,h in m['source_sha256'].items():assert sha(ROOT/name)==h,name
pin=ROOT/m['source_pin_path'];assert sha(pin)==m['source_pin_sha256']
assert pin.stat().st_mtime_ns<(RUN/'manifest.json').stat().st_mtime_ns
roots=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
def em(x,y):return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1]
def norm(x):return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]
count=mask_entries=nontrivial_A_checks=0;cases=[]
for D in m['D_values']:
 d=json.loads((RUN/f'norm-groups-D{D}.json').read_text());s=json.loads((RUN/f'summary-D{D}.json').read_text());groups=d['active_norm_groups'];U=s['U']
 assert U*U==D and sorted([g['norm'] for g in groups]+[n for ns in d['rejected_integer_norms'].values() for n in ns])==list(range(D+1,2*D))
 S=0;z=[0,0]
 for g in groups:
  A=g['A_U'];N=g['norm'];multy=g['ideal_multiplicity'];e=((N-1)//6)%6;w=g['order6_profile_node_exponent']
  assert e==g['chi_epsilon_exponent'] and g['order6_profile_node_zeta6']==list(roots[w])
  assert tuple(A*t for t in roots[(e+w)%6])==(abs(A),0)
  S+=multy*abs(A)
  for j in (0,1):z[j]+=multy*A*roots[e][j]
  if abs(A)>1:
   actual=0
   for labels in product((0,1,2),repeat=len(g['ideal_prime_norms'])):
    a=b=1;sgn=1
    for n,label in zip(g['ideal_prime_norms'],labels):
     if label==1:a*=n;sgn=-sgn
     elif label==2:b*=n;sgn=-sgn
    if a<=U and b<=U:actual+=sgn
   assert actual==A,(D,N,A,actual);nontrivial_A_checks+=1
  count+=1
 assert S==s['sum_abs_A_over_ideals'] and Q(s['unit_row_energy'])==Q(S*S,D)
 assert z==s['unsigned_order6_nodal_sum_zeta6'] and Q(s['unsigned_nodal_comparator_energy'])==Q(z[0]**2+z[0]*z[1]+z[1]**2,D)
 tower=d['ideal_tower_family'];vs=tower['rows'];assert len(vs)==40
 assert len({tuple(v['literal_row_omega']) for v in vs})==40
 for v in vs:
  beta=tuple(v['generator_omega']);p=(1,0)
  for j in range(6):p=em(p,beta)
  assert em((1,1),p)==tuple(v['literal_row_omega']) and norm(em((1,1),p))==v['norm']**6
  split={int(p):c for p,c in v['split_prime_coverage'].items()};inert=set(v['inert_prime_coverage']);allowed=[]
  for g in groups:
   multy=1
   for p,e in g['rational_prime_factors']:
    if p%3==1:
     sigma=split.get(p,0)
     if e==1:multy*=2-sigma
     elif sigma:multy=0;break
    elif p in inert:multy=0;break
   allowed.append(multy);mask_entries+=1
  assert allowed==v['allowed_norm_group_multiplicities']
  T=sum(a*abs(g['A_U']) for a,g in zip(allowed,groups));assert T==v['T_v'] and Q(v['row_energy'])==Q(T*T,D)
 for c in tower['caps']:
  X=c['X'];primary=[v for v in vs if v['good_S'] and v['norm']<=X];dyadic=[v for v in vs if v['good_S'] and 2*v['norm']>=X and v['norm']<X]
  assert c['H']==X**6
  for label,rows in [('primary_goodS_cumulative',primary),('secondary_goodS_dyadic',dyadic)]:
   assert c[label]['rows']==len(rows) and Q(c[label]['energy'])==sum((Q(v['row_energy']) for v in rows),Q(0))
  assert primary and any(v['norm']==1 for v in primary)
 cap=tower['capacity_matched'];H=cap['H_floor_D_3over4'];X=cap['X_floor_H_1over6'];assert H**4<=D**3<(H+1)**4 and X**6<=H<(X+1)**6
 selected=[v for v in vs if v['good_S'] and v['norm']<=X];assert len(selected)==cap['selected_goodS_cumulative']['rows']==1
 at49=[v for v in vs if v['norm']==49];assert sorted(int(v['split_prime_coverage']['7']) for v in at49)==[1,1,2]
 assert min(v['T_v'] for v in at49 if v['split_prime_coverage']['7']==1)>next(v['T_v'] for v in at49 if v['split_prime_coverage']['7']==2)
 cases.append(dict(D=D,unit_energy=s['unit_row_energy'],unit_energy_over_D=s['energy_divided_by_D'],X64_goodS_rows=tower['caps'][-1]['primary_goodS_cumulative']['rows'],X64_energy=tower['caps'][-1]['primary_goodS_cumulative']['energy'],matched_cap=X))
# Refusals use existing accepted paths or a never-created invalid target.
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1');module='examples/profile_uniformity/unit_profile.py';invalid=ROOT/'outputs/experiments/2026-11-05-profile-uniformity-invalid-v2'
contracts=[]
for name,args,needle in [('existing_run',['--output',str(RUN),'--source-pin',str(pin)],'Preserve existing output'),('existing_source_pin',['--freeze-source-pin',str(pin)],'Preserve existing output'),('non_square_D',['--D','257','--source-pin',str(pin),'--output',str(invalid)],'integer square'),('float_D_text',['--D','256.0','--source-pin',str(pin),'--output',str(invalid)],'invalid int value')]:
 p=subprocess.run([sys.executable,module,*args],cwd=ROOT,env=env,capture_output=True,text=True)
 assert p.returncode and needle in p.stderr,(name,p.returncode,p.stderr)
 contracts.append(dict(name=name,refused=True,returncode=p.returncode,reason=needle))
assert not invalid.exists()
for name,h in m['source_sha256'].items():assert sha(ROOT/name)==h
report=dict(passed=True,scope='Implementation saved-record and fresh-output contract consistency only; independent full scientific audit belongs to a separate reviewer',run_manifest_sha256=sha(RUN/'manifest.json'),source_pin_sha256=sha(pin),sources_frozen_before_manifest=True,norm_groups_checked=count,raw_mask_multiplicity_entries_checked=mask_entries,nontrivial_A_direct_ternary_definition_checks=nontrivial_A_checks,all_small_ideal_rows_distinct=40,source_and_artifact_hashes_pass=True,contracts=contracts,cases=cases,checker_sha256=sha(Path(__file__)),fixed_profile_counterexample_claim=False,asymptotic_cDX_proof_claim=False,exact_conductor_claim=False)
with OUT.open('x') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('cases','contracts')},indent=2))
