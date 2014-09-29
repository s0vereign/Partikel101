# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 11:02:26 2014

@author: max

 This is the executing script for 
 Project Particle 101


"""

from __future__  import division
import numpy as np
import math
from Computer import Computer
from Drawer   import Drawer
from Particle import Particle
from Field    import Field
from Constants import Constants as cons

U0 = 1e4#V
z0 = 0.02
roh0 = 0.01
B0 = 5
d = np.sqrt(1/2 * (z0**2 + roh0**2 / 2))

r0 = np.array([1.0,1.0,0.0])
m = 52019.47214708469#MeV
q = 6
cp0 = np.sqrt((0.28204529073527773e-6 + m**2)**2 - m**2) * np.array([1,0,0]) 
tStart = 0
tEnd = 1e-7
dt = 1e-11

def E_Feld(x,y,z, t):
    
    try:
        roh = np.sqrt(x**2 + y**2)
        #E = - U0 / (2 * d**2) * (2 * z - roh)
        Ez = - U0 / (2 * d**2) *  2 * z
        Eroh = U0 / (2 * d**2) *  roh
        Ex = Eroh / (np.cos(np.arctan2(y,x)))
        Ey = Eroh / (np.sin(np.arctan2(y,x)))
        
        assert isinstance(x, np.float64)
        assert isinstance(y, np.float64)
        assert isinstance(Eroh, np.float64)
        assert isinstance(roh, np.float64)
    except BaseException, e:
        print(e)
        print(type(x),x)
        print(type(y),y)
        print(type(Eroh), Eroh)
        print(type(roh), roh)
    
    return [Ex, Ey, Ez];

def B_Feld(x,y,z, t):
    Bx = 0;
    By = 0;
    Bz = B0;
    
    return [Bx, By, Bz];



E = Field(E_Feld)
B = Field(B_Feld)
particle = Particle(r0, cp0, m, q)

#print("Radius [m]:", particle.getBeta()*particle.getGamma()*particle.getM()*1e6/(cons.c*np.linalg.norm(B.calcField(r0,0))))


comput = Computer(dt)
comput.start(E, B, particle, tStart, tEnd)

r = Drawer()
r.Draw(particle, tStart, tEnd, dt)
#print(particle.getKineticEnergy()[-1]);
