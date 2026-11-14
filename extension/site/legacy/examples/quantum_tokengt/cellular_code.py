"""Exact F2 cellular CSS diagnostic on the actual genus-two dessin cellulation.

This additional *bad-distance* example is distinct from the executed three-
qubit repetition channel. A one-face cellulation does not give a useful memory.
"""
import itertools,json
from pathlib import Path

def span(rows):
    values={0}
    for row in rows:values|={v^row for v in list(values)}
    return values

def diagnostic(m=5):
    assert m>=3 and m%2==1
    edges=[(b,2+j) for b in range(2) for j in range(m)]
    # Clean subdivision: two black vertices, m degree-two white vertices,
    # 2m physical edges, one face. Each edge occurs twice in its face boundary.
    hx=[sum((1<<i) for i,e in enumerate(edges) if v in e) for v in range(m+2)]
    hz=[0];sx=span(hx);sz=span(hz);rankx=len(sx).bit_length()-1;rankz=0;n=len(edges)
    assert all((a&b).bit_count()%2==0 for a in hx for b in hz)
    dx=next(w for w in range(1,n+1) if any(sum(1<<i for i in s) not in sx for s in itertools.combinations(range(n),w)))
    dz=None;zwitness=None
    for w in range(1,n+1):
        for positions in itertools.combinations(range(n),w):
            z=sum(1<<i for i in positions)
            if z not in sz and all((a&z).bit_count()%2==0 for a in hx):dz=w;zwitness=list(positions);break
        if dz is not None:break
    return dict(m=m,genus=(m-1)//2,physical_vertices=m+2,physical_edges=edges,faces=1,
        boundary1_rows=hx,boundary2_columns=hz,rank_HX=rankx,rank_HZ=rankz,encoded_qubits=n-rankx-rankz,
        distance_X=dx,distance_Z=dz,distance=min(dx,dz),Z_logical_witness_edges=zwitness,
        chain_condition=True,scope='Exact finite CSS stabilizer rank/distance; single-face plaquetteboundaryiszero overF2, so distance1 and no useful topologicalprotection. No faulttolerance/hardwareclaim.')

def main():
    d=diagnostic();assert (d['encoded_qubits'],d['distance_X'],d['distance_Z'])==(4,1,4)
    out=Path(__file__).resolve().parents[2]/'outputs/checks/2026-11-03-actual-rg/quantum-tokengt';out.mkdir(parents=True,exist_ok=True)
    (out/'cellular-css.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d))
if __name__=='__main__':main()
