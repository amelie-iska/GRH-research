"""Small, reproducible finite carriers of the book's surface technology.

NumPy reference backend; no claim to faithfully represent the completed order.
Conventions: qubit 0 is most significant; gates act on column state vectors.
"""
import numpy as np
from math import pi
I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.diag([1,-1]).astype(complex)

def kron(*ops):
    out=np.array([[1]],complex)
    for op in ops: out=np.kron(out,op)
    return out

def gate1(g,q,n): return kron(*(g if j==q else I for j in range(n)))
def ry(t): return np.cos(t/2)*I-1j*np.sin(t/2)*Y
def rz(t): return np.cos(t/2)*I-1j*np.sin(t/2)*Z

def cnot(a,b,n):
    m=np.zeros((2**n,2**n),complex)
    for j in range(2**n):
        k=j^(1<<(n-1-b)) if j&(1<<(n-1-a)) else j
        m[k,j]=1
    return m

def cz(a,b,n):
    return np.diag([-1 if j&(1<<(n-1-a)) and j&(1<<(n-1-b)) else 1 for j in range(2**n)]).astype(complex)

def clock_shift(d):
    z=np.exp(2j*pi/d)
    U=np.diag(z**np.arange(d)); V=np.roll(np.eye(d),1,axis=0)
    return U,V,z

def twisted_shift(d,u):
    C=np.roll(np.eye(d,dtype=complex),1,axis=0); C[0,-1]=u
    return C

def graph_hamiltonian(n,edges,h):
    return -sum((gate1(Z,a,n)@gate1(Z,b,n) for a,b in edges),np.zeros((2**n,2**n),complex))-h*sum((gate1(X,q,n) for q in range(n)),np.zeros((2**n,2**n),complex))

def ansatz(theta,n,edges):
    """Two Ry/Rz layers with CZ edges, followed by disjoint pooling CNOTs."""
    theta=np.asarray(theta).reshape(2,n,2); U=np.eye(2**n,dtype=complex)
    for layer in theta:
        for q,(a,b) in enumerate(layer): U=gate1(rz(b)@ry(a),q,n)@U
        for a,b in edges: U=cz(a,b,n)@U
    for q in range(n//2): U=cnot(q,n//2+q,n)@U
    return U

def reduced_keep(state,n,keep):
    """Partial trace over the final n-keep qubits; CPTP pooling."""
    A=state.reshape(2**keep,2**(n-keep))
    return A@A.conj().T

def effective_ising(k1,k2):
    # Sum the middle spin in a three-site, zero-field chain.
    return np.arctanh(np.tanh(k1)*np.tanh(k2))

def encoded_patch(x):
    s=np.array([1,0,0,0],complex)
    return (np.kron(ry(x[0]),ry(x[1]))@s)

def patch_features(theta,states):
    U=ansatz(theta,2,[(0,1)]); states=states@U.T
    probabilities=abs(states)**2
    return probabilities@np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],float)
