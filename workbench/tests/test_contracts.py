import copy
import itertools
import json
from pathlib import Path
import random
import subprocess
import sys
import unittest
from fractions import Fraction as F
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from contracts import certificate, replay, rational, mutate, seed_step, tropical_step, gentle_check, canonical, digest

class Contracts(unittest.TestCase):
    def test_heat_boundary(self):
        for r in ['0','1/100','1/4']:
            c=certificate('heat',{'r':r}); self.assertEqual(sum(map(F,c['claim']['weights'])),1);replay(c)
        for r in ['-1/100','251/1000','NaN','1e-9','1/0',True,0.1,'01','1/-2']:
            with self.subTest(r=r),self.assertRaises(ValueError): certificate('heat',{'r':r})
    def test_gain_witness(self):
        inp={'matrix':[['1/4','3/2'],['3/32','1/4']],'weights':['4','1'],'rate':'5/8'}
        c=certificate('gain',inp);self.assertEqual(c['claim']['row_slack'],['0/1','0/1'])
        inp['rate']='3/5'
        with self.assertRaises(ValueError): certificate('gain',inp)
    def test_rank_and_budget(self):
        self.assertEqual(certificate('rank',{'draws':4095,'exceedances':0})['claim']['p'],'1/4096')
        for e in [-1,4096,True,1.0]:
            with self.assertRaises(ValueError): certificate('rank',{'draws':4095,'exceedances':e})
        c=certificate('risk',{'tests':288,'per_test':'1/10000','drift':'1/100','alpha':'1/20'})
        self.assertEqual(c['claim']['upper_bound'],'97/2500')
        with self.assertRaises(ValueError): certificate('risk',{'tests':288,'per_test':'1/1000','drift':'0','alpha':'1/20'})
    def test_mutation_involution_and_seed(self):
        for a,b,c in itertools.product(range(-2,3),repeat=3):
            m=[[0,a,b],[-a,0,c],[-b,-c,0]]
            for k in range(3):
                p=mutate(m,k);self.assertEqual(mutate(p,k),m)
                x=[F(2),F(3),F(5)];p,y=seed_step(m,x,k)
                self.assertEqual(seed_step(p,y,k),(m,x))
                u=[-2,1,3];self.assertEqual(tropical_step(p,tropical_step(m,u,k),k),u)
    def test_A2_pentagon(self):
        b=[[0,1],[-1,0]];x=[F(2),F(5)]
        for k in [0,1,0,1,0]: b,x=seed_step(b,x,k)
        self.assertEqual(x,[F(5),F(2)]);self.assertEqual(b,[[0,-1],[1,0]])
    def test_gentle_and_finite_dimension(self):
        self.assertTrue(gentle_check(3,[[0,1],[1,2]],[[0,1]])['gentle'])
        self.assertTrue(gentle_check(3,[[0,1],[1,2],[2,0]],[[0,1],[1,2],[2,0]])['gentle'])
        self.assertFalse(gentle_check(3,[[0,1],[1,2],[2,0]],[])['finite_dimensional'])
        self.assertFalse(gentle_check(4,[[0,1],[0,2],[0,3]],[])['gentle'])
        with self.assertRaises(ValueError): gentle_check(3,[[0,1],[1,2]],[[1,0]])
    def test_tamper_and_limits(self):
        c=certificate('heat',{'r':'1/8'})
        for key in ['scope','schema','claim','kind','inputs']:
            t=copy.deepcopy(c);t[key]='forged'
            with self.assertRaises((ValueError,TypeError)): replay(t)
        with self.assertRaises(ValueError): certificate('heat',{'r':'1/8','extra':0})
        with self.assertRaises(ValueError): rational('1'*97)
        with self.assertRaises(ValueError): mutate([[0,True],[-1,0]],0)
        with self.assertRaises(ValueError): seed_step([[0,65],[-65,0]],[F(1),F(1)],0)
        self.assertEqual(len(digest(c)),64)
    def test_JS_python_parity(self):
        cases=[]
        for e in range(0,128,7):cases.append(['rank',{'draws':127,'exceedances':e}])
        for n in range(26):cases.append(['heat',{'r':f'{n}/100'}])
        rng=random.Random(196883)
        for _ in range(128):
            a,b,c=[rng.randrange(-3,4) for _ in range(3)]
            cases.append(['mutation',{'matrix':[[0,a,b],[-a,0,c],[-b,-c,0]],'seed':['2','3','5'],'vertex':rng.randrange(3)}])
        cases.extend([['gain',{'matrix':[['1/4','3/2'],['3/32','1/4']],'weights':['4','1'],'rate':'5/8'}],['risk',{'tests':288,'per_test':'1/10000','drift':'1/100','alpha':'1/20'}]])
        path=Path(__file__).resolve().parents[1]/'site/core.js'
        script='const fs=require("node:fs"),c=require(process.argv[1]);process.stdout.write(JSON.stringify(JSON.parse(fs.readFileSync(0,"utf8")).map(([k,v])=>c.certificate(k,v))));'
        out=subprocess.run(['node','-e',script,str(path)],input=json.dumps(cases),text=True,capture_output=True,check=True)
        self.assertEqual(json.loads(out.stdout),[certificate(k,v) for k,v in cases])
    def test_binary64(self):
        path=Path(__file__).resolve().parents[1]/'site/core.js'
        vals=[0,0.1,0.25,-0.125,1.234567890123,1e20,1e-20]
        script='const c=require(process.argv[1]);console.log(JSON.stringify(JSON.parse(process.argv[2]).map(c.binary64)));'
        out=subprocess.run(['node','-e',script,str(path),json.dumps(vals)],capture_output=True,text=True,check=True)
        self.assertEqual([F(s) for s in json.loads(out.stdout)],[F(v) for v in vals])

if __name__=='__main__': unittest.main(verbosity=2)
