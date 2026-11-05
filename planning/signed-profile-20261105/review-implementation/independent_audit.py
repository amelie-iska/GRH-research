#!/usr/bin/env python3
"""Independent all-six-case audit. No author SPF/case/test routine is called."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from itertools import product
from unittest.mock import patch
import hashlib,json,math,time
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104');B=R/'planning/signed-profile-20261105/review-implementation';O=R/'outputs/checks/2026-11-05-signed-profile/review-implementation';RUN=R/'outputs/experiments/2026-11-05-profile-uniformity-v2'
PINS=json.loads((B/'source-pins-v1.json').read_text());counts=Counter();started=time.monotonic()
def ck(x,key):
 if not x:raise AssertionError(key)
 counts[key]+=1

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bindings():
 ck(sha(RUN/'manifest.json')==PINS['manifest_sha256'],'bindings')
 for n,h in PINS['source_sha256'].items():ck(sha(R/n)==h,'bindings')
 for n,h in PINS['artifact_sha256'].items():ck(sha(RUN/n)==h,'bindings')
bindings();M=json.loads((RUN/'manifest.json').read_text());limit=2*max(M['D_values'])
# Ordinary Eratosthenes primes plus trial division, not author SPF.
sieve=bytearray(b'\1')*(limit+1);sieve[:2]=b'\0\0'
for p in range(2,math.isqrt(limit)+1):
 if sieve[p]:sieve[p*p::p]=b'\0'*(((limit-p*p)//p)+1)
PRIMES=[p for p in range(2,math.isqrt(limit)+2) if sieve[p]]
def factor(n):
 out=[]
 for p in PRIMES:
  if p*p>n:break
  e=0
  while n%p==0:n//=p;e+=1
  if e:out.append((p,e))
 if n>1:out.append((n,1))
 return out

def en(v):return v[0]**2-v[0]*v[1]+v[1]**2
def em(v,w):return(v[0]*w[0]-v[1]*w[1],v[0]*w[1]+v[1]*w[0]-v[1]*w[1])
def power(v,k):
 out=(1,0)
 for _ in range(k):out=em(out,v)
 return out

def div(v,w):
 n=en(w);x,y=em(v,(w[0]-w[1],-w[1]));return None if x%n or y%n else(x//n,y//n)
units=[(a,b) for a in range(-2,3) for b in range(-2,3) if en((a,b))==1]
def canon(v):return min(em(v,u) for u in units)
def elements(cap,primary=False):
 b=2*math.isqrt(cap)+2
 return sorted(((a,c) for a in range(-b,b+1) for c in range(-b,b+1) if 0<en((a,c))<=cap and (not primary or a%3==1 and c%3==0)),key=lambda v:(en(v),v))
vs=sorted({canon(v) for v in elements(64)},key=lambda v:(en(v),v));ck(len(vs)==40,'tower_enumeration')
small_primes=[]
for v in vs:
 n=en(v);p=math.isqrt(n)
 if (sieve[n] and (n==3 or n%3==1)) or (p*p==n and sieve[p] and p%3==2):small_primes.append(v)
V=[]
for v in vs:
 rem=v;fs={}
 for p in small_primes:
  e=0
  while True:
   q=div(rem,p)
   if q is None:break
   rem=q;e+=1
  if e:fs[p]=e
 ck(en(rem)==1,'tower_factorization');V.append({'g':v,'norm':en(v),'fs':fs,'support':set(fs),'good':en(v)%2!=0 and en(v)%3!=0,'row':em((1,1),power(v,6))})
# Formal prime keys retain both split ideals. Label order is fixed by canonical generators.
by_split={p:sorted(g for g in small_primes if en(g)==p) for p in range(2,65) if sieve[p] and p%3==1}
def vkeys(v):
 out=set()
 for g in v['support']:
  n=en(g)
  if n in (3,4):continue
  if sieve[n]:out.add((n,by_split[n].index(g)))
  else:out.add((math.isqrt(n),2))
 return out
for v in V:v['keys']=vkeys(v)

def norm_group(n):
 fs=factor(n)
 if any(p in (2,3) for p,e in fs):return None,'S_prime_2_or_3'
 ideal_norms=[];mandatory=set();choices=[]
 for p,e in fs:
  if p%3==1:
   if e>2:return None,'split_exponent_above_2'
   ideal_norms += [p]*e
   if e==2:mandatory.update(((p,0),(p,1)))
   else:choices.append(((p,0),(p,1)))
  else:
   if e!=2:return None,'inert_exponent_not_2'
   ideal_norms.append(p*p);mandatory.add((p,2))
 ds=sorted(math.prod(a for a,bit in zip(ideal_norms,bits) if bit) for bits in product((0,1),repeat=len(ideal_norms)))
 supports=[frozenset(mandatory|set(opts)) for opts in product(*choices)] if choices else [frozenset(mandatory)]
 return {'fs':fs,'pn':ideal_norms,'mu':(-1)**len(ideal_norms),'ds':ds,'supports':supports},None

def iroot(n,k):
 a,b=0,n+1
 while b-a>1:
  m=(a+b)//2
  if m**k<=n:a=m
  else:b=m
 return a
# Doubled rational/sqrt(-3) roots, independent of implementation complex routines.
ROOTS=((2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1))
small=json.loads((RUN/'independent-small-checks.json').read_text());reports=[];norm_total=0;allowed_total=0;min_count=None;min_energy=None;parsed_groups={};tower_tables={};summary_values={}
for D in M['D_values']:
 data=json.loads((RUN/f'norm-groups-D{D}.json').read_text());summary=json.loads((RUN/f'summary-D{D}.json').read_text());U=math.isqrt(D);ck(U*U==D and data['U']==summary['U']==U,'parameters')
 groups=data['active_norm_groups'];lookup={g['norm']:g for g in groups};rejected={};T=[0]*40;C=[0]*40;Acount=Asum=0;minus=0;xx=yy=0;hist_r=Counter();hist_a=Counter();hist_w=Counter();hist_phase=Counter();mine=[]
 for n in range(D+1,2*D):
  ind,why=norm_group(n)
  if why:rejected.setdefault(why,[]).append(n);ck(n not in lookup,'rejection_partition');continue
  g=lookup[n];r=sum(d>U and n//d>U for d in ind['ds']);a=ind['mu']*(r-1);mult=len(ind['supports']);phase=((n-1)//6)%6;wm=(-phase+(3 if a<0 else 0))%6;chi=-1 if phase%2 else 1;real=1 if a*chi>0 else -1
  ck(g['rational_prime_factors']==list(map(list,ind['fs'])) and g['ideal_prime_norms']==ind['pn'] and g['ideal_multiplicity']==mult and g['mu']==ind['mu'] and g['divisor_norms']==ind['ds'],'all_norm_group_factor_tables')
  ck(g['r_U']==r and g['A_U']==a and r%2==0 and a%2!=0,'all_coefficients')
  ck(g['chi_minus_one']==chi and g['chi_epsilon_exponent']==phase and g['order6_profile_node_exponent']==wm and tuple(g['order6_profile_node_zeta6'])==((ROOTS[wm][0]-ROOTS[wm][1])//2,ROOTS[wm][1]) and g['real_minus_one_profile_node']==real,'all_profile_nodes')
  ck(a*chi*real==abs(a) and ((phase+wm)%6==(0 if a>0 else 3)),'alignment')
  ck(Q(4*n-1,4*D)>1 and Q(4*n+1,4*D)<2,'bump_support_endpoints')
  for i,v in enumerate(V):
   allowed=sum(fs.isdisjoint(v['keys']) for fs in ind['supports']);ck(allowed==data['ideal_tower_family']['rows'][i]['allowed_norm_group_multiplicities'][len(mine)],'all_raw_mask_multiplicities');T[i]+=allowed*abs(a);C[i]+=allowed;allowed_total+=1
  Acount+=mult;Asum+=mult*abs(a);minus+=mult*a*chi;x,y=ROOTS[phase];xx+=mult*a*x;yy+=mult*a*y;hist_r[r]+=1;hist_a[a]+=1;hist_w[real]+=1;hist_phase[wm]+=1;mine.append((n,ind,a,wm));norm_total+=1
 ck(rejected==data['rejected_integer_norms'] and len(mine)+sum(map(len,rejected.values()))==D-1,'complete_integer_partition')
 ck(Acount==summary['active_squarefree_ideal_columns'] and Asum==summary['sum_abs_A_over_ideals'] and len(mine)==summary['active_norm_groups'],'summary_counts')
 for key,val in [('unit_row_energy',Q(Asum**2,D)),('main_order6_profile_energy',Q(Asum**2,D)),('energy_divided_by_D',Q(Asum**2,D**2)),('count_only_energy_lower_bound',Q(Acount**2,D)),('column_count_divided_by_D',Q(Acount,D)),('unsigned_real_minus_one_nodal_comparator_energy',Q(minus**2,D)),('unsigned_order6_nodal_comparator_energy',Q(xx*xx+3*yy*yy,4*D)),('unsigned_nodal_comparator_energy',Q(xx*xx+3*yy*yy,4*D))]:ck(Q(summary[key])==val,'summary_exact_energies')
 ck(summary['unsigned_order6_nodal_sum_zeta6']==[(xx-yy)//2,yy] and summary['unsigned_real_minus_one_nodal_sum_over_ideals']==minus,'unsigned_comparators')
 for key,h in [('r_U_norm_group_histogram',hist_r),('A_U_norm_group_histogram',hist_a),('real_minus_one_profile_node_histogram',hist_w),('order6_profile_node_exponent_histogram',hist_phase)]:ck(summary[key]=={str(k):v for k,v in h.items()},'summary_histograms')
 for i,(v,sv) in enumerate(zip(V,data['ideal_tower_family']['rows'])):
  actualfs={canon(tuple(f['generator'])):f['exponent'] for f in sv['factors']};ck(tuple(sv['generator_omega'])==v['g'] and sv['norm']==v['norm'] and actualfs==v['fs'] and sv['good_S']==v['good'] and sv['squarefree']==all(e==1 for e in v['fs'].values()),'all_tower_ideal_metadata')
  split=Counter();inert=[]
  for p,idx in v['keys']:
   if idx==2:inert.append(p)
   else:split[p]+=1
  ck(sv['split_prime_coverage']=={str(p):s for p,s in split.items()} and sv['inert_prime_coverage']==sorted(inert),'tower_coverage_serialization')
  ck(tuple(sv['literal_row_omega'])==v['row'] and sv['literal_row_norm']==v['norm']**6 and en(v['row'])==v['norm']**6,'literal_sixth_power_rows')
  ck(sv['T_v']==T[i] and sv['allowed_ideal_columns']==C[i] and Q(sv['row_energy'])==Q(T[i]**2,D),'tower_amplitude_energy')
 def stats(indices):return dict(rows=len(indices),energy=sum((Q(T[i]**2,D) for i in indices),Q(0)),sum_T_v=sum(T[i] for i in indices))
 for cap,sc in zip(data['ideal_tower_family']['caps'],summary['tower_cumulative_caps']):
  X=cap['X'];good=[i for i,v in enumerate(V) if v['good'] and v['norm']<=X];dyad=[i for i,v in enumerate(V) if v['good'] and X<=2*v['norm'] and v['norm']<X]
  ck(cap==sc and cap['H']==X**6 and cap['secondary_goodS_dyadic_interval']=='[X/2,X)','cumulative_dyadic_labels')
  for key,inds in [('primary_goodS_cumulative',good),('secondary_goodS_dyadic',dyad)]:
   got=stats(inds);saved=cap[key];ck(saved['rows']==got['rows'] and Q(saved['energy'])==got['energy'] and saved['sum_T_v']==got['sum_T_v'],'cumulative_dyadic_sums')
 matched=data['ideal_tower_family']['capacity_matched'];H=iroot(D**3,4);X=iroot(H,6);inds=[i for i,v in enumerate(V) if v['good'] and v['norm']<=X];expect=stats(inds)
 ck(matched==summary['capacity_matched_tower'] and matched['H_floor_D_3over4']==H and matched['X_floor_H_1over6']==X and matched['selected_goodS_cumulative']['rows']==expect['rows'] and Q(matched['selected_goodS_cumulative']['energy'])==expect['energy'] and matched['selected_goodS_cumulative']['sum_T_v']==expect['sum_T_v'],'canonical_capacity_matching')
 min_count=min(Q(Acount,D),min_count) if min_count is not None else Q(Acount,D);min_energy=min(Q(Asum**2,D**2),min_energy) if min_energy is not None else Q(Asum**2,D**2)
 reports.append(dict(D=D,U=U,norm_groups=len(mine),ideal_columns=Acount,sum_abs_A=Asum,energy=str(Q(Asum**2,D)),capacity_H=H,capacity_X=X,capacity_rows=expect['rows']))
 if D<=1024:parsed_groups[D]=(lookup,summary);tower_tables[D]=data['ideal_tower_family']['rows']
 print(json.dumps({'progress':'all norm/mask/summary tables PASS','D':D,'norm_groups':len(mine),'elapsed':round(time.monotonic()-started,2)}),flush=True)
 del data,groups,lookup,mine
ck(Q(M['minimum_observed_column_count_over_D'])==min_count and Q(M['minimum_observed_energy_over_D'])==min_energy,'manifest_minima')
# Independent actual ideals and finite fields for smallD, not author's helper enumeration.
primegens=[v for v in elements(2048,True) if en(v)%2 and en(v)%3 and ((sieve[en(v)] and en(v)%3==1) or (v[1]==0 and sieve[abs(v[0])] and abs(v[0])%3==2))]
def actual_factor(g):
 rem=g;out=[]
 for p in primegens:
  if en(p)>en(rem):break
  e=0
  while True:
   q=div(rem,p)
   if q is None:break
   rem=q;e+=1
  if e:out.append((p,e))
 ck(en(rem)==1,'actual_column_factorization');return out

def fp_symbol(fs,u):
 total=0
 for (a,b),e in fs:
  normp=a*a-a*b+b*b
  if b:
   p=normp;w=(-a*pow(b,-1,p))%p;z=(u[0]+u[1]*w)%p
   if z==0:return None
   value=pow(z,(p-1)//6,p);phase=[pow(1+w,k,p) for k in range(6)].index(value)
  else:
   p=abs(a);z=(u[0]%p,u[1]%p)
   if z==(0,0):return None
   def fm(x,y):return tuple(t%p for t in em(x,y))
   def pw(x,k):
    out=(1,0)
    while k:
     if k&1:out=fm(out,x)
     x=fm(x,x);k//=2
    return out
   value=pw(z,(p*p-1)//6);phase=[pw((1,1),k) for k in range(6)].index(value)
  total=(total+e*phase)%6
 return total
actual_columns=raw_symbols=raw_zeros=0;h1_controls=[]
for D in [256,1024]:
 lookup,summary=parsed_groups[D];U=math.isqrt(D);columns=[];aliascount=Counter()
 for g in elements(2*D,True):
  n=en(g)
  if not(D<n<2*D) or n%2==0 or n%3==0:continue
  fs=actual_factor(g)
  if any(e!=1 for p,e in fs):continue
  pn=[en(p) for p,e in fs];AU=0
  for placement in product((0,1,2),repeat=len(pn)):
   aa=math.prod(p for p,c in zip(pn,placement) if c==1);bb=math.prod(p for p,c in zip(pn,placement) if c==2)
   if aa<=U and bb<=U:AU+=(-1)**sum(c!=0 for c in placement)
  phase=fp_symbol(fs,(1,1));minus=fp_symbol(fs,(-1,0));row=lookup[n]
  ck(AU==row['A_U'] and phase==row['chi_epsilon_exponent'] and minus==(0 if row['chi_minus_one']==1 else 3),'direct_original_A_unit_symbols');aliascount[n]+=1;columns.append((g,fs,{canon(p) for p,e in fs},AU,row['order6_profile_node_exponent']));actual_columns+=1
 ck(dict(aliascount)=={n:v['ideal_multiplicity'] for n,v in lookup.items()},'direct_all_norm_fibers')
 expected=next(c for c in small['cases'] if c['D']==D);ck(expected['enumerated_ideal_columns']==len(columns),'saved_small_case_counts')
 for i,(v,saved) in enumerate(zip(V,expected['tower_rows'])):
  total=0;allowed=[];zeros=0
  for g,fs,support,a,w in columns:
   e=fp_symbol(fs,v['row']);survive=support.isdisjoint(v['support']);ck((e is not None)==survive,'direct_all_raw_zero_masks');raw_symbols+=1
   if survive:ck((e+w)%6==(0 if a>0 else 3),'direct_all_profile_alignment');total+=abs(a);allowed.append((support,abs(a)))
   else:zeros+=1;raw_zeros+=1
  h1=sum(a*b for fs,a in allowed for gs,b in allowed if fs.isdisjoint(gs))
  ck(total==saved['T_v'] and zeros==saved['raw_zero_columns'] and h1==saved['h1_ordered_pair_numerator'] and Q(saved['h1_selected_row_contribution'])==Q(h1,D),'direct_selected_h1_pair_sums')
  h1_controls.append((D,v['norm'],v['good'],h1))
 for cap in expected['cumulative_goodS_selected_h1']:
  X=cap['X'];selected=[Q(h,D) for dd,n,good,h in h1_controls if dd==D and good and n<=X]
  ck(cap['rows']==len(selected) and cap['H']==X**6 and Q(cap['selected_h1_contribution'])==sum(selected,Q(0)),'direct_cumulative_h1_sums')
# Negative controls use independent arithmetic and in-memory reads only.
N=1369;ds=[1,37,37,1369];ck(sum(d>32 and N//d>32 for d in ds)==2 and sum(d>32 and N//d>32 for d in set(ds))==1,'negative_divisor_deduplication')
rows49=[(v,tower_tables[256][i]) for i,v in enumerate(V) if v['norm']==49];ck(len(rows49)==3 and sorted(len([p for p in v['support'] if en(p)==7]) for v,s in rows49)==[1,1,2],'negative_norm_only_tower_keys');ck(min(s['T_v'] for v,s in rows49 if not s['squarefree'])>next(s['T_v'] for v,s in rows49 if s['squarefree']),'negative_prime_square_vs_split_product')
ck(fp_symbol([((1,3),1)],(1,1))==1 and all(k%6!=0 for k in range(1,6)),'nonprincipal_proper_powers')
ck(raw_zeros>0,'negative_primitive_restoration');ck(next(r for r in reports if r['D']==256)['energy']==str(Q(74**2,256)),'exact_unit_energy_control')
# Import ONLY public hash/output refusal contracts, never author compute/tests.
sys.path.insert(0,str(R/'examples/profile_uniformity'));import unit_profile as Author
original=Path.read_bytes;tamper=[]
for rel in ['examples/profile_uniformity/unit_profile.py','outputs/experiments/2026-11-05-profile-uniformity-v2/norm-groups-D256.json','outputs/experiments/2026-11-05-profile-uniformity-v2/summary-D256.json']:
 target=(R/rel).resolve()
 def reader(p):
  raw=original(p);return raw+b' reviewer in-memory alteration' if p.resolve()==target else raw
 with patch.object(Path,'read_bytes',reader):
  try:Author.verify_run(RUN)
  except RuntimeError as e:message=str(e)
  else:raise AssertionError('tamper accepted '+rel)
 ck('changed' in message.lower(),'tamper_refusal');tamper.append(dict(path=rel,refused=True,message=message))
try:Author.refuse_existing(RUN)
except FileExistsError:ck(True,'existing_output_refusal')
else:raise AssertionError('existing output accepted')
bindings()
receipt={'verdict':'PASS','scope':'Independent all-six-case norm/support/table/energy audit and actual smallD raw/h1 reconstruction; no asymptotic density proof, fixed-W/GRH claim or code/data changes','source_manifest_sha256':PINS['manifest_sha256'],'source_sha256':PINS['source_sha256'],'artifact_sha256':PINS['artifact_sha256'],'checks':dict(counts),'grouped_check_units':sum(counts.values()),'norm_groups_reconstructed':norm_total,'tower_allowed_multiplicities_reconstructed':allowed_total,'canonical_ideal_rows':40,'actual_small_ideal_columns':actual_columns,'actual_raw_symbols':raw_symbols,'actual_raw_zeros':raw_zeros,'small_selected_h1_rows':len(h1_controls),'cases':reports,'minimum_observed_column_count_over_D':str(min_count),'minimum_observed_energy_over_D':str(min_energy),'tamper_controls':tamper,'decoded_key_contract':'JSON split-prime-coverage keys are strings; normalize to integers before using int-key helper. Accepted generator uses fresh int-key objects and all saved allowed-mask vectors were independently checked.','not_run':'Author test suite/compute_case/run not invoked. No old15-column or training traces read. No browser, deps, Lean, auth or publication.','reviewer_sha256':sha(Path(__file__)),'elapsed_seconds':round(time.monotonic()-started,3)}
p=O/'independent-implementation-v1.json'
with p.open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps({'verdict':'PASS','checks':sum(counts.values()),'norm_groups':norm_total,'raw_symbols':raw_symbols,'elapsed':receipt['elapsed_seconds'],'receipt':str(p)}),flush=True)
