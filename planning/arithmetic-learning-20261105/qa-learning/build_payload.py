"""Extract display projections from immutable exact v2 arithmetic states. No training."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,math,sys,gzip,base64
ROOT=Path(__file__).resolve().parents[3]
RUN=ROOT/'outputs/experiments/2026-11-05-arithmetic-learning-v2'
DEST=ROOT/'web/data/arithmetic-learning.json'
OUT=ROOT/'outputs/checks/2026-11-05-arithmetic-learning/ui-learning'
EXPECTED_MANIFEST='1eb22dfdadaf4a92e6b6231b7edd2fbfab0e68e0751237ce45e7a11bdb6dc3b4'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(RUN/'manifest.json')==EXPECTED_MANIFEST,'Frozen manifest changed'
manifest=json.loads((RUN/'manifest.json').read_text())
pins={str((RUN/n).relative_to(ROOT)):v for n,v in manifest['artifact_sha256'].items()}
pins.update(manifest['source_sha256']);pins[str((RUN/'manifest.json').relative_to(ROOT))]=EXPECTED_MANIFEST
for n,v in pins.items():assert sha(ROOT/n)==v,('Source binding failed',n)
data=json.loads((RUN/'input.json').read_text());counts={'floats':0,'exactStrings':0,'states':0}
def val(x):
 q=Q(x);v=float(q);assert math.isfinite(v);assert abs(Q.from_float(v)-q)<=max(abs(q),Q(1,10**300))*Q(1,10**14);counts['floats']+=1;return v
def exact(x):
 s=str(x);assert Q(s)==Q(x);counts['exactStrings']+=1;return s
def vec(v):return list(map(val,v))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]+a[1]*b[1]
def abs2(a):return a[0]**2+a[0]*a[1]+a[1]**2
def logq(q):
 q=Q(q)
 if not q:return None
 # Avoid floating numerator/denominator overflow. Independent from val projection.
 v=math.log10(q.numerator)-math.log10(q.denominator);assert abs(v-math.log10(float(q)))<1e-10;return v
AUDIT=[0,1,30,34,60,100,164]
payload=dict(schema='arithmetic-learning-display-v1',source_run=str(RUN.relative_to(ROOT)),manifest_sha256=EXPECTED_MANIFEST,input_sha256=manifest['input_sha256'],source_sha256=pins,seed=manifest['seed'],tau=manifest['tau'],D=data['D'],U=data['U'],H=data['H'],profile_formula=manifest['profile_formula'],coefficient_scope=data['coefficient_scope'],nonprincipal_scope=data['nonprincipal_scope'],columns=data['columns'],pairs=data['pairs'],blocks=data['blocks'],audit_coordinates=AUDIT,projection_scope='All coordinates and residuals are binary64 display projections of exact saved rational states. Exact current-state strings are bundled for seven labelled audit coordinates; every target is exact. Full source states remain linked. No browser training.',cases=[])
for summary in manifest['cases']:
 c=json.loads((RUN/summary['file']).read_text());rc=data['row_cases'][c['row_set']];target=[list(map(Q,p)) for p in rc['Gamma']];weights={k:[list(map(Q,p)) for p in c['weights_'+k]] for k in ['CC','CM']};lam=list(map(Q,c['positive_weights']));
 diagonal={k:tuple(Q(c['exact'][k][j])-sum((p['mu_q']*mul(w,t)[j] for p,w,t in zip(data['pairs'],weights[k],target)),Q(0))/data['D'] for j in [0,1]) for k in ['CC','CM']}
 case=dict(id=summary['file'].removesuffix('.json'),source_file=str((RUN/summary['file']).relative_to(ROOT)),source_sha256=manifest['artifact_sha256'][summary['file']],row_set=c['row_set'],profile=c['profile'],row_count=rc['row_count'],unit_rows=rc['units'],raw_zero_entries=rc['raw_zero_entries'],negative_q_nonzero_CC_pair_ids=c['negative_q_nonzero_CC_pair_ids'],target_exact=[[exact(v) for v in p] for p in rc['Gamma']],target=[vec(p) for p in target],exact={k:[exact(v) for v in p] for k,p in c['exact'].items()},exact_display={k:vec(p) for k,p in c['exact'].items()},weights_CC=c['weights_CC'],weights_CM=c['weights_CM'],K_CC_squared=c['K_CC_squared'],K_CM_squared=c['K_CM_squared'],features=c['feature_predictions'],histogram_summary=[dict(block=h['block'],invalid_rows=h['invalid_rows'],occupied_phases=len(h['cells'])) for h in rc['histograms']],trajectories={})
 for method in ['metric','ordinary']:
  source=c[method+'_GD'];states=[]
  for s in source['states']:
   g=[tuple(map(Q,p)) for p in s['coordinates']];res=[(x[0]-t[0],x[1]-t[1]) for x,t in zip(g,target)];loss=Q(s['weighted_full_loss']);assert loss==sum(w*abs2(v) for w,v in zip(lam,res))
   predicted={k:tuple(diagonal[k][j]+sum((p['mu_q']*mul(w,x)[j] for p,w,x in zip(data['pairs'],weights[k],g)),Q(0))/data['D'] for j in [0,1]) for k in ['CC','CM']}
   bounds={k:Q(c['K_'+k+'_squared'])*loss/data['D']**2 for k in ['CC','CM']};bounds['uniform']=loss/min(lam)
   errors={k:tuple(predicted[k][j]-Q(c['exact'][k][j]) for j in [0,1]) for k in ['CC','CM']}
   if method=='metric':
    for k in ['CC','CM']:
     assert tuple(map(Q,s['predicted_'+k]))==predicted[k];assert Q(s['certificate_'+k+'_squared'])==bounds[k];assert Q(s['actual_error_'+k+'_squared'])==abs2(errors[k])
   state=dict(step=s['step'],coordinates=[vec(x) for x in g],residuals=[vec(x) for x in res],audit_exact={str(i):[exact(v) for v in s['coordinates'][i]] for i in AUDIT},loss=val(loss),loss_exact=exact(s['weighted_full_loss']),log_loss=logq(loss),predicted={k:vec(v) for k,v in predicted.items()},errors={k:vec(v) for k,v in errors.items()},log_bounds_squared={k:logq(v) for k,v in bounds.items()},bounds_squared={k:val(v) for k,v in bounds.items()},actual_errors_squared={k:val(abs2(v)) for k,v in errors.items()},accepted=bool(s.get('accepted',False)))
   states.append(state);counts['states']+=1
  case['trajectories'][method]=dict(updates=source['updates_executed'],type=source['type'],states=states,requested_tau_certified=method=='metric',budget_limited=method=='ordinary',eta=source.get('eta'),rho=source.get('rho'))
 payload['cases'].append(case)
for case in payload['cases']:
 for method,t in case['trajectories'].items():
  states=t.pop('states');raw=json.dumps(states,separators=(',',':'),sort_keys=True).encode();packed=gzip.compress(raw,compresslevel=9,mtime=0)
  assert json.loads(gzip.decompress(packed))==states
  t.update(state_count=len(states),states_sha256=hashlib.sha256(raw).hexdigest(),states_encoding='gzip-base64 UTF8 JSON; native browser DecompressionStream',states_gzip_base64=base64.b64encode(packed).decode())
serialized=(json.dumps(payload,separators=(',',':'),sort_keys=True)+'\n').encode()
if '--verify' in sys.argv:assert DEST.read_bytes()==serialized,'Display bytes differ from source-derived projection'
else:
 assert not DEST.exists() or DEST.read_bytes()==(OUT/'payload-unpacked-v1.json').read_bytes(),'Preserve accepted payload; use --verify'
 DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_bytes(serialized)
for n,v in pins.items():assert sha(ROOT/n)==v,('Protected source changed during extraction',n)
receipt=dict(passed=True,payload=str(DEST.relative_to(ROOT)),sha256=hashlib.sha256(serialized).hexdigest(),bytes=len(serialized),source_pins=pins,checks=counts,checks_scope='Every coordinate/residual/prediction/error/loss/certificate display float checked against exact Fraction at relative tolerance1e-14; exact strings parsed identically; every generated byte reproduced in --verify; all metric signed outputs match saved source fields; ordinary signed outputs/certificates are display extractions from actual saved states and the declared transfer inequality.',no_training=True,full_input_bundled=False)
# Verification writes a new receipt name, preserving the original extraction receipt.
name='payload-verified-v2.json' if '--verify' in sys.argv else 'payload-built-v2.json'
(OUT/name).write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({k:v for k,v in receipt.items() if k!='source_pins'}))
