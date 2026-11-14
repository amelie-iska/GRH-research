import unittest,sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from workbench.integration.arithmetic import compile_oracle,replay,expected
from workbench.integration.neural_operator import walk,polynomial,quantum_channel,analytic_weights
class UniformArithmeticAndOperators(unittest.TestCase):
 def test_field_add_complete_registers(self):
  c=compile_oracle(7,'add');x=np.tile(np.arange(64,dtype=np.uint64),16);z=np.repeat(np.arange(16,dtype=np.uint64),64);np.testing.assert_array_equal(replay(c,x,z),z^expected(c,x))
 def test_field_multiply_complete_registers(self):
  c=compile_oracle(7,'multiply');x=np.tile(np.arange(64,dtype=np.uint64),16);z=np.repeat(np.arange(16,dtype=np.uint64),64);np.testing.assert_array_equal(replay(c,x,z),z^expected(c,x))
 def test_inverse_complete_registers(self):
  c=compile_oracle(13,'inverse');x=np.tile(np.arange(16,dtype=np.uint64),32);z=np.repeat(np.arange(32,dtype=np.uint64),16);np.testing.assert_array_equal(replay(c,x,z),z^expected(c,x))
 def test_invalid_moduli(self):
  for p in(0,1,9,True,65522):
   with self.assertRaises(ValueError):compile_oracle(p,'add')
 def test_replay_budget_domain(self):
  c=compile_oracle(7,'add')
  with self.assertRaises(ValueError):replay(c,[64])
 def test_polynomial_cover_intertwines(self):
  w=np.arange(1,9,dtype=float);w/=w.sum();U=np.tile(np.eye(3),(5,1));np.testing.assert_allclose(polynomial(walk(15),w)@U,U@polynomial(walk(3),w),atol=1e-14)
 def test_channel_and_probability_diagonal(self):
  rng=np.random.default_rng(8);a=rng.normal(size=(9,9))+1j*rng.normal(size=(9,9));rho=a@a.conj().T;rho/=np.trace(rho);w=analytic_weights(1.5);out=quantum_channel(rho,w);self.assertAlmostEqual(np.trace(out).real,1);self.assertGreater(np.linalg.eigvalsh(out).min(),-1e-12);np.testing.assert_allclose(np.diag(out).real,polynomial(walk(9),w)@np.diag(rho).real,atol=1e-14)
 def test_zero_time_identity(self):np.testing.assert_array_equal(polynomial(walk(9),analytic_weights(0)),np.eye(9))
if __name__=='__main__':unittest.main(verbosity=2)
