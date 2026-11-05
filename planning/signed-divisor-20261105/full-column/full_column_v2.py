#!/usr/bin/env python3
"""New full-column exact signed ideal-divisor energies; Python standard library only."""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
from math import isqrt
from fractions import Fraction
from itertools import product
from collections import Counter
import argparse
import hashlib
import json
import resource
import time
import types

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
PHASES = ((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))
COMPONENTS = ('A','C','mu')
PAIRS = tuple(x+y for x in COMPONENTS for y in COMPONENTS)
HELPERS = {
 'examples/profile_uniformity/ideal_tower.py': '77dc26658a188ff6669bf577fcb8298b875ab2a5e4f8e0bfe628b94c9b9430d4',
 'examples/profile_uniformity/unit_profile.py': '66b117ef6536b52315c4a4f2b27f03d9f2d00ae60149e2b1a55c48f2e843b203',
}
OLD_INPUTS = {
 'outputs/checks/2026-11-05-signed-weights/joint-budget/fixed-profile-h1-v1.json': 'e4ebc41b81e040cd8cf7ba6ae2644bb725fba6c6939af25c7a8a1074289db35d',
 'web/data/fixed-h1.json': 'bdb7e93b2a1e377094b69ea5ababf5ad43d198365c47712aa767ca3791b9d8fe',
}
SCOPE = ('Exact finite original full-annular squarefree good ideal columns, common fixed smooth '
 'W_delta with delta=1/240000, principal nu, literal unit class1, explicitly declared '
 'nonprincipal row block. All ordered coprime pairs are covered by exact ideal-divisor '
 'inversion, including all raw zeros. No asymptotic saving, bounded-seminorm uniformity, '
 'GRH, learned model, conductor reduction, or positivity of the signed h1 slice is claimed.')

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(',',':'))+'\n').encode()

def write_new(path, value):
    with path.open('xb') as handle:
        handle.write(canonical(value))

def emul(x,y):
    a,b=x; c,d=y
    return (a*c-b*d, a*d+b*c-b*d)

def econj(x):
    return (x[0]-x[1], -x[1])

def eadd(x,y):
    return (x[0]+y[0], x[1]+y[1])

def enorm(x):
    return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]

def scale(x,k):
    return (k*x[0],k*x[1])

def subsets(ids):
    out=[()]
    for p in ids:
        out += [d+(p,) for d in out]
    return out

def finite_profile_node(D,N):
    if type(D) is not int or not 1 < D <= 60000:
        raise ValueError('fixed-profile flat-node certificate is restricted to integer 1<D<=60000')
    return int(D < N < 2*D)

def load_helpers(captured):
    modules={}
    for name,path in [('ideal_tower','examples/profile_uniformity/ideal_tower.py'),
                      ('full_column_captured_unit_profile','examples/profile_uniformity/unit_profile.py')]:
        raw=captured[path]
        if sha(raw) != HELPERS[path]:
            raise RuntimeError('Unapproved helper bytes: '+path)
        module=types.ModuleType(name)
        module.__file__=str(ROOT/path)
        sys.modules[name]=module
        exec(compile(raw,str(ROOT/path),'exec'), module.__dict__)
        modules[name]=module
    return modules['ideal_tower'],modules['full_column_captured_unit_profile']

def source_paths(old_rows=False):
    paths=[str(p.relative_to(ROOT)) for p in sorted(HERE.glob('*')) if p.is_file()]
    paths += list(HELPERS)
    if old_rows:
        paths += list(OLD_INPUTS)
    return paths

def capture_sources(output,old_rows=False):
    paths=source_paths(old_rows)
    captured={p:(ROOT/p).read_bytes() for p in paths}
    for p,h in {**HELPERS,**(OLD_INPUTS if old_rows else {})}.items():
        if sha(captured[p]) != h:
            raise RuntimeError('Frozen input changed: '+p)
    snapshot=output/'source-snapshot'
    snapshot.mkdir()
    for p,raw in captured.items():
        destination=snapshot/p
        destination.parent.mkdir(parents=True,exist_ok=True)
        with destination.open('xb') as handle:
            handle.write(raw)
    pins={p:dict(sha256=sha(raw),bytes=len(raw)) for p,raw in captured.items()}
    write_new(output/'source-freeze.json',dict(schema='full-column-source-freeze-v1',files=pins,
      captured_before_arithmetic=True,helper_execution='Captured pure modules, never old main/run/tests; no pycache',
      inputs_immutable=True))
    return captured,pins

def prime_catalog(cap,T,P,spf):
    bound=isqrt(2*cap)+2
    bynorm={}
    b0=-bound+((-(-bound))%3)
    for a in range(-bound,bound+1):
        if a%3 != 1:
            continue
        for b in range(b0,bound+1,3):
            N=a*a-a*b+b*b
            if 7 <= N <= cap and N%6==1 and spf[N]==N:
                bynorm.setdefault(N,[]).append((a,b))
    primes=[]
    split={}
    inert={}
    for p in range(5,cap+1):
        if spf[p] != p:
            continue
        if p%3==1:
            gens=sorted(bynorm.get(p,[]))
            assert len(gens)==2,(p,gens)
            for g in gens:
                primes.append(dict(generator=g,norm=p,rational_prime=p,kind='split'))
        elif p*p<=cap:
            g=(-p,0)
            assert g[0]%3==1
            primes.append(dict(generator=g,norm=p*p,rational_prime=p,kind='inert'))
    primes.sort(key=lambda p:(p['norm'],p['generator']))
    for i,p in enumerate(primes):
        p['id']=i
        (split if p['kind']=='split' else inert).setdefault(p['rational_prime'],[]).append(i)
    return primes,split,inert

def original_coefficients(prime_norms,N,U):
    # Ordered actual a,b,c factor assignments in the original small-small/long-long convolution.
    A=C=0
    for places in product(range(3),repeat=len(prime_norms)):
        na=nb=1
        parity=0
        for q,place in zip(prime_norms,places):
            if place==0:
                na*=q; parity+=1
            elif place==1:
                nb*=q; parity+=1
        sign=(-1)**parity
        if na<=U and nb<=U:
            A+=sign
        if na>U and nb>U:
            C+=sign
    mu=(-1)**len(prime_norms)
    divnorm=[1]
    for q in prime_norms:
        divnorm += [v*q for v in divnorm]
    r=sum(d>U and N//d>U for d in divnorm)
    assert (2*mu if N<=U else 0)-A+C==mu
    if N>U and U*U<=N<=7*U*U: # Actual squarefree high-window simplification is checked after direct convolution.
        assert C==mu*r and A==mu*(r-1)
    return A,C,mu,r

def full_support(D,U,T,P):
    cap=2*D
    spf=P.sieve_spf(cap)
    primes,split,inert=prime_catalog(cap,T,P,spf)
    columns=[];ledger=[]
    bygen=set()
    for N in range(D,2*D+1):
        group,why=P.ideal_norm_group(N,spf)
        if why:
            ledger.append(dict(norm=N,multiplicity=0,rejection=why));continue
        choices=[]
        for p,e in group['rational_prime_factors']:
            if p%3==1:
                ids=split[p]
                choices.append([(i,) for i in ids] if e==1 else [tuple(ids)])
            else:
                choices.append([tuple(inert[p])])
        A,C,mu,r=original_coefficients(group['ideal_prime_norms'],N,U)
        made=0
        for blocks in product(*choices):
            ids=tuple(sorted(i for block in blocks for i in block))
            assert len(ids)==len(set(ids))
            g=(1,0)
            for i in ids:
                g=T.mul(g,primes[i]['generator'])
            assert T.norm(g)==N and g[0]%3==1 and g[1]%3==0
            assert g not in bygen;bygen.add(g)
            columns.append(dict(id=len(columns),generator=g,norm=N,prime_ids=ids,
              A=A,C=C,mu=mu,r_U=r,W=finite_profile_node(D,N),nu_omega=(1,0)))
            made+=1
        assert made==group['ideal_multiplicity']
        ledger.append(dict(norm=N,multiplicity=made,rejection=None,mu=mu,A=A,C=C,r_U=r,
          rational_prime_factors=group['rational_prime_factors'],
          ideal_prime_norms=group['ideal_prime_norms'],W=finite_profile_node(D,N)))
    columns.sort(key=lambda c:(c['norm'],c['generator']))
    for i,c in enumerate(columns):c['id']=i
    assert sum(r['multiplicity'] for r in ledger)==len(columns)
    return primes,columns,ledger

def sf_small(cap,primes,T):
    chosen=[p for p in primes if p['norm']<=cap]
    out=[dict(generator=(1,0),norm=1,prime_ids=())]
    for p in chosen:
        additions=[]
        for v in out:
            N=v['norm']*p['norm']
            if N<=cap:
                additions.append(dict(generator=T.mul(v['generator'],p['generator']),norm=N,
                  prime_ids=v['prime_ids']+(p['id'],)))
        out += additions
    return sorted(out,key=lambda v:(v['norm'],v['generator']))

def make_rows(D,A1,A2,primes,T,captured,old_rows):
    H=T.integer_root(D**3,4)
    small=sf_small(max(2*A1-1,2*A2-1),primes,T)
    rows=[]
    for a in small:
        if not A1<=a['norm']<2*A1:continue
        for b in small:
            if not A2<=b['norm']<2*A2:continue
            if set(a['prime_ids']) & set(b['prime_ids']):continue
            N=a['norm']*b['norm']**2
            if N>H:continue
            u=T.mul(a['generator'],T.power(b['generator'],2))
            assert T.norm(u)==N
            # A nonempty first factor gives an outside-S valuation exactly1, hence nonprincipal.
            assert a['prime_ids']
            rows.append(dict(v1=a['generator'],v2=b['generator'],u=u,N=N,
              v1_prime_ids=a['prime_ids'],v2_prime_ids=b['prime_ids'],literal_unit=(1,0),
              nonprincipal_reason='a prime of v1 has valuation1 outsideS; v1,v2 squarefree/coprime',
              v3_v4_v5_v6=(1,1,1,1)))
    rows.sort(key=lambda r:(r['N'],r['v1'],r['v2']))
    if old_rows:
        old=json.loads(captured[next(iter(OLD_INPUTS))])['blocks'][1]
        assert D==60000 and A1==37 and A2==7 and H==3833 and old['row_count']==20
        key=lambda r:(tuple(r['v1']),tuple(r['v2']),tuple(r['u']),r['N'])
        oldkeys={key(r) for r in old['all_rows_in_actual_block']}
        assert len(oldkeys)==20 and {key(r) for r in rows}==oldkeys
        # The literal old row arrays are the input to the new all-column run.
        lookup={key(r):r for r in rows}
        rows=[{**lookup[key(r)],'v1':r['v1'],'v2':r['v2'],'u':r['u'],'N':r['N']} for r in old['all_rows_in_actual_block']]
    assert rows
    for i,r in enumerate(rows):r['id']=i
    return rows,H

def divisor_incidence(columns):
    incidence={}
    for c in columns:
        for d in subsets(c['prime_ids']):
            incidence.setdefault(d,[]).append(c['id'])
    assert () in incidence
    assert all(c['prime_ids'] in incidence for c in columns)
    return incidence

def resource_estimate(primes,columns,rows,incidence):
    nnz=sum(map(len,incidence.values()))
    return dict(prime_ideals=len(primes),columns=len(columns),active_columns=sum(c['W'] for c in columns),
      rows=len(rows),divisors=len(incidence),column_divisor_incidences=nnz,
      single_prime_row_symbol_evaluations=len(rows)*len(primes),
      column_row_values=len(rows)*len(columns),row_incidence_visits=len(rows)*nnz,
      ordered_pair_row_visits_if_literal=len(rows)*len(columns)**2,
      maximum_column_ideal_prime_count=max(len(c['prime_ids']) for c in columns),
      dense_F_arrays_not_retained=True,
      rough_memory_ceiling_MiB=256,rough_output_ceiling_MiB=100,
      caution='Resource ceilings are planning estimates, not measured guarantees; character/GCD work is not executed by estimate mode')

def all_symbols(primes,columns,rows,T):
    table=[]
    for row in rows:
        locals_=[T.direct_symbol([(p['generator'],1)],row['u']) for p in primes]
        values=[]
        for c in columns:
            local=[locals_[p] for p in c['prime_ids']]
            values.append(None if None in local else sum(local)%6)
        table.append(values)
    return table

def matrix(F):
    return [emul(x,econj(y)) for x in F for y in F]

def msum(a,b,k=1):
    return [eadd(x,scale(y,k)) for x,y in zip(a,b)]

def zero_matrix():
    return [(0,0)]*9

def qmatrix(a,D):
    return {p:[str(Fraction(z[0],D)),str(Fraction(z[1],D))] for p,z in zip(PAIRS,a)}

def direct_literal(columns,rows,table):
    totals=zero_matrix();byrow=[];paircount=0
    for ri,row in enumerate(rows):
        result=zero_matrix()
        for m in columns:
            pm=table[ri][m['id']]
            if pm is None or not m['W']:continue
            x=[scale(PHASES[pm],m[k]) for k in COMPONENTS]
            for n in columns:
                if set(m['prime_ids']) & set(n['prime_ids']):continue
                pn=table[ri][n['id']]
                if pn is None or not n['W']:continue
                paircount+=1
                y=[scale(PHASES[pn],n[k]) for k in COMPONENTS]
                result=msum(result,[emul(a,econj(b)) for a in x for b in y])
        byrow.append(result);totals=msum(totals,result)
    return dict(total=totals,by_row=byrow,nonzero_weight_coprime_pair_row_visits=paircount)

def check_old_submatrix(columns,rows,table,captured):
    old=json.loads(captured['web/data/fixed-h1.json'])
    lookup={tuple(c['generator']):c['id'] for c in columns}
    ids=[lookup[tuple(c['generator'])] for c in old['columns']]
    oldrow={tuple(r['u']):r for r in old['rows']}
    checks=0
    for ri,row in enumerate(rows):
        for j,ci in enumerate(ids):
            assert table[ri][ci]==oldrow[tuple(row['u'])]['phases'][j]
            checks+=1
    return dict(immutable_control_only=True,raw_phase_values_checked=checks,
      selected_column_ids=ids,old_scripts_executed=False,
      scope='Old two-column entries are a control submatrix; the result uses every annular ideal column')

def execute(output,D,U,A1,A2,old_rows=False,literal=False,estimate_only=False):
    if output.exists():raise FileExistsError('Preserve existing output: '+str(output))
    if type(D) is not int or not 1<D<=60000 or type(U) is not int or U<1:
        raise ValueError('Exact positive integers and 1<D<=60000 required')
    if not 2*D<=7*U*U or U*U>D:raise ValueError('Actual high window 2D/7<=U²<=D required')
    output.mkdir(parents=True)
    started=time.monotonic_ns()
    captured,pins=capture_sources(output,old_rows)
    T,P=load_helpers(captured)
    parameters=dict(schema='signed-divisor-full-column-v1',scope=SCOPE,D=D,U=U,A1=A1,A2=A2,
      H=T.integer_root(D**3,4),S='All prime ideals above2and3',nu='principal1',
      annulus='Closed D<=Nm<=2D; W=0 at endpoints and1 at every strict integer norm node',
      rowblock='Primary1mod3 squarefree good pairwise-coprime v1,v2; A_j<=Nv_j<2A_j; u=v1*v2²; Nu<=H; v3..v6=1; literal unit1',
      profile=dict(fixed_once=True,delta='1/240000',
        smoothstep='s(t)=0 for t<=0; exp(-1/t)/(exp(-1/t)+exp(-1/(1-t))) for0<t<1;1 for t>=1',
        formula='W_delta(y)=s((y-1)/delta)s((2-y)/delta)',supnorm='1',
        nodal_proof='1/D>=1/60000=4delta for every integer1<D<=60000; all strict nodes on plateau',
        derivative_cost='For fixed k, O_k(240000^k), fixed and potentially enormous; no bounded-seminorm or asymptotic claim'),
      arithmetic='Z[omega] integers; omega²+omega+1=0; conjugate(a,b)=(a-b,-b); linear first',
      seed=None,old_rows_reused=old_rows,literal_pair_verification=literal)
    write_new(output/'parameters.json',parameters)
    primes,columns,ledger=full_support(D,U,T,P)
    rows,H=make_rows(D,A1,A2,primes,T,captured,old_rows)
    incidence=divisor_incidence(columns)
    estimate=resource_estimate(primes,columns,rows,incidence)
    estimate['support_preparation_ns']=time.monotonic_ns()-started
    write_new(output/'resource-estimate.json',estimate)
    write_new(output/'prime-ideals.json',primes)
    write_new(output/'columns.json',columns)
    write_new(output/'rows.json',rows)
    with (output/'norm-ledger.jsonl').open('xb') as handle:
        for r in ledger:handle.write(canonical(r))
    if estimate_only:
        finish_manifest(output,pins,dict(passed=True,estimate_only=True,resources=estimate),started)
        return estimate
    table=all_symbols(primes,columns,rows,T)
    write_new(output/'raw-character-phases.json',table)
    old_control=check_old_submatrix(columns,rows,table,captured) if old_rows else None
    ordered=sorted(incidence,key=lambda d:(len(d),d))
    zmats={};rownet=[zero_matrix() for r in rows]
    plus=zero_matrix();minus=zero_matrix();pair_z={}
    with (output/'divisor-energies.jsonl').open('xb') as handle:
        for di,d in enumerate(ordered):
            F=[];allowed=[];mask=[]
            for ri,row in enumerate(rows):
                f=[[0,0] for k in COMPONENTS];count=0
                for ci in incidence[d]:
                    phase=table[ri][ci]
                    if phase is None or not columns[ci]['W']:continue
                    count+=1;v=PHASES[phase]
                    for j,k in enumerate(COMPONENTS):
                        coefficient=columns[ci][k]
                        f[j][0]+=coefficient*v[0];f[j][1]+=coefficient*v[1]
                f=[tuple(v) for v in f]
                assert f[0]==eadd(f[1],scale(f[2],-1))
                F.append(f);allowed.append(count)
                rawmask=all(T.direct_symbol([(primes[p]['generator'],1)],row['u']) is not None for p in d)
                mask.append(rawmask)
                if not rawmask:assert count==0 and all(x==(0,0) for x in f)
            z=zero_matrix()
            sign=(-1)**len(d)
            for ri,f in enumerate(F):
                term=matrix(f);z=msum(z,term);rownet[ri]=msum(rownet[ri],term,sign)
            for i in (0,4,8):assert z[i][1]==0 and z[i][0]>=0
            for a in range(3):
                for b in range(3):assert z[3*a+b]==econj(z[3*b+a])
            assert z[0]==eadd(eadd(z[4],z[8]),scale(eadd(z[5],z[7]),-1))
            zmats[d]=z;pair_z[d]=len(incidence[d])**2
            if sign==1:plus=msum(plus,z)
            else:minus=msum(minus,z)
            dg=(1,0);dn=1
            for p in d:dg=T.mul(dg,primes[p]['generator']);dn*=primes[p]['norm']
            handle.write(canonical(dict(id=di,prime_ids=d,generator=dg,norm=dn,mu=sign,
              incident_columns=len(incidence[d]),active_incident_columns=sum(columns[i]['W'] for i in incidence[d]),
              row_allowed_active_column_counts=allowed,row_raw_d_masks=mask,F_omega=F,
              Z_omega={p:v for p,v in zip(PAIRS,z)})))
    net=msum(plus,minus,-1)
    aggregate=zero_matrix()
    for row in rownet:aggregate=msum(aggregate,row)
    assert aggregate==net
    # Independent full-row accumulation and diagonal counts; no divisor factorization of X.
    direct_full=zero_matrix();diagonal=zero_matrix();full_byrow=[];diag_byrow=[]
    for ri,row in enumerate(rows):
        f=[(0,0)]*3;diag=zero_matrix()
        for ci,c in enumerate(columns):
            phase=table[ri][ci]
            if phase is None or not c['W']:continue
            terms=[scale(PHASES[phase],c[k]) for k in COMPONENTS]
            f=[eadd(x,y) for x,y in zip(f,terms)]
            diag=msum(diag,matrix(terms))
        z=matrix(f);full_byrow.append(z);diag_byrow.append(diag)
        direct_full=msum(direct_full,z);diagonal=msum(diagonal,diag)
    assert direct_full==zmats[()]
    # Inversion partitions ALL ordered pairs by their EXACT gcd, not a coprime residual proxy.
    gcdmats={d:zero_matrix() for d in ordered};gcdcounts={d:0 for d in ordered}
    for d in ordered:
        for g in subsets(d):
            sign=(-1)**(len(d)-len(g))
            gcdmats[g]=msum(gcdmats[g],zmats[d],sign)
            gcdcounts[g]+=sign*pair_z[d]
    assert gcdmats[()]==net and all(n>=0 for n in gcdcounts.values())
    allgcd=zero_matrix()
    reconstructed={d:zero_matrix() for d in ordered};count_reconstructed={d:0 for d in ordered}
    with (output/'gcd-classes.jsonl').open('xb') as handle:
        for g in ordered:
            allgcd=msum(allgcd,gcdmats[g])
            for d in subsets(g):
                reconstructed[d]=msum(reconstructed[d],gcdmats[g])
                count_reconstructed[d]+=gcdcounts[g]
            handle.write(canonical(dict(prime_ids=g,ordered_column_pair_count=gcdcounts[g],
              contribution_omega={p:v for p,v in zip(PAIRS,gcdmats[g])})))
    assert allgcd==zmats[()] and sum(gcdcounts.values())==len(columns)**2
    assert reconstructed==zmats and count_reconstructed==pair_z
    # A divisor equal to an annular column admits only that column: all self divisors remain.
    for c in columns:
        assert incidence[c['prime_ids']]==[c['id']]
        assert sum((-1)**len(d) for d in subsets(c['prime_ids']))==0
    literal_check=None
    if literal:
        literal_check=direct_literal(columns,rows,table)
        assert literal_check['total']==net and literal_check['by_row']==rownet
        write_new(output/'literal-ordered-pair-check.json',literal_check)
    write_new(output/'row-identities.json',dict(rows=[dict(row_id=i,
      full_energy_omega={p:v for p,v in zip(PAIRS,full_byrow[i])},
      diagonal_omega={p:v for p,v in zip(PAIRS,diag_byrow[i])},
      coprime_h1_numerator_omega={p:v for p,v in zip(PAIRS,rownet[i])}) for i in range(len(rows))]))
    budget={}
    for index,p in enumerate(PAIRS):
        item=dict(even_mu_Z_omega=plus[index],odd_mu_Z_omega=minus[index],signed_numerator_omega=net[index],
          signed_squared_complex_norm=enorm(net[index]))
        if index in (0,4,8):
            mass=plus[index][0]+minus[index][0]
            item.update(total_unsigned_mass=mass,cancellation_ratio=str(Fraction(abs(net[index][0]),mass)) if mass else '0')
        budget[p]=item
    summary=dict(schema='signed-divisor-full-column-summary-v1',passed=True,scope=SCOPE,parameters=parameters,
      resources=estimate,counts=dict(columns=len(columns),active_columns=sum(c['W'] for c in columns),
        rows=len(rows),divisors=len(ordered),ordered_coprime_column_pairs=gcdcounts[()],
        raw_zero_column_row_values=sum(v is None for row in table for v in row),
        raw_one_column_row_values=sum(v==0 for row in table for v in row),
        squarefree_ideals_with_nonsquarefree_rational_norm=sum(len({primes[p]['rational_prime'] for p in c['prime_ids']})<len(c['prime_ids']) or any(primes[p]['kind']=='inert' for p in c['prime_ids']) for c in columns)),
      divisor_budget=budget,normalized_h1=qmatrix(net,D),full_row_energy=qmatrix(zmats[()],D),
      diagonal=qmatrix(diagonal,D),old_selected_submatrix_control=old_control,
      checks=dict(original_coefficients_direct_ternary=True,all_raw_zeros_retained=True,
        all_rows_nonprincipal_by_v1=True,all_divisors_including_self=True,
        all_nine_crosscomponents=True,hermitian=True,A_equals_C_minus_mu=True,
        all_gcd_classes_inverted_and_reconstructed=True,all_row_identities=True,
        small_literal_pair_check=literal,large_literal_pair_check=False),
      normalized_scope='Divide signed numerator by D once; X already contains original Mobius signs, no extra mu(q)',
      gcd_slice_psd_claim=False,asymptotic_claim=False)
    finish_manifest(output,pins,summary,started)
    return summary

def finish_manifest(output,pins,summary,started):
    summary.update(elapsed_ns=time.monotonic_ns()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    for p,v in pins.items():
        if sha((ROOT/p).read_bytes())!=v['sha256']:raise RuntimeError('Source changed during run: '+p)
    summary['source_bytes_unchanged']=True
    write_new(output/'summary.json',summary)
    files={str(p.relative_to(output)):dict(bytes=p.stat().st_size,sha256=sha(p.read_bytes()))
      for p in sorted(output.rglob('*')) if p.is_file()}
    write_new(output/'manifest.json',dict(schema='signed-divisor-full-column-manifest-v1',passed=True,
      output=str(output.relative_to(ROOT)),files=files,source_freeze_sha256=sha((output/'source-freeze.json').read_bytes()),
      summary_sha256=sha((output/'summary.json').read_bytes()),scope=SCOPE))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--D',required=True,type=int)
    parser.add_argument('--U',required=True,type=int)
    parser.add_argument('--A1',required=True,type=int)
    parser.add_argument('--A2',required=True,type=int)
    parser.add_argument('--out',required=True,type=Path)
    parser.add_argument('--old-rows',action='store_true')
    parser.add_argument('--literal-pairs',action='store_true')
    parser.add_argument('--estimate-only',action='store_true')
    args=parser.parse_args()
    output=args.out if args.out.is_absolute() else ROOT/args.out
    result=execute(output,args.D,args.U,args.A1,args.A2,args.old_rows,args.literal_pairs,args.estimate_only)
    print(json.dumps(dict(passed=result.get('passed',True),output=str(output),
      columns=result.get('counts',result).get('columns'),elapsed_ns=result.get('elapsed_ns'),
      summary_sha256=sha((output/'summary.json').read_bytes())),sort_keys=True))

if __name__=='__main__':
    main()
