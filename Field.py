# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 16:17:03 2014

@author: max

Description: returnfield returns a magnetic or elecrical field 
vector. calcfield calculates the field

"""

import SciPy

class Field:
    
    def __init__(self, f):
        self.field = f;
        
    #@Override
    def returnField(self, x,y,z,t):
        return self.field;
        
        
    #@Override
    def calcField(self, x,y,z,t):
        return self.field(x,y,z,t);
        
        
    