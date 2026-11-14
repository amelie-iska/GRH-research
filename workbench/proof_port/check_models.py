"""Executable witnesses for source-proof review, not a numerical UAP proof.

The 2-WL example diagnoses a fixed-order IGN proof route. It is not an upper
bound on every transformer that is allowed to inspect raw absolute identifiers.
All circuit outcomes are checked against an independent Boolean interpreter.
"""
from __future__ import annotations
import argparse, itertools, json, math, random
from collections import Counter
from fractions import Fraction
from pathlib import Path


def graph_pair():
    points=list(itertools.product(range(4),repeat=2))
    steps={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
    rook=[[int(i!=j and (x==u or y==v)) for j,(u,v) in enumerate(points)]for i,(x,y) in enumerate(points)]
    shrikhande=[[int(((u-x)%4,(v-y)%4)in steps)for u,v in points]for x,y in points]
    return rook,shrikhande


def pair_refinement(graphs,rounds=8):
    """Joint-palette ordered-pair WL refinement, with exact finite tuples."""
    colors=[[[0 if i==j else (1 if a[i][j]else 2)for j in range(len(a))]for i in range(len(a))]for a in graphs]
    history=[]
    for step in range(rounds):
        signatures=[]
        for c in colors:
            n=len(c);signatures.append([[(c[i][j],tuple(sorted((c[i][k],c[k][j])for k in range(n))))for j in range(n)]for i in range(n)])
        palette={v:i for i,v in enumerate(sorted({s for g in signatures for row in g for s in row}))}
        colors=[[[palette[s]for s in row]for row in g]for g in signatures]
        hist=[sorted(Counter(x for row in c for x in row).items())for c in colors]
        history.append({'round':step+1,'colors':len(palette),'histograms':hist,'equal':all(h==hist[0]for h in hist)})
    return history


def clique_count(a,k=4):
    return sum(all(a[i][j]for i,j in itertools.combinations(subset,2))for subset in itertools.combinations(range(len(a)),k))


def hull(points):
    p=sorted(set(points))
    if len(p)<=1:return p
    def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    low=[];high=[]
    for x in p:
        while len(low)>1 and cross(low[-2],low[-1],x)<=0:low.pop()
        low.append(x)
    for x in reversed(p):
        while len(high)>1 and cross(high[-2],high[-1],x)<=0:high.pop()
        high.append(x)
    return low[:-1]+high[:-1]


def minkowski(a,b):return hull([(x+u,y+v)for x,y in a for u,v in b])


def softmax_hessian_witness(delta=2.,temperature=1.):
    r=math.exp(-delta/temperature);p=1/(1+r)
    actual=2*p*(1-p)/temperature
    return {'scores':[delta,0.],'temperature':temperature,'hessian_operator_norm':actual,
            'source_claimed_bound':r/temperature,'safe_trace_bound':2*r/temperature,
            'violates_source_bound':actual>r/temperature,
            'scope':'Binary log-sum-exp Hessian; missing factor two in the inspected formula.'}


def relu(x):return max(0,x)
def gate_neural(op,x,y=0):
    and_value=relu(x+y-1)
    if op=='AND':return and_value
    if op=='OR':return x+y-and_value
    if op=='XOR':return x+y-2*and_value
    if op=='NOT':return 1-x
    raise ValueError('Unknown gate')


def circuit(gates,inputs,neural=False,interventions=None):
    if any(type(v)is not int or v not in (0,1)for v in inputs):raise ValueError('Boolean inputs required')
    values=inputs.copy();interventions=interventions or {}
    if any(type(k)is not int or type(v)is not int or v not in (0,1) for k,v in interventions.items()):raise ValueError('Invalid intervention')
    for i,(op,wires)in enumerate(gates,len(inputs)):
        if any(type(j)is not int or not 0<=j<i for j in wires):raise ValueError('Circuit must be acyclic and ordered')
        if op not in ('AND','OR','XOR','NOT') or len(wires)!=(1 if op=='NOT'else 2):raise ValueError('Wrong gate arity')
        x=values[wires[0]];y=values[wires[1]]if len(wires)>1 else 0
        if i in interventions:v=interventions[i]
        elif neural:v=gate_neural(op,x,y)
        else:v=int((x and y)if op=='AND'else (x or y)if op=='OR'else (x!=y)if op=='XOR'else not x)
        values.append(v)
    if any(k<len(inputs)or k>=len(values)for k in interventions):raise ValueError('Intervention must name an actual gate')
    return values


def finite_relu_interpolator(points,outputs):
    if not points or len(points)!=len(outputs)or len({tuple(x)for x in points})!=len(points):raise ValueError('Distinct finite points required')
    dim=len(points[0]);odim=len(outputs[0])
    if any(len(x)!=dim for x in points)or any(len(y)!=odim for y in outputs):raise ValueError('Shape mismatch')
    delta=min((max(abs(a-b)for a,b in zip(x,y))for x,y in itertools.combinations(points,2)),default=Fraction(1))/2
    def evaluate(x):
        if len(x)!=dim:raise ValueError('Input shape mismatch')
        weights=[max(Fraction(0),1-max(abs(a-b)for a,b in zip(x,p))/delta)for p in points]
        return [sum(w*y[j]for w,y in zip(weights,outputs))for j in range(odim)]
    return evaluate


def gate_audit(seed=402,examples=120):
    rng=random.Random(seed);count=0
    for _ in range(examples):
        gates=[]
        for j in range(12):
            op=rng.choice(['AND','OR','XOR','NOT']);gates.append((op,[rng.randrange(4+j)for _ in range(1 if op=='NOT'else 2)]))
        for bits in itertools.product((0,1),repeat=4):
            for interventions in ({},{rng.randrange(4,16):rng.randrange(2)}):
                if circuit(gates,list(bits),True,interventions)!=circuit(gates,list(bits),False,interventions):raise ValueError('Circuit mismatch')
                count+=1
    return count


def report():
    a,b=graph_pair();wl=pair_refinement([a,b]);rng=random.Random(91);polygons=[]
    for _ in range(30):
        p=hull([(rng.randrange(-20,21),rng.randrange(-20,21))for _ in range(16)])
        q=hull([(rng.randrange(-20,21),rng.randrange(-20,21))for _ in range(16)])
        s=minkowski(p,q)
        if len(s)>len(p)+len(q):raise ValueError('Planar bound violated')
        polygons.append([len(p),len(q),len(s)])
    points=[[Fraction(i),Fraction(j)]for i,j in itertools.product(range(3),repeat=2)]
    outputs=[[x[0]**2+2*x[1],x[0]*x[1]]for x in points];f=finite_relu_interpolator(points,outputs)
    exact=all(f(x)==y for x,y in zip(points,outputs))
    return {'schema':'grh.expressivity-witnesses.v1',
      'fixed_order_dependency':{'rook_K4':clique_count(a),'shrikhande_K4':clique_count(b),'pair_refinement':wl,
       'scope':'Fixed-order IGN/2-WL dependency warning, not an upper bound for every raw-ID TokenGT.'},
      'hessian':softmax_hessian_witness(),
      'planar_minkowski':{'cases':polygons,'bound':'For convex polygons, each oriented edge-normal occurs in the union of summand normals, hence vertices <= sum of summand vertices. The general proof, not finite examples alone, excludes quadratic asymptotics for two planar N-gons.'},
      'hard_routing':{'q':[-1e-9,0.,1e-9],'score_argmax_value':[-1.,0.,1.],
       'scope':'Tie-average is zero; one-sided limits disagree. The max potential is continuous but the selected value need not be.'},
      'exact_finite_relu_interpolation':{'points':len(points),'passed':exact},
      'circuit_execution':{'comparisons':gate_audit(),'semantics':'Boolean interpreter versus shared affine/ReLU gates, including gate interventions; constructed execution, not learned understanding.'},
      'Lp_spike':{'supremum':1,'integral_formula':'2/(k*(p+1)) for k>=2 and triangular spike on [0,1]','uniform_convergence':False}}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);args=p.parse_args();r=report();s=json.dumps(r,indent=2)
    if args.output:args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(s+'\n')
    print(s)
