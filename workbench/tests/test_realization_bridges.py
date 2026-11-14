import json,sys,unittest,itertools
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'workbench'))
from realization_bridges import order_multiply,order_matrix,matrix_multiply,heat_transition,quantum_diffusion,torus_spectrum,project_ground,report
from quantum_surface import MODEL,cpu_state,DEFAULT

class RealizationBridges(unittest.TestCase):
 def test_order_closure_and_realization(self):
  samples=list(itertools.product((-1,0,1),repeat=4))
  for p in [2,3]:
   for x,y in zip(samples,reversed(samples)):
    self.assertEqual(order_matrix(order_multiply(x,y,p),p),matrix_multiply(order_matrix(x,p),order_matrix(y,p)))
    self.assertTrue(all(v.denominator==1 for v in order_multiply(x,y,p)))
 def test_generic_matrix_units(self):
  self.assertEqual(order_matrix((0,0,Q(1,3),0),3),[[0,0],[1,0]])
 def test_gentle_special_fiber(self):
  u=(0,1,0,0);v=(0,0,1,0)
  self.assertEqual(order_multiply(u,u,0),(0,0,0,0));self.assertEqual(order_multiply(v,v,0),(0,0,0,0));self.assertEqual(order_multiply(u,v,0),(0,0,0,0));self.assertEqual(order_multiply(v,u,0),(0,0,0,0))
 def test_bistochastic_exact(self):
  for r in [Q(0),Q(1,8),Q(1,4)]:
   p=heat_transition(3,r);self.assertTrue(all(sum(row)==1 for row in p));self.assertTrue(all(sum(p[i][j]for i in range(9))==1 for j in range(9)))
 def test_channel_kraus_not_unitary(self):
  p=heat_transition();v=np.ones(9)/3;rho=np.outer(v,v);out,comp=quantum_diffusion(p,rho)
  np.testing.assert_allclose(comp,np.eye(9),atol=1e-14);self.assertAlmostEqual(np.trace(out),1);self.assertLess(np.trace(out@out),1)
 def test_spectrum_and_ground(self):
  model=json.loads(MODEL.read_text());r=torus_spectrum(model)
  self.assertEqual((r['gap'],r['ground_degeneracy'],r['dimension']),('4',4,262144))
  self.assertEqual(torus_spectrum(model,Q(3,2),Q(1,3))['gap'],'4/3')
  base=cpu_state(model);np.testing.assert_allclose(project_ground(model,base),base,atol=1e-13)
 def test_energy_certificate(self):
  r=report()['energy_certificate'];self.assertGreaterEqual(r['slack'],-1e-12);self.assertTrue(0<=r['ground_space_probability']<=1)
 def test_bad_domains(self):
  with self.assertRaises(ValueError):heat_transition(3,Q(1,3))
  with self.assertRaises(ValueError):quantum_diffusion([[1,0],[0,-1]],np.eye(2)/2)

if __name__=='__main__':unittest.main(verbosity=2)
