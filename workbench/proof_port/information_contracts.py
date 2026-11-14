"""Finite exact information/probability controls for the proof port.

A deterministic prefix certificate cannot add Shannon information to the FULL
prefix. It can expose information absent from a restricted context/model. A
likelihood-ratio stopping bound holds under its stated null law, not under an
unvalidated physical noise model.
"""
from fractions import Fraction as Q
from collections import defaultdict
import itertools,math


def conditional_entropy(rows,target,condition):
    groups=defaultdict(lambda:defaultdict(Q));total=Q(0)
    for values,weight in rows:
        weight=Q(weight)
        if weight<0:raise ValueError('Nonnegative weights required')
        groups[tuple(values[i]for i in condition)][tuple(values[i]for i in target)]+=weight;total+=weight
    if total!=1:raise ValueError('Probability must sum to one')
    answer=0.
    for counts in groups.values():
        mass=sum(counts.values())
        for p in counts.values():
            if p:answer-=float(p)*math.log2(float(p/mass))
    return answer


def deterministic_prefix_example():
    # Columns are prefix bit 0, prefix bit 1, target parity, certificate parity.
    rows=[((a,b,a^b,a^b),Q(1,4))for a,b in itertools.product((0,1),repeat=2)]
    full=conditional_entropy(rows,[2],[0,1]);augmented=conditional_entropy(rows,[2],[0,1,3])
    restricted=conditional_entropy(rows,[2],[0]);restricted_augmented=conditional_entropy(rows,[2],[0,3])
    return dict(full_prefix_bits=full,full_prefix_plus_certificate_bits=augmented,
                restricted_context_bits=restricted,restricted_plus_certificate_bits=restricted_augmented,
                scope='Exact finite distribution; deterministic preprocessing reveals no additional information beyond its full input, but can aid a restricted decoder.')


def finite_stopping_check(horizon=10,alpha=Q(1,20)):
    if type(horizon)is not int or not 1<=horizon<=14 or not 0<alpha<=1:raise ValueError('Bounded horizon and alpha required')
    crossed_p=Q(0);crossed_q=Q(0);leaves=0
    def visit(history,p,q):
        nonlocal crossed_p,crossed_q,leaves
        if q/p>=1/alpha:crossed_p+=p;crossed_q+=q;leaves+=1;return
        if len(history)==horizon:return
        # The alternative is predictable: it sees history only.
        prob_one=Q(3,4)if sum(history)%2==0 else Q(1,4)
        visit(history+(0,),p/2,q*(1-prob_one));visit(history+(1,),p/2,q*prob_one)
    visit((),Q(1),Q(1))
    if crossed_q>1 or crossed_p>alpha*crossed_q or crossed_p>alpha:raise ValueError('Finite first-crossing inequality failed')
    return dict(horizon=horizon,alpha=str(alpha),null_first_crossing_probability=str(crossed_p),alternative_prefix_mass=str(crossed_q),first_crossing_prefixes=leaves,
                scope='Exact binary reference under the declared fair-coin null and predictable alternative. Not calibration of measured cosmological/physiological data.')
