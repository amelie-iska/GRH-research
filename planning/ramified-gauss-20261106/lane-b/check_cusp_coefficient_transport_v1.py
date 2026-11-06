from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib,json,datetime

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"outputs/checks/2026-11-06-ramified-gauss/lane-b/coefficient-transport-v1"
OUT.mkdir(parents=True,exist_ok=True)
RESULT=OUT/"checks-v1.json"
assert not RESULT.exists(), "Immutable result exists; no replay."

def E(a=0,b=0): return (F(a),F(b))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def mul(x,y):
    a,b=x; c,d=y
    return (a*c-b*d,a*d+b*c-b*d)
def conj(x): return (x[0]-x[1],-x[1])
def norm(x):
    a,b=x
    return a*a-a*b+b*b
def div(x,y):
    z=mul(x,conj(y)); n=norm(y)
    assert n
    return (z[0]/n,z[1]/n)
def power(x,n):
    if n<0: return power(div(E(1),x),-n)
    z=E(1)
    for _ in range(n): z=mul(z,x)
    return z
def trace(x): return 2*x[0]-x[1]
def mod1(x): return x-F(x.numerator//x.denominator)
def primary_mod3(x):
    a,b=x
    return a.denominator==b.denominator==1 and (int(a)-1)%3==0 and int(b)%3==0
def ser(x): return [str(x[0]),str(x[1])]

lam=E(1,2); omega=E(0,1)
rs=[E(-2,-3),E(4,3),E(-5,-3),E(7,3)]
cs=[E(-2,-3),E(4,3),E(-5,-3)]
ds=[E(1),E(4,3)]
translations=[E(1),omega,E(2,-1)]
assert [norm(x) for x in rs]==[7,13,19,37]
assert all(primary_mod3(x) for x in rs+cs+ds)
assert norm(lam)==3 and power(lam,2)==E(-3)

affine=0; wrong=0; first_negative=None
for B,r,c,c_sf,d,L in product(range(1,4),rs,translations,cs,ds,(-3,-4)):
    mu=mul(power(lam,L),mul(c_sf,power(d,3)))
    nu=mul(power(lam,-2*B),mu)
    delta=neg(div(mul(power(lam,4+2*B),c),r))
    correct_phase=trace(mul(nu,delta))
    source_phase=trace(neg(div(mul(mul(power(lam,4),mu),c),r)))
    assert correct_phase==source_phase
    assert norm(nu)==F(3)**(-2*B)*norm(mu)
    # The coefficient amplitude3^-B plus Nnu^-sigma has exponent
    # -B+2B*sigma = B(2sigma-1), with rational sigma test points.
    for sigma in (F(25,24),F(13,12),F(3,2)):
        assert -F(B)+2*B*sigma==B*(2*sigma-1)
    bad_delta=neg(div(mul(power(lam,4),c),r))
    bad=trace(mul(nu,bad_delta))
    if mod1(bad-source_phase):
        wrong+=1
        if first_negative is None:
            first_negative={"B":B,"r":ser(r),"translation_c":ser(c),
              "mu":ser(mu),"correct_trace":str(source_phase),
              "wrong_trace":str(bad),"nonzero_phase_difference_mod1":str(mod1(bad-source_phase))}
    affine+=1
assert affine==432 and wrong>0

branches=0; selected=0
for n,eps,sign,c,d in product(range(1,5),(E(1),omega,power(omega,2)),(1,-1),cs,ds):
    mu=mul(E(sign),mul(eps,mul(power(lam,3*n-4),mul(c,power(d,3)))))
    x=mul(power(lam,3),mu)
    assert not primary_mod3(x)
    branches+=1
for n,sign,c,d in product(range(5),(1,-1),cs,ds):
    mu=mul(E(sign),mul(power(lam,3*n-3),mul(c,power(d,3))))
    x=mul(power(lam,3),mu)
    actual=primary_mod3(x)
    assert actual==(n==0 and sign==1)
    selected+=int(actual); branches+=1
assert branches==204 and selected==6

# NEW rational upper envelopes for the explicit lambda-series norm:
z=F(1,9)
tau_bound=6*3**7*z/(1-z)+2*3**6/(1-z)
assert tau_bound==F(3**8,2)
assert 27*3**5==3**8
geometric_checks=0
for n in range(1,13):
    part=sum((z**j for j in range(1,n+1)),F(0))
    tail=z**(n+1)/(1-z)
    assert part+tail==z/(1-z)
    assert 6*3**7*(part+tail)+2*3**6/(1-z)==tau_bound
    geometric_checks+=1

note="planning/ramified-gauss-20261106/lane-b/CUSP_COEFFICIENT_NORM_AND_ACTUAL_MATCH-v1.md"
companion="planning/ramified-gauss-20261106/lane-b/ACTUAL_CUSP_COEFFICIENT_CONVENTION-v1.md"
out={
"schema":"ramified-gauss-new-cusp-coefficient-transport-controls-v1",
"created_at_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
"passed":True,"new_exact_Eisenstein_affine_transport_states":affine,
"omitted_lambda_2B_negative_control_states":wrong,
"first_exact_negative_control":first_negative,
"new_actual_primary_support_branch_checks":branches,
"selected_positive_n0_states":selected,
"new_exact_rational_lambda_norm_envelope_checks":geometric_checks,
"tau_geometric_upper_constant":str(tau_bound),"all27_cusp_uniform_upper_constant":3**8,
"material_parameters":{
"field":"Q(omega), omega^2+omega+1=0, lambda=1+2omega",
"B_values":[1,2,3],"r_primary_generators":[ser(x) for x in rs],
"r_norms":[7,13,19,37],"c_squarefree_prime_generators":[ser(x) for x in cs],
"d_generators":[ser(x) for x in ds],"moving_translation_c":[ser(x) for x in translations],
"affine_mu_lambda_exponents":[-3,-4],
"branch_families":"Both literal DR tau families, n1..4/all units and n0..4/signs",
"randomness":"none","floating_point_operations":0},
"note":{"path":note,"sha256":hashlib.sha256((ROOT/note).read_bytes()).hexdigest()},
"required_coefficient_companion":{"path":companion,"sha256":hashlib.sha256((ROOT/companion).read_bytes()).hexdigest()},
"producer_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
"scope":"NEW exact coefficient-index/phase/primary-support and rational geometric-norm controls only. These use actual Eisenstein numbers but compute NO Gauss character values, primitive e/w dataset, row energies or training/Lean. They are not a numerical proof of the analytic bound. Accepted prior projector/matrix/tail/fixture controls were NOT rerun."}
RESULT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps({"result":str(RESULT.relative_to(ROOT)),"sha256":hashlib.sha256(RESULT.read_bytes()).hexdigest(),"affine_states":affine,"branch_checks":branches,"negative_states":wrong,"passed":True}))
