import math as m
import numpy as np
from random import random
import matplotlib.pyplot as plt

N = 1000000
xPts = []
yPts = []

def crossingOnlyOneLine(lineLen, x, y, rad):
  xHit = m.floor(x + lineLen*m.cos(rad))
  yHit = m.floor(y + lineLen*m.sin(rad))
  return xHit + yHit == 1

for lineLen in np.linspace(0, m.sqrt(2), 3000):
  xPts.append(lineLen)
  tempVar = 0
  for x in range(N):
    if crossingOnlyOneLine(lineLen, random(), random(), random()*m.pi/2):
      tempVar += 1
  yPts.append((float(tempVar))/N)

plt.plot(xPts, yPts)
plt.show()
