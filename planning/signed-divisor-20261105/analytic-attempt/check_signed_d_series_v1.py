"""Fresh exact nine-state/cutoff controls; no old table, arithmetic module or dependency."""
from pathlib import Path
from itertools import product
from fractions import Fraction as F
from math import prod,isqrt
import hashlib,json
P=Path(__file__).resolve().parent;ROOT=P.parents[2];OUT=ROOT/'outputs/checks/2026-11-05-signed-divisor/analytic'
# Exact multivariate integer polynomials in(z,a1,a2,b1,b2).
ZERO=(0,)*5;ONE={ZERO:1}
def add(a,b):
 c=dict(a)
 for e,v in b.items():c[e]=c.get(e,0)+v
 return {e:v for e,v in c.items()if v}
def scale(c,a):return {e:c*v for e,v in a.items()if c*v}
def mul(a,b):
 c={}
 for e,x in a.items():
  for f,y in b.items():
   q=tuple(i+j for i,j in zip(e,f));c[q]=c.get(q,0)+x*y
 return {e:v for e,v in c.items()if v}
def var(j):return {tuple(int(i==j)for i in range(5)):1}
def sub1(a):return add(ONE,scale(-1,a))
def subst1(a,js):
 c={}
 for e,v in a.items():
  q=tuple(0 if i in js else x for i,x in enumerate(e));c[q]=c.get(q,0)+v
 return {e:v for e,v in c.items()if v}
z,a1,a2,b1,b2=[var(j)for j in range(5)];ap=add(ONE,scale(-1,add(a1,a2)));bp=add(ONE,scale(-1,add(b1,b2)));fp=sub1(mul(z,mul(ap,bp)));rp=fp;dp=sub1(z)
for x in [a1,a2,b1,b2]:rp=mul(rp,sub1(mul(z,x)))
for x,y in product([a1,a2],[b1,b2]):dp=mul(dp,sub1(mul(z,mul(x,y))))
difference=add(rp,scale(-1,dp));assert all(e[0]>=2 for e in difference);assert sum(abs(v)for e,v in rp.items()if e[0]>=2)<=146;assert sum(abs(v)for e,v in dp.items()if e[0]>=2)<=26
assert subst1(rp,{1,2,3,4})==subst1(dp,{1,2,3,4});assert subst1(fp,{1,2,3,4})==sub1(z)
assert subst1(rp,{2,4})==subst1(dp,{2,4});assert subst1(fp,{2,4})==sub1(mul(z,mul(a1,b1)))
# The actual annular finite-cutoff control, with overlapping residual prime13.
D=1500;U=25;dprime=7;aa=(13,19);bb=(13,31)
def aval(primes):
 ans=0
 for places in product(range(3),repeat=len(primes)):
  n1=prod(q for q,j in zip(primes,places)if j==1);n2=prod(q for q,j in zip(primes,places)if j==2)
  if n1<=U and n2<=U:ans+=(-1)**sum(j>0 for j in places)
 return ans
def fixedslot(primes,places):return [prod(q for q,j in zip(primes,places)if j==k)for k in [1,2]]
states={};admissible={};enumerated=0
for i,j in product(range(3),repeat=2):
 ans=0;count=0
 for pa,pb in product(product(range(3),repeat=2),repeat=2):
  enumerated+=1;ca=fixedslot(aa,pa);cb=fixedslot(bb,pb)
  if i:ca[i-1]*=dprime
  if j:cb[j-1]*=dprime
  if max(ca+cb)>U:continue
  count+=1;ans+=(-1)**(1+int(i>0)+int(j>0)+sum(t>0 for t in pa+pb))
 states[str(i)+str(j)]=ans;admissible[str(i)+str(j)]=count
assert enumerated==729 and states=={'00':-1,'01':0,'02':0,'10':1,'11':0,'12':0,'20':1,'21':0,'22':0}
assert [aval(aa),aval(bb),aval((7,)+aa),aval((7,)+bb)]==[-1,-1,1,-1]
assert sum(states.values())==1 and sum(v for k,v in states.items()if k!='00')==2
assert D<7*prod(aa)<2*D and D<7*prod(bb)<2*D and 2*D<=7*U*U and U*U<=D
assert F(11,10)<F(7*prod(aa),D)<F(19,10) and F(11,10)<F(7*prod(bb),D)<F(19,10)
# The finite-prime Euler model contains the exact eight-state numerator, not only d00.
finite_checks=[]
for sigma in [2,3]:
 direct=F(0)
 for has7,has37 in product([0,1],repeat=2):
  ds=tuple(q for q,t in [(7,has7),(37,has37)]if t);n=prod(ds);direct+=F((-1)**len(ds)*aval(ds+aa)*aval(ds+bb),n**sigma)
 z7=F(1,7**sigma);z37=F(1,37**sigma);numerator=1+F(2)*z7/(1-z7);base=(1-z7)*(1-z37);assert direct==base*numerator
 finite_checks.append(dict(sigma=sigma,direct=str(direct),finite_numerator=str(numerator),euler_base=str(base)))
# Original pair's gcd inversion still cancels; no global obstruction is inferred.
mu_gcd=[1,-1,-1,1];pair_terms=[-v for v in mu_gcd];assert sum(pair_terms)==0
# Primary-generator labels pin genuine Eisenstein prime ideals and a nonprincipal row.
gens=[(1,3),(4,3),(-2,3),(1,6),(7,6)];ns=[a*a-a*b+b*b for a,b in gens];assert ns==[7,13,19,31,43]and all(a%3==1 and b%3==0 for a,b in gens)
H=isqrt(isqrt(D**3));assert H==241 and 37<=43<74 and 43<=H and 43 not in set((7,)+aa+bb)
r=dict(passed=True,scope='New signed common-divisor nine/eight-state algebra; no original signed bound or global pole obstruction',proof_path=str(P/'SIGNED_D_SERIES-v1.md'),proof_sha256=hashlib.sha256((P/'SIGNED_D_SERIES-v1.md').read_bytes()).hexdigest(),checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),symbolic_variables=['z','alpha1','alpha2','beta1','beta2'],linear_terms_cancel=True,symbolic_R_tail_l1=sum(abs(v)for e,v in rp.items()if e[0]>=2),symbolic_D_tail_l1=sum(abs(v)for e,v in dp.items()if e[0]>=2),uniform_majorant_172_valid=True,zero_aux_and_two_zero_aux_slices_exact=True,D=D,U=U,H=H,row_primary_generator=gens[-1],row_norm=43,pure_block_A1=37,A2=1,residual_a_norm=prod(aa),residual_b_norm=prod(bb),residual_overlap_norm=13,d_norm=7,actual_column_norms=[7*prod(aa),7*prod(bb)],AU_values=[-1,-1,1,-1],joint_cutoff_assignments_enumerated=enumerated,admissible_by_d_state=admissible,signed_d_state_coefficients=states,actual_d_coefficient=1,d00_only_coefficient=-1,non00_e_unit_correction=2,finite_prime_model_checks=finite_checks,original_pair_gcd_norm=91,original_pair_gcd_signed_terms=pair_terms,original_pair_total_zero=True,common_profile='One fixed smooth plateau on[1.1,1.9], supported[1,2]; actual values1',raw_row_coprime_to_all_factors=True,all_ideals_squarefree=True,old_controls_or_tables_used=False,new_dependencies=False)
with(OUT/'exact-common-divisor-v1.json').open('x')as f:json.dump(r,f,indent=2);f.write('\n')
print(json.dumps(dict(passed=True,enumerated_joint_cutoff_assignments=enumerated,d_state_coefficients=states,e_unit_correction=2,finite_prime_sigma_checks=2,symbolic_tail_bounds=[r['symbolic_R_tail_l1'],r['symbolic_D_tail_l1']],original_pair_total_zero=True)))
