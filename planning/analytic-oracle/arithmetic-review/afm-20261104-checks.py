"""Independent finite consistency checks for a prose AFM draft, not a Lean proof."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[3]
checks={}
count=0
for e in range(96):
 r=e%6;a0=int(r==1);a1=r if r>=2 else 0;a2=e//6
 assert a0+a1+6*a2==e and a0*a1==0
 assert int(r!=0)==int(bool(a0 or a1))
 assert int((2*e)%6!=0)==int(e%3!=0)
 count+=1
checks['prime_valuation_support_cases']=count
count=0
for e in range(2,96):
 c=e%2;b=(e-3*c)//2
 assert b>=0 and c in(0,1) and 2*b+3*c==e
 count+=1
checks['squarefull_coordinate_cases']=count
for s in [F(1),F(2,3)]:assert 2*s>1 and 3*s>1
checks['squarefull_series_exponents']=['1','2/3']
rows=[]
for tau in [F(0),F(1,100),F(1,10),F(1,2),F(1),F(2),F(10)]:
 goal=1+tau;terms=[F(1),1+tau,1+F(2,3)*tau]
 assert all(x<=goal for x in terms)
 rows.append(dict(tau=str(tau),powers=[str(x) for x in terms],target=str(goal)))
checks['large_sieve_cutoff_exponents']=rows
assert not (F(1)<=1+F(-1,10))
checks['height_less_than_one_negative_control']=True
for a,b in [(8,9),(27,36),(32,81),(32,36)]:assert a<b
count=0
for delta in [F(1,1000),F(1,100),F(1,10),F(1,4),F(499,1000)]:
 for eps in [F(1,1000),F(1,10),F(1,4)]:
  alpha=F(3,2)-eps;assert F(5,4)<=alpha<F(3,2)
  far=2*delta*6/(3*(alpha-1));assert far<=8
  assert 3+far<=11 and 3*6*11<200
  pole=(F(3,2)+delta)/(F(1,2)-delta);assert pole>1
  count+=1
checks['poisson_integer_envelope_cases']=count
# Fixed S-smooth norm sum is dominated by its finite Euler product.
norms=[3,4,7];J=20
finite=F(1);infinite=F(1)
for q in norms:
 finite*=sum((F(1,q)**e for e in range(J+1)),F(0))
 infinite*=1/(1-F(1,q))
assert finite<=infinite
checks['S_smooth_finite_sum_bound']={'norms':norms,'max_valuation':J,'exact_upper':str(infinite)}
result={'passed':True,'checks':checks,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Finite valuation, exponent and rational-envelope consistency only; does not prove Kummer identification, AFE, large sieve or GRH','GRH_proved':False,'new_Lean_declarations':0}
out=ROOT/'outputs/checks/2026-11-04-validated-oracle/arithmetic';out.mkdir(parents=True,exist_ok=True)
(out/'afm-20261104-finite-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':True,'valuation_cases':96,'squarefull_cases':94,'poisson_cases':count}))
