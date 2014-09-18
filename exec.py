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
from Constants import Constants

def E_Feld(x,y,z, t):

    Ex = 0;
    Ey = 0;
    Ez = 0;
    return [Ex, Ey, Ez];

def B_Feld(x,y,z, t):
    """
    This function provied
    """    
    
    Bx = 0;
    By = 0.2;
    Bz = 0;
    
    return [Bx, By, Bz];


r0 = np.array([0,0,0])
m = Constants.mp
q = Constants.e
cp0 = np.array([np.sqrt(20e6**2 - m**2),0,0])
tStart = 0
tEnd = 100
dt = 1e-3

E = Field(E_Feld)
B = Field(B_Feld)
particle = Particle(r0, cp0, m, q)
comput = Computer(dt)
comput.start(E, B, particle, tStart, tEnd)

r = Drawer()
r.DrawTrajectory(particle.getTrajectory())
r.DrawKineticEnergy(particle.getKineticEnergy(), tStart, tEnd, dt)
