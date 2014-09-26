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



r0 = np.array([0,0,0])
m = cons.me
q = cons.e
#whats's the idea in calculating cp0 this way??!?!?!?
cp0 = np.sqrt(0.3) * np.array([1,0,0]) 
tStart = 0
tEnd = 1e-8
dt = 1e-10

def E_Feld(x,y,z, t):
    d1 = cons.d1
    d2 = cons.d2
    r = np.array([x,y,z]);
    rbetr = np.linalg.norm(r);
    s1 = 1/(rbetr+0.5*cons.d1b)**2-1/(rbetr-0.5*cons.d1b)**2
    s2 = 1/(rbetr+0.5*cons.d2b)**2-1/(rbetr-0.5*cons.d2b)**2
    sg = s1+s2                  #Calculating the reziproke terms
    Eges = q**2/(4*math.pi*cons.e0)*sg
    # so much for the norm of the field now let's get to the 
    # direction
    
    er1 = r + 0.5*d1/(np.linalg.norm(r+0.5*cons.d1))+ r-0.5*d1/np.linalg.norm(r-0.5*d1)
    er2 = r + 0.5*cons.d2/np.linalg.norm(r+0.5*cons.d1) + r - 0.5*d2/np.linalg.norm(r-0.5*d2)
    er = er1 + er2;
    #calculated the direction of the field
    
    
    
    return Eges*er;

def B_Feld(x,y,z, t):
    Bx = 0;
    By = 0;
    Bz = 0.2;
    
    return [Bx, By, Bz];



E = Field(E_Feld)
B = Field(B_Feld)
particle = Particle(r0, cp0, m, q)

#print("Radius [m]:", particle.getBeta()*particle.getGamma()*particle.getM()*1e6/(Constants.c*np.linalg.norm(B.calcField(r0,0))))


comput = Computer(dt)
comput.start(E, B, particle, tStart, tEnd)

r = Drawer()
r.Draw(particle, tStart, tEnd, dt)
print(particle.getKineticEnergy()[-1]);
