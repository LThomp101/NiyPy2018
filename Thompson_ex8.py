#Thompson Ex 8
import numpy as np
import matplotlib.pyplot as pl
from math import tan, cos, asinh, pi
##coordinates = open("Thompson_coords.txt", "r").readlines()
##coordinates = open("coords.txt", "r").readlines()
coordinatesO = open("world_outline.txt","r").readlines()
n = len(coordinatesO)
loopO = np.empty(dtint)
xO = np.zeros(n)
yO = np.zeros(n)
oldloop = 1
fp = 0
for k in range(n):
    loopO[k] = int(coordinates[k].split()[0])
    xO[k] = float(coordinates[k].split()[2]) ## longitude
    yO[k] = float(coordinates[k].split()[1]) ## latitude
    xOR = xO * (pi/180)
    yOR = yO * (pi/180)
    yOutline = yOR
    xOutline = (1.25 * asinh(tan(xOR * .8))
    if loopO[k] != oldloop:
       pl.plot(xOutline[fp:k],yOutline[fp:k],"b")
       fp = k
       oldloop += 1
       
coordinatesO = open("world_graticule.txt", "r").readlines()
n = len(coordinatesG)
loopG = np.empty(dtint)*
xG = np.zeros(n)
xG = np.zeros(n)
oldloop = 1
fp = 0
for k in range(n):
    loopG[k] = int(coordinates[k].split()[0])
    xG[k] = float(coordinates[k].split()[2])
    yG[k] = float(coordinates[k].split()[1])
    xGR = xG * (pi/180)
    yGR = yG * (pi/180)
    yGraticule = yGR
    xGraticule = (1.25 * (asinh))*(tan (yGR * .8))
    if loopG[k] != poldloop:
        pl.plot(xGraticule[fp:k],yGraticule[fp:k],"b")
        fp = k
        oldloop += 1

pl.plot(x[fp:k],y[fp:k],"b")
pl.savefig("Thompson_ex8.pdf")    
pl.show()
         
