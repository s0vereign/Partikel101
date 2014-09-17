# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 16:26:04 2014

@author: max
"""

import numpy as np

from Constants import Constants

class Particle:
    """Particle contains importent properties and methods for 
       describing a particle
    """
    def __init__(self, 
                 r0 = np.array([0,0,0]),
                 v0 = np.array([0,0,0]),
                 m = 1,
                 q = 1):
        """Initialise all relevant properties.
        """
        self.v0 = v0;
        self.r0 = r0;
        self.v = [];
        self.r = [];
        self.a = 0;
        self.m = m;
        self.q = q;
    
    def getCurrentV(self):
        """Returns the current velocity of the particle (last entry of all
           tracked velocities)
        """
        return self.v[-1::1].pop() if self.v[-1::1] else self.v0;
    
    def getA(self):
        """Returns current acceleration
        """
        return self.a;
    
    def getM(self):
        """Returns the mass of the particle
        """
        return self.m;
        
    def getQ(self):
        """Returns the charge (in coulombs) of the particle
        """
        return self.q;
        
    def getCurrentPos(self):
        """Returns current position (last entry of trajectory-list)
        """
        return self.r[-1::1].pop() if self.r[-1::1] else self.r0
    
    def addPos(self, r):
        """ Adds a position to the list of positions (= the trajectory).
            Numpy-Array (3) expected!
        """
        self.r.append(r);
        
    def addV(self, v):
        """ Updates current velocity
        """
        self.v.append(v);
        
    def setA(self, a):
        """Updates the particle's current acceleration
        """
        self.a = a;
        
    def getTrajectory(self):
        """Returns the list of positions (= the trajectory)
        """

        return self.r;
        
    def getVelocities(self):
        """Returns all available velocities
        """
        return self.v;
        
    def getKineticEnergy(self, factor = 1, electronVolt = True):
        """Returns the kinetic energy, standard: electron volts (alternative: Joule)
           with any factor (e.g. factor = 10^6 = 1M -> Megaelectron volts/Joule)
        """
        AbsVector = lambda vVec: np.linalg.norm(vVec);
        EkinJoule = lambda v: (1 / np.sqrt(1 - AbsVector(v)**2 / Constants.c**2) - 1) * self.m * Constants.c**2;
        if electronVolt:
            return [ EkinJoule(v) * Constants.e / factor for v in self.v] # Ekin in eV
        else:
            return [EkinJoule(v) / factor for v in self.v] # Ekin in Joule