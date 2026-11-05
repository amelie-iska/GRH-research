"""Exact certificate reconstruction plus secondary existing-mpmath diagnostics."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib,time
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'examples/analytic_oracle'))
import adaptive_theta as a
import mpmath as mp
mp.mp.dps=140
OUT=ROOT/'outputs/checks/2026-11-05-adaptive-theta/review';source={n:(ROOT/'examples/analytic_oracle'/n).read_bytes() for n in ['precision.py','adaptive_theta.py']};rows=[];checks=0

def m(v):return mp.mpf(v.numerator)/v.denominator

def contained(box,x):return mp.mpf(box['lo'])/(1<<box['dyadic_bits'])<=x<=mp.mpf(box['hi'])/(1<<box['dyadic_bits'])

def reference(q,s):
 parity,chi=a.FAMILIES[q]
 return mp.power(q/mp.pi,(s+parity)/2)*mp.gamma((s+parity)/2)*mp.dirichlet(s,chi)

def inspect(r,s,node=None):
 global checks
 eta=r['requested_sample_error'];budget=r['budget'];box=r['quadrature_sum_box'];bits=r['bits']
 reconstructed=sum((F(int(box[name]['hi'])-int(box[name]['lo']),2*(1<<bits)) for name in ['real','imag']),F())
 assert reconstructed==r['raw_interval_radius']<=budget['interval_arithmetic'];checks+=1
 B=r['budget_rounding_bits'];unit=F(1,1<<B);plan=a.parameters(r['q'],eta)
 raw={'n_tail':plan.n_tail,'time_tail':plan.time_tail,'quadrature':plan.quadrature,'discard':plan.discard,'interval_arithmetic':reconstructed}
 for name,value in raw.items():
  rounded=F(-(-value.numerator*(1<<B)//value.denominator),1<<B)
  assert budget[name]==rounded and 0<=budget[name]-value<unit;checks+=1
 assert 5*unit<=eta/8 and r['radius']<=7*eta/8;checks+=1
 assert all(v>=0 for v in budget.values()) and r['radius']==sum(budget.values(),F())<=eta;checks+=1
 assert all(raw[name]<=eta/8 for name in ['n_tail','time_tail','quadrature','discard']);checks+=1
 assert reconstructed<=eta/4;checks+=1
 assert r['center_real']==F(int(box['real']['lo'])+int(box['real']['hi']),2*(1<<bits));checks+=1
 assert r['center_imag']==F(int(box['imag']['lo'])+int(box['imag']['hi']),2*(1<<bits));checks+=1
 assert contained(r['node_box']['real'],s.real) and contained(r['node_box']['imag'],s.imag);checks+=1
 truth=reference(r['q'],s);distance=abs(truth-mp.mpc(m(r['center_real']),m(r['center_imag'])))
 assert distance<=m(r['radius']);checks+=1
 if node is not None:
  assert contained(r['root_box']['real'],node.real) and contained(r['root_box']['imag'],node.imag);checks+=1
 for attempt in r['precision_attempts'][:-1]:assert attempt['interval_radius']>eta/4;checks+=1
 assert r['precision_attempts'][-1]['interval_radius']==reconstructed;checks+=1
 rows.append({'certificate':a.encode(r),'mpmath_target_real':str(truth.real),'mpmath_target_imag':str(truth.imag),'mpmath_distance_to_center':str(distance),'diagnostic_error_to_certified_radius_ratio':str(distance/m(r['radius']))})
 print(json.dumps({'q':r['q'],'eta':str(eta),'kind':r['target_kind'],'bits':bits,'attempt_bits':[v['bits'] for v in r['precision_attempts']],'diagnostic_error_ratio':str(distance/m(r['radius']))}),flush=True)

for eta in [F(1,10**24),F(1,10**32)]:
 for q in [3,4,5]:
  x,y=(F(-1),F(4,3)) if q==5 else (F(1,2),F())
  r=a.point(q,x,y,eta,initial_bits=32);inspect(r,mp.mpc(m(x),m(y)))
 # A fresh asymmetric true circle node, rebuilt from initial precision32.
 q=5;j=7;count=64;node=mp.exp(2*mp.pi*mp.j*j/count);s=mp.mpf('0.5')+mp.mpf(6)/5*node
 r=a.circle(q,j,count,eta,initial_bits=32);inspect(r,s,node)
assert all((ROOT/'examples/analytic_oracle'/n).read_bytes()==b for n,b in source.items()),'source changed during diagnostics'
report={'passed':True,'checks':checks,'samples':rows,'source_sha256':{n:hashlib.sha256(b).hexdigest() for n,b in source.items()},'mpmath_version':mp.__version__,'mpmath_digits':mp.mp.dps,'mpmath_is_secondary_diagnostic_not_interval_proof':True,'certificates_exactly_reconstructed':True}
p=OUT/('sample-diagnostics-'+str(time.time_ns())+'.json');p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'report':str(p),'passed':True,'checks':checks,'samples':len(rows),'mpmath_version':mp.__version__}))
