"""Trained mass-preserving graph heat operator with a cover-compatible CPTP lift.

Shared time-conditioned coefficients select a convex lazy-walk polynomial.
Exact heat and the analytic Poisson mixture remain stronger explicit baselines.
"""
import argparse,hashlib,json
from pathlib import Path
import numpy as np
import torch
from scipy.stats import poisson
torch.set_num_threads(2)
DT=torch.float64
K=24
class HeatWeights(torch.nn.Module):
 def __init__(self,seed):
  super().__init__();torch.manual_seed(seed);self.net=torch.nn.Sequential(torch.nn.Linear(1,16),torch.nn.Tanh(),torch.nn.Linear(16,K+1)).double()
 def forward(self,t):
  tail=torch.softmax(self.net(t[:,None]),dim=1);atom=torch.exp(-4*t)[:,None];e0=torch.zeros_like(tail);e0[:,0]=1;return atom*e0+(1-atom)*tail

def walk(n):
 shift=np.roll(np.eye(n),1,axis=0);return .5*np.eye(n)+.25*(shift+shift.T)
def polynomial(P,w):
 power=np.eye(len(P));out=np.zeros_like(P)
 for coefficient in w:out+=coefficient*power;power=power@P
 return out
def quantum_channel(rho,w):
 current=rho.copy();out=np.zeros_like(rho)
 for coefficient in w:
  out+=coefficient*current;current=.5*current+.25*(np.roll(np.roll(current,1,0),1,1)+np.roll(np.roll(current,-1,0),-1,1))
 return out
def analytic_weights(t):
 w=poisson.pmf(np.arange(K+1),4*t);w[0]+=poisson.sf(K,4*t);return w

def run(output):
 rows=[];models=[];train_t=np.linspace(0,2,17);val_t=(train_t[:-1]+train_t[1:])/2;eig=np.concatenate([np.linalg.eigvalsh(walk(n))for n in(3,6)]);powers=torch.tensor(eig[:,None]**np.arange(K+1),dtype=DT);tx=torch.tensor(train_t,dtype=DT);vx=torch.tensor(val_t,dtype=DT);target=torch.exp(-4*tx[:,None]*(1-torch.tensor(eig)[None,:]));vt=torch.exp(-4*vx[:,None]*(1-torch.tensor(eig)[None,:]))
 for seed in(17,29,47):
  model=HeatWeights(seed);opt=torch.optim.Adam(model.parameters(),lr=.025);best=None;history=[]
  for step in range(501):
   pred=model(tx)@powers.T;loss=((pred-target)**2).mean()
   if step%25==0:
    with torch.no_grad():vl=float(((model(vx)@powers.T-vt)**2).mean())
    history.append({'step':step,'train_spectral_mse':float(loss.detach()),'validation_spectral_mse':vl})
    if best is None or vl<best[0]:best=(vl,step,{k:v.detach().clone()for k,v in model.state_dict().items()})
   if step<500:opt.zero_grad();loss.backward();opt.step()
  model.load_state_dict(best[2]);model.eval()
  for n in(9,15,24):
   P=walk(n);evals,V=np.linalg.eigh(P)
   for t in(.03,.17,.41,.73,1.13,1.57,1.91):
    with torch.no_grad():w=model(torch.tensor([t],dtype=DT))[0].numpy()
    predicted=polynomial(P,w);exact=(V*np.exp(-4*t*(1-evals)))@V.T;analytic=polynomial(P,analytic_weights(t));error=float(np.linalg.norm(predicted-exact,2));baseP=walk(3);U=np.tile(np.eye(3),(n//3,1));inter=float(np.max(abs(predicted@U-U@polynomial(baseP,w))));rng=np.random.default_rng(n*100+seed);a=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));rho=a@a.conj().T;rho/=np.trace(rho);coarse=quantum_channel(rho,w)
    row={'seed':seed,'nodes':n,'time':t,'operator_norm_error':error,'analytic_poisson_error':float(np.linalg.norm(analytic-exact,2)),'analytic_tail_bound':float(2*poisson.sf(K,4*t)),'cover_intertwining_error':inter,'column_sum_error':float(np.max(abs(predicted.sum(0)-1))),'minimum_transition':float(predicted.min()),'channel_trace_error':float(abs(np.trace(coarse)-1)),'channel_min_eigenvalue':float(np.linalg.eigvalsh(coarse).min()),'diagonal_channel_match':float(np.max(abs(np.diag(coarse).real-predicted@np.diag(rho).real)))}
    if inter>1e-12 or row['column_sum_error']>1e-12 or row['channel_min_eigenvalue']< -1e-12 or row['diagonal_channel_match']>1e-12:raise AssertionError('Structural contract failed')
    rows.append(row)
  models.append({'seed':seed,'selected_step':best[1],'history':history,'weights':{k:v.tolist()for k,v in model.state_dict().items()},'parameter_count':sum(p.numel()for p in model.parameters())})
 result={'schema':'grh.cover-compatible-neural-operator.v1','polynomial_degree':K,'trained_sizes':[3,6],'heldout_sizes':[9,15,24],'training_times':train_t.tolist(),'validation_times':val_t.tolist(),'test_times':[.03,.17,.41,.73,1.13,1.57,1.91],'models':models,'results':rows,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Actually trained finite time-conditioned heat operator. Shared coefficients preserve stochasticity, CPTP lift and covering intertwining. Error measured against exact heat and same-degree analytic Poisson baseline; not a quantum advantage or continuum interacting-field solution.'};output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(result,indent=2)+'\n');return result

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=run(a.output);print(json.dumps({'cases':len(r['results']),'max_learned_error':max(x['operator_norm_error']for x in r['results']),'max_analytic_error':max(x['analytic_poisson_error']for x in r['results']),'max_cover_residual':max(x['cover_intertwining_error']for x in r['results'])},indent=2))
