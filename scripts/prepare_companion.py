#!/usr/bin/env python3
"""Publish saved local experiment artifacts into the local companion bundle."""
from pathlib import Path
import json,shutil
ROOT=Path(__file__).resolve().parents[1]
out=json.loads((ROOT/'outputs/experiments/renormalization-pennylane/training.json').read_text())
p=ROOT/'outputs/experiments/toricgt-hybrid/training.json'
if p.exists():out['models'].append(json.loads(p.read_text()))
p=json.loads((ROOT/'outputs/experiments/photonic-pooling/photonic.json').read_text())
out['models'].append(dict(name='Photonic Gaussian pooling',backend=p['backend'],modes=2,parameters=p['parameters'],epochs=p['epochs'],train_size=p['train_size'],test_size=p['test_size'],architecture='opposite squeezers, fixed source beamsplitter, learned shared beamsplitter, covariance readout',objective=p['objective'],curve=p['curve'],examples=p['examples']))
blocks=[['TFIM ground states','Ry / Rz + CZ','CNOT pooling','Partial trace'],['Ising edge patch','Shared quantum features','Linear coupling head','Exact decimation loss'],['Three edge patches','Shared quantum features','Softmax attention','Star–triangle loss'],['ToricGT Weyl carrier','Quantum feature circuit','Learned eigenvalue','Exact PSD verifier'],['Opposite squeezers','Source beamsplitter','Learned beamsplitter','Covariance loss']]
extra=ROOT/'outputs/experiments/higher-genus-qcnn/training.json'
if extra.exists():
 out['models'].append(json.loads(extra.read_text()))
 blocks.append(['Genus-four edge labels','Nine-qubit circuit','Four-qubit discard','Held-out compression'])
for m,b in zip(out['models'],blocks):m['display_blocks']=b
(ROOT/'web/data/training.json').write_text(json.dumps(out,indent=2)+'\n')
media=ROOT/'web/media';media.mkdir(exist_ok=True)
video=ROOT/'outputs/animations/videos/manim_surface/480p15/SurfaceClock.mp4'
if video.exists():shutil.copyfile(video,media/'SurfaceClock.mp4')
print('Prepared',len(out['models']),'saved models')
