#!/usr/bin/env python3
"""Train a shared passive photonic pooling layer with Strawberry Fields.

Family: differently scaled two-mode Gaussian states rotated by one fixed
unknown mixing angle. Objective: minimize the retained output position variance
plus discarded output momentum variance. This recovers a principal-axis
coarse graining, not an interacting field-theory fixed point.
"""
from pathlib import Path
import json
import numpy as np
import strawberryfields as sf
from strawberryfields import ops
ROOT=Path(__file__).resolve().parents[2]
seed=20261103
# Deterministic split over squeezing values; held-out states never enter updates.
rs=np.linspace(.1,.9,16);train=np.array([i for i in range(16) if i%4]);test=np.array([i for i in range(16) if not i%4])
source_angle=.47

def predict(theta,r):
    program=sf.Program(2)
    with program.context as q:
        ops.Sgate(r)|q[0];ops.Sgate(-r)|q[1]
        ops.BSgate(source_angle,0)|(q[0],q[1])
        ops.BSgate(theta,0)|(q[0],q[1])
    covariance=sf.Engine('gaussian').run(program).state.cov()
    # SF covariance ordering: x0,x1,p0,p1, hbar=2.
    return float(covariance[0,0]+covariance[3,3])

def loss(theta,idx):return float(np.mean([predict(theta,float(rs[i])) for i in idx]))
theta=.2;curve=[]
for epoch in range(61):
    curve.append(dict(epoch=epoch,train=loss(theta,train),test=loss(theta,test),theta=theta))
    if epoch==60:break
    eps=1e-5;grad=(loss(theta+eps,train)-loss(theta-eps,train))/(2*eps)
    theta-=.045*grad
out=dict(seed=seed,backend='Strawberry Fields '+sf.__version__+' gaussian CPU',source_angle=source_angle,parameters=1,epochs=60,train_size=len(train),test_size=len(test),objective='recover low-variance principal axes by a shared beamsplitter; finite Gaussian coarse graining',curve=curve,final_angle=theta,analytic_optimum=-source_angle,examples=[dict(squeezing=float(rs[i]),objective=predict(theta,float(rs[i])),optimal=float(2*np.exp(-2*rs[i]))) for i in test])
assert abs(theta+source_angle)<1e-4
for folder in [ROOT/'outputs/experiments/photonic-pooling',ROOT/'web/data']:
 folder.mkdir(parents=True,exist_ok=True);(folder/'photonic.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
