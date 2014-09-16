# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 16:17:03 2014

@author: max

Description: returnfield returns a magnetic or elecrical field 
vector. calcfield calculates the field

"""

import scipy as sc
import matplotlib as mp
import numpy as np

class Field:
<<<<<<< HEAD
    #@Override
        
    def __init__ Field(self):
        
        
        

    def returnfied(x,y,z,t):
        
        
=======
    
    def __init__(self, f):
        self.field = f;
        
>>>>>>> 765aeb77b860e67d3806478eea67deeb8202067f
    #@Override
    def returnField(self, x,y,z,t):
        return self.field;
        
        
    #@Override
    def calcField(self, x,y,z,t):
        return self.field(x,y,z,t);
        
        
    