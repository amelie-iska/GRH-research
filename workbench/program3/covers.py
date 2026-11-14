"""Finite voltage covers with relation, order and neural transport checks.

A bound-quiver cover, a cellular surface cover and a network pullback are
separately specified. Zero monomial relations lift pathwise. A nonzero integral
relation additionally needs compatible endpoints/voltages; reduction mod pi can
remove this requirement and therefore lose information.
"""
from __future__ import annotations
from fractions import Fraction as Q
import argparse,itertools,json,math,sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from contracts import gentle_check


def lift_quiver(vertices,arrows,relations,degree,voltages):
    if type(degree)is not int or not 1<=degree<=16 or len(voltages)!=len(arrows)or any(type(x)is not int for x in voltages):raise ValueError('Bounded integral voltage data required')
    base=gentle_check(vertices,arrows,relations)
    if not base['gentle']:raise ValueError('Base must satisfy finite gentle conditions')
    lifted=[]
    for i,(u,v)in enumerate(arrows):
        for sheet in range(degree):lifted.append([u*degree+sheet,v*degree+(sheet+voltages[i])%degree])
    rel=[]
    for a,b in relations:
        for sheet in range(degree):rel.append([a*degree+sheet,b*degree+(sheet+voltages[a])%degree])
    verdict=gentle_check(vertices*degree,lifted,rel)
    if not verdict['gentle']:raise ValueError('Lifted gentle conditions failed')
    for v in range(vertices):
        for s in range(degree):
            out=[j//degree for j,e in enumerate(lifted)if e[0]==v*degree+s];inn=[j//degree for j,e in enumerate(lifted)if e[1]==v*degree+s]
            if sorted(out)!=[j for j,e in enumerate(arrows)if e[0]==v]or sorted(inn)!=[j for j,e in enumerate(arrows)if e[1]==v]:raise ValueError('Star bijection failed')
    return dict(base_vertices=vertices,degree=degree,base_arrows=arrows,base_relations=relations,voltages=[v%degree for v in voltages],vertices=vertices*degree,arrows=lifted,relations=rel,base_gentle=base,lifted_gentle=verdict,local_star_bijections=True)


def adjacency(n,arrows):
    a=np.zeros((n,n))
    for u,v in arrows:a[v,u]+=1
    return a


def lift_matrix(n,degree):return np.repeat(np.eye(n),degree,axis=0)


def softmax(x,axis=-1):
    e=np.exp(x-np.max(x,axis=axis,keepdims=True));return e/e.sum(axis=axis,keepdims=True)


def global_attention(x):
    scores=x@x.T/math.sqrt(x.shape[1]);return softmax(scores)@x


def maxplus_attention(x):
    scores=x@x.T/math.sqrt(x.shape[1]);return (scores[:,:,None]+x[None,:,:]).max(axis=1)-scores.max(axis=1)[:,None]


def local_layer(x,a):
    degree=np.maximum(a.sum(1,keepdims=True),1);return np.maximum(0,.4*x+.6*(a@x)/degree)


def order_voltage_check(degree,up,down,uniformizer):
    if type(degree)is not int or not 1<=degree<=16 or any(type(v)is not int for v in [up,down,uniformizer]):raise ValueError('Integral finite data required')
    shift=np.roll(np.eye(degree,dtype=object),up+down,axis=0)
    residual=uniformizer*(shift-np.eye(degree,dtype=object))
    return dict(degree=degree,up_voltage=up%degree,down_voltage=down%degree,cycle_voltage=(up+down)%degree,uniformizer=uniformizer,relation_residual=residual.tolist(),relation_preserved=bool(np.all(residual==0)),scope='Matrix form of uv=pi e on a specified lifted sheet module. A zero special-fiber relation need not lift to this same integral relation.')


def surface_cover(base_x=3,base_y=3,degree=2):
    if type(degree)is not int or not 1<=degree<=8:raise ValueError('Degree out of range')
    # Two directed oriented edge roles, before forgetting the cell structure.
    def cells(nx,ny):
        index=lambda x,y:(y%ny)*nx+(x%nx);edges=[];faces=[]
        for y in range(ny):
            for x in range(nx):edges.append([index(x,y),index(x+1,y)])
        for y in range(ny):
            for x in range(nx):edges.append([index(x,y),index(x,y+1)])
        V=nx*ny
        for y in range(ny):
            for x in range(nx):faces.append([[index(x,y),1],[V+index(x+1,y),1],[index(x,y+1),-1],[V+index(x,y),-1]])
        d1=np.zeros((V,2*V),dtype=int);d2=np.zeros((2*V,V),dtype=int)
        for j,(u,v)in enumerate(edges):d1[u,j]-=1;d1[v,j]+=1
        for f,terms in enumerate(faces):
            for e,s in terms:d2[e,f]+=s
        return edges,faces,d1,d2
    nx=base_x*degree;ny=base_y;base=cells(base_x,base_y);cover=cells(nx,ny)
    vertex_map=[(i//nx)*base_x+(i%nx)%base_x for i in range(nx*ny)];edge_map=[]
    for role in range(2):edge_map.extend([role*base_x*base_y+vertex_map[i]for i in range(nx*ny)])
    face_map=vertex_map.copy()
    U0=np.eye(base_x*base_y)[vertex_map];U1=np.eye(2*base_x*base_y)[edge_map];U2=np.eye(base_x*base_y)[face_map]
    errors=[np.max(abs(cover[2].T@U0-U1@base[2].T)),np.max(abs(cover[3].T@U1-U2@base[3].T)),np.max(abs(cover[2]@cover[3]))]
    if max(errors)!=0:raise ValueError('Cellular pullback or boundary relation failed')
    return dict(base_dimensions=[base_x,base_y],cover_dimensions=[nx,ny],degree=degree,base_cells=[base_x*base_y,2*base_x*base_y,base_x*base_y],cover_cells=[nx*ny,2*nx*ny,nx*ny],genus_base=1,genus_cover=1,vertex_map=vertex_map,edge_map=edge_map,face_map=face_map,chain_pullback_errors=[float(x)for x in errors],orientation_preserved=True,scope='Explicit unramified rectangular torus cellulation cover. Not a general automatic lift of marked/branched surface data.')


def run(output):
    rng=np.random.default_rng(29017);rows=[]
    for d in (2,3,5):
        c=lift_quiver(3,[[0,1],[1,2],[2,0]],[[0,1],[1,2],[2,0]],d,[0,0,1]);U=lift_matrix(3,d);P=U.T/d;A=adjacency(3,c['base_arrows']);B=adjacency(3*d,c['arrows']);x=rng.normal(size=(3,4));lift=U@x
        errors=dict(left_inverse=float(np.max(abs(P@U-np.eye(3)))),projection=float(np.max(abs((U@P)@(U@P)-U@P))),directed_intertwiner=float(np.max(abs(B@U-U@A))),local_layer=float(np.max(abs(local_layer(lift,B)-U@local_layer(x,A)))),global_softmax=float(np.max(abs(global_attention(lift)-U@global_attention(x)))),global_maxplus=float(np.max(abs(maxplus_attention(lift)-U@maxplus_attention(x)))))
        # Arbitrary per-sheet IDs break descent. This is an explicit negative control.
        labelled=lift.copy();labelled[:,0]+=np.arange(3*d)/(3*d)
        broken=float(np.max(abs(global_attention(labelled)-U@P@global_attention(labelled))))
        if max(errors.values())>1e-12 or broken<1e-4:raise ValueError('Neural covering audit failed')
        c.update(errors=errors,absolute_identifier_counterexample=broken,base_features=x.tolist(),lifted_features=lift.tolist(),local_outputs=local_layer(lift,B).tolist());rows.append(c)
    orders=[order_voltage_check(2,1,0,3),order_voltage_check(2,1,0,0),order_voltage_check(2,1,1,3)]
    result=dict(schema='grh.covering-network.v1',quiver_covers=rows,surface_covers=[surface_cover(degree=d)for d in(2,3)],integral_relation_checks=orders,modular_average_counterexample={'field_characteristic':2,'cover_degree':2,'sum_of_constant_ones':0,'required_reynolds_denominator_invertible':False},theory='Finite local bijections transport monomial relations and tied local operations. Uniform replicated keys cancel in normalized attention. Fiber averaging requires an invertible cover degree; arbitrary identifiers or nonzero-voltage integral relations can obstruct descent.')
    output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(result,indent=2)+'\n');return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=run(a.output);print(json.dumps({'covers':[{'degree':x['degree'],'errors':x['errors'],'identifier_failure':x['absolute_identifier_counterexample']}for x in r['quiver_covers']],'order_checks':r['integral_relation_checks']},indent=2))
