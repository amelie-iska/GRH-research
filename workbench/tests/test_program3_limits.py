import unittest,sys,math
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from program3.extended_controls import cycle_gaps,nested_width

class CoverAndWidthLimits(unittest.TestCase):
 def test_cover_gap_decreases_despite_intertwining(self):
  rows=cycle_gaps();self.assertTrue(all(x['base_intertwining_error']==0 for x in rows));self.assertTrue(all(a['positive_gap']>b['positive_gap']for a,b in zip(rows,rows[1:])))
 def test_tied_parameter_replication_not_independent_width(self):
  rows=nested_width()['fully_tied_counterexample']
  for seed in (3,5,7,11):
   errors=[r['max_error']for r in rows if r['seed']==seed];self.assertEqual(len(set(errors)),1);self.assertGreater(errors[0],.1)
 def test_common_phase_preserves_complex_cross_product(self):
  rng=np.random.default_rng(18);a=rng.normal(size=(3,40))+1j*rng.normal(size=(3,40));phase=np.exp(2j*np.pi*rng.random(40));b=a*phase
  for i in range(3):
   for j in range(3):np.testing.assert_allclose(b[i]*b[j].conj(),a[i]*a[j].conj(),atol=1e-14)
 def test_independent_phase_does_not_preserve_cross_product(self):
  rng=np.random.default_rng(18);a=rng.normal(size=(3,40))+1j*rng.normal(size=(3,40));b=a*np.exp(2j*np.pi*rng.random((3,40)))
  self.assertGreater(np.max(abs(b[0]*b[1].conj()-a[0]*a[1].conj())),1.)

if __name__=='__main__':unittest.main(verbosity=2)
