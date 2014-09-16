# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 16:29:15 2014

@author: max
"""


import numpy as np
import matplotlib.pyplot as plt
class Drawer:
    
    
     
    
    def __init__(self,r):
    
        self.r = r;
           
    
    def setTraj(self,t):
        
        """
        Gets a Array of R^3 Vectors
        and safes it to r                
        
                    
        """
        
        self.r = t; 
        
    def Draw(self):
        """        
        Draws the calculated trajectory
        
        
        """
        
        x = [];
        y = [];
        z = [];        
        
        fig = plt.figure();
        for i in range(len(self.r)):
            
            vh = self.r[i];
            
            x.append(vh[1]);
            y.append(vh[2]);
            z.append(vh[3]);
                      
        ax = fig.gca(projection='3d');
        ax.plot(x,y,z,label = 'Tajectory');
        ax.legend();
        plt.show()
            
            
        