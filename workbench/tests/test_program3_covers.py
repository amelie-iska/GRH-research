import sys,unittest,itertools
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from program3.covers import lift_quiver,lift_matrix,adjacency,local_layer,global_attention,maxplus_attention,order_voltage_check,surface_cover

class CoveringNetworks(unittest.TestCase):
 def test_all_small_voltages(self):
  for d in (1,2,3):
   for v in itertools.product(range(d),repeat=3):
    c=lift_quiver(3,[[0,1],[1,2],[2,0]],[[0,1],[1,2],[2,0]],d,v);self.assertTrue(c['lifted_gentle']['gentle']);self.assertEqual(len(c['arrows']),3*d)
 def test_local_and_global_lift(self):
  c=lift_quiver(3,[[0,1],[1,2],[2,0]],[[0,1],[1,2],[2,0]],4,[0,0,1]);U=lift_matrix(3,4);x=np.array([[1.,2],[-3,4],[.5,-1]])
  np.testing.assert_allclose(local_layer(U@x,adjacency(12,c['arrows'])),U@local_layer(x,adjacency(3,c['base_arrows'])))
  for fn in [global_attention,maxplus_attention]:np.testing.assert_allclose(fn(U@x),U@fn(x),atol=1e-12)
 def test_reynolds_projection(self):
  U=lift_matrix(3,5);P=U.T/5;np.testing.assert_allclose(P@U,np.eye(3));np.testing.assert_allclose((U@P)@(U@P),U@P)
 def test_order_obstruction(self):
  self.assertFalse(order_voltage_check(2,1,0,3)['relation_preserved']);self.assertTrue(order_voltage_check(2,1,0,0)['relation_preserved']);self.assertTrue(order_voltage_check(2,1,1,3)['relation_preserved'])
 def test_cellular_covers(self):
  for d in (1,2,3,4):self.assertEqual(surface_cover(degree=d)['chain_pullback_errors'],[0.,0.,0.])
 def test_relation_input_rejected(self):
  with self.assertRaises(ValueError):lift_quiver(3,[[0,1],[1,2],[2,0]],[],2,[0,0,1])
 def test_deck_action_edges(self):
  c=lift_quiver(3,[[0,1],[1,2],[2,0]],[[0,1],[1,2],[2,0]],3,[1,0,2]);edges=set(map(tuple,c['arrows']));deck=lambda x:(x//3)*3+(x+1)%3
  self.assertTrue(all((deck(a),deck(b))in edges for a,b in edges))

if __name__=='__main__':unittest.main(verbosity=2)
