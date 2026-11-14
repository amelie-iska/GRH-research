import sys,math,unittest
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from half_density import field,jacobian,flow,cayley,COEFFICIENTS,LAMBDAS,FORCING,VISCOSITY

class HalfDensity(unittest.TestCase):
 def test_energy_cancellation(self):
  rng=np.random.default_rng(4)
  for u in rng.normal(size=(100,3)):
   self.assertAlmostEqual(np.dot(u,field(u)),-VISCOSITY*np.dot(LAMBDAS*u,u)+np.dot(FORCING,u),places=12)
 def test_jacobian_independent_difference(self):
  u=np.array([.3,-.7,1.2]);h=1e-6
  fd=np.column_stack([(field(u+h*np.eye(3)[j])-field(u-h*np.eye(3)[j]))/(2*h)for j in range(3)])
  np.testing.assert_allclose(jacobian(u),fd,atol=2e-10)
 def test_phase_divergence(self):self.assertAlmostEqual(np.trace(jacobian([.2,.6,-.9])),-VISCOSITY*sum(LAMBDAS))
 def test_flow_inverse_and_jacobian(self):
  u=np.array([.3,-.7,1.2]);v,J,_=flow(u,.5);w,_,_=flow(v,-.5)
  np.testing.assert_allclose(w,u,atol=1e-10);self.assertAlmostEqual(np.linalg.det(J),math.exp(-VISCOSITY*sum(LAMBDAS)*.5),places=10)
 def test_cayley_unitarity(self):
  for n in [8,16,32]:
   _,A,U=cayley(n,.3);np.testing.assert_allclose(A.T,-A,atol=0);np.testing.assert_allclose(U.T@U,np.eye(n),atol=1e-14)
 def test_cayley_reverse(self):
  _,_,U=cayley(16,.2);_,_,V=cayley(16,-.2);np.testing.assert_allclose(U@V,np.eye(16),atol=1e-14)
 def test_domain(self):
  with self.assertRaises(ValueError):flow([0,0,float('nan')],1)
  with self.assertRaises(ValueError):cayley(10000)

if __name__=='__main__':unittest.main(verbosity=2)
