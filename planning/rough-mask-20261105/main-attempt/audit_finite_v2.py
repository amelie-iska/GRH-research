"""Independent fresh rough-mask audit; pure arithmetic, no author/old imports."""
from pathlib import Path
from math import gcd,isqrt
from itertools import product,combinations
from collections import Counter,defaultdict
from fractions import Fraction
import hashlib,json,datetime,time,traceback,resource,os
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104');INPUT=R/'outputs/checks/2026-11-05-rough-mask/finite/run-v1';OUT=R/'outputs/checks/2026-11-05-rough-mask/main-attempt'
sha=lambda b:hashlib.sha256(b).hexdigest()
def norm(g):a,b=g;return a*a-a*b+b*b
def mul(g,h):a,b=g;c,d=h;return a*c-b*d,a*d+b*c-b*d
def conj(g):a,b=g;return a-b,-b
def div(g,h):a,b=mul(g,conj(h));n=norm(h);return (a//n,b//n)if a%n==b%n==0 else None
def add(g,h):return g[0]+h[0],g[1]+h[1]
def scale(c,g):return c*g[0],c*g[1]
def prime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
def pinorm(n):return prime(n)and n%3==1 or isqrt(n)**2==n and prime(isqrt(n))and isqrt(n)%3==2
UNITS=[(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]
def value(ph):return (0,0)if ph is None else UNITS[ph]
def sumv(xs):
 z=(0,0)
 for x in xs:z=add(z,x)
 return z

def run_case(D):
 raw=(INPUT/f'D{D}-v1.json').read_bytes();d=json.loads(raw);param=d['parameters'];assert d['passed'];U=param['U'];H=param['H'];A1=param['A1'];A2=param['A2'];cap=2*D
 assert U*U<=D and 2*D<=7*U*U and param['nu']=='principal1' and param['literal_unit']==1
 assert param['profile']['fixed_delta']=='1/4096' and D<=1024 and Fraction(1,D)>=Fraction(4,4096)
 if param['capacity_is_floor_D_3over4']:assert H**4<=D**3<(H+1)**4
 else:assert D==900 and H==384 and H**4>D**3
 b=isqrt((4*cap+2)//3)+2
 ideals=sorted([(a,c)for a in range(-b,b+1)for c in range(-b,b+1)if a%3==1 and c%3==0 and 1<=norm((a,c))<=cap and gcd(norm((a,c)),6)==1],key=lambda g:(norm(g),g))
 records=d['all_good_ideals'];assert [tuple(x['generator'])for x in records]==ideals
 iid={g:i for i,g in enumerate(ideals)};Ns=list(map(norm,ideals));ps=[tuple(x['generator'])for x in d['prime_ideals']];assert len(ps)==len(set(ps))
 expected_primes={g for g in ideals if pinorm(norm(g))};assert set(ps)==expected_primes
 pn=list(map(norm,ps))
 for i,x in enumerate(d['prime_ideals']):
  assert x['id']==i and x['norm']==pn[i];p=pn[i]if prime(pn[i])else isqrt(pn[i]);assert x['rational_prime']==p and x['kind']==('split'if prime(pn[i])else'inert')
 def factor(g):
  rem=g;fac=[]
  for i,p in sorted(enumerate(ps),key=lambda x:(pn[x[0]],x[1])):
   while norm(rem)>=pn[i]:
    q=div(rem,p)
    if q is None:break
    rem=q;fac.append(i)
  assert rem==(1,0),g
  return tuple(sorted(fac))
 fac=[factor(g)for g in ideals];sets=[set(f)for f in fac];sf=[i for i,f in enumerate(fac)if len(f)==len(set(f))];sfset=set(sf);acache={}
 def AU(f):
  f=tuple(sorted(f));assert len(f)==len(set(f))
  if f in acache:return acache[f]
  v=0
  for places in product(range(3),repeat=len(f)):
   x=y=1;k=0
   for p,place in zip(f,places):
    if place==0:x*=pn[p];k+=1
    elif place==1:y*=pn[p];k+=1
   if x<=U and y<=U:v+=(-1)**k
  acache[f]=v;return v
 Avec={i:AU(fac[i])for i in sf};mu=[(-1)**len(f)if i in sfset else 0 for i,f in enumerate(fac)]
 for i,x in enumerate(records):
  assert x['id']==i and x['norm']==Ns[i] and x['prime_ids']==sorted(sets[i]) and x['factors']==[[p,k]for p,k in sorted(Counter(fac[i]).items())] and x['mu']==mu[i] and x['squarefree']==(i in sfset)
  if i in sfset:assert x['A']==Avec[i]
  else:assert 'A'not in x
 cols=[i for i in sf if D<=Ns[i]<=2*D];assert d['original_columns']==cols
 # Reconstruct the complete literal row block, not a selected submatrix.
 v1s=[i for i in sf if A1<=Ns[i]<2*A1];v2s=[i for i in sf if A2<=Ns[i]<2*A2];expected_rows={}
 for a in v1s:
  for b2 in v2s:
   if sets[a]&sets[b2]:continue
   u=mul(ideals[a],mul(ideals[b2],ideals[b2]))
   if norm(u)<=H:expected_rows[(ideals[a],ideals[b2])]=u
 rows=d['rows'];assert len(rows)==len(expected_rows);assert len({(tuple(x['v1']),tuple(x['v2']))for x in rows})==len(rows)
 for i,x in enumerate(rows):
  v1=tuple(x['v1']);v2=tuple(x['v2']);u=tuple(x['u']);assert x['id']==i and expected_rows[v1,v2]==u and x['N']==norm(u)<=H and x['literal_unit']==[1,0]
  assert x['v1_prime_ids']==list(fac[iid[v1]]) and x['v2_prime_ids']==list(fac[iid[v2]]) and fac[iid[v1]]
  assert all(Counter(factor(u))[p]==1 for p in fac[iid[v1]])
 def fieldpow(g,e,p):
  v=(1,0)
  while e:
   if e&1:v=tuple(x%p for x in mul(v,g))
   g=tuple(x%p for x in mul(g,g));e//=2
  return v
 def localphase(i,u):
  pg=ps[i];q=pn[i]
  if prime(q):
   lam=(-pg[0]*pow(pg[1],-1,q))%q;assert (lam*lam+lam+1)%q==0;z=(u[0]+u[1]*lam)%q
   if z==0:return None
   z=pow(z,(q-1)//6,q);units=[pow((1+lam)%q,k,q)for k in range(6)];assert len(set(units))==6;return units.index(z)
  p=isqrt(q);z=(u[0]%p,u[1]%p)
  if z==(0,0):return None
  z=fieldpow(z,(q-1)//6,p);units=[tuple(x%p for x in t)for t in UNITS];assert len(set(units))==6;return units.index(z)
 phases=[];local=[];phasechecks=0
 for ri,row in enumerate(rows):
  u=tuple(row['u']);lp=[localphase(i,u)for i in range(len(ps))];local.append(lp);ph={}
  for i in sf:
   vals=[lp[p]for p in fac[i]];ph[i]=None if any(x is None for x in vals)else sum(vals)%6
  expected={str(i):ph[i]for i in sf};assert d['all_SF_residual_raw_phases'][ri]==expected;phasechecks+=len(expected);phases.append(ph)
 # Direct original AA and complete ideal-divisor sums, including self divisors.
 divisors=set()
 for i in cols:
  ids=fac[i]
  for bits in product([0,1],repeat=len(ids)):divisors.add(tuple(p for p,bv in zip(ids,bits)if bv))
 direct=[];fd=[]
 for ri in range(len(rows)):
  vals={i:scale(Avec[i],value(phases[ri][i]))if D<Ns[i]<2*D else(0,0)for i in cols};z=(0,0)
  for i in cols:
   for j in cols:
    if not sets[i]&sets[j]:z=add(z,mul(vals[i],conj(vals[j])))
  buckets={f:sumv(vals[i]for i in cols if set(f)<=sets[i])for f in divisors};inv=sum((-1)**len(f)*norm(v)for f,v in buckets.items());assert z==(inv,0)
  direct.append(inv);fd.append(buckets)
 smooth=[i for i in sf if all(pn[p]<=U for p in fac[i])];rough=[p for p in range(len(ps))if pn[p]>U]
 own_smooth={};own_rough={};rowcalc=[defaultdict(int)for _ in rows];transfers=0;aux=0;activecoef=0;termschecked=0
 def terms(fi,p):
  F=Ns[fi];P=1 if p is None else pn[p];out=[]
  for ai in sf:
   if sets[fi]&sets[ai]or not D<F*P*Ns[ai]<2*D:continue
   fg=mul(ideals[fi],ideals[ai]);faid=iid[fg];m=fg if p is None else mul(fg,ps[p]);removed=p is not None and p in sets[ai]
   out.append((ai,faid,m,removed))
  return out
 termsets={};
 for fi in smooth:
  t=terms(fi,None)
  termsets[fi,None]=t
  for p in rough:
   if Ns[fi]*pn[p]>=2*D:continue
   t=terms(fi,p)
   termsets[fi,p]=t
 for ri,row in enumerate(rows):
  for (fi,p),tt in termsets.items():
   fmask=phases[ri][fi]is not None;Pnorm=1 if p is None else pn[p];lp=0 if p is None else local[ri][p];pmask=lp is not None;values={};term_records=[]
   for ai,faid,m,removed in tt:
    v=scale(Avec[faid],value(phases[ri][ai]));values[ai]=(v,removed);termschecked+=1
    extsf=len(factor(m))==len(set(factor(m)));assert extsf==(not removed)
    term_records.append(dict(a_id=ai,a_norm=Ns[ai],fa_id=faid,original_A_fa=Avec[faid],raw_phase=phases[ri][ai],value_omega=list(v),removed_by_p=removed,auxiliary_nonSF=not extsf,extended_fpa_squarefree=extsf,extended_column_norm=norm(m),extended_generator_omega=list(m)))
    if p is not None:
     assert Ns[faid]<7*U and Avec[faid]==mu[faid]*(2*(Ns[faid]<=U)-1) and abs(Avec[faid])==1;activecoef+=1;aux+=not extsf
   T=sumv(v for v,r in values.values());base=dict(row=ri,f=fi,mu_f=mu[fi],f_raw_mask=fmask,T_omega=list(T),terms=term_records)
   if p is None:
    bucket=fd[ri].get(fac[fi],(0,0));assert bucket==mul(value(phases[ri][fi]),T);transfers+=1;base.update(original_Fd_omega=list(bucket),contribution_raw=mu[fi]*int(fmask)*norm(T));own_smooth[ri,fi]=base;rowcalc[ri]['smooth_raw']+=base['contribution_raw'];continue
   Tp=sumv(v for v,r in values.values()if not r);z=scale(1,value(lp))if fi==0 and D<Pnorm*Pnorm<2*D else(0,0)
   assert add(T,scale(-1,Tp))==z
   components={k:(0,0)for k in ['full','actual','row','residual','both_residual','row_residual_overlap']}
   for va,ra in values.values():
    for vb,rb in values.values():
     v=mul(va,conj(vb));flags={'full':True,'actual':pmask and not(ra or rb),'row':not pmask,'residual':pmask and(ra or rb),'both_residual':ra and rb,'row_residual_overlap':not pmask and(ra or rb)}
     for k,take in flags.items():
      if take:components[k]=add(components[k],v)
   assert components['full']==(norm(T),0) and components['actual']==(int(pmask)*norm(Tp),0) and components['row_residual_overlap']==(0,0)
   prod=mul(T,conj(z));delta=(2*prod[0]-prod[1]-norm(z))if pmask else 0;assert components['residual']==(delta,0)
   common=tuple(sorted(fac[fi]+(p,)));bucket=fd[ri].get(common,(0,0));assert bucket==mul(mul(value(phases[ri][fi]),value(lp)),Tp);transfers+=1
   base.update(p=p,P=Pnorm,p_raw_mask=pmask,T_p_masked_omega=list(Tp),z_p_omega=list(z),full_square=norm(T),masked_square=int(pmask)*norm(Tp),original_F_fp_omega=list(bucket),lower_support=str(Fraction(D,Ns[fi]*Pnorm)),delta_residual_formula=delta,direct_residual_pair_components={k:list(v)for k,v in components.items()})
   own_rough[ri,fi,p]=base;c=mu[fi]*int(fmask);rowcalc[ri]['K_S_raw']+=c*norm(T);rowcalc[ri]['K_mask_raw']+=c*int(pmask)*norm(Tp);rowcalc[ri]['Delta_row_raw']+=c*components['row'][0];rowcalc[ri]['Delta_residual_raw']+=c*delta;rowcalc[ri]['residual_intersection_subtraction_raw']+=c*components['both_residual'][0]
 assert len(own_smooth)==len(d['smooth_states']) and len(own_rough)==len(d['rough_states'])
 for s in d['smooth_states']:assert s==own_smooth[s['row'],s['f']],('smooth',s['row'],s['f'])
 for s in d['rough_states']:assert s==own_rough[s['row'],s['f'],s['p']],('rough',s['row'],s['f'],s['p'])
 pairs=[]
 for ri,row in enumerate(rows):
  for p,q in combinations(rough,2):
   N=pn[p]*pn[q]
   if not D<N<2*D:continue
   pg=mul(ps[p],ps[q]);ci=iid[pg];assert ci in cols and fac[ci]==tuple(sorted([p,q]));mask=local[ri][p]is not None and local[ri][q]is not None
   pairs.append(dict(row=ri,p=p,q=q,norm=N,original_column=ci,row_raw_mask=mask,contribution_raw=int(mask),unordered_distinct_ideal_pair=True));rowcalc[ri]['unit_two_rough_raw']+=int(mask)
  rowcalc[ri]['wrong_repeated_prime_unit_extra_raw']=sum(int(local[ri][p]is not None)for p in rough if D<pn[p]**2<2*D)
 assert pairs==d['unit_two_rough_pairs']
 for ri,r in enumerate(rowcalc):
  r['Delta_raw']=r['K_S_raw']-r['K_mask_raw'];r['original_AA_raw']=direct[ri];r['S_only_replaced_AA_raw']=r['smooth_raw']-r['K_S_raw']+r['unit_two_rough_raw'];assert r['Delta_raw']==r['Delta_row_raw']+r['Delta_residual_raw'];assert direct[ri]==r['smooth_raw']-r['K_mask_raw']+r['unit_two_rough_raw']
  saved=d['row_totals'][ri]
  for k,v in r.items():
   if k=='S_only_replaced_AA_raw':continue
   assert saved[k]==([v,0]if k=='original_AA_raw'else v),(D,ri,k,saved[k],v)
  assert saved['direct_divisor_raw']==direct[ri]
 totals={k:sum(r[k]for r in rowcalc)for k in d['raw_totals']};assert totals==d['raw_totals'];assert {k:str(Fraction(v,D))for k,v in totals.items()}==d['normalized_by_D_once']
 for sample in d['nonreal_oriented_samples']:
  s=own_rough[sample['row'],sample['f'],sample['p']];ts={t['a_id']:tuple(t['value_omega'])for t in s['terms']};v=mul(ts[sample['a']],conj(ts[sample['b']]));assert list(v)==sample['oriented_omega'] and v[1]!=0
 for x in d['rational_norm_mask_negative_controls']:
  ri=x['row'];p=x['p'];assert local[ri][p]==x['raw_phase'] and local[ri][p]is not None and gcd(pn[p],rows[ri]['N'])>1 and x['ideal_coprime'] and x['rational_norm_mask_would_delete']
 assert d['counts']['original_columns']==len(cols) and d['counts']['actual_rows']==len(rows) and d['counts']['all_ideals']==len(ideals) and d['counts']['SF_ideals']==len(sf) and d['counts']['rough_prime_states']==len(own_rough) and d['counts']['auxiliary_nonSF_residual_terms']==aux
 return dict(passed=True,D=D,U=U,H=H,A1=A1,A2=A2,input_sha256=sha(raw),all_good_ideals=len(ideals),SF_ideals=len(sf),prime_ideals=len(ps),columns=len(cols),rows=len(rows),literal_residual_phases_compared=phasechecks,smooth_states=len(own_smooth),rough_states=len(own_rough),original_complex_Fd_transfers=transfers,residual_term_records_compared=termschecked,active_rough_unit_coefficient_occurrences=activecoef,auxiliary_nonSF_terms=aux,ordered_original_pair_visits=len(rows)*len(cols)**2,all_raw_totals=totals,critical_capacity=H**4<=D**3,direct_row_AA=direct)

def main():
 start=time.monotonic();manifest=(INPUT/'manifest.json').read_bytes();assert sha(manifest)=='d8ebdc9410e0e24c3dfd999ea33c10864d28b4e9f008913e08d26233217268cf';m=json.loads(manifest)
 for n,x in m['files'].items():assert sha((INPUT/n).read_bytes())==x['sha256'] and (INPUT/n).stat().st_size==x['bytes']
 cases=[]
 for D in [200,512,900]:
  case=run_case(D);cases.append(case);p=OUT/f'independent-finite-D{D}-v2.json';assert not p.exists();p.write_text(json.dumps(case,indent=2,sort_keys=True)+'\n');print(json.dumps({'D':D,'passed':True,'AA':case['all_raw_totals']['original_AA_raw'],'Delta':case['all_raw_totals']['Delta_raw']}),flush=True)
 for n,x in m['files'].items():assert sha((INPUT/n).read_bytes())==x['sha256']
 report=dict(passed=True,cases=cases,input_manifest_sha256=sha(manifest),checker_sha256=sha(Path(__file__).read_bytes()),elapsed_seconds=time.monotonic()-start,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,author_checker_or_old_imports_executed=False,source_data_changed=False,scope='Independent NEW AA finite reconstruction only; no asymptotic/GRH claim, no oldrun/data reads')
 p=OUT/'independent-finite-v2.json';assert not p.exists();p.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n');print(json.dumps({'passed':True,'receipt':str(p),'sha256':sha(p.read_bytes()),'seconds':report['elapsed_seconds']}))
if __name__=='__main__':
 try:main()
 except BaseException as e:
  p=OUT/'independent-finite-failure-v2.json';assert not p.exists();p.write_text(json.dumps({'passed':False,'error':repr(e),'traceback':traceback.format_exc(),'checker_sha256':sha(Path(__file__).read_bytes()),'source_data_changed':False},indent=2)+'\n');raise
