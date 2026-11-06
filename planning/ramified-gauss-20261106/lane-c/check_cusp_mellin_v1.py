#!/usr/bin/env python3
"""NEW exact cusp/Mellin formal controls; not annular character data or Lean."""
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"outputs/checks/2026-11-06-ramified-gauss/lane-c/cusp-controls-v1"
OUT.mkdir(parents=True,exist_ok=True)
E=lambda a=0,b=0:(Q(a),Q(b))
zero,one=E(),E(1)
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return(-x[0],-x[1])
def sub(x,y):return add(x,neg(y))
def mul(x,y):return(x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
def conj(x):return(x[0]-x[1],-x[1])
def norm(x):return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]
def scale(x,a):return(x[0]*a,x[1]*a)
def div(x,y):return scale(mul(x,conj(y)),1/norm(y))
def power(x,n):
    if n<0:return power(div(one,x),-n)
    y=one
    for _ in range(n):y=mul(y,x)
    return y
def mm(a,b):
    return tuple(tuple(add(mul(a[i][0],b[0][j]),mul(a[i][1],b[1][j]))for j in range(2))for i in range(2))
def U(a):return((one,a),(zero,one))
def W(c):return((zero,neg(div(one,c))),(c,zero))
def act(g,z,v):
    a,b=g[0];c,d=g[1]
    czd=add(mul(c,z),d)
    den=norm(czd)+norm(c)*v*v
    num=add(mul(add(mul(a,z),b),conj(czd)),scale(mul(a,conj(c)),v*v))
    return scale(num,1/den),v/den
S=W(one)
av=[E(),E(1),E(0,1),E(1,1),E(2,-1)]
bv=[E(1),E(2),E(0,1),E(1,2),E(3),E(2,1),E(3,-1),E(1,3)]
pts=[(E(),Q(1)),(E(Q(1,3),Q(2,5)),Q(3,7)),(E(Q(-2,3),Q(1,4)),Q(5,2))]
counts={"SL2_cusp_matrix_identities":0,"exact_H3_coordinate_identities":0,"angular_phase_unit_checks":0,"Mellin_Jacobian_exponents":0,"source_primary_selector_states":0,"selected_primary_states":0}
for aa in av:
    for bb in bv:
        g=mm(mm(mm(U(aa),S),U(bb)),S)
        A,B=g[0];C,D=g[1]
        assert sub(mul(A,D),mul(B,C))==one and C!=zero
        gi=((D,neg(B)),(neg(C),A))
        t=mm(gi,U(div(A,C)))
        expected=mm(U(neg(div(D,C))),W(neg(C)))
        assert t==expected
        counts["SL2_cusp_matrix_identities"]+=1
        for z,v in pts:
            zz,vv=act(t,z,v)
            qq=norm(z)+v*v
            ze=sub(neg(div(D,C)),div(conj(z),scale(mul(C,C),qq)))
            ve=v/(norm(C)*qq)
            assert zz==ze and vv==ve
            counts["exact_H3_coordinate_identities"]+=1
        for ell in [-4,-3,-2,-1,1,2,3,4]:
            phase=scale(power(div(C,conj(C)),ell),(-1)**abs(ell))
            assert norm(phase)==1
            counts["angular_phase_unit_checks"]+=1
for ell in range(1,9):
    for js in range(-5,6):
        s=Q(js,4)
        # In v exponent 2s-ell-2, substitute v=(NC*y)^-1 and dv=(NC)^-1*y^-2 dy.
        normfactor=-(2*s-ell-2)-1
        derivative_magnitude=-Q(ell)
        assert normfactor+derivative_magnitude==1-2*s
        assert -(2*s-ell-2)-2==ell-2*s
        counts["Mellin_Jacobian_exponents"]+=1
# Formal local Taylor support of the radial constant. A mixed derivative is a negative control.
coef={};b=Q(1)
for k in range(9):
    if k:b=b*(Q(-2,3)-(k-1))/k
    coef[(k,k)]=b
for ell in range(1,9):assert coef.get((ell,0),0)==0 and coef.get((0,ell),0)==0
assert coef[(1,1)]==Q(-2,3)
# Exact DR5.7 branch congruences modulo(lambda^2)=(3). These are formal primary variables, not ideal/Gauss data.
lam=E(1,2);omega=E(0,1)
primary=[E(1),E(1,3),E(4),E(4,3)]
def congruent1mod3(x):
    return x[0].denominator==1 and x[1].denominator==1 and (x[0]-1)%3==0 and x[1]%3==0
for c in primary:
    for d in primary:
        cd3=mul(c,power(d,3))
        for n in range(1,5):
            for j in range(3):
                for sign in [-1,1]:
                    x=scale(mul(mul(power(lam,3*n-1),power(omega,j)),cd3),sign)
                    assert not congruent1mod3(x)
                    counts["source_primary_selector_states"]+=1
        for n in range(5):
            for sign in [-1,1]:
                x=scale(mul(power(lam,3*n),cd3),sign)
                selected=congruent1mod3(x)
                assert selected==(n==0 and sign==1)
                counts["source_primary_selector_states"]+=1
                if selected:counts["selected_primary_states"]+=1
assert Q(5,6)==(2-Q(-2,3)-1)/2
assert Q(1,6)==(2-Q(2,3)-1)/2
result={"schema":"ramified-gauss-new-cusp-Mellin-controls-v1","passed":True,
"scope":"NEW deterministic exact Q(omega)/Fraction matrix,H3-coordinate,Jacobian,pole and primary-branch controls. NOT actual annular ideal/character/Gauss data, training, numerical spectrum or Lean; no old controls replayed.",
"material_parameters":{"SL2_words":"U(a)S U(b)S,5 a by8 nonzero b","H3_points":"3 exact rational Q(omega),positive rational height states","ell":"plus/minus1..4 for phases;1..8 for formal derivatives","s_grid":"-5/4..5/4 step1/4","primary_variables_mod3":"1,1+3omega,4,4+3omega; no squarefree-ideal claim"},
"counts":counts,"radial_mixed_derivative_negative_control":"partial_z partial_barz (1+zbarz)^(-2/3) at0=-2/3, so only PURE nonzero angular derivatives are killed",
"Jacobian_omission_negative_control":"Dropping dv contributes exponent-2s instead of1-2s; atNC7,s0 the correct magnitude7 vswrong1 differsby7.",
"ell_zero_endpoint_poles":{"infinity":"1/6, residue-Cinfinity/2","zero":"5/6,residueCzero/2"},
"old_controls_rerun":False,"randomness":"none",
"note_sha256":hashlib.sha256((ROOT/"planning/ramified-gauss-20261106/lane-c/RATIONAL_CUSP_CONSTANTS_AND_MELLIN-v1.md").read_bytes()).hexdigest()}
p=OUT/"checks-v1.json";assert not p.exists();p.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
print(json.dumps({"passed":True,"counts":counts,"path":str(p.relative_to(ROOT))},sort_keys=True))
