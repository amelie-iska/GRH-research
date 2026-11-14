"""Immutable supplementary-dataset utilities. No model or credential imports."""
from pathlib import Path
import hashlib,json,platform
import numpy as np

SEED=20261104
def canonical(v):return json.dumps(v,sort_keys=True,separators=(',',':'),allow_nan=False)
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def split(group):
    x=int(hashlib.sha256(('grh-supplement-v1:'+group).encode()).hexdigest()[:12],16)/16**12
    return 'train' if x<.8 else 'validation' if x<.9 else 'test'
def fresh(path):
    path=Path(path)
    if path.exists():raise FileExistsError('Use a new immutable output directory')
    path.mkdir(parents=True);return path
def write_json(path,value):Path(path).write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')
def finish(out,rows,report,description):
    """One explicit, stable Arrow schema; full scientific payload remains lossless JSON."""
    import pyarrow as pa
    import pyarrow.parquet as pq
    out=Path(out);(out/'data').mkdir()
    schema=pa.schema([('record_id',pa.string()),('family',pa.string()),('group_id',pa.string()),
        ('split',pa.string()),('evidence',pa.string()),('condition_json',pa.string()),
        ('target_json',pa.string()),('payload_json',pa.string())])
    counts={}
    for name in ['train','validation','test']:
        subset=[r for r in rows if r['split']==name];assert subset,name;counts[name]=len(subset)
        table=pa.Table.from_pylist(subset,schema=schema)
        pq.write_table(table,out/'data'/f'{name}-00000-of-00001.parquet',compression='zstd',version='2.6')
        actual=pq.read_table(out/'data'/f'{name}-00000-of-00001.parquet').to_pylist()
        assert actual==subset,'Parquet round-trip changed a field'
    report.update(records=len(rows),split_counts=counts,groups=len({r['group_id'] for r in rows}),
                  numpy=np.__version__,python=platform.python_version(),seed=SEED,
                  native_model_admission=False,neural_optimizer_updates=0)
    write_json(out/'quality.json',report)
    write_json(out/'examples.json',[json.loads(r['payload_json']) for r in rows[:3]])
    files={str(p.relative_to(out)):{'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(out.rglob('*')) if p.is_file()}
    write_json(out/'manifest.json',dict(schema='grh-complementary-physics-v1',description=description,
        files=files,source_code_sha256={p.name:sha(p) for p in Path(__file__).parent.glob('*.py')},
        split_policy='Whole parent / scaffold-similarity groups, never random rows',seed=SEED))
    return report
def row(identity,family,group,conditions,targets,payload):
    return dict(record_id=identity,family=family,group_id=group,split=split(group),
        evidence='synthetic_computed',condition_json=canonical(conditions),target_json=canonical(targets),payload_json=canonical(payload))

def connected_groups(items,similar):
    """Transitive closure, so no accepted similarity edge crosses a split."""
    parent=list(range(len(items)));edges=[]
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    for i in range(len(items)):
        for j in range(i):
            reason=similar(items[i],items[j])
            if reason:parent[find(i)]=find(j);edges.append((i,j,reason))
    groups={i:find(i) for i in range(len(items))}
    return groups,edges

def assign_components(rows,component_map):
    """Greedy whole-component balance; never break a large similarity component."""
    from collections import Counter,defaultdict
    old=Counter(r['group_id'] for r in rows);counts=Counter()
    for g,n in old.items():counts[component_map[g]]+=n
    if len(counts)<3:raise ValueError('Similarity graph has fewer than three components; do not manufacture an independent split')
    allocation=Counter();assignment={};ratios={'train':.8,'validation':.1,'test':.1}
    order=sorted(counts,key=lambda g:(-counts[g],hashlib.sha256(g.encode()).hexdigest()))
    for k,g in enumerate(order):
        missing=[s for s in ratios if s not in assignment.values()]
        eligible=missing if len(order)-k<=len(missing) else list(ratios)
        chosen=min(eligible,key=lambda s:(allocation[s]+counts[g])/ratios[s]);assignment[g]=chosen;allocation[chosen]+=counts[g]
    for r in rows:r['group_id']=component_map[r['group_id']];r['split']=assignment[r['group_id']]
    assert all(len({r['split'] for r in rows if r['group_id']==g})==1 for g in assignment)
    return dict(component_count=len(counts),largest_component_rows=max(counts.values()),split_rows=dict(allocation),
                policy='Connected similarity components, greedy whole-component80/10/10 balance; oversized components preserved')

def persistence(points):
    """Complete finite Euclidean VR H0/H1 over F2, including all triangles."""
    from itertools import combinations
    points=np.asarray(points);n=len(points);dist=np.linalg.norm(points[:,None]-points[None,:],axis=-1)
    simplices=[(0.,(i,)) for i in range(n)]
    simplices +=[(float(dist[i,j]),(i,j)) for i,j in combinations(range(n),2)]
    simplices +=[(float(max(dist[i,j],dist[i,k],dist[j,k])),(i,j,k)) for i,j,k in combinations(range(n),3)]
    simplices.sort(key=lambda x:(x[0],len(x[1]),x[1]));lookup={s:i for i,(_,s) in enumerate(simplices)}
    reduced={};positive={};bars={0:[],1:[]}
    for j,(value,s) in enumerate(simplices):
        col={lookup[s[:k]+s[k+1:]] for k in range(len(s))} if len(s)>1 else set()
        while col and max(col) in reduced:col ^= reduced[max(col)]
        if col:
            pivot=max(col);reduced[pivot]=col;birth=simplices[pivot][0];dim=len(simplices[pivot][1])-1
            if dim<=1 and value>birth+1e-10:bars[dim].append([birth,value])
            positive.pop(pivot,None)
        elif len(s)<=2:positive[j]=True
    return dict(H0=bars[0],H1=bars[1],H0_essential=sum(len(simplices[i][1])==1 for i in positive),
                metric='Euclidean heavy-atom distances in angstrom',coefficient_field='F2',max_simplex_dimension=2)
