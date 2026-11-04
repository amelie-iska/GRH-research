from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parents[2]
wave=json.loads((root/'web/data/synthetic-training/orbital-v1/wavepackets.json').read_text())['cases']
chem=json.loads((root/'web/data/synthetic-training/torsion-v2/torsion-flow.json').read_text())['experiments']
fig,axes=plt.subplots(1,3,figsize=(12,3.5),layout='constrained')
for c in wave[:2]:
    axes[0].plot(c['time'],np.array(c['site_probability'])[:,:4].sum(1),label='winding '+str(c['topology']['winding']))
axes[0].set(title='Matched SSH endpoint excitation',xlabel='Physical model time (ℏ=1)',ylabel='Probability on first four sites');axes[0].legend(fontsize=8);axes[0].grid(alpha=.15)
x,z=np.meshgrid(np.linspace(-7,7,180),np.linspace(-7,7,180));r=np.hypot(x,z);psi=z*np.exp(-r/2)/(4*np.sqrt(2*np.pi));axes[1].contourf(x,z,abs(psi)**2,levels=20,cmap='magma');axes[1].contour(x,z,psi,levels=[0],colors=['#6dc9e7'],linewidths=1);axes[1].set(title='Analytic hydrogen 2pᶻ density slice',xlabel='x / a₀',ylabel='z / a₀');axes[1].set_aspect('equal')
labels=[];classic=[];quantum=[]
for e in chem:
    for method in ['flow','score']:
        labels.append(f"T{e['target']['dimension']} {method}");classic.append(next(m['endpoint_total_variation'] for m in e['models'] if m['method']==method and not m['quantum']));quantum.append(next(m['endpoint_total_variation'] for m in e['models'] if m['method']==method and m['quantum']))
pos=np.arange(4);axes[2].bar(pos-.18,classic,.36,label='classical');axes[2].bar(pos+.18,quantum,.36,label='quantum hybrid');axes[2].set_xticks(pos,labels,rotation=25);axes[2].set(title='Actual learned endpoint diagnostics',ylabel='Histogram total variation');axes[2].legend(fontsize=7);axes[2].text(.02,.97,'Flow and score use different endpoint laws',transform=axes[2].transAxes,va='top',fontsize=7)
fig.savefig(root/'book/figures/orbital-flow.pdf');fig.savefig(root/'outputs/renders/2026-11-04-synthetic-training/orbital-flow-book.png',dpi=170)
print('Generated actual transport/analytic orbital/trained endpoint publication figure')
