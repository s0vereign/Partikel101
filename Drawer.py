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
        
    def Draw(self, particle, t_start, t_end, dt):
        """        
        Draws the calculated trajectory
        """
        r = particle.getTrajectory();
        ekin = particle.getKineticEnergy();
        
        trigs = particle.getTriggers();
        E = particle.getField();
        z1 = particle.getZ();
        
        x,y,z = [], [], []
        for i in r:
            x.append(i[0]);
            y.append(i[1]);
            z.append(i[2]);
            
        t =  np.arange(t_start,t_end + dt,dt);
        
        fig = plt.figure(figsize=(8,6));
        gs = gridspec.GridSpec(3, 1, height_ratios=[4, 2, 2])
        
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
        
        for i in range(len(trigs)):
            xy1 = trigs[i]
            ax.annotate('Cavity',xy = (xy1[0],xy1[1]), xytext = (xy1[0],xy1[1]+10), arrowprops=dict(facecolor='black', shrink=0.05))
        ax.set_ylim(0,60);
        
        ax = fig.add_subplot(gs[2])
        ax.plot(z1,E);     
        ax.set_xlabel('$z$');
        ax.set_ylabel('$MeV/m$');
        
        plt.show()
