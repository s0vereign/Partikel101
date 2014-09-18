# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 16:29:43 2014

@author: max
"""

import numpy as np

from Constants import Constants

class Computer:
    
    def __init__(self, dt = 1e-3):
        self.dt = dt;
    
    def step(self, E, B, particle, t):
        gamma = particle.getGamma(particle.getBeta(particle.getCurrentcp()));
        F = particle.getQ() * (
                E.calcField( particle.getCurrentPos(), t ) + 
                    np.cross(
                        particle.getCurrentcp()*Constants.c / (gamma * particle.getM()),
                        B.calcField( particle.getCurrentPos(), t)
                    )
            );
        a = F / (particle.getM() * gamma) * Constants.c**2;
        
        e_cp = particle.getCurrentcp()/np.linalg.norm(particle.getCurrentcp());
        a_p  = np.dot(a,e_cp)*e_cp;
        a_s  = a-a_p;
        
        
        #velocity-verlet-algorithms, see http://www.vizgep.bme.hu/letoltesek/targyak/BMEGEVG1MOD/verlet.pdf cp = particle.getCurrentcp() + 1 / 2.0 * ( particle.getA() + a ) *(gamma*Particle.getM())*1/Constants.c)* self.dt

        r = particle.getCurrentPos() + (particle.getCurrentcp()*Constants.c)/(gamma*particle.getM()) * self.dt + 1.0/2 * particle.getA() * self.dt**2
        
        cp_1 = particle.getCurrentcp() + a_p*self.dt*(gamma*particle.getM())/Constants.c;
        cp_2 = cp_1 + a_s*self.dt*(gamma*particle.getM())/Constants.c;        
        cp = cp_2/np.linalg.norm(cp_2)*np.linalg.norm(cp_1)        
        
        particle.addPos(r);
        particle.addcp(cp);
        particle.setA(a);
        
       
        
    def start(self, E, B, particle, start, end):
      
        for i in range(start, end):
            for t in np.arange(i, i+1, self.dt):
                self.step(E, B, particle, t)
            print("{:5.1f} %".format((i+1)/end*100))

    