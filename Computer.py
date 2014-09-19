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
                        particle.getCurrentcp() * Constants.c / (gamma * particle.getM()),
                        B.calcField( particle.getCurrentPos(), t)
                    )
            );
        #a = F / (particle.getM() * gamma);
        e__ = 1.60217657e-19
        a = F * Constants.c**2 / particle.getM() * e__**2
#        print("F:", F)
#        print("a:", a)

        ev = particle.getCurrentcp() / np.linalg.norm(particle.getCurrentcp())
        a_p = np.dot(particle.getA(), ev) * ev
        if np.linalg.norm(a_p) < 1e-9:
            a_p = np.array([0,0,0])
        a_s = particle.getA() - a_p
        
        #velocity-verlet-algorithms, see http://www.vizgep.bme.hu/letoltesek/targyak/BMEGEVG1MOD/verlet.pdf
        r = particle.getCurrentPos() + (particle.getCurrentcp())/(gamma*particle.getM()) * self.dt + \
            1.0/2 * particle.getA() * self.dt**2 
        cp = particle.getCurrentcp() + particle.getA()*self.dt*Constants.c**2*particle.getM();

        cp_1 = particle.getCurrentcp() + a_p * self.dt * Constants.c**2 * particle.getM()
        cp_2 = cp_1 + a_s * self.dt * Constants.c**2 * particle.getM()
        cp = cp_2 / np.linalg.norm(cp_2) * np.linalg.norm(cp_1)
        
#        print("a_p", np.linalg.norm(a_p))
#        print("|cp_1|", np.linalg.norm(cp_1))
#        print("|cp|", np.linalg.norm(cp))
        
        particle.addPos(r);
        particle.addcp(cp);
        particle.setA(a);
        
       
        
    def start(self, E, B, particle, start, end):
        r = particle.getBeta()*particle.getGamma()*particle.getM()/(Constants.c*0.2)
        print(r)
        for i in range(start, end):
            for t in np.arange(i, i+1, self.dt):
                self.step(E, B, particle, t)
            print("{:5.1f} %".format((i+1)/end*100))

    
