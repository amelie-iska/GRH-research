#!/usr/bin/env python3
"""New exact finite checks for joint masked Gauss balance, not an analytic estimate."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from functools import lru_cache
from itertools import product
from collections import Counter
from math import gcd
import argparse, hashlib, json, time


def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a


def divexact(a,b):
    a=trim(a); b=trim(b); q=[0]*max(1,len(a)-len(b)+1)
    assert b[-1]==1
    while len(a)>=len(b):
        j=len(a)-len(b); c=a[-1]; q[j]=c
        for i,x in enumerate(b):a[j+i]-=c*x
        a=trim(a)
        if a==[0]:break
    assert a==[0], (a,b)
    return trim(q)


@lru_cache(None)
def cyclo(n):
    a=[-1]+[0]*(n-1)+[1]
    for d in range(1,n):
        if n%d==0:a=divexact(a,cyclo(d))
    return tuple(a)


class Ring:
    def __init__(self,n):
        self.n=n; self.mod=cyclo(n); self.d=len(self.mod)-1
        self.zero=(0,)*self.d; self.one=(1,)+(0,)*(self.d-1)
        self.zpowers=[self.one]
        for i in range(1,n):
            a=[0]+list(self.zpowers[-1]); self.zpowers.append(self.reduce(a))
        assert self.reduce([0]+list(self.zpowers[-1]))==self.one
    def reduce(self,a):
        a=list(a)
        if len(a)<self.d:a.extend([0]*(self.d-len(a)))
        for j in range(len(a)-1,self.d-1,-1):
            c=a[j]
            if c:
                for i,x in enumerate(self.mod):a[j-self.d+i]-=c*x
        return tuple(a[:self.d])
    def z(self,e):return self.zpowers[e%self.n]
    def add(self,a,b):return tuple(x+y for x,y in zip(a,b))
    def scale(self,c,a):return tuple(c*x for x in a)
    def mul(self,a,b):
        c=[0]*(2*self.d-1)
        for i,x in enumerate(a):
            if x:
                for j,y in enumerate(b):
                    if y:c[i+j]+=x*y
        return self.reduce(c)
    def total(self,it):
        a=self.zero
        for b in it:a=self.add(a,b)
        return a
    def prod(self,it):
        a=self.one
        for b in it:a=self.mul(a,b)
        return a


class Field:
    def __init__(self,p,inert=False):
        self.p=p; self.inert=inert
        self.xs=list(product(range(p),repeat=2)) if inert else list(range(p))
        self.zero=(0,0) if inert else 0; self.one=(1,0) if inert else 1
        self.Q=len(self.xs)
        for g in self.xs:
            if g==self.zero:continue
            vals=[]; x=self.one
            for i in range(self.Q-1):vals.append(x);x=self.mul(x,g)
            if len(set(vals))==self.Q-1 and x==self.one:
                self.generator=g; self.logs={z:i for i,z in enumerate(vals)};break
        assert len(self.logs)==self.Q-1
    def add(self,a,b):
        if self.inert:return ((a[0]+b[0])%self.p,(a[1]+b[1])%self.p)
        return (a+b)%self.p
    def neg(self,a):
        if self.inert:return ((-a[0])%self.p,(-a[1])%self.p)
        return (-a)%self.p
    def mul(self,a,b):
        if self.inert:
            x,y=a;z,w=b
            return ((x*z-y*w)%self.p,(x*w+y*z-y*w)%self.p)
        return a*b%self.p
    def trace(self,a):return (2*a[0]-a[1])%self.p if self.inert else a


def local_checks():
    reports=[]; assertions=0
    for p,inert in [(7,False),(13,False),(19,False),(5,True)]:
        F=Field(p,inert); R=Ring(6*p)
        chi=lambda z,j: R.z(p*j*F.logs[z])
        def G(j,t):
            return R.total(R.z(p*j*F.logs[z]+6*F.trace(F.mul(t,z))) for z in F.logs)
        taus={j:G(j,F.one) for j in range(1,6)}
        for j in range(1,7):
            for t in F.xs:
                value=G(j,t)
                if j==6:expected=R.scale(F.Q-1 if t==F.zero else -1,R.one)
                elif t==F.zero:expected=R.zero
                else:expected=R.mul(chi(t,-j),taus[j])
                assert value==expected; assertions+=1
        minus=F.neg(F.one)
        for eps in [1,5]:
            lhs=R.prod(taus[(j*eps)%6] for j in range(1,6))
            rhs=R.scale(F.Q**2,R.mul(chi(minus,3),taus[3]))
            assert lhs==rhs; assertions+=1
        for j in [1,2,3]:
            assert R.mul(taus[j],taus[6-j])==R.scale(F.Q,chi(minus,j));assertions+=1
        J=R.total(R.mul(chi(z,1),chi(F.add(F.one,F.neg(z)),2))
                  for z in F.logs if F.add(F.one,F.neg(z))!=F.zero)
        assert R.prod([taus[1],taus[2],taus[3]])==R.scale(F.Q,R.mul(chi(minus,3),J));assertions+=1
        reports.append(dict(characteristic=p,field_order=F.Q,inert=inert,
                            generator=F.generator,cyclotomic_order=R.n,degree=R.d))
    return dict(assertions=assertions,fields=reports)


def masked_eisenstein_crt_checks():
    # q=(3+omega), h=(4+omega), L=(11+6omega). Norms 7,13,91.
    # O/L=Z/91 via omega -> 74. Tr(x/(delta*(11+6omega)))=-6*x/91.
    # alpha=4+omega=1 mod q; beta=3+omega=-1 mod h.
    F=Field(7); R=Ring(546); L=91
    assert (3+74)%7==0 and (4+74)%13==0
    assert (4+74)%7==1 and (3+74)%13==12
    units=[x for x in range(L) if gcd(x,L)==1]
    def phase(e):return R.z(91*e)
    taus={j:R.total(R.z(91*j*F.logs[x]-78*x) for x in F.logs) for j in range(1,6)}
    G={}
    assertions=0
    for j in range(1,7):
        for k in range(L):
            value=R.total(R.z(91*j*F.logs[x%7]-36*k*x) for x in units)
            G[j%6,k]=value
            ch=12 if k%13==0 else -1
            if j==6:expected=R.scale(ch*(6 if k%7==0 else -1),R.one)
            elif k%7==0:expected=R.zero
            else:expected=R.scale(ch,R.mul(taus[j],phase(-j*F.logs[k%7])))
            assert value==expected,(j,k);assertions+=1
    test_k=[(1,2,3,4,5,0),(13,26,39,52,65,13),(1,13,2,26,3,7),
            (7,1,2,3,4,1),(1,2,3,4,7,13),(90,89,88,87,86,85)]
    for eps in [1,5]:
        for ks in test_k:
            lhs=R.prod(G[(eps*j)%6,ks[j-1]] for j in range(1,7))
            if any(k%7==0 for k in ks[:5]):rhs=R.zero
            else:
                K=1
                for j,k in enumerate(ks[:5],1):K=K*pow(k,j,7)%7
                ram=1
                for k in ks[:5]:ram*=12 if k%13==0 else -1
                ram*=(12 if ks[5]%13==0 else -1)*(6 if ks[5]%7==0 else -1)
                # xi_q(-alpha)=xi_q(-1)=-1, since alpha=1 mod q.
                rhs=R.scale(-49*ram,R.mul(taus[3],phase(-eps*F.logs[K])))
            assert lhs==rhs,(eps,ks);assertions+=1
    return dict(assertions=assertions,q_generator=[3,1],h_generator=[4,1],
                L_generator=[11,6],norms=[7,13,91],omega_mod_L=74,
                additive_exponent='-6*k*x/91',tau_q_exponent='-x/7',
                full_period_transforms=546,mixed_frequency_tuples=len(test_k)*2,
                cyclotomic_order=R.n,cyclotomic_degree=R.d)


def composite_orientation_checks():
    # q=(3+omega)(4+omega)=(11+6omega), h=1.
    F7=Field(7);F13=Field(13);R=Ring(546); C=Ring(6)
    units=[x for x in range(91) if gcd(x,91)==1]
    orientations=list(product([1,5],repeat=2))
    def exponent(x,orientation):return (orientation[0]*F7.logs[x%7]+orientation[1]*F13.logs[x%13])%6
    def tau(j,orientation):return R.total(R.z(91*j*exponent(x,orientation)-36*x) for x in units)
    xi=tau(3,(1,1));assertions=0
    for orientation in orientations:
        lhs=R.prod(tau(j,orientation) for j in range(1,6))
        assert lhs==R.scale(-91**2,xi);assertions+=1
    table=[[C.z(-exponent(x,ori)) for ori in orientations] for x in units]
    # Exact orthogonality of all four original orientations on unit K.
    for i,j in product(range(4),repeat=2):
        val=C.total(C.z(-exponent(x,orientations[i])+exponent(x,orientations[j])) for x in units)
        assert val==C.scale(72 if i==j else 0,C.one);assertions+=1
    # An actual nonconstant complex vector in Z[zeta6], no sign-covariance fixture.
    coeff=[C.add(C.one,C.z(1)),C.add(C.scale(2,C.one),C.scale(-1,C.z(1))),
           C.add(C.scale(-1,C.one),C.scale(2,C.z(1))),C.scale(3,C.one)]
    def conj(a):return C.total(C.scale(c,C.z(-i)) for i,c in enumerate(a))
    vals=[C.total(C.mul(a,z) for a,z in zip(coeff,row)) for row in table]
    normlhs=C.total(C.mul(a,conj(a)) for a in vals)
    normrhs=C.scale(72,C.total(C.mul(a,conj(a)) for a in coeff))
    assert normlhs==normrhs;assertions+=1
    diagonal=[x for x in units if F7.logs[x%7]%3==0 and F13.logs[x%13]%3==0]
    assert len(diagonal)==8;assertions+=1
    assert all(len(set(row))==1 for x,row in zip(units,table) if x in diagonal);assertions+=1
    assert all(len(set(row))>1 for x,row in zip(units,table) if x not in diagonal);assertions+=1
    # Exhaustive five-unit-frequency product-map fibers for local q=7.
    fibers=Counter()
    for ks in product(range(1,7),repeat=5):
        K=1
        for j,k in enumerate(ks,1):K=K*pow(k,j,7)%7
        fibers[K]+=1
    assert set(fibers.values())=={6**4} and len(fibers)==6;assertions+=1
    return dict(assertions=assertions,q_generator=[11,6],q_norm=91,orientations=4,
                uniform_unit_products=72,orthogonality_entries=16,
                cubic_coherent_diagonal=diagonal,diagonal_cardinality=8,
                exact_parseval_norm=list(normlhs),
                local_five_frequency_tuples=6**5,fiber_cardinality=6**4)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();assert not args.output.exists(),'Preserve every previous output'
    t=time.time()
    report=dict(passed=True,local=local_checks(),masked_crt=masked_eisenstein_crt_checks(),
                composite_orientation=composite_orientation_checks())
    report['assertions']=sum(report[k]['assertions'] for k in ['local','masked_crt','composite_orientation'])
    report['elapsed_seconds']=round(time.time()-t,3)
    report['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    report['scope']='Exact finite Gauss/CRT/orientation identities only; not an incomplete signed-moment estimate, exponent saving, Lean or GRH result.'
    with args.output.open('x') as f:json.dump(report,f,indent=2);f.write('\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
