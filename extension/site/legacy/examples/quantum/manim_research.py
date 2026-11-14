"""Corrected finite research animations. Existing Manim; no TeX or installs.

The legacy SurfaceClock is not a theta dessin. These new scenes distinguish
an actual topological embedding, intrinsic AR morphisms, polynomial syzygies,
and a learned finite quantum channel. None is an arithmetic spectral proof.
"""
from pathlib import Path
import json
import numpy as np
from manim import (
    Scene, ThreeDScene, Surface, ParametricFunction, Dot3D, VGroup,
    Text, Line, Arrow, Circle, Rectangle, RoundedRectangle, Dot, Cross,
    Create, FadeIn, FadeOut, Write, Transform, MoveAlongPath, Indicate,
    LaggedStart, AnimationGroup, UP, DOWN, LEFT, RIGHT, ORIGIN, DEGREES,
    WHITE, BLACK, TAU,
)

ROOT=Path(__file__).resolve().parents[2]
PAPER="#f5f3ec"
INK="#183c34"
GREEN="#145e4d"
BLUE="#487ca8"
ORANGE="#c16b37"
PALE="#cad9cb"
RED="#a84943"


def label(text,size=24,color=INK):
    return Text(text,font_size=size,color=color)


def top_title(scene,title,subtitle):
    t=label(title,30).to_edge(UP,buff=.24)
    s=label(subtitle,17).next_to(t,DOWN,buff=.13)
    scene.add(t,s)
    return VGroup(t,s)


class ThetaDessin(ThreeDScene):
    """Actual elliptic theta graph, not three disconnected torus loops."""
    def construct(self):
        self.camera.background_color=PAPER
        self.set_camera_orientation(phi=65*DEGREES,theta=-42*DEGREES)
        title=label("The actual theta dessin on a torus",29).to_edge(UP,buff=.22)
        subtitle=label("Topological embedding; not a uniformizing metric or arithmetic flow",16).next_to(title,DOWN,buff=.12)
        caption=label("Two black endpoints; three arcs; three white degree-two vertices",17).to_edge(DOWN,buff=.22)
        self.add_fixed_in_frame_mobjects(title,subtitle,caption)

        def torus(u,v):
            return np.array([(2+.62*np.cos(TAU*v))*np.cos(TAU*u),
                             (2+.62*np.cos(TAU*v))*np.sin(TAU*u),
                             .62*np.sin(TAU*v)])
        mesh=Surface(torus,u_range=[0,1],v_range=[0,1],resolution=(28,16),
                     checkerboard_colors=[PALE,"#dce4d8"],fill_opacity=.24,
                     stroke_color="#b3c5b7",stroke_width=.45)
        lifts=[(1/3,1/3),(-2/3,1/3),(1/3,-2/3)]
        colors=[ORANGE,BLUE,GREEN]
        paths=VGroup(*[ParametricFunction(lambda t,a=a,b=b:torus(a*t,b*t),
                     t_range=[0,1],color=color,stroke_width=5)
                     for (a,b),color in zip(lifts,colors)])
        black=VGroup(Dot3D(torus(0,0),radius=.13,color=BLACK),
                     Dot3D(torus(1/3,1/3),radius=.13,color=BLACK))
        white=VGroup(*[Dot3D(torus(a/2,b/2),radius=.095,color=WHITE,
                              stroke_color=GREEN,stroke_width=1.1)
                       for a,b in lifts])
        # All three arcs share exactly the two endpoint positions on the torus.
        assert all(np.linalg.norm(torus(a,b)-torus(1/3,1/3))<1e-12 for a,b in lifts)
        self.play(FadeIn(mesh),run_time=.8)
        self.play(FadeIn(black),run_time=.5)
        self.play(LaggedStart(*(Create(path) for path in paths),lag_ratio=.25),run_time=2)
        white_labels=VGroup(*[label("W"+str(j+1),16).move_to(torus(a/2,b/2)+np.array([0,0,.25]))
                             for j,(a,b) in enumerate(lifts)])
        self.add_fixed_orientation_mobjects(*white_labels)
        self.play(FadeIn(white),FadeIn(white_labels),run_time=.6)
        self.begin_ambient_camera_rotation(rate=.18)
        self.wait(3)
        self.stop_ambient_camera_rotation()


class HLSDiamond(Scene):
    """The signed central window of one intrinsic H3 component."""
    def construct(self):
        self.camera.background_color=PAPER
        top_title(self,"Four signed AR meshes in nine actual objects",
                  "Intrinsic H3 quotient category; not ambient or derived AR transfer")
        positions={
            "A":[-4.7,0,0],"B":[-2.35,1.12,0],"C":[0,2.24,0],
            "D":[-2.35,-1.12,0],"E":[0,0,0],"F":[2.35,1.12,0],
            "G":[0,-2.24,0],"H":[2.35,-1.12,0],"I":[4.7,0,0]}
        words={"A":"M(cwc)","B":"M(wc)","C":"M(hwc)","D":"M(cw)",
               "E":"M(w), w=ab","F":"M(hw)","G":"M(cwh)",
               "H":"M(wh)","I":"M(hwh)"}
        objects={}
        for name,pos in positions.items():
            main=label(name,24).move_to(pos)
            word=label(words[name],13).next_to(main,DOWN,buff=.07)
            objects[name]=VGroup(main,word)
        arrows_data=[("A","B","p"),("A","D","-p"),
                     ("B","C","i"),("B","E","p"),
                     ("C","F","-p"),("D","E","p"),
                     ("D","G","-i"),("E","F","i"),
                     ("E","H","i"),("F","I","-i"),
                     ("G","H","p"),("H","I","i")]
        arrows={};signs=VGroup()
        for a,b,s in arrows_data:
            start=np.array(positions[a],float);end=np.array(positions[b],float)
            arrow=Arrow(start,end,buff=.39,stroke_width=2.3,color=GREEN,
                        max_tip_length_to_length_ratio=.065)
            arrows[(a,b)]=arrow
            delta=end-start;normal=np.array([-delta[1],delta[0],0]);normal/=np.linalg.norm(normal)
            signs.add(label(s,17,ORANGE).move_to((start+end)/2+.16*normal))
        caption=label("E=M(ab); each small diamond is an exact mesh",18).to_edge(DOWN,buff=.56)
        formula=label("(B->E)(A->B) + (D->E)(A->D) = 0",19).to_edge(DOWN,buff=.18)
        self.play(FadeIn(VGroup(*objects.values())),run_time=.8)
        self.play(LaggedStart(*(Create(x) for x in arrows.values()),lag_ratio=.05),run_time=1.7)
        self.play(FadeIn(signs),Write(caption),run_time=.8)
        first=[("A","B"),("B","E"),("A","D"),("D","E")]
        self.play(*(arrows[e].animate.set_color(ORANGE) for e in first),run_time=.5)
        dots=VGroup(Dot(positions["A"],radius=.065,color=BLUE),
                    Dot(positions["A"],radius=.065,color=ORANGE))
        self.add(dots)
        self.play(MoveAlongPath(dots[0],Line(positions["A"],positions["B"])),
                  MoveAlongPath(dots[1],Line(positions["A"],positions["D"])),run_time=.75)
        self.play(MoveAlongPath(dots[0],Line(positions["B"],positions["E"])),
                  MoveAlongPath(dots[1],Line(positions["D"],positions["E"])),run_time=.75)
        self.play(FadeOut(dots),Write(formula),run_time=.65)
        self.wait(2)


def _multiply_polynomials(a,b):
    out={}
    for (i,j),c in a.items():
        for (k,l),d in b.items():out[(i+k,j+l)]=out.get((i+k,j+l),0)+c*d
    return {e:c for e,c in out.items() if c}


def _check_syzygy_identity():
    d1=[{(2,0):1},{(1,1):1},{(0,2):1}]
    d2=[[{(0,1):-1},{}],[{(1,0):1},{(0,1):-1}],[{},{(1,0):1}]]
    for column in range(2):
        result={}
        for row in range(3):
            for e,c in _multiply_polynomials(d1[row],d2[row][column]).items():result[e]=result.get(e,0)+c
        assert all(c==0 for c in result.values())


class Bifiltration(Scene):
    """Three nonzero pieces and two syzygies over an auxiliary polynomial ring."""
    def construct(self):
        self.camera.background_color=PAPER
        _check_syzygy_identity()
        top_title(self,"A finite bifiltration and its syzygies",
                  "M = R/(x,y)^2 with R = k[x,y], an auxiliary persistence ring")
        origin=np.array([-5.2,-1.6,0.]);step=1.45
        axes=VGroup(Arrow(origin-.25*RIGHT,origin+3.5*step*RIGHT,color=INK,buff=0,stroke_width=2,tip_length=.13),
                    Arrow(origin-.25*UP,origin+3.0*step*UP,color=INK,buff=0,stroke_width=2,tip_length=.13))
        self.play(Create(axes),run_time=.6)
        coords=lambda i,j:origin+step*i*RIGHT+step*j*UP
        grid=VGroup()
        for i in range(4):
            for j in range(3):
                grid.add(Dot(coords(i,j),radius=.025,color=PALE))
        names={(0,0):"1 : (0,0)",(1,0):"x : (1,0)",(0,1):"y : (0,1)"}
        good=VGroup()
        for (i,j),s in names.items():
            good.add(Dot(coords(i,j),radius=.07,color=GREEN),
                     label(s,16).next_to(coords(i,j),DOWN if j==0 else LEFT,buff=.13))
        maps=VGroup(Arrow(coords(0,0),coords(1,0),color=GREEN,buff=.12,stroke_width=2.5,tip_length=.14),
                     Arrow(coords(0,0),coords(0,1),color=GREEN,buff=.12,stroke_width=2.5,tip_length=.14))
        forbidden=VGroup()
        for (i,j),s in { (2,0):"x^2 = 0",(1,1):"xy = 0",(0,2):"y^2 = 0"}.items():
            ring=Circle(radius=.10,color=RED).move_to(coords(i,j))
            forbidden.add(ring,label(s,15,RED).next_to(ring,DOWN if j==0 else RIGHT,buff=.12))
        self.play(FadeIn(grid),FadeIn(good),Create(maps),run_time=1)
        self.play(FadeIn(forbidden),run_time=.7)
        resolution=label("0 -> R^2 -> R^3 -> R -> M -> 0",19).move_to([3.0,1.6,0])
        matrix1=Text("d1 = [ x^2  xy  y^2 ]",font="Menlo",font_size=19,color=INK).move_to([3.,.85,0])
        matrix2=Text("     [ -y   0 ]\nd2 = [  x  -y ]\n     [  0   x ]",font="Menlo",font_size=18,color=INK).move_to([3.,-.25,0])
        zero=label("d1 d2 = [ 0, 0 ]",24,GREEN).move_to([3.,-1.55,0])
        self.play(Write(resolution),Write(matrix1),run_time=1)
        self.play(Write(matrix2),run_time=1.2)
        self.play(Write(zero),run_time=.7)
        foot=VGroup(label("Graded shifts and full exactness are given in the source/book.",16),
                    label("The animation checks a chain identity; it is not a proof of exactness.",16))
        foot.arrange(DOWN,buff=.13).to_edge(DOWN,buff=.25)
        self.play(FadeIn(foot),run_time=.6)
        self.wait(2)


class QCNNPooling(Scene):
    """Actual four-qubit learned circuit; schematic movement is not amplitudes."""
    def construct(self):
        self.camera.background_color=PAPER
        data=json.loads((ROOT/"outputs/experiments/renormalization-pennylane/training.json").read_text())
        model=next(m for m in data["models"] if m["name"]=="Four-qubit QCNN compression")
        weights=np.asarray(model["theta"]).reshape(2,4,2)
        top_title(self,"A trained four-qubit pooling channel",
                  "Saved parameters (rounded); arrows show data flow, not amplitudes")
        ys=[1.6,.55,-.50,-1.55]
        wires=VGroup(*[Line([-5.6,y,0],[5.65,y,0],color=PALE,stroke_width=2) for y in ys])
        names=VGroup(*[label("q"+str(q),19).move_to([-6.,y,0]) for q,y in enumerate(ys)])
        self.play(Create(wires),FadeIn(names),run_time=.65)
        gate_groups=[]
        for layer,(rx,rz,first_cz) in enumerate([(-4.7,-4.0,-3.4),(-1.2,-.5,.25)]):
            gates=VGroup()
            for q,y in enumerate(ys):
                for j,(x,name) in enumerate([(rx,"Ry"),(rz,"Rz")]):
                    box=RoundedRectangle(width=.57,height=.54,corner_radius=.04,
                                         color=GREEN,fill_color="#e3ece1",fill_opacity=1,stroke_width=1.2).move_to([x,y,0])
                    text=label(name+"\n"+format(weights[layer,q,j],"+.2f"),11).move_to(box)
                    gates.add(box,text)
            for j,(a,b) in enumerate([(0,1),(1,2),(2,3),(3,0)]):
                x=first_cz+.48*j
                gates.add(Line([x,ys[a],0],[x,ys[b],0],color=BLUE,stroke_width=1.8),
                          Dot([x,ys[a],0],radius=.045,color=BLUE),
                          Dot([x,ys[b],0],radius=.045,color=BLUE))
            gate_groups.append(gates)
        self.play(LaggedStart(*(FadeIn(g) for g in gate_groups),lag_ratio=.3),run_time=1.5)
        pooling=VGroup()
        for a,b,x in [(0,2,2.75),(1,3,3.55)]:
            pooling.add(Line([x,ys[a],0],[x,ys[b],0],color=ORANGE,stroke_width=2),
                        Dot([x,ys[a],0],radius=.055,color=ORANGE),
                        Circle(radius=.12,color=ORANGE,stroke_width=2).move_to([x,ys[b],0]),
                        Line([x-.12,ys[b],0],[x+.12,ys[b],0],color=ORANGE,stroke_width=2),
                        Line([x,ys[b]-.12,0],[x,ys[b]+.12,0],color=ORANGE,stroke_width=2))
        discard=RoundedRectangle(width=1.0,height=2.0,corner_radius=.08,color="#8b938c",
                                 fill_color="#d9ddd5",fill_opacity=.8).move_to([4.8,(ys[2]+ys[3])/2,0])
        trace=label("trace\nout",16).move_to(discard)
        keep=label("keep q0,q1",16,GREEN).move_to([5.,2.15,0])
        self.play(FadeIn(pooling),FadeIn(discard),Write(trace),Write(keep),run_time=.9)
        dots=VGroup(*[Dot([-5.6,y,0],radius=.05,color=ORANGE) for y in ys]);self.add(dots)
        self.play(*(dot.animate.move_to([4.1,y,0]) for dot,y in zip(dots,ys)),run_time=1.8)
        self.play(FadeOut(VGroup(dots[2],dots[3])),
                  dots[0].animate.move_to([5.65,ys[0],0]),dots[1].animate.move_to([5.65,ys[1],0]),run_time=.8)
        formula=label("E(rho) = Tr_(q2,q3) [ W rho W* ]",24).move_to([0,-2.45,0])
        detail=label("A CPTP channel; not an isometry from C^16 to C^4",17).move_to([0,-3.00,0])
        loss=label("Final held-out discard loss: "+format(model["curve"][-1]["test"],".4f")+" (substantial residual)",16,ORANGE).move_to([0,-3.45,0])
        self.play(Write(formula),FadeIn(detail),FadeIn(loss),run_time=1)
        self.wait(2)
