"""Exact scientific checks for independent variable-precision theta modules."""
import unittest,importlib.util,sys
from pathlib import Path
from fractions import Fraction as F

class AdaptiveTheta(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.path=Path(__file__).with_name('precision.py')
  if cls.path.exists():
   spec=importlib.util.spec_from_file_location('precision',cls.path);cls.module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=cls.module;spec.loader.exec_module(cls.module)
 def test_precision_module_exists(self):
  self.assertTrue(self.path.is_file(),'Variable-precision certified primitives are missing')
 def test_sampler_module_exists(self):
  self.assertTrue(Path(__file__).with_name('adaptive_theta.py').is_file(),'Adaptive theta sampler is missing')
 def test_requested_sample_radius(self):
  p=Path(__file__).with_name('adaptive_theta.py')
  if not p.exists():self.skipTest('feature missing')
  import adaptive_theta as a
  for q in [3,4,5]:
   r=a.point(q,F(1,2),F(0),F(1,10**24))
   self.assertLessEqual(r['radius'],F(1,10**24))
   self.assertEqual(r['radius'],sum(r['budget'].values(),F()))
   self.assertTrue(all(x>=0 for x in r['budget'].values()))
 def test_adaptive_budget_serializes_without_global_integer_limit_change(self):
  p=Path(__file__).with_name('adaptive_theta.py')
  if not p.exists():self.skipTest('feature missing')
  import adaptive_theta as a,json
  before=sys.get_int_max_str_digits()
  r=a.point(5,F(1,2),F(0),F(1,10**32))
  json.dumps(a.encode(r))
  self.assertEqual(sys.get_int_max_str_digits(),before)
  self.assertEqual(a.encode(F(1,1<<15000))['denominator'],self.module.decimal_integer(1<<15000))
  c=self.module.Context(16000)
  encoded=c.real(F(-1,7)).encode()
  self.assertEqual(self.module.parse_integer(encoded['lo']),c.real(F(-1,7)).lo)
  self.assertEqual(sys.get_int_max_str_digits(),before)
 def test_exact_endpoints_and_precision_guards(self):
  if not self.path.exists():self.skipTest('feature missing')
  c=self.module.Context(80)
  a=c.bounds(F(-5,7),F(2,3));b=c.bounds(F(3,5),F(7,6))
  for x in [F(-5,7),F(2,3)]:
   for y in [F(3,5),F(7,6)]:
    self.assertTrue((a+b).contains(x+y));self.assertTrue((a*b).contains(x*y));self.assertTrue((a/b).contains(x/y))
  with self.assertRaises(TypeError):c.real(.5)
  with self.assertRaises(TypeError):c.real(True)
  for bad in [0.0,False]:
   with self.assertRaises(TypeError):c.complex(c.complex(1),bad)
  with self.assertRaises(TypeError):a+self.module.Context(96).real(1)
  for bad in [0,-2,True,8.0]:
   with self.assertRaises((ValueError,TypeError)):self.module.Context(bad)
 def test_transcendental_identities_and_refinement(self):
  if not self.path.exists():self.skipTest('feature missing')
  widths=[]
  for bits in [64,128,256]:
   c=self.module.Context(bits);p=c.pi();self.assertTrue(p.lo>3*c.scale and p.hi<F(22,7)*c.scale)
   z=c.exp(c.complex(0,p));self.assertTrue(z.re.contains(-1) and z.im.contains(0))
   x=c.exp(c.complex(c.log(F(3,2)),0));self.assertTrue(x.re.contains(F(3,2)) and x.im.contains(0))
   widths.append(p.radius())
  self.assertGreater(widths[0],widths[1]);self.assertGreater(widths[1],widths[2])

if __name__=='__main__':unittest.main()
