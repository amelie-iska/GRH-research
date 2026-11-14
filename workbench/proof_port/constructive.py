"""Exact positive constructions supporting the graph-to-graph proof repair.

These are constructed mechanisms, not trained-network benchmarks. The attention
weights below are exactly softmax(log(2) on the designated identifier, 0 elsewhere).
"""
from fractions import Fraction as Q
import itertools


def gather(features):
    if not features or not features[0] or any(len(x)!=len(features[0])for x in features):raise ValueError('Nonempty rectangular features')
    x=[[Q(v)for v in row]for row in features];n=len(x);d=len(x[0])
    total=[sum(row[c]for row in x)for c in range(d)]
    mean=[v/n for v in total]
    heads=[[(total[c]+row[c])/(n+1)for c in range(d)]for row in x]
    recovered=[[(n+1)*row[c]-n*mean[c]for c in range(d)]for row in heads]
    return {'uniform_head':mean,'identifier_heads':heads,'recovered':recovered}


def permute_matrix(a,p):
    if sorted(p)!=list(range(len(a)))or any(len(row)!=len(a)for row in a):raise ValueError('Bad permutation/matrix')
    # New index p[i] receives old index i.
    b=[[0]*len(a)for _ in a]
    for i in range(len(a)):
        for j in range(len(a)):b[p[i]][p[j]]=a[i][j]
    return b


def reynolds_node_map(base,a):
    n=len(a);out=[Q(0)]*n;count=0
    if not 1<=n<=7:raise ValueError('Explicit factorial resource bound')
    for p in itertools.permutations(range(n)):
        y=base(permute_matrix(a,p))
        if len(y)!=n:raise ValueError('Output action dimension mismatch')
        for i in range(n):out[i]+=Q(y[p[i]])
        count+=1
    return [v/count for v in out]


def square_spline(x,knots):
    x=Q(x);t=[Q(v)for v in knots]
    if len(t)<2 or any(a>=b for a,b in zip(t,t[1:]))or not t[0]<=x<=t[-1]:raise ValueError('Increasing covering knots required')
    slopes=[a+b for a,b in zip(t,t[1:])]
    value=t[0]**2+slopes[0]*(x-t[0])
    for i in range(1,len(slopes)):value+=(slopes[i]-slopes[i-1])*max(Q(0),x-t[i])
    return value


def product_spline(x,y,knots):
    return (square_spline(Q(x)+Q(y),knots)-square_spline(Q(x)-Q(y),knots))/4


def select_slot(value,bit,bound):
    value,bit,bound=Q(value),Q(bit),Q(bound)
    if bit not in (0,1)or bound<0 or abs(value)>bound:raise ValueError('Bounded value and one-hot bit required')
    return max(Q(0),value+bound*bit)-max(Q(0),value-bound*bit)-bound*bit
