#!/usr/bin/env python3
"""Focused failure controls, not a substitute for the independent literal audit."""
import sys
sys.dont_write_bytecode=True
import unittest
from fractions import Fraction
import full_column_v1 as F

class Controls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.captured={p:(F.ROOT/p).read_bytes() for p in F.HELPERS}
        cls.T,cls.P=F.load_helpers(cls.captured)

    def test_omega_conjugation_is_not_componentwise(self):
        x=(4,-4)
        self.assertEqual(F.econj(x),(8,4))
        self.assertEqual(F.emul(x,F.econj(x)),(48,0))
        self.assertNotEqual(F.emul(x,(4,4)),(48,0))

    def test_fixed_profile_guard_and_nodes(self):
        self.assertEqual([F.finite_profile_node(60000,N) for N in (60000,60001,119999,120000)],[0,1,1,0])
        for D in (60001,144.0,True):
            with self.assertRaises(ValueError):F.finite_profile_node(D,145)
        self.assertGreaterEqual(Fraction(1,60000),4*Fraction(1,240000))

    def test_ideal_squarefreeness_traps(self):
        spf=self.P.sieve_spf(1000)
        a,_=self.P.ideal_norm_group(49,spf)
        b,_=self.P.ideal_norm_group(25,spf)
        self.assertEqual((a['mu'],a['ideal_multiplicity'],a['ideal_prime_norms']),(1,1,[7,7]))
        self.assertEqual((b['mu'],b['ideal_multiplicity'],b['ideal_prime_norms']),(-1,1,[25]))
        self.assertIsNone(self.P.ideal_norm_group(125,spf)[0])
        self.assertIsNone(self.P.ideal_norm_group(343,spf)[0])

    def test_local_zeros_and_split_orientation(self):
        self.assertIsNone(self.T.direct_symbol([((1,3),1)],(1,3)))
        a=self.T.direct_symbol([((1,3),1)],(2,0))
        b=self.T.direct_symbol([((-2,-3),1)],(2,0))
        self.assertEqual((a,b),(2,4))
        self.assertNotEqual(a,b)
        self.assertIsNone(self.T.direct_symbol([((-5,0),1)],(5,0)))
        self.assertIsNotNone(self.T.direct_symbol([((-5,0),1)],(0,1)))

    def test_full_self_divisor_is_necessary(self):
        ids=(0,1,2)
        self.assertEqual(sum((-1)**len(d) for d in F.subsets(ids)),0)
        truncated=[d for d in F.subsets(ids) if d!=ids]
        self.assertNotEqual(sum((-1)**len(d) for d in truncated),0)
        self.assertEqual(len(F.subsets(ids)),8)

    def test_stale_helper_refused(self):
        bad=dict(self.captured)
        p=next(iter(F.HELPERS));bad[p]+=b'\n# changed\n'
        with self.assertRaises(RuntimeError):F.load_helpers(bad)

    def test_existing_output_refused_before_read_or_write(self):
        with self.assertRaises(FileExistsError):F.execute(F.HERE,144,12,13,1)

    def test_original_coefficients_actual_cutoff(self):
        self.assertEqual(F.original_coefficients([7,7],49,3),(1,2,1,2))
        whole=F.original_coefficients([7,7],49,12)[0]
        separate=F.original_coefficients([7],7,12)[0]*F.original_coefficients([7],7,12)[0]
        self.assertNotEqual(whole,separate)

if __name__=='__main__':
    unittest.main(verbosity=2)
