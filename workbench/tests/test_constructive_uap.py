import itertools,sys,unittest
from fractions import Fraction as Q
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'proof_port'))
from constructive import gather,permute_matrix,reynolds_node_map,square_spline,product_spline,select_slot

class ConstructiveUniform(unittest.TestCase):
 def test_exact_softmax_gather(self):
  for n in range(1,17):
   x=[[Q(i-3,7),Q(i*i+1,3)]for i in range(n)]
   self.assertEqual(gather(x)['recovered'],x)
 def test_relu_square_error(self):
  knots=[Q(i,4)for i in range(-8,9)];h=Q(1,4)
  for x in [Q(i,100)for i in range(-200,201)]:self.assertLessEqual(abs(square_spline(x,knots)-x*x),h*h/4)
 def test_relu_product_error(self):
  knots=[Q(i,4)for i in range(-8,9)]
  for x,y in itertools.product([Q(i,8)for i in range(-8,9)],repeat=2):self.assertLessEqual(abs(product_spline(x,y,knots)-x*y),Q(1,128))
 def test_slot_gate(self):
  for x,b in itertools.product([Q(i,4)for i in range(-8,9)],(0,1)):self.assertEqual(select_slot(x,b,2),x*b)
 def test_exact_reynolds_equivariance(self):
  def base(a):return [sum(a[i])+3*i+2*a[0][i]for i in range(len(a))]
  for bits in itertools.product((0,1),repeat=3):
   a=[[0]*3 for _ in range(3)]
   for (i,j),v in zip(itertools.combinations(range(3),2),bits):a[i][j]=a[j][i]=v
   f=reynolds_node_map(base,a)
   for p in itertools.permutations(range(3)):
    fp=reynolds_node_map(base,permute_matrix(a,p));self.assertEqual([fp[p[i]]for i in range(3)],f)
 def test_domains(self):
  with self.assertRaises(ValueError):gather([])
  with self.assertRaises(ValueError):select_slot(3,1,2)
  with self.assertRaises(ValueError):square_spline(0,[1,0])

if __name__=='__main__':unittest.main(verbosity=2)
