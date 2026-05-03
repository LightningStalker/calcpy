#!/bin/python
# Sqare of distance energy falloff of isotropic pattern radiator

from getkey import getkey

print()

while True:
    try:
        distance = float(input(' distance in meters? '))
        break
    except ValueError:
        print('ERROR: I need a real number.')

while True:
    try:
        intensity = float(input(' intensity  in  lux? '))
        break
    except ValueError:
        print('ERROR: I need a real number.')

print('\n lumens at source:', end=' ')
print(distance ** 2.0 * intensity, end='', flush=True)
getkey()
print()
