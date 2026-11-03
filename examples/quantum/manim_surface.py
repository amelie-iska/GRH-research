"""Render with the existing Manim environment; no installation is performed.

manim -ql --media_dir outputs/animations examples/quantum/manim_surface.py SurfaceClock
The torus is a topological carrier. The moving dot is a finite clock basis
label, not an arithmetic particle or claimed geodesic flow.
"""
from manim import *
import numpy as np
class SurfaceClock(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=65*DEGREES,theta=-45*DEGREES)
        torus=lambda u,v:np.array([(2+.65*np.cos(v))*np.cos(u),(2+.65*np.cos(v))*np.sin(u),.65*np.sin(v)])
        surface=Surface(torus,u_range=[0,TAU],v_range=[0,TAU],resolution=(24,12),fill_opacity=.18,checkerboard_colors=[TEAL_E,TEAL_D],stroke_opacity=.25)
        self.add(surface)
        loops=VGroup(*[ParametricFunction(lambda t,j=j:torus(t,TAU*j/3),t_range=[0,TAU],color=[TEAL,ORANGE,BLUE][j]) for j in range(3)])
        self.play(Create(loops),run_time=2)
        points=VGroup(*[Dot3D(torus(TAU*j/4,0),radius=.12,color=YELLOW) for j in range(4)])
        self.play(FadeIn(points),run_time=1)
        self.begin_ambient_camera_rotation(rate=.12)
        for j in range(4):
            self.play(points[j].animate.set_color(RED),run_time=.35)
            self.play(points[j].animate.set_color(YELLOW),run_time=.35)
        self.wait(1)
