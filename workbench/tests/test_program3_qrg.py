import sys,unittest
from pathlib import Path
import numpy as np
import torch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from program3.qrg import HierarchicalQNN,hierarchy_kraus,channel_audit,frozen_predict,thermal_states,stage_unitary_np,DT

class HierarchicalChannels(unittest.TestCase):
 def test_unitarity(self):
  for n in (2,4):
   u=stage_unitary_np([.2,.4,-.7],n);np.testing.assert_allclose(u.conj().T@u,np.eye(1<<n),atol=1e-14)
 def test_complete_hierarchy(self):self.assertLess(channel_audit([.1,.2,.3,.4,.5,.6])['completeness_error'],1e-13)
 def test_frozen_independent_prediction(self):
  model=HierarchicalQNN(17);x=np.random.default_rng(1).normal(size=(40,4));pred=model(torch.tensor(x,dtype=DT)).detach().numpy();np.testing.assert_allclose(pred,frozen_predict(x,model.export()),atol=1e-12)
 def test_autograd(self):
  model=HierarchicalQNN(3);x=torch.tensor([[.2,.4,.6,.8]],dtype=DT);model(x).sum().backward();analytic=model.theta.grad.detach().numpy().copy();original=model.theta.detach().clone();h=1e-6
  for i in range(6):
   with torch.no_grad():model.theta.copy_(original);model.theta[i]+=h
   plus=float(model(x).detach())
   with torch.no_grad():model.theta.copy_(original);model.theta[i]-=h
   minus=float(model(x).detach());self.assertAlmostEqual((plus-minus)/(2*h),analytic[i],places=7)
 def test_thermal_states_and_split(self):
  rows=thermal_states();self.assertEqual(len(rows),33)
  sets={s:{r['g']for r in rows if r['split']==s}for s in ['train','validation','test']}
  self.assertFalse(sets['train']&sets['test']);self.assertFalse(sets['validation']&sets['test'])
  for r in rows:self.assertAlmostEqual(np.trace(r['rho']).real,1);self.assertGreater(np.linalg.eigvalsh(r['rho']).min(),0)
 def test_width_kernel_psd(self):
  x=np.random.default_rng(7).normal(size=(12,4));k=np.exp(-((x[:,None,:]-x[None,:,:])**2).sum(-1)/2);self.assertGreater(np.linalg.eigvalsh(k).min(),-1e-13)
 def test_invalid_parameter(self):
  with self.assertRaises(ValueError):hierarchy_kraus([float('nan')]*6)

if __name__=='__main__':unittest.main(verbosity=2)
