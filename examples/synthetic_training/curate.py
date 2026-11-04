"""Additional immutable curation pass: all-conformer geometry and split witnesses."""
import argparse,json,shutil
from collections import Counter,defaultdict
from pathlib import Path
import numpy as np
import pyarrow.parquet as pq
from common import fresh,finish,canonical,sha,connected_groups,assign_components,write_json,stratum

def read_rows(folder):
    return [r for p in sorted((folder/'data').glob('*.parquet')) for r in pq.read_table(p).to_pylist()]

def curate(source,out):
    source=Path(source);out=fresh(out);rows=read_rows(source)
    manifest=json.loads((source/'manifest.json').read_text())
    for name,item in manifest['files'].items():assert sha(source/name)==item['sha256']
    old_audit=json.loads((source/'split-audit.json').read_text());report=json.loads((source/'quality.json').read_text())
    payloads=[json.loads(r['payload_json']) for r in rows]
    if 'molecules' in old_audit:
        # Each existing chemical similarity component is indivisible. Add edges
        # for close rotation/permutation-invariant heavy-atom distance descriptors.
        groups=sorted({r['group_id'] for r in rows});features=defaultdict(list)
        for r,p in zip(rows,payloads):
            c=p['conditions'];z=np.array(c['atomic_numbers']);x=np.array(c['coordinates_angstrom'])[z>1]
            sig=tuple(sorted(z[z>1].tolist()));d=np.linalg.norm(x[:,None]-x[None,:],axis=-1)
            descriptor=np.sort(d[np.triu_indices(len(x),1)])
            features[r['group_id']].append((sig,descriptor,r['record_id']))
        minimum={};witness={}
        def similar(a,b):
            best=float('inf');pair=None
            for sig,x,id1 in features[a]:
                for other,y,id2 in features[b]:
                    if sig!=other:continue
                    distance=float(np.sqrt(np.mean((x-y)**2)))
                    if distance<best:best=distance;pair=(id1,id2)
            minimum[tuple(sorted((a,b)))]=best;witness[tuple(sorted((a,b)))]=pair
            return 'heavy_element_multiset_and_sorted_pair_distance_RMS<=0.10angstrom' if best<=.10 else None
        components,edges=connected_groups(groups,similar)
        mapping={g:f'bio-geometry-component-{components[i]:04d}' for i,g in enumerate(groups)}
        allocation=assign_components(rows,mapping);assignment={r['group_id']:r['split'] for r in rows}
        cross=[]
        for (a,b),distance in minimum.items():
            if np.isfinite(distance) and assignment[mapping[a]]!=assignment[mapping[b]]:
                cross.append(dict(a=a,b=b,distance_angstrom=distance,record_pair=witness[(a,b)]))
        assert all(p['distance_angstrom']>.10 for p in cross)
        original=json.loads(json.dumps(old_audit))
        old_audit.update(initial_chemical_split_policy_preserved_as_components=True,geometric_threshold_angstrom=.10,
            geometric_metric='RMS difference of sorted all heavy-atom pair distances, comparing identical heavy-element multisets; all emitted conformers/perturbations considered',
            geometric_metric_limit='Conservative invariant descriptor, not a complete congruence invariant or a certified RMSD optimizer. False-positive grouping is possible.',
            added_geometry_edges=[dict(a=groups[i],b=groups[j],reason=reason,witness=witness[tuple(sorted((groups[i],groups[j])))]) for i,j,reason in edges],
            cross_split_nearest_geometry=sorted(cross,key=lambda p:p['distance_angstrom'])[:20],
            final_component_allocation=allocation)
        for m in old_audit['molecules']:
            if m['component'] in mapping:m['component']=mapping[m['component']];m['split']=assignment[m['component']]
        from rdkit import Chem,DataStructs
        from rdkit.Chem import rdFingerprintGenerator
        fingerprint=rdFingerprintGenerator.GetMorganGenerator(radius=2,fpSize=2048,includeChirality=False)
        molecules=old_audit['molecules'];fps=[fingerprint.GetFingerprint(Chem.MolFromSmiles(m['smiles'])) for m in molecules]
        chemistry=[]
        for i,m in enumerate(molecules):
            for j,other in enumerate(molecules[:i]):
                if m['split'] and other['split'] and m['split']!=other['split']:
                    chemistry.append(dict(a=m['parent'],b=other['parent'],tanimoto=DataStructs.TanimotoSimilarity(fps[i],fps[j])))
        assert all(v['tanimoto']<.65 for v in chemistry)
        old_audit.update(allocation)
        old_audit.update(parent_audit=original,cross_split_max_Morgan_Tanimoto=max([x['tanimoto'] for x in chemistry],default=0.),
            cross_split_nearest_chemical=sorted(chemistry,key=lambda x:-x['tanimoto'])[:20])
    else:
        # The material generation already grouped all accepted proximity edges.
        # Recompute cross-split nearest parameter and finite-spectrum distances.
        base=[(r,p) for r,p in zip(rows,payloads) if r['record_id'].endswith('-base')];near=[]
        for i,(r,p) in enumerate(base):
            f=r['family'];c=p['conditions']['parameters']
            def vector(c):
                if f=='ssh':return np.sort([c['t1']/2,c['t2']/2])
                if f=='kitaev':return np.array([c['t']/2,c['delta'],abs(c['mu'])/4])
                if f=='qwz':return np.array([c['mass']/6])
                if f=='rice_mele_pump':return np.array([c['dimerization'],c['stagger']/2])
                if f=='harper_photonic':return np.array([c['hopping']/2,c['onsite']/2])
                return np.array([c['Jplus']/3,c['Jminus']/3,c['field']])
            threshold=.012 if f=='qwz' else .06
            for other,q in base[:i]:
                if other['family']!=f or other['split']==r['split']:continue
                cc=q['conditions']['parameters']
                if c.get('q',c.get('m'))!=cc.get('q',cc.get('m')):continue
                d=float(np.linalg.norm(vector(c)-vector(cc)));assert d>threshold
                e=np.array(p['targets'].get('open_spectrum',[]));ee=np.array(q['targets'].get('open_spectrum',[]))
                sd=float(np.linalg.norm(e-ee)/max(np.linalg.norm(e),np.linalg.norm(ee),1e-12)) if len(e) else None
                if sd is not None:assert sd>.012
                near.append(dict(a=r['record_id'],b=other['record_id'],family=f,parameter_distance=d,spectrum_relative_distance=sd))
        old_audit['cross_split_nearest_parameter']=sorted(near,key=lambda x:x['parameter_distance'])[:30]
        old_audit['cross_split_nearest_spectrum']=sorted([x for x in near if x['spectrum_relative_distance'] is not None],key=lambda x:x['spectrum_relative_distance'])[:30]
    strata=Counter()
    for r,p in zip(rows,payloads):
        strata[(r['split'],stratum(r))]+=1
    old_audit['stratum_counts']=[dict(split=s,stratum=t,records=n) for (s,t),n in sorted(strata.items())]
    old_audit['bulk_slice_note']='Periodic bulk curves use ky=0; finite open strips use ky=.37. A single strip is not an edge-dispersion proof.'
    old_audit['limitation']='Component-level strata are balanced where feasible; phase/rare-stratum coverage can be lost to indivisible large components. No universal leakage or overfitting guarantee; leave-family-out requires separate evaluation.'
    old_audit['final_assignments']=[dict(record_id=r['record_id'],component=r['group_id'],split=r['split']) for r in rows]
    old_audit['cross_split_known_similarity_edges']=0
    write_json(out/'split-audit.json',old_audit)
    if (source/'failures.json').exists():shutil.copyfile(source/'failures.json',out/'failures.json')
    report.update(curation_parent_manifest_sha256=sha(source/'manifest.json'),geometric_and_topological_split_audit=True)
    # All computed labels are immutable across the curation-only pass.
    assert sorted((r['record_id'],r['condition_json'],r['target_json'],r['payload_json']) for r in rows)==sorted((r['record_id'],r['condition_json'],r['target_json'],r['payload_json']) for r in read_rows(source))
    code=out/'parent_generation_source';code.mkdir()
    for name,digest in manifest['source_code_sha256'].items():
        p=source/'generation_source'/name
        if not p.exists():p=Path(__file__).parent/name
        assert sha(p)==digest,'Original generator changed: preserve and use its exact source snapshot'
        shutil.copyfile(p,code/name)
    write_json(out/'parent-manifest.json',manifest)
    finish(out,rows,report,manifest['description']+'; additional similarity curation')
    print(dict(output=str(out),records=len(rows),split_counts=report['split_counts']))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();curate(a.source,a.output)
