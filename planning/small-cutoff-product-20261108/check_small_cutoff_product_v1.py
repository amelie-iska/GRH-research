from bisect import bisect_left,bisect_right
from pathlib import Path
source=Path('planning/coherent-mixed-band-20261108/check_mixed_sub_u_v1.py')
code=source.read_text()
assert code.count('counts=Counter()')==1
# Import only the arithmetic definitions. The old fixtures are never run.
exec(compile(code.split('counts=Counter()',1)[0],str(source),'exec'))

def all_ideals(bound):
    def generate(start,indices,n):
        yield n,indices
        for p in range(start,len(P)):
            if n*norms[p]>bound:
                break
            power=norms[p]
            valuation=1
            while n*power<=bound:
                yield from generate(p+1,indices+(p,)*valuation,n*power)
                valuation+=1
                power*=norms[p]
    return sorted(generate(0,(),1))

def raw_ideal(indices,u):
    z=(1,0)
    for p in indices:
        z=mul(z,local_symbol(p,u))
    return z

@lru_cache(None)
def actual_partial(m,U,Z):
    return sum(mu(x)*mu(y) for x in splits(m) for y in splits(m-x)
               if norm(x)<=U and norm(y)<=U and norm(x)*norm(y)<=Z)

@lru_cache(None)
def beta(d,z,U,Z):
    return sum(mu(x)*mu(y)*mu(z)
               for x in splits(d) for y in splits(d-x) for left in splits(z)
               if norm(x)*norm(left)<=U and norm(y)*norm(z-left)<=U
               and norm(x)*norm(y)*norm(z)<=Z)

counts=Counter()
cases=[]
for D,U,H,A1,A2 in [(280,16,65,13,1),(3600,59,460,7,7),(7500,83,780,13,7)]:
    assert U**2<=D<=Q(7,2)*U**2 and H**4<=D**3
    sf_ideals=sf(2*D)
    ann=[I for I in sf_ideals if D<norm(I)<2*D]
    rows=[(x,y,mul(generator(x),power(generator(y),2)))
          for x in sf_ideals if A1<=norm(x)<2*A1
          for y in sf_ideals if A2<=norm(y)<2*A2
          and not x&y and norm(x)*norm(y)**2<=H]
    assert rows
    ordinary=all_ideals(2*D)
    ordinary_norms=[n for n,b in ordinary]
    assert len({b for n,b in ordinary})==len(ordinary)
    ds=sorted({I for I in sf_ideals if norm(I) in (1,7,13,49,91)}
              | {ann[-1]},key=lambda I:(norm(I),tuple(sorted(I))))
    zrs=sorted(sf(max(29,isqrt(2*D))),key=lambda I:(norm(I),tuple(sorted(I))))
    selected_nonzero=0
    for d in ds:
        Nd=norm(d)
        for Z in (1,8,29):
            for p1,p2,u in rows:
                if d&(p1|p2):
                    counts['raw_d_row_zeros']+=1
                    continue
                direct=zero
                for m in ann:
                    if not d<=m:
                        continue
                    a=m-d
                    part=actual_partial(m,U,Z)
                    by_parts=sum(beta(d,z,U,Z) for z in splits(a) if norm(z)<=Z)
                    assert part==by_parts
                    counts['exact_cutoff_assignments']+=1
                    if part!=ternary(m,U):
                        counts['nontrivial_complement_columns']+=1
                    direct=add(direct,scale(mul(w(Q(norm(m),D)),symbol(a,u)),part))
                small=zero
                large=zero
                wrong_disjoint=zero
                wrong_mask=zero
                for z in zrs:
                    Nz=norm(z)
                    if Nz>Z:
                        break
                    if z&d:
                        continue
                    outer=beta(d,z,U,Z)
                    if not outer:
                        continue
                    pref=scale(symbol(z,u),outer)
                    if pref==zero:
                        counts['raw_z_row_zeros']+=1
                        continue
                    mask=d|z|p1|p2
                    X=Q(D,Nd*Nz)
                    for r in zrs:
                        Nr=norm(r)
                        if Nr*Nr>=2*X:
                            break
                        if r&mask:
                            counts['masked_square_factors']+=1
                            continue
                        C=X/(Nr*Nr)
                        zeta=scale(mul(pref,power(symbol(r,u),2)),mu(r))
                        for Nb,b in ordinary[bisect_right(ordinary_norms,C):
                                             bisect_left(ordinary_norms,2*C)]:
                            raw=raw_ideal(b,u)
                            val=mul(mul(zeta,raw),w(Q(Nb,1)/C))
                            wrong_mask=add(wrong_mask,val)
                            if mask.intersection(b):
                                counts['masked_inner_paths']+=1
                                continue
                            if C>11:
                                small=add(small,val)
                                counts['short_square_divisor_paths']+=1
                            else:
                                large=add(large,val)
                                counts['long_square_divisor_paths']+=1
                            if not r.intersection(b):
                                wrong_disjoint=add(wrong_disjoint,val)
                            else:
                                counts['live_repeated_r_b_prime_paths']+=1
                assert add(small,large)==direct,(D,U,Nd,Z,u)
                selected_nonzero+=direct!=zero
                counts['exact_split_amplitudes']+=1
                counts['false_disjointness_changes_amplitude']+=wrong_disjoint!=direct
                counts['dropped_b_mask_changes_amplitude']+=wrong_mask!=direct
    assert selected_nonzero
    cases.append({'D':D,'U':U,'H':H,'pivots':[A1,A2],'rows':len(rows),
                  'annular_columns':len(ann),'selected_d':len(ds),
                  'nonzero_cutoff_amplitudes':selected_nonzero})

# New sixth-power valuation controls, with actual row and prime symbols.
# b0 and q can share a prime and q can itself be nonsquarefree.
for exponents in product((0,1,5,6,7,11,12,13),repeat=3):
    indices=(0,1,2)
    b=tuple(p for p,e in zip(indices,exponents) for _ in range(e))
    b0=tuple(p for p,e in zip(indices,exponents) for _ in range(e%6))
    q=tuple(p for p,e in zip(indices,exponents) for _ in range(e//6))
    assert sorted(b0+q*6)==list(b)
    for v1 in indices:
        u=primary(v1)
        value=raw_ideal(b,u)
        mask=zero if v1 in q else (1,0)
        assert value==mul(mask,raw_ideal(b0,u))
        counts['sixth_factor_raw_mask_checks']+=1
        counts['overlapping_sixth_factor_support']+=bool(set(b0)&set(q))
        counts['sixth_factor_masks_a_row']+=v1 in q

def bound_powers(a1,a2,c):
    return (2*(a1+a2)-c,a1+a2,a2+c,a2+5*a1/6+c/3,a2+a1/3+5*c/6)
a,b,c=Q(5,12),Q(1,6),Q(31,66)
assert bound_powers(a,b,c)==(Q(23,33),Q(7,12),Q(7,11),Q(59,88),Q(23,33))
assert Q(23,33)+Q(1,20)==Q(493,660)
assert Q(3,4)-Q(493,660)==Q(1,330)
assert Q(3,4)-Q(23,33)==Q(7,132)
assert (Q(23,33)+Q(13,12))/2==Q(235,264)
assert max(bound_powers(Q(3,4),Q(0),Q(21,32)))==Q(27,32)
for da,db in product(range(-5,6),repeat=2):
    assert max(bound_powers(a+Q(da,10000),b+Q(db,10000),c))+Q(1,20)<Q(3,4)
    counts['exact_neighborhood_powers']+=1
for k in ('false_disjointness_changes_amplitude','dropped_b_mask_changes_amplitude',
          'raw_z_row_zeros','raw_d_row_zeros','short_square_divisor_paths','long_square_divisor_paths',
          'overlapping_sixth_factor_support','sixth_factor_masks_a_row'):
    assert counts[k]>0,k
result={'schema':'small-cutoff-product-controls-v1','passed':True,'cases':cases,
        'scope':'Exact finite cutoff decomposition, square-divisor amplitudes and raw masks. These controls do not test an asymptotic Poisson or sieve estimate.',
        **dict(counts)}
out=Path('outputs/checks/2026-11-08-small-cutoff-product/controls-v1.json')
with out.open('x') as handle:
    json.dump(result,handle,indent=2)
    handle.write('\n')
print(json.dumps(result))
