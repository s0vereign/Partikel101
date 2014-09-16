# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 16:26:04 2014

@author: max
"""

import numpy as np

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
        self.v = v0;
        self.r = [r0];
        self.a = 0;
        self.m = m;
        self.q = q;
    
    def getV(self):
        """Returns the current velocity of the particle
        """
        return self.v;
    
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
        return self.r[-1::1].pop()
    
    def addPos(self, r):
        """ Adds a position to the list of positions (= the trajectory).
            Numpy-Array (3) expected!
        """
        self.r.append(r);
        
    def setV(self, v):
        """ Updates current velocity
        """
        self.v = v;
        
    def setA(self, a):
        """Updates the particle's current acceleration
        """
        self.a = a;
        
    def getTrajectory(self):
        """Returns the list of positions (= the trajectory)
        """

        return self.r;
        
        
        
