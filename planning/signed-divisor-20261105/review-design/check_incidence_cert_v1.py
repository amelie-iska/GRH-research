from pathlib import Path
import sys,json,hashlib
sys.dont_write_bytecode=True
from independent_small_family_v1 import add,mul,conj,norm,scale,divisors,ZERO
R=Path(__file__).resolve().parents[3];O=R/'outputs/checks/2026-11-05-signed-divisor/review-design';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();source=R/'planning/signed-divisor-20261105/root/DIVISOR_INCIDENCE_LIFT-v2.md';assert sha(source)=='a062a9b85603c0e7b300c219db10724c4b33f57c060eb51e6a5b5f201faa3732'
checks=[];bindings={}
for D,name in [(144,'independent-D144-v1.json'),(576,'independent-D576-v2.json')]:
 p=O/name;bindings[str(p.relative_to(R))]=sha(p);d=json.loads(p.read_text());cols=d['columns'];raw=d['raw_character_values'];ds=[[x[0]for x in divisors(tuple(tuple(p)for p in c['fs']))]for c in cols];Ed={tuple(x['g']):0 for x in d['divisors']}
 for values in raw:
  for j,z in enumerate(values):
   if tuple(z)!=ZERO:
    for g in ds[j]:Ed[g]+=1
 B=[sum(Ed[g]for g in sub)for sub in ds];K=[[ZERO for _ in cols]for _ in cols]
 for i,c in enumerate(cols):
  for j,e in enumerate(cols):
   if set(map(tuple,c['fs']))&set(map(tuple,e['fs'])):continue
   for values in raw:K[i][j]=add(K[i][j],mul(values[i],conj(values[j])))
 def energy(v):
  out=ZERO
  for i,x in enumerate(v):
   if tuple(x)==ZERO:continue
   for j,y in enumerate(v):
    if tuple(y)!=ZERO:out=add(out,mul(mul(x,conj(y)),K[i][j]))
  assert out[1]==0
  return out[0]
 def weighted(v):return sum(b*norm(z)for b,z in zip(B,v))
 vectors={k:[(c['x'][i],0)for c in cols]for i,k in enumerate(['A','C','mu'])}
 assert energy(vectors['A'])==d['direct_pair'][0][0][0]
 cases=[('A_single-prime-truncation',vectors['A'],[x if len(c['fs'])<=1 else ZERO for c,x in zip(cols,vectors['A'])]),('C_half-annulus-truncation',vectors['C'],[x if norm(c['g'])<=3*D//2 else ZERO for c,x in zip(cols,vectors['C'])]),('mu_alternate-column-truncation',vectors['mu'],[x if i%2==0 else ZERO for i,x in enumerate(vectors['mu'])])]
 for channel in ['A','mu']:
  v=vectors[channel];chosen=None
  for j in range(len(cols)):
   t=list(v);t[j]=add(t[j],(-1,0));diff=energy(v)-energy(t)
   if diff!=0:chosen=j;break
  assert chosen is not None
  q=chosen;factor=B[q]+1;x=[scale(z,factor)for z in v];t=list(x);t[q]=add(t[q],(-1,0));cases.append((channel+'_scaled-actual-vector-one-entry-error',x,t))
 for label,x,t in cases:
  e=[add(z,scale(w,-1))for z,w in zip(x,t)];T=weighted(t);E=weighted(e);difference=abs(energy(x)-energy(t));L=difference-E
  assert T>=0 and E>=0
  if L>0:assert L*L<=4*T*E
  checks.append({'D':D,'label':label,'T_integer':T,'E_integer':E,'D_times_absolute_pairing_error':difference,'L_integer':L,'nonvacuous_squared_check':L>0,'squared_check_passed':True})
result={'passed':True,'source_path':str(source.relative_to(R)),'source_sha256':sha(source),'independent_data_sha256':bindings,'checks':checks,'count':len(checks),'nonvacuous_squared_checks':sum(c['nonvacuous_squared_check']for c in checks),'exact_arithmetic':'Integer Z[omega] only; L=D*abs(Qx-Qt)-E, if L>0 check L²<=4TE. No square-root floats or field/author rerun.','scope':'Finite coefficient-error certificate for actual small-family phase tables. Three literal A/C/mu truncations and two scaled actual-vector one-entry perturbations per family; the scaled controls are lemma tests, not original-family energy measurements or an asymptotic bound.','checker_sha256':sha(Path(__file__))}
p=O/'incidence-cert-controls-v1.json'
with p.open('x')as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({'passed':True,'checks':len(checks),'nonvacuous':result['nonvacuous_squared_checks'],'receipt':str(p.relative_to(R)),'sha256':sha(p)},indent=2))
