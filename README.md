Partikel101
===========
!!!!!!!IMPORTANT:
Use the branch Units oder Penning if you would like to work with the code.!!!!!!



Simulation for relativistic particles in electromagnetic fields. 
Project during internship Helmholtz Zentrum Dresden-Rossendorf www.hzdr.de



Language: Python
Libraries: SciPy(incl. Matplotlib etc.)

It's now finished and will not be updated. 
The three branches: 

Master: Was the first prototype without correct units, only simulates a homogenic magnetic field and
        one electron.Note that this branch is the most useless.
        
units: Simulates a resonator cavity. ~1m length and an elektron starts with a kinetic energy of 20MeV

Penning: Simulates Ions in a Penning trap, the user has to configure the requiered frequency w_+ (See wikipedia or arxiv
         for more deails) the programm will calculate the rest. 




Usage:

    
    Update the functions E_Feld and B_Feld to your wanted fields,
    the parameters x, y, z and t are useable. The B-field's unit is Tesla,
    the unit of the electrical field is V/m.
    Change the values for your disered particle, whereas the first parameter
    is the beginning location in metre, the second vector is the velocity
    in m/s, followed by the mass in kg and it's charge in coulomb. Be aware
    of using to small numbers due to the limited precision of the computer
    at that small numbers for e.g. protons or electrons.
    At last set the start- and endtime in the line starting with
    comput.start by changing the 4th and 5th parameter (time in seconds). for
    more precise results change the dt-steps for the integration in the line
    above by inserting any number when creating Computer(<desired dt>),
    standard is 10^-3 seconds.
    The whole starting and inital conditions are in exec.py as the central 
    script to change all the possible conditions. The other classes are just
    intended to solve the rest. 
