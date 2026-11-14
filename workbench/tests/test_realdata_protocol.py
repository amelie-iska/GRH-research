import importlib.util
from pathlib import Path
import unittest
import numpy as np
p=Path(__file__).resolve().parents[1]/'experiments/run_realdata.py'
s=importlib.util.spec_from_file_location('study',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)

class Protocol(unittest.TestCase):
 def test_split_and_future_invariance(self):
  x=np.arange(1000,dtype=np.int64)**2;ids=np.arange(1000);a=m.prepare(x,ids)
  y=x.copy();y[600:]+=123456;b=m.prepare(y,ids)
  np.testing.assert_equal(a['edges'],b['edges']);np.testing.assert_equal(a['reps'],b['reps'])
  np.testing.assert_equal(a['groups']['train']['context'],b['groups']['train']['context'])
  for name,start,end in [('train',0,600),('validation',600,800),('test',800,1000)]:
   idx=a['groups'][name]['index'];self.assertTrue(np.all(idx-1-m.LAG>start));self.assertTrue(np.all(idx<end))
 def test_exact_residual_reconstruction(self):
  x=np.arange(1000,dtype=np.int64)**2;d=m.prepare(x,np.arange(1000));g=d['groups']['test'];r=g['target']-d['reps'][g['y']]
  np.testing.assert_equal(d['reps'][g['y']]+r,g['target'])
  prob=np.full((len(g['y']),d['K']),1/d['K']);a,b=m.code_lengths(prob,g,d['reps'])
  self.assertTrue(np.all(b>=1));self.assertTrue(np.allclose(a,np.log2(d['K'])))
  out=m.summarize(prob,g,d['reps']);self.assertEqual(out['canonical_target_bytes'],4*len(g['y']))
 def test_gap_not_concatenated(self):
  ids=np.arange(1000);ids[300:]+=3;d=m.prepare(np.arange(1000),ids)
  self.assertFalse(any(300<=i<=308 for i in d['groups']['train']['index']))
 def test_invalid_probability(self):
  d=m.prepare(np.arange(1000)**2,np.arange(1000));g=d['groups']['test'];p=np.zeros((len(g['y']),d['K']))
  with self.assertRaises(ValueError):m.code_lengths(p,g,d['reps'])
 def test_fixed_precision(self):
  self.assertEqual(m.fixed('315.71',100),31571)
  with self.assertRaises(ValueError):m.fixed('1.001',100)

if __name__=='__main__':unittest.main(verbosity=2)
