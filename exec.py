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
from math import *
from Computer import Computer
from Drawer   import Drawer
from Particle import Particle
from Field    import Field
from Constants import Constants

def E_Feld(x,y,z, t):
    Ex = 0;
    Ey = 0;
    Ez = 20*(math.sin(Constants.w*t)*sin((Constants.w/Constants.c)*z));
    
    #~ if(Ez < 0):
        #~ Ez = Ez*-1
        
    rb = np.sqrt((x**2)+(y**2)+(z**2))

    if(rb > 9*Constants.lamb*0.5):Ez = 0;
        
    return [Ex, Ey, Ez];

def B_Feld(x,y,z, t):
    Bx = 0;
    By = 0;
    Bz = 0;
    
    return [Bx, By, Bz];



r0 = np.array([0,0,0])
m = Constants.me
q = Constants.e
#whats's the idea in calculating cp0 this way??!?!?!?
cp0 = np.sqrt((20+m)**2 - m**2) * np.array([0,0,1]) 
tStart = 0
tEnd = 3.5*1e-9
dt = 1e-11

E = Field(E_Feld)
B = Field(B_Feld)
particle = Particle(r0, cp0, m, q)

#print("Radius [m]:", particle.getBeta()*particle.getGamma()*particle.getM()*1e6/(Constants.c*np.linalg.norm(B.calcField(r0,0))))


comput = Computer(dt)
comput.start(E, B, particle, tStart, tEnd)

r = Drawer()
r.Draw(particle, tStart, tEnd, dt)
print(particle.getKineticEnergy()[-1])