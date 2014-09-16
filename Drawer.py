# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 16:29:15 2014

@author: max
"""


import matplotlib as mp
from scipy import numpy as np
class Drawer:
    
    
    r = np.array();
    x = [];    
    y = [];
    z = [];    
    
    def __init__(self):
    
        pass;
    
    
    def setTraj(t):
        
        """
        Gets a Array of R^3 Vectors
        and safes it to r                
        
                    
        """
        
        r = t; 
        
    def Draw():
        """        
        Draws the calculated trajectory
        
        
        """
        
        fig = plt.figure();
        for i in range(len(r)):
            
            vh = r[i];
            
            x.append(vh[1]);
            y.append(vh[2]);
            z.append(vh[3]);
                      
        ax = fig.gca(projection='3d');
        ax.plot(x,y,z,label = 'Tajectory');
        ax.legend();
        plt.show()
            
            
        