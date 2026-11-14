from pathlib import Path
import json,math
import numpy as np
from scipy.integrate import quad
from scipy.linalg import expm
from electron_clouds import gaussian_integrals
from common import write_json,sha
root=Path(__file__).resolve().parents[2];folder=root/'outputs/experiments/2026-11-04-electron-clouds-v1';data=json.loads((folder/'clouds.json').read_text());maximum=0.;state_error=0.
for case in data['cases']:
    centers=np.array(case['centers']);alpha=np.array(case['alpha']);S,L,H=gaussian_integrals(centers,alpha,np.array(case['nuclei']) if 'nuclei' in case else None,case.get('nuclear_charges'));h=np.array(case['H_real'])+1j*np.array(case['H_imag']);C0=np.array(case['occupied_real'])+1j*np.array(case['occupied_imag'])
    for t in [0.,.27,case['maximum_time']]:
        C=expm(-1j*h*t)@C0;D=L@C;error=float(np.max(abs(D.conj().T@S@D-np.eye(C.shape[1]))));state_error=max(state_error,error);assert error<1e-10
    if 'nuclei' in case:
        # Independent Laplace-transform quadrature of nuclear Coulomb integrals.
        for i in range(len(alpha)):
            for j in range(len(alpha)):
                a,b=alpha[i],alpha[j];p=a+b;mu=a*b/p;P=(a*centers[i]+b*centers[j])/p;N=(2*a/np.pi)**.75*(2*b/np.pi)**.75;d2=np.sum((centers[i]-centers[j])**2);s=N*np.exp(-mu*d2)*(np.pi/p)**1.5
                nodes,weights=np.polynomial.hermite.hermgauss(3);kinetic=0.
                for x,wx in zip(nodes,weights):
                    for y,wy in zip(nodes,weights):
                        for z,wz in zip(nodes,weights):
                            point=P+np.array([x,y,z])/np.sqrt(p);kinetic+=wx*wy*wz*2*a*b*np.dot(point-centers[i],point-centers[j])
                kinetic*=N*np.exp(-mu*d2)/p**1.5
                potential=0.
                for R,Z in zip(case['nuclei'],case['nuclear_charges']):
                    distance=np.sum((P-R)**2)
                    value,_=quad(lambda u:2/np.sqrt(np.pi)*N*np.exp(-mu*d2)*(np.pi/(p+u*u))**1.5*np.exp(-p*u*u/(p+u*u)*distance),0,np.inf,epsabs=1e-11,epsrel=1e-11)
                    potential-=Z*value
                maximum=max(maximum,abs(kinetic+potential-H[i,j]));assert abs(kinetic+potential-H[i,j])<1e-9
        assert np.max(abs(L@H@L-h))<1e-10
    assert case['maximum_decoded_charge_error']<.003
    assert max(abs(x-case['model_electron_number']) for x in case['voxel_integrated_charge_range'])<1e-5
manifest=json.loads((folder/'manifest.json').read_text())
for name,item in manifest['files'].items():assert sha(folder/name)==item['sha256']
report=dict(passed=True,Coulomb_Laplace_quadrature_and_kinetic_Hermite_max_error=maximum,coherent_continuum_particle_normalization_max_error=state_error,all_volume_manifest_hashes=True,
    cases=[dict(id=c['id'],electrons=c['model_electron_number'],voxel_integral=c['voxel_integrated_charge_range'],decoded_charge_error=c['maximum_decoded_charge_error']) for c in data['cases']],
    scope='Independent finite-basis/integral checks, not a converged peptide electronic-structure or interval-verified quantum-chemistry calculation')
write_json(root/'outputs/checks/2026-11-04-synthetic-training/cloud-physics.json',report);print(json.dumps(report,indent=2))
