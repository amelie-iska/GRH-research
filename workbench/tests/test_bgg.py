import sys,itertools,unittest
from pathlib import Path
from fractions import Fraction as F
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from bgg import sl2,sl2_defects,exterior_generators,differential,contracting_homotopy,zero,identity,multiply,add,scale,nonzero

class BGG(unittest.TestCase):
 def test_true_finite_quotients(self):
  for n in range(9):self.assertTrue(all(not v for v in sl2_defects(n,n+1).values()))
 def test_cutoff_defect_formula(self):
  for lam in [-3,-1,0,2,F(1,2)]:
   for k in range(1,10):
    out=sl2_defects(lam,k);c=k*(k-1-lam)
    expected=[] if c==0 else [[k-1,k-1,str(c)]]
    self.assertEqual(out['ef_minus_h'],expected)
    self.assertEqual(out['he_minus_2e'],[]);self.assertEqual(out['hf_plus_2f'],[])
 def test_singular_embedding_coefficients(self):
  for n in range(9):
   for j in range(20):
    self.assertEqual((n+1+j)*(n-(n+1+j)+1),j*((-n-2)-j+1))
    self.assertEqual(n-2*(n+1+j),(-n-2)-2*j)
 def test_exterior_relations(self):
  for m in range(1,5):
   ops=exterior_generators(m);z=zero(1<<m)
   for i,a in enumerate(ops):
    self.assertEqual(multiply(a,a),z)
    for b in ops[i+1:]:self.assertEqual(add(multiply(a,b),multiply(b,a)),z)
 def test_differential_and_homotopy(self):
  for x in itertools.product((-1,0,1),repeat=3):
   d=differential(x);self.assertEqual(multiply(d,d),zero(8))
   if any(x):
    h=contracting_homotopy(x);self.assertEqual(add(multiply(d,h),multiply(h,d)),identity(8))
   else:
    with self.assertRaises(ValueError):contracting_homotopy(x)
 def test_integral_torsion_boundary(self):
  d=differential([2]);h=contracting_homotopy([2]);self.assertEqual(d[1][0],2);self.assertEqual(h[0][1],F(1,2))
  self.assertEqual(add(multiply(d,h),multiply(h,d)),identity(2))
  # Rational contraction used a nonintegral coefficient: no integral exactness claim.
 def test_domains(self):
  for x in [True,.5,float('inf')]:
   with self.assertRaises(ValueError):sl2(x,3)
  for k in [0,33,True]:
   with self.assertRaises(ValueError):sl2(2,k)
  with self.assertRaises(ValueError):exterior_generators(6)

if __name__=='__main__':unittest.main(verbosity=2)
