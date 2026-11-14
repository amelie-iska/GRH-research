#!/usr/bin/env python3
"""Fixed trained channel on a designed coherent family; freeze finite graph labels.

No training. Distance estimates are floating-point, not interval certificates.
Integer labels define the exact combinatorial object used by the browser.
"""
from pathlib import Path
import hashlib,json,sys
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'examples/quantum'))
from surface_models import ansatz,reduced_keep


def main():
    checkpoint=ROOT/'outputs/experiments/renormalization-pennylane/training.json'
    data=json.loads(checkpoint.read_text());theta=data['models'][0]['theta']
    U=ansatz(theta,4,[(0,1),(1,2),(2,3),(3,0)])
    assert np.linalg.norm(U.conj().T@U-np.eye(16))<1e-10
    states=[];points=[]
    for j in range(8):
        phi=2*np.pi*j/8
        q=np.array([1,np.exp(1j*phi)])/np.sqrt(2)
        state=np.zeros(16,complex);state[0]=q[0];state[8]=q[1]
        states.append(state);points.append(dict(id=j,label=f'equator{j}',birth=500,position=[float(np.cos(phi)),float(np.sin(phi)),0]))
    for name,j,z,birth in [('north',0,1,1000),('south',8,-1,0)]:
        state=np.zeros(16,complex);state[j]=1;states.append(state)
        points.append(dict(id=len(points),label=name,birth=birth,position=[0,0,z]))
    inputs=[np.outer(s,s.conj()) for s in states]
    outputs=[reduced_keep(U@s,4,2) for s in states]
    def distances(rhos):
        return [[float(np.clip(np.abs(np.linalg.eigvalsh(a-b)).sum()/2,0,1)) for b in rhos] for a in rhos]
    din=np.array(distances(inputs));dout=np.array(distances(outputs));scale=1000
    ilabel=np.ceil(scale*din).astype(int);olabel=np.ceil(scale*dout).astype(int)
    np.fill_diagonal(ilabel,0);np.fill_diagonal(olabel,0)
    assert np.max(dout-din)<1e-10 and np.all(olabel<=ilabel)
    for r in outputs:assert abs(np.trace(r)-1)<1e-10 and np.linalg.eigvalsh(r)[0]>-1e-10
    out=dict(schema_version=1,points=points,scale=scale,input_labels=ilabel.tolist(),output_labels=olabel.tolist(),
        numerical_input_distances=din.tolist(),numerical_output_distances=dout.tolist(),
        input_amplitudes=[[[float(v.real),float(v.imag)] for v in s] for s in states],
        output_densities=[[[[float(v.real),float(v.imag)] for v in row] for row in r] for r in outputs],
        provenance=dict(kind='designed coherent test family through one saved trained channel',
            checkpoint=str(checkpoint.relative_to(ROOT)),checkpoint_sha256=hashlib.sha256(checkpoint.read_bytes()).hexdigest(),
            channel_implementation='examples/quantum/surface_models.py',
            channel_implementation_sha256=hashlib.sha256((ROOT/'examples/quantum/surface_models.py').read_bytes()).hexdigest(),
            training_seed=data['seed'],training='No optimizer run; not claimed as training or held-out data',
            generator_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            channel='Same four-qubit saved U for all states, trace out final two wires; qubit0 most significant',
            labels='ceil(1000*clipped numerical trace distance); fixed integer labels, not certified exact quantum distances',
            birth='Fixed input (I+Z0)/2 population grade: south0, equator500, north1000; reused for output',
            topology='Flag2-skeleton; H0/H1 only; layout uses input Bloch coordinates for both graphs'),
        checks=dict(unitary_error=float(np.linalg.norm(U.conj().T@U-np.eye(16))),
            numerical_contractivity_violation=float(max(0,np.max(dout-din))),integer_output_labels_below_input=True))
    body=json.dumps(out,indent=2)+'\n';digest=hashlib.sha256(body.encode()).hexdigest()
    folder=ROOT/'web/data/persistence';folder.mkdir(parents=True,exist_ok=True)
    target=folder/('quantum-'+digest[:16]+'.json')
    if target.exists():assert target.read_text()==body
    else:target.write_text(body)
    manifest=dict(file=target.name,sha256=digest,source='examples/persistence/export_quantum_bifiltration.py')
    (folder/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps(dict(points=10,saved_channel=True,sha256=digest,checks=out['checks']),indent=2))


if __name__=='__main__':main()
