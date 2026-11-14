"""Uniform reversible field XOR oracles, without input-table synthesis.

Carry/borrow, schoolbook product and constant-divisor long division are emitted
as X/CX/CCX. Compute/copy/uncompute restores every work wire. This reference uses
polynomial saved work, not the low-ancilla Cuccaro construction.
"""
from __future__ import annotations
import argparse,hashlib,json,math
from collections import Counter
from pathlib import Path
import numpy as np
ZERO,ONE=-1,-2

class BooleanCompiler:
 def __init__(self,inputs,outputs):
  self.inputs,self.outputs=inputs,outputs;self.start=inputs+outputs;self.next=self.start;self.compute=[]
 def allocate(self):
  q=self.next;self.next+=1;return q
 def not_(self,a):return self.xor(a,ONE)
 def xor(self,a,b):
  if a==b:return ZERO
  if a==ZERO:return b
  if b==ZERO:return a
  q=self.allocate()
  for x in (a,b):self.compute.append((q,)if x==ONE else(x,q))
  return q
 def and_(self,a,b):
  if ZERO in(a,b):return ZERO
  if a==ONE:return b
  if b==ONE:return a
  if a==b:return a
  q=self.allocate();self.compute.append((a,b,q));return q
 def select(self,condition,yes,no):return[self.xor(b,self.and_(condition,self.xor(a,b)))for a,b in zip(yes,no)]
 @staticmethod
 def constant(value,width):return[ONE if value>>i&1 else ZERO for i in range(width)]
 def add(self,a,b):
  if len(a)!=len(b):raise ValueError('Mismatched bit widths')
  out=[];carry=ZERO
  for x,y in zip(a,b):
   parity=self.xor(x,y);out.append(self.xor(parity,carry));carry=self.xor(self.and_(x,y),self.and_(parity,carry))
  return out,carry
 def subtract(self,a,b):
  if len(a)!=len(b):raise ValueError('Mismatched bit widths')
  out=[];borrow=ZERO
  for x,y in zip(a,b):
   parity=self.xor(x,y);out.append(self.xor(parity,borrow));borrow=self.xor(self.and_(self.not_(x),y),self.and_(self.not_(parity),borrow))
  return out,borrow
 def less_than(self,a,p):return self.subtract(a,self.constant(p,len(a)))[1]
 def reduce(self,bits,p,n):
  remainder=[ZERO]*(n+1);divisor=self.constant(p,n+1)
  for bit in reversed(bits):
   shifted=[bit]+remainder[:n];difference,borrow=self.subtract(shifted,divisor);remainder=self.select(self.not_(borrow),difference,shifted)
  return remainder[:n]
 def multiply_mod(self,a,b,p):
  n=len(a);acc=[ZERO]*(2*n)
  for j,y in enumerate(b):
   row=[ZERO]*j+[self.and_(x,y)for x in a]+[ZERO]*(n-j);acc,_=self.add(acc,row)
  return self.reduce(acc,p,n)
 def finish(self,result):
  if len(result)!=self.outputs:raise ValueError('Output width mismatch')
  copied=[]
  for i,x in enumerate(result):
   if x!=ZERO:copied.append((self.inputs+i,)if x==ONE else(x,self.inputs+i))
  return self.compute+copied+list(reversed(self.compute))

def compile_oracle(p,operation):
 if type(p)is not int or not 3<=p<=65521 or any(p%d==0 for d in range(2,math.isqrt(p)+1)):raise ValueError('Declared odd prime 3..65521 required')
 if operation not in('add','multiply','inverse'):raise ValueError('Unknown operation')
 n=p.bit_length();arity=1 if operation=='inverse'else 2
 if operation=='inverse'and n>8:raise ValueError('Inversion reference capped at 8 bits')
 b=BooleanCompiler(arity*n,n+1);x=list(range(n));y=list(range(n,2*n));valid=b.less_than(x,p)
 if arity==2:valid=b.and_(valid,b.less_than(y,p))
 if operation=='add':
  total,carry=b.add(x,y);total.append(carry);diff,borrow=b.subtract(total,b.constant(p,n+1));out=b.select(b.not_(borrow),diff,total)[:n]
 elif operation=='multiply':out=b.multiply_mod(x,y,p)
 else:
  nonzero=ZERO
  for bit in x:nonzero=b.xor(b.xor(nonzero,bit),b.and_(nonzero,bit))
  valid=b.and_(valid,nonzero);out=b.constant(1,n)
  for bit in bin(p-2)[2:]:
   out=b.multiply_mod(out,out,p)
   if bit=='1':out=b.multiply_mod(out,x,p)
 answer=[b.and_(valid,q)for q in out]+[valid];gates=b.finish(answer);count=Counter(('X','CX','CCX')[len(g)-1]for g in gates);clock=[0]*b.next
 for gate in gates:
  depth=1+max(clock[q]for q in gate)
  for q in gate:clock[q]=depth
 return {'schema':'grh.uniform-field-oracle.v1','p':p,'bits':n,'operation':operation,'input_bits':arity*n,'output_bits':n+1,'qubits':b.next,'scratch_start':b.start,'gates':gates,'resources':{'gate_counts':dict(count),'total_gates':len(gates),'qubits':b.next,'clean_scratch':b.next-b.start,'all_to_all_depth':max(clock)},'specification':'Input preserved; output XOR (field result + 2^n validity); invalid inputs and inverse(0) contribute zero; scratch restored.','construction':'Uniform carry/borrow, schoolbook multiplication, binary long division, Fermat inversion, compute/copy/uncompute. No input enumeration in generator.','scope':'Ideal logical X/CX/CCX; no routing, fault tolerance, low-ancilla optimality or complete large-field elliptic scalar multiplication claim.'}

def replay(c,inputs,initial_output=None):
 inputs=np.asarray(inputs,dtype=np.uint64)
 if initial_output is None:initial_output=np.zeros(len(inputs),dtype=np.uint64)
 initial_output=np.asarray(initial_output,dtype=np.uint64)
 if inputs.ndim!=1 or initial_output.shape!=inputs.shape or np.any(inputs>=2**c['input_bits'])or np.any(initial_output>=2**c['output_bits']):raise ValueError('Register outside domain')
 state=np.zeros((c['qubits'],len(inputs)),dtype=np.bool_)
 for j in range(c['input_bits']):state[j]=(inputs>>j)&1
 for j in range(c['output_bits']):state[c['input_bits']+j]=(initial_output>>j)&1
 for gate in c['gates']:
  if len(gate)==1:state[gate[-1]]^=True
  elif len(gate)==2:state[gate[-1]]^=state[gate[0]]
  else:state[gate[-1]]^=state[gate[0]]&state[gate[1]]
 if state[c['scratch_start']:].any():raise AssertionError('Ancilla cleanup failed')
 preserved=np.zeros(len(inputs),dtype=np.uint64);out=np.zeros(len(inputs),dtype=np.uint64)
 for j in range(c['input_bits']):preserved|=state[j].astype(np.uint64)<<j
 for j in range(c['output_bits']):out|=state[c['input_bits']+j].astype(np.uint64)<<j
 if not np.array_equal(preserved,inputs):raise AssertionError('Inputs changed')
 return out

def expected(c,inputs):
 p,n=c['p'],c['bits'];answers=[]
 for raw in inputs:
  x=int(raw)&(2**n-1);y=int(raw)>>n
  if x>=p or(c['operation']!='inverse'and y>=p)or(c['operation']=='inverse'and x==0):val=0
  else:
   f=(x+y)%p if c['operation']=='add'else x*y%p if c['operation']=='multiply'else pow(x,-1,p);val=f|(1<<n)
  answers.append(val)
 return np.array(answers,dtype=np.uint64)

def run(output):
 output.mkdir(parents=True,exist_ok=True);rng=np.random.default_rng(2026111404);records=[]
 for p in(7,13,31,251,65521):
  for op in('add','multiply','inverse'):
   if op=='inverse'and p.bit_length()>8:continue
   c=compile_oracle(p,op);exhaustive=c['input_bits']<=10;inputs=np.arange(2**c['input_bits'],dtype=np.uint64)if exhaustive else rng.integers(0,2**c['input_bits'],size=96,dtype=np.uint64)
   n=c['bits'];endpoints=[0,p-1,p,(1<<n)-1];extra=endpoints if op=='inverse'else[x|(y<<n)for x in endpoints for y in endpoints];inputs=np.unique(np.concatenate([inputs,np.array(extra,dtype=np.uint64)]));z=rng.integers(0,2**c['output_bits'],size=len(inputs),dtype=np.uint64);got=replay(c,inputs,z)
   if not np.array_equal(got,z^expected(c,inputs)):raise AssertionError((p,op,'modular specification failed'))
   if not np.array_equal(replay(c,inputs,got),z):raise AssertionError('XOR involution failed')
   row={k:v for k,v in c.items()if k!='gates'};row.update(tested_words=len(inputs),exhaustive_input_domain=exhaustive,arbitrary_output_replay=True,clean_scratch=True);raw=json.dumps(c,separators=(',',':')).encode();row['circuit_sha256']=hashlib.sha256(raw).hexdigest()
   if p in(7,13):
    name=f'field-{p}-{op}.json';(output/name).write_bytes(raw);row['emitted_circuit']=name
   records.append(row)
 report={'schema':'grh.uniform-arithmetic-study.v1','seed':2026111404,'records':records,'complexity':'For n-bit modulus: addition O(n) gates/work, multiplication O(n^2), exponent inversion O(n^3); reverse cleanup doubles compute cost.','test_scope':'Exhaustive input domains through 10 input bits, seeded arbitrary output per input and explicit boundaries; wider instances sampled.','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()};(output/'results.json').write_text(json.dumps(report,indent=2)+'\n');return report

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=run(a.output);print(json.dumps([{'p':x['p'],'op':x['operation'],'gates':x['resources']['total_gates'],'scratch':x['resources']['clean_scratch'],'tests':x['tested_words']}for x in r['records']],indent=2))
