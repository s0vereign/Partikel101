# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 16:29:43 2014

@author: max
"""
from __future__ import division
import numpy as np

from Constants import Constants

class Computer:
    
    def __init__(self, dt = 1e-3):
        self.dt = dt;

    
    def step(self, E, B, particle, t):
        gamma = particle.getGamma();
        F =(    particle.getQ()*
                E.calcField( particle.getCurrentPos(), t ) + 
                    np.cross(
                        particle.getCurrentcp() * Constants.c / ( gamma * particle.getM()),
                        B.calcField( particle.getCurrentPos(), t)
                    )
            );
        #a = F / (particle.getM() * gamma);
        a = F / (particle.getM() * 1e6 * particle.getGamma()) * Constants.c**2
#        print("v:", particle.getCurrentcp())
#        print("a:", a)
        
        #velocity-verlet-algorithms, see http://www.vizgep.bme.hu/letoltesek/targyak/BMEGEVG1MOD/verlet.pdf
        r = particle.getCurrentPos() + (Constants.c * particle.getCurrentcp())/(gamma*particle.getM()) * self.dt + \
            1.0/2 * a * self.dt**2 
            
#        print("a:", a)
        cp = particle.getCurrentcp() + a * self.dt * particle.getM() * gamma / Constants.c
#        print("v_neu", cp* np.linalg.norm(particle.getCurrentcp()) / np.linalg.norm(cp))
        cp = cp * np.linalg.norm(particle.getCurrentcp()) / np.linalg.norm(cp)
        
        particle.addPos(r);
        particle.addcp(cp);
        #particle.setA(a);
        
       
        
    def start(self, E, B, particle, start, end):
        r = particle.getBeta()*particle.getGamma()*particle.getM()*1e6/(Constants.c*0.2)
        print(r)

        for t in np.arange(start, end, self.dt):
            self.step(E, B, particle, t)

    
