#!/usr/bin/env python3
"""Numerical finite window in the infinite regular {7,3} Poincare tiling.

No compact quotient or closed-surface dessin is inferred from this window.
The browser implementation uses the same circle/reflection formulas.
"""
from math import cos,pi,sqrt,hypot
from pathlib import Path
import json

def edge_circle(a,b):
 r1=(a[0]*a[0]+a[1]*a[1]+1)/2;r2=(b[0]*b[0]+b[1]*b[1]+1)/2
 det=a[0]*b[1]-a[1]*b[0]
 if abs(det)<1e-12:
  length=hypot(*a);return (a[0]/length,a[1]/length),None
 c=((r1*b[1]-r2*a[1])/det,(a[0]*r2-b[0]*r1)/det)
 return c,c[0]*c[0]+c[1]*c[1]-1

def reflect(z,c,r2):
 if r2 is None:
  dot=z[0]*c[0]+z[1]*c[1];return 2*dot*c[0]-z[0],2*dot*c[1]-z[1]
 x=z[0]-c[0];y=z[1]-c[1];n=x*x+y*y
 return c[0]+r2*x/n,c[1]+r2*y/n

def patch(depth=3,cap=450):
 from math import sin
 radius=sqrt(cos(pi/7+pi/3)/cos(pi/7-pi/3))
 vertices=[(radius*cos(2*pi*i/7),radius*sin(2*pi*i/7)) for i in range(7)]
 tiles=[(vertices,0)];seen={(0,0)};residual=0.
 for verts,d in tiles:
  if d>=depth:continue
  for i in range(7):
   c,r2=edge_circle(verts[i],verts[(i+1)%7])
   if r2 is not None:
    assert r2>0
    residual=max(residual,abs((c[0]*c[0]+c[1]*c[1])-r2-1))
   for z in [verts[i],verts[(i+1)%7]]:
    zp=reflect(z,c,r2);residual=max(residual,hypot(zp[0]-z[0],zp[1]-z[1]))
   new=[reflect(z,c,r2) for z in verts]
   if any(hypot(*z)>.995 for z in new):continue
   key=tuple(round(sum(z[j] for z in new)/7,6) for j in [0,1])
   if key in seen:continue
   seen.add(key);tiles.append((new,d+1))
   if len(tiles)>=cap:return tiles,residual
 return tiles,residual
if __name__=='__main__':
 tiles,error=patch();assert error<1e-8
 out=dict(p=7,q=3,depth=3,tile_cap=450,tiles=len(tiles),reflection_fixed_endpoint_residual=error,scope='finite floating-point visualization; infinite tiling specified by reflection construction, no closed quotient certificate')
 dest=Path(__file__).resolve().parents[1]/'outputs/checks/2026-11-03-book/hyperbolic.json';dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
