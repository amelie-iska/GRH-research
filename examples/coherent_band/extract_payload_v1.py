#!/usr/bin/env python3
"""Compact DISPLAY extraction; never executes the frozen Perron/SVD controls."""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
from fractions import Fraction
from math import isqrt
import argparse, hashlib, json, types
ROOT = Path(__file__).resolve().parents[2]
SOURCE = 'outputs/checks/2026-11-06-coherent-band/root/finite-schur-controls-v1/controls-v1.json'
SOURCE_SHA = 'fd5b33de0c54632b46d0515f5a3f67c7b91ceb896d09bd5f0303256f9fe91a04'
PRODUCER = 'planning/coherent-band-20261106/root/check_finite_schur_v1.py'
HELPER = 'examples/profile_uniformity/ideal_tower.py'
PROOF = 'planning/coherent-band-20261106/root/FINITE_CUTOFF_SCHUR-v1.md'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def frac(q): return [q.numerator, q.denominator]
def write_new(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('x') as f: f.write(json.dumps(value, sort_keys=True, separators=(',', ':'))+'\n')
def extract():
    raw = ROOT/SOURCE
    assert sha(raw) == SOURCE_SHA
    original = json.loads(raw.read_text())
    assert original['passed'] and original['count'] == 1511 and original['dps'] == 55
    assert sha(ROOT/PRODUCER) == original['script_sha256']
    assert sha(ROOT/HELPER) == original['helper_sha256']
    assert sha(ROOT/PROOF) == original['proof_note_sha256']
    helper = types.ModuleType('coherent_band_metadata_only')
    helper.__file__ = str(ROOT/HELPER)
    exec(compile((ROOT/HELPER).read_bytes(), str(ROOT/HELPER), 'exec'), helper.__dict__)
    ideals = [a for a in helper.canonical_ideals(97) if a['good_S'] and a['squarefree']]
    rows = [a for a in ideals if a['norm'] <= 43]
    assert (len(rows), len(ideals)) == (14,29)
    def ideal(a, i):
        fs=[]
        for f in a['factors']:
            q=isqrt(f['norm']); inert=q*q == f['norm']
            fs.append(dict(generator=list(f['generator']),norm=f['norm'],exponent=f['exponent'],kind='inert' if inert else 'split',rational_prime=q if inert else f['norm']))
        return dict(id=i,norm=a['norm'],generator=list(a['generator_omega']),factors=fs,good_S=a['good_S'],squarefree=a['squarefree'])
    ri=[ideal(a,i) for i,a in enumerate(rows)]; ci=[ideal(a,i) for i,a in enumerate(ideals)]
    lookup={(c['label'],c.get('X'),c.get('i'),c.get('j')):c for c in original['checks']}
    result=[]
    for case in original['cases']:
        D=int(Fraction(case['D'])); X=case['X']; U=case['U']
        assert D*2 == X and U*U == D and len(case['states']) == 406
        entries=[]
        for idx, s in enumerate(case['states']):
            i,j=s['i'],s['j']; assert idx == i*29+j
            row,col=ri[i],ci[j]
            rkeys={tuple(f['generator']) for f in row['factors']}; ckeys={tuple(f['generator']) for f in col['factors']}
            common=sorted(rkeys & ckeys); product=row['norm']*col['norm']
            causes=(['shared_ideal_prime'] if common else [])+(['product_cutoff'] if product>X else [])
            assert s['mask'] == int(not causes)
            entry=dict(i=i,j=j,support=s['mask'],mask_causes=causes,common_factors=[list(g) for g in common],product_norm=product,x_fraction=frac(Fraction(product,D)))
            if s['mask']:
                assert (s['Nd'],s['Na']) == (row['norm'],col['norm'])
                assert s['phase6'] in (0,2,4)
                k={0:[1,0],2:[0,1],4:[-1,-1]}[s['phase6']]
                er=lookup['double_cutoff_error',X,i,j]
                x=Fraction(product,D); amplitude=((x-1)*(2-x))**3 if 1<x<2 else Fraction(0)
                entry.update(phase6=s['phase6'],A_U=s['A_U'],A_T=[s['A_T_real'],s['A_T_imag']],W=[s['W_real'],s['W_imag']],K_omega=k,AU_K_omega=[s['A_U']*v for v in k],profile_amplitude_fraction=frac(amplitude),profile_angle_fraction=frac(x/7) if amplitude else None,A_T_error=er['error'],A_T_control_bound=er['bound'])
            else:
                entry.update(phase6=None,A_U=None,A_T=None,W=None,K_omega=[0,0],AU_K_omega=[0,0],profile_amplitude_fraction=None,profile_angle_fraction=None,A_T_error=None,A_T_control_bound=None)
            entries.append(entry)
        supported=sum(x['support'] for x in entries)
        inert=sum(x['support'] and any(f['kind']=='inert' for f in ri[x['i']]['factors']+ci[x['j']]['factors']) for x in entries)
        assert (supported,406-supported,inert)==(case['supported'],case['raw_zero_states'],case['inert_factor_entries'])
        comparison={}
        for label in ['finite_integral_operator_bound','Frobenius_residual_bound','actual_AU_operator_bound','common_complex_W_operator_bound']:
            check=lookup[label,X,None,None]; comparison[label]={k:v for k,v in check.items() if k not in ['label','passed','X']}
        result.append(dict(D=D,X=X,U=U,T=case['T'],shape=case['shape'],supported=supported,masked=406-supported,inert_factor_entries=inert,G=case['G'],norms={k:case[k] for k in ['K_norm','AU_K_norm','AU_T_K_norm','residual_norm','W_AU_K_norm']},comparisons=comparison,entries=entries))
    assert sum(c['masked'] for c in result)==786
    assert sum(c['inert_factor_entries'] for c in result)==42
    inputs={x:sha(ROOT/x) for x in [SOURCE,PRODUCER,HELPER,PROOF,str(Path(__file__).relative_to(ROOT))]}
    return dict(schema='coherent-band-schur-display-v1',scope='Saved auxiliary actual-good-ideal cubic matrices; not original physical-row-family data, training, interval enclosures or a new proof.',source=dict(path=SOURCE,sha256=SOURCE_SHA,checks=1511,dps=55,interval_enclosures=False,inputs_sha256=inputs),generator_convention='Exact source canonical unit representative, not silently replaced by a primary generator; prime factors retain source generators.',support='1_{(d,a)=1} * 1_{Nd Na <= X}; all indices good squarefree ideals; X=2D.',profile=dict(formula='((x-1)(2-x))^3 exp(i x/7) for 1<x<2; 0 otherwise',regularity='C2 including endpoints',exact_argument='x=Nd Na/D',saved_coordinates='55-digit numerical projection, not interval-enclosed'),totals=dict(cases=3,rows=14,columns=29,states=1218,masked=786,inert_factor_entries=42),row_ideals=ri,column_ideals=ci,cases=result)
def main():
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--receipt',required=True);a=p.parse_args()
    out=Path(a.output);out=out if out.is_absolute() else ROOT/out
    rec=Path(a.receipt);rec=rec if rec.is_absolute() else ROOT/rec
    value=extract();write_new(out,value)
    write_new(rec,dict(passed=True,scope='Display extraction only, no frozen controls/SVD/Perron evaluator rerun',output=str(out.relative_to(ROOT)),sha256=sha(out),bytes=out.stat().st_size,source_sha256=SOURCE_SHA,extractor_sha256=sha(Path(__file__)),counts=value['totals']))
    print(json.dumps(dict(passed=True,output=str(out.relative_to(ROOT)),sha256=sha(out),bytes=out.stat().st_size)))
if __name__=='__main__':main()
