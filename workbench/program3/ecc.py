"""Complete finite reversible ECC reference with emitted X/CX/CCX circuits.

Affine coordinates and a unique infinity flag are used. Invalid point words are
fixed by every in-place translation. The compiler is a bounded truth-table/
permutation construction, not a scalable cryptanalytic implementation. Every
control and clean-work gate, including coherent decomposition cleanup, is paid.
"""
from __future__ import annotations
from dataclasses import dataclass
from collections import Counter
import argparse,hashlib,itertools,json,math
from pathlib import Path
import numpy as np


def integer(x,lo,hi):
    if type(x)is not int or not lo<=x<=hi:raise ValueError('Integer outside domain')
    return x

@dataclass(frozen=True)
class Curve:
    p:int=7
    a:int=0
    b:int=3
    def __post_init__(self):
        integer(self.p,5,43);integer(self.a,0,self.p-1);integer(self.b,0,self.p-1)
        if any(self.p%d==0 for d in range(2,math.isqrt(self.p)+1))or (4*self.a**3+27*self.b**2)%self.p==0:raise ValueError('Nonsingular prime-field curve required')
    @property
    def bits(self):return self.p.bit_length()
    @property
    def width(self):return 2*self.bits+1
    @property
    def infinity(self):return 1<<(2*self.bits)
    def points(self):return [None]+[(x,y)for x in range(self.p)for y in range(self.p)if (y*y-x**3-self.a*x-self.b)%self.p==0]
    def encode(self,P):
        if P is None:return self.infinity
        if type(P)not in(tuple,list)or len(P)!=2 or any(type(x)is not int or not 0<=x<self.p for x in P)or (P[1]**2-P[0]**3-self.a*P[0]-self.b)%self.p:raise ValueError('Not a curve point')
        return P[0]|(P[1]<<self.bits)
    def decode(self,word):
        integer(word,0,(1<<self.width)-1)
        if word==self.infinity:return None
        mask=(1<<self.bits)-1;P=(word&mask,(word>>self.bits)&mask)
        if word>>(2*self.bits)or self.encode(P)!=word:raise ValueError('Invalid affine/infinity word')
        return P
    def add(self,P,Q):
        self.encode(P);self.encode(Q)
        if P is None:return Q
        if Q is None:return P
        x,y=P;u,v=Q;p=self.p
        if x==u and (y+v)%p==0:return None
        slope=((3*x*x+self.a)*pow(2*y,-1,p)if P==Q else(v-y)*pow((u-x)%p,-1,p))%p
        z=(slope*slope-x-u)%p;return (z,(slope*(x-z)-y)%p)
    def mul(self,k,P):
        if type(k)is not int:raise ValueError('Integer scalar required')
        if k<0:return self.mul(-k,None if P is None else(P[0],-P[1]%self.p))
        out=None
        while k:
            if k&1:out=self.add(out,P)
            P=self.add(P,P);k>>=1
        return out
    def phi(self,P,beta):
        if self.a or not 1<beta<self.p or pow(beta,3,self.p)!=1:raise ValueError('Declared j=0 endomorphism required')
        return None if P is None else(beta*P[0]%self.p,P[1])


class Builder:
    def __init__(self,n,wires_work):
        integer(n,1,62);self.n=n;self.work=list(wires_work);self.gates=[]
        if len(set(self.work))!=len(self.work)or any(type(q)is not int or not 0<=q<n for q in self.work):raise ValueError('Bad work registers')
    def emit(self,target,controls=()):
        wires=list(controls)+[target]
        if len(controls)>2 or len(set(wires))!=len(wires)or any(type(q)is not int or not 0<=q<self.n for q in wires):raise ValueError('Invalid primitive gate')
        self.gates.append(dict(gate=['X','CX','CCX'][len(controls)],target=target,controls=list(controls)))
    def mcx(self,controls,target):
        controls=list(controls);k=len(controls)
        if target in controls or len(set(controls))!=k or set(controls+[target])&set(self.work):raise ValueError('Controls/target overlap scratch')
        if k<=2:self.emit(target,controls);return
        if len(self.work)<k-2:raise ValueError('Insufficient clean workspace')
        before=len(self.gates);self.emit(self.work[0],controls[:2])
        for j in range(2,k-1):self.emit(self.work[j-1],[self.work[j-2],controls[j]])
        compute=self.gates[before:].copy();self.emit(target,[self.work[k-3],controls[-1]])
        self.gates.extend(reversed(compute))
    def match_flip(self,wires,pattern,target,extra=()):
        integer(pattern,0,(1<<len(wires))-1)
        negative=[q for i,q in enumerate(wires)if not pattern>>i&1]
        for q in negative:self.emit(q)
        self.mcx(list(wires)+list(extra),target)
        for q in reversed(negative):self.emit(q)
    def endpoint_swap(self,register,a,b,extra=()):
        if a==b:return
        integer(a,0,(1<<len(register))-1);integer(b,0,(1<<len(register))-1)
        path=[a]
        for i in range(len(register)):
            if (a^b)>>i&1:path.append(path[-1]^(1<<i))
        neighbors=list(zip(path,path[1:]));sequence=neighbors+list(reversed(neighbors[:-1]))
        for u,v in sequence:
            bit=(u^v).bit_length()-1;wires=[q for i,q in enumerate(register)if i!=bit]
            pattern=sum(((u>>i)&1)<<j for j,i in enumerate(i for i in range(len(register))if i!=bit))
            self.match_flip(wires,pattern,register[bit],extra)
    def permutation(self,register,mapping,extra=()):
        if set(mapping)!=set(mapping.values()):raise ValueError('Map is not a permutation on its declared support')
        seen=set()
        for start in sorted(mapping):
            if start in seen:continue
            cycle=[];x=start
            while x not in seen:seen.add(x);cycle.append(x);x=mapping[x]
            if x!=start:raise ValueError('Invalid cycle closure')
            for other in cycle[1:]:self.endpoint_swap(register,cycle[0],other,extra)
    def xor_table(self,inputs,outputs,table):
        if set(inputs)&set(outputs):raise ValueError('Oracle registers overlap')
        for pattern,value in sorted(table.items()):
            integer(value,0,(1<<len(outputs))-1)
            for bit,target in enumerate(outputs):
                if value>>bit&1:self.match_flip(inputs,pattern,target)
    def inverse(self):self.gates.reverse()


def execute_words(gates,words):
    out=np.asarray(words,dtype=np.uint64).copy()
    for g in gates:
        mask=sum(1<<c for c in g['controls']);selected=(out&np.uint64(mask))==mask
        out[selected]^=np.uint64(1<<g['target'])
    return out


def count_circuit(circuit):
    n=integer(circuit['qubits'],1,62);clock=[0]*n;ccx_clock=[0]*n;count=Counter();scratch=set(circuit['work_wires'])
    for g in circuit['gates']:
        op=g['gate'];controls=g['controls'];t=g['target'];wires=controls+[t]
        if op not in('X','CX','CCX')or len(controls)!=('X','CX','CCX').index(op)or len(set(wires))!=len(wires):raise ValueError('Malformed gate stream')
        for q in wires:integer(q,0,n-1)
        count[op]+=1;depth=max(clock[q]for q in wires)+1;td=max(ccx_clock[q]for q in wires)+(op=='CCX')
        for q in wires:clock[q]=depth;ccx_clock[q]=td
    return dict(gates=dict(count),total_gates=sum(count.values()),logical_qubits=n,clean_work_qubits=len(scratch),depth_all_to_all=max(clock),ccx_layers=max(ccx_clock),gate_set='X, CX, CCX; all-to-all connectivity; no routing or error correction charged',physical_qubits=None)


def translation(curve,point):return {curve.encode(P):curve.encode(curve.add(P,point))for P in curve.points()}


def decomposition(curve,G):
    order=next(n for n in range(1,len(curve.points())+1)if curve.mul(n,G)is None)
    beta=next(x for x in range(2,curve.p)if pow(x,3,curve.p)==1);image=curve.phi(G,beta)
    lam=next(k for k in range(order)if curve.mul(k,G)==image)
    for radius in range(1,order):
        candidates={}
        for a,b in itertools.product(range(-radius,radius+1),repeat=2):
            residue=(a+lam*b)%order;score=(max(abs(a),abs(b)),abs(a)+abs(b),a,b)
            if residue not in candidates or score<candidates[residue][0]:candidates[residue]=(score,(a,b))
        if len(candidates)==order:break
    width=radius.bit_length()+1
    return dict(order=order,beta=beta,eigenvalue=lam,radius=radius,signed_width=width,pairs=[candidates[k][1]for k in range(order)],phi_generator=image)


def scalar_circuit(curve,G,variant):
    if variant not in('binary','endomorphism'):raise ValueError('Unknown algorithm')
    info=decomposition(curve,G);s=info['order'].bit_length();w=curve.width;d=2*info['signed_width']if variant=='endomorphism'else 0
    scalar=list(range(s));point=list(range(s,s+w));split=list(range(s+w,s+w+d));work=list(range(s+w+d,s+w+d+max(w-2,s-2)))
    builder=Builder(s+w+d+len(work),work);stages=[]
    def stage(name,start):stages.append(dict(name=name,first_gate=start,last_gate=len(builder.gates),gates=len(builder.gates)-start))
    if variant=='binary':
        for bit,control in enumerate(scalar):
            start=len(builder.gates);builder.permutation(point,translation(curve,curve.mul(1<<bit,G)),[control]);stage('controlled add '+str(1<<bit)+'G',start)
    else:
        k=info['signed_width'];mask=(1<<k)-1;table={i:(info['pairs'][i%info['order']][0]&mask)|((info['pairs'][i%info['order']][1]&mask)<<k)for i in range(1<<s)}
        start=len(builder.gates);builder.xor_table(scalar,split,table);compute=builder.gates.copy();stage('coherent signed decomposition',start)
        for j,P in enumerate([G,info['phi_generator']]):
            for bit in range(k):
                weight=-(1<<bit)if bit==k-1 else 1<<bit;start=len(builder.gates)
                builder.permutation(point,translation(curve,curve.mul(weight,P)),[split[j*k+bit]]);stage(f'component {j}, signed weight {weight}',start)
        start=len(builder.gates);builder.gates.extend(reversed(compute));stage('uncompute decomposition',start)
    result=dict(schema='grh.ecc.circuit.v1',variant=variant,curve={'p':curve.p,'a':curve.a,'b':curve.b},generator=G,encoding={'coordinate_bits':curve.bits,'point_bits':w,'infinity_word':curve.infinity,'invalid_words':'fixed by every translation','endianness':'qubit q is bit q'},scalar_wires=scalar,point_wires=point,decomposition_wires=split,work_wires=work,qubits=builder.n,stages=stages,endomorphism=info,gates=builder.gates)
    result['resources']=count_circuit(result);return result


def field_oracle(p,operation):
    Curve(p,0,1);b=p.bit_length();arity=1 if operation=='inverse'else 2
    if operation not in('add','multiply','inverse'):raise ValueError('Unknown field operation')
    inputs=list(range(arity*b));outputs=list(range(arity*b,arity*b+b+(operation=='inverse')));start=len(inputs)+len(outputs);work=list(range(start,start+max(0,len(inputs)-2)));builder=Builder(start+len(work),work);table={}
    for x in range(p):
        for y in(range(p)if arity==2 else[0]):
            val=(x+y)%p if operation=='add'else x*y%p if operation=='multiply'else(0 if x==0 else pow(x,-1,p)|(1<<b))
            table[x|(y<<b)]=val
    builder.xor_table(inputs,outputs,table)
    c=dict(schema='grh.ecc.field-oracle.v1',p=p,operation=operation,inputs=inputs,outputs=outputs,qubits=builder.n,work_wires=work,gates=builder.gates,semantics='XOR computed output; invalid field inputs map to zero; inverse(0) has validity flag zero')
    c['resources']=count_circuit(c);return c,table


def validate_scalar(curve,c):
    s=len(c['scalar_wires']);w=curve.width;N=1<<(s+w)
    inputs=np.arange(N,dtype=np.uint64);output=execute_words(c['gates'],inputs)
    expected=inputs.copy();valid={curve.encode(P):P for P in curve.points()}
    for word,P in valid.items():
        for k in range(1<<s):expected[k|(word<<s)]=k|(curve.encode(curve.add(P,curve.mul(k,tuple(c['generator']))))<<s)
    if not np.array_equal(output,expected):raise ValueError('Full-domain circuit semantics or ancilla cleanup failed')
    back=execute_words(list(reversed(c['gates'])),output)
    if not np.array_equal(back,inputs):raise ValueError('Circuit inverse failed')
    # Since every emitted gate is a permutation without phases, all basis checks
    # also fix the linear action on their span. Independently sample amplitudes.
    rng=np.random.default_rng(831);choose=rng.choice(N,min(128,N),replace=False);amp=rng.normal(size=len(choose))+1j*rng.normal(size=len(choose));amp/=np.linalg.norm(amp)
    generated=execute_words(c['gates'],choose.astype(np.uint64));target=expected[choose]
    if not np.array_equal(generated,target):raise ValueError('Coherent support mismatch')
    return dict(full_input_words=N,valid_point_scalar_pairs=len(valid)*(1<<s),invalid_point_scalar_pairs=(2**w-len(valid))*(1<<s),all_data_words_checked=True,all_decomposition_and_scratch_return_zero=True,inverse_replay=True,superposition_terms=len(choose),amplitude_norm=float(np.vdot(amp,amp).real),scope='Exhaustive computational-basis semantics on clean-work inputs plus phase-free linear extension and a complex-amplitude support replay; dense GPU is a separate check.')


def run(output):
    output.mkdir(parents=True,exist_ok=True);records=[]
    for curve in [Curve(7,0,3),Curve(13,0,2)]:
        G=curve.points()[1];info=decomposition(curve,G);rows=[]
        for variant in ['binary','endomorphism']:
            c=scalar_circuit(curve,G,variant);v=validate_scalar(curve,c);path=output/f'ecc-p{curve.p}-{variant}.json';path.write_text(json.dumps(c,separators=(',',':'))+'\n')
            parsed=json.loads(path.read_text());counts=count_circuit(parsed)
            if counts!=c['resources']:raise ValueError('Independent serialized gate recount differs')
            rows.append(dict(variant=variant,circuit_file=path.name,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),resources=counts,validation=v,stages=c['stages']))
        records.append(dict(curve={'p':curve.p,'a':0,'b':curve.b},points=curve.points(),generator=G,endomorphism=info,algorithms=rows,endomorphism_ccx_improvement=rows[1]['resources']['gates'].get('CCX',0)<rows[0]['resources']['gates'].get('CCX',0)))
    fields=[]
    for op in ['add','multiply','inverse']:
        c,table=field_oracle(7,op);n=len(c['inputs']);b=len(c['outputs']);inputs=np.arange(1<<(n+b),dtype=np.uint64);got=execute_words(c['gates'],inputs);expected=inputs.copy()
        for x,val in table.items():
            for y in range(1<<b):expected[x|(y<<n)]=x|((y^val)<<n)
        if not np.array_equal(got,expected):raise ValueError('Field XOR oracle failure')
        path=output/f'field-{op}.json';path.write_text(json.dumps(c,separators=(',',':'))+'\n');fields.append(dict(operation=op,resources=c['resources'],checked_input_output_words=len(inputs),scratch_clean=True,circuit_file=path.name))
    report=dict(schema='grh.resource-certified-ecc.v1',curves=records,field_oracles=fields,assumptions={'coordinate_system':'affine x,y plus unique infinity bit; no projective conversion hidden','curve_family':'nonsingular y²=x³+b over the declared small prime fields','base':'public fixed generator; phi(G) is classically computed and recorded','logical_gates':'ideal X/CX/CCX, connectivity unrestricted','error_correction':'not included; no physical-qubit or wall-clock advantage asserted','compiler':'explicit bounded truth-table/Gray-transposition synthesis; exponential in encoding width','ancillas':'all work and decomposition registers initialized and restored to zero','decomposition':'exact finite residue table, coherently computed and uncomputed','success':'deterministic on every word in the declared clean-work domain','purpose':'arithmetical specification and full resource comparison, not a cryptographic-key recovery service'})
    (output/'results.json').write_text(json.dumps(report,indent=2)+'\n');return report

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=run(a.output)
    print(json.dumps({'curves':[{'p':x['curve']['p'],'algorithms':[(v['variant'],v['resources'])for v in x['algorithms']]}for x in r['curves']],'field_oracles':r['field_oracles']},indent=2))
