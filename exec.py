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
    Ex = 7;
    Ey = 6;
    Ez = 6;
    return [Ex, Ey, Ez];

def B_Feld(x,y,z, t):
    Bx = 2;
    By = 3;
    Bz = 0;
    return [Bx, By, Bz];

E = Field(E_Feld)
B = Field(B_Feld)
electron = Particle(np.array([10,0,0]), np.array([1,1,1]), 1, 1)

comput = Computer(0.02)
comput.start(E, B, electron, 0, 1000)


#print(electron.getTrajectory())

r = Drawer(electron.getTrajectory())
r.Draw()