"""Independent exact-endpoint design checks; no imports of producer code."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json, sys
sys.set_int_max_str_digits(100000)
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'outputs/checks/2026-11-05-adaptive-readout/design/design-checks.json'
FROZEN=ROOT/'outputs/experiments/2026-11-04-validated-oracle-final-v5/oracle-certificates.json'
SHA='85e3bed76ad4067084ab5f8413b7159e4c5169e5d7cef0469d36164e82dfbca8'
SOURCE={'dyadic.py':'82e995ae9f67395980cec3f06bf493931de0413c7ce024562283882c01425170','theta_oracle.py':'c50857831de0fc5faa6829cf539c7d31dc32958b76412c27689235aeba95d2c1'}
if OUT.exists(): raise FileExistsError('Preserve earlier design evidence')
frozen_bytes=FROZEN.read_bytes(); assert hashlib.sha256(frozen_bytes).hexdigest()==SHA
j=json.loads(frozen_bytes)
for name,expected in SOURCE.items():
 for p in (ROOT/'examples/analytic_oracle'/name,FROZEN.parent/name):
  assert hashlib.sha256(p.read_bytes()).hexdigest()==expected
assert j['source_sha256']==SOURCE
f=lambda x:F(int(x['numerator']),int(x['denominator']))
def enc(x):
 if isinstance(x,F):return {'numerator':str(x.numerator),'denominator':str(x.denominator),'display':float(x)}
 if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [enc(v) for v in x]
 return x
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[1],-a[0])
def mul(a,b):
 v=[x*y for x in a for y in b];return (min(v),max(v))
def ca(a,b):return (add(a[0],b[0]),add(a[1],b[1]))
def cm(a,b):return (add(mul(a[0],b[0]),neg(mul(a[1],b[1]))),add(mul(a[0],b[1]),mul(a[1],b[0])))
def scale(a,x):return (mul(a[0],(x,x)),mul(a[1],(x,x)))
def component(x):
 assert type(x['dyadic_bits']) is int and x['dyadic_bits']==224
 lo,hi=F(int(x['lo']),2**224),F(int(x['hi']),2**224);assert lo<=hi;return (lo,hi)
def box(x):return (component(x['real']),component(x['imag']))
def rad(b):return sum(((v[1]-v[0])/2 for v in b),F())
def mid(b):return tuple((v[0]+v[1])/2 for v in b)
def subset(a,b):return all(y[0]<=x[0]<=x[1]<=y[1] for x,y in zip(a,b))
u,v,w=F(7,12),F(7,24),F(1,2**64)
results=[];passed=0
for q in (3,4,5):
 rows=[s for s in j['samples'] if s['q']==q]
 assert len(rows)==64 and all(s['node_index']==i and s['node_count']==64 for i,s in enumerate(rows));passed+=1
 eta=max(f(s['radius']) for s in rows);M={3:4,4:10,5:6}[q]
 labels=[((f(s['center_real']),)*2,(f(s['center_imag']),)*2) for s in rows]
 roots=[(box(s['root_box'])[0],neg(box(s['root_box'])[1])) for s in rows]
 powers=[((F(1),F(1)),(F(),F())) for s in rows]
 boxes=[]
 for n in range(64):
  total=((F(),F()),(F(),F()))
  for label,power in zip(labels,powers):total=ca(total,cm(label,power))
  boxes.append(scale(total,F(1,64)))
  powers=[cm(p,z) for p,z in zip(powers,roots)]
 bases=[];A=F();S_u=F();S_v=F()
 for d,b in enumerate(boxes):
  A+=rad(b)*u**d;S_u+=u**d;S_v+=v**d
  oracle=eta*S_u;alias=M*w/(1-w)*S_v;taylor=M*v**(d+1)/(1-v)
  bases.append({'degree':d,'oracle':oracle,'alias':alias,'Taylor':taylor,'exact_endpoint_DFT_arithmetic':A,'base':oracle+alias+taylor+A})
 dmin=min(range(64),key=lambda d:bases[d]['base']);floor=bases[dmin]['base']
 # Strict-slack selector: equality deliberately refuses, eps above floor admits.
 select=lambda eps:next((d for d,r in enumerate(bases) if r['base']<eps),None)
 assert select(floor) is None and select(floor+F(1,10**40)) is not None;passed+=2
 selected={}
 for eps in (F(1,10**12),F(1,10**15),F(1,10**16),F(1,10**20)):
  d=select(eps)
  if d is None:selected[str(eps)]={'status':'not_certified'};continue
  targets=[mid(b) for b in boxes[:d+1]]
  state=[(F(),F()) for _ in targets];loss_prev=None;weighted_prev=None;k=0
  slack=eps-bases[d]['base']
  while True:
   diffs=[(a-x,b-y) for (a,b),(x,y) in zip(state,targets)]
   loss=sum((a*a+b*b for a,b in diffs),F())/2
   weighted=sum(((abs(a)+abs(b))*u**n for n,(a,b) in enumerate(diffs)),F())
   if loss_prev is not None:
    assert loss==F(9,16)*loss_prev and weighted==F(3,4)*weighted_prev;passed+=2
   if weighted<=slack:break
   loss_prev,weighted_prev=loss,weighted
   state=[((3*a+x)/4,(3*b+y)/4) for (a,b),(x,y) in zip(state,targets)];k+=1
   assert k<10000
  assert bases[d]['base']+weighted<=eps;passed+=1
  selected[str(eps)]={'status':'certified_design','degree':d,'steps':k,'bound':bases[d]['base']+weighted}
 # Existing versioned output uses outward dyadic operations; its B must contain
 # independently propagated exact-endpoint natural rectangles for each degree.
 output_comparisons=[]
 for version in ('1e-12-v1','1e-15-v1'):
  p=ROOT/f'outputs/experiments/2026-11-05-adaptive-readout-{version}/readout-certificates.json'
  if not p.exists():continue
  data=json.loads(p.read_text());r=next(r for r in data['readouts'] if r['q']==q)
  for n,b in enumerate(r['target_rectangles']):assert subset(boxes[n],box(b));passed+=1
  assert r['minimum_base_degree']==dmin;passed+=1
  actual_floor=f(r['minimum_base_budget']);assert actual_floor>=floor;passed+=1
  output_comparisons.append({'version':version,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'minimum_base_degree':dmin,'actual_outward_dyadic_floor':actual_floor,'exact_endpoint_floor':floor,'extra_dyadic_width_floor':actual_floor-floor})
 results.append({'q':q,'eta':eta,'minimum_base_degree':dmin,'exact_endpoint_floor':floor,'floors_by_degree':bases,'request_design_checks':selected,'existing_output_comparisons':output_comparisons})
assert hashlib.sha256(FROZEN.read_bytes()).hexdigest()==SHA
for name,expected in SOURCE.items():assert hashlib.sha256((ROOT/'examples/analytic_oracle'/name).read_bytes()).hexdigest()==expected
report={'status':'passed','checks_passed':passed,'input_certificate_sha256':SHA,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'meaning':'Independent exact-rational endpoint DFT and finite-readout parameter/loss checks; not an oracle rerun or formal proof','results':results}
OUT.write_text(json.dumps(enc(report),indent=2)+'\n')
print(json.dumps({'checks_passed':passed,'receipt':str(OUT),'floors':[{'q':r['q'],'degree':r['minimum_base_degree'],'display':float(r['exact_endpoint_floor'])} for r in results]}))
