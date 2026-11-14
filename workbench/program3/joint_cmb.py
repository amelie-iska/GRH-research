"""Exploratory joint-product phase calibration preserving cross-product spectra.

A single random phase per harmonic mode acts on all three products, so complex
cross-products are retained. This avoids treating repeated views of one sky as
independent observations. It remains a conditional phase-group model, not a full
instrument likelihood, and is explicitly designed after the initial scan.
"""
import argparse,hashlib,json,math
from pathlib import Path
import numpy as np
from .cmb import prepare,catalogue,score,rank_p,wilson,SEED,LMAX,NSIDE
from .cmb_followup import reference


def joint_surrogates(alms,count,seed):
 import healpy as hp
 names=['ILC','V','W'];ell,m=hp.Alm.getlm(LMAX);rng=np.random.default_rng(seed);out={k:[]for k in names};max_error=0.
 for _ in range(count):
  phases=np.exp(2j*math.pi*rng.random(len(ell)));phases[m==0]=rng.choice([-1.,1.],int((m==0).sum()));phases[ell<2]=1
  changed={k:alms[k]*phases for k in names}
  for i,a in enumerate(names):
   for b in names[i:]:
    original=alms[a]*np.conj(alms[b]);error=float(np.max(abs(changed[a]*np.conj(changed[b])-original)/np.maximum(1,abs(original))))
    max_error=max(max_error,error)
  for k in names:out[k].append(hp.alm2map(changed[k],NSIDE,lmax=LMAX,pol=False))
 if max_error>2e-12:raise ValueError('Joint phase operation changed a harmonic cross-product')
 return {k:np.asarray(v)for k,v in out.items()},max_error


def run(data,original,output):
 maps,alms,points,keep,meta=prepare(data);cat=catalogue(points,keep);prior=json.loads(original.read_text());weights=prior['model'];ref_sky,e1=joint_surrogates(alms,128,SEED+810);refs={k:reference(ref_sky[k],cat,weights)for k in maps}
 calibration,e2=joint_surrogates(alms,511,SEED+811);values=np.stack([score(calibration[k],cat,refs[k],weights)for k in ['ILC','V','W']],axis=1);maxima=values.max(axis=(1,2,3))
 observed=np.stack([score(maps[k],cat,refs[k],weights)[0]for k in ['ILC','V','W']]);winner=np.unravel_index(observed.argmax(),observed.shape);maximum=float(observed[winner]);p=rank_p(maxima,maximum)
 validation,e3=joint_surrogates(alms,256,SEED+812);validation_max=np.stack([score(validation[k],cat,refs[k],weights)for k in ['ILC','V','W']],axis=1).max(axis=(1,2,3));reject=sum(rank_p(maxima,x)<=.05 for x in validation_max)
 result=dict(schema='grh.cmb.joint-phase-control.v1',designed_after_initial_scan=True,trained_weights_unchanged=True,original_results_sha256=hashlib.sha256(original.read_bytes()).hexdigest(),group_action='One common unit-modulus harmonic phase per l,m across ILC,V,W; real signs for m=0.',preserved='Every per-mode product a_lm^A conjugate(a_lm^B), including auto-power and relative cross-product phase.',max_relative_crossproduct_error=max(e1,e2,e3),search_size={'products':3,'methods':3,'templates':len(cat['labels'])},calibration_draws=511,joint_maximum=maximum,joint_rank=p,selected_product=['ILC','V','W'][winner[0]],selected_method=int(winner[1]),selected_template=int(winner[2]),template=cat['labels'][winner[2]],null_validation={'draws':256,'rejections':reject,'fraction':reject/256,'wilson_interval':wilson(reject,256)},calibration_maxima=maxima.tolist(),observed_scores=observed.tolist(),scope='Exploratory family-wide conditional phase-group rank, preserving observed product dependence at harmonic level. No independent-products assumption or extra Bonferroni factor is used. Group invariance of real noise/foreground processing remains unestablished; this is not a CCC posterior or a full-instrument detection significance.')
 output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k not in('observed_scores','calibration_maxima')},indent=2));return result

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--data',type=Path,required=True);p.add_argument('--original',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();run(a.data,a.original,a.output)
