#!/usr/bin/env python3
"""Exact ideal-convolution and sextic-mask diagnostics in Z[omega].

Every good ideal is represented once by its primary generator. The finite
annular profile is rational, not a claimed analytic smooth-weight estimate.
No random sampling, learned input, numerical zero or GRH hypothesis is used.
"""
from pathlib import Path
from itertools import product
from functools import lru_cache
from math import isqrt
from fractions import Fraction
import argparse,json
from check_reciprocity_period import emul,norm,prime,prime_symbol,power

ROOT=Path(__file__).resolve().parents[1]
PHASES=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))

def elements(X,primary=False):
    B=isqrt(2*X)+2
    return sorted(((a,b) for a in range(-B,B+1) for b in range(-B,B+1)
        if 0<norm((a,b))<=X and (not primary or (a%3==1 and b%3==0))),
        key=lambda x:(norm(x),x))

def quotient(x,y):
    q=norm(y);a,b=emul(x,(y[0]-y[1],-y[1]))
    return (a//q,b//q) if a%q==b%q==0 else None

def universe(X):
    gens=[g for g in elements(X,True) if norm(g)%2 and norm(g)%3]
    primegens=[g for g in gens if prime(norm(g)) or
        (g[1]==0 and prime(abs(g[0])) and abs(g[0])%3==2)]
    rows=[]
    for g in gens:
        remainder=g;f=[]
        for pi in primegens:
            e=0
            while (v:=quotient(remainder,pi)) is not None:
                remainder=v;e+=1
            if e:f.append((pi,e))
        assert remainder==(1,0),(g,remainder)
        mu=0 if any(e>1 for _,e in f) else (-1)**len(f)
        rows.append(dict(g=g,q=norm(g),f=tuple(f),mu=mu,sf=all(e==1 for _,e in f)))
    index={r['g']:i for i,r in enumerate(rows)}
    divs=[]
    for r in rows:
        out=[]
        for es in product(*(range(e+1) for _,e in r['f'])):
            g=(1,0)
            for (pi,_),e in zip(r['f'],es):g=emul(g,power(pi,e))
            assert norm(r['g'])==norm(g)*norm(quotient(r['g'],g))
            out.append(index[g])
        divs.append(out)
    return rows,index,divs,primegens

def scalar_symbol(f,x):
    out=0
    for pi,e in f:
        t=prime_symbol(pi,x)
        if t is None:return None
        out=(out+e*t)%6
    return out

def check(X=1024):
    ideals,index,divs,primegens=universe(X)
    pairs={i:[(d,index[quotient(n['g'],ideals[d]['g'])]) for d in divs[i]]
           for i,n in enumerate(ideals)}
    triples={i:[(a,b,c) for a,r in pairs[i] for b,c in pairs[r]] for i in range(len(ideals))}
    for i,ts in triples.items():
        for a,b,c in ts:assert emul(emul(ideals[a]['g'],ideals[b]['g']),ideals[c]['g'])==ideals[i]['g']
    cutoffs=[1,3,7,16,32];split={};group_checks=0
    for U in cutoffs:
        a=[r['mu'] if r['q']<=U else 0 for r in ideals]
        b=[r['mu']-a[i] for i,r in enumerate(ideals)]
        beta=[sum(a[x]*a[y] for x,y in pairs[i]) for i in range(len(ideals))]
        gu=[sum(b[d] for d in divs[i]) for i in range(len(ideals))]
        I=[sum(a[x]*a[y] for x,y,_ in triples[i]) for i in range(len(ideals))]
        II=[sum(b[x]*b[y] for x,y,_ in triples[i]) for i in range(len(ideals))]
        for i,n in enumerate(ideals):
            assert 2*a[i]-I[i]+II[i]==n['mu']
            assert I[i]==sum(beta[d] for d,c in pairs[i])
            assert II[i]==sum(b[d]*gu[c] for d,c in pairs[i])
            if n['q']>U:assert gu[i]==-sum(a[d] for d in divs[i])
            if n['sf']:
                count=sum(ideals[d]['q']<=U and ideals[c]['q']<=U for d,c in pairs[i])
                assert beta[i]==n['mu']*count
                for x,y,z in triples[i]:
                    sets=[set(pi for pi,_ in ideals[j]['f']) for j in (x,y,z)]
                    assert all(not sets[j]&sets[k] for j,k in [(0,1),(0,2),(1,2)])
                if U==1 and n['q']>1:assert I[i]==1 and II[i]==n['mu']+1>=0
            group_checks+=1
        split[U]=(a,I,II)
    energies=[];zero_tests=0
    for D,H in [(128,16),(256,32),(512,64)]:
        row=elements(H);columns=[i for i,r in enumerate(ideals) if r['sf'] and D<=r['q']<=2*D]
        for fixed_numerator in [(1,0),(2,0)]:
            nu={i:scalar_symbol(ideals[i]['f'],fixed_numerator) for i in columns}
            assert all(v is not None for v in nu.values())
            for U in [1,7,16,32]:
                a,I,II=split[U];sq=[0,0,0,0];unit=None
                for u in row:
                    amps=[[0,0] for _ in range(4)]
                    for i in columns:
                        n=ideals[i];phase=scalar_symbol(n['f'],u)
                        if phase is None:zero_tests+=1;continue
                        # Fixed rational finite diagnostic profile only.
                        w=((n['q']-D)*(2*D-n['q']))**2
                        root=PHASES[(nu[i]+phase)%6]
                        for j,c in enumerate([n['mu'],2*a[i],I[i],II[i]]):
                            amps[j][0]+=c*w*root[0];amps[j][1]+=c*w*root[1]
                    assert tuple(amps[0])==tuple(amps[1][k]-amps[2][k]+amps[3][k] for k in range(2))
                    for j,amp in enumerate(amps):sq[j]+=norm(amp)
                    if u==(1,0):unit=amps
                energies.append(dict(D=D,H=H,U=U,nu_numerator=fixed_numerator,
                    all_element_rows=len(row),squarefree_columns=len(columns),
                    normalized_energies=[str(Fraction(x,D**9)) for x in sq],
                    unit_row_weighted_numerators=unit))
    # Primitive oscillation and zero-preserving period are distinct even after
    # regrouping a*s. Finite exponent ledgers use the actual prime ideals.
    sf=[r for r in ideals if r['sf'] and r['q']>1][:30];conductors=0
    for n in sf:
        for t in sf:
            P={pi for pi,_ in n['f']};Q={pi for pi,_ in t['f']}
            gcdq=1;osc=1;period=1
            for pi in P&Q:gcdq*=norm(pi)
            for pi in P^Q:osc*=norm(pi)
            for pi in P|Q:period*=norm(pi)
            assert osc*gcdq*gcdq==n['q']*t['q']
            assert period*gcdq==n['q']*t['q']
            conductors+=1
    # Dropping total squarefreeness changes EACH piece, although the full
    # unrestricted convolution identity still cancels these contributions.
    pi=next(g for g in primegens if norm(g)==7);i=index[emul(pi,pi)]
    assert not ideals[i]['sf'] and split[1][1][i]==split[1][2][i]==1
    # The U=1 positivity proof cannot be recycled for a different cutoff.
    # Distinct conjugate primes over7 and one prime over13 give norm637.
    p13=next(g for g in primegens if norm(g)==13)
    j=index[emul((7,0),p13)]
    assert ideals[j]['sf'] and ideals[j]['mu']==-1
    assert split[7][1][j]==-1 and split[7][2][j]==-2
    return dict(passed=True,max_norm=X,good_ideals=len(ideals),including_inert_prime_ideals=True,
        cutoffs=cutoffs,coefficient_and_group_checks=group_checks,
        component_order=['original','2*short','type_I','type_II'],energies=energies,
        original_zero_encounters=zero_tests,conductor_pair_ledgers=conductors,
        nonsquarefree_piece_control=dict(generator=ideals[i]['g'],norm=49,I=1,II=1,mu=0),
        different_cutoff_sign_control=dict(generator=ideals[j]['g'],norm=637,U=7,I=-1,II=-2,mu=-1),
        scope='Exact finite ideal/character algebra; rational diagnostic W, principal and fixed Kummer nu=chi_n(2); no analytic mean-square certificate')

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=ROOT/'outputs/checks/2026-11-03-mobius-split/exact.json');args=p.parse_args()
    result=check();args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='energies'},indent=2))

if __name__=='__main__':main()
