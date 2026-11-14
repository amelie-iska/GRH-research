"""Checked finite complex wave packets with explicit, distinct topology labels."""
from pathlib import Path
import argparse,json,math
import numpy as np
from common import fresh,write_json,sha

def packet(name,H,positions,edges,initial,topology,site_groups=None):
    e,v=np.linalg.eigh(H);assert np.max(abs(H-H.conj().T))<1e-12
    initial=np.asarray(initial,complex);initial/=np.linalg.norm(initial);times=np.linspace(0,45,241);states=np.exp(-1j*times[:,None]*e)@(v.conj().T@initial)[:,None] if False else (np.exp(-1j*times[:,None]*e)*(v.conj().T@initial)[None,:])@v.T
    error=float(np.max(abs(np.sum(abs(states)**2,axis=1)-1)));assert error<1e-11
    groups=site_groups or [[i] for i in range(len(H))];prob=np.array([[float(np.sum(abs(psi[g])**2)) for g in groups] for psi in states])
    currents=[];coherence=[];continuity=0.
    for psi in states:
        derivative=-1j*H@psi;dn=2*np.real(psi.conj()*derivative);flux=np.zeros(len(H));J=[]
        for a,b in edges:
            value=-2*np.imag(H[a,b]*psi[b]*psi[a].conjugate());flux[a]+=value;flux[b]-=value;J.append(float(value))
        continuity=max(continuity,float(np.max(abs(dn+flux))));currents.append(J)
        coherence.append((psi[:,None]*psi[None,:].conj()).tolist() if False else [])
    assert continuity<1e-10
    return dict(id=name,title=name.replace('_',' '),hamiltonian_real=H.real.tolist(),hamiltonian_imag=H.imag.tolist(),positions=positions,edges=edges,groups=groups,
        initial_real=initial.real.tolist(),initial_imag=initial.imag.tolist(),eigenvalues=e.tolist(),eigenvectors_real=v.real.tolist(),eigenvectors_imag=v.imag.tolist(),
        time=times.tolist(),psi_real=states.real.tolist(),psi_imag=states.imag.tolist(),site_probability=prob.tolist(),bond_current=currents,
        normalization_error=error,continuity_error=continuity,topology=topology,units='Dimensionless hbar=1; finite effective orbitals, not ab-initio atomic density',
        observables=dict(return_probability=(abs(states@initial.conj())**2).tolist(),inverse_participation=np.sum(prob**2,axis=1).tolist()))

def main(out):
    out=fresh(out);cases=[]
    for topological in [False,True]:
        n=48;H=np.zeros((n,n),complex);t1,t2=(.55,1.45) if topological else (1.45,.55);edges=[]
        for i in range(n-1):H[i,i+1]=H[i+1,i]=t1 if i%2==0 else t2;edges.append((i,i+1))
        initial=np.eye(n)[0];positions=[[i*.55,.35*(-1)**i,0] for i in range(n)]
        cases.append(packet('SSH_topological_edge' if topological else 'SSH_trivial_control',H,positions,edges,initial,dict(kind='Chiral one-dimensional SSH winding',winding=int(topological),t1=t1,t2=t2,bulk_gap=2*abs(t1-t2),scope='Infinite periodic bulk invariant versus actual finite open-chain propagation; matched local initial states.')))
    n=61;H=np.zeros((n,n),complex);edges=[]
    for i in range(n-1):
        hopping=(1.5 if i%2==0 else .5) if i<30 else (.5 if i%2==0 else 1.5);H[i,i+1]=H[i+1,i]=hopping;edges.append((i,i+1))
    e,v=np.linalg.eigh(H);zero=v[:,np.argmin(abs(e))];assert abs(e[np.argmin(abs(e))])<1e-12 and abs(zero[30])**2>.5
    cases.append(packet('SSH_domain_wall_zero_mode',H,[[i*.45,.35*(-1)**i,0] for i in range(n)],edges,np.eye(n)[30],dict(kind='Interface between SSH winding0 and1; chiral sublattice index1',left_winding=0,right_winding=1,zero_energy=float(e[np.argmin(abs(e))]),center_mode_weight=float(abs(zero[30])**2),scope='An odd irreducible bipartite finite chain has one exact zero mode; localization follows the strong/weak recurrence.')))
    sx=np.array([[0,1],[1,0]],complex);sy=np.array([[0,-1j],[1j,0]],complex);sz=np.diag([1.,-1.]);nx,ny=12,10;N=nx*ny*2
    for mass in [-1.,-3.]:
        H=np.zeros((N,N),complex);positions=[];groups=[]
        for y in range(ny):
            for x in range(nx):
                i=2*(x+nx*y);H[i:i+2,i:i+2]=mass*sz;positions.extend([[x,y,-.1],[x,y,.1]]);groups.append([i,i+1])
                for dx,dy,T in [(1,0,(sz-1j*sx)/2),(0,1,(sz-1j*sy)/2)]:
                    if x+dx<nx and y+dy<ny:
                        j=2*((x+dx)+nx*(y+dy));H[i:i+2,j:j+2]=T;H[j:j+2,i:i+2]=T.conj().T
        edges=[(i,j) for i in range(N) for j in range(i+1,N) if abs(H[i,j])>1e-12];initial=np.zeros(N,complex);initial[0]=1/math.sqrt(2);initial[1]=1j/math.sqrt(2)
        case=packet('QWZ_Chern_edge_packet' if mass==-1 else 'QWZ_trivial_bulk_control',H,positions,edges,initial,dict(kind='Two-dimensional QWZ occupied-band Chern invariant',chern=-1 if mass==-1 else 0,mass=mass,bulk_gap=2*min(abs(mass+2),abs(mass),abs(mass-2)),nx=nx,ny=ny,scope='Same unfiltered corner spinor in both controls. Finite edge probability is not itself a Chern proof.'))
        boundary=[i for y in range(ny) for x in range(nx) if x in [0,nx-1] or y in [0,ny-1] for i in [x+nx*y]]
        case['observables']['boundary_probability']=np.array(case['site_probability'])[:,boundary].sum(1).tolist();cases.append(case)
    write_json(out/'wavepackets.json',dict(cases=cases,scope='Executed finite Schrodinger propagation and continuity. Bulk winding/Chern, phase vortices and geometric persistence are different invariants.'))
    write_json(out/'manifest.json',dict(source_sha256=sha(__file__),files={p.name:dict(sha256=sha(p),bytes=p.stat().st_size) for p in out.iterdir() if p.is_file()}))
    print(dict(cases=len(cases),output=str(out)))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();main(a.output)
