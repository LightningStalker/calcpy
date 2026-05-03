#!/bin/python
# Series Section Transformers
# From ARRL Antenna Book, 23rd Edition ©2015
# Project Crew™ 5/3/2026

from math import pi, tau, sqrt, atan, fabs, floor, ceil

# SWR calc
def swr(Rl: float, Xl: float, Z0: float) -> float:
    R:   float = Rl / Z0
    X:   float = fabs(Xl) / Z0
    B:   float = ( (X * X + 1) / R ) + R
    return( ( B + sqrt(B * B - 4) ) / 2 )

# input
print()
while True:
    value = input('  Frequency (MHz)......................: ')
    try:
        f: float = float(value)
    except ValueError:
        print('  Valid number, please')
        continue
    if 0.135 <= f <= 1000.0:
        break
    else:
        print('  Valid range, please: 0.135-1,000MHz')

while True:
    value = input('  Load real (\u2126)........................: ')
    try:
        Rl: float = float(value)
    except ValueError:
        print('  Valid number, please')
        continue
    if 1.0 <= Rl <= 10000.0:
        break
    else:
        print('  Valid range, please: 1-10,000')

while True:
    value = input('  Load imaginary (\u00b1j)..................: ')
    try:
        Xl: float = float(value)
    except ValueError:
        print('  Valid number, please')
        continue
    if -10000.0 <= Xl <= 10000.0:
        break
    else:
        print('  Valid range, please: \u00b110,000')

while True:
    value = input('  Line impedance (\u2126)...................: ')
    try:
        Z0: float = float(value)
    except ValueError:
        print('  Valid number, please')
        continue
    if 25.0 <= Z0 <= 600.0:
        break
    else:
        print('  Valid range, please: 25-600')

while True:
    value = input('  Line velocity factor (VF)............: ')
    try:
        v0: float = float(value)
    except ValueError:
        print('  Valid number, please')
        continue
    if 0.5 <= v0 <= 1.0:
        break
    else:
        print('  Valid range, please: 0.5-1.0')

SWR: float =   swr(Rl, Xl, Z0)
Z1a: float =  ceil( Z0 * sqrt(SWR) )
Z1b: float = floor( Z0 / sqrt(SWR) )

print('  SWR = ', round(SWR, 3), ', so matching section has to be ', Z1a, '\u2126 or above or ', Z1b, '\u2126 and lower.', sep='')

while True:
    value = input('  Matching section impedance (\u2126).......: ')
    try:
        Z1: float = float(value)
    except ValueError:
        print('  Valid number, please')
        continue
    if 25.0 <= Z1 <= 600.0:
        pass
    else:
        print('  Valid range, please: 25-600')
        continue
    if Z0 != Z1:
        pass
    else:
        print('  Line and matching section are the same!')
    if Z1a > Z1 > Z1b:
        print('  It can\'t be between ', Z1b, ' and ', Z1a, '.', sep='')
    else:
        break

while True:
    value = input('  Matching section velocity factor (VF): ')
    try:
        v1: float = float(value)
    except ValueError:
        print('  Valid number, please')
        continue
    if 0.5 <= v1 <= 1.0:
        break
    else:
        print('  Valid range, please: 0.5-1.0')

# main() {
# wavelength in meters
wm: float = 299.792458 / f

# ... the imperial units
wf: float = 984.0 / f

# VF correction
m0: float = wm * v0
m1: float = wm * v1
f0: float = wf * v0
f1: float = wf * v1

# SSTrafo calc
n:  float = Z1 / Z0
r:  float = Rl / Z0
x:  float = Xl / Z0
# print('n =', n, 'r =', r, 'x =', x)

B:  float = sqrt( ( (r - 1) ** 2 + x * x ) / ( r * (n - 1 / n) ** 2 - (r - 1) ** 2 - x * x ) )
L2: float = atan(fabs(B)) / tau
A:  float = ( (n - r / n) * B + x ) / ( r + x * n * B - 1 )
if A > 0:
    L1: float = atan(A) / tau
else:
    L1: float = ( atan(A) + pi ) / tau  # add 180° if A is negative

# output
print('\n    \u21132 is length of matching section.  \u21131 is length of line from the matching')
print('  section to the load.\n')
print('    metric:')
print('  \u21131 = {:8.3f}m,  \u21132 = {:8.3f}m'.format(L1 * m0, L2 * m1), sep='', end='\n\n')
print('    imperial:')
print('  \u21131 = {:7.2f}ft,  \u21132 = {:7.2f}ft'.format(L1 * f0, L2 * f1), sep='', end='\n\n')
