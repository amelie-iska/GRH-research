#!/usr/bin/env python3
"""Render publication figures from saved experiment data, with no training."""
from pathlib import Path
import json,numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'book/figures';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'figure.dpi':160})
data=json.loads((ROOT/'outputs/experiments/renormalization-pennylane/training.json').read_text())
fig,axs=plt.subplots(1,3,figsize=(12,3.3),constrained_layout=True)
for ax,m in zip(axs,data['models']):
 for key,c in [('train','#145e4d'),('test','#c16b37')]:ax.semilogy([r['epoch'] for r in m['curve']],[r[key] for r in m['curve']],color=c,label=key)
 ax.set_title(m['name'].replace('Quantum-feature ','').replace('Shared quantum ','').replace('Four-qubit ',''));ax.set_xlabel('Epoch');ax.set_ylabel('Loss');ax.legend(frameon=False)
fig.savefig(OUT/'training-curves.pdf');plt.close(fig)
photo=json.loads((ROOT/'outputs/experiments/photonic-pooling/photonic.json').read_text())
fig,ax=plt.subplots(figsize=(6,3));ax.plot([r['epoch'] for r in photo['curve']],[r['theta'] for r in photo['curve']],color='#145e4d');ax.axhline(photo['analytic_optimum'],ls='--',color='#c16b37',label='Known optimum');ax.set_xlabel('Epoch');ax.set_ylabel('Learned beamsplitter angle');ax.legend();fig.tight_layout();fig.savefig(OUT/'photonic-angle.pdf');plt.close(fig)
fig=plt.figure(figsize=(9,4));ax=fig.add_subplot(121,projection='3d');u,v=np.meshgrid(np.linspace(0,2*np.pi,45),np.linspace(0,2*np.pi,24));ax.plot_wireframe((1.55+.5*np.cos(v))*np.cos(u),(1.55+.5*np.cos(v))*np.sin(u),.5*np.sin(v),color='#b2c5b3',linewidth=.4)
for a,b,c in [(1/3,1/3,'#c16b37'),(-2/3,1/3,'#487ca8'),(1/3,-2/3,'#145e4d')]:
 t=np.linspace(0,1,101);u=2*np.pi*a*t;v=2*np.pi*b*t;ax.plot((1.55+.5*np.cos(v))*np.cos(u),(1.55+.5*np.cos(v))*np.sin(u),.5*np.sin(v),color=c,linewidth=2)
ax.set_axis_off();ax.set_title('Cellular theta on a topological torus')
ax=fig.add_subplot(122);m=5
for j in range(m):
 a=2*np.pi*j/m;r=np.linspace(0,1,80);ax.plot(r*np.cos(a),r*np.sin(a),color='#145e4d');ax.scatter([np.cos(a)],[np.sin(a)],facecolor='white',edgecolor='#145e4d',s=50)
ax.scatter([0],[0],color='#145e4d',s=60);ax.set_aspect('equal');ax.axis('off');ax.set_title('Genus-two dessin: two-sheet x-projection');ax.text(0,-1.3,'Two black lifts; five clean branch points; one face',ha='center',fontsize=9)
fig.tight_layout();fig.savefig(OUT/'dessin-carriers.pdf');plt.close(fig)
print('Rendered three figures from saved outputs')
