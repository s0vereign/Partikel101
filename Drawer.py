# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 16:29:15 2014

@author: max
"""


from __future__ import division
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import gridspec
import matplotlib.pyplot as plt
import numpy as np

class Drawer:
    def __init__(self):
        pass    
        
    def Draw(self, r, ekin, t_start, t_end, dt):
        """        
        Draws the calculated trajectory
        """
        x,y,z = [], [], []
        for i in r:
            x.append(i[0]);
            y.append(i[1]);
            z.append(i[2]);
            
        t =  np.arange(t_start,t_end + dt,dt);
        
        fig = plt.figure(figsize=(8,6));
        gs = gridspec.GridSpec(2, 1, height_ratios=[4, 1])
        
        ax = fig.add_subplot(gs[0], projection='3d')
        ax.plot(x,y,z,label = 'Trajectory');
        ax.set_xlabel("$\mathbf{\hat{x}}$")
        ax.set_ylabel("$\mathbf{\hat{y}}$")
        ax.set_zlabel("$\mathbf{\hat{z}}$")
        ax.legend();
        
        ax = fig.add_subplot(gs[1])
        #ax.title('Plotting the Kinetic Energy');
        ax.plot(t,ekin);
        ax.set_ylabel('Kinetic Energy [MeV]');
        ax.set_xlabel('Time [s]');
        
        plt.show()
