"""Recompute adaptive theta output rounding, with no decimal-limit mutation.

Uses the independent exact parameter design, not producer interval arithmetic.
The interval component is the worst accepted eta/4, not an executed sample.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
from check_design import select

ROOT=Path(__file__).resolve().parents[3]

def bits(eta):
    if not isinstance(eta,F) or eta<=0:
        raise ValueError('Positive exact Fraction request required')
    B=max(32,eta.denominator.bit_length()-eta.numerator.bit_length()+8)
    while F(5,1<<B)>eta/8:
        B+=1
    return B

def up(x,B):
    return F(-(-x.numerator*(1<<B)//x.denominator),1<<B)

def encode(v):
    if isinstance(v,F):
        return {'numerator':str(v.numerator),'denominator':str(v.denominator),'display':float(v)}
    if isinstance(v,dict):
        return {k:encode(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)):
        return [encode(x) for x in v]
    return v

def run(output):
    if output.exists():
        raise FileExistsError('Preserve previous check output')
    controls=0
    for eta in [F(1),F(1,10**24),F(1,10**32),F(1,10**100),F(7,9),F(10**8)]:
        B=bits(eta)
        assert F(5,1<<B)<=eta/8
        controls+=1
        for x in [F(),F(1),F(1,3*(1<<B)),eta/8,eta/4]:
            assert x<=up(x,B)<x+F(1,1<<B)
            controls+=1
    records=[]
    for e in [24,32]:
        eta=F(1,10**e)
        B=bits(eta)
        assert B=={24:87,32:114}[e]
        for q in [3,4,5]:
            r=select(q,eta)
            raw=dict(r['budgets'],interval_arithmetic=eta/4)
            rounded={k:up(x,B) for k,x in raw.items()}
            for key,x in raw.items():
                assert x<=rounded[key]<x+F(1,1<<B)
                controls+=1
            radius=sum(rounded.values(),F())
            assert sum(raw.values(),F())<=3*eta/4
            assert radius<=7*eta/8<eta
            controls+=2
            records.append({'q':q,'eta':eta,'N':r['N'],'J':r['J'],'T':r['T'],'K':r['K'],
                            'active_pairs':r['active_pairs'],'potential_pairs':r['potential_pairs'],
                            'discarded_pairs':r['discarded_pairs'],'budget_rounding_bits':B,
                            'raw_interval_radius_acceptance':eta/4,'rounded_budgets_with_worst_interval':rounded,
                            'literal_reported_radius_majorant':radius,'maximum_allowed_majorant':7*eta/8,
                            'raw_analytic_display':{k:float(x) for k,x in r['budgets'].items()},
                            'raw_analytic_exact_reconstruction':'q,N,J,K and exact formulas in check_design.py; whole-pair set follows from q,N,J,eta threshold'})
    names=['planning/adaptive-theta-20261105/design/check_serialized_design.py',
           'planning/adaptive-theta-20261105/design/check_design.py',
           'planning/adaptive-theta-20261105/design/DESIGN.md',
           'planning/adaptive-theta-20261105/design/adaptive-theta-core-proposal.tex',
           'planning/adaptive-theta-20261105/design/adaptive-theta-details-proposal.tex',
           'examples/analytic_oracle/adaptive_theta.py','examples/analytic_oracle/precision.py']
    hashes={n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in names}
    payload={'scope':'Exact output-budget design check, conditional on successful interval radius<=eta/4; not an executed sampler acceptance',
             'records':records,'controls':controls,'source_sha256':hashes,'special_functions_used':False,
             'integer_string_limit_changed':False,'new_Lean_declarations':0,'GRH_proved':False}
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(encode(payload),indent=2)+'\n')
    print(json.dumps({'records':len(records),'controls':controls,'rounding_bits':[87,114],
                      'literal_reported_majorants':[float(r['literal_reported_radius_majorant']) for r in records]}))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    run(args.output)
