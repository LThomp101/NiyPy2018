#Thompson Ex 7
import numpy as np
import matplotlib.pyplot as pl
coordinates = open("Thompson_coords.txt", "r").readlines()
##coordinates = open("coords.txt", "r").readlines()
n = len(coordinates)
Easting = 435746.50
Northing = 4392521.86
loop = np.empty(n)
x = np.zeros(n)  
y = np.zeros(n)
oldloop = 1
fp = 0
for k  in range(n):
    loop[k] = int(coordinates[k].split()[0])
    x[k] = float(coordinates[k].split()[2]) + Easting ## add UTM easting
    y[k] = float(coordinates[k].split()[3]) + Northing ## add UTM northing
    if loop[k] != oldloop:
       pl.plot(x[fp:k],y[fp:k])
       fp = k
       oldloop += 1
pl.plot(x[fp:k],y[fp:k])
##pl.arrow(100, 25, 40, -60, 25, 35)
pl.arrow(-10 + Easting , -50 + Northing, 0, 20, head_width=3 ) ## will need to change -10, 50 to UTM
pl.annotate ( "N", xy=(-8 + Easting,-50 + Northing) )         ## will need to change to UTM
##pl.axis('scaled', 'equal')
pl.axis('scaled')
pl.title('Thompson Ex 7 Map', y=1.08)
#pl.axis('equal')
   # pl.plot (x,y)
pl.savefig("Thompson_ex7.pdf")    
pl.show()
         
