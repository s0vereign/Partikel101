# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 11:02:26 2014

@author: max

 This is the executing script for 
 Project Particle 101


"""

import numpy as np

from Computer import Computer
from Drawer   import Drawer
from Particle import Particle
from Field    import Field

E = Field(lambda : 0)
B = Field(lambda : 0)
electron = Particle(np.array([0,0,0]), np.array([0,0,0]), 9.10938291e-31, 1.60217657e-19)

comput = Computer()
comput.start(E, B, electron, 0, 10)


r = Drawer(electron.getTrajectory())
r.Draw()