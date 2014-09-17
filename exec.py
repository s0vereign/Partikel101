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
<<<<<<< HEAD
def E_Feld(x,y,z, t):
=======

def E_Feld(x,y,z, t):

>>>>>>> e72b31e97c982243d63772b82dd61a670c0bc94a
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

<<<<<<< HEAD

m = 1
q = 1
v0 = np.array([0,0,Constants.c*0.08])
r0 = np.array([0,0,0])
=======
r0 = np.array([0,0,0])
v0 = np.array([0.008 * Constants.c,0,0])
m = Constants.me
q = Constants.e
>>>>>>> e72b31e97c982243d63772b82dd61a670c0bc94a

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
<<<<<<< HEAD
r.DrawKineticEnergy(particle.getKineticEnergy(), tStart, tEnd, dt)
=======
#r.DrawKineticEnergy(particle.getKineticEnergy(electronVolt=False), tStart, tEnd, dt)
r.DrawKineticEnergy(particle.getVelocities(), tStart, tEnd, dt)
>>>>>>> e72b31e97c982243d63772b82dd61a670c0bc94a
