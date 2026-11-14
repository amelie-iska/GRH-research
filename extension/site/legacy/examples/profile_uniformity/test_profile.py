#!/usr/bin/env python3
"""Focused exact controls for fresh norm-group/profile data."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as Q
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parent))
import unit_profile as P

class ProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.spf=P.sieve_spf(4095)

    def test_split_and_inert_norm_groups(self):
        g,why=P.ideal_norm_group(49,self.spf)
        self.assertIsNone(why);self.assertEqual(g['mu'],1);self.assertEqual(g['ideal_multiplicity'],1)
        self.assertEqual(g['ideal_prime_norms'],[7,7]);self.assertEqual(g['divisor_norms'],[1,7,7,49])
        g,why=P.ideal_norm_group(25,self.spf)
        self.assertEqual(g['mu'],-1);self.assertEqual(g['ideal_multiplicity'],1)
        self.assertEqual(g['ideal_prime_norms'],[25]);self.assertEqual(g['divisor_norms'],[1,25])
        g,why=P.ideal_norm_group(91,self.spf)
        self.assertEqual(g['ideal_multiplicity'],4);self.assertEqual(g['mu'],1)
        self.assertEqual(g['divisor_norms'],[1,7,13,91])
        for n in (2,3,4,6,12,21,50):self.assertEqual(P.ideal_norm_group(n,self.spf)[1],'S_prime_2_or_3')
        for n in (5,11,55):self.assertEqual(P.ideal_norm_group(n,self.spf)[1],'inert_exponent_not_2')
        self.assertEqual(P.ideal_norm_group(343,self.spf)[1],'split_exponent_above_2')
        self.assertEqual(P.ideal_norm_group(625,self.spf)[1],'inert_exponent_not_2')

    def test_long_factor_multiplicity_and_strict_cutoff(self):
        ds=[1,7,7,49]
        self.assertEqual(P.long_factor_count(ds,49,6),2)
        self.assertEqual(P.long_factor_count(ds,49,7),0)
        self.assertEqual(P.long_factor_count(sorted(set(ds)),49,6),1) # forbidden norm-divisor deduplication

    def test_complete_profile_signs_and_exact_energy(self):
        data,summary=P.compute_case(256,self.spf)
        rows=data['active_norm_groups'];rejected=data['rejected_integer_norms']
        all_n=[r['norm'] for r in rows]+[n for values in rejected.values() for n in values]
        self.assertEqual(sorted(all_n),list(range(257,512)))
        self.assertTrue(rows);self.assertTrue(all(r['r_U']%2==0 and abs(r['A_U'])%2==1 for r in rows))
        aligned=sum(r['ideal_multiplicity']*r['A_U']*r['chi_minus_one']*r['real_minus_one_profile_node'] for r in rows)
        self.assertEqual(aligned,summary['sum_abs_A_over_ideals'])
        self.assertEqual(summary['unit_row_energy'],Q(aligned*aligned,256))
        self.assertGreaterEqual(summary['unit_row_energy'],summary['count_only_energy_lower_bound'])
        self.assertEqual({r['real_minus_one_profile_node'] for r in rows},{-1,1})
        self.assertTrue(data['signed_profile']['varies_with_D']);self.assertTrue(data['unsigned_nodal_comparator']['varies_with_D'])
        self.assertFalse(data['unsigned_nodal_comparator']['fixed_profile_baseline'])
        self.assertEqual(summary['principal_residue'],0)

    def test_common_profile_exact_nodes_and_support(self):
        data,_=P.compute_case(256,self.spf);values={r['norm']:r['real_minus_one_profile_node'] for r in data['active_norm_groups']}
        for n in range(255,514):self.assertEqual(P.profile_integer_node(n,values),values.get(n,0))
        for n in values:
            self.assertGreater(Q(4*n-1,4*256),1)
            self.assertLess(Q(4*n+1,4*256),2)
        self.assertLess(Q(1,2*256),Q(1,256)) # disjoint bump support widths vs centre spacing
        self.assertEqual(P.character_minus_one_by_norm(7),-1)
        self.assertEqual(P.character_minus_one_by_norm(13),1)
        for n in values:self.assertEqual(P.character_minus_one_by_norm(n),1 if n%4==1 else -1)

    def test_original_ideal_enumeration_and_A_helper(self):
        expected=P.current_source_hashes();checks=P.explicit_crosschecks([256,1024],expected)
        self.assertEqual(checks['D_values'],[256,1024])
        self.assertGreater(checks['explicit_ideal_columns'],0)
        self.assertEqual(checks['original_A_checks'],checks['explicit_ideal_columns'])
        self.assertEqual(checks['direct_symbol_checks'],checks['explicit_ideal_columns'])
        self.assertEqual(checks['norm_group_multiplicities_match'],True)
        self.assertEqual(checks['raw_character_at_norm7'],-1)
        self.assertEqual(checks['raw_epsilon_character_at_norm7_phase'],1)
        self.assertGreater(checks['tower_raw_symbol_checks'],checks['explicit_ideal_columns'])
        for c in checks['cases']:
            self.assertTrue(all(v['h1_ordered_pair_numerator']>0 for v in c['tower_rows']))

    def test_order6_unit_and_non_norm_only_tower_masks(self):
        data,summary=P.compute_case(256,self.spf)
        self.assertEqual(data['literal_row'],[1,1])
        self.assertEqual(data['main_profile'],'order6_signed_profile')
        self.assertTrue(data['order6_signed_profile']['all_nontrivial_powers_nonprincipal'])
        self.assertFalse(data['order6_signed_profile']['exact_conductor_claim'])
        for g in data['active_norm_groups']:
            a=g['A_U'];phase=(g['chi_epsilon_exponent']+g['order6_profile_node_exponent'])%6
            z=P.Tower.PH_ZETA[phase];self.assertEqual((a*z[0],a*z[1]),(abs(a),0))
        tower=data['ideal_tower_family'];at49=[v for v in tower['rows'] if v['norm']==49]
        self.assertEqual(len(at49),3)
        self.assertEqual(sorted(v['split_prime_coverage'][7] for v in at49),[1,1,2])
        self.assertEqual(sum(not v['squarefree'] for v in at49),2)
        self.assertGreater(min(v['T_v'] for v in at49 if v['split_prime_coverage'][7]==1),next(v['T_v'] for v in at49 if v['split_prime_coverage'][7]==2))
        for c in tower['caps']:
            self.assertGreaterEqual(c['primary_goodS_cumulative']['rows'],1)
            self.assertGreaterEqual(c['primary_goodS_cumulative']['energy'],summary['unit_row_energy'])
            self.assertEqual(c['H'],c['X']**6)
        self.assertEqual(next(c for c in tower['caps'] if c['X']==4)['secondary_goodS_dyadic']['rows'],0)
        cap=tower['capacity_matched'];self.assertEqual(cap['X_floor_H_1over6'],2)
        self.assertEqual(P.Tower.direct_symbol((((1,3),1),),(1,1)),1)

    def test_exact_parameters_stale_sources_and_existing_outputs(self):
        for n in (0,1,2,255,1.0,True):
            with self.assertRaises((ValueError,TypeError)):P.validate_D(n)
        self.assertEqual(P.validate_D(256),16)
        with self.assertRaises(FileExistsError):P.refuse_existing(P.HERE)
        hashes=P.current_source_hashes();self.assertTrue(P.check_source_hashes(hashes))
        name=next(iter(hashes))
        def stale(path):
            raw=path.read_bytes()
            return raw+b' altered in memory' if str(path.relative_to(P.ROOT))==name else raw
        with self.assertRaisesRegex(RuntimeError,'Source bytes changed'):P.check_source_hashes(hashes,stale)

if __name__=='__main__':unittest.main(verbosity=2)
