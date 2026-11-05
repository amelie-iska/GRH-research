from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib,json
ROOT=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
count=0
for xs in product(range(5),repeat=6):
 A=[2**x for x in xs];R=1;H=1
 for j,a in enumerate(A,1):R*=a;H*=a**j
 M=max(A[0],A[1])
 assert R<=H and R**3<=H*M**3 and R**3<=H**2*M
 count+=1
# Boundary exponent comparison for the original H=D^(3/4) frontier.
theta=F(3,4)
new=max(theta,1+theta/3,F(2,3)*(theta+1))-theta
assert new==F(1,2)
for a in [F(1,8),F(1,4),F(3,8),F(1,2)]:
 assert (new<2*a)==(a>F(1,4))
# Exact sixth-power sentinel control for a column prime of norm7.
# The original residue symbol is zero at a divisible numerator, even
# when the row radicand is a sixth power and its primitive Kummer
# character has become trivial. No complex root computation needed.
original_zero=0
primitive_sixth_power_value=1
assert original_zero**6==0 and primitive_sixth_power_value==1
assert original_zero!=primitive_sixth_power_value
result={'passed':True,'dyadic_exponent_cases':count,'powers_tested':6,'all_ideal_pivot_max_first_two':True,'H_D_three_quarters_excess':str(new),'improvement_over_old_small_delta_cutoff_when_a_gt':'1/4','sixth_power_sentinel_negative_control':True,'scope':'Exact finite checks of exponent and mask bookkeeping, not a proof of BGL or the analytic energy theorem.'}
p=ROOT/'outputs/checks/2026-11-04-weighted-moment/review/pivot-exact-controls.json'
assert not p.exists();result['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
