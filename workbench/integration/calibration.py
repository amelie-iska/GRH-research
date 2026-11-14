"""Exploratory higher-resolution joint-phase calibration and finite-MC intervals.

Frozen original observations/templates/weights; refreshed reference statistics.
Batched draws; this is not an independent physical WMAP likelihood.
"""
import argparse,hashlib,json
from pathlib import Path
import numpy as np
from scipy.stats import beta
from workbench.program3.cmb import prepare,catalogue,score
from workbench.program3.cmb_followup import reference
from workbench.program3.joint_cmb import joint_surrogates
CALIBRATION=4095
VALIDATION=1024
SEED=2026111404

def interval(k,n,alpha=.05):
 if not 0<=k<=n or n<=0:raise ValueError('Invalid binomial counts')
 return[0. if k==0 else float(beta.ppf(alpha/2,k,n-k+1)),1. if k==n else float(beta.ppf(1-alpha/2,k+1,n-k))]
def maxima(alms,cat,refs,weights,count,seed):
 parts=[];errors=[];batches=[]
 for start in range(0,count,128):
  size=min(128,count-start);draws,error=joint_surrogates(alms,size,seed+start);values=np.stack([score(draws[k],cat,refs[k],weights)for k in('ILC','V','W')],axis=1);parts.append(values.max(axis=(1,2,3)));errors.append(error);batches.append({'seed':seed+start,'draws':size})
 return np.concatenate(parts),max(errors),batches

def run(data,original,output):
 maps,alms,points,keep,metadata=prepare(data);cat=catalogue(points,keep);prior=json.loads(original.read_text());weights=prior['model'];refskies,error=joint_surrogates(alms,512,SEED);refs={k:reference(refskies[k],cat,weights)for k in maps}
 observed=np.stack([score(maps[k],cat,refs[k],weights)[0]for k in('ILC','V','W')]);maximum=float(observed.max());winner=np.unravel_index(observed.argmax(),observed.shape);null,ce,cb=maxima(alms,cat,refs,weights,CALIBRATION,SEED+10000);validation,ve,vb=maxima(alms,cat,refs,weights,VALIDATION,SEED+100000);k=int((null>=maximum).sum());p=(1+k)/(CALIBRATION+1);pv=(1+np.sum(null[:,None]>=validation[None,:],axis=0))/(CALIBRATION+1);rejections=int((pv<=.05).sum())
 r={'schema':'grh.integrated-calibration.v1','exploratory_after_original':True,'original_result_sha256':hashlib.sha256(original.read_bytes()).hexdigest(),'trained_weights_sha256':hashlib.sha256(json.dumps(weights,sort_keys=True).encode()).hexdigest(),'model_unchanged':True,'search_size':{'products':3,'methods':3,'templates':len(cat['labels'])},'reference_draws':512,'calibration_draws':CALIBRATION,'validation_draws':VALIDATION,'observed_maximum':maximum,'exceedances':k,'rank_p':p,'rank_resolution':1/(CALIBRATION+1),'conditional_tail_binomial_interval_95':interval(k,CALIBRATION),'selected_product':('ILC','V','W')[winner[0]],'selected_method':int(winner[1]),'selected_template':int(winner[2]),'null_validation':{'rejections':rejections,'draws':VALIDATION,'fraction':rejections/VALIDATION,'interval_95':interval(rejections,VALIDATION)},'max_crossproduct_error':max(error,ce,ve),'calibration_batches':cb,'validation_batches':vb,'null_maxima':null.tolist(),'scope':'Precision refinement of the conditional joint-phase null with refreshed normalization. Binomial intervals quantify simulation uncertainty conditional on this null, observed score and reference, not foreground/instrument misspecification or a probability for CCC.','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()};output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items()if k not in('null_maxima','calibration_batches','validation_batches')},indent=2));return r

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--data',type=Path,required=True);p.add_argument('--original',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();run(a.data,a.original,a.output)
