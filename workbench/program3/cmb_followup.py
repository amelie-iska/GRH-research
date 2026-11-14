"""Explicitly exploratory null-sensitivity and frequency-residual checks.

These checks were designed after the first three product ranks were inspected.
They are not backdated as predeclared confirmations. Original results are never
replaced. A common ILC-derived reference and V-W residual test expose dependence
on the null representation; neither is a full instrument/foreground likelihood.
"""
import argparse,json,hashlib
from pathlib import Path
import numpy as np
from .cmb import prepare,catalogue,surrogates,moments,radial,angles,score,rank_p,SEED
from .qrg import frozen_predict


def reference(skies,cat,weights):
 g,r=moments(skies,cat);f=radial(skies,cat);q=frozen_predict(angles(f,np.array(weights['input_scale_microkelvin'])).reshape(-1,4),weights).reshape(len(skies),-1)
 return dict(g_mean=g.mean(0),g_std=np.maximum(g.std(0,ddof=1),1e-9),r_mean=r.mean(0),r_std=np.maximum(r.std(0,ddof=1),1e-9),q_mean=q.mean(0),q_std=np.maximum(q.std(0,ddof=1),1e-9))


def run(data,original,output):
 maps,alms,points,keep,meta=prepare(data);cat=catalogue(points,keep);prior=json.loads(original.read_text());weights=prior['model']
 training=surrogates(alms['ILC'],128,SEED+710);ref=reference(training,cat,weights);cal=surrogates(alms['ILC'],511,SEED+711);maxima=score(cal,cat,ref,weights).max(axis=(1,2));rows=[]
 for name,sky in maps.items():
  values=score(sky,cat,ref,weights)[0];winner=np.unravel_index(np.argmax(values),values.shape)
  rows.append(dict(product=name,common_reference_maximum=float(values[winner]),common_reference_surrogate_rank=rank_p(maxima,values[winner]),selected_method=int(winner[0]),selected_template=int(winner[1]),full_sky_rms_microkelvin=float(np.sqrt(np.mean(sky**2))),retained_sky_rms_microkelvin=float(np.sqrt(np.mean(sky[keep]**2)))))
 diff=maps['V']-maps['W'];diffalm=alms['V']-alms['W'];dref=reference(surrogates(diffalm,128,SEED+720),cat,weights);dmax=score(surrogates(diffalm,511,SEED+721),cat,dref,weights).max(axis=(1,2));dscore=score(diff,cat,dref,weights)[0];w=np.unravel_index(np.argmax(dscore),dscore.shape)
 cross={a+'_'+b:float(np.corrcoef(maps[a][keep],maps[b][keep])[0,1])for a,b in [('ILC','V'),('ILC','W'),('V','W')]}
 report=dict(schema='grh.cmb-exploratory-followup.v1',designed_after_initial_results=True,original_results_sha256=hashlib.sha256(original.read_bytes()).hexdigest(),frozen_model_unchanged=weights==prior['model'],common_ILC_reference=rows,shared_reference_scope='Same processed ILC coefficient magnitudes and independently randomized phases for all products. This changes the reference hypothesis and is a sensitivity diagnostic, not new independent evidence.',frequency_difference=dict(product='V-W',joint_maximum=float(dscore[w]),phase_surrogate_rank=rank_p(dmax,dscore[w]),selected_method=int(w[0]),selected_template=int(w[1]),rms_microkelvin=float(np.sqrt(np.mean(diff[keep]**2))),map_microkelvin=diff.tolist(),scope='Difference of processed thermodynamic maps sharing the same CMB sky. Different beams, instrument noise and foreground-cleaning residuals remain; not a pure foreground estimator.'),masked_cross_product_correlations=cross,scope='Exploratory robustness checks retained alongside the initial predeclared scan. Their ranks are not multiplied, pooled with the original family bound, or interpreted as CCC probabilities.')
 output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(report,indent=2)+'\n');return report

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--data',type=Path,required=True);p.add_argument('--original',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=run(a.data,a.original,a.output);print(json.dumps({k:v for k,v in r.items()if k!='frequency_difference'},indent=2));print('V-W rank',r['frequency_difference']['phase_surrogate_rank'])
