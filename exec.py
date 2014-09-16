# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 11:02:26 2014

@author: max

 This is the executing script for 
 Project Particle 101


"""

import numpy as np

from Computer import Computer
from Drawer   import Drawer
from Particle import Particle
from Field    import Field

def E_Feld(x,y,z, t):
    Ex = 0;
    Ey = 0;
    Ez = 0;
    return [Ex, Ey, Ez];

def B_Feld(x,y,z, t):
    Bx = 0;
    By = 0;
    Bz = 1;
    return [Bx, By, Bz];

E = Field(E_Feld)
B = Field(B_Feld)
electron = Particle(np.array([0,0,0]), np.array([0,0,0]), 9.10938291e-31, 1.60217657e-19)

comput = Computer()
comput.start(E, B, electron, 0, 1)


print(electron.getTrajectory())

r = Drawer(electron.getTrajectory())
r.Draw()