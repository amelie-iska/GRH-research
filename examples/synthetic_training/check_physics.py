"""Focused independent reference/negative controls; no training or installation."""
import json,math
import numpy as np
from materials import bloch,chern,chain,make
from common import SEED,persistence,connected_groups,assign_components,row

def main():
    # Exact gap closures are intentionally missed by odd BZ meshes.
    for mass in [-2.,0.,2.]:
        exact=2*min(abs(mass+2),abs(mass),abs(mass-2));assert exact==0
        a=chern(bloch('qwz',{'mass':mass},32));assert a['gap']<1e-12
    cs={str(m):chern(bloch('qwz',{'mass':m},64))['value'] for m in [-3.,-1.,1.,3.]}
    assert abs(cs['-3.0'])<1e-10 and abs(cs['3.0'])<1e-10
    assert abs(cs['-1.0'])==1 and abs(cs['1.0'])==1 and cs['-1.0']*cs['1.0']<0
    # Independent d-vector degree integral confirms the FHS orientation.
    k=np.arange(512)*2*np.pi/512;x,y=np.meshgrid(k,k,indexing='ij');m=-1.
    d=np.stack([np.sin(x),np.sin(y),m+np.cos(x)+np.cos(y)],-1)
    dx=np.stack([np.cos(x),0*x,-np.sin(x)],-1);dy=np.stack([0*y,np.cos(y),-np.sin(y)],-1)
    degree=float((np.sum(d*np.cross(dx,dy),-1)/np.linalg.norm(d,axis=-1)**3).mean()*np.pi)
    assert abs(cs['-1.0']+degree)<1e-8,(cs,degree)
    records=make(0,'kitaev',np.random.default_rng(SEED))
    for r in records:
        p=json.loads(r['payload_json']);H=np.array(p['hamiltonian_real'])+1j*np.array(p['hamiltonian_imag']);n=len(H)//2
        J=np.block([[np.zeros((n,n)),np.eye(n)],[np.eye(n),np.zeros((n,n))]])
        assert np.max(abs(J@H.conj()@J+H))<1e-12
        bad=H.copy();bad[0,0]+=.1;assert np.max(abs(J@bad.conj()@J+bad))>.09
    square=persistence(np.array([[0,0],[1,0],[1,1],[0,1]]));assert square['H0_essential']==1
    assert np.allclose(square['H1'],[[1,math.sqrt(2)]])
    moved=persistence(np.array([[0,0],[1,0],[1,1],[0,1]])@np.array([[0,-1],[1,0]])+4)
    assert square==moved
    components,edges=connected_groups([0,1,2,7],lambda a,b:'close' if abs(a-b)==1 else None)
    assert components[0]==components[2] and components[3]!=components[2]
    print(json.dumps(dict(passed=True,chern=cs,independent_degree_integral=degree,
        gap_closure_negative_controls=3,BdG_variants=3,particle_hole_mutant_detected=True,
        VR_square_bar=square['H1'],transitive_similarity=True),indent=2))
if __name__=='__main__':main()
