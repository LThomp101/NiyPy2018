# Laniya Thompson

discharges = open("white_clay_discharge_2017.txt", "r").readlines()
n = len(discharges)

qtot = 0.0 #totaling or holder for yearly discharge 
qfish = 100.0 #holder for minumum we can take for the fish needs to be above
qpump = 5.0 #Max amount you can take per day/ 5 cft/sec
qdays = 0
for k in range (n): 
    q = float(discharges[k].split()[3]) 
    q = max (0.0, q - qfish) #Grabs higher number/ Lower
    q = min (q, qpump) #If over 5 you can only take 5
    qdays = qdays + 1 #Add a day
    qtot = qtot + q #Finding average
    date = discharges[k].split()[2]
    year = int(date.split("-")[0])
    month = int(date.split("-")[1])
    day = int(date.split("-")[2])
    if day == 31 and month == 12:
       print year, qtot/qdays
       qtot = 0
       qdays = 0
    
