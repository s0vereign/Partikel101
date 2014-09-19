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
#        print("------------------------------")
#        print("T:", t)
#        print("Gamma:", gamma)
#        print("CP:", particle.getCurrentcp())
#        print("Beta:", particle.getBeta())
#        print("v:", np.linalg.norm(particle.getCurrentcp() * Constants.c / (gamma * particle.getM())))
        F = particle.getQ() * (
                E.calcField( particle.getCurrentPos(), t ) + 
                    np.cross(
                        particle.getCurrentcp() * Constants.c / ( gamma * particle.getM()),
                        B.calcField( particle.getCurrentPos(), t)
                    )
            );
        #a = F / (particle.getM() * gamma);
        a = F / (particle.getM() * 1e6) * Constants.c**2 * 1e10
        print("v:", particle.getCurrentcp())
        print("a:", a)
        
        #velocity-verlet-algorithms, see http://www.vizgep.bme.hu/letoltesek/targyak/BMEGEVG1MOD/verlet.pdf
        r = particle.getCurrentPos() + (Constants.c * particle.getCurrentcp())/(gamma*particle.getM()) * self.dt + \
            1.0/2 * a * self.dt**2 
            
        print("a:", a)
        cp = particle.getCurrentcp() + a * self.dt / Constants.c**2 * particle.getM() * gamma
        print("v_neu", cp* np.linalg.norm(particle.getCurrentcp()) / np.linalg.norm(cp))
        #cp = cp* np.linalg.norm(particle.getCurrentcp()) / np.linalg.norm(cp)
        
        particle.addPos(r);
        particle.addcp(cp);
        #particle.setA(a);
        
       
        
    def start(self, E, B, particle, start, end):
        r = particle.getBeta()*particle.getGamma()*particle.getM()/(Constants.c*0.2)*1e6
        print(r)
        #for i in range(start, end):
        for t in np.arange(start, end, self.dt):
            self.step(E, B, particle, t)
        #print("{:5.1f} %".format((i+1)/end*100))

    
