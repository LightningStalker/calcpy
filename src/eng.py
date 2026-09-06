#!/bin/python
# display the numbers in Engineering form
# Project crew™ 9/4/2026

print('\n    Convert to Engineering form')
while True:
    value = input('\n  Number? ')
    try:
        number: float = float(value)
        break
    except ValueError:
        print('  Valid number, please')
    except:
        print('  Input error')
print('\n   {:e}'.format(number))
