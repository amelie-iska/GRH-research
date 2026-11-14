"""Static publication figure from the exact interactive dataset examples."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parents[2]
data=json.loads((root/'web/data/synthetic-training/large-v2/examples.json').read_text())
pdb=next(c for c in data['cases'] if c['title'].startswith('PDB residue transfer / 1L2Y'))
md=next(c for c in data['cases'] if c['domain']=='molecule')
fig=plt.figure(figsize=(11,3.7),layout='constrained');ax=fig.add_subplot(131,projection='3d');x=np.array(pdb['positions']);field=np.array(pdb['electronic']['targets']['charge_modulation'])[20]
for i,j in pdb['edges']:ax.plot(*x[[i,j]].T,color='#bcc9cc',lw=.6,alpha=.5)
v=max(abs(field).max(),1e-3);ax.scatter(*x.T,c=field,cmap='coolwarm',vmin=-v,vmax=v,s=26,depthshade=False)
ax.set_title('Trp-cage1L2Y: recorded CA subsystem\nSynthetic orbital modulation, t=6',fontsize=9);ax.set(xlabel='x (Å)',ylabel='y (Å)',zlabel='');ax.tick_params(labelsize=7)
ax=fig.add_subplot(132);t=np.array(pdb['electronic']['targets']['time']);occupation=np.array(pdb['electronic']['targets']['occupation'])
for i in [0,1,2]:ax.plot(t,occupation[:,i],label=f'Orbital {i}')
ax.set(title='Effective contact-Hamiltonian dynamics',xlabel='Dimensionless time (ℏ=1)',ylabel='Occupation');ax.legend(fontsize=7);ax.grid(alpha=.18)
ax=fig.add_subplot(133);e=np.array(md['energy']);t=np.array([f['time_fs'] for f in md['frames']]);ax.plot(t,e-e[0],color='#1d8b9e')
ax.set(title='Separate MMFF94 nuclear trajectory',xlabel='Time (fs)',ylabel='Total energy − initial (kcal/mol)');ax.grid(alpha=.18)
fig.savefig(root/'book/figures/complementary-datasets.pdf');fig.savefig(root/'outputs/renders/2026-11-04-synthetic-training/dataset-book.png',dpi=170)
print({'source_examples':str(root/'web/data/synthetic-training/large-v2/examples.json'),'PDB_record':pdb['id'],'MD_record':md['id'],'PDF':'book/figures/complementary-datasets.pdf'})
