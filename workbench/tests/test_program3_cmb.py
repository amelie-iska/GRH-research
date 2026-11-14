import unittest,sys,itertools
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from program3.cmb import rank_p,wilson,angles,PRODUCTS

class CMBContracts(unittest.TestCase):
 def test_rank_resolution_and_ties(self):
  self.assertEqual(rank_p([0]*511,1),1/512);self.assertEqual(rank_p([0]*511,0),1);self.assertEqual(rank_p([0,1,1],1),3/4)
 def test_exchangeable_finite_rank(self):
  for values in itertools.product(range(3),repeat=4):
   for k in range(1,5):
    ranks=[rank_p([v for j,v in enumerate(values)if j!=i],values[i])for i in range(4)]
    self.assertLessEqual(sum(x<=k/4 for x in ranks),k)
 def test_wilson(self):
  for k in (0,1,10,100):
   lo,hi=wilson(k,100);self.assertLessEqual(lo,k/100+1e-12);self.assertGreaterEqual(hi,k/100-1e-12);self.assertTrue(-1e-12<=lo<=hi<=1+1e-12)
 def test_bounded_angle_encoding(self):
  out=angles(np.array([[-1e9,0,1e9,3.]]),np.ones(4));self.assertTrue(np.all(abs(out)<np.pi));self.assertEqual(out[0,1],0)
 def test_official_sources_only(self):
  self.assertEqual(set(PRODUCTS),{'ILC','V','W','KQ85'});self.assertTrue(all(v[0].startswith('https://lambda.gsfc.nasa.gov/')for v in PRODUCTS.values()))

if __name__=='__main__':unittest.main(verbosity=2)
