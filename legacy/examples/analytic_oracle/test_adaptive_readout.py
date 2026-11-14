"""Focused exact readout checks; run with Python unittest, no new packages."""
import unittest
from fractions import Fraction as F
from pathlib import Path
import importlib.util

class AdaptiveReadout(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  path=Path(__file__).with_name('adaptive_readout.py')
  cls.module_path=path
  if path.exists():
   spec=importlib.util.spec_from_file_location('adaptive_readout',path)
   cls.api=importlib.util.module_from_spec(spec);spec.loader.exec_module(cls.api)
 def test_requested_api_exists(self):
  self.assertTrue(self.module_path.is_file(),'Requested-tolerance executed readout is missing')
 def test_exact_update_and_loss(self):
  if not self.module_path.exists():self.skipTest('feature missing')
  trace=self.api.train([(F(1),F(2)),(F(-3),F(1,2))],F(1,10**6))
  self.assertEqual(trace[1]['coefficients'],[(F(1,4),F(1,2)),(F(-3,4),F(1,8))])
  for old,new in zip(trace,trace[1:]):
   self.assertEqual(new['objective'],old['objective']*F(9,16))
   self.assertLess(new['residual'],old['residual'])
  self.assertLessEqual(trace[-1]['residual'],F(1,10**6))
 def test_budget_and_floor(self):
  if not self.module_path.exists():self.skipTest('feature missing')
  data=self.api.load_frozen()
  for q in [3,4,5]:
   result=self.api.certify(data,q,F(1,10**15))
   parts=result['budget'];total=sum(parts.values(),F())
   self.assertEqual(total,result['compact_uniform_bound'])
   self.assertLessEqual(total,F(1,10**15))
   self.assertLess(result['degree'],64)
   self.assertEqual(result['trace'][0]['iteration'],0)
   self.assertEqual(result['trace'][-1]['iteration'],result['steps'])
   with self.assertRaises(self.api.ToleranceNotCertified):self.api.certify(data,q,F(1,10**18))
 def test_cached_fourier_bounds_cannot_be_mutated(self):
  if not self.module_path.exists():self.skipTest('feature missing')
  bounds,_=self.api.fourier(3)
  with self.assertRaises(TypeError):bounds[0]=bounds[1]
 def test_large_exact_values_keep_exact_endpoints(self):
  if not self.module_path.exists():self.skipTest('feature missing')
  encoded=self.api.encode(F(10**1000))
  self.assertEqual(encoded['numerator'],str(10**1000))
  self.assertIsNone(encoded['display'])
 def test_generator_targets_are_rejected_explicitly(self):
  if not self.module_path.exists():self.skipTest('feature missing')
  with self.assertRaises(TypeError):self.api.train(((F(1),F(0)) for _ in range(2)),F(1,10))
 def test_exact_input_guards(self):
  if not self.module_path.exists():self.skipTest('feature missing')
  data=self.api.load_frozen()
  for bad in [0,-1,0.1,True,'1e-15']:
   with self.assertRaises((ValueError,TypeError)):self.api.certify(data,3,bad)
  for bad in [2,3.0,True]:
   with self.assertRaises((ValueError,TypeError)):self.api.certify(data,bad,F(1,10))

if __name__=='__main__':unittest.main()
