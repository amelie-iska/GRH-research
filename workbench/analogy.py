"""Directed analogy witnesses and finite ground-rule deduction.

A graph-mapping witness checks syntax and declared relation words, not equality
of unknown physical laws. Semantic commutation requires an additional proof or
measured error bound. Retrieval scores alone never become deductions.
"""
from __future__ import annotations
from dataclasses import dataclass
import math

@dataclass(frozen=True)
class Memory:
    identity:str
    groups:frozenset[str]
    split:str
    encoder:str
    key:tuple[float,...]


def retrieve(query:tuple[float,...],groups:frozenset[str],encoder:str,bank:list[Memory],k:int=4):
    if type(k)is not int or k<1 or not groups or not query or not all(math.isfinite(x) for x in query):raise ValueError('Explicit query/groups and finite bounded request required')
    out=[]
    for x in bank:
        if x.split!='train':raise ValueError('Memory bank must contain training objects only')
        if x.encoder!=encoder:raise ValueError('Stale encoder/codebook identity')
        if len(x.key)!=len(query) or not all(math.isfinite(v) for v in x.key):raise ValueError('Invalid embedding')
        if groups & x.groups:continue
        out.append((sum((a-b)**2 for a,b in zip(query,x.key)),x.identity))
    return sorted(out)[:k]


def verify_mapping(source_nodes:dict,target_nodes:dict,source_edges:dict,target_edges:dict,node_map:dict,paths:dict,relation_words:dict)->bool:
    if set(node_map)!=set(source_nodes) or set(paths)!=set(source_edges):raise ValueError('Incomplete node or branch coverage')
    if len(set(node_map.values()))!=len(node_map):raise ValueError('This contract requires injective boundary vertices')
    if any(v not in target_nodes or source_nodes[u]!=target_nodes[v] for u,v in node_map.items()):raise ValueError('Node type mismatch')
    for key,(u,v,relation) in source_edges.items():
        path=paths[key]
        if not isinstance(path,list) or not path or any(e not in target_edges for e in path):raise ValueError('Explicit nonempty target path required')
        edges=[target_edges[e] for e in path]
        if edges[0][0]!=node_map[u] or edges[-1][1]!=node_map[v] or any(a[1]!=b[0] for a,b in zip(edges,edges[1:])):raise ValueError('Direction or path boundary mismatch')
        if tuple(e[2] for e in edges) not in relation_words.get(relation,set()):raise ValueError('Unlicensed relation composition')
    return True


def verify_deduction(initial:frozenset[str],rules:dict,steps:list[tuple[str,str]])->frozenset[str]:
    known=set(initial)
    if len(steps)>10000:raise ValueError('Derivation budget exceeded')
    for rule,claim in steps:
        if rule not in rules:raise ValueError('Unknown rule')
        premises,conclusion=rules[rule]
        if claim!=conclusion or not set(premises)<=known:raise ValueError('Unproved premise or wrong conclusion')
        known.add(claim)
    return frozenset(known)
