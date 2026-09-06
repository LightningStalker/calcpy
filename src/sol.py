#!/bin/python
# Nagaoka-Rosa solenoid inductance calculation
# Compare to the D W Knight 'L_calcs.ods' ca. 1/11/2016
# Project Crew™ 4/19/2026
import sys
from math import pi, tau, log, sqrt, exp

f     = 144                             # frequency in MHz
N     = 9.2                             # turns count
dw    = 0.0045                          # coax shield/braid diameter
jw    = 0.0061                          # coax outer diam. incl. jacket
Df    = 0.0223                          # form diameter
D     = Df + jw                         # effective coil diameter
lWire = N * pi * D                      # length of the wire

RCu = 17.241                            # wire resistivity (copper)

def LxRosa(h: float, D: float, N: float, dw: float, p: float) -> float:
# External inductance in henrys of a round-wire solenoid, using the Nagaoka-Rosa method.
#  D W Knight. V 1.00, 2016-01-11
# Calls functions W82W(), KMGO() and Rosaks90()

# h  = coil length / m
# D  = coil diameter / m
# N  = number of turns
# dw = wire diameter / m
# p  = winding pitch / m
    kNagaoka: float = W82W(D / h)
    Lsheet:   float = 1e-7 * pi * pi * D * D * N * N * kNagaoka / h
    Rosacorr: float = KMGO(N) + Rosaks90(p / dw, p / D, 0)
    
    return(Lsheet - 2E-7 * pi * D * N * Rosacorr)

def W82W(x: float) -> float:
# calculates Nagaoka's coeff. using Wheeler 1982 eqn (7) as modified by
# Bob Weaver. Max error is +/- 21ppM.  D W Knight, June 2012.

# x = Diam. / length
    if x == 0:
        return(1)
    else:
        zk: float =  2.0  / (pi * x)
        k0: float =  1.0  / (log(8.0 / pi) - 0.5)
        k2: float = 24.0  / (3.0 * pi * pi - 16.0)
        w:  float = -0.47 / (0.755 + x) ** 1.44
        p:  float = k0 + 3.437 / x + k2 / (x * x) + w
        
        return(zk * (log(1.0 + 1.0 / zk) + 1.0 / p))

def KMGO(N: float) -> float:
# Rosa's round-wire solenoid mutual inductance correction. D W Knight, April 2010
# Optimised version of Grover's 1929 formula. Max error is +/-0.000000013

# N  = number of turns
    if N < 1:
        return(0)
    else:
        return(log(2 * pi) - 1.5 - log(N) / (6 * N) - 0.33084236 / N - 1 / (120 * N ** 3) + 1 / (504 * N ** 5) - 0.0011925 / N ** 7 + 0.000507 / N ** 9)

def Rosaks90(pdw: float, pD: float, fi: float) -> float:
# Rosa's self inductance correction, continuous empirical version.
# Based on Bob Weaver's modified version of Wheeler 82-7
#  D W Knight, July 2012.  www.g3ynh.info

# pdw = pitch / wire diam , pD = pitch / coil diam, 
# fi = internal inductance factor, zero for none, 1 for LF.
    Ddw: float = (1 / pD) / ( 1 / pdw)
    k0:  float = 1 / (log (8 / pi) - 0.5)
    k2:  float = 24 / (3 * pi * pi - 16)
    w:   float = -0.47 / (0.755 + 1 / pD) ** 1.44
    pn:  float = k0 + 3.437 * pD + k2 * pD * pD + w
    
    return(log(1 + pi / (2 * pD)) + 1 / pn - log(8 * Ddw) + 2 - fi * sqrt(1 + (pD / pi) * (pD / pi)) / 4)

def Flpml(q: float) -> float:
# Calculates internal inductance factor within 160ppM using PACAML formula.
# see: Practical continuous funcs and formulae for int. Z of cylindrical conductors.
#  D. W. Knight, Mar. 2010.  www.g3ynh.info 
    if q < 0.0001:
        return(1.0)
    else:
        i:  float = (4 / q) * ( 1 / sqrt(2) ) * (1 + 0.01209 / (q + 1) - 0.63523 / (q * q + 1) + 0.16476 / (q * q * q + 1))
        i         = i * ( 1 - exp(-1 * (1 / i) ** 1.5819) ) ** (1 / 1.5819)
        z:  float = 0.38691 * q
        zz: float = z ** 1.2652 - z ** -0.39709
        y:  float = -0.198584 / (1 + 0.25741 * zz * zz) ** 2.62343
        
        return(i * (1 - y))

def Lintern(lw: float, d: float, f: float, Kiacs: float, mur: float) -> float:
# Internal inductance of a round wire. Version 1.00, 9th Jan 2016.
# Calls function Flpml(q) for inductance factor Theta.
#  lw = length of wire / m
#  d = wire diameter / m
#  f = frequency / Hz
#  Kiacs is proportionate conductivity relative to IACS. For electrical Cu at 20 deg. C, Kiacs = 1
#  mur = relative permeability of the wire = 1 for non magnetic conductors
    rho:   float = 17.241e-9 / Kiacs
    delta: float = sqrt( rho / ( 4e-7 * pi * pi * f * mur ) )
    q:     float = d / ( delta * sqrt(2) )
    Theta: float = Flpml(q)
    
    return(lw * 5e-8 * mur * Theta)


def main() -> int:
    h:      float = N * dw                             # coil length
    Lext:   float = LxRosa(h, D, N, dw, jw) * 1e6      # extern. induct.
    
    # Dskin:  float = sqrt(10.0 * RCu / (4.0 * pi ** 2 * 820.0))  # skin depth
    # Lfact:  float = Flpml(0.9144 / (sqrt(2) * Dskin))     # intern. L factor
    # LlUnit: float = 0.05 * Lfact        # internal L per unit length
    # lWire:  float = sqrt( (40.0 * pi * 50.9856) ** 2 + 70.9596 ** 2 ) / 1000.0  # wire length
    # Lint:   float = LlUnit * lWire      # internal L
    Lint:  float = Lintern(lWire, dw, f, 1, 1) * 1e6

    print('Lint', Lint)
    print('Lext', Lext)
    L:   float = Lext + Lint
    Xl:  float = tau * f * L     # reactance (L in henry)
    print("D =", D, "  Length/Diameter: ", h / D)
    print('L  = ', L, '\u00b5H')
    print('Xl = ', Xl, sep='')
    print('Medhurst\'s coil #31 total calculated L =', Lint + 1e6 * LxRosa(0.0709596, 0.0503941490665763, 40.0, 0.0009144, 0.00177399))
    print('Approximate SRF =', 299.792458 / (2 * lWire), 'MHz')
    print()
    return 0

if __name__ == "__main__":
    sys.exit(main())
