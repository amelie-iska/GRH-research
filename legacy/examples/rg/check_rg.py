#!/usr/bin/env python3
"""Physics acceptance checks for actual finite RG, not a compression metric."""
import json
from pathlib import Path
import numpy as np
from scipy.special import logsumexp
from rg_math import (dessin, spins, fine_action, black_decimation, decimate, walsh,
                     transfer_step, transfer_logz, correlation_length, quantum_example)
ROOT=Path(__file__).resolve().parents[2]
def main():
 rng=np.random.default_rng(20261103);checks=[]
 for m in [3,5,9]:
  d=dessin(m);assert d['genus']==(m-1)//2 and len(d['physical_edges'])==2*m
  params=[.57,.83,-.24];v=fine_action(m,params);keep=list(range(2,m+2));vp=decimate(v,keep)
  assert np.max(abs(vp-black_decimation(m,params)))<1e-12
  c=walsh(vp);assert np.max(abs(walsh(c,normalized=False)-vp))<1e-11
  assert abs(logsumexp(v)-logsumexp(vp))<1e-12
  keep2=list(range(0,m,2));nested=decimate(vp,keep2);direct=decimate(v,[keep[q] for q in keep2])
  assert np.max(abs(nested-direct))<1e-12
  p=np.exp(v-logsumexp(v));pp=np.exp(vp-logsumexp(vp))
  err=abs(p@spins(m+2)[:,2]-pp@spins(m)[:,0]);assert err<1e-12
  noise=rng.uniform(-.08,.08,len(vp));eps=np.max(abs(noise))
  assert np.max(abs(decimate(vp+noise,keep2)-nested))<=eps+1e-12
  checks.append(dict(m=m,genus=d['genus'],constant=float(c[0]),higher_body_max=float(max(abs(c[k]) for k in range(1,2**m) if k.bit_count()>2)),retained_observable_error=float(err)))
 for K,h in [(0,0),(.4,0),(1.1,.35),(1.8,-.2)]:
  C=.17;z=transfer_logz(64,K,h,C);kp,hp,cp=transfer_step(K,h,C)
  assert abs(transfer_logz(32,kp,hp,cp)-z)<1e-11
  xi=correlation_length(K,h);xip=correlation_length(kp,hp)
  assert abs(2*xip-xi)<1e-10
  if h==0:assert abs(np.tanh(kp)-np.tanh(K)**2)<1e-12
 q=quantum_example(5,[.52,.66,.21],beta=.73,transverse=.47)
 assert max(q['checks'].values())<1e-9
 assert q['higher_body_norm']>1e-5
 qc=quantum_example(5,[.57,.83,-.24],beta=1,transverse=0)
 expected=-walsh(black_decimation(5,[.57,.83,-.24]))
 for term in qc['coefficients']:
  if 'X' in term['word'] or 'Y' in term['word']:assert abs(term['value'])<1e-10
  else:
   mask=int(''.join('1' if q=='Z' else '0' for q in term['word']),2)
   assert abs(term['value']-expected[mask])<1e-10
 assert max(abs(f['logZ']-q['logZ']) for f in q['flow'])<1e-10
 report={'passed':True,'seed':20261103,'classical':checks,'quantum':q['checks'],'scope':'finite partition/marginal RG identities; no universality or arithmetic proof'}
 out=ROOT/'outputs/checks/2026-11-03-actual-rg';out.mkdir(parents=True,exist_ok=True)
 (out/'physics-checks.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
