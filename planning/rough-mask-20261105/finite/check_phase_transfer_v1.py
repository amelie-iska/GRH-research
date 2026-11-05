"""Read-only coefficient and COMPLEX phase checks on the fresh frozen output, not a rerun."""
from pathlib import Path
from fractions import Fraction
import hashlib,json
ROOT=Path(__file__).resolve().parents[3];RUN=ROOT/'outputs/checks/2026-11-05-rough-mask/finite/run-v1'
sha=lambda b:hashlib.sha256(b).hexdigest()
PH=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))
def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def N(a):return a[0]*a[0]-a[0]*a[1]+a[1]*a[1]
assert sha((RUN/'manifest.json').read_bytes())=='d8ebdc9410e0e24c3dfd999ea33c10864d28b4e9f008913e08d26233217268cf'
results=[];tables=[]
for D in (200,512,900):
 d=json.loads((RUN/f'D{D}-v1.json').read_bytes());ideals=d['all_good_ideals'];primes=d['prime_ideals'];bygen={tuple(a['generator']):a for a in ideals};original=set(d['original_columns']);prime_sfid={p['id']:bygen[tuple(p['generator'])]['id'] for p in primes};phases=d['all_SF_residual_raw_phases']
 checks=coefficients=auxiliaries=0;negative=None
 for s in d['smooth_states']+d['rough_states']:
  ri=s['row'];f=ideals[s['f']];pf=phases[ri][str(f['id'])];pp=phases[ri][str(prime_sfid[s['p']])] if 'p'in s else 0
  T=s['T_p_masked_omega'] if 'p'in s else s['T_omega'];expected=(0,0) if pf is None or pp is None else mul(PH[(pf+pp)%6],T)
  key='original_F_fp_omega' if 'p'in s else 'original_Fd_omega'
  assert tuple(s[key])==expected;checks+=1
  if 'p'not in s:continue
  for t in s['terms']:
   m=bygen[tuple(t['extended_generator_omega'])];assert N(m['generator'])==t['extended_column_norm']
   if t['auxiliary_nonSF']:
    assert not m['squarefree'] and m['id']not in original and f['norm']==1 and ideals[t['a_id']]['prime_ids']==[s['p']];auxiliaries+=1
   else:
    assert m['squarefree'] and m['id']in original and m['A']==t['original_A_fa'];coefficients+=1
    ma=phases[ri][str(m['id'])];pa=t['raw_phase'];totalphase=None if pf is None or pp is None or pa is None else (pf+pp+pa)%6
    assert ma==totalphase
    if negative is None and expected!=(0,0):negative=dict(f=f['id'],p=s['p'],row=ri,actual_coefficient=m['A'],wrong_mu_p_factor=-m['A'],actual_F=expected,wrong_sign_F=tuple(-x for x in expected),norms_same_but_complex_values_differ=True)
 assert negative is not None
 results.append(dict(D=D,passed=True,full_complex_F_transfer_checks=checks,actual_original_coefficient_and_phase_checks=coefficients,auxiliary_nonSF_terms_checked=auxiliaries,coefficient_sign_negative=negative))
 r=d['raw_totals'];clean=r['smooth_raw']-r['K_S_raw'];raw=dict(K0=r['smooth_raw'],KT=r['K_mask_raw'],KS=r['K_S_raw'],Erow=r['Delta_row_raw'],Eres=r['Delta_residual_raw'],Ctwo=r['unit_two_rough_raw'],Delta=r['Delta_raw'],original_AA=r['original_AA_raw'],S_only_with_unit_correction=r['S_only_replaced_AA_raw'],clean_S_only_main=clean,original_minus_clean= r['original_AA_raw']-clean)
 assert raw['Delta']==raw['KS']-raw['KT']==raw['Erow']+raw['Eres'] and raw['original_minus_clean']==raw['Delta']+raw['Ctwo']
 tables.append(dict(D=D,raw_numerators=raw,normalized_exactly_once={k:str(Fraction(v,D)) for k,v in raw.items()},mixed_capacity_scope=d['parameters']['capacity_scope']))
value=dict(passed=True,input_manifest_sha256=sha((RUN/'manifest.json').read_bytes()),checker_sha256=sha(Path(__file__).read_bytes()),cases=results,tables=tables,raw_evaluator_rerun=False,old_diagnostics_or_helpers_imported=False,scope='Fresh saved-output complex phase/coefficient transfer and normalization bookkeeping. No analytic bound validation.')
out=ROOT/'outputs/checks/2026-11-05-rough-mask/finite/phase-transfer-and-normalization-v1.json'
with out.open('x') as f:json.dump(value,f,sort_keys=True,indent=2);f.write('\n')
print(sha(out.read_bytes()));print(json.dumps(results,sort_keys=True))
