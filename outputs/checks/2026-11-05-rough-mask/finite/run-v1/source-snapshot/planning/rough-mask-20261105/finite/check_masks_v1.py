#!/usr/bin/env python3
"""Fresh exact AA rough-mask replacement, original coefficients and literal characters."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from math import isqrt
from fractions import Fraction
from itertools import product,combinations
import argparse,hashlib,json,time,types,resource,subprocess,traceback
RUN_OUTPUT=None
ROOT=Path(__file__).resolve().parents[3];HERE=Path(__file__).resolve().parent
HELPER='examples/profile_uniformity/ideal_tower.py';HELPER_SHA='77dc26658a188ff6669bf577fcb8298b875ab2a5e4f8e0bfe628b94c9b9430d4'
ROUGH='planning/signed-divisor-20261105/postrelease-research/smooth-rough-v1/SMOOTH_ROUGH_REDUCTION-v3.md';ROUGH_SHA='039548240acab66f883b6fc0d9bcee0e42a84fec5c390472ad501ef045e862c6'
PH=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))
CASES=((200,10,53,13,1,True),(512,16,107,19,1,True),(900,30,384,7,7,False))
sha=lambda b:hashlib.sha256(b).hexdigest()
def dump(v):return (json.dumps(v,sort_keys=True,separators=(',',':'))+'\n').encode()
def write(path,v):
 with path.open('xb') as f:f.write(dump(v))
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def neg(a):return(-a[0],-a[1])
def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def conj(a):return(a[0]-a[1],-a[1])
def norm(a):return a[0]*a[0]-a[0]*a[1]+a[1]*a[1]
def scale(a,k):return(a[0]*k,a[1]*k)
def total(xs):
 out=(0,0)
 for x in xs:out=add(out,x)
 return out
def subsets(ids):
 out=[()]
 for p in ids:out += [d+(p,) for d in out]
 return out
def node(D,N):
 if type(D)is not int or not 1<D<=1024:raise ValueError('Fixed profile nodes require integer1<D<=1024')
 return int(D<N<2*D)
def AU(ids,primes,U):
 value=0
 for places in product(range(3),repeat=len(ids)):
  x=y=1;parity=0
  for i,place in zip(ids,places):
   if place==0:x*=primes[i]['norm'];parity+=1
   elif place==1:y*=primes[i]['norm'];parity+=1
  if x<=U and y<=U:value+=(-1)**parity
 return value

def universe(cap,T):
 gens=sorted((g for g in T.elements(cap) if g[0]%3==1 and g[1]%3==0 and T.norm(g)%2 and T.norm(g)%3),key=lambda g:(T.norm(g),g))
 pg=[g for g in gens if T.prime(T.norm(g)) or(g[1]==0 and T.prime(abs(g[0])) and abs(g[0])%3==2)]
 primes=[dict(id=i,generator=g,norm=T.norm(g),kind='inert' if g[1]==0 else 'split',rational_prime=abs(g[0]) if g[1]==0 else T.norm(g)) for i,g in enumerate(pg)]
 ideals=[]
 for g in gens:
  rem=g;fs=[]
  for p in primes:
   e=0
   while (q:=T.quotient(rem,p['generator']))is not None:rem=q;e+=1
   if e:fs.append((p['id'],e))
  assert rem==(1,0)
  sf=all(e==1 for _,e in fs)
  ideals.append(dict(id=len(ideals),generator=g,norm=T.norm(g),factors=fs,squarefree=sf,prime_ids=tuple(i for i,e in fs),mu=(-1)**len(fs) if sf else 0))
 return primes,ideals

def compute(case,T,out):
 D,U,H,A1,A2,matched=case;assert U*U<=D and 2*D<=7*U*U
 started=time.monotonic_ns();primes,ideals=universe(2*D,T);sf=[a for a in ideals if a['squarefree']];byids={a['prime_ids']:a for a in sf}
 for a in sf:a['A']=AU(a['prime_ids'],primes,U)
 columns=[a for a in sf if D<=a['norm']<=2*D]
 rows=[]
 for a in sf:
  if not A1<=a['norm']<2*A1:continue
  for b in sf:
   if not A2<=b['norm']<2*A2 or set(a['prime_ids'])&set(b['prime_ids']):continue
   N=a['norm']*b['norm']**2
   if N>H:continue
   assert a['prime_ids']
   u=T.mul(a['generator'],T.power(b['generator'],2));assert T.norm(u)==N
   rows.append(dict(id=len(rows),v1=a['generator'],v2=b['generator'],u=u,N=N,v1_prime_ids=a['prime_ids'],v2_prime_ids=b['prime_ids'],literal_unit=(1,0),nonprincipal_reason='v1 prime valuation1 outsideS, with pairwise-coprime SF first factors'))
 if matched:assert H==T.integer_root(D**3,4)
 assert len(rows)=={200:5,512:7,900:2}[D]
 phases=[];locals_=[]
 for r in rows:
  lp=[T.direct_symbol([(p['generator'],1)],r['u']) for p in primes];locals_.append(lp)
  vals={}
  for a in sf:
   ps=[lp[i] for i in a['prime_ids']];vals[a['id']]=None if None in ps else sum(ps)%6
  phases.append(vals)
 smooth=[f for f in sf if all(primes[i]['norm']<=U for i in f['prime_ids'])]
 rough=[p for p in primes if p['norm']>U]
 incidence={}
 for m in columns:
  for ds in subsets(m['prime_ids']):incidence.setdefault(ds,[]).append(m)
 def val(ri,a):
  phase=phases[ri][a['id']]
  return (0,0) if phase is None else scale(PH[phase],a['A']*node(D,a['norm']))
 directrows=[];divisorrows=[]
 for ri,r in enumerate(rows):
  direct=(0,0)
  for a in columns:
   av=val(ri,a)
   for b in columns:
    if not set(a['prime_ids'])&set(b['prime_ids']):direct=add(direct,mul(av,conj(val(ri,b))))
  divsum=0
  for ds,cols in incidence.items():
   F=total(val(ri,a) for a in cols);divsum+=(-1)**len(ds)*norm(F)
  assert direct==(divsum,0);directrows.append(direct);divisorrows.append(divsum)
 states=[];smoothstates=[];unitpairs=[];rowstats=[];nonreal_pairs=[];rawintersection_count=0;allremoved=0
 counters=dict(raw_residual_zeros=0,auxiliary_nonSF_residual_terms=0,subunit_L_unit_residual_states=0,masked_f_states=0)
 def residuals(ri,f,P,pid=None):
  terms=[]
  for a in sf:
   N=f['norm']*P*a['norm']
   if not node(D,N) or set(a['prime_ids'])&set(f['prime_ids']):continue
   fa=byids[tuple(sorted(f['prime_ids']+a['prime_ids']))];phase=phases[ri][a['id']]
   v=(0,0) if phase is None else scale(PH[phase],fa['A'])
   removed=pid is not None and pid in a['prime_ids']
   if removed:assert f['norm']==1 and a['prime_ids']==(pid,) and fa['A']==1
   extended_generator=T.mul(T.mul(f['generator'],primes[pid]['generator']),a['generator']) if pid is not None else T.mul(f['generator'],a['generator'])
   terms.append(dict(extended_generator_omega=extended_generator,a_id=a['id'],fa_id=fa['id'],a_norm=a['norm'],original_A_fa=fa['A'],raw_phase=phase,value_omega=v,removed_by_p=removed,extended_column_norm=N,extended_fpa_squarefree=not removed,auxiliary_nonSF=removed))
  return terms
 for ri,row in enumerate(rows):
  sm=km=ks=dr=de=ct=0;intersection_subtracted=0;wrong_f_mask_buckets=0
  for f in smooth:
   fmask=all(locals_[ri][i] is not None for i in f['prime_ids']);mu=f['mu']
   terms=residuals(ri,f,1);Tfull=total(t['value_omega'] for t in terms)
   rawF=total(val(ri,m) for m in incidence.get(f['prime_ids'],[]))
   assert norm(rawF)==int(fmask)*norm(Tfull)
   sm+=mu*int(fmask)*norm(Tfull)
   if not fmask and norm(Tfull):wrong_f_mask_buckets+=1
   smoothstates.append(dict(row=ri,f=f['id'],f_raw_mask=fmask,mu_f=mu,T_omega=Tfull,original_Fd_omega=rawF,terms=terms,contribution_raw=mu*int(fmask)*norm(Tfull)))
   for p in rough:
    P=p['norm']
    if f['norm']*P>2*D:continue
    pid=p['id'];terms=residuals(ri,f,P,pid);Tp=total(t['value_omega'] for t in terms);Tmasked=total(t['value_omega'] for t in terms if not t['removed_by_p']);pMask=locals_[ri][pid] is not None
    zp=scale(PH[locals_[ri][pid]],node(D,P*P)) if pMask else (0,0)
    assert add(Tp,neg(Tmasked))==(zp if f['norm']==1 else (0,0))
    ds=tuple(sorted(f['prime_ids']+(pid,)));rawFd=total(val(ri,m) for m in incidence.get(ds,[]))
    assert norm(rawFd)==int(fmask and pMask)*norm(Tmasked)
    fullpair=maskedpair=rowpair=respair=bothpair=overlap=(0,0)
    for a in terms:
     for b in terms:
      z=mul(a['value_omega'],conj(b['value_omega']));fullpair=add(fullpair,z)
      if pMask and not a['removed_by_p'] and not b['removed_by_p']:maskedpair=add(maskedpair,z)
      if not pMask:rowpair=add(rowpair,z)
      if pMask and(a['removed_by_p'] or b['removed_by_p']):respair=add(respair,z)
      if a['removed_by_p'] and b['removed_by_p']:bothpair=add(bothpair,z)
      if not pMask and(a['removed_by_p'] or b['removed_by_p']):overlap=add(overlap,z);rawintersection_count+=1
      if z[1] and len(nonreal_pairs)<12:nonreal_pairs.append(dict(row=ri,f=f['id'],p=pid,a=a['a_id'],b=b['a_id'],oriented_omega=z))
    assert fullpair==(norm(Tp),0) and maskedpair==(int(pMask)*norm(Tmasked),0)
    assert add(rowpair,respair)==add(fullpair,neg(maskedpair)) and overlap==(0,0)
    exactres=2*mul(Tp,conj(zp))[0]-mul(Tp,conj(zp))[1]-norm(zp) # twice the real part in omega basis
    assert respair==(exactres if pMask and f['norm']==1 else 0,0)
    if f['norm']==1:assert bothpair==(norm(zp),0)
    ks+=mu*int(fmask)*norm(Tp);km+=mu*int(fmask and pMask)*norm(Tmasked)
    dr+=mu*int(fmask and not pMask)*norm(Tp)
    de+=int(pMask and f['norm']==1)*exactres
    if f['norm']==1 and pMask:intersection_subtracted+=norm(zp)
    allremoved+=sum(t['removed_by_p'] for t in terms)
    counters['raw_residual_zeros']+=sum(t['raw_phase'] is None for t in terms)
    counters['auxiliary_nonSF_residual_terms']+=sum(t['removed_by_p'] for t in terms)
    counters['masked_f_states']+=int(not fmask and bool(terms))
    low=Fraction(D,f['norm']*P)
    if Fraction(1,2)<low<1 and any(t['a_norm']==1 for t in terms):counters['subunit_L_unit_residual_states']+=1
    states.append(dict(row=ri,f=f['id'],p=pid,P=P,f_raw_mask=fmask,p_raw_mask=pMask,mu_f=mu,lower_support=str(low),terms=terms,T_omega=Tp,T_p_masked_omega=Tmasked,z_p_omega=zp if f['norm']==1 else (0,0),original_F_fp_omega=rawFd,full_square=norm(Tp),masked_square=int(pMask)*norm(Tmasked),direct_residual_pair_components=dict(full=fullpair,actual=maskedpair,row=rowpair,residual=respair,both_residual=bothpair,row_residual_overlap=overlap),delta_residual_formula=exactres if f['norm']==1 and pMask else 0))
  wrong_repeated=0
  for p in rough:
   if node(D,p['norm']**2) and locals_[ri][p['id']] is not None:wrong_repeated+=1
  for p,q in combinations(rough,2):
   if not node(D,p['norm']*q['norm']):continue
   mask=locals_[ri][p['id']] is not None and locals_[ri][q['id']] is not None
   ids=tuple(sorted((p['id'],q['id'])));m=byids[ids];assert m['A']==1 and incidence[ids]==[m]
   ct+=int(mask);unitpairs.append(dict(row=ri,p=p['id'],q=q['id'],original_column=m['id'],norm=m['norm'],row_raw_mask=mask,contribution_raw=int(mask),unordered_distinct_ideal_pair=True))
  assert ks-km==dr+de
  assert directrows[ri]==(sm-km+ct,0)==(sm-ks+ct+dr+de,0)
  rowstats.append(dict(row=ri,original_AA_raw=directrows[ri],direct_divisor_raw=divisorrows[ri],smooth_raw=sm,K_mask_raw=km,K_S_raw=ks,unit_two_rough_raw=ct,Delta_raw=ks-km,Delta_row_raw=dr,Delta_residual_raw=de,residual_intersection_subtraction_raw=intersection_subtracted,wrong_repeated_prime_unit_extra_raw=wrong_repeated,wrong_f_mask_nonzero_buckets=wrong_f_mask_buckets))
 result={k:sum(r[k] for r in rowstats) for k in ['smooth_raw','K_mask_raw','K_S_raw','unit_two_rough_raw','Delta_raw','Delta_row_raw','Delta_residual_raw','residual_intersection_subtraction_raw','wrong_repeated_prime_unit_extra_raw']}
 rawAA=total(directrows);assert rawAA[1]==0
 result['original_AA_raw']=rawAA[0];result['S_only_replaced_AA_raw']=result['smooth_raw']-result['K_S_raw']+result['unit_two_rough_raw']
 assert result['original_AA_raw']-result['S_only_replaced_AA_raw']==result['Delta_raw']
 assert result['unit_two_rough_raw']>0 and result['residual_intersection_subtraction_raw']>0 and result['wrong_repeated_prime_unit_extra_raw']>0 and nonreal_pairs
 if D==900:assert result['Delta_row_raw']==0 and counters['masked_f_states']>0
 else:assert result['Delta_row_raw']>0
 assert counters['subunit_L_unit_residual_states']>0 and allremoved>0
 if D!=900:assert rawintersection_count>0
 else:assert rawintersection_count==0
 rational_controls=[]
 for ri,row in enumerate(rows):
  for p in primes:
   if any(p['id']!=q and p['norm']==primes[q]['norm'] for q in row['v1_prime_ids']) and locals_[ri][p['id']] is not None:
    rational_controls.append(dict(row=ri,p=p['id'],ideal_coprime=True,rational_norm_mask_would_delete=True,raw_phase=locals_[ri][p['id']]))
 assert rational_controls if D!=900 else True
 parameters=dict(D=D,U=U,H=H,A1=A1,A2=A2,capacity_is_floor_D_3over4=matched,capacity_scope='floorD^.75' if matched else 'explicit fixture H384, notfloorD^.75',literal_unit=1,nu='principal1',S='primesabove2,3',profile=dict(fixed_delta='1/4096',finite_grid='integer1<D<=1024',strict_node_weight=1,endpoint_weight=0,derivative_cost='O_k4096^k, large fixed constants; no asymptotic estimate'),AA_only=True)
 data=dict(schema='fresh-rough-mask-finite-v1',passed=True,parameters=parameters,prime_ideals=primes,all_good_ideals=ideals,original_columns=[m['id'] for m in columns],rows=rows,all_SF_residual_raw_phases=[{str(k):v for k,v in r.items()} for r in phases],smooth_states=smoothstates,rough_states=states,unit_two_rough_pairs=unitpairs,row_totals=rowstats,raw_totals=result,normalized_by_D_once={k:str(Fraction(v,D)) for k,v in result.items()},counts=dict(original_columns=len(columns),actual_rows=len(rows),all_ideals=len(ideals),SF_ideals=len(sf),rough_prime_states=len(states),nonreal_oriented_samples=len(nonreal_pairs),raw_row_residual_intersection_pairs=rawintersection_count,**counters),nonreal_oriented_samples=nonreal_pairs,rational_norm_mask_negative_controls=rational_controls,negative_controls=dict(omit_unit_correction_changes_raw_AA=result['unit_two_rough_raw'],omit_row_correction_changes_raw_AA=result['Delta_row_raw'],omit_residual_intersection_changes_raw_AA=result['residual_intersection_subtraction_raw'],include_repeated_rough_prime_pairs_adds_false_units=result['wrong_repeated_prime_unit_extra_raw'],nonSF_auxiliary_columns_never_original=True),scope='NEW finite exact AA identities only, different declared row blocks. No asymptotic saving, GRH, globalPSD, allnine-channel replacement or learning claim.',elapsed_ns=time.monotonic_ns()-started)
 write(out/f'D{D}-v1.json',data)
 return dict(D=D,parameters=parameters,counts=data['counts'],raw_totals=result,normalized_by_D_once=data['normalized_by_D_once'],elapsed_ns=data['elapsed_ns'])

def main():
 global RUN_OUTPUT
 p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path);a=p.parse_args();out=a.out if a.out.is_absolute() else ROOT/a.out
 if out.exists():raise FileExistsError('Preserve existing output: '+str(out))
 out.mkdir(parents=True);RUN_OUTPUT=out
 protected=dict(HEAD=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),index_sha256=sha((ROOT/'.git/index').read_bytes()))
 assert mul((1,1),conj((1,1)))==(1,0) and mul((1,1),(1,-1))!=(1,0)
 paths=[str(q.relative_to(ROOT)) for q in sorted(HERE.iterdir()) if q.is_file()]+[HELPER,ROUGH];captured={p:(ROOT/p).read_bytes() for p in paths};assert sha(captured[HELPER])==HELPER_SHA and sha(captured[ROUGH])==ROUGH_SHA
 snap=out/'source-snapshot';snap.mkdir()
 for p,raw in captured.items():
  q=snap/p;q.parent.mkdir(parents=True,exist_ok=True)
  with q.open('xb') as f:f.write(raw)
 pins={p:dict(sha256=sha(raw),bytes=len(raw)) for p,raw in captured.items()};write(out/'source-freeze.json',dict(files=pins,pure_helper_only=True,no_accepted_run_import=True))
 T=types.ModuleType('fresh_rough_tower');T.__file__=str(ROOT/HELPER);exec(compile(captured[HELPER],str(ROOT/HELPER),'exec'),T.__dict__)
 started=time.monotonic_ns();results=[compute(case,T,out) for case in CASES]
 assert all(sha((ROOT/p).read_bytes())==pin['sha256'] for p,pin in pins.items())
 assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==protected['HEAD'] and sha((ROOT/'.git/index').read_bytes())==protected['index_sha256']
 summary=dict(passed=True,protected_source_state=protected,cases=results,elapsed_ns=time.monotonic_ns()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,source_unchanged=True,old_runs_executed=False,no_publication_or_index_actions=True)
 write(out/'summary.json',summary);files={str(q.relative_to(out)):dict(bytes=q.stat().st_size,sha256=sha(q.read_bytes())) for q in sorted(out.rglob('*')) if q.is_file()};write(out/'manifest.json',dict(passed=True,files=files,scope='Fresh exact rough-mask finite identities, no analytic saving/GRH'))
 print(json.dumps(summary,sort_keys=True))
if __name__=='__main__':
 try:main()
 except Exception as error:
  if RUN_OUTPUT is not None:write(RUN_OUTPUT/'failure.json',dict(passed=False,error_type=type(error).__name__,error=str(error),traceback=traceback.format_exc(),source_sha256=sha(Path(__file__).read_bytes())))
  raise
