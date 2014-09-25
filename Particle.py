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
    def getPos(self,i):
        
        """
        returns the r of a certain index in the
        position field
        
        """
        
        return self.r[i];        
        
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
    
    def calcKineticEnergy(self,cp):
        """
        Takes cp as argument and the returns the kinetic Energy for this CP
        """        
        
        
        return np.sqrt(np.linalg.norm(cp)**2 + self.getM()**2)
    def saveField(self,E):
        """
        Saves the Field it's in!
        
        """
        self.E.append(E);
        
    def Trigger(self,t,cp):
        """
        Computer 'Triggers' if end of Cavity is reached
        and saves it with this method into the cavity 
        """        
        
        
        self.z.append([t,self.calcKineticEnergy(cp)]);
    
    def getTriggers(self):
        
        """
        returns all the saved triggerevents from above
        """
        return self.z ;