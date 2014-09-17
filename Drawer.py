# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 16:29:15 2014

@author: max
"""



import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from __future__ import division
import matplotlib.pyplot as plt

class Drawer:
    
    
     
    
    def __init__(self,r,v):
    
        self.r = r;
        self.v = v;        
        
        
    def Draw(self):
        """        
        Draws the calculated trajectory
        
        
        """
        
        fig = plt.figure();
        ax = fig.gca(projection='3d')
        
        x = [];
        y = [];
        z = [];        
        
        
        for i in self.r:
            
            x.append(i[0]);
            y.append(i[1]);
            z.append(i[2]);
                      
        #ax = fig.gca(projection='3d');
        ax.plot(x,y,z,label = 'Tajectory');
        ax.legend();
        plt.show()
        
        
     def Draw_Ekin(self,ekin,t_start,t_end,dt):   
         
         
         t =  np.arange(t_start,t_end,dt);
         plt.title('PLotting the Kinetic Energy');
         plt.plot(t,ekin);
         plt.ylabel('Kinetic Energy [J]');
         plt.xlabel('Time');
         plt.show();
            
        
    