################################################################################
# 
# Author:                   Alex Hiller
# Year:                     2019
# Animation Description:    <++>
# 
################################################################################

from manimlib.imports import *


class PlotFunctions(GraphScene):
    CONFIG = {
    "x_min" : -10,
    "x_max" : 10,
    "y_min" : -1.5,
    "y_max" : 1.5,
    "graph_origin" : ORIGIN ,
    "function_color" : RED ,
    "axes_color" : GREEN,
    "x_labeled_nums" :range(-10,12,2),
    }
    def construct(self):
        self.setup_axes(animate=True)
        func_graph  = self.get_graph(self.func_to_graph,self.function_color)
        func_graph2 = self.get_graph(self.func_to_graph2)
        vert_line   = self.get_vertical_line_to_graph(TAU,func_graph,color=YELLOW)
        graph_lab   = self.get_graph_label(func_graph, label = "\\cos(x)")
        graph_lab2  = self.get_graph_label(func_graph2,label = "\\sin(x)", x_val=-10, direction=UP/2)
        two_pi      = TexMobject("x = 2 \\pi")
        label_coord = self.input_to_graph_point(TAU,func_graph)
        two_pi.next_to(label_coord,RIGHT+UP)
        self.play(ShowCreation(func_graph),
                  ShowCreation(func_graph2))
        self.play(ShowCreation(vert_line), 
                  ShowCreation(graph_lab), 
                  ShowCreation(graph_lab2),
                  ShowCreation(two_pi))
     
    def func_to_graph(self,x):
        return np.cos(x)
     
    def func_to_graph2(self,x):
        return np.sin(x)




class opAmp(Scene):     # Must inherit from the 'Scene' class.
    def construct(self):        # Must have the construct() method in class.
        # Construct mobjects here
        # <++>
        op_amp = TextMobject(r"""
        \begin{circuitikz}[scale=1]\draw
        (5,.5) node [op amp] (opamp) {}
        (0,0) node [left] {$U_{we}$} to [R, l=$R_d$, o-*] (2,0)
        to [R, l=$R_d$, *-*] (opamp.+)
        to [C, l_=$C_{d2}$, *-] ($(opamp.+)+(0,-2)$) node [ground] {}
        (opamp.out) |- (3.5,2) to [C, l_=$C_{d1}$, *-] (2,2) to [short] (2,0)
        (opamp.-) -| (3.5,2)
        (opamp.out) to [short, *-o] (7,.5) node [right] {$U_{wy}$};
        \end{circuitikz}
        """)
        
        self.add(op_amp)
        self.wait(5)

        # Animate them here
        # <++>, e.g.
        # self.add(my_mobject)
        # self.play(Transform(my_mobject, new_form)

def main():
    pass



if __name__ == '__main__':
    main()
