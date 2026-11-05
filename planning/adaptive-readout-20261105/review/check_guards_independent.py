"""Adversarial runtime guards and verifier-negative controls.

Import author API only to probe guards. Exact expected floors and arithmetic
are independently rebuilt by check_adaptive_independent, never author math.
No production files are mutated; existing experiments are hashed unchanged.
"""
from fractions import Fraction as Q
from pathlib import Path
from copy import deepcopy
from unittest.mock import patch
import dataclasses, hashlib, importlib.util, json, sys, time
import check_adaptive_independent as independent
ROOT=independent.ROOT
sys.path.insert(0,str(ROOT/'examples/analytic_oracle'))
import adaptive_readout as api
OUT=ROOT/'outputs/checks/2026-11-05-adaptive-readout/review'
count=0
def reject(name,func,errors=(ValueError,TypeError)):
 global count
 try:func()
 except errors:count+=1;return
 raise AssertionError(name+' unexpectedly accepted')
def unchanged(directory):
 return {str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in directory.iterdir() if p.is_file()}
def setfrac(container,key,value):
 container[key]={'numerator':str(value.numerator),'denominator':str(value.denominator),'display':float(value)}
def main():
 global count
 up=api.load_frozen()
 assert independent.hashfile(independent.UPSTREAM/'oracle-certificates.json')==independent.FROZEN_SHA
 B={}
 for q in(3,4,5):
  rows=sorted([r for r in up['samples'] if r['q']==q],key=lambda r:r['node_index'])
  B[q]=independent.independent_bounds(rows)
 for q in(2,6,0,-3,3.0,True,False,Q(3),'3',None):
  reject('bad conductor '+repr(q),lambda q=q:api.certify(up,q,Q(1,10**15)))
 for eps in(0,-1,0.1,True,False,'1e-15',None,Q(),Q(-1)):
  reject('bad epsilon '+repr(eps),lambda eps=eps:api.certify(up,3,eps))
 for q in(3.0,True,Q(3)):
  reject('primed Fourier cache type',lambda q=q:api.fourier(q))
 for field in('radius','center_real','center_imag'):
  data=deepcopy(up);data['samples'][0][field]['numerator']=str(int(data['samples'][0][field]['numerator'])+1)
  reject('frozen supplied '+field,lambda data=data:api.certify(data,3,Q(1,10**15)))
 data=deepcopy(up);data['samples'][0]['root_box']['real']['lo']=str(int(data['samples'][0]['root_box']['real']['lo'])+1)
 reject('frozen supplied root endpoint',lambda:api.certify(data,3,Q(1,10**15)))
 tampered=OUT/('tampered-frozen-'+str(time.time_ns())+'.json')
 tampered.write_bytes((independent.UPSTREAM/'oracle-certificates.json').read_bytes()+b'\n')
 reject('frozen bytes hash',lambda:api.load_frozen(tampered))
 bounds,_=api.fourier(3)
 reject('cached tuple mutation',lambda:bounds.__setitem__(0,bounds[1]),(AttributeError,TypeError))
 reject('cached rectangle mutation',lambda:setattr(bounds[0].re,'lo',0),(dataclasses.FrozenInstanceError,))
 for targets in([],[(1,Q(2))],[(Q(1),2.0)],[(Q(1),)],[(Q(1),Q(2),Q(3))],[None],None):
  reject('malformed targets',lambda targets=targets:api.train(targets,Q(1,100)))
 for residual in(Q(),Q(-1),0.1,True,None):
  reject('bad training slack',lambda residual=residual:api.train([(Q(1),Q(2))],residual))
 # A supported iterable must train its actual targets; rejection is also safe.
 try:
  trace=api.train(((Q(1),Q(2)) for _ in range(1)),Q(1,100))
 except (TypeError,ValueError):pass
 else:
  assert trace[0]['coefficients']==[(Q(),Q())]
  assert trace[0]['objective']==Q(5,2)
  assert trace[1]['coefficients']==[(Q(1,4),Q(1,2))]
 count+=1
 reject('empty generator targets',lambda:api.train((x for x in []),Q(1,100)))
 ordinary=api.train([(Q(1),Q(2))],Q(1,100))
 assert ordinary[0]['objective']==Q(5,2) and ordinary[1]['objective']==Q(45,32)
 assert api.encode(Q(10**1000))['display'] is None
 positive=[]
 for q in(3,4,5):
  b,eta=B[q];bases=[sum(independent.base(b,eta,q,d).values(),Q()) for d in range(64)]
  floor=min(bases)
  for eps in(floor,floor-Q(1,10**80),Q(1,10**18)):
   try:api.certify(up,q,eps)
   except api.ToleranceNotCertified as e:assert e.floor==floor;count+=1
   else:raise AssertionError('floor boundary accepted')
  for eps in(floor+Q(1,10**80),Q(34,10**17),bases[0]):
   r=api.certify(up,q,eps);assert r['degree']==next(d for d,z in enumerate(bases) if z<eps)
   assert sum(r['budget'].values(),Q())==r['compact_uniform_bound']<=eps
   assert r['trace'][-1]['residual']<=eps-bases[r['degree']]
   if len(r['trace'])>1:assert r['trace'][-2]['residual']>eps-bases[r['degree']]
   positive.append({'q':q,'epsilon':str(eps),'degree':r['degree'],'steps':r['steps'],'bound':float(r['compact_uniform_bound'])})
  assert r['degree']>0
 experiment=ROOT/'outputs/experiments/2026-11-05-adaptive-readout-1e-15-v3'
 before=unchanged(experiment);reject('existing output',lambda:api.run(experiment,Q(1,10**15)),(FileExistsError,));assert unchanged(experiment)==before
 reject('non-Path output',lambda:api.run(str(OUT/'unsafe-string'),Q(1,10**15)),(TypeError,))
 refusal=OUT/('refusal-no-artifacts-'+str(time.time_ns()))
 reject('too-small run',lambda:api.run(refusal,Q(1,10**18)),(api.ToleranceNotCertified,));assert not refusal.exists()
 # Simulate source changing between entry snapshot and pre-emission guard.
 source_path=ROOT/'examples/analytic_oracle/adaptive_readout.py';original=Path.read_bytes;calls=0
 def changing(path):
  nonlocal calls
  value=original(path)
  if path==source_path:
   calls+=1
   if calls>=2:return value+b'\n'
  return value
 guarded=OUT/('changed-source-no-artifacts-'+str(time.time_ns()))
 with patch.object(Path,'read_bytes',changing):
  reject('source drift',lambda:api.run(guarded,Q(1,10**12)),(AssertionError,))
 assert not guarded.exists()
 # Our independent verifier must catch semantically altered output fields.
 record=json.loads((experiment/'readout-certificates.json').read_text());negative=[]
 mutations={
  'objective normalization':lambda x:setfrac(x['readouts'][0]['trace'][0],'objective',2*independent.f(x['readouts'][0]['trace'][0]['objective'])),
  'iterate coefficient':lambda x:setfrac(x['readouts'][0]['trace'][1]['coefficients'][0],0,Q(1)),
  'total bound':lambda x:setfrac(x['readouts'][0],'compact_uniform_bound',Q()),
  'budget term':lambda x:setfrac(x['readouts'][0]['budget'],'oracle',Q()),
  'reported degree':lambda x:x['readouts'][0].__setitem__('degree',28),
  'reported stop count':lambda x:x['readouts'][0].__setitem__('steps',1),
  'raw coefficient basis':lambda x:x['readouts'][0].__setitem__('coefficient_basis','(s-1/2)^n'),
  'DFT rectangle':lambda x:x['readouts'][0]['target_rectangles'][0]['real'].__setitem__('lo','0'),
  'reported floor':lambda x:setfrac(x['readouts'][0],'minimum_base_budget',Q()),
  'base degree scan':lambda x:setfrac(x['readouts'][0]['all_degree_base_budgets'],0,Q()),
  'source hash':lambda x:x['source_sha256'].__setitem__('adaptive_readout.py','0'*64),
  'input hash':lambda x:x.__setitem__('input_certificate_sha256','0'*64)}
 for name,mutate in mutations.items():
  altered=deepcopy(record);mutate(altered)
  reject('verifier negative '+name,lambda altered=altered:independent.verify(experiment,up,B,data=altered),(AssertionError,ValueError,StopIteration))
  negative.append(name)
 assert unchanged(experiment)==before
 report={'passed':True,'runtime_and_verifier_negative_controls':count,'positive_strict_margin_runs':positive,'verifier_tampering_detected':negative,'final_source_sha256':independent.hashfile(source_path),'existing_output_hashes_unchanged':True,'simulated_source_drift_refused':True,'tampered_input_retained':str(tampered),'GRH_proved':False,'new_Lean_declarations':0}
 p=OUT/('independent-guards-'+str(time.time_ns())+'.json');p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'report':str(p),**report},indent=2))
if __name__=='__main__':main()
