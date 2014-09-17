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
    Ex = 1000;
    Ey = 5000;
    Ez = 8000;
    return [Ex, Ey, Ez];

def B_Feld(x,y,z, t):
    """
    This function provied
    """    
    
    Bx = 0;
    By = 0;
    Bz = 0;
    
    return [Bx, By, Bz];

r0 = np.array([0,0,0])
v0 = np.array([0,0,1000])
m = 1
q = 1

tStart = 0
tEnd = 10
dt = 1e-4

E = Field(E_Feld)
B = Field(B_Feld)
particle = Particle(r0, v0, m, q)

comput = Computer(dt)
comput.start(E, B, particle, tStart, tEnd)


r = Drawer()
r.DrawTrajectory(particle.getTrajectory())
r.DrawKineticEnergy(particle.getKineticEnergy(), tStart, tEnd, dt)
