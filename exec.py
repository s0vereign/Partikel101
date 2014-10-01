# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 11:02:26 2014

@author: max

 This is the executing script for
 Project Particle 101


"""

from __future__  import division
import numpy as np
from Computer import Computer
from Drawer   import Drawer
from Particle import Particle
from Field    import Field
from Constants import Constants as cons

roh0 = 8e-4#m
z0 = roh0 / np.sqrt(2)#m
d = np.sqrt(1.0/2 * (z0**2 + roh0**2 / 2))
#d = 10e-3#m

m = cons.mp#MeV
q = 1

r = roh0#m

n1 = 5e3
n2 = 10
r0 = np.array([1.0,1.0,1.0])

omega_plus = 1e10

omega_c = omega_plus * (1 + 1.0 / n1)
omega_minus = omega_plus/n1
omega_z = omega_plus/n2

B0 = (omega_c) * m * 1e6 / (q*cons.c**2)
U0 = (omega_z)**2 * 1e6 *m / (q * cons.c**2) * d**2
#U0 = 9e3
cp0 = m*np.sqrt( 1.0 / (1 - omega_minus**2 * r**2 / cons.c**2) - 1) * np.array([1,0,0]) # m * sqrt(gamma**2 - 1) * e_cp0

print("\omega_c = {:5.2e}".format(omega_c))
print("\omega_+ = {:5.2e}".format(omega_plus))
print("\omega_- = {:5.2e}".format(omega_minus))
print("\omega_z = {:5.2e}".format(omega_z))

#~ print(r"\frac{\omega_+}{\omega_-} = {:5.2e}".format(omega_plus / omega_minus))
#~ print(r"\frac{\omega_+}{\omega_z} = {:5.2e}".format(omega_plus / omega_z))

print("U = {:5.2e}".format(U0))
print("B = {:5.2e}".format(B0))

tStart = 0
tEnd = 1e-7
dt = 1e-11


def E_Feld(x,y,z, t):
    Ex = U0 / (2 * d**2) * x
    Ey = U0 / (2 * d**2) * y
    Ez = - U0 / d**2 * z

    #return [0,0,Ez]
    return [Ex, Ey, Ez];

def B_Feld(x,y,z, t):
    Bx = 0;
    By = 0;
    Bz = B0;

    #return [0,0,0]
    return [Bx, By, Bz];

E = Field(E_Feld)
B = Field(B_Feld)
particle = Particle(r0, cp0, m, q)

comput = Computer(dt)
comput.start(E, B, particle, tStart, tEnd)

r = Drawer()
r.Draw(particle, tStart, tEnd, dt)
