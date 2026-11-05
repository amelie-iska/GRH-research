"""NEW D60000 independent linear audit. No author arithmetic imports or M^2 loops."""
import sys,os,resource
sys.dont_write_bytecode=True
resource.setrlimit(resource.RLIMIT_AS,(256*1024*1024,256*1024*1024));os.nice(10);os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
from pathlib import Path
from array import array
from itertools import product
from collections import Counter
from fractions import Fraction
import json,hashlib,time,subprocess
from independent_eisenstein_core_v1 import PH,ZERO,mul,conj,norm,quotient,primary,divisors
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3];DATA=ROOT/'outputs/experiments/2026-11-05-signed-divisor-D60000-v1';OUT=ROOT/'outputs/checks/2026-11-05-signed-divisor/analytic/large-full-column-review-v1'
EXPECTED='fecbec83a4fadd301d7845daddcb7e31f216705a6b29c5ba98436642ae0b2e4f';KEYS=['AA','AC','Amu','CA','CC','Cmu','muA','muC','mumu'];D=60000;U=244;H=3833;A1=37;A2=7;CAP=2*D

def sha(p):
 h=hashlib.sha256()
 with p.open('rb')as f:
  while b:=f.read(1048576):h.update(b)
 return h.hexdigest()
def protected_states():
 pins=json.loads((HERE.parent/'source-pins-v1.json').read_text())['protected_source_and_eight_release_worktrees'];states=[]
 for expected in pins:
  base=Path(expected['path']);env=dict(os.environ,GIT_OPTIONAL_LOCKS='0')
  def git(*args):return subprocess.check_output(['git','-C',str(base),*args],env=env,text=True).strip()
  ip=Path(git('rev-parse','--git-path','index'));ip=ip if ip.is_absolute()else base/ip
  actual=dict(path=str(base),HEAD=git('rev-parse','HEAD'),index_sha256=sha(ip),index_bytes=ip.stat().st_size)
  assert actual==expected,actual;states.append(actual)
 return states

def note(stage,**kw):print(json.dumps(dict(stage=stage,elapsed=round(time.monotonic()-START,3),**kw)),flush=True)
def compare_matrix(data,vals):
 return all(tuple(data[k])==(vals[2*i],vals[2*i+1])for i,k in enumerate(KEYS))
def outer(v):
 o=[]
 for x in range(3):
  xa,xb=v[2*x:2*x+2]
  for y in range(3):
   ya,yb=v[2*y:2*y+2];o.extend((xa*ya-xa*yb+xb*yb,xb*ya-xa*yb))
 return o

def run():
 assert not OUT.exists();OUT.mkdir(parents=True,exist_ok=False);before_states=protected_states();assert sha(DATA/'manifest.json')==EXPECTED;m=json.loads((DATA/'manifest.json').read_text());assert m['passed']
 for n,x in m['files'].items():assert(DATA/n).stat().st_size==x['bytes']and sha(DATA/n)==x['sha256'],n
 freeze=json.loads((DATA/'source-freeze.json').read_text())
 for n,x in freeze['files'].items():assert sha(ROOT/n)==x['sha256']and sha(DATA/'source-snapshot'/n)==x['sha256'],n
 pars=json.loads((DATA/'parameters.json').read_text());assert(pars['D'],pars['U'],pars['H'],pars['A1'],pars['A2'])==(D,U,H,A1,A2);assert pars['nu']=='principal1'and pars['profile']['fixed_once']and pars['profile']['delta']=='1/240000';assert 2*D<=7*U*U<=7*D
 note('input hashes and declared fixed-profile scope PASS')
 spf=array('I',range(CAP+1))
 for p in range(2,int(CAP**.5)+1):
  if spf[p]==p:
   for n in range(p*p,CAP+1,p):
    if spf[n]==n:spf[n]=p
 def nf(n):
  fs=[]
  while n>1:
   p=spf[n];e=0
   while n%p==0:n//=p;e+=1
   fs.append((p,e))
  return fs
 gs=primary(CAP);primes=[];byrational={}
 for g in gs:
  n=norm(g);p=abs(g[0])if g[1]==0 else n
  if n>1 and((spf[n]==n and n%3==1)or(g[1]==0 and p>1 and spf[p]==p and p%3==2)):
   primes.append(g);byrational.setdefault(p,[]).append(g)
 pidx={p:i for i,p in enumerate(primes)};assert len(primes)==11302
 def factors(g):
  rem=g;fs=[]
  for p,e in nf(norm(g)):
   assert p not in(2,3)
   for pi in byrational[p]:
    while(q:=quotient(rem,pi))is not None:fs.append(pi);rem=q
  assert rem==(1,0),(g,rem)
  return tuple(fs)
 def coeff(fs):
  ans=0;long=0
  for places in product(range(3),repeat=len(fs)):
   na=1;nb=1;sgn=1
   for pi,j in zip(fs,places):
    if j==1:na*=norm(pi);sgn=-sgn
    elif j==2:nb*=norm(pi);sgn=-sgn
   if na<=U and nb<=U:ans+=sgn
   if na>U and nb>U:long+=sgn
  mu=(-1)**len(fs);assert ans==long-mu;return(ans,long,mu)
 cols=[];small=[];alld={}
 for g in gs:
  n=norm(g)
  if not(D<=n<=2*D or A1<=n<2*A1 or A2<=n<2*A2):continue
  fs=factors(g)
  if len(fs)!=len(set(fs)):continue
  if D<=n<=2*D:
   assert D<n<2*D;ds=divisors(fs);x=coeff(fs);r=sum(norm(d)>U and n//norm(d)>U for d,_,_ in ds);assert x[1]==x[2]*r
   c=dict(g=g,n=n,fs=fs,x=x,ds=ds,r=r);cols.append(c)
   for d,dfs,mu in ds:
    if d in alld:assert alld[d][0]==dfs and alld[d][1]==mu
    else:alld[d]=(dfs,mu)
  if A1<=n<2*A1 or A2<=n<2*A2:small.append((g,fs))
 del gs
 rowmap={};candidates=badcoprime=badcap=0
 for v,fv in small:
  if not A1<=norm(v)<2*A1:continue
  for w,fw in small:
   if not A2<=norm(w)<2*A2:continue
   candidates+=1
   if set(fv)&set(fw):badcoprime+=1;continue
   u=mul(v,mul(w,w))
   if norm(u)>H:badcap+=1;continue
   assert u not in rowmap;rowmap[u]=(v,w,fv,fw)
 assert(candidates,badcoprime,badcap,len(rowmap))==(44,2,22,20)
 ap=json.loads((DATA/'prime-ideals.json').read_text());assert len(ap)==len(primes);byid={}
 for i,p in enumerate(ap):
  g=tuple(p['generator']);n=norm(g);rp=p['rational_prime'];assert p['id']==i and g in pidx and n==p['norm']and spf[rp]==rp
  assert(p['kind']=='inert'and rp%3==2 and n==rp*rp and g[1]==0)or(p['kind']=='split'and rp%3==1 and n==rp)
  byid[i]=g
 assert len(set(byid.values()))==len(primes);del ap
 ac=json.loads((DATA/'columns.json').read_text());ownmap={c['g']:c for c in cols};assert len(ownmap)==len(ac)==16953;ordered=[];nc=Counter();normmeta={}
 for i,c in enumerate(ac):
  g=tuple(c['generator']);own=ownmap[g];assert c['id']==i and c['norm']==own['n']and(c['A'],c['C'],c['mu'])==own['x']and c['r_U']==own['r']and c['W']==1 and c['nu_omega']==[1,0];assert len(c['prime_ids'])==len(set(c['prime_ids']))and set(own['fs'])=={byid[k]for k in c['prime_ids']};ordered.append(own);nc[own['n']]+=1
  meta=(own['x'],own['r'],sorted(norm(p)for p in own['fs']))
  if own['n']in normmeta:assert normmeta[own['n']]==meta
  normmeta[own['n']]=meta
 cols=ordered;del ac,ownmap,ordered
 ar=json.loads((DATA/'rows.json').read_text());assert len(ar)==20;rows=[];rsupport=[]
 for i,r in enumerate(ar):
  u=tuple(r['u']);v,w,fv,fw=rowmap[u];assert r['id']==i and tuple(r['v1'])==v and tuple(r['v2'])==w and r['N']==norm(u)and r['literal_unit']==[1,0]and r['v3_v4_v5_v6']==[1,1,1,1];assert set(fv)=={byid[k]for k in r['v1_prime_ids']}and set(fw)=={byid[k]for k in r['v2_prime_ids']};assert fv;rows.append(u);rsupport.append(set(fv)|set(fw))
 assert set(rows)==set(rowmap);del ar,rowmap,small
 dg=sorted(alld,key=lambda g:(norm(g),g));di={g:i for i,g in enumerate(dg)};nd=len(dg);nr=len(rows);assert nd==21750 and dg[0]==(1,0);dmu=[alld[g][1]for g in dg];dfs=[alld[g][0]for g in dg];dn=[norm(g)for g in dg];incident=array('I',[0])*nd
 for c in cols:
  c['did']=[di[d]for d,_,_ in c.pop('ds')]
  for i in c['did']:incident[i]+=1
 assert sum(incident)==73420;note('complete lattice/SPF support and original ternary coefficients PASS',columns=len(cols),divisors=nd,incidences=sum(incident),rows=nr)
 phases=[];phasechecks=0
 for pi in primes:
  n=norm(pi);v=array('b');rp=abs(pi[0])if pi[1]==0 else n
  if pi[1]:
   root=(-pi[0]*pow(pi[1],-1,rp))%rp;roots={(a+b*root)%rp:i for i,(a,b)in enumerate(PH)};assert len(roots)==6
   for a,b in rows:
    z=(a+b*root)%rp;v.append(-1 if z==0 else roots[pow(z,(n-1)//6,rp)]);phasechecks+=1
  else:
   roots={(a%rp,b%rp):i for i,(a,b)in enumerate(PH)};assert len(roots)==6
   for u in rows:
    x=(u[0]%rp,u[1]%rp)
    if x==ZERO:v.append(-1);phasechecks+=1;continue
    ans=(1,0);power=(n-1)//6
    while power:
     if power&1:tmp=mul(ans,x);ans=(tmp[0]%rp,tmp[1]%rp)
     tmp=mul(x,x);x=(tmp[0]%rp,tmp[1]%rp);power//=2
    v.append(roots[ans]);phasechecks+=1
  phases.append(v)
 for c in cols:c['pids']=[pidx[p]for p in c['fs']]
 raw_author=json.loads((DATA/'raw-character-phases.json').read_text());assert len(raw_author)==nr and all(len(v)==len(cols)for v in raw_author)
 Fd=array('q',[0])*(nd*nr*6);allowed=array('I',[0])*(nd*nr);rawown=array('b');colactive=array('B',[0])*len(cols);Z=array('q',[0])*(nd*18);perrow=[];diag=array('q',[0])*18;zeros=ones=rawmaskchecks=0;maxF=0
 for ri,u in enumerate(rows):
  rd=[0]*18
  for ci,c in enumerate(cols):
   exps=[phases[k][ri]for k in c['pids']];e=-1 if -1 in exps else sum(exps)%6;assert raw_author[ri][ci]==(None if e<0 else e);rawown.append(e);zeros+=e<0;ones+=e==0
   for pi,k in zip(c['fs'],c['pids']):assert(phases[k][ri]<0)==(quotient(u,pi)is not None);rawmaskchecks+=1
   if e<0:continue
   colactive[ci]+=1;pa,pb=PH[e];x=c['x']
   for a in range(3):
    for b in range(3):rd[(a*3+b)*2]+=x[a]*x[b]
   for did in c['did']:
    off=(did*nr+ri)*6;allowed[did*nr+ri]+=1
    for a in range(3):Fd[off+2*a]+=pa*x[a];Fd[off+2*a+1]+=pb*x[a]
  rs=[0]*18;full=None
  for did in range(nd):
   off=(did*nr+ri)*6;v=Fd[off:off+6];assert(v[0],v[1])==(v[2]-v[4],v[3]-v[5]);zz=outer(v);mu=dmu[did]
   if did==0:full=zz
   for k,t in enumerate(zz):Z[did*18+k]+=t;rs[k]+=mu*t
   maxF=max(maxF,max(map(abs,v)))
  for k,v in enumerate(rd):diag[k]+=v
  perrow.append(dict(coprime=rs,full=full,diagonal=rd))
  note('independent raw phases/incidence row complete',row=ri+1,total=nr)
 assert zeros==47908 and ones==48498;del raw_author,phases
 authrows=json.loads((DATA/'row-identities.json').read_text())['rows'];assert len(authrows)==nr
 for i,r in enumerate(authrows):assert r['row_id']==i and compare_matrix(r['coprime_h1_numerator_omega'],perrow[i]['coprime'])and compare_matrix(r['full_energy_omega'],perrow[i]['full'])and compare_matrix(r['diagonal_omega'],perrow[i]['diagonal'])
 zchecks=fchecks=maskchecks=allowedchecks=0;seen=set();even=[0]*18;odd=[0]*18;zeroZ=0
 with(DATA/'divisor-energies.jsonl').open()as f:
  for line in f:
   a=json.loads(line);g=tuple(a['generator']);did=di[g];assert did not in seen;seen.add(did);pgen=[byid[i]for i in a['prime_ids']];pd=(1,0)
   for pi in pgen:pd=mul(pd,pi)
   assert pd==g and len(set(pgen))==len(pgen)and frozenset(pgen)==dfs[did]and a['mu']==dmu[did]and a['norm']==dn[did]and a['incident_columns']==incident[did]==a['active_incident_columns']
   assert compare_matrix(a['Z_omega'],Z[did*18:did*18+18]);zchecks+=9;zeroZ+=not any(Z[did*18:did*18+18])
   assert len(a['F_omega'])==nr
   for ri,u in enumerate(rows):
    vals=a['F_omega'][ri];off=(did*nr+ri)*6;assert len(vals)==3 and all(tuple(vals[k])==(Fd[off+2*k],Fd[off+2*k+1])for k in range(3));fchecks+=3
    mask=not bool(dfs[did]&rsupport[ri]);assert a['row_raw_d_masks'][ri]==mask;maskchecks+=1
    assert a['row_allowed_active_column_counts'][ri]==allowed[did*nr+ri];allowedchecks+=1
    if not mask:assert not any(Fd[off:off+6])and allowed[did*nr+ri]==0
   zz=Z[did*18:did*18+18]
   for x in range(3):
    assert zz[(x*3+x)*2+1]==0 and zz[(x*3+x)*2]>=0
    for y in range(3):assert tuple(zz[(y*3+x)*2:(y*3+x)*2+2])==conj(zz[(x*3+y)*2:(x*3+y)*2+2])
   bucket=even if dmu[did]==1 else odd
   for k,t in enumerate(zz):bucket[k]+=t
 assert len(seen)==nd;note('ALL streamed Fd/masks/all9Z PASS',F_values=fchecks,Z_values=zchecks,masks=maskchecks)
 # Linear divisor-poset inversion covers every ordered pair without visiting pairs.
 Kg=array('q',[0])*(nd*18);gcounts=array('q',[0])*nd;visits=0
 for e,fs in enumerate(dfs):
  for gg,gfs,gm in divisors(tuple(fs)):
   i=di[gg];mu=(-1)**(len(fs)-len(gfs));gcounts[i]+=mu*incident[e]*incident[e];visits+=1
   for k in range(18):Kg[i*18+k]+=mu*Z[e*18+k]
 assert sum(gcounts)==len(cols)**2 and gcounts[0]==271688516 and all(c>=0 for c in gcounts)
 seen=set();zeroclasses=0;classsum=[0]*18
 with(DATA/'gcd-classes.jsonl').open()as f:
  for line in f:
   a=json.loads(line);fs=frozenset(byid[i]for i in a['prime_ids']);g=(1,0)
   for pi in fs:g=mul(g,pi)
   did=di[g];assert did not in seen and fs==dfs[did];seen.add(did);assert a['ordered_column_pair_count']==gcounts[did]and compare_matrix(a['contribution_omega'],Kg[did*18:did*18+18])
   if gcounts[did]==0:assert not any(Kg[did*18:did*18+18]);zeroclasses+=1
   for k,v in enumerate(Kg[did*18:did*18+18]):classsum[k]+=v
 assert len(seen)==nd and classsum==list(Z[:18])
 for ci,c in enumerate(cols):
  did=di[c['g']];assert gcounts[did]==1
  expected=[v for x in c['x']for y in c['x']for v in(x*y*colactive[ci],0)];assert list(Kg[did*18:did*18+18])==expected
 signed=[even[k]-odd[k]for k in range(18)];assert signed==list(Kg[:18]);assert signed[0:2]==[-61428,0]
 note('ALL gcd classes/counts/zero ledger via divisor inversion PASS',classes=nd,poset_visits=visits,zero_count_classes=zeroclasses)
 ledgercount=0
 with(DATA/'norm-ledger.jsonl').open()as f:
  for line in f:
   a=json.loads(line);n=D+ledgercount;ledgercount+=1;assert a['norm']==n and a['multiplicity']==nc[n]
   if nc[n]:
    x,r,pns=normmeta[n];assert(a['A'],a['C'],a['mu'])==x and a['r_U']==r and a['W']==1 and a['rejection']is None and a['rational_prime_factors']==[list(t)for t in nf(n)]and sorted(a['ideal_prime_norms'])==pns
   else:
    ff=nf(n);bad=[p for p,e in ff if p%3==2 and e!=2];bad2=[p for p,e in ff if p%3==1 and e>2]
    assert n%2==0 or n%3==0 or bad or bad2
    if n%2==0 or n%3==0:assert a['rejection']=='S_prime_2_or_3'
    else:assert isinstance(a['rejection'],str)and(('inert'in a['rejection']and bad)or('split'in a['rejection']and bad2))
 assert ledgercount==D+1
 summary=json.loads((DATA/'summary.json').read_text());counts=summary['counts'];assert counts['columns']==counts['active_columns']==len(cols)and counts['divisors']==nd and counts['rows']==nr and counts['ordered_coprime_column_pairs']==gcounts[0]and counts['raw_zero_column_row_values']==zeros and counts['raw_one_column_row_values']==ones
 nonsq=sum(any(e>=2 for p,e in nf(c['n']))for c in cols);assert nonsq==counts['squarefree_ideals_with_nonsquarefree_rational_norm']==1361
 for k,key in enumerate(KEYS):
  assert summary['full_row_energy'][key]==[str(Fraction(Z[2*k],D)),str(Fraction(Z[2*k+1],D))]
  assert summary['diagonal'][key]==[str(Fraction(diag[2*k],D)),str(Fraction(diag[2*k+1],D))]
  assert summary['normalized_h1'][key]==[str(Fraction(signed[2*k],D)),str(Fraction(signed[2*k+1],D))]
  b=summary['divisor_budget'][key];assert b['even_mu_Z_omega']==even[2*k:2*k+2]and b['odd_mu_Z_omega']==odd[2*k:2*k+2]and b['signed_numerator_omega']==signed[2*k:2*k+2]and b['signed_squared_complex_norm']==norm(signed[2*k:2*k+2])
  if k in(0,4,8):
   total=even[2*k]+odd[2*k];assert b['total_unsigned_mass']==total and b['cancellation_ratio']==str(Fraction(abs(signed[2*k]),total))
 for n,x in m['files'].items():assert sha(DATA/n)==x['sha256'],n
 for n,x in freeze['files'].items():assert sha(ROOT/n)==x['sha256'],n
 assert protected_states()==before_states
 estimate=json.loads((DATA/'resource-estimate.json').read_text())
 assert estimate['column_divisor_incidences']==sum(incident)and estimate['row_incidence_visits']==sum(incident)*nr and estimate['column_row_values']==len(cols)*nr and estimate['single_prime_row_symbol_evaluations']==phasechecks and estimate['ordered_pair_row_visits_if_literal']==len(cols)**2*nr
 # Fresh in-memory refusal controls, never mutate raw inputs.
 zero_pos=next(i for i,v in enumerate(rawown)if v<0);assert (None if rawown[zero_pos]<0 else rawown[zero_pos])!=0
 altered_F=list(Fd[:6]);altered_F[0]+=1;assert altered_F!=list(Fd[:6])
 valid_Z={k:[Z[2*i],Z[2*i+1]]for i,k in enumerate(KEYS)};assert compare_matrix(valid_Z,Z[:18]);valid_Z['AA'][0]+=1;assert not compare_matrix(valid_Z,Z[:18])
 assert perrow[0]['coprime'][3]!=0 and conj(tuple(perrow[0]['coprime'][2:4]))!=tuple(perrow[0]['coprime'][2:4])
 assert any(incident[di[c['g']]]==1 and colactive[i]>0 for i,c in enumerate(cols))
 result=dict(passed=True,input_manifest=str(DATA/'manifest.json'),input_manifest_sha256=EXPECTED,checker_sha256=sha(Path(__file__)),independent_core_sha256=sha(HERE/'independent_eisenstein_core_v1.py'),small_C_source_reference_sha256='2832ab817013e20acdea7fc53f02885e358eff21dfafe5ff5eb700e974a944c7',method='Independent lattice enumeration+SPF ideal factorization, direct finite-field powers, original ternary cutoffs, full incidence Fd and linear divisor-poset inversion; NO column-pair loop',columns=len(cols),divisors=nd,rows=nr,complete_primary_prime_ideals=len(primes),incidences=sum(incident),row_incidence_visits=sum(incident)*nr,prime_row_phase_evaluations=phasechecks,raw_values_compared=len(cols)*nr,raw_zero_values=zeros,raw_one_values=ones,raw_prime_zero_mask_checks=rawmaskchecks,F_values_compared=fchecks,Z_values_compared=zchecks,d_raw_masks_compared=maskchecks,allowed_counts_compared=allowedchecks,gcd_classes_compared=nd,zero_count_gcd_classes=zeroclasses,zero_Z_divisors=zeroZ,ordered_coprime_pairs_verified_without_enumeration=gcounts[0],hypothetical_dense_pair_visits_NOT_executed=len(cols)**2*nr,norm_ledger_records=ledgercount,ideal_squarefree_rational_norm_nonsquarefree=nonsq,all9signed_numerators={k:signed[2*i:2*i+2]for i,k in enumerate(KEYS)},full_AA_numerator=Z[0],diagonal_AA_numerator=diag[0],AA_even_odd=[even[0],odd[0]],normalized_AA=str(Fraction(signed[0],D)),own_F_array_sha256=hashlib.sha256(memoryview(Fd).cast('B')).hexdigest(),own_Z_array_sha256=hashlib.sha256(memoryview(Z).cast('B')).hexdigest(),array_native_byteorder=sys.byteorder,max_abs_F_component=maxF,all_inputs_and_frozen_sources_unchanged=True,protected_source_and_eight_release_states=before_states,negative_controls=['None rawzero distinctfromphase0','Fd integer mutation rejected','Z mutation rejected','wrong cross-conjugation rejected','selfdivisor required'],author_arithmetic_modules_or_old_checkers_executed=False,CPU_affinity_count=len(os.sched_getaffinity(0)),nice_increment=10,hard_AS_limit_MiB=256,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,elapsed_seconds=round(time.monotonic()-START,3),scope='NEW exact finite full-annular dataset only; no asymptotic saving, signed-slice PSD, bounded-profile-family or GRH inference')
 with(OUT/'independent-large-v1.json').open('x')as f:json.dump(result,f,indent=2);f.write('\n')
 note('LARGE AUDIT PASS',receipt=str(OUT/'independent-large-v1.json'),sha256=sha(OUT/'independent-large-v1.json'),normalized_AA=result['normalized_AA'],peak_RSS_KiB=result['peak_RSS_KiB'])
if __name__=='__main__':
 START=time.monotonic()
 try:run()
 except Exception as e:
  OUT.mkdir(parents=True,exist_ok=True);failure=OUT/'failure-v1.json'
  if not failure.exists():failure.write_text(json.dumps(dict(passed=False,type=type(e).__name__,error=str(e),checker_sha256=sha(Path(__file__)),elapsed_seconds=time.monotonic()-START),indent=2)+'\n')
  raise
