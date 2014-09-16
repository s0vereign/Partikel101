# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 16:29:43 2014

@author: max
"""

import numpy as np

class Computer:
    
    def __init__(self, dt = 1e-3):
        self.dt = dt;
        self.c = 299792458 # m/s
    
    def step(self, E, B, particle, t):
        F = particle.getQ() * (
                E.calcField( particle.getCurrentPos(), t ) + 
                    np.cross(
                        particle.getV(),
                        B.calcField( particle.getCurrentPos(), t)
                    )
            );
        gamma = 1 / np.sqrt(1 - particle.getV()**2 / self.c**2)
        a = F / (particle.getM() * gamma);
        
        #velocity-verlet-algorithms, see http://www.vizgep.bme.hu/letoltesek/targyak/BMEGEVG1MOD/verlet.pdf
        r = particle.getCurrentPos() + particle.getV() * self.dt + 1.0/2 * particle.getA() * self.dt**2
        v = particle.getV() + 1 / 2.0 * ( particle.getA() + a ) * self.dt
        
        particle.addPos(r);
        particle.setV(v);
        particle.setA(a);
       
        
    def start(self, E, B, particle, start, end):
        for t in np.arange(start, end, self.dt):
            self.step(E, B, particle, t)
