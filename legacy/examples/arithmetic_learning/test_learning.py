#!/usr/bin/env python3
"""Focused independent finite-field, loss, mask, stale-input and replay controls."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json
import os
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parent))
import learn as L

class ArithmeticLearningTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=L.build_data()

    def test_full_activated_ideal_support_and_counts(self):
        d=self.data
        self.assertEqual(len(d['columns']),15)
        self.assertEqual(len(d['pairs']),210)
        self.assertEqual([d['row_cases'][s]['row_count'] for s in ('all_literal','guaranteed_nonprincipal')],[2262,2148])
        for c in d['columns']:
            ps=c['primes']; N=c['norm']; ds=[]
            for mask in range(1<<len(ps)):
                n=1
                for j,(a,b) in enumerate(ps):
                    if mask>>j&1:n*=a*a-a*b+b*b
                ds.append(n)
            self.assertEqual(sum(n>60 and N>60*n for n in ds),c['r_U'])
            self.assertEqual(len(set(ps)),len(ps))
        self.assertEqual(len({tuple(c['generator']) for c in d['columns']}),15)
        self.assertLess(len({c['norm'] for c in d['columns']}),15) # norm-only keys lose ideals

    def test_independent_all_local_symbols_and_all_Gram_targets(self):
        # Independent modular exponentiation. No ResidueField, prime_symbol,
        # scalar_symbol, author multiplication, or phase table is used here.
        d=self.data; primes=d['prime_ideals']; tables=[]
        for a,b in primes:
            p=a*a-a*b+b*b; omega=(-a*pow(b,-1,p))%p
            roots=[pow((1+omega)%p,e,p) for e in range(6)]
            self.assertEqual(len(set(roots)),6)
            tables.append((p,omega,{z:e for e,z in enumerate(roots)}))
        independent=[]; local_cases=0
        prime_index={tuple(p):i for i,p in enumerate(primes)}
        for row in d['rows']:
            a,b=row['element']; exponents=[]
            for p,omega,roots in tables:
                z=(a+b*omega)%p
                exponents.append(None if z==0 else roots[pow(z,(p-1)//6,p)])
                local_cases+=1
            self.assertEqual(exponents,row['prime_phases'])
            vals=[]
            for c in d['columns']:
                es=[exponents[prime_index[tuple(p)]] for p in c['primes']]
                vals.append(None if None in es else sum(es)%6)
            self.assertEqual(vals,row['raw_column_phases']); independent.append(vals)
        self.assertEqual(local_cases,2262*14)
        # Twice the independent rational/sqrt(-3) coordinates.
        roots=((2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1))
        for case in d['row_cases'].values():
            for i,j in product(range(15),repeat=2):
                x=y=0
                for row in case['row_indices']:
                    a,b=independent[row][i],independent[row][j]
                    if a is None or b is None:continue
                    xx,yy=roots[(a-b)%6];x+=xx;y+=yy
                self.assertEqual((x-y)%2,0)
                self.assertEqual((Q(x-y,2),Q(y)),case['Gamma_matrix'][i][j])

    def test_correct_complex_metric_and_gradient(self):
        z=(Q(2,3),Q(-4,5));w=(Q(7,3),Q(5,4))
        self.assertEqual(L.mul(z,L.conj(z)),(L.abs2(z),Q(0)))
        self.assertEqual(L.conj(L.mul(z,w)),L.mul(L.conj(z),L.conj(w)))
        self.assertEqual(L.abs2((Q(1),Q(1))),3)
        self.assertNotEqual(L.abs2((Q(1),Q(1))),2) # false Euclidean coordinate norm
        lam=Q(7,5);t=Q(1,17)
        for axis in (0,1):
            zp=list(z);zm=list(z);zp[axis]+=t;zm[axis]-=t
            central=lam*(L.abs2(zp)-L.abs2(zm))/(2*t)
            correct=lam*(2*z[axis]+z[1-axis])
            self.assertEqual(central,correct)
            self.assertNotEqual(central,2*lam*z[axis]) # wrong coordinate gradient

    def test_loss_is_full_sum_not_mean_or_real_part(self):
        g=[(Q(1),Q(1)),(Q(2),Q(-1))];t=[L.ZERO,L.ZERO];weights=[Q(2),Q(3)]
        self.assertEqual(L.full_loss(g,t,weights),15)
        self.assertNotEqual(L.full_loss(g,t,weights),Q(15,2))
        case=self.data['row_cases']['all_literal']; target=case['Gamma']
        real=[(a+b/2,Q(0)) for a,b in target]
        self.assertTrue(any(b for a,b in target))
        self.assertGreater(L.full_loss(real,target,[Q(1)]*len(target)),0)
        # Wrong metric underestimates a valid uniform complex error budget.
        self.assertGreater(L.abs2((Q(1),Q(1))),Q(1)**2+Q(1)**2)

    def test_metric_GD_and_ordinary_GD_contractions(self):
        target=[(Q(3),Q(2)),(Q(-1),Q(5))];g=[(Q(2),Q(-3)),(Q(7),Q(1))];weights=[Q(2),Q(7)]
        old=L.full_loss(g,target,weights); new=L.metric_step(g,target)
        self.assertEqual(4*L.full_loss(new,target,weights),old)
        out,eta=L.ordinary_step(g,target,weights);rho=1-min(weights)/(3*max(weights))
        self.assertEqual(eta,Q(2,21));self.assertLessEqual(L.full_loss(out,target,weights),rho*rho*old)
        self.assertNotEqual(out,new)

    def test_full_phase_orthogonality_and_restricted_feature_kernel(self):
        # Factor the exact finite geometric sum; every active orientation is distinct.
        for b in self.data['blocks']:
            orientations=b['orientations']
            for a,c in product(orientations,repeat=2):
                x=(Q(1),Q(0))
                for s,t in zip(a['signs'],c['signs']):
                    x=L.mul(x,L.scale(Q(1,6),L.total(L.PH[((s-t)*e)%6] for e in range(6))))
                self.assertEqual(x,L.ONE if a['mask']==c['mask'] else L.ZERO)
        restricted=next(b for b in self.data['blocks'] if len(b['orientations'])<2**len(b['q']))
        # K_J(0,0)=|J|, whereas the forbidden full-cube product is2^k.
        self.assertNotEqual(len(restricted['orientations']),2**len(restricted['q']))

    def test_raw_common_prime_zeros_and_literal_units(self):
        d=self.data;found=False
        for b in d['blocks']:
            if not b['h']:continue
            for row in d['rows']:
                u=row['element']
                if any(L.quotient(u,p) is not None for p in b['h']) and all(L.prime_symbol(p,u) is not None for p in b['q']):
                    pair=d['pairs'][b['orientations'][0]['pair']]
                    self.assertIsNone(row['raw_column_phases'][pair['m']]); self.assertIsNone(row['raw_column_phases'][pair['n']])
                    found=True;break
            if found:break
        self.assertTrue(found) # dropping h would restore a false nonzero value
        self.assertEqual(L.PH[0],(1,0));self.assertNotEqual(L.PH[0],L.ZERO)
        units=[r for r in d['rows'] if r['norm']==1]
        self.assertEqual(len(units),6)
        self.assertTrue(all(all(v is not None for v in row['raw_column_phases']) for row in units))
        G=d['row_cases']['all_literal']['Gamma_matrix']
        self.assertEqual(G[0][0][0],2262) # dropping unit rows gives2256, a different target
        self.assertTrue(any(row['outside_S_norm']==1 and row['norm']>1 for row in d['rows']))

    def test_signed_conductor_complex_profile_and_scalar_cancellation(self):
        d=self.data;case=d['row_cases']['all_literal']; W,cc,cm,lam=L.weights(d,'complex');target=case['Gamma']
        signed=L.total(L.scale(p['mu_q'],L.mul(a,x)) for p,a,x in zip(d['pairs'],cc,target))
        unsigned=L.total(L.mul(a,x) for a,x in zip(cc,target))
        self.assertNotEqual(signed,unsigned)
        self.assertTrue(any(p['mu_q']<0 and a!=L.ZERO and x!=L.ZERO for p,a,x in zip(d['pairs'],cc,target)))
        wrong=[]
        for p in d['pairs']:
            i,j=p['m'],p['n'];wrong.append(L.scale(d['columns'][i]['r_U']*d['columns'][j]['r_U'],L.mul(W[i],W[j])))
        self.assertNotEqual(L.total(L.mul(a,x) for a,x in zip(cc,target)),L.total(L.mul(a,x) for a,x in zip(wrong,target)))
        nonzero=[L.scale(p['mu_q'],a) for p,a in zip(d['pairs'],cc) if a!=L.ZERO]
        a,b=nonzero[:2];residual=[b,L.scale(-1,a)]
        self.assertEqual(L.add(L.mul(a,residual[0]),L.mul(b,residual[1])),L.ZERO)
        self.assertGreater(L.full_loss(residual,[L.ZERO,L.ZERO],[Q(1),Q(1)]),0)
        self.assertTrue(all(v>=1 for v in lam))

    def test_exact_tau_and_fresh_output_contract(self):
        self.assertEqual(L.parse_tau('1e-12'),Q(1,10**12))
        self.assertEqual(L.parse_tau('1/1000'),Q(1,1000))
        for bad in (0.1,1e-12,True,1,0,None):
            with self.assertRaises(TypeError):L.parse_tau(bad)
        for bad in ('0','-1','nan','inf','0/4'):
            with self.assertRaises((ValueError,ZeroDivisionError)):L.parse_tau(bad)
        with self.assertRaises(FileExistsError):L.refuse_existing(L.HERE)

    def test_stale_source_refusal_without_mutating_files(self):
        expected=L.source_hashes();self.assertTrue(L.check_sources(expected))
        first=next(iter(expected))
        def stale_reader(path):
            data=path.read_bytes()
            return data+b' altered' if str(path.relative_to(L.ROOT))==first else data
        with self.assertRaisesRegex(RuntimeError,'Stale source bytes'):L.check_sources(expected,stale_reader)

    @unittest.skipUnless(os.environ.get('ARITHMETIC_LEARNING_RUN'),'set ARITHMETIC_LEARNING_RUN to replay a completed immutable run')
    def test_complete_recorded_metric_trajectory_and_binding(self):
        path=Path(os.environ['ARITHMETIC_LEARNING_RUN']);self.assertTrue(L.verify_run(path))
        m=json.loads((path/'manifest.json').read_text());self.assertEqual(m['columns'],15)
        for summary in m['cases']:
            run=json.loads((path/summary['file']).read_text()); case=self.data['row_cases'][run['row_set']]
            target=case['Gamma'];weights=[Q(v) for v in run['positive_weights']]; previous=None;initial=None
            for state in run['metric_GD']['states']:
                g=[tuple(Q(x) for x in z) for z in state['coordinates']]
                if initial is None:initial=g
                if previous is not None:self.assertEqual(g,[tuple((x+y)/2 for x,y in zip(a,b)) for a,b in zip(previous,target)])
                loss=L.full_loss(g,target,weights);self.assertEqual(loss,Q(state['weighted_full_loss']))
                if state['step']>0:self.assertEqual(loss*4,Q(prev_state['weighted_full_loss']))
                previous=g;prev_state=state
            final=run['metric_GD']['states'][-1];self.assertTrue(final['accepted']);tau=Q(run['tau'])
            for key in ('certificate_CC_squared','certificate_CM_squared','uniform_coordinate_certificate_squared'):
                self.assertLessEqual(Q(final[key]),tau*tau)
            self.assertEqual(len(run['ordinary_GD']['states']),51)
            self.assertFalse(run['ordinary_GD']['requested_tau_certified'])

if __name__=='__main__':unittest.main(verbosity=2)
