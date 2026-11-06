#!/usr/bin/env python3
"""Independent display mapping checks; no SVD/Perron/scientific control rerun."""
from pathlib import Path
from fractions import Fraction
from decimal import Decimal,localcontext
import argparse,hashlib,json,math
ROOT=Path(__file__).resolve().parents[2]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def mul(x,y):a,b=x;c,d=y;return (a*c-b*d,a*d+b*c-b*d)
def norm(x):a,b=x;return a*a-a*b+b*b
def quotient(x,y):
 a,b=x;c,d=y;n=norm(y);u=a*(c-d)+b*d;v=b*c-a*d
 assert u%n==0 and v%n==0
 return (u//n,v//n)
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();out=Path(a.output);out=out if out.is_absolute() else ROOT/out
 payload=ROOT/'web/data/coherent-band-schur-v1.json';j=json.loads(payload.read_text());raw=json.loads((ROOT/j['source']['path']).read_text())
 assert sha(ROOT/j['source']['path'])==j['source']['sha256']
 for path,h in j['source']['inputs_sha256'].items():assert sha(ROOT/path)==h,path
 assert j['source']['checks']==raw['count']==1511 and j['source']['dps']==raw['dps']==55
 assert j['source']['interval_enclosures'] is False
 ideals=j['row_ideals']+j['column_ideals']
 for ideal in ideals:
  assert norm(ideal['generator'])==ideal['norm']
  z=(1,0)
  for f in ideal['factors']:
   assert f['exponent']==1 and norm(f['generator'])==f['norm'];z=mul(z,f['generator'])
   assert f['norm']==f['rational_prime']**(2 if f['kind']=='inert' else 1)
  assert norm(quotient(ideal['generator'],z))==1
  assert ideal['norm']%2 and ideal['norm']%3
 checks=0;inert=0;masked=0;max_w_error=0.0
 for c,src in zip(j['cases'],raw['cases']):
  assert c['X']==src['X'] and str(c['D'])==str(int(Fraction(src['D']))) and c['U']==src['U'];assert c['shape']==src['shape']==[14,29]
  assert all(c['norms'][k]==src[k] for k in c['norms'])
  for e,s in zip(c['entries'],src['states']):
   assert (e['i'],e['j'],e['support'])==(s['i'],s['j'],s['mask'])
   row=j['row_ideals'][e['i']];col=j['column_ideals'][e['j']];prod=row['norm']*col['norm'];assert e['product_norm']==prod
   common={tuple(f['generator']) for f in row['factors']} & {tuple(f['generator']) for f in col['factors']}
   assert e['support']==int(not common and prod<=c['X']);assert common=={tuple(g) for g in e['common_factors']}
   assert Fraction(*e['x_fraction'])==Fraction(prod,c['D'])
   if not e['support']:
    masked+=1;assert all(e[k] is None for k in ['A_U','A_T','W','phase6']);assert e['K_omega']==e['AU_K_omega']==[0,0]
   else:
    assert (s['Nd'],s['Na'])==(row['norm'],col['norm'])
    assert e['phase6']==s['phase6'] and e['A_U']==s['A_U'];assert e['A_T']==[s['A_T_real'],s['A_T_imag']];assert e['W']==[s['W_real'],s['W_imag']]
    assert e['K_omega']=={0:[1,0],2:[0,1],4:[-1,-1]}[e['phase6']];assert e['AU_K_omega']==[e['A_U']*v for v in e['K_omega']]
    x=Fraction(prod,c['D']);amp=((x-1)*(2-x))**3 if 1<x<2 else Fraction(0);assert Fraction(*e['profile_amplitude_fraction'])==amp
    expected=complex(float(amp)*math.cos(float(x)/7),float(amp)*math.sin(float(x)/7));actual=complex(*map(float,e['W']));max_w_error=max(max_w_error,abs(actual-expected));assert abs(actual-expected)<2e-17
    with localcontext() as ctx:
     ctx.prec=85;re,im=map(Decimal,e['W']);ampd=Decimal(amp.numerator)/Decimal(amp.denominator)
     assert abs(re*re+im*im-ampd*ampd)<Decimal('1e-53')
     ar,ai=map(Decimal,e['A_T']);err=((ar-Decimal(e['A_U']))**2+ai*ai).sqrt();assert abs(err-Decimal(e['A_T_error']))<Decimal('1e-53')
    inert+=any(f['kind']=='inert' for f in row['factors']+col['factors'])
   checks+=1
 assert (checks,masked,inert)==(1218,786,42)
 rec=dict(passed=True,scope='Display-only exact-source mapping and double projection validation; no operator norms/Perron/scientific controls recomputed',payload_sha256=sha(payload),checker_sha256=sha(Path(__file__)),states_checked=checks,source_masked=masked,supported_inert_factor_entries=inert,ideal_factorizations_checked=len(ideals),all_saved_numeric_strings_exact=True,max_W_double_projection_error=max_w_error,W_projection_tolerance=2e-17,decimal_saved_value_consistency_tolerance='1e-53')
 out.parent.mkdir(parents=True,exist_ok=True);out.open('x').write(json.dumps(rec,indent=2,sort_keys=True)+'\n');print(json.dumps(rec))
if __name__=='__main__':main()
