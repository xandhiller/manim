################################################################################
# 
# Author:               Alex Hiller
# Year:                 2019
# Program Description:  <++>
# 
################################################################################

from manimlib.imports import *


class circuit(Scene):
    def construct(self):
        _circuit=TextMobject(r"""
            \begin{circuitikz}[scale=1.2]\draw
                (0,0) node[anchor=east] {B}
                to[short, o-*] (1,0)
                to[R=20, *-*] (1,2)
                to[R=10, v=$v_x$] (3,2) -- (4,2)
                to[cI=${5} v_x$, *-*] (4,0) -- (3,0)
                to[R=5, *-*] (3,2)
                (3,0) -- (1,0)
                (1,2) to[short, -o] (0,2) node[anchor=east]{A} ;
            \end{circuitikz}
            """)
        self.add(_circuit)
        self.wait(10)


class james(Scene):
    def construct(self):
        _line=TextMobject(r"\[ x_1 = x_0 - \frac{f(x_0)}{f'(x_0)} \]")
        _outro=TextMobject(r"The End")
        _sum=TextMobject(r"\[ \sum^{\infty}_{n=0} \frac{1}{n} \]")
        
        self.add(_line)
        self.wait(5)
        self.play(Transform(_line, _sum))
        self.wait(5)
        self.play(Transform(_line, _outro))
        self.wait(5)
        self.play(FadeOut(_line))



class myText(Scene):
    def construct(self):
        first = "$\\frac{x}{y}$"
        fst= TextMobject(first)
        second = "blah blah blah"
        scn = TextMobject(second)
        third = r"$\sum^{\infty}$"
        trd = TextMobject(third)
        trd.next_to(fst, DOWN)  
        scn.next_to(fst, DOWN)


        self.add(fst, scn)
        self.wait(5)
        self.play(Transform(scn, trd))
        self.wait(5)
        scn.shift(3*DOWN)
        
        


class mySquare(Scene):
    def construct(self):
        square = Square()
        square.rotate(2*PI)
        self.play(ShowCreation(square))
        self.play(FadeOut(square))


def main():
    mySquare()


if __name__ == '__main__':
    main()
