"""Fresh exact formal common-d Gauss/gauge algebra and new long-divisor budgets.
No actual character/ideal-family or accepted old controls are run.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
S=Path("/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104")
O=S/"outputs/checks/2026-11-06-unit-gauss/lane-b/controls-v1"
assert not O.exists();O.mkdir()
n=4
# Symmetric reciprocity phases in F3; formal prime Gauss variables remain independent.
c=[[0 if i==j else (i+j+i*j+1)%3 for j in range(n)]for i in range(n)]
theta=[0,1,2,0];rho=[1,0,1,2];gamma=[0,2,1,1];nu=[2,1,0,1];angle=[1,1,2,0]
def bits(s):return [i for i in range(n)if s>>i&1]
def dot(w,s):return sum(w[i]for i in bits(s))%3
def cross(a,b):return sum(c[i][j]for i in bits(a)for j in bits(b))%3
def mul(a,b):return ((a[0]+b[0])%3,tuple(x+y for x,y in zip(a[1],b[1])))
def bar(a):return ((-a[0])%3,tuple(-x for x in a[1]))
def phase(x):return (x%3,(0,)*n)
def gauss(s):
 phase_part=-sum(c[i][j]for i in bits(s)for j in bits(s)if i<j)
 return (phase_part%3,tuple(int(s>>i&1)for i in range(n)))
left=[(theta[i]+rho[i]+gamma[i]+nu[i]+angle[i])%3 for i in range(n)]
right=[(-theta[i]-rho[i]-gamma[i]+nu[i]+angle[i])%3 for i in range(n)]
common=[2*(theta[i]+rho[i]+gamma[i])%3 for i in range(n)]
def coeff(v,z):return mul(mul(phase(dot(left,v)),bar(phase(dot(right,z)))),mul(bar(gauss(v)),gauss(z)))
identities=0;reconstructions=0;overlap_residuals=0;nontrivial_common_phase=0
for v in range(1<<n):
 for z in range(1<<n):
  intersection=v&z;total=0
  for d in range(1<<n):
   if d&intersection!=d:continue
   a=v^d;b=z^d
   assert not d&a and not d&b
   actual=coeff(v,z)
   residual=mul(mul(phase(dot(left,a)),bar(phase(dot(right,b)))),mul(bar(gauss(a)),gauss(b)))
   transformed=mul(phase(dot(common,d)+cross(d,a)-cross(d,b)),residual)
   assert transformed==actual,(v,z,d)
   total+=(-1)**len(bits(d));identities+=1
   overlap_residuals+=bool(a&b)
   nontrivial_common_phase+=bool(dot(common,d))
  assert total==int(not intersection);reconstructions+=1
# One actual-pattern finite-component gauge control: dropping rho(d)^2 breaks inversion.
v=z=d=1;a=b=0
correct=coeff(v,z)
residual=mul(mul(phase(dot(left,a)),bar(phase(dot(right,b)))),mul(bar(gauss(a)),gauss(b)))
wrong_common=[(common[i]-2*rho[i])%3 for i in range(n)]
wrong=mul(phase(dot(wrong_common,d)),residual)
assert correct!=wrong and correct[1]==wrong[1]==(0,)*n
cube=[(1,0),(0,1),(-1,-1)]
difference=(cube[correct[0]][0]-cube[wrong[0]][0],cube[correct[0]][1]-cube[wrong[0]][1])
assert difference!=(0,0)
# Exact exponent assembly of the NEW d-tail (not the finished original-k tail).
pref=F(3,4)+F(1,16);cut=F(1,32)
powers={"constant_tail":pref-F(1,2),"quadratic_d_tail":pref-2*cut,"mixed_d_tail":pref-F(1,6)-cut,"equalnorm_correction":pref-1}
assert powers=={"constant_tail":F(5,16),"quadratic_d_tail":F(3,4),"mixed_d_tail":F(59,96),"equalnorm_correction":F(-3,16)}
assert all(x<=F(3,4)for x in powers.values())
# Positive prefix sum term exponents; square then A1V/(D R).
# S_R <= sqrtR*D1/4 +sqrt(D/R)+D5/12.
for r in [F(i,64)for i in range(65)]:
 terms=[r/F(2)+F(1,4),(1-r)/2,F(5,12)]
 assembled=[pref-1-r+2*t for t in terms]
 assert assembled==[pref-F(1,2),pref-2*r,pref-F(1,6)-r]
# New certificate improves SAME-kernel elementary R0^-1 threshold.
assert (pref-F(3,4))/2==F(1,32)and pref-F(3,4)==F(1,16)
note=S/"planning/unit-gauss-20261106/lane-b/LONG_DIVISOR_CUBIC_MEAN_ATTEMPT-v2.md"
result=dict(passed=True,note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),formal_common_d_gauge_identities=identities,formal_Mobius_reconstructions=reconstructions,residual_overlap_states=overlap_residuals,nontrivial_common_phase_states=nontrivial_common_phase,
rho_square_omission_negative_control={"v":v,"z":z,"d":d,"correct_phase":correct[0],"wrong_phase":wrong[0],"exact_Zomega_difference":difference},
new_critical_exponents={k:str(v)for k,v in powers.items()},positive_prefix_scale_checks=65,
formal_material_parameters={"prime_labels":n,"reciprocity_matrix_mod3":c,"theta_mod3":theta,"rho_mod3":rho,"Gamma_mod3":gamma,"nu_mod3":nu,"angular_gauge_mod3":angle,"Gauss_prime_variables":"independent formal unitary Laurent variables","randomness":"none"},
scope="Fresh synthetic exact Laurent/F3/Integer/Fraction checks of common-Gauss cancellation, retained rho-square and NEW long-divisor exponent assembly only. NOT actual Eisenstein characters/Gauss samples/ideal energy, numerical theorem proof, training or Lean. Accepted old controls not rerun.")
(O/"checks-v1.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
print(json.dumps({"passed":True,"checks_sha256":hashlib.sha256((O/"checks-v1.json").read_bytes()).hexdigest(),"formal_states":identities,"reconstructions":reconstructions,"scale_checks":65,"negative_control":difference}))
