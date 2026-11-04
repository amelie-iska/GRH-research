"""Independent source-anchor physical reconstruction and release-boundary audit."""
import argparse,json
from pathlib import Path
from collections import Counter,defaultdict
import numpy as np
import pyarrow.parquet as pq
from common import sha,write_json

def check(root):
    from rdkit import Chem,DataStructs
    from rdkit.Chem import AllChem,rdFingerprintGenerator
    from rdkit.Chem.Scaffolds import MurckoScaffold
    from biomolecules import graph_stereo_ok
    manifest=json.loads((root/'manifest.json').read_text())
    for name,item in manifest['files'].items():assert sha(root/name)==item['sha256'],name
    records=[r for p in (root/'source_anchors').glob('*.parquet') for r in pq.read_table(p).to_pylist()]
    held=[];geometry=defaultdict(list);gen=rdFingerprintGenerator.GetMorganGenerator(radius=2,fpSize=2048,includeChirality=False)
    def feature(s):
        m=Chem.MolFromSmiles(s)
        return Chem.MolToSmiles(m,isomericSmiles=False),MurckoScaffold.MurckoScaffoldSmiles(mol=m,includeChirality=False),gen.GetFingerprint(m)
    def geom(c):
        z=np.array(c['atomic_numbers']);x=np.array(c['coordinates_angstrom'])[z>1];d=np.linalg.norm(x[:,None]-x[None,:],axis=-1)
        return tuple(sorted(z[z>1].tolist())),np.sort(d[np.triu_indices(len(x),1)])
    for f in (root/'data').glob('*.parquet'):
        for r in pq.read_table(f).to_pylist():
            if r['split']=='train':continue
            p=json.loads(r['payload_json'])
            if 'canonical_smiles' not in p:continue
            held.append(feature(p['canonical_smiles']));sig,d=geom(p['conditions']);geometry[sig].append(d)
    types={1.:Chem.BondType.SINGLE,1.5:Chem.BondType.AROMATIC,2.:Chem.BondType.DOUBLE,3.:Chem.BondType.TRIPLE}
    maxe=0.;maxf=0.;molecular=0;maxsim=0.;mind=float('inf');pdb={}
    for r in records:
        assert r['split']=='train';p=json.loads(r['payload_json']);c=p['conditions'];t=p['targets'];source=p['source']
        assert json.loads(r['condition_json'])==c and json.loads(r['target_json'])==t
        if 'canonical_smiles' in c:
            b=Chem.RWMol()
            for i,z in enumerate(c['atomic_numbers']):
                a=Chem.Atom(int(z));a.SetFormalCharge(c['formal_charges'][i]);a.SetIsotope(c['isotopes'][i]);a.SetChiralTag(Chem.ChiralType.values[c['chiral_tags'][i]]);b.AddAtom(a)
            for bond in c['bonds']:b.AddBond(bond['source'],bond['target'],types[bond['order']])
            m=b.GetMol();Chem.SanitizeMol(m)
            for i,bond in enumerate(c['bonds']):
                bb=m.GetBondWithIdx(i)
                if len(bond['stereo_atoms'])==2:bb.SetStereoAtoms(*bond['stereo_atoms'])
                bb.SetStereo(Chem.BondStereo.values[bond['stereo']])
            assert Chem.MolToSmiles(Chem.RemoveHs(m),isomericSmiles=True)==c['canonical_smiles']
            x=np.array(c['coordinates_angstrom']);assert graph_stereo_ok(m,x)
            conf=Chem.Conformer(m.GetNumAtoms())
            for i,q in enumerate(x):conf.SetAtomPosition(i,tuple(q))
            m.AddConformer(conf);props=AllChem.MMFFGetMoleculeProperties(m,mmffVariant='MMFF94');ff=AllChem.MMFFGetMoleculeForceField(m,props,nonBondedThresh=100.,ignoreInterfragInteractions=False)
            e=abs(ff.CalcEnergy()-t['energy_kcal_mol']);f=np.max(abs(np.array(ff.CalcGrad()).reshape(-1,3)+t['forces_kcal_mol_angstrom']))
            assert e<1e-6 and f<1e-5;maxe=max(maxe,e);maxf=max(maxf,float(f));molecular+=1
            constitution,scaffold,fp=feature(c['canonical_smiles'])
            for hc,hs,hfp in held:
                sim=DataStructs.TanimotoSimilarity(fp,hfp);maxsim=max(maxsim,sim)
                assert constitution!=hc and not(scaffold and scaffold==hs) and sim<.65
            sig,d=geom(c)
            for other in geometry[sig]:
                distance=float(np.sqrt(np.mean((d-other)**2)));mind=min(mind,distance);assert distance>.10
        else:
            H=np.array(c['hamiltonian_real'])+1j*np.array(c['hamiltonian_imag']);assert np.max(abs(H-H.conj().T))<1e-12
            if 'eigenspectrum' in t:assert np.max(abs(np.linalg.eigvalsh(H)-t['eigenspectrum']))<1e-10
            if c.get('residue_subsystem'):
                requested=source['requested_record_id'];path=root/'sources'/'PDB'/(requested+'.pdb');assert sha(path)==source['sha256']
                header=next(line[62:66].strip().upper() for line in path.read_text().splitlines() if line.startswith('HEADER'))
                assert header==source['pdb_HEADER_id']==source['record_id']
                if requested=='1HRW':assert source['replacement_record_id']=='1LE0'
                pdb[requested]=dict(actual_HEADER=header,archive_status=source['archive_status'])
    return dict(passed=True,anchor_rows=len(records),parent_groups=len({r['group_id'] for r in records}),origin_counts=dict(Counter(r['origin_class'] for r in records)),
        molecular_rows_recomputed=molecular,MMFF_energy_max_error=maxe,MMFF_force_max_error=maxf,all_anchor_geometry_stereochemistry=True,
        cross_configuration_max_Morgan=maxsim,cross_configuration_min_geometry= None if not np.isfinite(mind) else mind,
        within_release_threshold_crossings=0,PDB_source_headers=pdb,all_manifest_hashes=True,all_source_anchors_train_only=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--dataset',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();report=check(a.dataset);write_json(a.output,report);print(json.dumps(report,indent=2))
