import unittest,sys,json
from pathlib import Path
from fractions import Fraction as F

class AdaptiveFamily(unittest.TestCase):
 def test_family_driver_exists(self):
  self.assertTrue(Path(__file__).with_name('adaptive_family.py').is_file(),'End-to-end adaptive family driver missing')
 def test_fourier_rejects_empty_and_negative_degree(self):
  if not Path(__file__).with_name('adaptive_family.py').exists():self.skipTest('feature missing')
  import adaptive_family as a
  for degree in [-1,False,0]:
   with self.assertRaises((TypeError,ValueError)):a.fourier([],degree,128)
 def test_analytic_allocations(self):
  if not Path(__file__).with_name('adaptive_family.py').exists():self.skipTest('feature missing')
  import adaptive_family as a
  for eps in [F(1,10**8),F(1,10**24),F(1,10**40)]:
   d,m,eta=a.choices(eps)
   self.assertGreater(m,d)
   self.assertLessEqual(10*a.V**(d+1)/(1-a.V),eps/8)
   self.assertLessEqual(10*F(1,2**m)/(1-F(1,2**m))/(1-a.V),eps/8)
   self.assertLessEqual(eta/(1-a.U),eps/8)
 def test_compressed_trace_is_actual_replay(self):
  if not Path(__file__).with_name('adaptive_family.py').exists():self.skipTest('feature missing')
  import adaptive_family as a
  targets=[(F(1,3),F(-2,5)),(F(7,4),F(1,11))]
  rows=a.compressed_train(targets,F(1,10**15))
  self.assertEqual(rows[1]['coefficient_scale'],F(1,4))
  state=[(F(),F()) for _ in targets]
  for row in rows:
   recovered=[(row['coefficient_scale']*x,row['coefficient_scale']*y) for x,y in targets]
   self.assertEqual(recovered,state)
   self.assertEqual(row['coefficient_state_sha256'],a.state_hash(state))
   state=[((3*x+u)/4,(3*y+v)/4) for (x,y),(u,v) in zip(state,targets)]

if __name__=='__main__':unittest.main()
