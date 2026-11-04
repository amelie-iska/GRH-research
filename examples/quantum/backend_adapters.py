#!/usr/bin/env python3
"""Optional SDK cross-checks for a finite four-level clock/shift carrier.

No installation, authentication, cloud or GPU selection occurs on import.
Invoke with --backend cirq|qiskit|pennylane|strawberryfields|cuquantum|cudaq.
These are finite-carrier validations, not faithful completed-order realizations.
"""
import argparse,json
import numpy as np
from surface_models import clock_shift

def run(backend):
    U,V,z=clock_shift(4)
    F=np.array([[np.exp(2j*np.pi*j*k/4)/2 for k in range(4)] for j in range(4)])
    expected=(V@U@F)[:,0]
    if backend=='cirq':
        import cirq
        qs=cirq.LineQubit.range(2)
        circuit=cirq.Circuit(cirq.MatrixGate(F)(*qs),cirq.MatrixGate(U)(*qs),cirq.MatrixGate(V)(*qs))
        state=cirq.Simulator(dtype=np.complex128,seed=20261103).simulate(circuit).final_state_vector
    elif backend=='qiskit':
        from qiskit import QuantumCircuit
        from qiskit.quantum_info import Statevector
        circuit=QuantumCircuit(2);circuit.unitary(F,[0,1],label='Fourier');circuit.unitary(U,[0,1],label='clock');circuit.unitary(V,[0,1],label='shift')
        state=np.asarray(Statevector.from_instruction(circuit).data)
    elif backend=='pennylane':
        import pennylane as qml
        dev=qml.device('default.qubit',wires=2,shots=None)
        @qml.qnode(dev)
        def circuit():
            qml.QubitUnitary(F,wires=[0,1]);qml.QubitUnitary(U,wires=[0,1]);qml.QubitUnitary(V,wires=[0,1]);return qml.state()
        state=np.asarray(circuit())
    elif backend=='strawberryfields':
        # A genuine photonic model: one photon in four modes, passive U(4).
        # Mode 0 is first, so |1,0,0,0> labels carrier basis 0.
        import strawberryfields as sf
        from strawberryfields import ops
        program=sf.Program(4)
        with program.context as q:
            ops.Fock(1)|q[0]
            ops.Interferometer(F)|q
            ops.Interferometer(U)|q
            ops.Interferometer(V)|q
        result=sf.Engine('fock',backend_options={'cutoff_dim':2}).run(program)
        dm=result.state.dm()
        block=np.empty((4,4),complex)
        for i in range(4):
            for j in range(4):
                left=[0]*4;right=[0]*4;left[i]=1;right[j]=1
                index=tuple(x for pair in zip(left,right) for x in pair)
                block[i,j]=dm[index]
        error=float(np.linalg.norm(block-np.outer(expected,expected.conj())))
        assert error<1e-6,error
        return dict(backend=backend,error=error,comparison='one-photon density matrix including off-diagonal phases',scope='four-mode photonic carrier, cutoff2; passive number-conserving gates')
    elif backend=='cuquantum':
        # Explicit local GPU allocation only when this backend is selected.
        import cupy as cp
        from cuquantum import contract
        state=cp.asnumpy(contract('ij,jk,k->i',cp.asarray(V),cp.asarray(U),cp.asarray(F[:,0])))
    elif backend=='cudaq':
        import cudaq
        # Uses the current local target; never silently selects a remote backend.
        if cudaq.get_target().name not in ['qpp-cpu','nvidia']:
            raise RuntimeError('Choose an approved local CUDA-Q target explicitly')
        cudaq.register_operation('surface_fourier',F)
        cudaq.register_operation('surface_clock',U)
        cudaq.register_operation('surface_shift',V)
        @cudaq.kernel
        def circuit():
            q=cudaq.qvector(2)
            surface_fourier(q[0],q[1])
            surface_clock(q[0],q[1])
            surface_shift(q[0],q[1])
        state=np.asarray(cudaq.get_state(circuit))
    else:raise ValueError(backend)
    error=float(np.linalg.norm(state-expected))
    assert error<1e-6,(backend,error,state,expected)
    return dict(backend=backend,error=error,scope='four-level finite carrier; CPU/GPU backend-specific',state=[[float(x.real),float(x.imag)] for x in state])
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--backend',required=True,choices=['cirq','qiskit','pennylane','strawberryfields','cuquantum','cudaq']);a=p.parse_args()
    print(json.dumps(run(a.backend),indent=2))
