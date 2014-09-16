# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 16:29:43 2014

@author: max
"""

import numpy as np
import scipy.integrate as intg

class Computer:
    
    def __init__(self, dt = 1e-3):
        self.dt = dt;
        self.c = 299792458 # m/s
    
    def step(self, E, B, particle, t):
        
        #compute lorentz-force: F = q(E + v x B)
        F = lambda t, E, B, particle, direction: np.dot(
                    particle.getQ() * (
                        E.calcField( particle.getCurrentPos(), t ) + 
                        np.cross(
                            particle.getV(),
                            B.calcField( particle.getCurrentPos(), t)
                        )
                    ),
                    direction
            )
        end = [
            self.integrate(F, t, t + self.dt, (E, B, particle, np.array([1,0,0]))),
            self.integrate(F, t, t + self.dt, (E, B, particle, np.array([0,1,0]))).
            self.integrate(F, t, t + self.dt, (E, B, particle, np.array([0,0,1])))
        ];
        
        
        #unit-vector of the velocity of the particle
        Fend = F(t + self.dtdt, E, B, particle, np.array([1,1,1]));
        mag = np.linalg.norm(np.array(end));
        ev = 1 / np.linalg.norm(Fend) * Fend;
        v = np.sqrt(mag**2*self.c**2 / (particle.getM**2 * self.c**2 + mag**2))
        v = v * ev + particle.getV()
        #r
        r = particle.getCurrentPos() + particle.getV()*self.dt + v*self.dt
        particle.addPos(r)
        particle.setV(v)
        
    
    def integrate(F, start, end, arg):
        return intg.quad(F, start, end, args = arg)
        
    def start(self, E, B, particle, start, end):
        for t in range(start, end, self.dt):
            self.step(E, B, particle, t)