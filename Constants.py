# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 09:23:10 2014

@author: dani
"""

import math
import numpy as np

class Constants:
    c = 299792458; # m/s
    e = 1;# coulombs
    
    #masses in MeV / c**2
    me = 0.510;
    mp = 938.27;     
    mn = 939.565;    
    rf = 1.3e9;
    w  = 2*math.pi*rf;
    lamb = c/rf;
    U = 20.; #V/m
    
    """
    Definition of the quadrupol field!
    here we set where the 4 Charges will be placed
    and calculate the following norms of them!
    
    """
    
    rq1 = np.array([0,0,0]);
    rq2 = np.array([0,0,0]);
    rq3 = np.array([0,0,0]);
    rq4 = np.array([0,0,0]);
    d1  = rq1 - rq2;
    d2  = rq3 - rq4;
    d1b = np.linalg.norm(d1);
    d2b = np.linalg.norm(d2);
    
