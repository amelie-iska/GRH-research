"""Independent finite Euler-defect oracle, no production imports.
The variables are separate formal prime-ideal variables, so conjugate ideals
with equal rational norms are never identified. No analytic L-value computed.
"""
from pathlib import Path
from itertools import product
import json
import sympy as sp
OUT=Path(__file__).resolve().parent
PRIMES=[(7,2),(7,4),(13,3),(13,9),(19,7),(19,11)]
PHASES=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))
w=sp.Symbol('w');ts=sp.symbols('t0:6')

def emul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1]
def epow(a,n):
 r=(1,0)
 for _ in range(n):r=emul(r,a)
 return r
def phase(j,a):
 p,root=PRIMES[j];v=(a[0]+a[1]*root)%p
 if not v:return None
 return {pow(1+root,k,p):k for k in range(6)}[pow(v,(p-1)//6,p)]
def scalar(k):return PHASES[k][0]+PHASES[k][1]*w

def reduce(q):
 numerator,denominator=sp.fraction(sp.cancel(q))
 numerator=sp.rem(sp.Poly(numerator,w),sp.Poly(w*w+w+1,w)).as_expr()
 return sp.cancel(numerator/denominator)

pi=(1,3);p_index=0;assert phase(p_index,pi) is None
counts=0;events=[]
for e in range(1,7):
 u=epow(pi,e)
 for nu in ['principal','fixed-numerator-2']:
  eta=[0 if nu=='principal' else phase(j,(2,0)) for j in range(6)]
  actual=[None if phase(j,u) is None else (phase(j,u)+eta[j])%6 for j in range(6)]
  assert actual[0] is None
  if e==6:assert all(actual[j]==eta[j] for j in range(1,6))
  # At p, tame Kummer ramification is e mod6; its square is 2e mod6.
  # For e3 the Kummer square is globally principal, retaining unramified nu².
  # For e6 the Kummer character is globally principal, retaining nu.
  psi_ram=[False]*6;psi2_ram=[False]*6
  psi_ram[0]=e%6!=0;psi2_ram[0]=e%3!=0
  prim=[scalar(k) if k is not None else None for k in actual]
  square=[reduce(z*z) if z is not None else None for z in prim]
  if not psi_ram[0]:prim[0]=scalar(eta[0])
  if not psi2_ram[0]:square[0]=scalar((2*eta[0])%6)
  for deletion in [set(),{2},{2,4},{0,2}]:
   T=deletion|{0};target=sp.Integer(1);ratio=sp.Integer(1);defect=sp.Integer(1)
   for j,t in enumerate(ts):
    if j not in T:target*=1+prim[j]*t
    if not psi_ram[j]:ratio/=1-prim[j]*t
    if not psi2_ram[j]:ratio*=1-square[j]*t*t
    if j in T:
     if not psi_ram[j]:defect*=1-prim[j]*t
     if not psi2_ram[j]:defect/=1-square[j]*t*t
   # Factored local proof avoids expensive global rational expansion.
   for j,t in enumerate(ts):
    R=sp.Integer(1)
    if not psi_ram[j]:R/=1-prim[j]*t
    if not psi2_ram[j]:R*=1-square[j]*t*t
    D=sp.Integer(1)
    if j in T:
     if not psi_ram[j]:D*=1-prim[j]*t
     if not psi2_ram[j]:D/=1-square[j]*t*t
    desired=1 if j in T else 1+prim[j]*t
    assert reduce(R*D-desired)==0,(e,nu,T,j)
    counts+=1
   # Independent coefficient support over squarefree monomials.
   for support in product([0,1],repeat=6):
    masked=any(support[j] and j in T for j in range(6))
    phase_sum=sum(actual[j] for j in range(6) if support[j] and actual[j] is not None)%6
    rhs=0 if masked else scalar(phase_sum)
    lhs=sp.Integer(1)
    for j in range(6):
     if support[j]:lhs*=0 if j in T else prim[j]
    assert reduce(lhs-rhs)==0
   if e in [3,6] and nu=='principal' and T=={0}:
    t=ts[0]
    wrong=(1-t*t) if e==3 else 1+t
    assert wrong!=1
    events.append(dict(exponent=e,primitive_ramified=psi_ram[0],square_ramified=psi2_ram[0],
                       naive_local=str(wrong),required_masked_local='1'))
q=sp.Symbol('q')
assert sp.factor((1-1/q)/(1-1/q**2)-q/(q+1))==0
report=dict(passed=True,local_euler_checks=counts,squarefree_support_checks=6*2*4*64,
 prime_ideals=PRIMES,row_generator=pi,row_exponents=list(range(1,7)),
 fixed_nu=['principal','Kummer numerator2'],collapse_controls=events,
 principal_residue_local_factor='q/(q+1)',
 scope='Finite formal Euler/local coefficient diagnostics. Tame ramification law, global primitive Hecke construction, conductor bounds, FE/convexity and contour estimates remain mathematical proof/external classical inputs; no L-values or GRH certification.')
(OUT/'local-oracle.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
