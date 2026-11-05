"""NEW tiny smooth/rough controls; stdlib only, no accepted data/checker imports."""
from pathlib import Path
from itertools import product,combinations
from math import isqrt
from fractions import Fraction
import json,hashlib,os,subprocess,sys
sys.dont_write_bytecode=True;os.nice(10);os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3];OUT=ROOT/'outputs/checks/2026-11-05-signed-divisor/postrelease-research/smooth-rough-v1'
PH=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))
def norm(z):a,b=z;return a*a-a*b+b*b
def mul(z,w):a,b=z;c,d=w;return(a*c-b*d,a*d+b*c-b*d)
def conj(z):a,b=z;return(a-b,-b)
def div(z,w):a,b=mul(z,conj(w));n=norm(w);return(a//n,b//n)if a%n==b%n==0 else None
def isprime(n):return n>=2 and all(n%k for k in range(2,isqrt(n)+1))
def au(fs,U):
 ans=0
 for states in product((0,1,2),repeat=len(fs)):
  a=b=1;sgn=1
  for p,k in zip(fs,states):
   if k==1:a*=norm(p);sgn=-sgn
   if k==2:b*=norm(p);sgn=-sgn
  if a<=U and b<=U:ans+=sgn
 return ans
def local(pi,u):
 p=norm(pi);assert isprime(p)and pi[1];root=(-pi[0]*pow(pi[1],-1,p))%p;z=(u[0]+u[1]*root)%p
 if not z:return None
 powers={(a+b*root)%p:i for i,(a,b)in enumerate(PH)};return powers[pow(z,(p-1)//6,p)]
def raw(fs,u):
 e=[local(p,u)for p in fs];return(0,0)if None in e else PH[sum(e)%6]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def guards(pins):
 for n,h in pins['source_sha256'].items():assert sha(ROOT/n)==h,n
 for x in pins['protected_source_and_all_nine_release_worktrees']:
  b=Path(x['path']);env=dict(os.environ,GIT_OPTIONAL_LOCKS='0')
  def git(*args):return subprocess.check_output(['git','-C',str(b),*args],env=env,text=True).strip()
  ip=Path(git('rev-parse','--git-path','index'));ip=ip if ip.is_absolute()else b/ip
  assert dict(path=str(b),HEAD=git('rev-parse','HEAD'),index_sha256=sha(ip),index_bytes=ip.stat().st_size)==x
pins=json.loads((HERE/'source-pins-v1.json').read_text());guards(pins);assert not OUT.exists();OUT.mkdir(parents=True)
D=100;U=7;H=max(h for h in range(1,D+1)if h**4<=D**3);assert H==31 and U*U<=D and 2*D<=7*U*U
# Enumerate prime ideals de novo only up to the tiny control cap.
bound=isqrt(4*(2*D)//3)+1;primes=[]
for a in range(-bound,bound+1):
 for b in range(-bound,bound+1):
  n=norm((a,b))
  if not(a%3==1 and b%3==0 and 1<n<=2*D and n%2 and n%3):continue
  if isprime(n)and n%3==1 or b==0 and isprime(abs(a))and abs(a)%3==2:primes.append((a,b))
primes.sort(key=lambda p:(norm(p),p));rough=[p for p in primes if norm(p)>U];pairs=[(p,q)for p,q in combinations(rough,2)if D<=norm(p)*norm(q)<=2*D]
p=(1,-3);q=(4,3);u=(-2,-3);m=mul(p,q);assert norm(p)==norm(q)==13 and p!=q and m==(13,0)and norm(m)==169 and pairs==[(p,q)]
assert norm(u)==7<=H and div(u,p)is None and div(u,q)is None
A=au([p,q],U);assert A==1;chi=raw([p,q],u);assert mul(chi,conj(chi))==(1,0)
assert raw([p,q],p)==(0,0) # Deleted-set guard: this raw zero must not become1.
delta=Fraction(1,20);t=Fraction(169,100);assert 1+delta<=t<=2-delta
# s is exactly1 when its argument>=1, so the fixed profile value is exactly1.
profile_value=1;unit_two_rough_correction=profile_value**2;assert unit_two_rough_correction==1
mobius_sectors=[]
for bits in product((0,1),repeat=2):
 d=(1,0);left=[]
 for pi,bit in zip([p,q],bits):
  if bit:d=mul(d,pi)
  else:left.append(pi)
 a=(1,0)
 for pi in left:a=mul(a,pi)
 assert mul(d,a)==m
 mobius_sectors.append({'common_d':list(d),'residual_a_equals_b':list(a),'mu_d':(-1)**sum(bits),'actual_A_da':A,'raw_product':1,'profile_product':1})
assert sum(x['mu_d']for x in mobius_sectors)==0 and mobius_sectors[-1]['residual_a_equals_b']==[1,0]
h=(-2,-3);r=(-5,-3);z=mul(h,r);u2=(1,3);assert norm(h)==U and norm(r)==19>U and norm(z)==133 and au([h,r],U)==au([h],U)==-1
assert div(z,u2)is None and norm(u2)==7 # Actual ideal mask, despite shared rational norm7.
assert norm(h)*norm(m)>2*D and norm(m)*norm(r)>2*D
assert all(norm(p)>U and norm(q)>U for p,q in pairs)
# Reject dropping the only unit-sector two-prime term or inserting an extra mu(e).
assert unit_two_rough_correction!=0 and au([r,h],U)==-1 and -au([h],U)!=au([r,h],U)
guards(pins)
result={'passed':True,'scope':'NEW finite control for an exact A-A-only algebraic reduction; no accepted data/checker call, asymptotic saving or global slice lower bound','D':D,'U':U,'H':H,'S':'above2,3','nu':'principal1','fixed_profile_delta':'1/20','literal_row_primary':list(u),'unit_residual_pair':{'p':list(p),'q':list(q),'norms':[13,13],'product':list(m),'product_norm':169,'A_U':A,'raw_phase_omega':list(chi),'raw_phase_times_conjugate':[1,0],'profile_value':1,'two_rough_unordered_ideal_pairs_in_annulus':len(pairs),'omitted_unit_correction_error':1},'boundary_smooth_control':{'h':list(h),'norm_h':7,'rough_prime':list(r),'norm_rough_prime':19,'column':list(z),'norm_column':133,'A_U_column':-1,'A_U_h':-1,'coprime_literal_row':list(u2)},'selfpair_common_divisor_sectors':mobius_sectors,'full_coprime_selfpair_sum':0,'negative_controls':['omitting unit two-rough correction rejected','extra mu(e) in A_U rough invariance rejected','raw-zero product replaced by1 rejected','norm-at-U must be smooth','nonunit h cannot accompany two rough primes'],'checker_sha256':sha(Path(__file__)),'note_sha256':sha(HERE/'SMOOTH_ROUGH_REDUCTION-v1.md'),'source_pins_sha256':sha(HERE/'source-pins-v1.json'),'protected_source_and_all_nine_release_states_unchanged':True,'frozen233_candidate_index_unchanged':True,'frozen604_bundle_receipt_unchanged':True,'seed':None}
prep=Path(pins['protected_source_and_all_nine_release_worktrees'][-1]['path'])/'outputs/publication/20261105-signed-divisor/release-preparation-v1';assert sha(prep/'allowlist-final-v1.json')==pins['frozen_candidate_allowlist_sha256']and sha(prep/'site-bundle-v1.json')==pins['frozen_bundle_receipt_sha256']
out=OUT/'author-result-v1.json'
with out.open('x')as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({'passed':True,'receipt':str(out),'sha256':sha(out),'note_sha256':result['note_sha256']}))
