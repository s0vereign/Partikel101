# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 16:26:04 2014

@author: max
"""

from __future__  import division
import numpy as np

from Constants import Constants

class Particle:
    """
    Particle contains importent properties and methods for 
    describing a particle
    """
    def __init__(self, 
                 r0 = np.array([0,0,0]),
                 cp0 = np.array([0,0,0]),
                 m = 1,
                 q = 1):
        """Initialise all relevant properties.
        """
        self.cp = [cp0];   #in MeV
        self.r = [r0];     #in m
        self.a = 0;        #in m/s^2
        self.m = m;        #in MeV/c^2
        self.q = q;        #in elementary charges Q  = n*e
        self.z = []; 
        self.E = []        
        
    def getCurrentcp(self):
        """
        Returns the current velocity of the particle (last entry of all
           tracked velocities)
        """
        return self.cp[-1];
    
    def getA(self):
        """
        Returns current acceleration
        """
        return self.a;
    
    def getM(self):
        """
        Returns the mass of the particle
        """
        return self.m;
    
    def getBeta(self):
        """
        Gets the particle impuls and returns the 
        beta as an scalar!
        """
        return np.sqrt(1 - 1 / self.getGamma()**2)

    def getGamma(self):
        """
        returns gamma
        """
        return np.sqrt(np.linalg.norm(self.getCurrentcp())**2 / self.getM()**2 + 1);        
        
    def getQ(self):
        """
        Returns the charge (in coulombs) of the particle
        """
        return self.q;
        
    def getCurrentPos(self):
        """
        Returns current position (last entry of trajectory-list)
        """
        return self.r[-1]
    
    def addPos(self, r):
        """ 
        Adds a position to the list of positions (= the trajectory).
        Numpy-Array (3) expected!
        """
        self.r.append(r);
        
    def addcp(self, cp):
        """
        Updates current velocity
        """
        self.cp.append(cp);
        
    def setA(self, a):
        """
        Updates the particle's current acceleration
        """
        self.a = a;
        
    def getTrajectory(self):
        """
        Returns the list of positions (= the trajectory)
        """
        return self.r;
        
        
        
    def getKineticEnergy(self, factor = 1, electronVolt = True):
        """
        Returns the kinetic energy, standard: MeV         
        """
        return [np.sqrt(np.linalg.norm(cp)**2 + self.getM()**2) for cp in self.cp];
    
    def getZeroes(self,n):
                
        """
        Helping method to indicate the location between the Cavities
        Idea: According to the models of cavity resonators, the Field
        is zero when the particle is between two resonators!
        """
        
        
        self.z.append(n);
    def saveField(E):
        """
        Saves the Field it's in!
        
        """
        
    def getKineticEnergy2(self):            
        
        """
        Alternativ way to calc the kinetic Energy
        Returns the kinetic Energy of the whole run
        as an array!
        

        """                
        
        
        E_temp = []        
        g = []
        for i in range(len(self.cp)):
            
            g.append(np.sqrt(np.linalg.norm(self.cp[i])**2/ self.getM()**2 + 1));
            
        for j in range(len(self.cp)):
            
            cp1 = (g[j]-1)*self.getM();
            
            E_temp.append(cp1);
        
        return E_temp;
                    