"""Secondary independent mpmath diagnostics for saved complete family records."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib,time
import mpmath as mp
from check_family_exact import dec,integer
mp.mp.dps=130
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'outputs/checks/2026-11-05-adaptive-theta/review';checks=0;summary=[]
def m(x):return mp.mpf(x.numerator)/x.denominator
def contained(b,v):return mp.mpf(b['lo'])/(1<<b['dyadic_bits'])<=v<=mp.mpf(b['hi'])/(1<<b['dyadic_bits'])
def radius(b):return sum((F(integer(b[name]['hi'])-integer(b[name]['lo']),2*(1<<b[name]['dyadic_bits'])) for name in ['real','imag']),F())
def target(q,s):
 parity=0 if q==5 else 1;chi={3:(0,1,-1),4:(0,1,0,-1),5:(0,1,-1,-1,1)}[q]
 return mp.power(q/mp.pi,(s+parity)/2)*mp.gamma((s+parity)/2)*mp.dirichlet(s,chi)

def audit(r):
 global checks
 q=r['q'];count=r['sample_count'];labels=[];roots=[];maxsample=mp.mpf(0);maxratio=mp.mpf(0);maxdft=mp.mpf(0);maxboundary=mp.mpf(0)
 for j,sample in enumerate(r['samples']):
  z=mp.exp(2*mp.pi*mp.j*j/count);s=mp.mpf('0.5')+mp.mpf(6)/5*z
  assert contained(sample['root_box']['real'],z.real) and contained(sample['root_box']['imag'],z.imag);checks+=1
  assert contained(sample['node_box']['real'],s.real) and contained(sample['node_box']['imag'],s.imag);checks+=1
  label=mp.mpc(m(sample['center_real']),m(sample['center_imag']));truth=target(q,s);error=abs(truth-label)
  assert error<=m(sample['radius']);checks+=1
  maxsample=max(maxsample,error);maxratio=max(maxratio,error/m(sample['radius']));labels.append(label);roots.append(z.conjugate())
 powers=[mp.mpc(1) for _ in labels]
 for n,box in enumerate(r['target_rectangles']):
  reference=sum((label*power for label,power in zip(labels,powers)),mp.mpc(0))/count
  assert contained(box['real'],reference.real) and contained(box['imag'],reference.imag);checks+=1
  t=mp.mpc(m(r['targets'][n][0]),m(r['targets'][n][1]));displacement=abs(reference-t)
  assert displacement<=m(radius(box));checks+=1;maxdft=max(maxdft,displacement)
  powers=[x*z for x,z in zip(powers,roots)]
 coefficients=[mp.mpc(m(x),m(y)) for x,y in r['coefficients']]
 for j in range(48):
  s=mp.mpf('0.5')+mp.mpf(7)/10*mp.exp(2*mp.pi*mp.j*j/48);x=(s-mp.mpf('0.5'))/(mp.mpf(6)/5);value=mp.mpc(0)
  for coefficient in reversed(coefficients):value=value*x+coefficient
  error=abs(value-target(q,s));assert error<=m(r['compact_uniform_bound']);checks+=1;maxboundary=max(maxboundary,error)
 summary.append({'q':q,'samples':count,'DFT_coefficients':len(r['target_rectangles']),'boundary_points':48,'max_sample_reference_error':str(maxsample),'max_sample_error_to_radius_ratio':str(maxratio),'max_midpoint_to_true_root_DFT_error':str(maxdft),'max_compact_boundary_error':str(maxboundary),'certified_uniform_bound':str(r['compact_uniform_bound'])})
 print(json.dumps(summary[-1]),flush=True)

experiment=Path(sys.argv[1]);raw=(experiment/'family-certificates.json').read_bytes();data=dec(json.loads(raw))
for r in data['readouts']:audit(r)
report={'passed':True,'checks':checks,'experiment':str(experiment),'family_certificate_sha256':hashlib.sha256(raw).hexdigest(),'source_sha256':data['source_sha256'],'families':summary,'producer_imported':False,'author_arithmetic_imported':False,'mpmath_version':mp.__version__,'mpmath_digits':mp.mp.dps,'comparisons_are_secondary_diagnostics_not_proof':True}
p=OUT/('family-diagnostics-'+experiment.name+'-'+str(time.time_ns())+'.json');p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'report':str(p),'checks':checks,'passed':True}))
