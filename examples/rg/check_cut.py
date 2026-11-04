#!/usr/bin/env python3
"""Exact path/forbidden-chain diagnostics of the actual m5 gentle cut."""
from pathlib import Path
import json
m=5
# Distinct arrows on each branch; cut source0 on both.
arrows=[(branch,i,i-1) for i in range(1,m) for branch in [0,1]]
paths=[()]*m;levels=[m];previous=[(a,) for a in arrows]
for length in range(1,7):
 levels.append(len(previous));paths+=previous
 previous=[p+(a,) for p in previous for a in arrows if p[-1][2]==a[1] and p[-1][0]==a[0]]
assert levels==[5,8,6,4,2,0,0] and len(paths)==25
ext=[]
for degree in range(6):
 mat=[]
 for i in range(m):
  chains=[(a,) for a in arrows if a[1]==i]
  for n in range(1,degree):chains=[p+(a,) for p in chains for a in arrows if p[-1][2]==a[1] and p[-1][0]!=a[0]]
  mat.append([int(i==j) if degree==0 else sum(p[-1][2]==j for p in chains) for j in range(m)])
 ext.append(mat)
assert ext[4][4][0]==2 and all(v==0 for row in ext[5] for v in row)
assert all(v==0 for mat in ext[1:] for v in mat[0])
full_ext5=[[2*int(i==j) for j in range(m)] for i in range(m)]
report=dict(path_counts=levels,dimension=25,cut_ext_by_degree=ext,cut_simple_projective_dimensions=list(range(5)),original_completed_ext5=full_ext5,
 scope='Exact path/endpoint diagnostics; prose resolution and finite-dimensional global-dimension criterion supply the theorem; not an entire Lean category formalization')
out=Path(__file__).resolve().parents[2]/'outputs/checks/2026-11-03-actual-rg/cut.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
