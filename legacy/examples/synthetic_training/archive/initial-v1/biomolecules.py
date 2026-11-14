"""Additional computed molecular conformer/force data. Uses existing RDKit only."""
import argparse,json,math
from pathlib import Path
import numpy as np
from rdkit import Chem,DataStructs,rdBase
from rdkit.Chem import AllChem,rdFingerprintGenerator
from rdkit.Chem.Scaffolds import MurckoScaffold
from common import SEED,fresh,finish,row,write_json,persistence,connected_groups,assign_components

def library():
    # Designed neutral amides; identities are explicit graphs, not measured drugs.
    rings=['c1ccccc1','c1ccncc1','c1ccoc1','c1ccsc1','c1ccc2ccccc2c1','C1CCCCC1','C1CCC1','C1CC1']
    tails=['C','CC','CCC','CCO','CCN','C1CC1','C1CCC1','C1CCCCC1','c1ccccc1','Cc1ccccc1']
    entries=[('designed_amide',a+'C(=O)N'+b) for a in rings for b in tails]
    entries +=[('amino_acid',s) for s in ['NCC(=O)O','N[C@@H](C)C(=O)O','N[C@@H](CO)C(=O)O',
        'N[C@@H](C(C)C)C(=O)O','N[C@@H](CC(=O)O)C(=O)O','N[C@@H](CCCCN)C(=O)O',
        'N[C@@H](Cc1ccccc1)C(=O)O','N1CCC[C@H]1C(=O)O','N[C@@H](CS)C(=O)O']]
    entries +=[('small_biomolecular_building_block',s) for s in ['OCCO','OCC(O)CO','CC(=O)O','NCCO',
        'O=C1NC=CC(=O)N1','NC1=NC=CC(=O)N1','CC(=O)NCC(=O)O','C1CCSS1']]
    found={}
    for family,smiles in entries:
        m=Chem.MolFromSmiles(smiles)
        if m is None:raise ValueError('Designed chemical graph failed sanitization')
        key=Chem.MolToSmiles(m,isomericSmiles=True);found.setdefault(key,(family,m))
    return [(k,*found[k]) for k in sorted(found)]

def chirality_ok(m,reference,position):
    for atom in m.GetAtoms():
        if atom.GetChiralTag()==Chem.ChiralType.CHI_UNSPECIFIED:continue
        ns=[a.GetIdx() for a in atom.GetNeighbors()]
        if len(ns)!=4:continue
        a=np.linalg.det(reference[ns[:3]]-reference[ns[3]])
        b=np.linalg.det(position[ns[:3]]-position[ns[3]])
        if a*b<=0:return False
    return True

def generate(out,conformers):
    out=fresh(out);rng=np.random.default_rng(SEED);rows=[];failures=[];molecules=[];max_fd=0.;max_rotation=0.
    for index,(smiles,family,heavy) in enumerate(library()):
        parent=f'molecule-{index:04d}';mol=Chem.AddHs(heavy)
        if not AllChem.MMFFHasAllMoleculeParams(mol):failures.append(dict(parent=parent,stage='unsupported_MMFF94',smiles=smiles));continue
        prm=AllChem.ETKDGv3();prm.randomSeed=SEED+index;prm.numThreads=1;prm.pruneRmsThresh=.2;prm.enforceChirality=True
        cids=list(AllChem.EmbedMultipleConfs(mol,numConfs=conformers,params=prm))
        if not cids:failures.append(dict(parent=parent,stage='embedding_failed',smiles=smiles));continue
        props=AllChem.MMFFGetMoleculeProperties(mol,mmffVariant='MMFF94')
        charges=[float(props.GetMMFFPartialCharge(i)) for i in range(mol.GetNumAtoms())]
        assert abs(sum(charges)-Chem.GetFormalCharge(mol))<1e-6
        molecule_info=dict(parent=parent,smiles=smiles,family=family,heavy=heavy)
        molecules.append(molecule_info)
        bonds=[dict(source=b.GetBeginAtomIdx(),target=b.GetEndAtomIdx(),order=b.GetBondTypeAsDouble(),aromatic=b.GetIsAromatic()) for b in mol.GetBonds()]
        z=[a.GetAtomicNum() for a in mol.GetAtoms()];heavy_ids=[i for i,n in enumerate(z) if n>1]
        for cid in cids:
            ff=AllChem.MMFFGetMoleculeForceField(mol,props,confId=cid,nonBondedThresh=100.,ignoreInterfragInteractions=False)
            convergence=ff.Minimize(maxIts=2000,energyTol=1e-9,forceTol=1e-5)
            reference=np.array(mol.GetConformer(cid).GetPositions());base=float(ff.CalcEnergy(reference.ravel().tolist()))
            if convergence!=0:
                failures.append(dict(parent=parent,conformer=cid,stage='minimum_not_converged',energy=base));continue
            for sample,sigma in enumerate([0.,.015,.04,.08]):
                x=reference+rng.normal(0,sigma,reference.shape)
                if not chirality_ok(mol,reference,x):failures.append(dict(parent=parent,conformer=cid,sample=sample,stage='chirality_changed'));continue
                energy=float(ff.CalcEnergy(x.ravel().tolist()));grad=np.array(ff.CalcGrad(x.ravel().tolist())).reshape(-1,3)
                if not np.isfinite(energy) or not np.isfinite(grad).all() or energy-base>100:
                    failures.append(dict(parent=parent,conformer=cid,sample=sample,stage='energy_or_nonfinite_rejected'));continue
                # Independent central energy difference, three seeded coordinates.
                error=0.
                for k in rng.choice(x.size,3,replace=False):
                    h=1e-5;a=x.ravel().copy();b=a.copy();a[k]+=h;b[k]-=h
                    fd=(ff.CalcEnergy(a.tolist())-ff.CalcEnergy(b.tolist()))/(2*h)
                    error=max(error,abs(fd-grad.ravel()[k]))
                assert error<.003,error;max_fd=max(max_fd,error)
                if sample==0:
                    Q=np.linalg.qr(rng.normal(size=(3,3)))[0];Q[:,0]*=np.linalg.det(Q)
                    moved=x@Q+np.array([2.,-3.,1.]);e2=ff.CalcEnergy(moved.ravel().tolist());g2=np.array(ff.CalcGrad(moved.ravel().tolist())).reshape(-1,3)
                    err=max(abs(e2-energy),float(np.max(abs(g2-grad@Q))));assert err<1e-6;max_rotation=max(max_rotation,err)
                identity=f'{parent}-c{cid:02d}-p{sample}';top=persistence(x[heavy_ids])
                conditions=dict(atomic_numbers=z,bonds=bonds,coordinates_angstrom=x.tolist(),method='MMFF94',
                    protonation='Explicit neutral/formal-charge graph; not physiological protonation inference',known_chemical_topology=True)
                targets=dict(energy_kcal_per_mol=energy,forces_kcal_per_mol_angstrom=(-grad).tolist(),
                    forcefield_partial_charges_e=charges,heavy_atom_VR=top)
                inverse=dict(conditions=dict(atomic_numbers=z,bonds=bonds,noisy_coordinates_angstrom=x.tolist(),
                    request='Return the recorded local MMFF94 reference basin conformation'),
                    targets=dict(reference_coordinates_angstrom=reference.tolist()),
                    limitation='Basin-paired denoising supervision; not a unique global minimum or equilibrium conformer sample')
                payload=dict(id=identity,canonical_smiles=smiles,family=family,conditions=conditions,targets=targets,
                    inverse_task=inverse,parent=parent,conformer=cid,perturbation_sigma_angstrom=sigma,
                    reference_energy_kcal_per_mol=base,minimum_converged=True,gradient_finite_difference_error=error,
                    provenance=dict(engine='RDKit '+rdBase.rdkitVersion,forcefield='MMFF94',conformer_engine='ETKDGv3',seed=SEED+index,
                        evidence='synthetic_computed; not experimental, ab-initio, affinity, ADMET or biological efficacy'),
                    units=dict(energy='kcal/mol, MMFF94 internal convention, not cross-molecule atomization energy',coordinates='angstrom',forces='kcal/(mol angstrom)'))
                rows.append(row(identity,family,parent,conditions,targets,payload))
    # Conservative parent/constitution/scaffold/fingerprint connected closure.
    generator=rdFingerprintGenerator.GetMorganGenerator(radius=2,fpSize=2048,includeChirality=False)
    for m in molecules:
        m['fp']=generator.GetFingerprint(m['heavy']);m['scaffold']=MurckoScaffold.MurckoScaffoldSmiles(mol=m['heavy'],includeChirality=False)
        m['constitution']=Chem.MolToSmiles(m['heavy'],isomericSmiles=False)
    def similar(a,b):
        if a['constitution']==b['constitution']:return 'same_stereo_agnostic_constitution'
        if a['scaffold'] and a['scaffold']==b['scaffold']:return 'same_nonempty_Murcko_scaffold'
        if DataStructs.TanimotoSimilarity(a['fp'],b['fp'])>=.65:return 'Morgan_radius2_Tanimoto>=0.65'
        return None
    components,edges=connected_groups(molecules,similar)
    mapping={m['parent']:f'bio-component-{components[i]:04d}' for i,m in enumerate(molecules)}
    audit=assign_components(rows,mapping);assign={r['group_id']:r['split'] for r in rows}
    cross_max=0.;nearest=[]
    for i,m in enumerate(molecules):
        group=mapping[m['parent']]
        if group not in assign:continue
        for j in range(i):
            other=molecules[j];og=mapping[other['parent']]
            if og in assign and assign[og]!=assign[group]:cross_max=max(cross_max,DataStructs.TanimotoSimilarity(m['fp'],other['fp']))
    assert cross_max<.65
    write_json(out/'split-audit.json',dict(**audit,cross_split_similarity_edges=0,cross_split_max_Morgan_Tanimoto=cross_max,
        threshold=.65,same_Murcko_scaffold_crossings=0,same_parent_or_stereo_agnostic_constitution_crossings=0,
        molecules=[dict(parent=m['parent'],smiles=m['smiles'],component=mapping[m['parent']],split=assign.get(mapping[m['parent']])) for m in molecules],
        similarity_edges=[dict(a=molecules[i]['parent'],b=molecules[j]['parent'],reason=why) for i,j,why in edges],
        geometry_scope='All conformers, noisy geometries and inverse-task descendants of each molecular identity share a split. RMSD/TM-score protein folds are not claimed; these are small molecules, not protein sequences.',
        limitation='Threshold-relative finite audit, not proof of universal independence or prevention of overfitting'))
    write_json(out/'failures.json',failures)
    report=dict(passed=True,requested_molecules=len(library()),supported_molecules=len(molecules),requested_conformers=conformers,
        emitted_records=len(rows),retained_failure_count=len(failures),RDKit=rdBase.rdkitVersion,forcefield='MMFF94',
        maximum_force_finite_difference_error=max_fd,maximum_rigid_energy_force_error=max_rotation,
        geometric_topology='Complete heavy-atom Euclidean Vietoris-Rips H0/H1, F2 coefficients, all edges/triangles',
        training_claim='Additional candidate synthetic source; no Mora-3 code, data, optimizer or admission changed')
    finish(out,rows,report,'Additional MMFF94 conformer/force and finite geometric-topology corpus for Mora-3')
    print(dict(records=len(rows),output=str(out),components=audit['component_count']))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True,type=Path);p.add_argument('--conformers',type=int,default=8);a=p.parse_args();generate(a.output,a.conformers)
