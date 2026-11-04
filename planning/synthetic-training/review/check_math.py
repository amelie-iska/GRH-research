"""Read-only local CPU review; no Arrow/RDKit install or remote execution."""
from pathlib import Path
import hashlib,json,sys
import numpy as np

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'examples/synthetic_training'))
from common import persistence,connected_groups,assign_components
from materials import bloch,chern,chain,make

def main():
    base=ROOT/'outputs/datasets/synthetic-training-20261104'
    manifests=[]
    for name in ['aster-topological-response-v1','mora-conformer-response-v1']:
        folder=base/name;manifest=json.loads((folder/'manifest.json').read_text())
        for relative,item in manifest['files'].items():
            p=folder/relative
            assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256']
            assert p.stat().st_size==item['bytes']
        manifests.append(dict(dataset=name,checked_files=len(manifest['files'])))
    square=persistence([[0,0],[1,0],[1,1],[0,1]])
    assert square['H0']==[[0.,1.]]*3 and square['H0_essential']==1
    assert np.allclose(square['H1'],[[1,np.sqrt(2)]])
    # Rotation, translation and point-permutation invariance on a nondegenerate cloud.
    rng=np.random.default_rng(20261104);cloud=rng.normal(size=(8,3));Q=np.linalg.qr(rng.normal(size=(3,3)))[0]
    a=persistence(cloud);b=persistence((cloud@Q+np.array([2.,3.,4.]))[rng.permutation(8)])
    for k in ['H0','H1']:assert np.allclose(sorted(a[k]),sorted(b[k]))
    reference=[]
    for mass,expected in [(-3,0),(-1,-1),(1,1),(3,0)]:
        value=chern(bloch('qwz',dict(mass=mass),33));assert abs(value['value']-expected)<1e-12
        reference.append(dict(mass=mass,chern=value['value'],gauge_error=value['gauge_error']))
    # The implemented Fourier/strip conventions agree with the Bloch formulas.
    sx=np.array([[0,1],[1,0]],complex);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1,-1])
    ky=.37;kx=.81
    for family,params in [('qwz',dict(mass=.7)),('rice_mele_pump',dict(dimerization=.4,stagger=.8))]:
        if family=='qwz':
            onsite=np.sin(ky)*sy+(params['mass']+np.cos(ky))*sz;hop=(sz-1j*sx)/2
            target=np.sin(kx)*sx+np.sin(ky)*sy+(params['mass']+np.cos(kx)+np.cos(ky))*sz
        else:
            aa=1+params['dimerization']*np.cos(ky);bb=1-params['dimerization']*np.cos(ky)
            onsite=aa*sx+params['stagger']*np.sin(ky)*sz;hop=bb*(sx-1j*sy)/2
            target=(aa+bb*np.cos(kx))*sx+bb*np.sin(kx)*sy+params['stagger']*np.sin(ky)*sz
        assert abs(onsite+hop*np.exp(1j*kx)+hop.conj().T*np.exp(-1j*kx)-target).max()<1e-14
    # Counterexamples retain actual outputs rather than treating them as passes.
    critical=[]
    for mass in [0.,2.]:
        aa,bb=[chern(bloch('qwz',dict(mass=mass),n)) for n in [17,33]]
        guard=aa['value'] is not None and bb['value'] is not None and abs(aa['value']-bb['value'])<1e-8 and bb['gap']>.08
        critical.append(dict(mass=mass,mesh17=aa,mesh33=bb,initial_generator_accepts_as_gapped=guard,true_bulk_gap=0.))
        assert guard
    M=chain('kitaev',dict(t=1.,delta=.5,mu=.7));n=len(M)//2
    C=np.block([[np.zeros((n,n)),np.eye(n)],[np.eye(n),np.zeros((n,n))]])
    base_res=float(abs(C@M.conj()@C+M).max());assert base_res<1e-12
    M[0,0]+=.15;M[-1,-1]-=.1
    defect_res=float(abs(C@M.conj()@C+M).max());assert defect_res>.1
    # Connectivity is transitive and split assignment never breaks a component.
    cc,edges=connected_groups([0,1,2,9,10,20],lambda a,b:'near' if abs(a-b)<=1 else None)
    assert cc[0]==cc[1]==cc[2] and cc[3]==cc[4]
    rows=[dict(group_id=str(i),family='ssh',payload_json=json.dumps(dict(targets=dict(topology=dict(winding=i%2))))) for i in range(6)]
    allocation=assign_components(rows,{str(i):str(cc[i]) for i in range(6)})
    for i,j,_ in edges:assert rows[i]['split']==rows[j]['split']
    # Regression: revised generator must null actual critical and small-gap QWZ cases.
    class FixedMass:
        def __init__(self,mass):self.mass=mass;self.rng=np.random.default_rng(20261104)
        def uniform(self,low,high,size=None):
            return self.mass if size is None else self.rng.uniform(low,high,size)
    revised=[]
    for mass in [0.,2.,.03269341357763622,.03026983176640119]:
        generated=make(0,'qwz',FixedMass(mass))
        for r in generated:
            top=json.loads(r['target_json'])['topology']
            assert top['chern'] is None and top['gap']<=.08
        revised.append(dict(mass=mass,descendants_checked=len(generated),chern=None))
    revised_kitaev=[]
    for r in make(0,'kitaev',np.random.default_rng(20261104)):
        p=json.loads(r['payload_json']);matrix=np.array(p['hamiltonian_real'])+1j*np.array(p['hamiltonian_imag'])
        n=len(matrix)//2;exchange=np.r_[np.arange(n,2*n),np.arange(n)]
        error=float(abs(matrix.conj()[exchange][:,exchange]+matrix).max());assert error<1e-12
        revised_kitaev.append(dict(id=r['record_id'],PHS_residual=error))
    # Saved biomolecule sample topology is independently reproducible without RDKit.
    bio=json.loads((base/'mora-conformer-response-v1/examples.json').read_text())
    for item in bio:
        c=item['conditions'];x=np.array(c['coordinates_angstrom']);z=np.array(c['atomic_numbers'])
        actual=persistence(x[z>1]);saved=item['targets']['heavy_atom_VR']
        for k in ['H0','H1']:assert np.allclose(sorted(actual[k]),sorted(saved[k]))
        assert actual['H0_essential']==saved['H0_essential']
    result=dict(completed=True,manifest_integrity=manifests,persistence_square=square,
        persistence_rigid_permutation_invariance=True,saved_biomolecule_example_topology=True,
        regular_qwz_reference_cases=reference,strip_bloch_conventions_agree=True,
        connected_component_toy_allocation=allocation,
        counterexamples=dict(gapless_qwz_accepted_by_initial_guard=critical,
        kitaev_base_PHS_residual=base_res,kitaev_initial_boundary_defect_PHS_residual=defect_res),
        revised_generator_regressions=dict(qwz_null_cases=revised,kitaev_variants=revised_kitaev),
        limitation='No local pyarrow or RDKit: all-row Parquet inspection and MMFF rerun not performed; no dependency or remote execution')
    out=ROOT/'outputs/checks/2026-11-04-synthetic-training/review';out.mkdir(parents=True,exist_ok=True)
    (out/'math-review.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
