Partikel101
===========

Simulation for relativistic particles in electromagnetic fields. 
Project during internship Helmholtz Zentrum Dresden-Rossendorf www.hzdr.de

Language: Python
Libraries: SciPy(incl. Matplotlib etc.)

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
