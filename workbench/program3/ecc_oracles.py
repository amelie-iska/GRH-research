"""Finite variable-point addition XOR oracle, including explicit validity.

Complements fixed-base translations. Both input points remain available; result
and validity are XORed into an arbitrary output register, with clean scratch.
The lookup construction is bounded/nonuniform, not a polynomial-size compiler.
"""
import argparse,json,hashlib
from pathlib import Path
import numpy as np
from .ecc import Curve,Builder,count_circuit,execute_words


def compile_oracle(curve):
 w=curve.width;inputs=list(range(2*w));outputs=list(range(2*w,3*w+1));work=list(range(3*w+1,5*w-1));builder=Builder(5*w-1,work);table={}
 for P in curve.points():
  for Q in curve.points():table[curve.encode(P)|(curve.encode(Q)<<w)]=curve.encode(curve.add(P,Q))|(1<<w)
 builder.xor_table(inputs,outputs,table)
 c=dict(schema='grh.ecc.variable-add.v1',curve={'p':curve.p,'a':curve.a,'b':curve.b},qubits=builder.n,inputs=inputs,outputs=outputs,work_wires=work,gates=builder.gates,encoding={'point_bits':w,'infinity_word':curve.infinity,'validity_output_bit':w,'invalid_input_output_value':0},semantics='|P,Q,z,0> -> |P,Q,z XOR (valid,P+Q),0>; invalid point inputs have zero oracle value')
 c['resources']=count_circuit(c);return c,table


def run(output):
 output.mkdir(parents=True,exist_ok=True);curve=Curve();c,table=compile_oracle(curve);n=len(c['inputs']);inputs=np.arange(1<<n,dtype=np.uint64);expected=inputs.copy()
 for k,v in table.items():expected[k]=k|(v<<n)
 actual=execute_words(c['gates'],inputs)
 if not np.array_equal(actual,expected):raise ValueError('Full input-domain point oracle failed')
 rng=np.random.default_rng(741);x=rng.integers(0,1<<n,size=512,dtype=np.uint64);z=rng.integers(0,1<<len(c['outputs']),size=512,dtype=np.uint64);mixed=x|(z<<n);target=mixed.copy()
 for i,k in enumerate(x):target[i]^=np.uint64(table.get(int(k),0)<<n)
 if not np.array_equal(execute_words(c['gates'],mixed),target):raise ValueError('Arbitrary output XOR semantics failed')
 p=output/'variable-point-add.json';p.write_text(json.dumps(c,separators=(',',':'))+'\n');r=dict(schema='grh.variable-add-audit.v1',resources=c['resources'],all_input_words=len(inputs),valid_point_pairs=len(table),invalid_input_words=len(inputs)-len(table),nonzero_output_checks=len(mixed),scratch_clean=True,circuit_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),scope='Exhaustive input domain on zero output, structural XOR-output form plus 512 independent nonzero-output checks. No dense 34-qubit GPU claim.')
 (output/'variable-add-audit.json').write_text(json.dumps(r,indent=2)+'\n');return r

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();print(json.dumps(run(a.output),indent=2))
