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
                 cp0 = np.array([0,0,0]),
                 m = 1,
                 q = 1):
        """Initialise all relevant properties.
        """
        self.cp0 = cp0; #MeV
        self.r0 = r0;   #in m
        self.cp = [];   #in MeV
        self.r = [];    #in m
        self.a = 0;     #in m/s^2
        self.m = m;     #in MeV/c^2
        self.q = q;     #in elementary charges Q  = n*e
    
    def getCurrentcp(self):
        """Returns the current velocity of the particle (last entry of all
           tracked velocities)
        """
        return self.cp[-1::1].pop() if self.cp[-1::1] else self.cp0;
    
    def getA(self):
        """Returns current acceleration
        """
        return self.a;
    
    def getM(self):
        """Returns the mass of the particle
        """
        return self.m;
    


    def getBeta(self,cp):
        
        """
        Gets the particle impuls and returns the 
        beta as an scalar!
        """
        
        return (np.linalg.norm(cp)*(1/(Constants.c**2*self.getM())));


    def getGamma(self,Beta):
        """
        gets the Beta = v/c and returns the Gamma
        
        """
        
        return 1/(np.sqrt(1-Beta**2));
        
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
        
    def addcp(self, cp):
        """ Updates current velocity
        """
        self.cp.append(cp);
        
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
        return [(np.linalg.norm(cp)*1/(Constants.c*self.getM())) for cp in self.cp];
        
    def getKineticEnergy(self, factor = 1, electronVolt = True):
        """Returns the kinetic energy, standard: MeV         
        """
        
        return [((self.getGamma((self.getBeta(cp)))-1)*self.getM()*Constants.c**2) for cp in self.cp]; 
        
        
        
        
        
        