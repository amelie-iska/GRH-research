"""Fresh exact window and Gaussian normalization controls for the smooth partner band."""
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from json import dump
from math import cos, exp, hypot, pi, sin, sqrt
from pathlib import Path

ROOT = Path("planning/mid-divisor-20261109/lane-b")
OUT = Path("outputs/checks/2026-11-09-mid-divisor/lane-b")
NOTE = ROOT / "SMOOTH_RADIAL_PARTNER-v1.md"
PINS = {
    str(NOTE): "7e71ef83c62acd3f7fdbc4906e69ee88e9afa300ba2015012271359cb2555145",
    "planning/low-dual-cutoff-20261108/LOW_DUAL_CUTOFF-v1.md": "0d92323bbde25afbdb18ec6092e107be66a4837e2478191d21410c8e2a852b04",
    "planning/matched-poisson-20261108/MATCHED_POISSON_CROSS-v2.md": "8634bdac8792c95c057d79742551caa945b3885707424a3c5b039f923404cf99",
    "planning/unit-pair-core-20261108/lane-b/SELECTED_LOW_FREQUENCIES-v2.md": "f4925a9e4189a871774e91bb6816eb96368c851ee0c68446baea919aa364cafd",
    "planning/joint-unit-pair-20261109/lane-b/JOINT_EQUALITY_FREQUENCY-v2.md": "e268f0f5ab1a8472ad2d704a201ae59f62b0119380ca98926106631e38a565f5",
    "planning/joint-unit-pair-20261109/lane-c/FORCED_RADICAL_JOINT-v1.md": "48344a5ba51f9a78125ec61be466e72f71e2180c88dfe94e09e3aa64b365bd81",
}
for path, want in PINS.items():
    assert sha256(Path(path).read_bytes()).hexdigest() == want, path

def norm(x):
    a,b=x
    return a*a-a*b+b*b

def mul(x,y):
    a,b=x
    c,d=y
    return a*c-b*d,a*d+b*c-b*d

def conjugate(x):
    a,b=x
    return a-b,-b

def divides(v,x):
    V=norm(v)
    a,b=mul(x,conjugate(v))
    return a % V == b % V == 0

windows=0
middle_excluded=0
for direct,boundary,low,upper,nb,nk in product((F(1,2),F(1),F(3,2)),(F(1),),(1,7),(F(1,2),F(1),F(7),F(13)),(1,7,13),(1,7,13,19)):
    in_direct=direct<=boundary
    in_low=not in_direct and nk<=low
    in_middle=not in_direct and low<nk<=upper
    in_far=not in_direct and nk>max(low,upper)
    assert sum(map(int,(in_direct,in_low,in_middle,in_far)))==1
    selected=F(nk,20)
    lhs=selected*(int(in_direct)+int(in_low)+int(in_far)+int(in_middle and nb!=nk))
    rhs=selected-selected*int(in_middle and nb==nk)
    assert lhs==rhs
    windows+=1
    middle_excluded+=int(in_middle and nb==nk)
assert middle_excluded>0

selector=0
for x,y in product(range(-9,10),repeat=2):
    z=(x,y)
    if z==(0,0):
        continue
    p7=(3,1)
    p13=(4,1)
    assert norm(p7)==7 and norm(p13)==13
    assert int(not divides(p7,z) and not divides(p13,z)) == 1-int(divides(p7,z))-int(divides(p13,z))+int(divides(mul(p7,p13),z))
    selector+=1

rescaling=0
for L,Q,T,V,Nb in product((F(3,8),F(7,6),F(3)),(37,73),(F(1),F(9,2),F(73)),(1,7,13,37,73),(1,7,19,49)):
    Y=4*L*T/(3*Q)
    assert Y==4*(L*V)*(T/V)/(3*Q)
    assert Y*Nb/(L*V)==4*T*Nb/(3*Q*V)
    assert F(3*Q,4)/(L*V*(T/V))==F(3*Q,4)/(L*T)
    rescaling+=1

# A Gaussian test uses closed-form Fourier transforms and validates exact
# normalization. It is distinct from the compact-profile asymptotic argument.
def phase(x):
    return complex(cos(2*pi*x),sin(2*pi*x))

cells=[]
for Q in (37,73):
    for w in range(1,Q):
        if (w*w+w+1)%Q:
            continue
        generator=next((a,b) for a,b in product(range(-12,13),repeat=2) if norm((a,b))==Q and (a+b*w)%Q==0)
        eps=1+w
        sixth={pow(eps,k,Q):phase(k/6) for k in range(6)}
        symbol=[0j]+[sixth[pow(x,(Q-1)//6,Q)] for x in range(1,Q)]
        assert abs(symbol[eps]-1)<1e-14
        inv=conjugate(generator)
        inv_c=complex(inv[0]-inv[1]/2,inv[1]*sqrt(3)/2)/Q
        dual_unit=(2j/sqrt(3))*inv_c.conjugate()
        coeff=dual_unit.conjugate().real
        gauss=sum(symbol[x]*phase(x*coeff) for x in range(Q))
        assert abs(abs(gauss)-sqrt(Q))<3e-12, (Q,w,gauss)
        gamma=gauss/sqrt(Q)
        masks=(("unit",(1,0)),("good7",(3,1)),("good13",(4,1)),("conductor",generator),("conjugate_conductor",conjugate(generator)))
        # Exact finite lattice sample. The two conjugate orientations are
        # distinct conductor labels even when their rational norms coincide.
        bound=180
        primal_hist={}
        dual_hist={name:{} for name,_ in masks}
        for a,b in product(range(-bound,bound+1),repeat=2):
            s=symbol[(a+b*w)%Q]
            if not s:
                continue
            n=norm((a,b))
            primal_hist[n]=primal_hist.get(n,0j)+s/6
            if n>10000:
                continue
            for name,v in masks:
                if divides(v,(a,b)):
                    h=dual_hist[name]
                    h[n]=h.get(n,0j)+s.conjugate()/6
        for L,T,a,width,(name,v) in product((F(3,8),F(5,4),F(3)),(F(1),F(Q,5),F(Q),F(2*Q)),(F(3,4),F(5,4)),(F(1,2),),masks):
            V=norm(v)
            c=1/a+3*Q*width/(4*L*T)
            s_v=symbol[(v[0]+v[1]*w)%Q]
            left=2*float(L)*gamma/(sqrt(3*Q))*sum(s*exp(-pi*float(4*L*n/(3*Q*a)+width*n/T)) for n,s in dual_hist[name].items())
            right=s_v.conjugate()/float(V*a*c)*sum(s*exp(-pi*float(n/(L*V*c))) for n,s in primal_hist.items())
            err=abs(left-right)
            assert err<3e-10,(Q,w,L,T,name,err,left,right)
            cells.append((name,err,int(abs(left)>1e-7)))
assert any(name=="conjugate_conductor" and value for name,_,value in cells)
assert all(not value for name,_,value in cells if name=="conductor")
receipt = {
    "status":"pass",
    "source_hashes":PINS,
    "independent_windows":windows,
    "middle_removed":middle_excluded,
    "fixed_avoidance_projectors":selector,
    "exact_rescalings":rescaling,
    "gaussian_poisson_cells":len(cells),
    "nonzero_gaussian_cells":sum(value for _,_,value in cells),
    "gaussian_max_absolute_error":max(err for _,err,_ in cells),
    "control_scope":"The finite exact arithmetic checks retain strict original windows, norm equality, distinct conjugate conductors, and ideal divisibility. The separate floating-point Gaussian checks compare the original frequency-restricted side with the inverse primal side for both orientations at norms 37 and 73, with and without vanishing raw factors. The Gaussian test uses an analytic Schwartz profile and filter, and is not a run of the compact profile in the proof or a numerical verification of the bound.",
}
out = OUT/"smooth-radial-partner-controls-v1.json"
with out.open("x") as handle:
    dump(receipt,handle,indent=2,sort_keys=True)
    handle.write("\n")
print({k:v for k,v in receipt.items() if k not in ("source_hashes","control_scope")})
print(sha256(out.read_bytes()).hexdigest(),out)

