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
    
    def step(self, E, B, particle, t,n):
        """
        Calculates the Current position and momentum with the 
        Velocity verlet Algorithm. It also saves the calculated things
        into the particle. 
        """
        B1 = B.calcField( particle.getCurrentPos(), t);
        E1 = E.calcField(particle.getCurrentPos(),t);
        gamma = particle.getGamma();
        
        F = particle.getQ() * (
                E1 + 
                    np.cross(
                        particle.getCurrentcp() * Constants.c / ( gamma * particle.getM()),
                          B1
                    )
            );
        a = F / (particle.getM() * 1e6 * particle.getGamma()) * Constants.c**2
        
        #velocity-verlet-algorithms, see http://www.vizgep.bme.hu/letoltesek/targyak/BMEGEVG1MOD/verlet.pdf
        r = particle.getCurrentPos() + (Constants.c * particle.getCurrentcp())/(gamma*particle.getM()) * self.dt + \
            1.0/2 * a * self.dt**2 
               
        #cp = particle.getCurrentcp()+F*self.dt*Constants.c;
        aGes = a
        eCp = particle.getCurrentcp() / np.linalg.norm(particle.getCurrentcp());
        aP = np.dot(aGes, eCp) * eCp
        aV = aGes - aP
                
        cp_1 = particle.getCurrentcp() + aP * self.dt * particle.getM() * gamma / Constants.c
        cp_2 = cp_1 + aV * self.dt * particle.getM() * gamma / Constants.c
        cp = cp_2 / np.linalg.norm(cp_2) * np.linalg.norm(cp_1)
        
        particle.saveField(E1[2]);
        particle.saveZ(r[2]);
        particle.addPos(r);
        particle.addcp(cp);
        particle.setA(a);
        rval = np.linalg.norm(r-particle.getPos(0)); #|r-r0|
        
        if(rval >= n*Constants.lamb*0.5):#if n*lambda/2 reached?
            particle.Trigger(t,particle.calcKineticEnergy(cp));#if so trigger 
            n +=1                                              
            
        return n
        
    def start(self, E, B, particle, start, end,n = 0):
        for t in np.arange(start, end, self.dt):
           n =  self.step(E, B, particle, t,n)
