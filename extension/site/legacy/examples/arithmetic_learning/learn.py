#!/usr/bin/env python3
"""Exact finite Fourier-feature learning of actual coupled sextic correlations.

Metric GD on the full positive weighted complex loss; no GRH/PSD/global claim.
"""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from itertools import product
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
HELPERS = [ROOT/'scripts'/p for p in ('check_mobius_split.py', 'check_reciprocity_period.py', 'check_finite_correlation.py')]
IMPORT_HASHES = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in HELPERS}
sys.path.insert(0, str(ROOT/'scripts'))
from check_mobius_split import elements, quotient, scalar_symbol
from check_reciprocity_period import norm, prime, prime_symbol, emul

D, U, H = 6000, 60, 625
SEED = 20261105
NORMS = (7507, 7519, 8281, 10507)
PRIME_NORMS = (7, 13, 19, 73, 79, 103, 7507)
PH = ((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
ZERO = (Q(0), Q(0))
ONE = (Q(1), Q(0))
SCOPE = ('Fixed finite original-family coupled-character Fourier readout on the complete '
         '15 active squarefree columns of an explicitly specified smooth four-bump profile; '
         'literal rows and a separately labelled guaranteed nonprincipal subset. '
         'No asymptotic saving, generalization, PSD/determinant, Lean, quantum or GRH theorem.')

def add(a,b): return a[0]+b[0], a[1]+b[1]
def sub(a,b): return a[0]-b[0], a[1]-b[1]
def scale(t,a): return t*a[0], t*a[1]
def conj(a): return a[0]+a[1], -a[1]
def mul(a,b): return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]+a[1]*b[1]
def abs2(a): return a[0]*a[0]+a[0]*a[1]+a[1]*a[1]
def total(xs):
    out = ZERO
    for x in xs: out = add(out,x)
    return out

def encoded(x):
    if isinstance(x, Q): return str(x)
    if isinstance(x, Path): return str(x)
    raise TypeError(type(x).__name__)

def json_bytes(x): return (json.dumps(x, indent=2, default=encoded, sort_keys=True)+'\n').encode()
def digest(data): return hashlib.sha256(data).hexdigest()
def source_paths(): return [HERE/'learn.py', HERE/'test_learning.py', HERE/'README.md', *HELPERS]
def source_hashes(): return {str(p.relative_to(ROOT)): digest(p.read_bytes()) for p in source_paths()}
def check_sources(expected, reader=None):
    reader = reader or (lambda p: p.read_bytes())
    changed = [name for name, sha in expected.items() if digest(reader(ROOT/name)) != sha]
    if changed: raise RuntimeError('Stale source bytes: '+', '.join(changed))
    return True

def parse_tau(value):
    if type(value) not in (str, Q): raise TypeError('tau must be exact Fraction or rational text; binary floats are refused')
    if isinstance(value,str) and (len(value)>256 or not re.fullmatch(r'[+]?\d+(?:/\d+|(?:\.\d*)?(?:[eE][+-]?\d+)?)?',value)):
        raise ValueError('tau must be positive exact rational text')
    tau = Q(value)
    if tau <= 0: raise ValueError('tau must be strictly positive')
    return tau

def refuse_existing(output):
    if output.exists(): raise FileExistsError('Refusing existing output; preserve prior progress: '+str(output))

def strip_S(u):
    for p in ((2,0),(1,-1)):
        while (v := quotient(u,p)) is not None: u=v
    return u

def subset_divisor_norms(ps):
    out=[]
    for mask in range(1<<len(ps)):
        v=1
        for j,p in enumerate(ps):
            if mask>>j&1: v*=norm(p)
        out.append(v)
    return out

def columns():
    # Exhaust all primary generators at the four activated norms. No norm-only ideal keys.
    gens = elements(2*D, True)
    primes = [g for g in gens if norm(g) in PRIME_NORMS]
    assert len(primes)==14 and all(prime(norm(p)) for p in primes)
    out=[]
    for g in gens:
        if norm(g) not in NORMS: continue
        rem=g; fs=[]; squarefree=True
        for p in primes:
            e=0
            while (v:=quotient(rem,p)) is not None: rem=v; e+=1
            if e: fs.append(p); squarefree &= e==1
        assert rem==(1,0), (g,rem)
        if not squarefree: continue
        fs=tuple(sorted(fs)); ds=subset_divisor_norms(fs); N=norm(g)
        r=sum(d>U and N//d>U for d in ds)
        assert N%2 and N%3
        out.append(dict(id=len(out),generator=g,norm=N,primes=fs,mu=(-1)**len(fs),r_U=r,divisor_norms=ds))
    assert Counter(c['norm'] for c in out)==Counter({7507:2,7519:4,8281:1,10507:8})
    assert {c['r_U'] for c in out}=={0,2,4}
    assert all(c['r_U']==(0 if c['norm']==7507 else 4 if c['norm']==8281 else 2) for c in out)
    return out, sorted({p for c in out for p in c['primes']})

def build_data():
    check_sources(IMPORT_HASHES)
    assert Q(2*D,7)<=U*U<=D
    cs,ps=columns(); rows=elements(H)
    assert len(rows)==2262 and sum(norm(u)==1 for u in rows)==6
    prime_phases=[[prime_symbol(p,u) for p in ps] for u in rows]
    pi={p:i for i,p in enumerate(ps)}
    raw=[]
    for vals in prime_phases:
        line=[]
        for c in cs:
            es=[vals[pi[p]] for p in c['primes']]
            line.append(None if None in es else sum(es)%6)
        raw.append(line)
    blocks={}; pairs=[]
    for i,j in product(range(len(cs)),repeat=2):
        if i==j: continue
        A,B=set(cs[i]['primes']),set(cs[j]['primes'])
        h,q=tuple(sorted(A&B)),tuple(sorted(A^B)); r=A-B
        key=(h,q)
        if key not in blocks:
            blocks[key]=dict(id=len(blocks),h=h,q=q,Nh=prod_norm(h),Nq=prod_norm(q),phi_q=prod_minus_one(q),phase_group_size=6**len(q),orientations=[])
        block=blocks[key]
        mask=sum(1<<k for k,p in enumerate(q) if p in r)
        pair=dict(id=len(pairs),m=i,n=j,block=block['id'],orientation_mask=mask,mu_q=(-1)**len(q))
        assert cs[i]['mu']*cs[j]['mu']==pair['mu_q']
        block['orientations'].append(dict(pair=pair['id'],mask=mask,signs=[1 if p in r else -1 for p in q]))
        pairs.append(pair)
    assert len(pairs)==210
    bs=list(blocks.values())
    assert all(len({o['mask'] for o in b['orientations']})==len(b['orientations']) for b in bs)
    cases={}
    for name,indices in [('all_literal',list(range(len(rows)))),('guaranteed_nonprincipal',[i for i,u in enumerate(rows) if norm(strip_S(u))>1])]:
        if name=='guaranteed_nonprincipal': assert len(indices)==2148
        G=[]
        for i in range(len(cs)):
            line=[]
            for j in range(len(cs)):
                counts=[0]*6
                for row in indices:
                    a,b=raw[row][i],raw[row][j]
                    if a is not None and b is not None: counts[(a-b)%6]+=1
                line.append(total(scale(n,PH[e]) for e,n in enumerate(counts)))
            G.append(line)
        assert all(G[i][j]==conj(G[j][i]) for i,j in product(range(len(cs)),repeat=2))
        histograms=[]
        # Each histogram comes from all literal admissible rows; no sampled feature loss.
        for b in bs:
            hist=Counter(); invalid=0
            for row in indices:
                u=rows[row]
                if any(quotient(u,p) is not None for p in b['h']): invalid+=1; continue
                es=tuple(prime_phases[row][pi[p]] for p in b['q'])
                if None in es: invalid+=1; continue
                hist[es]+=1
            histograms.append(dict(block=b['id'],invalid_rows=invalid,cells=[dict(phase=e,count=n) for e,n in sorted(hist.items())]))
            assert sum(hist.values())+invalid==len(indices)
            for orientation in b['orientations']:
                p=pairs[orientation['pair']]
                got=total(scale(n,PH[sum(s*e for s,e in zip(orientation['signs'],phase))%6]) for phase,n in hist.items())
                assert got==G[p['m']][p['n']], (name,b['id'],p['id'])
        cases[name]=dict(row_indices=indices,row_count=len(indices),units=sum(norm(rows[i])==1 for i in indices),raw_zero_entries=sum(raw[i][j] is None for i in indices for j in range(len(cs))),Gamma_matrix=G,Gamma=[G[p['m']][p['n']] for p in pairs],histograms=histograms)
    return dict(D=D,U=U,H=H,S='prime ideals above2and3',nu='principal',columns=cs,prime_ideals=ps,rows=[dict(element=u,norm=norm(u),outside_S_norm=norm(strip_S(u)),prime_phases=p,raw_column_phases=r) for u,p,r in zip(rows,prime_phases,raw)],blocks=bs,pairs=pairs,row_cases=cases,coefficient_scope='ALL squarefree good ideal columns at the four activated integer norms, and no other integer norm is active',nonprincipal_scope='Guaranteed nonprincipal subset only; the114 outside-S-unit literal rows are omitted without asserting their principal/nonprincipal classification')

def prod_norm(ps):
    out=1
    for p in ps: out*=norm(p)
    return out

def prod_minus_one(ps):
    out=1
    for p in ps: out*=norm(p)-1
    return out

def nodal_weights(cs,profile):
    if profile not in ('real','complex'): raise ValueError('Unknown profile')
    # W(y)=sum_N w_N phi(4*(6000*y-N)); supports disjoint. Integer-norm samples exact.
    return [(Q(1), Q(0) if profile=='real' else Q(4*c['norm']-5*D,D)) for c in cs]

def weights(data,profile):
    cs=data['columns']; W=nodal_weights(cs,profile); dc=[]; dm=[]
    for p in data['pairs']:
        i,j=p['m'],p['n']; w=mul(W[i],conj(W[j]))
        dc.append(scale(cs[i]['r_U']*cs[j]['r_U'],w)); dm.append(scale(cs[i]['r_U'],w))
    lam=[Q(1)+abs2(a)+abs2(b) for a,b in zip(dc,dm)]
    return W,dc,dm,lam

def initial_state(pairs,seed=SEED):
    values={}
    for p in pairs:
        i,j=p['m'],p['n']
        if i<j:
            h=hashlib.sha256(f'{seed}:{i}:{j}'.encode()).digest()
            values[i,j]=(Q(int.from_bytes(h[:4],'big')%19-9,8),Q(int.from_bytes(h[4:8],'big')%19-9,8))
            values[j,i]=conj(values[i,j])
    return [values[p['m'],p['n']] for p in pairs]

def full_loss(g,target,lam): return sum((w*abs2(sub(x,y)) for x,y,w in zip(g,target,lam)),Q(0))
def metric_step(g,target): return [scale(Q(1,2),add(x,y)) for x,y in zip(g,target)]
def ordinary_step(g,target,lam):
    eta=Q(2,3)/max(lam)
    out=[]
    for x,y,w in zip(g,target,lam):
        a,b=sub(x,y); grad=(a+b/2,a/2+b)
        out.append(sub(x,scale(eta*w,grad)))
    return out,eta

def signed_readout(data,case,W,d,g,kind):
    cs=data['columns']; G=case['Gamma_matrix']
    diagonal=sum((Q(cs[i]['r_U']**2 if kind=='CC' else cs[i]['r_U'])*abs2(W[i])*G[i][i][0] for i in range(len(cs))),Q(0))
    signed=add((diagonal,Q(0)),total(scale(p['mu_q'],mul(a,x)) for p,a,x in zip(data['pairs'],d,g)))
    return scale(Q(1,D),signed)

def direct_readouts(data,case,W):
    cs=data['columns']; cc=mm=ZERO; cm=ZERO
    for row in case['row_indices']:
        es=data['rows'][row]['raw_column_phases']; C=M=ZERO
        for c,w,e in zip(cs,W,es):
            if e is None: continue
            v=scale(c['mu'],mul(w,PH[e])); M=add(M,v); C=add(C,scale(c['r_U'],v))
        cc=add(cc,(abs2(C),Q(0))); mm=add(mm,(abs2(M),Q(0))); cm=add(cm,mul(C,conj(M)))
    return dict(CC=scale(Q(1,D),cc),CM=scale(Q(1,D),cm),MM=scale(Q(1,D),mm))

def finite_feature_value(block,coefficients,phase):
    if len(phase)!=len(block['q']): raise ValueError('Feature phase dimension mismatch')
    return total(mul(coefficients[o['pair']],PH[-sum(s*e for s,e in zip(o['signs'],phase))%6]) for o in block['orientations'])

def feature_samples(data,g,target):
    out=[]
    for b in data['blocks']:
        k=len(b['q']); phases=sorted({(0,)*k,(1,)*k,tuple(j%6 for j in range(k)),tuple(3 if j%2 else 0 for j in range(k))})
        out.append(dict(block=b['id'],phase_group_size=b['phase_group_size'],active_orientation_count=len(b['orientations']),values=[dict(phase=e,prediction=finite_feature_value(b,g,e),target=finite_feature_value(b,target,e)) for e in phases]))
    return out

def train_case(data,row_name,profile,tau,seed,input_sha):
    tau=parse_tau(tau); case=data['row_cases'][row_name]; target=case['Gamma']; W,dc,dm,lam=weights(data,profile)
    Kcc=sum((abs2(d)/w for d,w in zip(dc,lam)),Q(0)); Kcm=sum((abs2(d)/w for d,w in zip(dm,lam)),Q(0))
    exact=direct_readouts(data,case,W)
    assert exact['CC']==signed_readout(data,case,W,dc,target,'CC')
    assert exact['CM']==signed_readout(data,case,W,dm,target,'CM')
    g=initial_state(data['pairs'],seed); states=[]; previous=None; steps=0
    while True:
        L=full_loss(g,target,lam)
        if previous is not None: assert L*4==previous
        predcc=signed_readout(data,case,W,dc,g,'CC'); predcm=signed_readout(data,case,W,dm,g,'CM')
        errcc=abs2(sub(predcc,exact['CC'])); errcm=abs2(sub(predcm,exact['CM']))
        boundcc=Kcc*L/D**2; boundcm=Kcm*L/D**2; uniform=L/min(lam)
        assert errcc<=boundcc and errcm<=boundcm
        assert all(abs2(sub(a,b))<=uniform for a,b in zip(g,target))
        ok=boundcc<=tau*tau and boundcm<=tau*tau and uniform<=tau*tau
        states.append(dict(step=steps,coordinates=g,weighted_full_loss=L,predicted_CC=predcc,predicted_CM=predcm,actual_error_CC_squared=errcc,actual_error_CM_squared=errcm,certificate_CC_squared=boundcc,certificate_CM_squared=boundcm,uniform_coordinate_certificate_squared=uniform,accepted=ok))
        if ok: break
        previous=L; g=metric_step(g,target); steps+=1
        if steps>10000: raise RuntimeError('Requested exact-resource budget exceeded, no certification claim')
    assert not any(s['accepted'] for s in states[:-1])
    assert all(g[p['id']]==conj(g[next(t['id'] for t in data['pairs'] if t['m']==p['n'] and t['n']==p['m'])]) for p in data['pairs'])
    # Execute actual ordinary-coordinate GD too, without claiming it reaches tau.
    og=initial_state(data['pairs'],seed); ordinary=[]; rho=Q(1)-min(lam)/(3*max(lam))
    for step in range(51):
        L=full_loss(og,target,lam)
        ordinary.append(dict(step=step,coordinates=og,weighted_full_loss=L))
        if step<50:
            nxt,eta=ordinary_step(og,target,lam)
            assert full_loss(nxt,target,lam)<=rho*rho*L
            og=nxt
    unsignedcc=scale(Q(1,D),total(mul(d,x) for d,x in zip(dc,target)))
    signedoffcc=scale(Q(1,D),total(scale(p['mu_q'],mul(d,x)) for p,d,x in zip(data['pairs'],dc,target)))
    assert unsignedcc!=signedoffcc
    negatives=[p['id'] for p,d,x in zip(data['pairs'],dc,target) if p['mu_q']==-1 and d!=ZERO and x!=ZERO]
    assert negatives
    return dict(schema='arithmetic-learning-case-v1',scope=SCOPE,input_sha256=input_sha,row_set=row_name,profile=profile,seed=seed,initialization='sha256(seed:m:n), two signed integers mod19 divided by8, conjugate reverse orientations',tau=tau,coordinates_basis='a+b*zeta6, |.|^2=a^2+ab+b^2',model='F_g(e)=sum_active_orientation g_r conjugate(theta_r(e)); readout of full finite feature projection equals g_r',loss='sum_all210activeorderedorientations lambda_r |g_r-Gamma_r|^2; no scalar-only fitting',positive_weights=lam,weights_CC=dc,weights_CM=dm,K_CC_squared=Kcc,K_CM_squared=Kcm,exact=exact,metric_GD=dict(type='preconditioned gradient of L/2 in block metric lambda_i*M, M=[[1,1/2],[1/2,1]]',alpha=Q(1,2),update='g_next=(g+Gamma)/2',updates_executed=steps,states=states,termination='For each fixed finite exact target and tau>0, L_T=4^-T L0, hence all finite rational squared thresholds are met after finitely many updates; no conductor/range/runtime uniformity'),ordinary_GD=dict(type='independent real-coordinate gradient of L/2, untied orientation parameters',eta=eta,rho=rho,updates_executed=50,budget_limited=True,requested_tau_certified=False,states=ordinary),feature_predictions=feature_samples(data,g,target),negative_q_nonzero_CC_pair_ids=negatives,negative_control_unsigned_offdiag_CC=unsignedcc,signed_offdiag_CC=signedoffcc)

def write_new(path,obj):
    with path.open('xb') as f: f.write(json_bytes(obj))

def run(output,tau='1e-12',seed=SEED):
    output=Path(output); refuse_existing(output); tau=parse_tau(tau)
    sources=source_hashes(); check_sources(IMPORT_HASHES)
    data=build_data(); payload=json_bytes(data); input_sha=digest(payload)
    output.mkdir(parents=True,exist_ok=False)
    with (output/'input.json').open('xb') as f:f.write(payload)
    summaries=[]
    for row_name,profile in product(('all_literal','guaranteed_nonprincipal'),('real','complex')):
        case=train_case(data,row_name,profile,tau,seed,input_sha)
        filename=f'{row_name}-{profile}.json'; write_new(output/filename,case)
        final=case['metric_GD']['states'][-1]
        summaries.append(dict(file=filename,row_set=row_name,profile=profile,updates=case['metric_GD']['updates_executed'],accepted=final['accepted'],final_loss=final['weighted_full_loss'],certificate_CC_squared=final['certificate_CC_squared'],certificate_CM_squared=final['certificate_CM_squared'],uniform_certificate_squared=final['uniform_coordinate_certificate_squared'],ordinary_updates=50,ordinary_budget_limited=True))
        print(json.dumps(dict(case=filename,updates=summaries[-1]['updates'],accepted=True)),flush=True)
    check_sources(sources)
    files={p.name:digest(p.read_bytes()) for p in sorted(output.iterdir()) if p.is_file()}
    manifest=dict(schema='arithmetic-learning-run-v1',passed=True,scope=SCOPE,tau=tau,seed=seed,source_sha256=sources,input_sha256=input_sha,artifact_sha256=files,columns=len(data['columns']),offdiagonal_coordinates=len(data['pairs']),blocks=len(data['blocks']),cases=summaries,profile_formula='phi(t)=exp(1-1/(1-t^2)) if |t|<1 else0; W(y)=sum_(N in{7507,7519,8281,10507}) w_N phi(4*(6000*y-N)); w_N=1 for real, 1+zeta6*(4N-30000)/6000 for complex. Integer nodes other than the four norms have W=0 exactly.',metric_GD_total_updates=sum(s['updates'] for s in summaries),ordinary_GD_total_updates=200,source_bytes_checked_before_and_after=True,resource='stdlib exact Fraction CPU; no GPU, package installation or upstream model training')
    write_new(output/'manifest.json',manifest)
    verify_run(output)
    print(json.dumps(dict(passed=True,output=str(output),columns=manifest['columns'],coordinates=manifest['offdiagonal_coordinates'],metric_updates=manifest['metric_GD_total_updates'])),flush=True)
    return manifest

def verify_run(output):
    output=Path(output); manifest=json.loads((output/'manifest.json').read_text())
    check_sources(manifest['source_sha256'])
    for name,sha in manifest['artifact_sha256'].items():
        if digest((output/name).read_bytes())!=sha: raise RuntimeError('Stale artifact bytes: '+name)
    if digest((output/'input.json').read_bytes())!=manifest['input_sha256']: raise RuntimeError('Stale input bytes')
    return True

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    g=p.add_mutually_exclusive_group(required=True); g.add_argument('--output',type=Path); g.add_argument('--verify',type=Path)
    p.add_argument('--tau',default='1e-12'); p.add_argument('--seed',type=int,default=SEED)
    a=p.parse_args()
    if a.verify: verify_run(a.verify); print('Source/input/artifact binding verified')
    else: run(a.output,a.tau,a.seed)
