# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 16:26:04 2014

@author: max
"""

import numpy as np

class Particle:
    def __init__(self, 
                 r0 = np.array([0,0,0]),
                 v0 = np.array([0,0,0]),
                 v = np.array([0,0,0]),
                 m = 0,
                 q = 0):
        self.r0 = r0;
        self.v0 = v0;
        self.v = v;
        self.r = [];
        self.m = m;
        self.q = q;
           
    def returnall():
        pass
        
    def getR0(self):
        return self.r0;
    
    def getV0(self):
        """Returns the velocity of the particle
        """
        return self.v0;
    
    def getV(self):
        """Returns the current velocity of the particle
        """
        return self.v;
    
    def getM(self):
        """Returns the mass of the particle
        """
        return self.m;
        
    def getQ(self):
        """Returns the charge (in coulombs) of the particle
        """
        return self.q;
    
    def addPos(self, r):
        """ Adds a position to the list of positions (= the trajectory).
            Numpy-Array (3) expected!
        """
        self.r.append(r);
        
    def setV(self, v):
        """ Updates current velocity
        """
        self.v = v;
        
    def getTrajectory(self):
        """Returns the list of positions (= the trajectory)
        """
        return self.r;
        
        
        
        
        