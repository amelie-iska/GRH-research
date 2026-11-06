#!/usr/bin/env python3
"""New c=6 literal-ray Fourier controls only; stdlib exact Z[omega]."""
from pathlib import Path
import argparse,hashlib,json,datetime

def add(x,y):return(x[0]+y[0],x[1]+y[1])
def mul(x,y):
 a,b=x;c,d=y
 return(a*c-b*d,a*d+b*c-b*d)
def norm(x):a,b=x;return a*a-a*b+b*b
def conj(x):a,b=x;return(a-b,-b)
ROOTS=[(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]
def root(n):return ROOTS[n%6]
def phase(beta,x):return root(mul(beta,x)[1])
def run():
 residues=[(a,b) for a in range(6) for b in range(6)]
 allowed=[x for x in residues if x[0]%3==1 and x[1]%3==0 and (x[0]%2,x[1]%2)!=(0,0)]
 assert allowed==[(1,0),(1,3),(4,3)]
 def total(xs):
  r=(0,0)
  for x in xs:r=add(r,x)
  return r
 fourier={beta:total(phase(beta,x) for x in allowed) for beta in residues}
 assert fourier[(0,0)]==(3,0)
 assert sum(norm(z) for z in fourier.values())==108
 for x in residues:
  rec=total(mul(fourier[b],conj(phase(b,x))) for b in residues)
  assert rec==((36,0) if x in allowed else (0,0)),(x,rec)
 projections=[]
 for exponent in range(6):
  z=total(root(exponent*j) for j in range(6))
  assert z==((6,0) if exponent==0 else (0,0))
  projections.append({'unit_character_exponent':exponent,'sum_omega':z})
 primary=[x for x in residues if x[0]%3==1 and x[1]%3==0]
 assert len(primary)==4 and len(primary)!=len(allowed)
 assert len({(a%3,b%3) for a,b in ROOTS})==6
 units3=[(a,b) for a in range(3) for b in range(3) if norm((a,b))%3]
 assert {(a%3,b%3) for a,b in ROOTS}==set(units3)
 return {'schema':'coherent-band-new-literal-ray-local-controls-v1','passed':True,
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':'Only NEW finite S/ray ring O/(6); not original arithmetic columns or a band-bound test.',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'parameters':{'modulus_generator':[6,0],'modulus_norm':36,'seed':None,'coordinate_basis':'1,omega','root':'epsilon=1+omega','additive_pairing':'exp(2pi i Tr(beta*x/(6delta)))=epsilon^(omega-coordinate(beta*x))'},
 'allowed_residues':allowed,'allowed_count':3,'S_mean_ideal_coefficient':{'numerator':1,'denominator':2},
 'fourier':[{'frequency':beta,'value_omega':fourier[beta],'norm_squared':norm(fourier[beta])} for beta in residues],
 'parseval_sum':108,'all36_inversion_equations_exact':True,
 'unit_projections':projections,'unique_primary_unit_section':True,
 'negative_control_drop_prime_above2':{'wrong_allowed_count':len(primary),'wrong_density':{'numerator':2,'denominator':3},'rejected':True},
 'no_original_q_characters_old_controls_or_numeric_approximations':True}
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--output',required=True);args=a.parse_args()
 result=run();dst=Path(args.output)
 with dst.open('x') as f:json.dump(result,f,sort_keys=True,indent=2);f.write('\n')
 print(json.dumps({'passed':True,'output':str(dst),'sha256':hashlib.sha256(dst.read_bytes()).hexdigest()}))
