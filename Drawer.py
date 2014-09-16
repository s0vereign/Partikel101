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
        for i in self.r:
            
            x.append(i[0]);
            y.append(i[1]);
            z.append(i[2]);
                      
        #ax = fig.gca(projection='3d');
        plt.plot(x,y,z,label = 'Tajectory');
        plt.legend();
        plt.show()
            
            
        