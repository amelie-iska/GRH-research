"""Family API/provenance negative controls and exact saved-record mutations."""
from pathlib import Path
from fractions import Fraction as F
from unittest.mock import patch
import sys,json,time,hashlib,copy
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'examples/analytic_oracle'))
import adaptive_family as a
import adaptive_theta as theta
import precision
import check_family_exact as independent
OUT=ROOT/'outputs/checks/2026-11-05-adaptive-theta/review';checks=0;failures=[];stamp=str(time.time_ns());sources={n:Path(a.__file__).with_name(n).read_bytes() for n in ['precision.py','adaptive_theta.py','adaptive_family.py','adaptive_readout.py','theta_oracle.py','dyadic.py']}
def check(ok,label):
 global checks
 checks+=1
 if not ok:failures.append(label)
def rejects(fn,label):
 try:fn()
 except (ValueError,TypeError,AssertionError,FileExistsError,KeyError):check(True,label)
 else:check(False,label)
for bad in [True,False,0,1,1.0,1e-24,F(),F(-1)]:rejects(lambda:a.choices(bad),f'choices exact positive Fraction {bad!r}')
for q in [True,False,3.0,F(3),2,6]:rejects(lambda:a.family(q,F(1,10**24)),f'family supported integer {q!r}')
for degree in [-1,True,False,1.0,F(1)]:rejects(lambda:a.fourier([],degree,128),f'fourier degree {degree!r}')
for rows in [[],(),None,iter([]),{},'']:
 rejects(lambda:a.fourier(rows,0,128),'nonempty concrete Fourier rows')
for bits in [True,False,31,32.0,F(128)]:rejects(lambda:a.fourier([{}],0,bits),'Fourier precision type/range')
for eps in [F(1,10**6),F(1,10**24),F(1,10**32),F(17,10**31),F(1,10**1000)]:
 d,m,eta=a.choices(eps);check(type(d) is int and type(m) is int and 0<=d<m and m%8==0 and eta==eps*F(5,96),'choices exact geometry')
 check(10*F(7,24)**(d+1)/(1-F(7,24))<=eps/8,'choices Taylor allocation')
 check(10*F(1,2**m)/(1-F(1,2**m))/(1-F(7,24))<=eps/8,'choices alias allocation')
# Training source must execute its vector loop; reconstruct every emitted scale.
for targets in [[(F(),F()),(F(),F())],[(F(1,3),F(-2,7)),(F(5,11),F())]]:
 with patch.object(a.old_readout,'train',wraps=a.old_readout.train) as actual:
  trace=a.compressed_train(targets,F(1,10**12));check(actual.call_count==1,'called accepted exact update loop')
 state=[(F(),F()) for _ in targets]
 for k,row in enumerate(trace):
  check(row['iteration']==k and row['coefficient_state_sha256']==independent.hash_state(state),'compressed actual state hash')
  check(all((x,y)==(row['coefficient_scale']*tx,row['coefficient_scale']*ty) for (x,y),(tx,ty) in zip(state,targets)),'compressed state exact reconstruction')
  state=[((3*x+tx)/4,(3*y+ty)/4) for (x,y),(tx,ty) in zip(state,targets)]
for module in [a,theta,precision]:
 p=OUT/('family-entry-source-'+module.__name__+'-'+stamp)
 with patch.object(module,'SOURCE_AT_IMPORT',module.SOURCE_AT_IMPORT+b'\n# simulated stale module\n'):
  rejects(lambda:a.run(p,F(1,1000),(3,)),'stale imported source refuses')
 check(not p.exists(),'stale import refusal emits no output')
original=Path.read_bytes

def historical_change(path):
 b=original(path)
 return b+b'\n# simulated historical change\n' if path.name=='adaptive_readout.py' and path.parent==Path(a.__file__).parent else b
p=OUT/('family-historical-source-'+stamp)
with patch.object(Path,'read_bytes',historical_change):rejects(lambda:a.run(p,F(1,1000),(3,)),'historical pin mismatch refuses')
check(not p.exists(),'historical pin refusal emits no output')
counts={}
def during_change(path):
 b=original(path)
 if path.name=='precision.py' and path.parent==Path(a.__file__).parent:
  counts[str(path)]=counts.get(str(path),0)+1
  if counts[str(path)]>1:return b+b'\n# simulated drift\n'
 return b
p=OUT/('family-provenance-drift-'+stamp)
mock={'q':3,'degree':0,'sample_count':8,'steps':0,'compact_uniform_bound':F(1,1000000)}
with patch.object(Path,'read_bytes',during_change),patch.object(a,'family',return_value=mock):rejects(lambda:a.run(p,F(1,1000),(3,)),'during-run drift refuses')
check(not (p/'family-certificates.json').exists(),'drift emits no valid certificate')
failure=json.loads((p/'failure.json').read_text());check(failure['coefficient_certificate'] is False and failure['completed_families']==1,'drift metadata uncertified')
before={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in p.iterdir() if f.is_file()};rejects(lambda:a.run(p,F(1,1000),(3,)),'existing output refuses');check(before=={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in p.iterdir() if f.is_file()},'existing output bytewise preserved')
p=OUT/('family-controlled-failure-'+stamp)
with patch.object(a,'family',side_effect=RuntimeError('controlled review failure')):
 try:a.run(p,F(1,1000),(3,))
 except RuntimeError:check(True,'family failure propagated')
 else:check(False,'family failure propagated')
failure=json.loads((p/'failure.json').read_text());check(failure['coefficient_certificate'] is False and failure['completed_families']==0 and not (p/'family-certificates.json').exists(),'controlled failure remains uncertified')
# Force the otherwise conservative Fourier retry, retaining valid enclosures.
original_circle=theta.circle;original_fourier=a.fourier;observed=[];fourier_calls=0
def observed_circle(q,j,count,eta,initial_bits=None):
 row=original_circle(q,j,count,eta,initial_bits=initial_bits)
 width=sum((F(independent.integer(row['root_box'][name]['hi'])-independent.integer(row['root_box'][name]['lo']),1<<row['root_box'][name]['dyadic_bits']) for name in ['real','imag']),F())
 observed.append((j,initial_bits,width));return row
def widened_first_fourier(rows,degree,bits):
 global fourier_calls
 bounds=original_fourier(rows,degree,bits);fourier_calls+=1
 if fourier_calls==1:
  z=bounds[0];ctx=z.context;wide=a.Complex(precision.Real(ctx,z.re.lo-ctx.scale,z.re.hi+ctx.scale),z.im)
  return (wide,)+bounds[1:]
 return bounds
with patch.object(theta,'circle',observed_circle),patch.object(a,'fourier',widened_first_fourier):
 retried=a.family(3,F(1,10**6))
check(len(retried['sample_precision_attempts'])==2 and fourier_calls==2,'forced Fourier width causes a retry')
count=retried['sample_count'];check(len(observed)==2*count,'every actual node/sample regenerated on Fourier retry')
first=[v for v in observed[:count] if v[0]==1][0];second=[v for v in observed[count:] if v[0]==1][0]
check(second[1]>first[1] and second[2]<first[2],'regenerated actual root width strictly shrinks')
check(retried['compact_uniform_bound']<=F(1,10**6),'forced retry completes with a valid bound')
# Mutation controls against the independently reconstructed exact certificate.
experiment=Path(sys.argv[1]);data=independent.dec(json.loads((experiment/'family-certificates.json').read_text()));base=data['readouts'][0]
mutations=[
 ('degree',lambda r:r.__setitem__('degree',r['degree']+1)),
 ('basis',lambda r:r.__setitem__('coefficient_basis','(s-1/2)^n')),
 ('sample radius',lambda r:r['samples'][0].__setitem__('radius',F())),
 ('sample budget',lambda r:r['samples'][0]['budget'].__setitem__('n_tail',F())),
 ('sample conductor',lambda r:r['samples'][0].__setitem__('q',4)),
 ('Fourier rectangle',lambda r:r['target_rectangles'][0]['real'].__setitem__('lo',str(int(r['target_rectangles'][0]['real']['lo'])-1))),
 ('target',lambda r:r['targets'][0].__setitem__(0,r['targets'][0][0]+1)),
 ('state scale',lambda r:r['trace'][1].__setitem__('coefficient_scale',r['trace'][1]['coefficient_scale']+1)),
 ('objective',lambda r:r['trace'][1].__setitem__('objective',r['trace'][1]['objective']+1)),
 ('residual',lambda r:r['trace'][1].__setitem__('residual',r['trace'][1]['residual']+1)),
 ('state hash',lambda r:r['trace'][1].__setitem__('coefficient_state_sha256','0'*64)),
 ('step count',lambda r:r.__setitem__('steps',r['steps']-1)),
 ('last state',lambda r:r['trace'].pop()),
 ('coefficient',lambda r:r['coefficients'][0].__setitem__(0,r['coefficients'][0][0]+1)),
 ('readout budget',lambda r:r['budget'].__setitem__('oracle',F())),
 ('global bound',lambda r:r.__setitem__('compact_uniform_bound',F())),
]
for label,mutate in mutations:
 r=copy.deepcopy(base);mutate(r);rejects(lambda:independent.audit_family(r),'independent mutation rejection: '+label)
check(all(Path(a.__file__).with_name(n).read_bytes()==b for n,b in sources.items()),'all sources stable')
report={'passed':not failures,'checks':checks,'failures':failures,'source_sha256':{n:hashlib.sha256(b).hexdigest() for n,b in sources.items()},'mutation_controls':len(mutations),'source_changes_were_simulations_only':True,'production_files_written':False,'saved_experiment_for_mutations':str(experiment)}
out=OUT/('family-guards-'+stamp+'.json');out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'report':str(out),**report}))
if failures:raise SystemExit(1)
