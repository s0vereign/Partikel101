# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 16:29:15 2014

@author: max
"""


from __future__ import division
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

class Drawer:
    
    
     
    
    def __init__(self):
        pass    
        
    def DrawTrajectory(self, r):
        """        
        Draws the calculated trajectory
        
        
        """
        
        fig = plt.figure();
        ax = fig.gca(projection='3d')
        
        x = [];
        y = [];
        z = [];        
        
        
        for i in r:
            
            x.append(i[0]);
            y.append(i[1]);
            z.append(i[2]);
                      
        #ax = fig.gca(projection='3d');
        ax.plot(x,y,z,label = 'Tajectory');
        ax.legend();
        plt.show()
        
    def DrawKineticEnergy(self,ekin,t_start,t_end,dt):   
         
             
             t =  np.arange(t_start,t_end,dt);
             print(len(t))
             print(len(ekin))
             plt.title('PLotting the Kinetic Energy');
             plt.plot(t,ekin);
             plt.ylabel('Kinetic Energy [eV]');
             plt.xlabel('Time');
             plt.show();
             
        
    """
    Draws the kinetic Energy 
    """
