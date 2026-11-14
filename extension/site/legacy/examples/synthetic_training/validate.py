"""All-row validation independent of simulation control flow. CPU; read-only models."""
import argparse,json,hashlib,math
from collections import defaultdict,Counter
from pathlib import Path
import numpy as np
import pyarrow.parquet as pq
from common import sha,write_json

def betti(points,radius):
    from itertools import combinations
    x=np.asarray(points);n=len(x);d=np.linalg.norm(x[:,None]-x[None,:],axis=-1)
    edges=[(i,j) for i,j in combinations(range(n),2) if d[i,j]<=radius];index={e:k for k,e in enumerate(edges)}
    parent=list(range(n))
    def root(i):
        while parent[i]!=i:i=parent[i]
        return i
    for i,j in edges:parent[root(i)]=root(j)
    b0=len({root(i) for i in range(n)});pivots={}
    for i,j,k in combinations(range(n),3):
        if max(d[i,j],d[i,k],d[j,k])>radius:continue
        v=(1<<index[i,j])^(1<<index[i,k])^(1<<index[j,k])
        while v and v.bit_length()-1 in pivots:v^=pivots[v.bit_length()-1]
        if v:pivots[v.bit_length()-1]=v
    return b0,len(edges)-n+b0-len(pivots)

def validate(folder):
    folder=Path(folder);manifest=json.loads((folder/'manifest.json').read_text())
    for name,item in manifest['files'].items():assert sha(folder/name)==item['sha256'],name
    rows=[r for p in sorted((folder/'data').glob('*.parquet')) for r in pq.read_table(p).to_pylist()]
    assert len({r['record_id'] for r in rows})==len(rows)
    parent_split=defaultdict(set);component_split=defaultdict(set);payloads=[]
    for r in rows:
        p=json.loads(r['payload_json']);payloads.append(p)
        assert json.loads(r['condition_json'])==p['conditions'] and json.loads(r['target_json'])==p['targets']
        parent_split[p['parent']].add(r['split']);component_split[r['group_id']].add(r['split'])
        assert not any(k in p['conditions'] for k in ['targets','observables','topology','energy_kcal_per_mol','forces_kcal_per_mol_angstrom'])
    assert all(len(v)==1 for v in parent_split.values()) and all(len(v)==1 for v in component_split.values())
    report=dict(passed=True,rows=len(rows),parents=len(parent_split),components=len(component_split),
        split_counts=dict(Counter(r['split'] for r in rows)),all_manifest_hashes=True,all_condition_target_projections=True,
        all_parent_and_component_split_separation=True,CPU_only=True)
    if 'hamiltonian_real' in payloads[0] or 'topology' in payloads[0]['targets']:
        max_error=0.;phs=0;null_qwz=0;base={p['parent']:p for p in payloads if p['id'].endswith('-base')}
        for p in payloads:
            c=p['conditions'];t=p['targets'];f=c['family']
            if 'hamiltonian_real' in p:
                H=np.array(p['hamiltonian_real'])+1j*np.array(p['hamiltonian_imag'])
                assert np.max(abs(H-H.conj().T))<1e-12
                e=np.linalg.eigvalsh(H);error=float(np.max(abs(e-np.array(t['open_spectrum']))));assert error<1e-11;max_error=max(max_error,error)
                assert min(t['edge_weight'])>-1e-12 and max(t['edge_weight'])<1+1e-12
                if c['intervention']=='gauge':assert np.max(abs(e-base[p['parent']]['targets']['open_spectrum']))<1e-11
                if f=='kitaev':
                    n=len(H)//2;idx=np.r_[np.arange(n,2*n),np.arange(n)]
                    assert np.max(abs(H.conj()[idx][:,idx]+H))<1e-12;phs+=1
            if f=='qwz':
                m=c['parameters']['mass'];gap=2*min(abs(m+2),abs(m),abs(m-2));assert abs(t['topology']['gap']-gap)<1e-12
                if gap<=.08:assert t['topology']['chern'] is None;null_qwz+=1
                elif t['topology']['chern'] is not None:assert t['topology']['chern']==(0 if abs(m)>2 else -1 if m<0 else 1)
            if f=='dessin_classical_rg':assert abs(sum(t['bulk_curve']['retained_probability'])-1)<1e-12
        report.update(all_Hermitian_eigenspectrum_max_error=max_error,particle_hole_checked_rows=phs,near_critical_QWZ_null_rows=null_qwz)
    else:
        from rdkit import Chem,DataStructs
        from rdkit.Chem import AllChem,rdFingerprintGenerator
        from rdkit.Chem.Scaffolds import MurckoScaffold
        from biomolecules import graph_stereo_ok
        max_energy=0.;max_force=0.;checked_vr=0;mirror_negative=0;chemistry={};geometry=defaultdict(list)
        for r,p in zip(rows,payloads):
            c=p['conditions'];t=p['targets'];x=np.array(c['coordinates_angstrom']);z=np.array(c['atomic_numbers'])
            builder=Chem.RWMol()
            for atomic in z:builder.AddAtom(Chem.Atom(int(atomic)))
            types={1.:Chem.BondType.SINGLE,2.:Chem.BondType.DOUBLE,3.:Chem.BondType.TRIPLE,1.5:Chem.BondType.AROMATIC}
            for b in c['bonds']:builder.AddBond(b['source'],b['target'],types[b['order']])
            m=builder.GetMol();Chem.SanitizeMol(m);conf=Chem.Conformer(m.GetNumAtoms())
            for i,point in enumerate(x):conf.SetAtomPosition(i,tuple(point))
            m.AddConformer(conf);Chem.AssignAtomChiralTagsFromStructure(m,confId=0,replaceExistingTags=True);Chem.AssignStereochemistry(m,cleanIt=True,force=True)
            assert Chem.MolToSmiles(Chem.RemoveHs(m),isomericSmiles=True)==p['canonical_smiles'],'Graph/geometry stereochemistry disagrees with chemical identity'
            props=AllChem.MMFFGetMoleculeProperties(m,mmffVariant='MMFF94')
            ff=AllChem.MMFFGetMoleculeForceField(m,props,nonBondedThresh=100.,ignoreInterfragInteractions=False)
            ee=abs(ff.CalcEnergy()-t['energy_kcal_per_mol']);fe=float(np.max(abs(np.array(ff.CalcGrad()).reshape(-1,3)+t['forces_kcal_per_mol_angstrom'])))
            assert ee<1e-6 and fe<1e-5,(ee,fe);max_energy=max(max_energy,ee);max_force=max(max_force,fe)
            assert graph_stereo_ok(m,x) and graph_stereo_ok(m,np.array(p['inverse_task']['targets']['reference_coordinates_angstrom']))
            if any(a.GetChiralTag()!=Chem.ChiralType.CHI_UNSPECIFIED for a in m.GetAtoms()) and mirror_negative<10:
                assert not graph_stereo_ok(m,-x);mirror_negative+=1
            top=t['heavy_atom_VR'];heavy=x[z>1];dist=np.linalg.norm(heavy[:,None]-heavy[None,:],axis=-1)
            geometry[tuple(sorted(z[z>1].tolist()))].append((r['split'],np.sort(dist[np.triu_indices(len(heavy),1)]),r['record_id']))
            chemistry[p['parent']]=(p['canonical_smiles'],r['split'])
            if checked_vr<12:
                for radius in np.quantile(dist[np.triu_indices(len(heavy),1)],[.1,.25,.5]):
                    b0,b1=betti(heavy,radius)
                    assert b0==top['H0_essential']+sum(a<=radius<b for a,b in top['H0'])
                    assert b1==sum(a<=radius<b for a,b in top['H1'])
                checked_vr+=1
        fingerprint=rdFingerprintGenerator.GetMorganGenerator(radius=2,fpSize=2048,includeChirality=False)
        items=[]
        for parent,(smiles,s) in chemistry.items():
            m=Chem.MolFromSmiles(smiles);items.append((parent,s,fingerprint.GetFingerprint(m),MurckoScaffold.MurckoScaffoldSmiles(mol=m,includeChirality=False),Chem.MolToSmiles(m,isomericSmiles=False)))
        max_tanimoto=0.
        for i,(_,s,fp,scaffold,constitution) in enumerate(items):
            for _,ss,other,sc,con in items[:i]:
                if s==ss:continue
                v=DataStructs.TanimotoSimilarity(fp,other);assert v<.65 and not(scaffold and scaffold==sc) and constitution!=con
                max_tanimoto=max(max_tanimoto,v)
        minimum_geometry=1e9
        for batch in geometry.values():
            for i,(s,x,_) in enumerate(batch):
                for ss,y,_ in batch[:i]:
                    if s!=ss:
                        d=float(np.sqrt(np.mean((x-y)**2)));assert d>.10;minimum_geometry=min(minimum_geometry,d)
        assert mirror_negative>0
        report.update(all_recomputed_MMFF_energy_max_error=max_energy,all_recomputed_MMFF_force_max_error=max_force,
            all_geometry_graph_stereochemistry=True,mirror_negative_controls=mirror_negative,
            independent_VR_rank_checks=checked_vr*3,cross_split_max_Morgan_Tanimoto=max_tanimoto,
            cross_split_min_heavy_distance_descriptor_angstrom=minimum_geometry if minimum_geometry<1e9 else None)
    return report
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--dataset',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=validate(a.dataset);write_json(a.output,r);print(json.dumps(r,indent=2))
