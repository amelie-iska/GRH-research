"""Export actual private-dataset examples, checked circuits and graph wavelets."""
import argparse,json,hashlib,shutil
from pathlib import Path
import numpy as np
import pyarrow.parquet as pq
from scipy.linalg import expm
from common import write_json,canonical,sha

def givens_circuit(H,time):
    e,v=np.linalg.eigh(H);U=(v*np.exp(-1j*e*time))@v.conj().T;A=U.copy();rotations=[];n=len(U)
    for col in range(n):
        for i in range(n-1,col,-1):
            a,b=A[i-1,col],A[i,col];r=np.hypot(abs(a),abs(b))
            if abs(b)<1e-13:continue
            G=np.array([[a.conjugate(),b.conjugate()],[-b,a]])/r;A[[i-1,i]]=G@A[[i-1,i]];rotations.append((i-1,i,G))
    diagonal=np.diag(A);actual=np.diag(diagonal);gates=[dict(kind='orbital phase',wires=[i],angle=float(np.angle(z))) for i,z in enumerate(diagonal)]
    for i,j,G in reversed(rotations):
        B=G.conj().T;actual[[i,j]]=B@actual[[i,j]]
        # Exact two-mode second quantization in |00>,|01>,|10>,|11>.
        F=np.zeros((4,4),complex);F[0,0]=1;F[1:3,1:3]=B[::-1,::-1];F[3,3]=np.linalg.det(B)
        assert np.max(abs(F.conj().T@F-np.eye(4)))<1e-12
        gates.append(dict(kind='adjacent fermionic Givens',wires=[i,j],matrix_real=B.real.tolist(),matrix_imag=B.imag.tolist()))
    error=float(np.max(abs(actual-U)));assert error<1e-11
    return dict(kind='Executed numerical U(N) adjacent-Givens compilation',time=time,modes=n,qubits=n,gates=gates,
        recomposition_max_error=error,scope='Number-conserving free fermions; exact two-mode matchgates verified. No hardware execution or many-body interacting compiler inferred.')

def hubbard_circuit(ratio,t,time):
    c=[]
    for q in range(4):
        a=np.zeros((16,16),complex)
        for b in range(16):
            if b>>q&1:a[b^(1<<q),b]=(-1)**((b&((1<<q)-1)).bit_count())
        c.append(a)
    number=[a.conj().T@a for a in c];terms=[-t*(c[0].conj().T@c[2]+c[2].conj().T@c[0]),-t*(c[1].conj().T@c[3]+c[3].conj().T@c[1]),ratio*t*number[0]@number[1],ratio*t*number[2]@number[3]]
    H=sum(terms);exact=expm(-1j*H*time);errors=[]
    for steps in [16,64,256]:
        step=np.eye(16,dtype=complex)
        for term in terms:step=expm(-1j*term*time/steps)@step
        approximate=np.linalg.matrix_power(step,steps);errors.append(dict(steps=steps,max_unitary_error=float(np.max(abs(approximate-exact)))))
    assert errors[-1]['max_unitary_error']<errors[0]['max_unitary_error']
    return dict(kind='Explicit4qubit Jordan-Wigner Hubbard circuit, first-order product formula',time=time,qubits=4,modes=4,
        gates=[dict(kind='fermion hopping with JW parity',wires=[0,2],parity=[1]),dict(kind='fermion hopping with JW parity',wires=[1,3],parity=[2]),dict(kind='onsite controlled phase',wires=[0,1],angle=-ratio*t*time/64),dict(kind='onsite controlled phase',wires=[2,3],angle=-ratio*t*time/64)],
        repeated_steps=64,convergence=errors,scope='Dense16state verification of actual Jordan-Wigner terms. Product formula is approximate; no hardware claim.')

def wavelet(n,edges):
    adjacency=np.zeros((n,n))
    for a,b in edges:adjacency[a,b]=adjacency[b,a]=1
    L=np.diag(adjacency.sum(1))-adjacency;e,v=np.linalg.eigh(L);assert e.min()>-1e-10
    return dict(eigenvalues=np.maximum(e,0).tolist(),eigenvectors=v.tolist(),formula='s L exp(-s L) delta_center; signed graph heat wavelet, not electron probability')

def rows(folder,sub='data'):
    return [r for p in sorted((folder/sub).glob('*.parquet')) for r in pq.read_table(p).to_pylist()]

def export(material,bio,out,asset_prefix='/data/synthetic-training/large-v2'):
    out=Path(out);out.mkdir(parents=True,exist_ok=True);(out/'structures').mkdir(exist_ok=True);cases=[]
    for folder in [material,bio]:
        isbio=folder==bio;static={r['record_id']:json.loads(r['payload_json']) for r in rows(folder)}
        all_dynamic=rows(folder,'electronic_dynamics');mdrows=rows(folder,'nuclear_md') if (folder/'nuclear_md').exists() else []
        selected=[]
        if not isbio:
            for family in sorted({r['family'] for r in all_dynamic}):
                candidates=[r for r in all_dynamic if r['family']==family]
                selected.append(candidates[len(candidates)//2])
        else:
            selected=mdrows[:3]+mdrows[-3:]
        for r in selected:
            p=json.loads(r['payload_json']);parent=p.get('parent_record_id');original=static.get(parent)
            if isbio:
                c=original['conditions'];coords=c['coordinates_angstrom'];z=c['atomic_numbers'];edges=[(b['source'],b['target']) for b in c['bonds']]
                frames=p['targets']['frames'];electronic_rows=[d for d in all_dynamic if json.loads(d['payload_json']).get('parent_record_id')==parent]
                electronic_data=json.loads(electronic_rows[0]['payload_json']) if electronic_rows else None
                circuit=None
                if electronic_data:
                    cc=electronic_data['conditions'];H=np.array(cc['hamiltonian_real'])+1j*np.array(cc['hamiltonian_imag']);circuit=givens_circuit(H,1.2)
                structures=write_structures(out/'structures',parent,original,frames,asset_prefix)
                case=dict(id=r['record_id'],title='Molecular MD / '+original['family']+' / '+parent,domain='molecule',positions=coords,atomic_numbers=z,edges=edges,
                    frames=frames,time=[f['time_fs'] for f in frames],time_units='fs',partial_charges=original['targets']['forcefield_partial_charges_e'],
                    electronic=electronic_data,circuit=circuit,structures=structures,smiles=original['canonical_smiles'],group=r['group_id'],split=r['split'],
                    native_data='Actual MMFF94 coordinates/forces. Electronic overlay is a separate uncalibrated dimensionless pi graph; its time does not equal the MD femtosecond axis.',
                    energy=p['targets']['total_energy_kcal_mol'],energy_drift=p['targets']['max_energy_drift_kcal_mol'])
            else:
                t=p['targets'];n=len(t['occupation'][0]);z=[0]*n
                if r['family']=='interacting_hubbard_dimer':
                    coords=[[0,.4,0],[0,-.4,0],[2,.4,0],[2,-.4,0]];edges=t['bond_edges'];c=p['conditions'];circuit=hubbard_circuit(c['U_over_t'],c['t'],.7)
                else:
                    coords=[[i*.7, .25*(-1)**i, .4*np.sin(i*.45)] for i in range(n)];edges=t['bond_edges'];c=p['conditions'];H=np.array(c['hamiltonian_real'])+1j*np.array(c['hamiltonian_imag'])
                    circuit=dict(kind='Exact Nambu evolution; Bogoliubov gate compiler remains separate',modes=n,qubits=n,gates=[],scope='Do not use number-conserving Givens gates to claim a paired BdG compiler.') if r['family']=='kitaev' else givens_circuit(H,1.2)
                case=dict(id=r['record_id'],title=r['family'].replace('_',' ')+' / '+r['split'],domain='effective material',positions=coords,atomic_numbers=z,edges=edges,
                    time=t['time'],time_units='dimensionless hbar=1',frames=[dict(coordinates_angstrom=coords) for _ in t['time']],electronic=p,circuit=circuit,
                    group=r['group_id'],split=r['split'],native_data='Schematic finite model-site coordinates, not atomic structure or a crystal/CIF. Charge overlay is discrete orbital occupation, not real-space electron density.')
            case['wavelet']=wavelet(len(coords),edges);cases.append(case)
        anchors=rows(folder,'source_anchors') if (folder/'source_anchors').exists() else []
        chosen=[]
        if not isbio:
            candidates=[r for r in anchors if json.loads(r['condition_json']).get('strain')==0 and json.loads(r['condition_json']).get('defect')=='none']
            if candidates:chosen=[max(candidates,key=lambda r:len(json.loads(r['condition_json'])['atomic_numbers']))]
        else:
            for source_id in ['1L2Y','1AZU','1HRW']:
                selected=[r for r in anchors if json.loads(r['payload_json'])['source'].get('requested_record_id')==source_id]
                if selected:chosen.append(selected[1])
        for r in chosen:
            p=json.loads(r['payload_json']);c=p['conditions'];s=p['source'];t=p['targets']['electronic_dynamics'];coords=c['coordinates_angstrom'];n=len(coords)
            H=np.array(c['hamiltonian_real'])+1j*np.array(c['hamiltonian_imag']);cc={**c,'initial_occupation_matrix_real':t['initial_occupation_matrix_real'],'initial_occupation_matrix_imag':t['initial_occupation_matrix_imag']}
            structures={}
            if c.get('residue_subsystem'):
                source_id=s['requested_record_id'];name=source_id+'.pdb';shutil.copyfile(folder/'sources'/'PDB'/name,out/'structures'/name);structures['pdb']=asset_prefix+'/structures/'+name
                z=[0]*n;note=f"Residue CA contact subsystem of {source_id}, actual HEADER {s['record_id']}. Source atom/residue mapping retained; downloaded PDB is the complete original source, not a simulated all-atom trajectory. Uncalibrated spinless dynamics, no CISS/rate claim."
            else:
                z=c['atomic_numbers'];name=r['record_id']+'.cif';cell=np.array(c['lattice_angstrom']);length=np.linalg.norm(cell,axis=1)
                angles=[np.degrees(np.arccos(np.clip(np.dot(cell[i],cell[j])/length[i]/length[j],-1,1))) for i,j in [(1,2),(0,2),(0,1)]]
                content=['data_'+r['record_id']]+[f'_cell_length_{a} {v:.10f}' for a,v in zip('abc',length)]+[f'_cell_angle_{a} {v:.10f}' for a,v in zip(['alpha','beta','gamma'],angles)]+["_symmetry_space_group_name_H-M 'P 1'",'loop_','_atom_site_label','_atom_site_type_symbol','_atom_site_fract_x','_atom_site_fract_y','_atom_site_fract_z']
                content +=[f'{symbol}{i+1} {symbol} '+ ' '.join(f'{q:.10f}' for q in x) for i,(symbol,x) in enumerate(zip(c['species'],c['fractional_coordinates']))]
                (out/'structures'/name).write_text('\n'.join(content)+'\n');structures['cif']=asset_prefix+'/structures/'+name
                note='Source-backed MP20 crystal geometry and explicit periodic-neighbor finite compression. CIF is the recorded geometry; dimensionless orbital dynamics is synthetic, not a DFT/Wannier result.'
            edges=t['bond_edges'];cases.append(dict(id=r['record_id'],title=('PDB residue transfer / ' if c.get('residue_subsystem') else 'MP20 crystal response / ')+s['record_id'],domain='source-backed effective system',positions=coords,atomic_numbers=z,edges=edges,
                time=t['time'],time_units='dimensionless hbar=1',frames=[dict(coordinates_angstrom=coords) for _ in t['time']],electronic=dict(conditions=cc,targets=t),circuit=givens_circuit(H,1.2),
                group=r['group_id'],split=r['split'],native_data=note,structures=structures,wavelet=wavelet(n,edges),source=s,origin_class=r['origin_class']))
    summaries=[]
    for folder in [material,bio]:
        summaries.append(dict(name=folder.name,manifest_sha256=sha(folder/'manifest.json'),quality=json.loads((folder/'quality.json').read_text()),
            dynamics=json.loads((folder/'dynamics-quality.json').read_text()),split_audit=json.loads((folder/'split-audit.json').read_text())))
    # Keep compact audit values in the browser; full assignment evidence stays in HF.
    for s in summaries:
        audit=s['split_audit'];s['split_audit']={k:v for k,v in audit.items() if k not in ['parent_audit','final_assignments','molecules','similarity_edges','added_geometry_edges']}
    write_json(out/'examples.json',dict(cases=cases,datasets=summaries,CPK=dict(H='#FFFFFF',C='#909090',N='#3050F8',O='#FF0D0D',S='#FFFF30'),
        field_scope='Gaussian splats are declared illustrative kernels on site values; not ab-initio volumetric density. Graph wavelets are signed Laplacian fields.'))
    print(dict(cases=len(cases),molecular=sum(c['domain']=='molecule' for c in cases),output=str(out)))

def write_structures(folder,identity,p,frames,asset_prefix):
    from rdkit import Chem
    c=p['conditions'];z=c['atomic_numbers'];table=Chem.GetPeriodicTable();x=frames[0]['coordinates_angstrom']
    xyz='\n'.join([str(len(z)),identity+'; angstrom; computed MMFF94']+[f'{table.GetElementSymbol(a)} {q[0]:.10f} {q[1]:.10f} {q[2]:.10f}' for a,q in zip(z,x)])+'\n'
    (folder/(identity+'.xyz')).write_text(xyz)
    builder=Chem.RWMol()
    for a in z:builder.AddAtom(Chem.Atom(a))
    types={1.:Chem.BondType.SINGLE,1.5:Chem.BondType.AROMATIC,2.:Chem.BondType.DOUBLE,3.:Chem.BondType.TRIPLE}
    for b in c['bonds']:builder.AddBond(b['source'],b['target'],types[b['order']])
    m=builder.GetMol();Chem.SanitizeMol(m);conf=Chem.Conformer(len(z))
    for i,q in enumerate(x):conf.SetAtomPosition(i,tuple(q))
    m.AddConformer(conf);Chem.AssignAtomChiralTagsFromStructure(m,0,True);m.SetProp('_Name',identity);m.SetProp('canonical_smiles',p['canonical_smiles']);m.SetProp('evidence','computed_MMFF94')
    path=folder/(identity+'.sdf');writer=Chem.SDWriter(str(path));writer.write(m);writer.close()
    check=Chem.SDMolSupplier(str(path),removeHs=False)[0];assert check is not None and check.GetNumAtoms()==len(z)
    return dict(xyz=asset_prefix+'/structures/'+identity+'.xyz',sdf=asset_prefix+'/structures/'+identity+'.sdf')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--materials',type=Path,required=True);p.add_argument('--bio',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--asset-prefix',default='/data/synthetic-training/large-v2');a=p.parse_args();export(a.materials,a.bio,a.output,a.asset_prefix)
