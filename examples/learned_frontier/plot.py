#!/usr/bin/env python3
"""Publication vector figures from preserved learned-frontier numerical records."""
from pathlib import Path
import json,shutil
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[2];out=ROOT/'outputs/figures/2026-11-04-learned-frontier';out.mkdir(parents=True,exist_ok=True)
summary=json.loads((ROOT/'web/data/learned-frontier/summary.json').read_text());run=json.loads((ROOT/'outputs/experiments/learned-frontier/generative-20261104-v1/record.json').read_text())
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42})
fig,axes=plt.subplots(2,2,figsize=(8,5.8),sharex=True,sharey=True)
for ax,r,s in zip(axes.flat,run['records'],summary['summary']):
    points=np.array(r['samples']);ax.scatter(points[:,0],points[:,1],s=6,alpha=.45,c='#127f99' if 'product' in r['architecture'] else '#8652b5')
    for x in [-1,1]:
        for y in [-1,1]:ax.add_patch(plt.Circle((x,y),.4,fill=False,lw=.8,color='#687b85'));ax.plot(x,y,'+',c='#263f4b',ms=5)
    ax.set_title(r['objective'].title()+' / '+('product' if 'product' in r['architecture'] else 'entangled')+f"\n3-seed mean TV={s['metrics']['total_variation']['mean']:.3f}");ax.set_xlim(-2,2);ax.set_ylim(-2,2);ax.set_aspect('equal');ax.grid(alpha=.15)
for ax in axes[-1]:ax.set_xlabel('Retained noisy black-spin coordinate x₀')
for ax in axes[:,0]:ax.set_ylabel('Coordinate x₁')
fig.tight_layout();fig.savefig(out/'learned-generative.pdf');plt.close(fig)
fig,axes=plt.subplots(1,2,figsize=(8,3.1));rows=summary['width']['rows'];x=[r['width'] for r in rows]
axes[0].errorbar(x,[r['kernel_relative_Frobenius_mean'] for r in rows],yerr=[r['kernel_relative_Frobenius_std'] for r in rows],marker='o',color='#147d96',capsize=3);axes[0].set(xscale='log',yscale='log',xlabel='Independent frozen quantum features',ylabel='Relative kernel error',title='Specified RBF width limit (8 seeds)');axes[0].grid(alpha=.2)
r=summary['state_flow']['rows'];axes[1].plot([v['t'] for v in r],[max(1e-8,1-v['fidelity']) for v in r],'-o',ms=3,color='#8652b5');axes[1].set(yscale='log',xlabel='Purification control time',ylabel='Grid infidelity',title='Separate coherent4qubit state flow');axes[1].grid(alpha=.2);fig.tight_layout();fig.savefig(out/'learned-width-flow.pdf');plt.close(fig)
fig,axes=plt.subplots(1,3,figsize=(8,2.9))
for ax,m,radius in zip(axes,[3,5,9],[4,3,2]):
    nodes=[(0.,2*np.pi,0,-1,'')];edges=[]
    for index,(angle,span,depth,parent,edge) in enumerate(nodes):
        if depth==radius:continue
        letters=[k for k in range(m) if k!=edge]
        for j,letter in enumerate(letters):
            width=span/len(letters);a=angle-span/2+width*(j+.5);nodes.append((a,width,depth+1,index,letter));edges.append((index,len(nodes)-1))
    xy=np.array([[d*np.cos(a),d*np.sin(a)] for a,w,d,p,e in nodes])
    for a,b in edges:ax.plot(xy[[a,b],0],xy[[a,b],1],lw=.5,color=['#147d96','#8652b5','#c28b35'][nodes[b][-1]%3])
    ax.scatter(xy[:,0],xy[:,1],s=3,c='#254a59');ax.set_title(f'genus {(m-1)//2}: m={m}\nF{m-1}, radius{radius}, {len(nodes)} vertices');ax.set_aspect('equal');ax.axis('off')
fig.tight_layout();fig.savefig(out/'learned-covers.pdf');plt.close(fig)
for name in ['learned-generative','learned-width-flow','learned-covers']:shutil.copyfile(out/(name+'.pdf'),ROOT/'book/figures'/(name+'.pdf'))
print('Three original vector figures generated from saved records; no source data changed')
