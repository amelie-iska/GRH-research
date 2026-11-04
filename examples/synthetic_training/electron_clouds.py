"""Real-space density volumes from normalized continuum finite-basis states.

H2+ uses analytic Gaussian kinetic/nuclear Coulomb integrals at fixed nuclei.
The peptide fixture is explicitly a different, uncalibrated dataset Hamiltonian.
"""
from pathlib import Path
import argparse,json,math
import numpy as np
from scipy.special import erf
from PIL import Image
from common import fresh,write_json,sha

def gaussian_integrals(centers,alpha,nuclei=None,charges=None):
    r=np.asarray(centers);a=np.asarray(alpha);p=a[:,None]+a[None,:];mu=a[:,None]*a[None,:]/p;d2=np.sum((r[:,None]-r[None,:])**2,axis=-1);N=(2*a/np.pi)**.75;factor=N[:,None]*N[None,:]*np.exp(-mu*d2)
    S=factor*(np.pi/p)**1.5;T=mu*(3-2*mu*d2)*S;V=np.zeros_like(S);P=(a[:,None,None]*r[:,None,:]+a[None,:,None]*r[None,:,:])/p[:,:,None]
    if nuclei is not None:
        for R,Z in zip(nuclei,charges):
            x=p*np.sum((P-R)**2,axis=-1);F=np.ones_like(x);mask=x>1e-10;F[mask]=.5*np.sqrt(np.pi/x[mask])*erf(np.sqrt(x[mask]));V-=Z*factor*2*np.pi/p*F
    e,v=np.linalg.eigh(S);assert e.min()>1e-8;L=(v/np.sqrt(e))@v.T
    assert np.max(abs(L@S@L-np.eye(len(S))))<1e-10
    return S,L,T+V

def volume(case,out):
    centers=np.array(case['centers']);alpha=np.array(case['alpha']);H=np.array(case['H_real'])+1j*np.array(case['H_imag']);occupied=np.array(case['occupied_real'])+1j*np.array(case['occupied_imag']);S,L,_=gaussian_integrals(centers,alpha);e,v=np.linalg.eigh(H);rank=occupied.shape[1]
    assert np.max(abs(occupied.conj().T@occupied-np.eye(rank)))<1e-10
    margin=4.5/math.sqrt(alpha.min());lo=centers.min(0)-margin;hi=centers.max(0)+margin;n=64
    axes=[np.linspace(lo[k],hi[k],n) for k in range(3)];xyz=np.stack(np.meshgrid(*axes,indexing='ij'),-1).reshape(-1,3);step=(hi-lo)/(n-1)
    G=(2*alpha/np.pi)**.75*np.exp(-np.sum((xyz[:,None,:]-centers[None,:,:])**2,axis=-1)*alpha[None,:]);times=np.linspace(0,case['maximum_time'],41);fields=[];charges=[];normerror=0.
    for time in times:
        U=(v*np.exp(-1j*e*time))@v.conj().T;C=U@occupied;A=L@C;psi=G@A;density=np.sum(abs(psi)**2,axis=1).reshape(n,n,n);normerror=max(normerror,float(np.max(abs(C.conj().T@C-np.eye(rank)))))
        q=density
        for dx in step[::-1]:q=np.trapz(q,dx=dx,axis=-1)
        charges.append(float(q));fields.append(density.astype(np.float32))
    maximum=float(max(q.max() for q in fields));dest=out/case['id'];dest.mkdir();cols=math.ceil(math.sqrt(n));rows=math.ceil(n/cols);filenames=[];max_quantized_charge_error=0.
    for k,rho in enumerate(fields):
        encoded=np.rint(np.sqrt(rho/maximum)*255).astype(np.uint8);decoded=(encoded.astype(float)/255)**2*maximum
        q=decoded
        for dx in step[::-1]:q=np.trapz(q,dx=dx,axis=-1)
        max_quantized_charge_error=max(max_quantized_charge_error,abs(float(q)-rank))
        atlas=np.zeros((rows*n,cols*n),np.uint8)
        for z in range(n):atlas[(z//cols)*n:(z//cols+1)*n,(z%cols)*n:(z%cols+1)*n]=encoded[:,:,z].T
        file=dest/f'frame-{k:03d}.png';Image.fromarray(atlas).save(file);filenames.append(case['id']+'/'+file.name)
    assert normerror<1e-10
    return dict(**case,grid=n,atlas_columns=cols,atlas_rows=rows,lower=lo.tolist(),upper=hi.tolist(),maximum_density=maximum,frames=filenames,time=times.tolist(),model_electron_number=rank,
        orthonormality_error=float(np.max(abs(L@S@L-np.eye(len(S))))),state_norm_error=normerror,voxel_integrated_charge_range=[min(charges),max(charges)],maximum_decoded_charge_error=max_quantized_charge_error,
        density_formula='rho(r,t)=sum_a |sum_i g_i(r) [S^-1/2 U(t) C0]_ia|^2; includes spatial coherence, not independent atom smears',
        encoding='sqrt(rho/maxrho) rounded to8bit PNG atlas; approximate spatial/time display interpolation; analytic full-space particle number is exact')

def main(out):
    out=fresh(out);cases=[]
    nuclei=np.array([[-1.,0,0],[1.,0,0]]);centers=np.repeat(nuclei,3,axis=0);alpha=np.tile([.3,1.2,4.8],2);S,L,H=gaussian_integrals(centers,alpha,nuclei,[1,1]);h=L@H@L
    e,v=np.linalg.eigh(S);sqrtS=(v*np.sqrt(e))@v.T;initial=sqrtS[:,[0]];initial/=np.linalg.norm(initial)
    cases.append(dict(id='H2plus-fixed-nuclei',title='H₂⁺: one-electron Coulomb charge transfer',centers=centers.tolist(),alpha=alpha.tolist(),H_real=h.tolist(),H_imag=np.zeros_like(h).tolist(),occupied_real=initial.tolist(),occupied_imag=np.zeros_like(initial).tolist(),maximum_time=50.,time_units='atomic time units',density_units='electron / a0^3',nuclei=nuclei.tolist(),nuclear_charges=[1,1],ground_electronic_energy_hartree=float(np.linalg.eigvalsh(h)[0]),nuclear_repulsion_hartree=.5,
        scope='Six normalized s-Gaussians, analytic kinetic and nuclear-Coulomb integrals, fixed nuclei R=2a0. One-electron Galerkin calculation; not a converged many-electron molecule or peptide density.'))
    fixture=Path(__file__).resolve().parents[2]/'web/data/synthetic-training/large-v2/examples.json';data=json.loads(fixture.read_text());c=next(c for c in data['cases'] if c['title'].startswith('PDB residue transfer / 1L2Y'));p=c['electronic'];H=np.array(p['conditions']['hamiltonian_real'])+1j*np.array(p['conditions']['hamiltonian_imag']);P0=np.array(p['conditions']['initial_occupation_matrix_real'])+1j*np.array(p['conditions']['initial_occupation_matrix_imag']);e,v=np.linalg.eigh(P0);C=v[:,e>.5]
    cases.append(dict(id='Trp-cage-effective-basis',title='Trp-cage: dataset finite-basis fermion density',centers=c['positions'],alpha=[.25]*len(H),H_real=H.real.tolist(),H_imag=H.imag.tolist(),occupied_real=C.real.tolist(),occupied_imag=C.imag.tolist(),maximum_time=12.,time_units='dimensionless hbar=1',density_units='model particles / angstrom^3',source_record_id=c['id'],source_PDB='1L2Y',scope='Explicit orthonormal Gaussian realization of the uncalibrated CA contact Hamiltonian, with model half filling. Not real protein valence-electron density, DFT or a measured charge-transfer rate.'))
    result=[volume(c,out) for c in cases];write_json(out/'clouds.json',dict(cases=result,origin_class='new_simulation',scope='Real density of the explicitly stated finite-basis models, distinct from the exact isolated-hydrogen benchmark and from ab-initio peptide density'))
    write_json(out/'manifest.json',dict(source_sha256=sha(__file__),files={str(p.relative_to(out)):dict(sha256=sha(p),bytes=p.stat().st_size) for p in out.rglob('*') if p.is_file()}));print([(c['id'],c['voxel_integrated_charge_range']) for c in result])
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();main(a.output)
