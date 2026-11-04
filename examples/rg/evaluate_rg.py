#!/usr/bin/env python3
"""Additional diagnostics; never changes trained parameters or source data."""
from pathlib import Path
import json
import numpy as np
from train_rg import features,augmented,ridge,classical_features
from rg_math import walsh,quantum_example,decimate,fine_action
ROOT=Path(__file__).resolve().parents[2];out=ROOT/'outputs/experiments/actual-rg'
def main():
 m=json.loads((out/'training.json').read_text());d=json.loads((out/'dataset.json').read_text())
 x=np.array(d['parameters']);y=np.array(d['targets']);tr=d['train'];te=d['test']
 pred=augmented(features(np.array(m['theta']),x))@np.array(m['head'])*m['target_scale']+m['target_mean']
 base=ridge(classical_features(x[tr]),(y[tr]-m['target_mean'])/m['target_scale'])
 bp=classical_features(x)@base*m['target_scale']+m['target_mean']
 mask=np.array([i.bit_count()>2 for i in range(32)])
 def interaction_metrics(p):
  a=np.array([walsh(v) for v in p[te]]);b=np.array([walsh(v) for v in y[te]])
  return dict(constant_MAE=float(np.mean(abs(a[:,0]-b[:,0]))),constant_RMSE=float(np.sqrt(np.mean((a[:,0]-b[:,0])**2))),higher_body_coefficient_RMSE=float(np.sqrt(np.mean((a[:,mask]-b[:,mask])**2))),target_higher_body_norm_mean=float(np.mean(np.linalg.norm(b[:,mask],axis=1))))
 beta=.73;params=[.57,.83,-.24];q=quantum_example(5,params,beta=beta,transverse=0)
 expected=-walsh(decimate(beta*fine_action(5,params),list(range(2,7))))/beta
 errs=[]
 for t in q['coefficients']:
  target=0 if 'X'in t['word']or'Y'in t['word'] else expected[int(''.join('1'if s=='Z'else'0' for s in t['word']),2)]
  errs.append(abs(t['value']-target))
 assert max(errs)<1e-10
 sensitivities=[]
 for j in range(12):
  delta=np.zeros(12);delta[j]=1e-5
  sensitivities.append(float(np.max(abs(features(np.array(m['theta'])+delta,x[te])-features(np.array(m['theta'])-delta,x[te])))/2e-5))
 result=dict(circuit_feature_sensitivity=sensitivities,nominal_circuit_angles=12,structurally_inactive_final_RZ_indices=[7,9,11],quantum_feature_model=interaction_metrics(pred),classical_baseline=interaction_metrics(bp),general_beta_classical_limit_pauli_error=max(errs),scope='additional evaluation only; all trained parameters/data preserved')
 (out/'evaluation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
