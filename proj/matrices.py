################################################################################
# 
# Author:                   Alex Hiller
# Year:                     2019
# Animation Description:    <++>
# 
################################################################################

from manimlib.imports import *

class testMatrix(Scene):     # Must inherit from the 'Scene' class.
    def construct(self):        # Must have the construct() method in class.
        # Construct mobjects here
        _matrix = TextMobject(r"""
        \[ \begin{bmatrix}
            a & b & c \\
            d & e & f \\
            g & h & i \\		
        \end{bmatrix} \]
        """)
        _matEquation = TextMobject(r"""
        \[ \begin{bmatrix}
            \cos\left(\phi\right)  & -\sin\left(\phi\right)  \\
            -\cos\left(\phi\right)  & \sin\left(\phi\right)  \\		
        \end{bmatrix}
        \mathbf{x} =
        \mathbf{x'} \]
        """)

        # Animate them here
        self.add(_matrix)
        self.wait(3)
        self.play(Transform(_matrix, _matEquation))
        self.wait(3)

def main():
    pass

if __name__ == '__main__':
    main()  
