#!/usr/bin/env python3
"""Independent CPU-backend and literal-loop checks for architecture trace exports.

No optimization, network, checkpoint mutation or dependency installation.
"""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys
import numpy as np
from scipy.special import erf

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"examples/architecture"))
from trace_schema import array,validate,source
import classical_traces as C


def nodes(trace):
    return {n["id"]:array(n["tensor"]) for n in trace["nodes"]}


def check_quantum_backend(trace, record):
    import pennylane as qml
    values=nodes(trace)
    prefixes=[n["id"][:-6] for n in trace["nodes"] if n["id"].endswith(".input")]
    error=0
    for prefix in prefixes:
        initial=values[prefix+".input"]
        n=int(np.log2(len(initial)))
        gates=[g for g in trace["nodes"] if g["id"].startswith(prefix+".") and "gate" in g]
        dev=qml.device("default.qubit",wires=n,shots=None)
        @qml.qnode(dev,interface=None,diff_method=None)
        def circuit():
            qml.StatePrep(initial,wires=range(n))
            for gate in gates:
                if gate["gate"]=="RY":qml.RY(gate["angle"],wires=gate["wires"][0])
                elif gate["gate"]=="RZ":qml.RZ(gate["angle"],wires=gate["wires"][0])
                elif gate["gate"]=="CZ":qml.CZ(wires=gate["wires"])
                elif gate["gate"]=="CNOT":qml.CNOT(wires=gate["wires"])
                else:raise AssertionError("Unknown gate")
            return qml.state()
        error=max(error,float(np.max(abs(circuit()-values[gates[-1]["id"]]))))
        # Check every stored state, not only the final probabilities.
        for gate in gates:
            state=values[gate["id"]]
            assert abs(np.vdot(state,state)-1)<1e-9
    assert error<1e-9
    record[trace["id"]+".pennylane_state_error"]=error


def check_two_other_backends(trace,record):
    import cirq
    from qiskit import QuantumCircuit
    from qiskit.quantum_info import Statevector
    values=nodes(trace);initial=values["patch.input"]
    gates=[g for g in trace["nodes"] if g["id"].startswith("patch.") and "gate" in g]
    qubits=cirq.LineQubit.range(2);cc=cirq.Circuit();qc=QuantumCircuit(2)
    for g in gates:
        wires=g["wires"]
        if g["gate"]=="RY":
            cc.append(cirq.ry(g["angle"])(qubits[wires[0]]));qc.ry(g["angle"],1-wires[0])
        elif g["gate"]=="RZ":
            cc.append(cirq.rz(g["angle"])(qubits[wires[0]]));qc.rz(g["angle"],1-wires[0])
        elif g["gate"]=="CZ":
            cc.append(cirq.CZ(*(qubits[q] for q in wires)));qc.cz(*(1-q for q in wires))
        else:
            cc.append(cirq.CNOT(*(qubits[q] for q in wires)));qc.cx(*(1-q for q in wires))
    ref=values[gates[-1]["id"]]
    c=cirq.Simulator(dtype=np.complex128).simulate(cc,qubit_order=qubits,initial_state=initial).final_state_vector
    q=np.asarray(Statevector(initial).evolve(qc))
    for name,state in [("cirq",c),("qiskit",q)]:
        err=float(np.max(abs(state-ref)));assert err<1e-9
        record[trace["id"]+"."+name+"_state_error"]=err


def check_photonic(trace,record):
    import strawberryfields as sf
    from strawberryfields import ops
    params=trace["input"];values=nodes(trace)
    for end,key in [(0,"squeezed_covariance"),(1,"source.covariance"),(2,"trained.covariance")]:
        program=sf.Program(2)
        with program.context as q:
            ops.Sgate(params["squeezing"])|q[0]
            ops.Sgate(-params["squeezing"])|q[1]
            if end>=1:ops.BSgate(params["source_angle"],0)|(q[0],q[1])
            if end>=2:ops.BSgate(params["trained_angle"],0)|(q[0],q[1])
        cov=sf.Engine("gaussian").run(program).state.cov()
        err=float(np.max(abs(cov-values[key])));assert err<1e-9
        record[trace["id"]+"."+key+".strawberryfields_error"]=err


def literal_attention(q,k,v,mask,mode):
    """Loop over heads/queries/keys/channels; no vectorized attention helper."""
    out=np.zeros_like(v)
    for b in range(q.shape[0]):
        for h in range(q.shape[1]):
            for i in range(q.shape[2]):
                js=[j for j in range(k.shape[2]) if mask[b,h,i,j]]
                if not js:continue
                s=[sum(q[b,h,i,c]*k[b,h,j,c] for c in range(q.shape[-1]))/np.sqrt(q.shape[-1]) for j in js]
                if mode=="softmax":
                    a=np.exp(np.array(s)-max(s));a/=a.sum()
                    for c in range(v.shape[-1]):out[b,h,i,c]=sum(a[z]*v[b,h,j,c] for z,j in enumerate(js))
                else:
                    for c in range(v.shape[-1]):out[b,h,i,c]=max(s[z]+v[b,h,j,c] for z,j in enumerate(js))
    return out


def literal_moe(x,mask,w,causal=False):
    b,length,d=x.shape
    output=np.zeros_like(x)
    for batch in range(b):
        logits=np.zeros((length,2))
        for i in range(length):
            for e in range(2):
                xv=x[batch,i]/max(np.linalg.norm(x[batch,i]),1e-6)
                kv=w["slot_keys"][e,0]/max(np.linalg.norm(w["slot_keys"][e,0]),1e-6)
                logits[i,e]=sum(xv[c]*kv[c] for c in range(d))
        for i in range(length):
            if not mask[batch,i]:continue
            combine=np.exp(logits[i]-max(logits[i]));combine/=combine.sum()
            for e in range(2):
                ids=[j for j in range(i if causal else length) if mask[batch,j]]
                slot=np.zeros(d)
                if ids:
                    # Upstream causal weights are centered over slots per row;
                    # ordinary dispatch is centered over tokens per slot.
                    weights=np.array([np.exp(logits[j,e]-max(logits[j])) if causal else np.exp(logits[j,e]-max(logits[ids,e])) for j in ids])
                    weights/=max(weights.sum(),1e-6)
                    slot=sum((weight*x[batch,j] for weight,j in zip(weights,ids)),np.zeros(d))
                a=slot@w["expert_w1"][e]+w["expert_b1"][e]
                hidden=.5*a*(1+erf(a/np.sqrt(2)))
                expert=hidden@w["expert_w2"][e]+w["expert_b2"][e]
                output[batch,i]+=combine[e]*expert*(1 if causal else .1)
    return output


def check_classical(trace,record):
    values=nodes(trace)
    w={key.removeprefix("weight."):value for key,value in values.items() if key.startswith("weight.")}
    for layer,mode in enumerate(trace["architecture"]["attention_modes"]):
        p=f"layer{layer}"
        ref=literal_attention(values[p+".query"],values[p+".key"],values[p+".value"],values[p+".legal"],mode)
        err=float(np.max(abs(ref-values[p+".context"])));assert err<1e-9
        record[trace["id"]+f".{p}.literal_attention_error"]=err
        if trace["architecture"]["feedforward"]=="moe":
            ref=literal_moe(values[p+".ff_norm"],values["token_mask"],w,trace["architecture"]["causal"])
            err=float(np.max(abs(ref-values[p+".moe.output"])));assert err<1e-9
            record[trace["id"]+f".{p}.literal_moe_error"]=err


def boundary_checks(record):
    w,x,e,endpoints,mask=C.fixture()
    tokens,_,_=C.tokenizer(w,x,e,endpoints)
    empty=np.zeros_like(mask)
    for mode in ["softmax","tropical","tropical_ring"]:
        a=C.attention(tokens,empty,w,mode)
        assert not np.any(a["context"]) and not np.any(a["winners"]) and not np.any(a["weights"])
        record["all_masked."+mode]=0
    # Exact floating tie set; a near-maximal value must not become a tie.
    z={k:np.zeros_like(v) for k,v in w.items()}
    xx=np.zeros((1,2,C.D));mm=np.ones((1,2),bool)
    a=C.attention(xx,mm,z,"tropical")
    assert np.all(a["winners"])
    z["qkv"][0,2*C.D]=1
    xx[0,0,0]=5e-13
    a=C.attention(xx,mm,z,"tropical")
    assert np.all(a["winners"][0,0,:,0,0]) and not np.any(a["winners"][0,0,:,1,0])
    record["exact_ties_and_near_tie_distinction"]=0
    # Permutation transports token data, validity and causal metadata together.
    permutation=np.array([6,2,0,3,5,1,4])
    ranks=np.array([[0,1,2,2**30,1,2,2]])
    for mode in ["softmax","tropical_ring"]:
        a=C.attention(tokens,mask,w,mode,ranks)
        p=C.attention(tokens[:,permutation],mask[:,permutation],w,mode,ranks[:,permutation])
        err=float(np.max(abs(p["output"]-a["output"][:,permutation])));assert err<1e-9
        record["transported_permutation."+mode]=err
    # Ground-state source/checkpoint bytes may not be modified by replay/tests.
    U=np.diag(1j**np.arange(4));V=np.roll(np.eye(4),-1,axis=0)
    assert np.linalg.norm(V@U-1j*U@V)<1e-12
    assert np.linalg.norm(U@V-1j*V@U)>1 # backwards convention must not flip silently
    record["weyl_convention_negative_control"]=0


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory",type=Path,default=ROOT/"web/data/architecture")
    parser.add_argument("--report",type=Path,default=ROOT/"outputs/checks/2026-11-03-architecture/trace-checks.json")
    args=parser.parse_args();manifest=json.loads((args.directory/"manifest.json").read_text())
    assert subprocess.check_output(["git","-C",str(ROOT/"external/ToricGT"),"rev-parse","HEAD"],text=True).strip()==C.PIN
    assert not subprocess.check_output(["git","-C",str(ROOT/"external/ToricGT"),"status","--porcelain"],text=True).strip()
    def protected():
        paths=list((ROOT/"outputs/experiments").rglob("training.json"))+[ROOT/"outputs/experiments/photonic-pooling/photonic.json"]
        return {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    before=protected();record={};traces=[]
    for entry in manifest["traces"]:
        path=args.directory/entry["file"];raw=path.read_bytes()
        assert hashlib.sha256(raw).hexdigest()==entry["sha256"]
        trace=json.loads(raw);validate(trace);assert trace["id"]==entry["id"]
        for s in [trace["provenance"]["implementation"]]+trace["provenance"].get("upstream_sources",[]):
            assert source(s["path"])==s
        if "checkpoint" in trace["provenance"]:
            for key in ["checkpoint","training_source"]:
                s=trace["provenance"][key];assert source(s["path"])==s
        traces.append(trace)
        if trace["category"]=="photonic-gaussian":check_photonic(trace,record)
        elif trace["provenance"]["kind"]=="trained-checkpoint-replay":check_quantum_backend(trace,record)
        else:check_classical(trace,record)
    for s in manifest["sources"]:assert source(s["path"])==s
    check_two_other_backends(next(t for t in traces if t["id"]=="quantum-convolution-0"),record)
    boundary_checks(record)
    assert before==protected()
    import pennylane,cirq,qiskit,strawberryfields
    report=dict(passed=True,traces=len(traces),trace_checks=sum(len(t["checks"]) for t in traces),
        independent_checks=len(record),errors=record,checkpoint_hashes_before_and_after=before,
        backends=dict(pennylane=pennylane.__version__,cirq=cirq.__version__,qiskit=qiskit.__version__,strawberryfields=strawberryfields.__version__),
        checker=source(__file__),manifest_sha256=hashlib.sha256((args.directory/"manifest.json").read_bytes()).hexdigest(),
        scope="Numerical trace export only; inspector, general Lean formalization and arithmetic bridge remain queued/open")
    args.report.parent.mkdir(parents=True,exist_ok=True)
    args.report.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({k:report[k] for k in ["passed","traces","trace_checks","independent_checks","backends"]},indent=2))


if __name__=="__main__":main()
