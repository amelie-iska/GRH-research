import unittest,sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from program3 import qrg,quantum_reference as independent

class DeferredDiscard(unittest.TestCase):
 def test_stage_and_deferred_channels(self):
  rng=np.random.default_rng(42)
  for _ in range(12):
   theta=rng.normal(size=6);psi=rng.normal(size=16)+1j*rng.normal(size=16);psi/=np.linalg.norm(psi);rho=np.outer(psi,psi.conj())
   a=qrg.hierarchy_kraus(theta)[2];b=independent.hierarchy_kraus(theta)[2]
   np.testing.assert_allclose(qrg.channel(rho,a),independent.channel(rho,b),atol=2e-14)
 def test_normalization(self):
  ks=independent.hierarchy_kraus([.3]*6)[2];np.testing.assert_allclose(sum(k.conj().T@k for k in ks),np.eye(16),atol=1e-14)

if __name__=='__main__':unittest.main(verbosity=2)
