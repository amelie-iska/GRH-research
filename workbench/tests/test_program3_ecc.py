import unittest,sys,itertools,json
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from program3.ecc import Curve,Builder,execute_words,count_circuit,scalar_circuit,validate_scalar,decomposition,field_oracle

class EllipticCircuits(unittest.TestCase):
 def test_curve_group(self):
  c=Curve();P=c.points();self.assertEqual(len(P),13)
  for x,y,z in itertools.product(P,repeat=3):self.assertEqual(c.add(c.add(x,y),z),c.add(x,c.add(y,z)))
 def test_endomorphism(self):
  c=Curve();G=c.points()[1];d=decomposition(c,G)
  for P,Q in itertools.product(c.points(),repeat=2):self.assertEqual(c.phi(c.add(P,Q),d['beta']),c.add(c.phi(P,d['beta']),c.phi(Q,d['beta'])))
  for k,(a,b)in enumerate(d['pairs']):self.assertEqual(c.mul(k,G),c.add(c.mul(a,G),c.mul(b,d['phi_generator'])))
 def test_total_point_encoding(self):
  c=Curve();valid={c.encode(P)for P in c.points()}
  for w in range(1<<c.width):
   if w in valid:self.assertEqual(c.encode(c.decode(w)),w)
   else:
    with self.assertRaises(ValueError):c.decode(w)
 def test_mcx_clean(self):
  for k in range(0,9):
   work=list(range(k+1,k+1+max(0,k-2)));b=Builder(k+1+len(work),work);b.mcx(list(range(k)),k);x=np.arange(1<<(k+1),dtype=np.uint64);y=execute_words(b.gates,x)
   expected=x.copy();expected[(x&((1<<k)-1))==((1<<k)-1)]^=1<<k
   np.testing.assert_array_equal(y,expected)
 def test_endpoint_swap(self):
  for a,b in itertools.combinations(range(16),2):
   c=Builder(5,[4]);c.endpoint_swap([0,1,2,3],a,b);x=np.arange(16,dtype=np.uint64);y=execute_words(c.gates,x);e=x.copy();e[a]=b;e[b]=a;np.testing.assert_array_equal(y,e)
 def test_full_scalar_binary(self):
  c=Curve();r=validate_scalar(c,scalar_circuit(c,c.points()[1],'binary'));self.assertTrue(r['all_data_words_checked'])
 def test_full_scalar_endomorphism(self):
  c=Curve();r=validate_scalar(c,scalar_circuit(c,c.points()[1],'endomorphism'));self.assertTrue(r['all_decomposition_and_scratch_return_zero'])
 def test_field_inverse_zero(self):
  c,t=field_oracle(7,'inverse');self.assertEqual(t[0],0)
  for x in range(1,7):self.assertEqual((t[x]&7)*x%7,1);self.assertTrue(t[x]&8)
 def test_malformed_domains(self):
  for args in [(9,0,1),(7,0,0),(True,0,1)]:
   with self.assertRaises(ValueError):Curve(*args)
  b=Builder(5,[4])
  with self.assertRaises(ValueError):b.mcx([0,1,2,3],4)
 def test_counter_is_from_stream(self):
  c=scalar_circuit(Curve(),(1,2),'binary');r=count_circuit(json.loads(json.dumps(c)));self.assertEqual(r['total_gates'],len(c['gates']));self.assertEqual(r,c['resources'])

if __name__=='__main__':unittest.main(verbosity=2)
