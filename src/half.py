#!/bin/python
# Half-life examiner thing
# Project Crew™ 6/7/2026

from math import log, e
import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np

print('\n    Half-life:\n')

while True:
    value = input('  elimination half-life (hours): ')
    try:
        halflife: float = float(value)
    except ValueError:
        print('  Valid number, please')
        continue
    if 0 < halflife:
        break
    else:
        print('  Must be > 0')

while True:
    value = input('  initial concentration @ t0...: ')
    try:
        C0: float = float(value)
    except ValueError:
        print('  Valid number, please')
        continue
    if 0 < C0:
        break
    else:
        print('  Must be > 0')

while True:
    value = input('  number of days...............: ')
    try:
        xmajors: float = float(value)
    except ValueError:
        print('  Valid number, please')
        continue
    if 0 < xmajors:
        break
    else:
        print('  Must be > 0')

while True:
    value = input('  day of examining.............: ')
    try:
        poi: float = float(value)
    except ValueError:
        print('  Valid number, please')
        continue
    if 0 < poi:
        break
    else:
        print('  Must be > 0')

k = log(2) / (halflife / 24)            # elimination constant (in days)

def foelim(t, C0, k):                   # First-order elimination
    return C0 * e ** (-k * t)        #   rate equation

foelim = np.frompyfunc(foelim, 3, 1)

fig, ax = plt.subplots(figsize=(5, 2.7))     # begin the plot our graph
ax.xaxis.set_major_locator(ticker.MultipleLocator(1.0))

# xmajors     = 15.0            # num major points on x-axis (days time)
granularity = 0.01            # numDataPoints = xmajors / granularity
# poi         = 3.0             # point of interest on x-axis

if poi > xmajors:             # 0 <= poi <= xmajors
    poi = xmajors

t = np.arange(0.0, xmajors, granularity)     # arrange the time axis
s = foelim(t, C0, k)
line = ax.plot(t, s, lw=2)
ax.grid(True)
annoy = poi / granularity     # y-axis location of point
ax.annotate("{:.2f} @ {}d".format(s[int(annoy)], poi), xy=(poi, s[int(annoy)]),
  xytext=(10, 10), size=16, arrowprops=dict(arrowstyle="-|>",
  connectionstyle="arc3, rad=-0.2"))

#ax.set_ylim(-2, 2)
plt.show()                              # show a little
