"""Audit a saved sample experiment; mpmath values are secondary diagnostics."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib,time
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'examples/analytic_oracle'))
import adaptive_theta as a
import mpmath as mp
mp.mp.dps=130
OUT=ROOT/'outputs/checks/2026-11-05-adaptive-theta/review'
experiment=Path(sys.argv[1]);data=json.loads((experiment/'sample-certificates.json').read_text());checks=0;rows=[]
def integer(s):
 sign=-1 if s.startswith('-') else 1;v=0
 for c in s.lstrip('+-'):v=v*10+int(c)
 return sign*v
def dec(x):
 if isinstance(x,dict) and 'numerator' in x and 'denominator' in x:return F(integer(x['numerator']),integer(x['denominator']))
 if isinstance(x,dict):return {k:dec(v) for k,v in x.items()}
 if isinstance(x,list):return [dec(v) for v in x]
 return x
def m(v):return mp.mpf(v.numerator)/v.denominator
def contained(b,x):return mp.mpf(b['lo'])/(1<<b['dyadic_bits'])<=x<=mp.mpf(b['hi'])/(1<<b['dyadic_bits'])
for name,digest in data['source_sha256'].items():assert hashlib.sha256((experiment/name).read_bytes()).hexdigest()==digest;checks+=1
assert data['sample_oracle_validated'] is True and data['readout_certificate'] is False and data['GRH_proved'] is False and data['new_Lean_declarations']==0;checks+=1
family_indices={}
for r in dec(data['samples']):
 q=r['q'];eta=r['requested_sample_error'];bits=r['bits'];B=r['budget_rounding_bits'];unit=F(1,1<<B);box=r['quadrature_sum_box'];plan=a.parameters(q,eta)
 assert (r['N'],r['J'],r['K'],r['active_pairs'],r['discarded_pairs'])==(plan.N,plan.J,plan.K,len(plan.active),plan.discarded_pairs);checks+=1
 rawradius=sum((F(integer(box[n]['hi'])-integer(box[n]['lo']),2*(1<<bits)) for n in ['real','imag']),F())
 assert rawradius==r['raw_interval_radius']<=eta/4;checks+=1
 raw={'n_tail':plan.n_tail,'time_tail':plan.time_tail,'quadrature':plan.quadrature,'discard':plan.discard,'interval_arithmetic':rawradius}
 for name,value in raw.items():
  rounded=F(-(-value.numerator*(1<<B)//value.denominator),1<<B)
  assert r['budget'][name]==rounded and 0<=rounded-value<unit;checks+=1
 assert 5*unit<=eta/8 and r['radius']==sum(r['budget'].values(),F())<=7*eta/8;checks+=1
 for component,name in [('real','center_real'),('imag','center_imag')]:assert r[name]==F(integer(box[component]['lo'])+integer(box[component]['hi']),2*(1<<bits));checks+=1
 j=r['node_index'];count=r['node_count'];root=mp.exp(2*mp.pi*mp.j*j/count);s=mp.mpf('0.5')+mp.mpf(6)/5*root
 assert contained(r['node_box']['real'],s.real) and contained(r['node_box']['imag'],s.imag) and contained(r['root_box']['real'],root.real) and contained(r['root_box']['imag'],root.imag);checks+=1
 parity,chi=a.FAMILIES[q];truth=mp.power(q/mp.pi,(s+parity)/2)*mp.gamma((s+parity)/2)*mp.dirichlet(s,chi)
 error=abs(truth-mp.mpc(m(r['center_real']),m(r['center_imag'])));assert error<=m(r['radius']);checks+=1
 assert count==data['circle_node_count'];family_indices.setdefault(q,[]).append(j);checks+=1
 rows.append({'q':q,'j':j,'m':count,'requested_sample_error':str(eta),'budget_rounding_bits':B,'bits':bits,'certified_radius':str(r['radius']),'diagnostic_error_to_radius_ratio':str(error/m(r['radius']))})
for q,indices in family_indices.items():
 assert indices==list(range(0,data['circle_node_count'],data['stride'])) and len(indices)==data['evaluated_sample_count_per_family'];checks+=1
 if data['complete_circle']:assert indices==list(range(data['circle_node_count']));checks+=1
assert data['complete_circle']==(data['stride']==1);checks+=1
report={'passed':True,'checks':checks,'experiment':str(experiment),'certificate_sha256':hashlib.sha256((experiment/'sample-certificates.json').read_bytes()).hexdigest(),'source_sha256':data['source_sha256'],'complete_circle':data['complete_circle'],'rows':rows,'mpmath_version':mp.__version__,'mpmath_digits':mp.mp.dps,'mpmath_is_secondary_diagnostic_not_proof':True,'readout_reviewed':False}
p=OUT/('saved-samples-'+experiment.name+'-'+str(time.time_ns())+'.json');p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'report':str(p),'passed':True,'checks':checks,'samples':len(rows),'source_sha256':data['source_sha256']}))
