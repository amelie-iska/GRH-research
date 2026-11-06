#!/usr/bin/env python3
"""NEW synthetic formal Dirichlet/subset algebra and scale-only HB checks.
No arithmetic characters, original family tables or numerical Gauss data.
"""
from pathlib import Path
from fractions import Fraction
from math import comb, prod
import argparse, datetime, hashlib, json, random, time

SYMBOLS = (("p7a",7),("p7b",7),("p13a",13),("p13b",13),
           ("p19",19),("p25",25),("p31",31),("p37",37))
TWICE_D = (4,22,94,1042,8194,10**6,7**5,13**5,2**65)
SCALE_D_EXPONENTS = (64,72,80)
SEED = 2026110609
RANDOM_BOXES_PER_D_J = 180

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def conv(a,b):
    """SF ideal coefficient: all ordered DISJOINT subset factors."""
    n=len(a)
    out=[0]*n
    for target in range(n):
        part=target
        while True:
            out[target] += a[part]*b[target ^ part]
            if part==0:
                break
            part=(part-1)&target
    return out

def powers(f,j):
    out=[[1]+[0]*(len(f)-1)]
    for _ in range(j):
        out.append(conv(out[-1],f))
    return out

def formal_checks():
    size=1<<len(SYMBOLS)
    norms=[prod(SYMBOLS[i][1] for i in range(len(SYMBOLS)) if m>>i&1)
           for m in range(size)]
    mu=[(-1)**m.bit_count() for m in range(size)]
    one=[1]*size
    delta=[1]+[0]*(size-1)
    assert conv(one,mu)==delta
    # Distinct symbols, even at equal norm, remain separate ideal coordinates.
    assert norms[1]==norms[2]==7 and 1!=2
    assert norms[4]==norms[8]==13 and 4!=8
    assert norms[3]==49 and mu[3]==1
    onepow=powers(one,4)
    cases=[]
    negative=None
    for q in TWICE_D:
        # EXACT threshold, no floating z=(2D)^(1/5).
        M=[mu[m] if norms[m]**5<=q else 0 for m in range(size)]
        diff=[mu[m]-M[m] for m in range(size)]
        assert diff[0]==0
        mpow=powers(M,5)
        dpow=powers(diff,5)
        truncated=[0]*size
        for j in range(1,6):
            term=conv(onepow[j-1],mpow[j])
            c=(-1)**(j-1)*comb(5,j)
            truncated=[x+c*y for x,y in zip(truncated,term)]
        rem=conv(onepow[4],dpow[5])
        assert all(mu[m]==truncated[m]+rem[m] for m in range(size))
        targets=[m for m in range(size) if norms[m]<=q]
        assert all(rem[m]==0 and truncated[m]==mu[m] for m in targets)
        outside=[norms[m] for m in range(size) if diff[m]]
        lower=min(outside) if outside else None
        if lower is not None:
            # Five nonzero mu-M factors have product at least lower^5>2D.
            assert lower**5>q
            assert all(norms[m]>=lower**5 for m in range(size) if dpow[5][m])
            assert all(norms[m]>=lower**5 for m in range(size) if rem[m])
        ties=[m for m in range(size) if norms[m]**5==q]
        assert all(M[m]==mu[m] for m in ties)
        cases.append({
            "twice_D":q,"D_exact":str(Fraction(q,2)),
            "full_SF_coefficient_identities":size,
            "target_coefficients_Nm_le_2D":len(targets),
            "target_remainder_nonzero":0,
            "remainder_nonzero_outside_target":sum(bool(rem[m]) for m in range(size)),
            "minimum_nonzero_mu_minus_M_norm":lower,
            "fifth_power_of_minimum":None if lower is None else lower**5,
            "exact_cutoff_tie_masks":ties,
        })
        if q==10**6:
            # Deliberately WRONG J=4 truncation with the SAME fifth-root cutoff.
            t4=[0]*size
            for j in range(1,5):
                term=conv(onepow[j-1],mpow[j])
                c=(-1)**(j-1)*comb(4,j)
                t4=[x+c*y for x,y in zip(t4,term)]
            r4=conv(onepow[3],dpow[4])
            assert all(mu[m]==t4[m]+r4[m] for m in range(size))
            witness=sum(1<<i for i in (4,5,6,7))
            assert all(SYMBOLS[i][1]**5>q for i in (4,5,6,7))
            assert norms[witness]==19*25*31*37==544825<=q
            assert mu[witness]==1 and t4[witness]==-23 and r4[witness]==24
            negative={
                "expected_failure_observed":True,"wrong_truncation":"J4 with same z5",
                "D_exact":"500000","twice_D":q,
                "distinct_symbols":[SYMBOLS[i][0] for i in (4,5,6,7)],
                "factor_norms":[19,25,31,37],
                "each_factor_norm_fifth_power_exceeds_2D":True,
                "product_norm":norms[witness],
                "true_mu":mu[witness],"wrong_truncated_coefficient":t4[witness],
                "omitted_remainder_coefficient":r4[witness],
                "all_target_failures_if_remainder_dropped":
                    sum(t4[m]!=mu[m] for m in targets),
            }
    assert negative is not None
    return {"symbols":[{"name":a,"norm":b} for a,b in SYMBOLS],
            "equal_norm_symbols_not_merged":True,
            "SF_only_scope":"Subset convolution verifies coefficients of squarefree formal ideal targets; it is not a repeated-prime-power ideal calculation.",
            "cases":cases,"negative_J4":negative}

def scale_partition(scales):
    """Uses ONLY lower dyadic scales and their fixed index order.
    Return a balanced index mask, or None for the unbalanced case.
    Integer cubes compare to P^(1/3),P^(2/3) without floats.
    """
    P=prod(scales)
    for i,a in enumerate(scales):
        if P <= a**3 <= P*P:
            return 1<<i
    if all(a**3<=P for a in scales):
        acc=1
        mask=0
        for i,a in enumerate(scales):
            acc*=a
            mask|=1<<i
            if acc**3>=P:
                assert acc**3<=P*P
                return mask
        raise AssertionError("greedy failed")
    return None

def brute_partition(scales):
    P=prod(scales)
    for mask in range(1,1<<len(scales)):
        a=prod(v for i,v in enumerate(scales) if mask>>i&1)
        if P<=a**3<=P*P:
            return mask
    return None

def root5(q):
    lo,hi=0,1
    while hi**5<=q:
        hi*=2
    while hi-lo>1:
        mid=(lo+hi)//2
        if mid**5<=q:
            lo=mid
        else:
            hi=mid
    return lo

def validate_box(D,L,scales,is_mu):
    if D<2**64:
        raise ValueError("Exhaustive TypeI classification requires D>=2^64")
    assert 1<=len(scales)<=9 and len(scales)==len(is_mu)
    assert all(a>=1 and a&(a-1)==0 for a in scales)
    assert L**4>=D**3
    P=prod(scales)
    assert P*(2**len(scales))>=L and P<=2*L
    assert all(a**5<=2*D for a,b in zip(scales,is_mu) if b)
    # Explicit sufficient threshold from the proof, verified in integers.
    assert all(a**3<=P for a,b in zip(scales,is_mu) if b)
    got=scale_partition(scales)
    brute=brute_partition(scales)
    assert (got is None)==(brute is None)
    if got is None:
        big=[i for i,a in enumerate(scales) if a**3>P*P]
        assert len(big)==1 and not is_mu[big[0]]
        rest=P//scales[big[0]]
        assert rest**3<P
        return {"kind":"TypeI","long_index":big[0],"scales":list(scales)}
    a=prod(v for i,v in enumerate(scales) if got>>i&1)
    b=P//a
    assert P<=a**3<=P*P and P<=b**3<=P*P
    return {"kind":"TypeII","group_mask":got,"scales":list(scales)}

def weak_composition(total,n,rng):
    if n==1:
        return [total]
    # Stars and bars with distinct bars, exact integer composition.
    bars=sorted(rng.sample(range(total+n-1),n-1))
    cuts=[-1]+bars+[total+n-1]
    return [cuts[i+1]-cuts[i]-1 for i in range(n)]

def scale_checks():
    rng=random.Random(SEED)
    stats=[]
    total=balanced=unbalanced=point_samples=0
    witness={"TypeI":None,"TypeII":None}
    for exponent in SCALE_D_EXPONENTS:
        D=2**exponent
        L=2**(3*exponent//4)
        max_mu=(exponent+1)//5
        zfloor=root5(2*D)
        assert zfloor**5<=2*D<(zfloor+1)**5
        for j in range(2,6):
            n=2*j-1
            is_mu=[True]*j+[False]*(j-1)
            E=3*exponent//4
            # Explicit long-unrestricted and balanced scale fixtures.
            long_exp=[0]*n
            long_exp[-1]=E
            if j==2:
                good_exp=[E//4,E//4,E-2*(E//4)]
            else:
                good_exp=[0]*n
                good_exp[-2]=E//2
                good_exp[-1]=E-E//2
            exponent_boxes=[long_exp,good_exp]
            for _ in range(RANDOM_BOXES_PER_D_J):
                while True:
                    E=rng.randint(3*exponent//4-n,3*exponent//4+1)
                    small=[rng.randint(0,max_mu) for _ in range(j)]
                    if sum(small)<=E:
                        break
                large=weak_composition(E-sum(small),j-1,rng)
                exponent_boxes.append(small+large)
            counts={"TypeI":0,"TypeII":0}
            for exps in exponent_boxes:
                scales=tuple(2**e for e in exps)
                out=validate_box(D,L,scales,is_mu)
                kind=out["kind"]
                counts[kind]+=1
                total+=1
                balanced+=kind=="TypeII"
                unbalanced+=kind=="TypeI"
                if witness[kind] is None:
                    witness[kind]={"D":D,"L":L,"j":j,
                                   "is_mu":is_mu,"classification":out}
                # Exact admissible one-variable samples, selected AFTER grouping.
                # They do not change the group and need not meet common-W support.
                for variant in range(2):
                    norms=[]
                    for a,flag in zip(scales,is_mu):
                        upper=min(2*a-1,zfloor) if flag else 2*a-1
                        if a==1:
                            upper=1   # singleton unit box
                        assert upper>=a
                        norms.append(a if variant==0 else rng.randint(a,upper))
                    assert scale_partition(scales)==out.get("group_mask")
                    if kind=="TypeII":
                        mask=out["group_mask"]
                        u=prod(v for i,v in enumerate(norms) if mask>>i&1)
                        v=prod(v for i,v in enumerate(norms) if not mask>>i&1)
                        assert u**3*512>=L and v**3*512>=L
                        assert u**3<=4*(512**3)*(L**2)
                        assert v**3<=4*(512**3)*(L**2)
                    point_samples+=1
            stats.append({"D_exponent":exponent,"D":D,"L":L,"j":j,
                          "factors":n,"boxes":len(exponent_boxes),**counts})
    # Guard, not a claim that the theorem fails at every smaller D.
    rejected=False
    try:
        validate_box(2**63,2**48,(2**24,2**24),(False,False))
    except ValueError:
        rejected=True
    assert rejected
    assert total==len(SCALE_D_EXPONENTS)*4*(RANDOM_BOXES_PER_D_J+2)
    return {"seed":SEED,"random_boxes_per_D_j":RANDOM_BOXES_PER_D_J,
            "D_exponents":list(SCALE_D_EXPONENTS),"j_values":[2,3,4,5],
            "j1_empty_in_this_large_D_residual_support":True,
            "total_boxes":total,"balanced":balanced,"unbalanced":unbalanced,
            "independent_bruteforce_subsets_agree":True,
            "per_coordinate_norm_samples_after_grouping":point_samples,
            "no_norm_dependent_grouping":True,
            "D_below_2_power_64_explicit_guard_observed":rejected,
            "macro_cubed_bounds":"L/512 <= Nu^3,Nv^3 <= 4*512^3*L^2",
            "scope":"Synthetic integer dyadic lower scales and formal HB factor flags, not actual ideal-family samples.",
            "by_D_j":stats,"examples":witness}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--root",required=True)
    parser.add_argument("--output",required=True)
    args=parser.parse_args()
    root=Path(args.root).resolve()
    out=Path(args.output).resolve()
    allowed=root/"outputs/checks/2026-11-06-gauss-book/lane-a"
    assert out.parent==allowed and not out.exists()
    note=root/"planning/gauss-book-20261106/lane-a/BALANCED_RESIDUAL_HEATH_BROWN_CUBIC-v2.md"
    assert sha(note)=="c28af64fffc0b7b46ba97ac83c4128eca6ae150218785d72be038affa2db608e"
    start=time.perf_counter()
    formal=formal_checks()
    scales=scale_checks()
    result={"passed":True,"created_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "kind":"NEW exact synthetic formal Dirichlet subset algebra and HB scale checks",
            "source":{"path":str(Path(__file__).resolve().relative_to(root)),
                      "sha256":sha(Path(__file__))},
            "note":{"path":str(note.relative_to(root)),"sha256":sha(note)},
            "material_parameters":{"symbols":SYMBOLS,"twice_D_cases":TWICE_D,
                                   "J":5,"cutoff_membership":"(Na)^5<=2D",
                                   "seed":SEED,
                                   "formal_target":"all squarefree subsets of eight distinct symbols",
                                   "repeated_norm_symbols":"two norm7 and two norm13, never merged"},
            "formal":formal,"scales":scales,
            "elapsed_seconds":time.perf_counter()-start,
            "not_actual_character_Gauss_or_family_data":True,
            "not_Lean_or_interval_arithmetic":True,
            "old_controls_or_original_tables_rerun":False,
            "no_dependency_or_source_index_environment_changes":True}
    out.open("x").write(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"passed":True,"output":str(out),"sha256":sha(out),
                      "formal_cases":len(formal["cases"]),
                      "full_SF_coefficient_identities":
                          sum(x["full_SF_coefficient_identities"] for x in formal["cases"]),
                      "target_coefficients":
                          sum(x["target_coefficients_Nm_le_2D"] for x in formal["cases"]),
                      "scale_boxes":scales["total_boxes"],
                      "balanced":scales["balanced"],"unbalanced":scales["unbalanced"],
                      "expected_J4_support_failure":formal["negative_J4"],
                      "elapsed_seconds":result["elapsed_seconds"]},sort_keys=True))
if __name__=="__main__":
    main()
