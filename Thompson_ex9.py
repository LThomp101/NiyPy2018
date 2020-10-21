import numpy as np
import matplotlib.pyplot as pl
beach = open("addison_data.txt","r").readlines()
nx = len(beach) - 2
nt = len(beach[0].split())
#print nx, nt

years = np.empty(nt)
date = np.empty(nt)
x = np.empty(nx)

cliff=np.empty([nt,nx])

for k in range(nx):
    x[k] = float(beach[k+2].split()[0])
    for l in range(nt):
        #print l, k
        cliff[l,k] = float(beach[k+2].split()[l+1])
for l in range (nt):
    years[l] = int(beach[0].split()[l])
    date[l] = int(beach[1].split()[l])
    pl.plot( x, cliff[l,:] )

for l in range(nt-1):
    DaysBtwn = 365 + date[l +1] - date[l]
    if years[l]%4 == 0:
        DaysBtwn += 1
    ChangeRate = (365 * np.sum(cliff[l+1,:] - cliff[l,:]) / nx) / DaysBtwn
    print ChangeRate
    
pl.legend(years, loc='lower left')
pl.xlabel('Baseline Position')
pl.ylabel('Distance To Cliff')
pl.savefig('ThompsonEx9.pdf')
pl.show()

