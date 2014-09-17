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
    Ex = 1;
    Ey = 0;
    Ez = 0;
    return [Ex, Ey, Ez];

def B_Feld(x,y,z, t):
"""
This function provied
"""    
    
    Bx = 0;
    By = 0;
    Bz = 0;
    
    return [Bx, By, Bz];

E = Field(E_Feld)
B = Field(B_Feld)
electron = Particle(np.array([0,0,0]), np.array([1,0,0]), 1, 1)

comput = Computer()
comput.start(E, B, electron, 0, 30)
particle = Particle(np.array([0,0,0]), np.array([1,0,0]), 1, 1)

comput = Computer()
comput.start(E, B, particle, 0, 10)


r = Drawer(particle.getTrajectory())
r.Draw()