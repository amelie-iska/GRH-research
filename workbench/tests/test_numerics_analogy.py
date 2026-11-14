import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from numerics import heat_mode,refinement,flux,rank
from analogy import Memory,retrieve,verify_mapping,verify_deduction

class Numerics(unittest.TestCase):
 def test_orders(self):
  r=refinement();self.assertTrue(all(1.98<p<2.02 for p in r['spatial_orders']));self.assertTrue(all(.99<p<1.02 for p in r['temporal_orders']))
  self.assertTrue(all(x['time']==1.5 for x in r['coupled']))
 def test_invalid_heat(self):
  for args in [(32,.08,1.5,1),(4,.08,1.5,None,2,1)]:
   with self.assertRaises(ValueError):heat_mode(*args)
 def test_flux_alias(self):
  self.assertFalse(flux(3,2)['admissible']);self.assertAlmostEqual(flux(3,2)['alias_error'],-4)
  self.assertTrue(flux(3,4)['admissible']);self.assertAlmostEqual(flux(3,4)['alias_error'],0)
 def test_bad_prime(self):
  self.assertEqual(rank([[1,0],[0,2]]),2);self.assertEqual(rank([[1,0],[0,2]],2),1)
  with self.assertRaises(ValueError):rank([[1]],4)

class Analogy(unittest.TestCase):
 def test_train_only_retrieval(self):
  b=[Memory('a',frozenset({'g1'}),'train','e1',(0.,1.)),Memory('b',frozenset({'g2'}),'train','e1',(1.,1.))]
  self.assertEqual(retrieve((0.,1.),frozenset({'g1'}),'e1',b),[(1.,'b')])
  with self.assertRaises(ValueError):retrieve((0.,1.),frozenset({'g3'}),'e2',b)
  with self.assertRaises(ValueError):retrieve((0.,1.),frozenset({'g3'}),'e1',[Memory('c',frozenset({'g4'}),'test','e1',(0.,1.))])
 def test_subpath_and_direction(self):
  a=dict(source_nodes={'a':'state','b':'state'},target_nodes={'x':'state','y':'state','z':'state'},source_edges={'e':('a','b','advance')},target_edges={'f':('x','y','tick'),'g':('y','z','tick')},node_map={'a':'x','b':'z'},paths={'e':['f','g']},relation_words={'advance':{('tick','tick')}})
  self.assertTrue(verify_mapping(**a));a['paths']={'e':['g','f']}
  with self.assertRaises(ValueError):verify_mapping(**a)
  a['paths']={}
  with self.assertRaises(ValueError):verify_mapping(**a)
 def test_deduction(self):
  r={'modus':({'P','P_implies_Q'},'Q'),'next':({'Q'},'R')}
  self.assertIn('R',verify_deduction(frozenset({'P','P_implies_Q'}),r,[('modus','Q'),('next','R')]))
  with self.assertRaises(ValueError):verify_deduction(frozenset({'P'}),r,[('modus','Q')])

if __name__=='__main__':unittest.main(verbosity=2)
