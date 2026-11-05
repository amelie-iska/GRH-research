"""Focused exact diagnostics for the new ordinary-character envelope.
No enumeration replaces the infinite lattice/character proof in the note.
Python standard library only; writes only to the explicit fresh output path.
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import combinations
import argparse, hashlib, json, math, subprocess

ROOT=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
ZERO=(0,0); ONE=(1,0)
# zeta6^2=zeta6-1, with rational/integer coordinates.
def ca(x,y): return (x[0]+y[0],x[1]+y[1])
def cm(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1])
def cc(x): return (x[0]+x[1],-x[1])
def cn(x): return x[0]*x[0]+x[0]*x[1]+x[1]*x[1]
def cs(x,n): return (x[0]*n,x[1]*n)
ZETA=[ONE,(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
def em(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
def ec(x): return (x[0]-x[1],-x[1])
def en(x): return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]
def eq(x,y):
 z=em(x,ec(y)); return (F(z[0],en(y)),F(z[1],en(y)))
def states(budget,prefix=()):
 j=len(prefix)+1
 if j==7:
  yield prefix; return
 for k in range(budget//j+1): yield from states(budget-j*k,prefix+(k,))
def primitive_root(p):
 return next(g for g in range(2,p) if len({pow(g,k,p) for k in range(p-1)})==p-1)

def run(output):
 assert not output.exists(), 'Fresh output target required'
 output.mkdir(parents=True)
 counts={'capacity_envelope':0,'face':0,'gauss':0,'character_domination':0,'reduced_fraction':0,'source_integrity':0}
 feasible=0; worst=[]
 for raw in states(36):
  x=tuple(F(k,48) for k in raw); C=sum((j+1)*x[j] for j in range(6)); r=sum(x); m=max(x[:2]); q=r-x[5]
  assert C<=F(3,4)
  slack=C-2*r+m
  assert slack>=0
  expected=x[2]+2*x[3]+3*x[4]+4*x[5]+(x[1]-x[0] if x[1]>x[0] else 0)
  assert slack==expected
  assert 2*C+m-3*r==(m-x[0])+x[1]+3*x[2]+5*x[3]+7*x[4]+9*x[5]>=0
  assert r<=C and 6*x[5]<=C
  old=max(r,1+r-m,F(2,3)+r-m/3)
  general=max(1+x[5],x[5]+2*q)
  quad=max(r,1+r-x[2])
  best=min(old,general,quad)
  assert best<=F(7,6)
  # Check the precise log version of min(D S,H^2/S^2).
  s=r-m; h=F(3,4)
  assert min(1+s,2*h-2*s)<=F(2,3)*(1+h)
  if best==F(7,6): worst.append([str(t) for t in x])
  counts['capacity_envelope']+=8; feasible+=1
 witness=(F(5,12),F(1,6),F(0),F(0),F(0),F(0))
 assert list(map(str,witness)) in worst
 for k in range(1001):
  a=F(k,4000); b=F(1,4)-a; q=2*a+b
  assert a>=0 and b>=0 and q<=F(1,2)
  assert max(F(1),2*q)==1
  # The pair-only estimate is useful but the triple is stronger.
  pair=max(1+b,4*a+b)
  assert max(F(1),2*q)<=pair
  counts['face']+=3
 # Primitive order-dividing6 character Gauss identity over small split fields.
 # Coefficients of e_p(t) in |tau|^2: p-1 at t0, -1 elsewhere.
 gauss_fields=[]
 for p in (7,13,19,31):
  g=primitive_root(p); logs={pow(g,k,p):k for k in range(p-1)}
  def chi(x,j): return ZERO if x%p==0 else ZETA[(j*logs[x%p])%6]
  for j in range(1,6):
   coeff=[ZERO]*p
   for xx in range(1,p):
    for yy in range(1,p):
     t=(xx-yy)%p; coeff[t]=ca(coeff[t],cm(chi(xx,j),cc(chi(yy,j))))
   assert coeff[0]==(p-1,0)
   assert all(c==(-1,0) for c in coeff[1:])
   # Since sum_t e_p(t)=0 this is exactly |tau|^2=p.
   assert sum((chi(x,j)[0] for x in range(1,p)))==0
   assert sum((chi(x,j)[1] for x in range(1,p)))==0
   counts['gauss']+=4
  gauss_fields.append({'norm':p,'primitive_root':g,'tested_powers':[1,2,3,4,5]})
  for seed in range(7):
   coeffs={z:((z*3+seed)%9-4,(z*z+seed)%7-3) for z in range(-2*p,2*p+1)}
   energies=[]
   for j in range(1,6):
    total=ZERO
    for z,c in coeffs.items():total=ca(total,cm(c,chi(z,j)))
    energies.append(cn(total))
   residue=[ZERO]*p
   for z,c in coeffs.items():residue[z%p]=ca(residue[z%p],c)
   allcharacter_energy=(p-1)*sum(cn(z) for z in residue[1:])
   assert sum(energies)<=allcharacter_energy
   counts['character_domination']+=1
 # Reduced fractions from three split ideals and one composite ideal.
 denoms=[((3,1),7),((4,1),13),((5,2),19),(em((3,1),(4,1)),91)]
 fractions=[]
 for f,n in denoms:
  assert en(f)==n
  for xx in range(n):
   if math.gcd(xx,n)==1:fractions.append((xx,f,n))
 for (xx,f,n),(yy,g,nn) in combinations(fractions,2):
  num=(em((xx,0),g)[0]-em((yy,0),f)[0],em((xx,0),g)[1]-em((yy,0),f)[1])
  den=em(f,g); z=eq(num,den)
  assert not (z[0].denominator==1 and z[1].denominator==1)
  # Every nonzero torus numerator is an Eisenstein integer, norm>=1.
  for k in ((0,0),(1,0),(0,1),(-1,1)):
   kd=em(k,den); shifted=(num[0]-kd[0],num[1]-kd[1])
   assert en(shifted)>=1
   assert F(en(shifted),en(den))>=F(1,n*nn)
  counts['reduced_fraction']+=5
 pinpath=ROOT/'planning/arithmetic-learning-20261105/mixed-attempt/source-pins-v1.json'
 pin=json.loads(pinpath.read_text())
 assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()==pin['source_head']
 index=Path(subprocess.check_output(['git','rev-parse','--git-path','index'],cwd=ROOT,text=True).strip())
 if not index.is_absolute():index=ROOT/index
 assert hashlib.sha256(index.read_bytes()).hexdigest()==pin['index_sha256']; counts['source_integrity']+=2
 for rel,info in pin['files'].items():
  data=(ROOT/rel).read_bytes()
  assert len(data)==info['bytes'] and hashlib.sha256(data).hexdigest()==info['sha256']
  counts['source_integrity']+=1
 result={'passed':True,'assertions':sum(counts.values()),'categories':counts,'feasible_capacity_states':feasible,'grid_denominator':48,'capacity_units':36,'worst_envelope_states':worst,'old_worst_exponent':'5/4','new_worst_exponent':'7/6','old_face_new_exponent':'1','new_target_gap_exponent':'5/12','primitive_gauss_fields':gauss_fields,'reduced_fractions':len(fractions),'seed_parameters':list(range(7)),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'source_head':pin['source_head'],'protected_index_sha256':pin['index_sha256'],'scope':'Exact finite capacity/envelope, primitive-Gauss, character-domination and fraction-bookkeeping checks only. Infinite ordinary large-sieve proof is prose; no Lean/GRH/generalization claim.'}
 (output/'mixed-radical-checks-v1.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);args=p.parse_args();run(args.output)
