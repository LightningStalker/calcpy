#!/bin/python
# Inductance of the inverse conical coil
# Base on work of Tesla coils "community"
# Project Crew™ 9/6/2026

from math import pi, pow, sqrt, sin, cos, tan

deg2rad = lambda deg: deg * pi / 180.0  # Convert degrees to radians

# measure twice, calculate n*unce
# units are the millimeters (mm)
N  = 7.68                               # turns count
a  = deg2rad(20)                        # slope angle
R  = 56                                 # mean radius
H  = tan(a) * R                         # height
W  = 64.9                               # from turns start to outer edge
Ri = 23.55                              # inner radius
Ro = 88.45                              # outer radius

# Wheeler25/Terman43 in millimeters
L1 = 5 * pow( (N * R), 2 ) / (1143 * R + 1270 * H)  # Solenoid component
L2 = 5 * pow( (N * R), 2 ) / (1016 * R + 1397 * W)  # Flat spiral ...
print( 'L = {:0.3f}'.format( sqrt( pow(L1 * sin(a), 2) + pow(L2 * cos(a), 2) ) ), '\u00b5H' )
print( 'N =', sqrt( 1143 * L1 * R + 1270 * H * L1 ) / (sqrt(5) * R) )
