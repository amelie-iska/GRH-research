#!/usr/bin/env python3
"""Exact finite constructions and explicitly numerical projections for the PDF."""
from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from verify_examples import ec_add, scalar_mul

OUT = Path(__file__).resolve().parents[1] / "manuscript/figures"
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                     "axes.spines.top": False, "axes.spines.right": False,
                     "axes.labelcolor": "#203449", "text.color": "#203449"})


def save(fig, stem):
    fig.savefig(OUT / f"{stem}.pdf", bbox_inches="tight")
    fig.savefig(OUT / f"{stem}.png", dpi=160, bbox_inches="tight")
    plt.close(fig)


fig, ax = plt.subplots(figsize=(6.5, 5.0), constrained_layout=True)
pts = [(x, y) for x in range(17) for y in range(17) if (y*y-x*x*x-2*x-2) % 17 == 0]
ax.scatter(*zip(*pts), color="#007e87", s=45)
for k in (1, 2, 3, 7):
    x, y = scalar_mul(k, (5, 1))
    ax.annotate(f"{k}P", (x, y), xytext=(6, 6), textcoords="offset points", fontsize=9)
ax.set(xlim=(-.7, 16.7), ylim=(-.7, 16.7), xticks=range(0, 17, 2), yticks=range(0, 17, 2),
       xlabel="x residue modulo 17", ylabel="y residue modulo 17",
       title="18 affine points, plus the point at infinity O")
ax.grid(alpha=.18)
ax.set_aspect("equal")
save(fig, "ecc17")

fig, ax = plt.subplots(figsize=(6.5, 4.8), constrained_layout=True)
prob = np.zeros((7, 7))
for u in range(7): prob[(3*u) % 7, u] = 1/7
img=ax.imshow(prob, origin="lower", vmin=0, vmax=1/7, cmap="Blues", interpolation="none")
for u in range(7): ax.text(u, (3*u) % 7, "1/7", ha="center", va="center", color="white", fontsize=9)
ax.set(xlabel="Fourier coordinate u", ylabel="Fourier coordinate v", xticks=range(7), yticks=range(7),
       title="Hidden relation v = 3u mod 7")
fig.colorbar(img, ax=ax, label="Exact probability")
save(fig, "fourier7")

fig, (ax, bx) = plt.subplots(1, 2, figsize=(8, 3.5), constrained_layout=True)
eps = np.linspace(0, 1, 301)
ax.plot(eps, eps**2, color="#007e87", lw=2, label="eigenvalue ε²")
ax.plot(eps, np.ones_like(eps), color="#bb733b", lw=2, label="eigenvalue 1")
ax.set(xlabel="ε", ylabel="Eigenvalue", title="Middle Hodge matrix diag(ε², 1)")
ax.legend(frameon=False, fontsize=8)
t = np.linspace(-2, 2, 301)
for eta in (1, .5, .1): bx.plot(t, eta**2*(1+t*t), label=f"η = {eta}")
bx.set(xlabel="Order parameter t", ylabel="Least eigenvalue", title="Scaled periodic-order complex")
bx.legend(frameon=False, fontsize=8)
save(fig, "hodge_gaps")

a,b = np.meshgrid(np.linspace(0,2*np.pi,70),np.linspace(0,2*np.pi,70))
u1,u2,v1,v2 = np.cos(a)/np.sqrt(2),np.sin(a)/np.sqrt(2),np.cos(b)/np.sqrt(2),np.sin(b)/np.sqrt(2)
x1,x2,y1,y2 = (u1+v1)/np.sqrt(2),(u2+v2)/np.sqrt(2),(u1-v1)/np.sqrt(2),(u2-v2)/np.sqrt(2)
# Orthographic projection of a specified rotation in the (x1,y2)-plane.
theta=.65
xp=np.cos(theta)*x1-np.sin(theta)*y2
fig=plt.figure(figsize=(6.5,5.0),constrained_layout=True)
ax=fig.add_subplot(111,projection="3d")
ax.plot_wireframe(xp,x2,y1,rstride=4,cstride=4,color="#007e87",alpha=.6,linewidth=.5)
ax.set(xlabel="rotated x1",ylabel="x2",zlabel="y1",
       title="Unit link of x1 y1 + x2 y2 = 0 in R⁴\nOrthographic 3D projection; overlaps are projection artifacts")
ax.set_box_aspect((1,1,1))
save(fig,"cone_link")

fig,ax=plt.subplots(figsize=(6.5,3.7),constrained_layout=True)
z=np.linspace(-.5,.5,401)
ax.plot(z,4*np.pi**2*z*z,color="#007e87",lw=2)
ax.scatter([0],[0],color="#bb733b",s=35,zorder=5)
ax.set(xlabel="Automorphy parameter s (t = 0; L1 = L2 = 1)",
       ylabel="Lowest twisted scalar eigenvalue",title="Flat torus: lowest eigenvalue approaches zero")
ax.grid(alpha=.15)
save(fig,"twisted_gap")
print(f"Created five PDF figures and PNG previews in {OUT}")
