#!/usr/bin/env python3
"""Train the same three architectures with actual PennyLane simulation calls.

The reference simulator and PennyLane share the stated circuit, seed and data.
Gradients use parameter shift (QCNN/convolution) or central differences
(nonlinear attention). No cloud/device authentication or shots are requested.
"""
from pathlib import Path
import json,platform
import numpy as np
import pennylane as qml
import train_renormalization as T
from surface_models import ansatz
root=Path(__file__).resolve().parents[2]
dev2=qml.device('default.qubit',wires=2,shots=None)
dev4=qml.device('default.qubit',wires=4,shots=None)
@qml.qnode(dev2,interface=None,diff_method=None)
def patch(theta,states):
    qml.StatePrep(states,wires=[0,1]);qml.QubitUnitary(ansatz(theta,2,[(0,1)]),wires=[0,1])
    return qml.expval(qml.PauliZ(0)),qml.expval(qml.PauliZ(1)),qml.expval(qml.PauliZ(0)@qml.PauliZ(1))
@qml.qnode(dev4,interface=None,diff_method=None)
def pool(theta,states):
    qml.StatePrep(states,wires=[0,1,2,3]);qml.QubitUnitary(ansatz(theta,4,[(0,1),(1,2),(2,3),(3,0)]),wires=[0,1,2,3])
    return qml.expval(qml.Projector([0,0],wires=[2,3]))
def features(theta,states):return np.asarray(patch(theta,states)).T
def scores(theta,states,edges,projector):return np.asarray(pool(theta,states))
# Meaningful backend equivalence check on nontrivial parameters and inputs.
rng=np.random.default_rng(817);theta=rng.normal(size=8);states=rng.normal(size=(9,4))+1j*rng.normal(size=(9,4));states/=np.linalg.norm(states,axis=1)[:,None]
error=float(np.max(abs(features(theta,states)-T.patch_features(theta,states))))
assert error<1e-10
T.patch_features=features;T.pooling_scores=scores
models=[T.pooling(),T.convolution(),T.attention()]
for m in models:m['backend']='PennyLane default.qubit CPU, analytic expectations'
out=dict(seed=T.SEED,python=platform.python_version(),pennylane=qml.__version__,numpy=np.__version__,backend_crosscheck_max_error=error,scope='finite synthetic training; no hardware or GRH claim',models=models)
for folder in [root/'outputs/experiments/renormalization-pennylane',root/'web/data']:
 folder.mkdir(parents=True,exist_ok=True);(folder/'training.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({m['name']:dict(first=m['curve'][0],last=m['curve'][-1]) for m in models},indent=2))
