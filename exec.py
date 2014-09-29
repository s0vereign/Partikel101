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

from IPython.display import display_latex

U0 = 1e4#V
z0 = 11.18e-3#m
roh0 = 13e-3#m
B0 = 5.9#T
d = np.sqrt(1/2 * (z0**2 + roh0**2 / 2))

r0 = np.array([0.0,0.0,0.0])
m = 52019.47214708469#MeV
q = 6
cp0 = np.sqrt((0.0002 + m)**2 - m**2) * np.array([1,0,1])
tStart = 0
tEnd = 1e-6
dt = 1e-10

def E_Feld(x,y,z, t):
    roh = np.sqrt(x**2 + y**2)
    #E = - U0 / (2 * d**2) * (2 * z - roh)
    Ez = - U0 / d**2 * z
    Eroh = U0 / (2 * d**2) *  roh
    Ex = Eroh * np.cos(np.arctan2(y,x))
    Ey = Eroh * np.sin(np.arctan2(y,x))
    
    return [Ex, Ey, Ez];
    #return [0,0,Ez]

def B_Feld(x,y,z, t):
    Bx = 0;
    By = 0;
    Bz = B0;
    
    return [Bx, By, Bz];
    #return [0,0,0]

E = Field(E_Feld)
B = Field(B_Feld)
particle = Particle(r0, cp0, m, q)

omega_c = q / m * cons.c**2 * B0 * 1e-6
omega_z = np.sqrt(q * cons.c**2 * U0/(m * d**2*1e6))
print(r"$\omega_c$ = {:5.2e}".format(omega_c))
print(r"$\omega_z$ = {:5.2e}".format(omega_z))
print(r"$\omega_+$ = {:5.2e}".format(omega_c/2 + np.sqrt(omega_c**2 / 4 - omega_z**2 / 2)))
print(r"$\omega_-$ = {:5.2e}".format(omega_c/2 - np.sqrt(omega_c**2 / 4 - omega_z**2 / 2)))

#print("Radius [m]:", particle.getBeta()*particle.getGamma()*particle.getM()*1e6/(cons.c*np.linalg.norm(B.calcField(r0,0))))
#print(particle.getBeta())

comput = Computer(dt)
comput.start(E, B, particle, tStart, tEnd)

r = Drawer()
r.Draw(particle, tStart, tEnd, dt)
#print(particle.getKineticEnergy()[-1]);
