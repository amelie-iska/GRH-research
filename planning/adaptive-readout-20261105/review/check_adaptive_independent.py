"""Independent exact verification; no import of producer or dyadic arithmetic.

Rebuilds outward integer rectangle arithmetic; trusts the pinned upstream
analytic certificate/review, not an unproved numerical equality. Optional
mpmath checks are diagnostics. Evidence is versioned by time_ns.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse, hashlib, json, time
ROOT=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
UPSTREAM=ROOT/'outputs/experiments/2026-11-04-validated-oracle-final-v5'
FROZEN_SHA='85e3bed76ad4067084ab5f8413b7159e4c5169e5d7cef0469d36164e82dfbca8'
DYADIC_SHA='82e995ae9f67395980cec3f06bf493931de0413c7ce024562283882c01425170'
THETA_SHA='c50857831de0fc5faa6829cf539c7d31dc32958b76412c27689235aeba95d2c1'
S=1<<224
u,v,w=Q(7,12),Q(7,24),Q(1,1<<64)
GROWTH={3:4,4:10,5:6}
def hashfile(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def f(x):
 assert isinstance(x,dict) and type(x['numerator']) is str and type(x['denominator']) is str
 return Q(int(x['numerator']),int(x['denominator']))
def ceil(a,b):return -((-a)//b)
def ri(x):return (x.numerator*S//x.denominator,ceil(x.numerator*S,x.denominator))
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def neg(a):return(-a[1],-a[0])
def mul(a,b):
 p=[x*y for x in a for y in b]
 return(min(p)//S,ceil(max(p),S))
def cadd(a,b):return(add(a[0],b[0]),add(a[1],b[1]))
def cmul(a,b):return(add(mul(a[0],b[0]),neg(mul(a[1],b[1]))),add(mul(a[0],b[1]),mul(a[1],b[0])))
def cdiv64(a):return tuple((x[0]//64,ceil(x[1],64)) for x in a)
def box(d):
 ans=[]
 for key in ('real','imag'):
  z=d[key];assert type(z['dyadic_bits'])is int and z['dyadic_bits']==224
  lo,hi=int(z['lo']),int(z['hi']);assert lo<=hi;ans.append((lo,hi))
 return tuple(ans)
def midpoint(a):return tuple(Q(x+y,2*S) for x,y in a)
def radius(a):return sum((Q(y-x,2*S) for x,y in a),Q())
def independent_bounds(rows):
 labels=[(ri(f(s['center_real'])),ri(f(s['center_imag']))) for s in rows]
 roots=[(box(s['root_box'])[0],neg(box(s['root_box'])[1])) for s in rows]
 powers=[((S,S),(0,0)) for _ in rows];bounds=[]
 for n in range(64):
  total=((0,0),(0,0))
  for j in range(64):total=cadd(total,cmul(labels[j],powers[j]))
  bounds.append(cdiv64(total))
  powers=[cmul(a,b) for a,b in zip(powers,roots)]
 return bounds,max(f(s['radius']) for s in rows)
def base(bounds,eta,q,d):
 return {'oracle':eta*sum((u**n for n in range(d+1)),Q()),
         'alias':GROWTH[q]*w/(1-w)*sum((v**n for n in range(d+1)),Q()),
         'Taylor':GROWTH[q]*v**(d+1)/(1-v),
         'coefficient_arithmetic':sum((radius(bounds[n])*u**n for n in range(d+1)),Q())}
def pairs(encoded):return [tuple(map(f,p)) for p in encoded]
def verify(directory,up,bounds,data=None):
 if data is None:data=json.loads((directory/'readout-certificates.json').read_text())
 assert data['input_certificate_sha256']==FROZEN_SHA and data['GRH_proved']is False and data['new_Lean_declarations']==0
 assert data['source_sha256']['dyadic.py']==DYADIC_SHA
 for name,sha in data['source_sha256'].items():assert hashfile(directory/name)==sha
 assert [r['q'] for r in data['readouts']]==[3,4,5]
 models=[];updates=0;coefficient_states=0
 for r in data['readouts']:
  q=r['q'];B,eta=bounds[q];eps=f(r['requested_tolerance']);d=r['degree'];steps=r['steps']
  assert type(q)is int and q in GROWTH and type(d)is int and 0<=d<64 and type(steps)is int and steps>=0
  assert r['sample_count']==64 and f(r['gradient_step'])==Q(1,4) and f(r['compact_radius'])==Q(7,10)
  assert r['coefficient_basis']=='((s-1/2)/(6/5))^n'
  assert 'rational Fourier-midpoint' in r['objective'] and 'not its exact optimizer trajectory' in r['original_gradient_relation']
  bs=[base(B,eta,q,j) for j in range(64)];totals=[sum(z.values(),Q()) for z in bs]
  assert list(map(f,r['all_degree_base_budgets']))==totals
  floor=min(range(64),key=lambda j:totals[j]);assert r['minimum_base_degree']==floor and f(r['minimum_base_budget'])==totals[floor]
  assert d==next(j for j in range(64) if totals[j]<eps)
  targets=[midpoint(z) for z in B[:d+1]]
  assert pairs(r['targets'])==targets and list(map(box,r['target_rectangles']))==B[:d+1]
  assert len(r['trace'])==steps+1
  previous=None;previous_J=None;previous_R=None;threshold=eps-totals[d]
  for k,t in enumerate(r['trace']):
   assert type(t['iteration'])is int and t['iteration']==k
   state=pairs(t['coefficients']);assert len(state)==d+1
   if previous is None:assert state==[(Q(),Q())]*(d+1)
   else:
    assert state==[((3*x+a)/4,(3*y+b)/4) for (x,y),(a,b) in zip(previous,targets)]
    updates+=1
   delta=[(x-a,y-b) for (x,y),(a,b) in zip(state,targets)]
   J=sum((x*x+y*y for x,y in delta),Q())/2
   R=sum(((abs(x)+abs(y))*u**n for n,(x,y) in enumerate(delta)),Q())
   assert f(t['objective'])==J and f(t['residual'])==R
   if previous is not None:assert J==previous_J*Q(9,16) and R==previous_R*Q(3,4)
   if k<steps:assert R>threshold
   else:assert R<=threshold
   previous,previous_J,previous_R=state,J,R;coefficient_states+=d+1
  assert pairs(r['coefficients'])==previous
  expected=dict(bs[d],optimization=previous_R);actual={k:f(z) for k,z in r['budget'].items()}
  assert actual==expected and len(actual)==5
  bound=sum(expected.values(),Q());assert f(r['compact_uniform_bound'])==bound<=eps
  models.append({'q':q,'degree':d,'steps':steps,'uniform_bound':float(bound),'minimum_base_degree':floor,'minimum_base_budget':float(totals[floor]),'actual_optimization':float(previous_R)})
 return {'directory':str(directory),'certificate_sha256':hashfile(directory/'readout-certificates.json'),'source_sha256':data['source_sha256'],'executed_updates_checked':updates,'coefficient_states_checked':coefficient_states,'models':models}
def diagnostics(directory,up):
 import mpmath as mp
 mp.mp.dps=110
 def number(x):return mp.mpf(x.numerator)/x.denominator
 def c(z):return mp.mpc(*map(number,z))
 families={3:(1,[0,1,-1]),4:(1,[0,1,0,-1]),5:(0,[0,1,-1,-1,1])}
 def target(q,s):
  a,chi=families[q];return(q/mp.pi)**((s+a)/2)*mp.gamma((s+a)/2)*mp.dirichlet(s,chi)
 data=json.loads((directory/'readout-certificates.json').read_text());models=[];coeffs=0;boundary=0
 for r in data['readouts']:
  q=r['q'];rows=sorted([s for s in up['samples'] if s['q']==q],key=lambda z:z['node_index']);labels=[c((f(s['center_real']),f(s['center_imag']))) for s in rows]
  for n,B in enumerate(map(box,r['target_rectangles'])):
   bn=sum(y*mp.exp(-2j*mp.pi*j*n/64) for j,y in enumerate(labels))/64
   for interval,z in zip(B,(bn.real,bn.imag)):assert number(Q(interval[0],S))<=z<=number(Q(interval[1],S))
   coeffs+=1
  a=[c(z) for z in pairs(r['coefficients'])];maximum=mp.mpf(0);bound=number(f(r['compact_uniform_bound']))
  for j in range(48):
   z=mp.mpf(7)/10*mp.exp(2j*mp.pi*j/48);s=mp.mpf(1)/2+z
   p=sum(an*(z/(mp.mpf(6)/5))**n for n,an in enumerate(a));error=abs(p-target(q,s))
   assert error<=bound;maximum=max(maximum,error);boundary+=1
  models.append({'q':q,'observed_48_boundary_max':float(maximum),'certificate':float(bound)})
 return {'directory':str(directory),'mpmath_version':mp.__version__,'dps':110,'Fourier_coefficients_contained':coeffs,'boundary_diagnostics':boundary,'models':models,'diagnostics_not_proof':True}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--directories',nargs='+',type=Path,required=True);ap.add_argument('--diagnostics',action='store_true');args=ap.parse_args()
 assert hashfile(UPSTREAM/'oracle-certificates.json')==FROZEN_SHA
 assert hashfile(UPSTREAM/'dyadic.py')==DYADIC_SHA and hashfile(UPSTREAM/'theta_oracle.py')==THETA_SHA
 up=json.loads((UPSTREAM/'oracle-certificates.json').read_text());assert len(up['samples'])==192
 bounds={}
 for q in GROWTH:
  rows=sorted([r for r in up['samples'] if r['q']==q],key=lambda r:r['node_index'])
  assert len(rows)==64 and all(type(r['q'])is int and r['node_index']==j and r['node_count']==64 for j,r in enumerate(rows))
  bounds[q]=independent_bounds(rows)
 report={'passed':True,'frozen_certificate_sha256':FROZEN_SHA,'independent_outward_DFT_rectangles':192,'all_degree_base_budgets_recomputed':192,'experiments':[verify(d,up,bounds) for d in args.directories],'arithmetic_imports':'Python standard library only; no author arithmetic imports','analytic_scope':'Reuses the independently reviewed fixed-label theta/Mellin and growth theorem; bounded finite certificate only','GRH_proved':False,'new_Lean_declarations':0}
 if args.diagnostics:report['diagnostics']=[diagnostics(d,up) for d in args.directories]
 p=ROOT/'outputs/checks/2026-11-05-adaptive-readout/review'/('independent-exact-'+str(time.time_ns())+'.json');p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'report':str(p),**report},indent=2))
if __name__=='__main__':main()
