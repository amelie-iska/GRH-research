from pathlib import Path
from fractions import Fraction as F
import json,hashlib
ROOT=Path("/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104")
OUT=ROOT/"outputs/checks/2026-11-06-unit-gauss/lane-c/interval-v1"
OUT.mkdir(parents=True,exist_ok=False)
def canon(k,N):
 out=[];start=1
 for length in [1<<j for j in range(N.bit_length()-1,-1,-1)]:
  if k>=length:
   out.append((start,start+length-1,N.bit_length()-length.bit_length()))
   start+=length;k-=length
 assert k==0
 return out
prefixes=0;intervals=0;depth_pairs=0
for n in range(1,65):
 N=1<<(n-1).bit_length();h=N.bit_length()-1;parts={}
 for k in range(n+1):
  blocks=canon(k,N);parts[k]=blocks
  flat=[j for lo,hi,d in blocks for j in range(lo,hi+1)]
  assert flat==list(range(1,k+1))
  assert len({d for lo,hi,d in blocks})==len(blocks)<=h+1
  prefixes+=1
 for depth in range(h+1):
  rowsets={}
  for k,blocks in parts.items():
   for lo,hi,d in blocks:
    if d==depth:rowsets.setdefault((lo,hi),set()).add(k)
  values=list(rowsets.values())
  for i,a in enumerate(values):
   for b in values[i+1:]:
    assert not a&b;depth_pairs+=1
 if n<=24:
  for a in range(n+1):
   for b in range(n+1):
    actual=[int(a<j<=b) if a<=b else 0 for j in range(1,n+1)]
    rebuilt=[int(a<=b)*(int(j<=b)-int(j<=a))for j in range(1,n+1)]
    assert actual==rebuilt;intervals+=1
values=[7,7,13,13,19,19,25,31,31]
distinct=sorted(set(values));fibre_cases=0
for lower in [0,7,8,13,19,25,31,32]:
 for upper in [0,7,13,18,19,25,31,32]:
  for lower_closed in [False,True]:
   for upper_closed in [False,True]:
    a=sum(x<lower if lower_closed else x<=lower for x in distinct)
    b=sum(x<=upper if upper_closed else x<upper for x in distinct)
    actual=[int((x>=lower if lower_closed else x>lower)and(x<=upper if upper_closed else x<upper))for x in values]
    rank=[int(a<distinct.index(x)+1<=b) if a<=b else 0 for x in values]
    assert actual==rank;fibre_cases+=1
A=[[F(1),F(1)],[F(-1),F(1)]];M=[[1,0],[1,1]]
assert [[sum(A[k][i]*A[k][j]for k in range(2))for j in range(2)]for i in range(2)]==[[2,0],[0,2]]
z=[F(1),F(-1,2)];B=[[A[i][j]*M[i][j]for j in range(2)]for i in range(2)]
ratio=sum(sum(B[i][j]*z[j]for j in range(2))**2 for i in range(2))/sum(x*x for x in z)
assert ratio==F(13,5)>2
note=ROOT/"planning/unit-gauss-20261106/lane-c/ROW_INTERVAL_SCHUR-v1.md"
result=dict(passed=True,prefix_cases=prefixes,interval_cases=intervals,disjoint_rowset_pairs=depth_pairs,repeated_fibre_endpoint_cases=fibre_cases,norm_one_counterexample_Rayleigh_ratio=str(ratio),original_matrix_norm_squared=2,note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),scope="Fresh deterministic finite combinatorial/Fraction controls for row-interval Schur lemma only; no actual ideal/character/Gauss data or Lean.",seed=None,producer_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
with(OUT/"checks-v1.json").open("x")as f:json.dump(result,f,indent=2,sort_keys=True);f.write("\n")
print(json.dumps(result))
