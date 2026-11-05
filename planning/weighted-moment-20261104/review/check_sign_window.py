from pathlib import Path
from fractions import Fraction as F
import itertools,json,hashlib,argparse

def main(output):
 if output.exists():raise FileExistsError('Preserve prior diagnostic report')
 # Four norm-prime generators and the inert rational prime5.
 generators=[(3,1),(4,1),(5,2),(6,1),(5,0)]
 norms=[a*a-a*b+b*b for a,b in generators]
 assert norms==[7,13,19,31,25] and len(set(norms))==5
 for p in norms[:4]:assert all(p%d for d in range(2,int(p**.5)+1))
 assert all((x*x+x+1)%5 for x in range(5)) # O/(5) is a field.
 cases=middle=0
 for mask in range(1<<len(norms)):
  ns=[n for i,n in enumerate(norms) if mask>>i&1];nm=1
  for n in ns:nm*=n
  mu=(-1)**len(ns)
  options=set(map(F,[1,2,5,7,10,13,19,25,31,50,100,300,1000,nm,max(1,nm-1)]));options.add(max(F(1),F(nm,2)))
  for U in options:
   A=0
   for choices in itertools.product(range(3),repeat=len(ns)):
    na=nb=1;sign=1
    for n,c in zip(ns,choices):
     if c==1:na*=n;sign=-sign
     elif c==2:nb*=n;sign=-sign
    if na<=U and nb<=U:A+=sign
   if nm<=U:assert A==mu
   if U<nm<=U*U:assert A==-mu;middle+=1
   cases+=1
 result={'passed':True,'exact_cutoff_cases':cases,'middle_window_cases':middle,'generators_in_Z_omega':generators,'prime_ideal_norms':norms,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact finite disjoint-convolution band controls; full identity has a prose proof. No sextic-symbol, analytic, Lean or GRH claim.'}
 output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(result,indent=2)+chr(10));print(json.dumps(result,indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();main(a.output)
