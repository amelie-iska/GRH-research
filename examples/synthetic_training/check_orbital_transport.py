import json,math
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from scipy.integrate import quad
from materials import bloch,chern
from common import write_json
root=Path(__file__).resolve().parents[2];data=json.loads((root/'outputs/experiments/2026-11-04-orbital-transport-v1/wavepackets.json').read_text());maximum=0.;checks=[]
for c in data['cases']:
    H=np.array(c['hamiltonian_real'])+1j*np.array(c['hamiltonian_imag']);initial=np.array(c['initial_real'])+1j*np.array(c['initial_imag'])
    for index in [0,17,100,240]:
        expected=expm(-1j*H*c['time'][index])@initial;actual=np.array(c['psi_real'][index])+1j*np.array(c['psi_imag'][index]);error=float(np.max(abs(expected-actual)));maximum=max(maximum,error);assert error<1e-11
    if c['id'].startswith('SSH'):
        signs=(-1.)**np.arange(len(H));assert np.max(abs(signs[:,None]*H*signs[None,:]+H))<1e-12
    if c['id'].startswith('QWZ'):
        for mesh in [32,64]:
            invariant=chern(bloch('qwz',dict(mass=c['topology']['mass']),mesh));assert abs(invariant['value']-c['topology']['chern'])<1e-10
    checks.append(dict(case=c['id'],normalization_error=c['normalization_error'],continuity_error=c['continuity_error']))
norms=[4*quad(lambda r:r*r*np.exp(-2*r),0,np.inf)[0],quad(lambda r:r**4*np.exp(-r),0,np.inf)[0]/24,quad(lambda r:(2-r)**2*r*r*np.exp(-r),0,np.inf)[0]/8]
assert max(abs(x-1) for x in norms)<1e-10
angle=np.linspace(0,2*np.pi,201);phase=np.unwrap(np.angle(np.cos(angle)+1j*np.sin(angle)));winding=(phase[-1]-phase[0])/(2*np.pi);assert abs(winding-1)<1e-12
report=dict(passed=True,independent_expm_max_error=maximum,cases=checks,hydrogen_radial_angular_norms=norms,complex_2p_phase_winding=winding,
    scope='Finite effective Hamiltonians and analytic nonrelativistic isolated hydrogen; no ab-initio molecule, many-electron density or GRH theorem')
write_json(root/'outputs/checks/2026-11-04-synthetic-training/orbital-verification.json',report);print(json.dumps(report,indent=2))
