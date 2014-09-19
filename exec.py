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
    Bx = 0;
    By = .2;
    Bz = 0;
    
    return [Bx, By, Bz];



r0 = np.array([0,0,0])
m = Constants.me
q = Constants.e
cp0 = np.sqrt(20**2 - m**2) * np.array([1,0,0])
print("cp0:",cp0)
print("Gamma1:", 20/m+1)
print("Gamma2:", np.sqrt(np.linalg.norm(cp0)**2 / m**2 + 1))
tStart = 0
tEnd = 1e-9
dt = 1e-11

E = Field(E_Feld)
B = Field(B_Feld)
particle = Particle(r0, cp0, m, q)
comput = Computer(dt)
comput.start(E, B, particle, tStart, tEnd)

r = Drawer()
r.DrawTrajectory(particle.getTrajectory())
#r.DrawKineticEnergy(particle.getKineticEnergy(), tStart, tEnd, dt)