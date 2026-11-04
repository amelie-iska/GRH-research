"""Read-only planned-corpus anchors and public PDB-derived effective systems.

All anchor descendants are TRAIN ONLY. They are not independent validation of
a model that may already have seen the source. New labels are explicitly computed.
"""
import argparse,json,hashlib,urllib.request,math
from pathlib import Path
from collections import Counter
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
from common import SEED,fresh,canonical,sha,write_json
from dynamics import electronic

def make_row(identity,source,conditions,targets,extra):
    payload=dict(id=identity,conditions=conditions,targets=targets,source=source,**extra)
    return dict(record_id=identity,family=extra['system_kind'],group_id=source['parent_group'],split='train',
        origin_class=source['origin_class'],planned_source_dataset=source['dataset'],planned_source_record_id=source['record_id'],
        label_origin='new_computed_effective_model_or_MMFF_response; source structure/identity evidence separate',
        condition_json=canonical(conditions),target_json=canonical(targets),payload_json=canonical(payload))

def aster(out):
    root=Path('/home/iska/Documents/amelie/quantum-mat/holonforge/data/processed/mp20-v2');rows=[];parents=[];rng=np.random.default_rng(SEED)
    with (root/'train.jsonl').open() as file:
        for line in file:
            p=json.loads(line)
            if p['original_split']!='train' or len(p['species'])<3:continue
            if len(parents)>=48:break
            parents.append(p)
    from ase.data import atomic_numbers
    for p in parents:
        frac=np.array(p['frac_coords']);cell=np.array(p['lattice']);z=[atomic_numbers[s] for s in p['species']]
        source=dict(dataset='CDVAE/MaterialsProject MP20 via existing Aster mp20-v2',record_id=p['id'],
            source_reference=p['source'],source_row_sha256=hashlib.sha256(canonical(p).encode()).hexdigest(),
            parent_group='existing-aster:'+p['split_group'],origin_class='planned_source_derived_simulation',
            source_model_partition='train',original_source_partition=p['original_split'],
            evidence='Reused source-computed structure; no inherited DFT energy/band label is a new calculation',
            planned_corpus_status='Present in existing model data/processed/mp20-v2/train.jsonl; model exposure not asserted')
        for strain in [-.025,0.,.025]:
            C=cell@np.diag([1+strain,1-strain/2,1]);xyz=frac@C
            for defect in ['none','last_site_vacancy']:
                ids=list(range(len(z)-(defect!='none')))
                if len(ids)<3:continue
                for field in [0.,.2]:
                    N=len(ids);H=np.diag([.05*(z[i]-np.mean(z)) for i in ids]).astype(complex)
                    for e in p['edges']:
                        i,j=e['source'],e['target']
                        if i>=N or j>=N:continue
                        image=np.array(e['image']);distance=np.linalg.norm((frac[j]+image-frac[i])@C)
                        phase=field*(image[0]+.37*image[1]+.13*image[2]);H[i,j]+=-np.exp(-distance/2)*np.exp(1j*phase)
                    H=(H+H.conj().T)/2
                    conditions=dict(species=[p['species'][i] for i in ids],atomic_numbers=[z[i] for i in ids],coordinates_angstrom=xyz[ids].tolist(),
                        lattice_angstrom=C.tolist(),fractional_coordinates=frac[ids].tolist(),source_atom_indices=ids,strain=strain,defect=defect,
                        model='Explicit one-orbital dimensionless finite periodic-neighbor compression; not DFT/Wannier fit',
                        hamiltonian_real=H.real.tolist(),hamiltonian_imag=H.imag.tolist(),synthetic_link_phase=field)
                    result=electronic(H);identity=f"mp20-anchor-{len(rows):05d}"
                    rows.append(make_row(identity,source,conditions,dict(eigenspectrum=np.linalg.eigvalsh(H).tolist(),electronic_dynamics=result),dict(system_kind='source_crystal_effective_subsystem',
                        variation_origin='source geometry at strain0/no vacancy; strain/vacancy/phase derivatives are new synthetic systems',
                        limit='No actual magnetic field, charge transfer, material phase, formation energy or synthesizability is inferred. Neighbor compression and model symmetrization are explicit.')))
    return rows,dict(native_source_parents=len(parents),source_file_sha256=sha(root/'train.jsonl'),source_path=str(root/'train.jsonl'))

def pubchem(out):
    from rdkit import Chem
    from rdkit.Chem import AllChem
    from biomolecules import graph_stereo_ok,chirality_ok
    root=Path('/home/iska/Documents/amelie/bio/Mora-3/outputs/data-intake/20261101-PubChem-corpus-pilot-v1');rows=[];seen=set();rng=np.random.default_rng(SEED);rejections=Counter();max_fd=0.
    for shard in sorted((root/'shards').glob('*.parquet')):
        for batch in pq.ParquetFile(shard).iter_batches(batch_size=64):
            for r in batch.to_pylist():
                if r['split']!='train' or not r['admitted_for_task'] or r['record_id'] in seen:continue
                raw=json.loads(r['native_payload']);smiles=raw['conditions'].get('native_smiles');mol=Chem.MolFromSmiles(smiles or '')
                if mol is None or not 3<=mol.GetNumHeavyAtoms()<=28 or Chem.GetFormalCharge(mol)!=0 or len(Chem.GetMolFrags(mol))!=1:continue
                if any(label=='?' for _,label in Chem.FindMolChiralCenters(mol,includeUnassigned=True)):continue
                mol=Chem.AddHs(mol)
                if not AllChem.MMFFHasAllMoleculeParams(mol):continue
                prm=AllChem.ETKDGv3();prm.randomSeed=SEED+len(seen);prm.numThreads=1
                if AllChem.EmbedMolecule(mol,prm)!=0:continue
                props=AllChem.MMFFGetMoleculeProperties(mol,mmffVariant='MMFF94');ff=AllChem.MMFFGetMoleculeForceField(mol,props,nonBondedThresh=100.,ignoreInterfragInteractions=False)
                if ff.Minimize(maxIts=2000)!=0:continue
                xyz=np.array(mol.GetConformer().GetPositions());z=[a.GetAtomicNum() for a in mol.GetAtoms()]
                if not graph_stereo_ok(mol,xyz):rejections['reference_stereochemistry']+=1;continue
                seen.add(r['record_id']);base=ff.CalcEnergy(xyz.ravel().tolist())
                source=dict(dataset='sagawa/pubchem-10m-canonicalized in existing Mora-3 corpus pilot',record_id=r['record_id'],revision=r['source_revision'],
                    source_manifest_sha256=r['source_sha256'],native_payload_sha256=r['native_payload_sha256'],source_shard_sha256=sha(shard),
                    parent_group='existing-mora:'+hashlib.sha256(r['group_ids_json'].encode()).hexdigest(),origin_class='planned_source_derived_simulation',source_model_partition='train',
                    source_license='Apache-2.0 dataset grant at pinned HF revision; native corpus receipt retained',
                    planned_corpus_status='Existing source admitted for representation task; no force/geometry training admission or model exposure inferred',
                    source_geometry_available=False,new_geometry_engine='ETKDGv3/MMFF94')
                bonds=[dict(source=b.GetBeginAtomIdx(),target=b.GetEndAtomIdx(),order=b.GetBondTypeAsDouble(),aromatic=b.GetIsAromatic(),stereo=int(b.GetStereo()),stereo_atoms=list(b.GetStereoAtoms())) for b in mol.GetBonds()]
                for sigma in [0.,.02,.05]:
                    x=xyz+rng.normal(0,sigma,xyz.shape);energy=ff.CalcEnergy(x.ravel().tolist());force=-np.array(ff.CalcGrad(x.ravel().tolist())).reshape(-1,3)
                    if not graph_stereo_ok(mol,x) or not chirality_ok(mol,xyz,x):rejections['perturbed_stereochemistry']+=1;continue
                    if not np.isfinite(energy) or not np.isfinite(force).all() or energy-base>100:rejections['energy_or_nonfinite']+=1;continue
                    error=0.
                    for k in rng.choice(x.size,3,replace=False):
                        a=x.ravel().copy();b=a.copy();a[k]+=1e-5;b[k]-=1e-5
                        fd=(ff.CalcEnergy(a.tolist())-ff.CalcEnergy(b.tolist()))/2e-5
                        error=max(error,abs(fd+force.ravel()[k]))
                    assert error<.003;max_fd=max(max_fd,error)
                    conditions=dict(canonical_smiles=Chem.MolToSmiles(Chem.RemoveHs(mol),isomericSmiles=True),atomic_numbers=z,
                        formal_charges=[a.GetFormalCharge() for a in mol.GetAtoms()],isotopes=[a.GetIsotope() for a in mol.GetAtoms()],
                        chiral_tags=[int(a.GetChiralTag()) for a in mol.GetAtoms()],bonds=bonds,coordinates_angstrom=x.tolist(),method='MMFF94',perturbation_sigma_angstrom=sigma,
                        atom_order='Explicit atom/bond arrays retain source graph order; canonical SMILES is identity only')
                    rows.append(make_row(f'pubchem-anchor-{len(rows):05d}',source,conditions,dict(energy_kcal_mol=energy,forces_kcal_mol_angstrom=force.tolist()),dict(evaluation=dict(gradient_finite_difference_error=error),system_kind='planned_molecular_identity_new_conformer',variation_origin='New computed3D conformations/force labels for reused planned source graph; not experimental or quantum-chemical labels')))
                if len(seen)>=32:return rows,dict(pubchem_source_parents=len(seen),existing_manifest_sha256=sha(root/'manifest.json'),rejections=dict(rejections),maximum_force_finite_difference_error=max_fd,all_emitted_geometry_CIP_checked=True)
        if len(seen)>=32:break
    return rows,dict(pubchem_source_parents=len(seen),existing_manifest_sha256=sha(root/'manifest.json'))

def pdb_sources(out):
    ids=['1L2Y','1VII','1HRW','1PPT','1AZU','1CRN','1UBQ','1ENH'];rows=[];sources=[];rng=np.random.default_rng(SEED)
    dest=out/'sources'/'PDB';dest.mkdir(parents=True)
    for identity in ids:
        url=f'https://files.rcsb.org/download/{identity}.pdb';req=urllib.request.Request(url,headers={'User-Agent':'GRH-complementary-physics/1.0'})
        with urllib.request.urlopen(req,timeout=30) as response:
            blob=response.read(2_000_001)
        if len(blob)>2_000_000:raise ValueError('Public PDB file exceeds declared budget')
        (dest/(identity+'.pdb')).write_bytes(blob);lines=blob.decode().splitlines();atoms=[];chain=None
        for line in lines:
            if line.startswith('ENDMDL'):break
            if not line.startswith('ATOM  ') or line[12:16].strip()!='CA' or line[16] not in ' A':continue
            if chain is None:chain=line[21]
            if line[21]!=chain or float(line[54:60] or 0)<=0:continue
            atoms.append(dict(residue=line[17:20].strip(),number=line[22:27].strip(),position=[float(line[30:38]),float(line[38:46]),float(line[46:54])],atom_serial=int(line[6:11])))
        if len(atoms)<4:raise ValueError('PDB source lacks a supported CA subsystem')
        atoms=atoms[:32];original=np.array([a['position'] for a in atoms]);original-=original.mean(0);N=len(atoms)
        header=next((line[62:66].strip().upper() for line in lines if line.startswith('HEADER')),identity)
        actual=header or identity
        source=dict(dataset='wwPDB/RCSB experimental coordinate archive',record_id=actual,requested_record_id=identity,
            archive_status='obsolete; superseded by 1LE0' if identity=='1HRW' else 'current at retrieval',replacement_record_id='1LE0' if identity=='1HRW' else None,
            pdb_HEADER_id=header,doi=f'10.2210/pdb{actual}/pdb',url=url,sha256=hashlib.sha256(blob).hexdigest(),license='CC0-1.0',
            parent_group='PDB:'+identity,origin_class='new_public_structure_anchor_related_to_planned_family',source_model_partition='not_enrolled',
            planned_relation='Related PDB structural family of Mora-3 inventoryINV-038; not a claim of PDBbind membership or imported affinity',
            evidence='Source experimental coordinate model; first deposited model/first CA chain, capped32residue subsystem, explicit atom/residue mapping',
            research_context=['arXiv:2108.09998v1','arXiv:2205.05353v1'],research_limit='Spinless effective transfer only. No measured CISS, spin polarization, redox rate or quantum-biological mechanism imported as a label.')
        sources.append(source)
        for variant in range(24):
            # Native structure plus explicitly synthetic geometric and Hamiltonian perturbations.
            x=original.copy();stretch=[.98,1.,1.02][variant%3];x[:,2]*=stretch
            if variant%8==7:x[:,0]*=-1
            decay=[2.,3.,4.,5.][(variant//3)%4];onsite=[0.,.15][variant//12];dist=np.linalg.norm(x[:,None]-x[None,:],axis=-1)
            H=np.zeros((N,N),complex)
            for i in range(N):
                H[i,i]=onsite*np.cos(i)
                for j in range(i):
                    if dist[i,j]<8.:H[i,j]=H[j,i]=-np.exp(-dist[i,j]/decay)
            conditions=dict(coarse_sites=atoms,coordinates_angstrom=x.tolist(),residue_subsystem=True,source_chain=chain,
                stretch_z=stretch,mirror_x=(variant%8==7),decay_length_angstrom=decay,onsite_amplitude=onsite,
                hamiltonian_real=H.real.tolist(),hamiltonian_imag=H.imag.tolist(),model='Uncalibrated dimensionless one-orbital per CA contact network; source-coordinates anchor only')
            rows.append(make_row(f'pdb-{identity}-variant{variant:03d}',source,conditions,dict(electronic_dynamics=electronic(H)),dict(system_kind='peptide_derived_effective_quantum_transfer',
                variation_origin='New effective Hamiltonian and geometric/mirror counterfactual. NMR model index is not time; source coordinates are not newly measured quantum dynamics.')))
    return rows,dict(PDB_sources=sources,PDB_source_parents=len(sources))

def main(model,out):
    out=fresh(out)
    if model=='aster':records,report=aster(out)
    else:
        records,report=pubchem(out);extra,pdb=pdb_sources(out);records+=extra;report.update(pdb)
    (out/'source_anchors').mkdir();pq.write_table(pa.Table.from_pylist(records),out/'source_anchors'/'train-00000-of-00001.parquet',compression='zstd')
    report.update(records=len(records),origin_counts=dict(Counter(r['origin_class'] for r in records)),all_anchor_descendants_train_only=True,
        source_model_repos_read_only=True,source_native_data_not_rewritten=True,model_admission=False,
        heldout_scope='These anchors are not blind evaluation. Default synthetic test sets still require global existing-corpus exposure checks before model performance claims.')
    write_json(out/'source-anchor-quality.json',report)
    write_json(out/'manifest.json',dict(files={str(p.relative_to(out)):{'sha256':sha(p),'bytes':p.stat().st_size} for p in out.rglob('*') if p.is_file()},source_code_sha256=sha(__file__)))
    print(dict(model=model,records=len(records),output=str(out)))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--model',choices=['aster','mora'],required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();main(a.model,a.output)
