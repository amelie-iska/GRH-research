"""Independent dense NumPy reference for the eight-amplitude token circuit."""
import numpy as np


def single_gate(gate, qubit):
    result=np.ones((1,1),complex)
    for q in range(3):
        result=np.kron(result,gate if q==qubit else np.eye(2))
    return result


def cnot(control,target):
    matrix=np.zeros((8,8),complex)
    for old in range(8):
        new=old ^ (1 << (2-target)) if old & (1 << (2-control)) else old
        matrix[new,old]=1
    return matrix


def simulate(angles,theta,trace=False):
    a=np.asarray(angles,float);t=np.asarray(theta,float)
    if a.shape!=(6,) or t.shape!=(2,3,2) or not np.isfinite(a).all() or not np.isfinite(t).all():
        raise ValueError("angles:[6], theta:[2,3,2], all finite")
    state=np.zeros(8,complex);state[0]=1
    history=[]
    for layer in range(2):
        for q in range(3):
            angle=a[q]+t[layer,q,0];c=np.cos(angle/2);s=np.sin(angle/2)
            state=single_gate(np.array([[c,-s],[s,c]]),q)@state
            if trace:history.append((f"RY({q})",state.copy()))
            angle=a[q+3]+t[layer,q,1]
            state=single_gate(np.diag(np.exp(np.array([-1j,1j])*angle/2)),q)@state
            if trace:history.append((f"RZ({q})",state.copy()))
        for control,target in [(0,1),(1,2)]:
            state=cnot(control,target)@state
            if trace:history.append((f"CNOT({control},{target})",state.copy()))
    u=np.diag(np.exp(2j*np.pi*np.arange(8)/8))
    v=np.zeros((8,8),complex)
    for j in range(8):v[(j-1)%8,j]=1
    expectations=[np.vdot(state,w@state) for w in (u,v,u@v)]
    features=np.asarray([part for z in expectations for part in (z.real,z.imag)])
    return features,state,history


def parameter_shift(angles,theta):
    t=np.asarray(theta,float);jac=np.zeros((6,12))
    for j in range(12):
        plus=t.copy().reshape(-1);minus=t.copy().reshape(-1)
        plus[j]+=np.pi/2;minus[j]-=np.pi/2
        jac[:,j]=(simulate(angles,plus.reshape(t.shape))[0]-simulate(angles,minus.reshape(t.shape))[0])/2
    return jac
