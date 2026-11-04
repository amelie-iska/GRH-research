"""Arrange native browser-rendered scientific canvases for the print edition."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parents[2];folder=root/'outputs/renders/2026-11-04-synthetic-training'
fig,axes=plt.subplots(1,3,figsize=(12,3),layout='constrained')
for ax,name,title in zip(axes,['atlas-protein-ribbon','atlas-wavepacket','atlas-hydrogen-vortex'],['PDB1L2Y: source secondary structure','Actual finite QWZ wave packet','Hydrogen2p: phase winding +1']):
    ax.imshow(plt.imread(folder/(name+'.png')));ax.axis('off');ax.set_title(title,fontsize=9)
fig.savefig(root/'book/figures/orbital-atlas.pdf');fig.savefig(folder/'orbital-atlas-book.png',dpi=170)
print('Arranged three native scientific canvas renders; data and source canvases unchanged')
