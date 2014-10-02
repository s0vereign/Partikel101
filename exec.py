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

roh0 = 8e-5#m
z0 = roh0 / np.sqrt(2)#m
d = np.sqrt(1.0/2 * (z0**2 + roh0**2 / 2))
#d = 10e-3#m
print(d)

m = 4*cons.mp#MeV
q = 2

r = roh0 * 2./3.#m


n1 =  1/3.# = omega_plus / omega_minus
n2 =  1# = omega_plus / omega_z
r0 = np.array([0.0,0.0,z0/2])

omega_plus = 1e9
omega_minus = omega_plus/n1
omega_c = omega_plus + omega_minus
omega_z = omega_plus/n2

B0 = omega_c * m * 1e6  / ( q * cons.c**2 )
U0 = omega_z**2 * m * 1e6 / ( q * cons.c**2 ) * d**2

#assert omega_c * r < cons.c, "\omega_- * r too great!"

cp0 = m * np.sqrt( 1.0 / (1 - omega_c**2 * r**2 / cons.c**2) - 1) * np.array([1,0,0]) # m * sqrt(gamma**2 - 1) * e_cp0

print("f_c = {:5.2e} Hz".format(omega_c / 2 / np.pi))
print("f_+ = {:5.2e} Hz".format(omega_plus / 2 / np.pi))
print("f_- = {:5.2e} Hz".format(omega_minus / 2 / np.pi))
print("f_z = {:5.2e} Hz".format(omega_z / 2 / np.pi))

print(r"\frac \omega_+ \omega_- = {:5.2e}".format(omega_plus / omega_minus))
print(r"\frac \omega_+ \omega_z = {:5.2e}".format(omega_plus / omega_z))

print("U = {:5.2e} V".format(U0))
print("B = {:4.2f} T".format(B0))

print("\roh_0 = {:5.2e} m".format(roh0))
print("cp_0 = {:5.2e} MeV".format(np.linalg.norm(cp0)))

print("############################################")
print("#              Backtracking                #")
print("############################################")

o_c = q * B0 * cons.c**2 / (m * 1e6)
o_z = np.sqrt(q * U0 * cons.c**2 /(m * 1e6 * d**2))

assert o_c**2 / 2 >= o_z**2, "\omega_c too small against \omega_z"

o_p = o_c / 2 + np.sqrt(o_c**2 / 4 - o_z**2 / 2)
o_m = o_c / 2 - np.sqrt(o_c**2 / 4 - o_z**2 / 2)

assert o_m < o_z < o_p, "\omega_- < \omega_z < \omega_+ condition not fulfilled!"

print("\Delta f_c = {:5.2e}".format(omega_c / o_c))
print("\Delta f_z = {:5.2e}".format(omega_z / o_z))
print("\Delta f_+ = {:5.2e}".format(omega_plus / o_p))
print("\Delta f_- = {:5.2e}".format(omega_minus / o_m))
	
print("\\frac f_+ f_- = {:5.2e}".format(o_p / o_m))
print("\\frac f_+ f_z = {:5.2e}".format(o_p / o_z))

print("f_+ = {:5.2e} Hz".format( o_p / 2 / np.pi))
print("f_- = {:5.2e} Hz".format( o_m / 2 / np.pi))
print("f_z = {:5.2e} Hz".format( o_z / 2 / np.pi))
print("f_c = {:5.2e} Hz".format( o_c / 2 / np.pi))

tStart = 0
tEnd = 5e-8
dt = 1e-11


def E_Feld(x,y,z, t):
    Ex = U0 / (2 * d**2) * x
    Ey = U0 / (2 * d**2) * y
    Ez = - U0 / d**2 * z

    #return [0,0,0]
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

print(r"\beta = {:5.2e}".format(particle.getBeta()))

comput = Computer(dt)
comput.start(E, B, particle, tStart, tEnd)

r = Drawer()
r.Draw(particle, tStart, tEnd, dt)
