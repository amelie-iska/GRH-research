"""Independent local orbital states, hydrogen current and torus transport checks."""
from pathlib import Path
import json,math
import numpy as np
from scipy.integrate import quad
from scipy.sparse.linalg import expm_multiply

ROOT=Path(__file__).resolve().parents[3]

def main():
    data=json.loads((ROOT/'outputs/experiments/2026-11-04-orbital-transport-v1/wavepackets.json').read_text())
    web=json.loads((ROOT/'web/data/synthetic-training/orbital-v1/wavepackets.json').read_text())
    results=[]
    for c,w in zip(data['cases'],web['cases']):
        assert c['id']==w['id'];H=np.array(c['hamiltonian_real'])+1j*np.array(c['hamiltonian_imag'])
        initial=np.array(c['initial_real'])+1j*np.array(c['initial_imag']);error=0.;current_error=0.;continuity=0.
        for k in [0,51,240]:
            t=c['time'][k];psi=expm_multiply(-1j*H*t,initial)
            saved=np.array(c['psi_real'][k])+1j*np.array(c['psi_imag'][k])
            error=max(error,float(abs(psi-saved).max()))
            dn=2*np.real(psi.conj()*(-1j*H@psi));flux=np.zeros(len(H));currents=[]
            for i,j in c['edges']:
                value=-2*np.imag(H[i,j]*psi[j]*psi[i].conjugate());flux[i]+=value;flux[j]-=value;currents.append(value)
            current_error=max(current_error,float(abs(np.array(currents)-c['bond_current'][k]).max()))
            continuity=max(continuity,float(abs(dn+flux).max()))
        assert max(error,current_error,continuity)<1e-10
        for name in ['hamiltonian_real','hamiltonian_imag','initial_real','initial_imag','eigenvalues','eigenvectors_real','eigenvectors_imag']:
            assert np.array_equal(np.array(c[name]),np.array(w[name]))
        if 'domain_wall' in c['id']:
            ev,V=np.linalg.eigh(H);assert sum(abs(ev)<1e-10)==1
            zero=V[:,np.argmin(abs(ev))];assert abs(zero[30])**2>.5 and abs(zero[1::2]).max()<1e-12
            assert np.max(abs(abs(zero[32::2]/zero[30:-2:2])-1/3))<1e-8
        results.append(dict(case=c['id'],Krylov_state_error=error,current_error=current_error,continuity_residual=continuity))
    norms=[4*quad(lambda r:r*r*np.exp(-2*r),0,np.inf)[0],quad(lambda r:(2-r)**2*r*r*np.exp(-r),0,np.inf)[0]/8,quad(lambda r:r**4*np.exp(-r),0,np.inf)[0]/24]
    assert max(abs(np.array(norms)-1))<1e-12
    def vortex(p):return (p[0]+1j*p[1])*np.exp(-np.linalg.norm(p)/2)/(8*np.sqrt(np.pi))
    current_error=0.;lz_error=0.
    for p in [np.array([1.,.7,.3]),np.array([-.8,1.1,-.2]),np.array([.2,-.9,1.2])]:
        h=1e-5;gradient=np.array([(vortex(p+h*np.eye(3)[i])-vortex(p-h*np.eye(3)[i]))/(2*h) for i in range(3)])
        exact=np.exp(-np.linalg.norm(p))/(64*np.pi)*np.array([-p[1],p[0],0.])
        current_error=max(current_error,float(abs(np.imag(vortex(p).conjugate()*gradient)-exact).max()))
        lz_error=max(lz_error,float(abs(-1j*(p[0]*gradient[1]-p[1]*gradient[0])-vortex(p))))
    assert current_error<1e-10 and lz_error<1e-9
    # Explicit conditional integrals for an independent uniform-torus coupling.
    D=-np.pi+(np.arange(8192)+.5)*2*np.pi/8192
    q=lambda x:(1+.3*np.cos(x)+.2*np.sin(2*x))/(2*np.pi)
    def rho_flux(x,t):
        vals=q(x+(1-t)*D);return vals.mean(),float((D*vals).mean())
    weak_error=0.
    for x,t in [(.4,.2),(-1.3,.7),(2.2,.95)]:
        h=1e-5;dr=(rho_flux(x,t+h)[0]-rho_flux(x,t-h)[0])/(2*h)
        dj=(rho_flux(x+h,t)[1]-rho_flux(x-h,t)[1])/(2*h)
        weak_error=max(weak_error,abs(dr+dj))
        assert abs(rho_flux(x,0)[0]-1/(2*np.pi))<1e-14
        assert abs(rho_flux(x,1)[0]-q(x))<1e-14 and abs(rho_flux(x,1)[1])<1e-14
    assert weak_error<1e-8
    result=dict(passed=True,finite_propagation=results,hydrogen_basis_norms=norms,
        hydrogen_vortex_current_FD_error=current_error,hydrogen_Lz_FD_error=lz_error,
        torus_conditional_integral_continuity_residual=weak_error,
        scope='Independent local NumPy/SciPy checks; no Torch, browser GPU, remote or training action')
    out=ROOT/'outputs/checks/2026-11-04-synthetic-training/review';out.mkdir(parents=True,exist_ok=True)
    (out/'orbital-math-review.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':main()
