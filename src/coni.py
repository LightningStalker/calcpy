#!/bin/python
# Inductance of the inverse conical coil
# Base on work of Tesla coils "community"
# Project Crew™ 9/6/2026

from math import pi, pow, sqrt, sin, cos, tan, atan

# deg2rad = lambda deg: deg * pi / 180.0  # Convert degrees to radians

# measure twice, calculate n*unce
# units are the millimeters (mm)
# from center (+) of the wire
N   = 7.68                              # turns count
D   = 176.9                             # outer diameter
H   = 32.193                            # height
W   = 64.9                              # from turns start to outer edge...
                                        #   measure flat to the base
# compute some values
Ro  = D / 2                             # outer radius
Ri  = Ro - W                            # inner radius
a   = atan(H / Ro)                      # slope angle in radians
R   = (Ri + Ro) / 2                     # mean radius
# p_v = tan(a) * R / N                    # pitch of winding
# p   = W / N

# Wheeler28/Terman43 in millimeters
L1 = 5 * pow( (N * R), 2 ) / (1143 * R + 1270 * H)  # Solenoid component
L2 = 5 * pow( (N * R), 2 ) / (1016 * R + 1397 * W)  # Planar     ...
# print( 'L1 =', L1, ': L2 =', L2)
print( 'L = {:0.3f}'.format( sqrt( pow(L1 * sin(a), 2) + pow(L2 * cos(a), 2) ) ), '\u00b5H' )

# i  = sqrt( 635 * L1 ** 2 * p_v ** 2 + 9 * L1 * R ** 3 )
# print( 'N =', ( sqrt(635) * i + 635 * L1 * p_v ) / (5 * R ** 2) )
# L1 = pow(L1 * sin(a), 2)
# print(sqrt((580644*p_v*L1*R**2*sin(a))/(127*sqrt(L1)*(5*sin(a)**2*R**3)*p_v)+(64516*p_v**2*L1)/(sin(a)**2*R**4))/2+(127*sqrt(L1)*p_v)/(R**2*sin(a)))
