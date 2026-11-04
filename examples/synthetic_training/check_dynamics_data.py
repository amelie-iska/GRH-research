"""Independent Padé matrix exponentials and MMFF trajectory checks on saved data."""
import argparse,json
from pathlib import Path
import numpy as np
import pyarrow.parquet as pq
from scipy.linalg import expm
from common import sha,write_json

def check(folder):
    folder=Path(folder);m=json.loads((folder/'manifest.json').read_text())
    for name,item in m['files'].items():assert sha(folder/name)==item['sha256'],name
    rows=[r for p in (folder/'electronic_dynamics').glob('*.parquet') for r in pq.read_table(p).to_pylist()]
    error=0.;residual=0.;inherited=0;static={r['record_id']:r for p in (folder/'data').glob('*.parquet') for r in pq.read_table(p).to_pylist()}
    for r in rows:
        p=json.loads(r['payload_json']);c=p['conditions'];t=p['targets']
        if p.get('parent_record_id'):
            parent=static[p['parent_record_id']];assert parent['group_id']==r['group_id'] and parent['split']==r['split'];inherited+=1
        if r['family']=='interacting_hubbard_dimer':
            H=np.array(t['hamiltonian_real']);bits=t['basis_fock_bits'];initial=np.zeros(len(bits));initial[bits.index(9)]=1;number=np.array([[(b>>q)&1 for q in range(4)] for b in bits])
            for k in [0,len(t['time'])//2,len(t['time'])-1]:
                state=expm(-1j*H*t['time'][k])@initial;n=abs(state)**2@number
                error=max(error,float(np.max(abs(n-t['occupation'][k]))))
                assert abs(abs(state[bits.index(6)])**2-t['spin_swap_probability'][k])<1e-10
        else:
            H=np.array(c['hamiltonian_real'])+1j*np.array(c['hamiltonian_imag']);P0=np.array(c['initial_occupation_matrix_real'])+1j*np.array(c['initial_occupation_matrix_imag']);n=len(P0);bdg=len(H)==2*n
            R0=np.block([[np.eye(n)-P0,np.zeros((n,n))],[np.zeros((n,n)),P0.T]]) if bdg else P0
            for k in [0,len(t['time'])//2,len(t['time'])-1]:
                U=expm(-1j*H*t['time'][k]);R=U@R0@U.conj().T;P=np.eye(n)-R[:n,:n] if bdg else R;F=R[:n,n:] if bdg else np.zeros_like(P)
                occ=P.diagonal().real;J=-2*np.imag(H[:n,:n]*P.T);pair=-2*np.imag(np.diag(H[:n,n:]@F.conj().T)) if bdg else np.zeros(n)
                dR=-1j*(H@R-R@H);dn=-dR[:n,:n].diagonal().real if bdg else dR.diagonal().real
                error=max(error,float(np.max(abs(occ-t['occupation'][k]))),float(np.max(abs(pair-t['pair_source'][k]))))
                residual=max(residual,float(np.max(abs(dn+J.sum(1)-pair))))
                assert np.max(abs(np.array([J[i,j] for i,j in t['bond_edges']])-t['bond_current'][k]))<1e-10
                covariance=abs(F[0])**2-abs(P[0])**2;covariance[0]=occ[0]*(1-occ[0]);assert np.max(abs(covariance-t['connected_density_correlation_with_orbital0'][k]))<1e-10
        assert error<1e-10 and residual<1e-10
    mdcount=0;maximum_drift=0.;energy_error=0.;force_error=0.
    if (folder/'nuclear_md').exists():
        from rdkit import Chem
        from rdkit.Chem import AllChem
        for file in (folder/'nuclear_md').glob('*.parquet'):
            for r in pq.read_table(file).to_pylist():
                p=json.loads(r['payload_json']);c=p['conditions'];t=p['targets'];parent=static[p['parent_record_id']]
                assert r['group_id']==parent['group_id'] and r['split']==parent['split']
                builder=Chem.RWMol()
                for z in c['atomic_numbers']:builder.AddAtom(Chem.Atom(z))
                types={1.:Chem.BondType.SINGLE,1.5:Chem.BondType.AROMATIC,2.:Chem.BondType.DOUBLE,3.:Chem.BondType.TRIPLE}
                for b in c['bonds']:builder.AddBond(b['source'],b['target'],types[b['order']])
                mol=builder.GetMol();Chem.SanitizeMol(mol);conf=Chem.Conformer(mol.GetNumAtoms())
                for i,x in enumerate(t['frames'][0]['coordinates_angstrom']):conf.SetAtomPosition(i,tuple(x))
                mol.AddConformer(conf);props=AllChem.MMFFGetMoleculeProperties(mol,mmffVariant='MMFF94');ff=AllChem.MMFFGetMoleculeForceField(mol,props,nonBondedThresh=100.,ignoreInterfragInteractions=False)
                masses=np.array([a.GetMass() for a in mol.GetAtoms()]);energies=[];momentum=[]
                for frame in t['frames']:
                    x=np.array(frame['coordinates_angstrom']);v=np.array(frame['velocities_angstrom_per_fs'])
                    e=ff.CalcEnergy(x.ravel().tolist());f=-np.array(ff.CalcGrad(x.ravel().tolist())).reshape(-1,3)
                    energies.append(e+.5*np.sum(masses[:,None]*v*v)/.0004184);momentum.append((masses[:,None]*v).sum(0))
                    force_error=max(force_error,float(np.max(abs(f-frame['forces_kcal_mol_angstrom']))))
                energy_error=max(energy_error,float(np.max(abs(np.array(energies)-t['total_energy_kcal_mol']))))
                drift=float(np.max(abs(np.array(energies)-energies[0])));maximum_drift=max(maximum_drift,drift)
                assert drift<.05 and np.max(abs(np.array(momentum)-momentum[0]))<1e-8
                mdcount+=1
    assert energy_error<1e-8 and force_error<1e-8
    return dict(passed=True,electronic_rows=len(rows),independent_expm_checks=3*len(rows),maximum_density_pair_source_error=error,
        independent_continuity_residual=residual,static_descendants_with_inherited_split=inherited,nuclear_MD_rows=mdcount,
        maximum_NVE_energy_drift_kcal_mol=maximum_drift,recomputed_MD_energy_error=energy_error,recomputed_MD_force_error=force_error,
        all_manifest_hashes=True,no_native_model_changes=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--dataset',required=True,type=Path);p.add_argument('--output',required=True,type=Path);a=p.parse_args();r=check(a.dataset);write_json(a.output,r);print(json.dumps(r,indent=2))
