################################################################################
# 
# Author:                   Alex Hiller
# Year:                     2019
# Animation Description:    <++>
# 
################################################################################

from manimlib.imports import *

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
