"""NumPy-only channel reference, usable in the isolated cuQuantum environment.

This independent basis-index implementation avoids importing the training stack
into the GPU runtime. Little-endian qubit q is bit q. Partial trace is explicit.
"""
import itertools,math
import numpy as np


def lifted_gates(theta):
 t=np.asarray(theta,dtype=float)
 if t.shape!=(6,)or not np.all(np.isfinite(t)):raise ValueError('Six finite angles required')
 gates=[]
 for active,params in [([0,1,2,3],t[:3]),([0,2],t[3:])]:
  for i in range(0,len(active),2):
   keep,discard=active[i:i+2]
   gates.extend([dict(gate='RY',target=keep,angle=float(params[0])),dict(gate='RY',target=discard,angle=float(params[1])),dict(gate='CX',control=keep,target=discard),dict(gate='RY',target=keep,angle=float(params[2]))])
 return gates


def unitary(gates,n=4):
 u=np.eye(1<<n,dtype=complex)
 for g in gates:
  t=g['target'];bit=1<<t
  if g['gate']=='CX':
   for i in range(1<<n):
    if (i>>g['control'])&1 and not(i&bit):u[[i,i|bit]]=u[[i|bit,i]]
  elif g['gate']=='RY':
   c=math.cos(g['angle']/2);s=math.sin(g['angle']/2)
   for i in range(1<<n):
    if not(i&bit):a=u[i].copy();b=u[i|bit].copy();u[i]=c*a-s*b;u[i|bit]=s*a+c*b
  else:raise ValueError('Unexpected gate')
 return u


def hierarchy_kraus(theta):
 gates=lifted_gates(theta);u=unitary(gates);ks=[]
 for discard in range(8):
  select=np.zeros((2,16))
  for keep in range(2):select[keep,keep|(discard<<1)]=1
  ks.append(select@u)
 return None,None,ks


def channel(rho,kraus):return sum(k@rho@k.conj().T for k in kraus)


def partial_trace_np(rho,keep,n):
 keep=list(keep);discard=[q for q in range(n)if q not in keep];out=np.zeros((1<<len(keep),)*2,complex)
 for i,j in itertools.product(range(1<<len(keep)),repeat=2):
  for d in range(1<<len(discard)):
   rest=sum(((d>>r)&1)<<q for r,q in enumerate(discard));a=rest|sum(((i>>r)&1)<<q for r,q in enumerate(keep));b=rest|sum(((j>>r)&1)<<q for r,q in enumerate(keep));out[i,j]+=rho[a,b]
 return out
