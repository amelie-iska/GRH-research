import sys,unittest,itertools
from fractions import Fraction as Q
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'proof_port'))
from information_contracts import conditional_entropy,deterministic_prefix_example,finite_stopping_check

class InformationContracts(unittest.TestCase):
 def test_prefix_certificate_information(self):
  r=deterministic_prefix_example();self.assertEqual(r['full_prefix_bits'],0);self.assertEqual(r['full_prefix_plus_certificate_bits'],0);self.assertEqual(r['restricted_context_bits'],1);self.assertEqual(r['restricted_plus_certificate_bits'],0)
 def test_finite_stopping(self):
  for n,a in itertools.product([4,8,12],[Q(1,2),Q(1,5),Q(1,20)]):self.assertLessEqual(Q(finite_stopping_check(n,a)['null_first_crossing_probability']),a)
 def test_probability_domain(self):
  with self.assertRaises(ValueError):conditional_entropy([((0,),Q(1,2))],[0],[])
  with self.assertRaises(ValueError):finite_stopping_check(100)

if __name__=='__main__':unittest.main(verbosity=2)
