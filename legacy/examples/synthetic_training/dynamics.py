"""Time-resolved complementary data: fermions/BdG, Hubbard exchange and MMFF MD.

All evolution is finite, explicitly model-labelled and CPU only. Effective pi
occupations are not ab-initio molecular charge densities or MMFF partial charges.
"""
import argparse,json,shutil,math
from collections import defaultdict
from pathlib import Path
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
from common import SEED,fresh,sha,write_json,canonical

def electronic(H,bdg=False):
    H=np.asarray(H,complex);N=len(H)//2 if bdg else len(H);h=H[:N,:N]
    initial=h+np.diag([.7]+[0.]*(N-2)+[-.3]);_,v=np.linalg.eigh(initial);P0=v[:,:N//2]@v[:,:N//2].conj().T
    R0=np.block([[np.eye(N)-P0,np.zeros((N,N))],[np.zeros((N,N)),P0.T]]) if bdg else P0
    e,v=np.linalg.eigh(H);times=np.linspace(0,12,41);edges=[(i,j) for i in range(N) for j in range(i+1,N) if abs(h[i,j])>1e-12]
    density=[];currents=[];correlation=[];source=[];maximum=0.;minocc=1.;maxocc=0.
    for t in times:
        U=(v*np.exp(-1j*e*t))@v.conj().T;R=U@R0@U.conj().T;dR=-1j*(H@R-R@H)
        P=np.eye(N)-R[:N,:N] if bdg else R;F=R[:N,N:] if bdg else np.zeros_like(P)
        n=P.diagonal().real;dn=-dR[:N,:N].diagonal().real if bdg else dR.diagonal().real
        J=-2*np.imag(h*P.T)
        pair=-2*np.imag(np.diag(H[:N,N:]@F.conj().T)) if bdg else np.zeros(N)
        assert np.max(abs(dn+J.sum(1)-pair))<1e-10,'Independent current/pair-source continuity'
        assert np.max(abs(P-P.conj().T))<1e-11 and np.min(n)>-1e-10 and np.max(n)<1+1e-10
        if not bdg:assert np.max(abs(pair))<1e-11 and abs(n.sum()-np.trace(P0).real)<1e-10
        assert np.max(abs(R@R-R))<1e-10
        if bdg:
            assert np.max(abs(F+F.T))<1e-10
            idx=np.r_[np.arange(N,2*N),np.arange(N)];assert np.max(abs(R.conj()[idx][:,idx]+R-np.eye(2*N)))<1e-10
        cov=abs(F[0])**2-abs(P[0])**2;cov[0]=n[0]*(1-n[0])
        density.append(n.tolist());currents.append([float(J[i,j]) for i,j in edges]);correlation.append(cov.tolist());source.append(pair.tolist())
        maximum=max(maximum,float(np.max(abs(dn+J.sum(1)-pair))));minocc=min(minocc,float(n.min()));maxocc=max(maxocc,float(n.max()))
    return dict(time=times.tolist(),occupation=density,bond_edges=edges,bond_current=currents,connected_density_correlation_with_orbital0=correlation,
        pair_source=source,charge_modulation=(-np.array(density)+np.array(density)[0]).tolist(),initial_occupation_matrix_real=P0.real.tolist(),
        initial_occupation_matrix_imag=P0.imag.tolist(),continuity_residual=maximum,occupation_range=[minocc,maxocc],
        convention='i dR/dt=[H,R], hbar=1; J_i->j=-2Im(h_ij P_ji); dn_i/dt=-sum_j J_ij+pair_source_i',
        exchange_scope='Gaussian Wick exchange hole -|P_ij|^2; BdG also includes +|F_ij|^2. This is not an interacting Coulomb exchange-energy calculation.',
        statistics='spinless fermions; BdG mean-field condensate can exchange particles' if bdg else 'spinless fermion Slater determinant')

def hubbard(ratio,t):
    basis=[i for i in range(16) if i.bit_count()==2];lookup={b:i for i,b in enumerate(basis)};H=np.zeros((6,6),complex)
    def hop(bits,dest,src):
        if not(bits>>src&1) or bits>>dest&1:return None
        sign=(-1)**((bits&((1<<src)-1)).bit_count());bits^=1<<src
        sign*=(-1)**((bits&((1<<dest)-1)).bit_count());return bits|(1<<dest),sign
    for j,b in enumerate(basis):
        H[j,j]=ratio*t*((b&3==3)+((b>>2)&3==3))
        for a,c in [(0,2),(2,0),(1,3),(3,1)]:
            result=hop(b,a,c)
            if result is not None:H[lookup[result[0]],j]-=t*result[1]
    energies,v=np.linalg.eigh(H);assert abs(energies[0]-(ratio*t-math.sqrt((ratio*t)**2+16*t*t))/2)<1e-10
    initial=np.zeros(6);initial[lookup[9]]=1.;times=np.linspace(0,30/t,81);density=[];current=[];corr=[];swap=[];residual=0.
    n=np.array([[(b>>i)&1 for i in range(4)] for b in basis]);psi0=v.conj().T@initial
    for time in times:
        psi=v@(np.exp(-1j*energies*time)*psi0);prob=abs(psi)**2;dn=2*np.real(psi.conj()*(-1j*H@psi))@n
        occ=prob@n;assert abs(occ.sum()-2)<1e-11 and abs(dn.sum())<1e-11
        J=np.array([np.vdot(psi,(-1j*(H@np.diag(n[:,s])-np.diag(n[:,s])@H))@psi).real for s in [0,1]])
        residual=max(residual,float(max(abs(dn[:2]+J).max(),abs(dn[2:]-J).max())))
        assert residual<1e-11
        density.append(occ.tolist());current.append(J.tolist());corr.append(((prob*n[:,0])@n-occ[0]*occ).tolist());swap.append(float(prob[lookup[6]]))
    return dict(time=times.tolist(),occupation=density,bond_edges=[(0,2),(1,3)],bond_current=current,
        connected_density_correlation_with_orbital0=corr,pair_source=np.zeros_like(density).tolist(),
        charge_modulation=(-np.array(density)+density[0]).tolist(),spin_swap_probability=swap,
        statistics='Exact interacting two-site spinful Hubbard dimer, N=2 sector; spin-orbital order0up,0down,1up,1down',
        exchange_gap=(math.sqrt((ratio*t)**2+16*t*t)-ratio*t)/2,hamiltonian_real=H.real.tolist(),basis_fock_bits=basis,
        continuity_residual=residual,convention='Dimensionless hbar=1; spin-specific bond current operator=-i[H,n_left_spin]; N=2 exactly')

def pi_matrix(p):
    c=p['conditions'];z=c['atomic_numbers'];x=np.array(c['coordinates_angstrom']);active=set()
    for b in c['bonds']:
        if b['order']>=1.5:active.update([b['source'],b['target']])
    for b in c['bonds']:
        if z[b['source']]==7 and b['target'] in active:active.add(b['source'])
        if z[b['target']]==7 and b['source'] in active:active.add(b['target'])
    active=sorted(active)
    if len(active)<3:return None
    index={a:i for i,a in enumerate(active)};onsite={6:0.,7:-.4,8:-.6,16:-.2}
    if any(z[i] not in onsite for i in active):return None
    H=np.diag([onsite[z[i]] for i in active]).astype(complex)
    for b in c['bonds']:
        i,j=b['source'],b['target']
        if i in index and j in index:H[index[i],index[j]]=H[index[j],index[i]]=-np.exp(-(np.linalg.norm(x[i]-x[j])/1.4-1))
    return H,active

def nuclear_md(p,dt=.1,steps=200,diagnostic=False):
    from rdkit import Chem
    from rdkit.Chem import AllChem
    c=p['conditions'];z=c['atomic_numbers'];builder=Chem.RWMol()
    for a in z:builder.AddAtom(Chem.Atom(a))
    types={1.:Chem.BondType.SINGLE,1.5:Chem.BondType.AROMATIC,2.:Chem.BondType.DOUBLE,3.:Chem.BondType.TRIPLE}
    for b in c['bonds']:builder.AddBond(b['source'],b['target'],types[b['order']])
    m=builder.GetMol();Chem.SanitizeMol(m);conf=Chem.Conformer(len(z));x=np.array(p['inverse_task']['targets']['reference_coordinates_angstrom'])
    for i,point in enumerate(x):conf.SetAtomPosition(i,tuple(point))
    m.AddConformer(conf);props=AllChem.MMFFGetMoleculeProperties(m,mmffVariant='MMFF94');ff=AllChem.MMFFGetMoleculeForceField(m,props,nonBondedThresh=100.,ignoreInterfragInteractions=False)
    mass=np.array([a.GetMass() for a in m.GetAtoms()]);rng=np.random.default_rng(int.from_bytes(__import__('hashlib').sha256(p['parent'].encode()).digest()[:4],'little'))
    factor=.0004184;v=rng.normal(size=x.shape)*np.sqrt(factor*.00198720425864083*300/mass)[:,None];v-=(mass[:,None]*v).sum(0)/mass.sum()
    def force(x):
        # Refresh RDKit's shared distance cache at these exact coordinates before
        # evaluating gradients. A Grad-only time loop reused stale distances.
        position=x.ravel().tolist();ff.CalcEnergy(position)
        return -np.array(ff.CalcGrad(position)).reshape(-1,3)
    f=force(x);frames=[];energies=[];momentum0=(mass[:,None]*v).sum(0);maxmomentum=0.
    for k in range(steps+1):
        if k%4==0:
            energy=float(ff.CalcEnergy(x.ravel().tolist())+.5*np.sum(mass[:,None]*v*v)/factor)
            energies.append(energy);frames.append(dict(time_fs=k*dt,coordinates_angstrom=x.tolist(),velocities_angstrom_per_fs=v.tolist(),forces_kcal_mol_angstrom=f.tolist()))
        if k==steps:break
        vv=v+.5*dt*factor*f/mass[:,None];x=x+dt*vv;f=force(x);v=vv+.5*dt*factor*f/mass[:,None]
        maxmomentum=max(maxmomentum,float(np.max(abs((mass[:,None]*v).sum(0)-momentum0))))
    drift=float(np.max(abs(np.array(energies)-energies[0])))
    if not diagnostic:assert drift<.05 and maxmomentum<1e-8,(p['id'],drift,maxmomentum)
    return dict(frames=frames,total_energy_kcal_mol=energies,max_energy_drift_kcal_mol=drift,momentum_residual=maxmomentum,
        initial_temperature_policy='300K Maxwell velocities, COM translation removed; finite isolated NVE trajectory, no thermostat or equilibrium sampling claim',
        charge_policy='MMFF partial charges remain fixed. Separate pi-model data describe effective orbital charge modulation, not an ab-initio charge trajectory.',
        integrator=f'Velocity Verlet,{dt}fs timestep,{steps}steps,{len(frames)}savedframes; acceleration conversion4.184e-4 A/fs^2 per(kcal/mol/A)/amu')

def augment(source,out):
    source=Path(source);out=fresh(out);old=json.loads((source/'manifest.json').read_text())
    for name,entry in old['files'].items():assert sha(source/name)==entry['sha256']
    for p in source.iterdir():
        if p.is_dir():shutil.copytree(p,out/p.name)
        elif p.name!='manifest.json':shutil.copyfile(p,out/p.name)
    write_json(out/'static-manifest.json',old)
    rows=[r for p in sorted((source/'data').glob('*.parquet')) for r in pq.read_table(p).to_pylist()];bio='condition_atomic_numbers' in rows[0]
    chosen=[];counts=defaultdict(set)
    for r in sorted(rows,key=lambda r:sha_bytes(r['record_id'])):
        p=json.loads(r['payload_json']);key=(r['split'],r['family']);limit=4 if not bio else 3
        if not bio and r['family']=='dessin_classical_rg':continue
        if bio and (p['perturbation_sigma_angstrom']!=0 or pi_matrix(p) is None):continue
        if p['parent'] not in counts[key] and len(counts[key])>=limit:continue
        counts[key].add(p['parent']);chosen.append((r,p))
    data=[];md=[]
    for r,p in chosen:
        if bio:
            H,active=pi_matrix(p);bdg=False
        else:H=np.array(p['hamiltonian_real'])+1j*np.array(p['hamiltonian_imag']);active=list(range(len(H)//2 if r['family']=='kitaev' else len(H)));bdg=r['family']=='kitaev'
        result=electronic(H,bdg);conditions=dict(hamiltonian_real=H.real.tolist(),hamiltonian_imag=H.imag.tolist(),active_atom_or_orbital_indices=active,
            initial_occupation_matrix_real=result['initial_occupation_matrix_real'],initial_occupation_matrix_imag=result['initial_occupation_matrix_imag'],statistics=result['statistics'],units='dimensionless;hbar=1')
        if bio:conditions['pi_model_scope']='Idealized uncalibrated spinless pi-orbital graph Hamiltonian. alpha:C0,N-.4,O-.6,S-.2; bond t=-exp(-(r/1.4A-1)). Not TDDFT, real partial charges, redox or biochemical electron transfer.'
        payload=dict(parent_record_id=r['record_id'],conditions=conditions,targets=result,source_group=r['group_id'],synthetic_computed=True)
        data.append(dynamic_row(r,payload))
        if bio and len([m for m in md if m['split']==r['split']])<4:
            resultmd=nuclear_md(p,dt=.05,steps=400);md.append(dict(record_id=r['record_id']+'-nuclear-md',family=r['family'],group_id=r['group_id'],split=r['split'],payload_json=canonical(dict(parent_record_id=r['record_id'],conditions=p['conditions'],targets=resultmd)),
                time_fs=[f['time_fs'] for f in resultmd['frames']],coordinates_angstrom=[f['coordinates_angstrom'] for f in resultmd['frames']],total_energy_kcal_mol=resultmd['total_energy_kcal_mol']))
    if not bio:
        for ratio in [2,3,4,6,8,10,12,14,16]:
            for scale in [.7,1.]:
                s='train' if ratio<=8 else 'validation' if ratio<=12 else 'test';result=hubbard(ratio,scale)
                r=dict(record_id=f'hubbard-UoverT{ratio}-t{scale}',family='interacting_hubbard_dimer',group_id=f'hubbard-ratio-{ratio}',split=s)
                payload=dict(conditions=dict(U_over_t=ratio,t=scale,filling=2,initial_fock_bits=9,units='dimensionless;hbar=1'),targets=result,
                    grouping='All coupling rescalings share ratio group; validation U/t10,12 and test14,16 are explicit OOD coupling holdouts with minimum ratio separation2')
                data.append(dynamic_row(r,payload))
    export_dynamic(out/'electronic_dynamics',data)
    if md:
        (out/'nuclear_md').mkdir()
        for s in ['train','validation','test']:
            batch=[r for r in md if r['split']==s];assert batch
            pq.write_table(pa.Table.from_pylist(batch),out/'nuclear_md'/f'{s}-00000-of-00001.parquet',compression='zstd')
    report=dict(electronic_rows=len(data),electronic_splits={s:sum(r['split']==s for r in data) for s in ['train','validation','test']},
        nuclear_MD_rows=len(md),all_static_parent_groups_inherited=True,static_data_unchanged=True,CPU_only=True,
        electron_exchange='Wick exchange/pair density correlations plus exact interacting Hubbard spin-swap benchmark for Aster',
        biochemical_scope='MMFF fixed-charge nuclear dynamics and separate idealized pi-orbital dynamics; no ab-initio charge or biological efficacy claim')
    write_json(out/'dynamics-quality.json',report)
    card=(out/'README.md').read_text();configs='''  - split: test
    path: data/test-*.parquet'''
    extra='''
- config_name: electronic_dynamics
  data_files:
  - split: train
    path: electronic_dynamics/train-*.parquet
  - split: validation
    path: electronic_dynamics/validation-*.parquet
  - split: test
    path: electronic_dynamics/test-*.parquet'''
    if md:extra+='''
- config_name: nuclear_md
  data_files:
  - split: train
    path: nuclear_md/train-*.parquet
  - split: validation
    path: nuclear_md/validation-*.parquet
  - split: test
    path: nuclear_md/test-*.parquet'''
    card=card.replace(configs,configs+extra)
    card+='''\n## Time-resolved configurations\n\n`electronic_dynamics` adds occupations, charge modulation, bond currents,\nconnected density correlations and explicit pair sources on finite Hamiltonians.\nNormal Slater dynamics conserves particle number; BdG mean-field dynamics has\na recorded condensate source. The Aster supplement also has an exact interacting\nHubbard dimer exchange/spin-swap benchmark, with coupling-ratio OOD splits.\nThe Mora pi-graph calculations use explicit **uncalibrated dimensionless**\nparameters, not TDDFT or real molecular partial-charge predictions. Its separate\n`nuclear_md` config uses0.05fs MMFF94 velocity Verlet,20fs trajectories, finite\nenergy/momentum checks and fixed charges. No solvent, redox, biological electron\ntransfer, equilibrium or experimental dynamics is asserted. All descendants\ninherit parent groups; Hubbard coupling rescalings have ratio groups.\n'''
    (out/'README.md').write_text(card)
    code=out/'dynamics_source';code.mkdir();shutil.copyfile(__file__,code/'dynamics.py')
    files={str(p.relative_to(out)):{'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(out.rglob('*')) if p.is_file() and p.name!='README.md'}
    write_json(out/'manifest.json',dict(**{k:v for k,v in old.items() if k!='files'},files=files,dynamics_source_sha256=sha(__file__),static_parent_manifest_sha256=sha(source/'manifest.json')))
    print(report)

def sha_bytes(s):return __import__('hashlib').sha256(s.encode()).hexdigest()
def dynamic_row(r,p):
    t=p['targets'];return dict(record_id=r['record_id']+'-electronic',family=r['family'],group_id=r['group_id'],split=r['split'],payload_json=canonical(p),
        time=t['time'],target_occupation=t['occupation'],bond_sources=[a for a,b in t['bond_edges']],bond_targets=[b for a,b in t['bond_edges']],
        target_bond_current=t['bond_current'],target_charge_modulation=t['charge_modulation'],target_pair_source=t['pair_source'],target_connected_correlation=t['connected_density_correlation_with_orbital0'])
def export_dynamic(folder,rows):
    folder.mkdir()
    for s in ['train','validation','test']:
        batch=[r for r in rows if r['split']==s];assert batch,s
        table=pa.Table.from_pylist(batch);target=folder/f'{s}-00000-of-00001.parquet';pq.write_table(table,target,compression='zstd')
        assert pq.read_table(target).to_pylist()==batch
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();augment(a.source,a.output)
