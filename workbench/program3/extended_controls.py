"""Additional transparent controls for covering limits and learned coarse graining.

Designed after the first finite hierarchy experiment: no original model weights
or observed-sky choices are retuned. Report whether learning quantum gates adds
value beyond fitting a readout to the same initialized channel.
"""
import argparse,json,math
from pathlib import Path
import numpy as np
from .covers import lift_quiver,adjacency,lift_matrix
from .qrg import HierarchicalQNN,thermal_states,hierarchy_kraus,Z


def cycle_gaps():
 rows=[]
 for d in (1,2,3,5,8):
  c=lift_quiver(3,[[0,1],[1,2],[2,0]],[[0,1],[1,2],[2,0]],d,[0,0,1]);A=adjacency(3*d,c['arrows']);L=2*np.eye(3*d)-A-A.T;values=np.linalg.eigvalsh(L);gap=float(values[1]);exact=4*math.sin(math.pi/(3*d))**2
  U=lift_matrix(3,d);base=3*np.eye(3)-np.ones((3,3))
  residual=float(np.max(abs(L@U-U@base)))
  if abs(gap-exact)>1e-12 or residual>1e-12:raise ValueError('Cover spectral transport failure')
  rows.append(dict(degree=d,vertices=3*d,positive_gap=gap,exact_gap=exact,base_intertwining_error=residual))
 return rows


def nested_width():
 rng=np.random.default_rng(6721);x=rng.normal(size=(12,4));target=np.exp(-((x[:,None,:]-x[None,:,:])**2).sum(-1)/2);rows=[];tied=[]
 for seed in (3,5,7,11):
  g=np.random.default_rng(seed);w=g.normal(size=(4096,4));phase=g.uniform(0,2*math.pi,4096);features=math.sqrt(2)*np.cos(x@w.T+phase)
  fixed=np.outer(features[:,0],features[:,0]);fixed_error=float(np.max(abs(fixed-target)))
  for M in (16,64,256,1024,4096):
   k=features[:,:M]@features[:,:M].T/M
   rows.append(dict(seed=seed,width=M,max_error=float(np.max(abs(k-target))),minimum_eigenvalue=float(np.linalg.eigvalsh(k).min())))
   # Tying every feature to the same circuit leaves this kernel independent of M.
   tied.append(dict(seed=seed,width=M,max_error=fixed_error,kernel_varies_with_width=False))
 return dict(nested_independent=rows,fully_tied_counterexample=tied,scope='Nested prefixes of the same independent feature sequence. Fully shared parameters do not supply independent width; their rank-one kernel is unchanged by repetition.')


def learned_gate_baselines(qrg):
 rows=[];states=thermal_states();rho=np.stack([r['rho']for r in states]);target=np.array([r['target']for r in states]);train=np.array([r['split']=='train'for r in states]);test=np.array([r['split']=='test'for r in states])
 for run in qrg['thermal_runs']:
  initial=HierarchicalQNN(run['seed']).export();_,_,ks=hierarchy_kraus(initial['theta']);observable=sum(k.conj().T@Z@k for k in ks)
  f=np.einsum('bij,ji->b',rho,observable).real;design=np.column_stack([f,np.ones(len(f))]);coef=np.linalg.lstsq(design[train],target[train],rcond=None)[0];prediction=design[test]@coef
  frozen_mse=float(np.mean((prediction-target[test])**2));raw_mse=float(np.mean((f[test]-target[test])**2))
  rows.append(dict(seed=run['seed'],initial_channel_raw_test_mse=raw_mse,initial_channel_train_only_linear_readout_test_mse=frozen_mse,initial_channel_train_design_condition=float(np.linalg.cond(design[train])),fitted_readout=coef.tolist(),learned_channel_test_mse=run['test_mse'],constant_test_mse=run['constant_test_mse'],learned_gates_improve_over_frozen_readout=run['test_mse']<frozen_mse))
 return dict(rows=rows,post_initial_experiment_diagnostic=True,weights_retrained=False,selection='Frozen initialization determined by the same public seed. Only its scalar readout is fitted on training couplings; test couplings do not select it.',exact_target_observable_oracle_mse=0.,oracle_scope='The full input density matrix and declared ZZ observable determine the target exactly. This is an analytic oracle, not an equally compressed learned representation.')


def run(qrgfile,output):
 qrg=json.loads(qrgfile.read_text());result=dict(schema='grh.program3.extended-controls.v1',cover_spectrum=cycle_gaps(),width_controls=nested_width(),gate_learning_baselines=learned_gate_baselines(qrg))
 output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(result,indent=2)+'\n');return result

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--qrg',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=run(a.qrg,a.output);print(json.dumps({'cover_spectrum':r['cover_spectrum'],'gate_learning_baselines':r['gate_learning_baselines']},indent=2))
