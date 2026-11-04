#!/usr/bin/env python3
"""Finite generative quantum example from the actual learned coarse action.

Classically computed32 amplitudes; no efficient many-body preparation claim.
Born samples have the learned classical Gibbs law. Dephasing gives the mixed
Gibbs density; the initial coherent pure state itself is not that density.
"""
from pathlib import Path
import json
import numpy as np
import pennylane as qml
from scipy.special import logsumexp
ROOT=Path(__file__).resolve().parents[2]
def main():
 seed=20261103;model=json.loads((ROOT/'outputs/experiments/actual-rg/training.json').read_text());sample=model['examples'][0]
 v=np.array(sample['predicted_logweights']);p=np.exp(v-logsumexp(v));amplitudes=np.sqrt(p)
 dev=qml.device('default.qubit',wires=5,shots=None)
 @qml.qnode(dev)
 def probabilities():qml.StatePrep(amplitudes,wires=range(5));return qml.probs(wires=range(5))
 analytical=np.asarray(probabilities());err=float(np.max(abs(analytical-p)));assert err<1e-12
 mixed=qml.device('default.mixed',wires=5,shots=None)
 @qml.qnode(mixed)
 def dephased():
  qml.StatePrep(amplitudes,wires=range(5))
  for q in range(5):qml.QubitChannel([np.diag([1.,0.]),np.diag([0.,1.])],wires=q)
  return qml.density_matrix(wires=range(5))
 rho=np.asarray(dephased());dephase_error=float(np.max(abs(rho-np.diag(p))));assert dephase_error<1e-10
 shots=4096;sampledev=qml.device('default.qubit',wires=5,shots=shots,seed=seed)
 @qml.qnode(sampledev)
 def draw():qml.StatePrep(amplitudes,wires=range(5));return qml.sample(wires=range(5))
 bits=np.asarray(draw(),int);values=bits@(2**np.arange(4,-1,-1));hist=np.bincount(values,minlength=32)/shots
 spin=1-2*((np.arange(32)[:,None]>>np.arange(4,-1,-1))&1)
 expected=p@spin;empirical=(1-2*bits).mean(0);delta=.05
 report=dict(seed=seed,shots=shots,physical_retained_white_sites=5,probabilities=p.tolist(),empirical_probabilities=hist.tolist(),expected_magnetizations=expected.tolist(),sample_magnetizations=empirical.tolist(),
  max_magnetization_sampling_error=float(max(abs(expected-empirical))),simultaneous_95pct_Hoeffding_radius=float(np.sqrt(2*np.log(10/delta)/shots)),born_probability_error=err,dephased_density_error=dephase_error,
  scope='Executed finite5qubit state preparation/dephasing/Born sampling from learned full RG action;32 amplitudes computed classically, no speedup or mixed-Gibbs preparation inferred from a pure state alone')
 (ROOT/'outputs/experiments/actual-rg/sampling.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
