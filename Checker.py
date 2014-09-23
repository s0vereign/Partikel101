# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 13:35:36 2014

Ignore this Class!

@author: max
"""

from __future__ import division
import scipy as sc
import numpy as np




class Checker:
    
    
    def __init__(self,particle,height,length,width):
        
        
        self.particle  = particle;
        self.height = height;
        self.length = length;
        self.width = width;




    def checkposX(self):
        
        if(particle.getCurrentPos()[1]>=length or particle.getCurrentPos()[1]<=0):
            
            return True
        else:
            
            return False
            
    def checkposY(self):
        
        if(particle.getCurrenPos()[0]>=height or particle.getCurrentPos()[0]<= 0):
            
            particle.addPos([0,0,0]);
            
            return True
            
        else:
            
            return False