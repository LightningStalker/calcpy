#!/bin/python
# Mixture ratio calc
# Project Crew™ 9/22/2026

# from nowhere import nothing

def verr()  : print('ERROR: I need a real number.', end='\n\n')
def nerr(n) :
    if n == 0: op: string = '>'
    else:      op: string = 'at least '
    print('ERROR: Has to be ', op, n, '.', sep='', end='\n\n')

print('1 USGal = 128 ounce = 8 pints = 4 quart = 3.7854118 litere = 3785.4118 '
    'mL.', end='\n\n')

while True:
    try:
        den = float(input('Parts gas/petro/diluent..: '))
        if den >= 1:
            break
        else:
            nerr(1)
    except ValueError:
        verr()

while True:
    try:
        num = float(input('Parts of oil/concentrate.: '))
        if num >= 1:
            break
        else:
            nerr(1)
    except ValueError:
        verr()

while True:
    try:
        vol = float(input('Start/target volume......: '))
        if vol > 0:
            break
        else:
            nerr(0)
    except ValueError:
        verr()

unit    = vol / (num + den)
conVol  = unit * num
dilVol  = unit * den

unit    = vol / num
sDilVol = unit * den
sTvol   = vol + sDilVol

unit    = vol / den
dDilVol = unit * num
dTvol   = vol + (unit * num)

print( '\n{:12.2f} units oil  + {:12.2f} gas  = {:12.2f} mixed volume'
    .format(conVol, dilVol, vol) )
print( '{:12.2f} units oil  + {:12.2f} gas  = {:12.2f} mixed volume'
    .format(vol, sDilVol, sTvol) )
print( '{:12.2f} units gas  + {:12.2f} oil  = {:12.2f} mixed volume'
    .format(vol, dDilVol, dTvol) )
