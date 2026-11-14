import itertools,json,math,sys,unittest
from pathlib import Path
from fractions import Fraction as F
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'proof_port'))
from check_models import graph_pair,pair_refinement,clique_count,hull,minkowski,softmax_hessian_witness,circuit,gate_neural,finite_relu_interpolator,gate_audit
from inventory import extract,uncomment,git_blob

class ExpressivityPort(unittest.TestCase):
 def test_source_comments_and_aliases(self):
  text='% \\begin{theorem}fake\\end{theorem}\n\\newtheorem{fact}{Proposition}\n\\begin{fact}[Real]\\label{f}x\\end{fact}\n\\begin{proof}y\\end{proof}\n'
  rows=extract(text);self.assertEqual(len(rows),1);self.assertEqual(rows[0]['labels'],['f']);self.assertEqual(rows[0]['status'],'source_port_only');self.assertIn('y',rows[0]['proof_latex'])
 def test_git_blob(self):self.assertEqual(git_blob(b''),'e69de29bb2d1d6434b8b29ae775ad8c2e48c5391')
 def test_graph_counterexample(self):
  a,b=graph_pair();self.assertEqual(clique_count(a),8);self.assertEqual(clique_count(b),0)
  self.assertTrue(all(r['equal']for r in pair_refinement([a,b])))
  for g in (a,b):
   self.assertTrue(all(sum(row)==6 for row in g))
   for i,j in itertools.combinations(range(16),2):self.assertEqual(sum(g[i][k]*g[j][k]for k in range(16)),2)
 def test_hessian_factor(self):
  r=softmax_hessian_witness();self.assertGreater(r['hessian_operator_norm'],r['source_claimed_bound']);self.assertLess(r['hessian_operator_norm'],r['safe_trace_bound'])
 def test_polygon_exact(self):
  a=[(0,0),(2,0),(2,2),(0,2)];b=[(0,1),(1,0),(0,-1),(-1,0)]
  self.assertEqual(len(minkowski(a,b)),8)
  self.assertEqual(hull([(0,0),(0,0),(1,1),(2,2)]),[(0,0),(2,2)])
 def test_relu_finite(self):
  p=[[F(0),F(0)],[F(1),F(0)],[F(0),F(1)]];y=[[F(3)],[F(-2)],[F(7)]]
  f=finite_relu_interpolator(p,y);self.assertEqual([f(x)for x in p],y)
  with self.assertRaises(ValueError):finite_relu_interpolator(p+p,y+y)
 def test_gate_truth_tables(self):
  for a,b in itertools.product((0,1),repeat=2):
   self.assertEqual(gate_neural('AND',a,b),a*b);self.assertEqual(gate_neural('XOR',a,b),int(a!=b));self.assertEqual(gate_neural('OR',a,b),int(bool(a or b)))
 def test_circuit_execution(self):self.assertEqual(gate_audit(examples=12),384)
 def test_circuit_rejects_future_wire(self):
  with self.assertRaises(ValueError):circuit([('AND',[0,2])],[1,0])
  with self.assertRaises(ValueError):circuit([('NOT',[0])],[1],interventions={2:1})
 def test_maxplus_is_not_score_winner(self):
  scores=[2,1];values=[[0,0],[5,-2]]
  self.assertEqual([max(range(2),key=lambda j:scores[j]+values[j][c])for c in range(2)],[1,0])
 def test_exact_margin(self):
  for i,j in itertools.product(range(-3,4),repeat=2):
   if i-j>2:
    for a,b in itertools.product([F(-1),F(0),F(1)],repeat=2):self.assertGreater(i+a,j+b)
 def test_token_symmetry_obstruction(self):
  # A constant identical-token input is fixed by token swap. An equivariant
  # output at that input must also be fixed; selecting one vertex violates it.
  x=(0,0);y=(1,0);self.assertEqual(x,x[::-1]);self.assertNotEqual(y,y[::-1])

if __name__=='__main__':unittest.main(verbosity=2)
