i = 110

k = ''
dvoich = []
dvoichFin = ['','','','','','','']
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
l7 = []

t = 0
while t < 128:
    
    b = bin(t)

    for k in b:
       dvoich.append(k)
    
    i = i + 1
 

    k = len(dvoich)
    i = k - 1
    j = 0
    while i > 1:
        dvoichFin[j] = dvoich[i]
        i = i - 1
        j = j + 1  

    i = 0
    while i < 7:
        if dvoichFin[i] == '':
            dvoichFin[i] = 0
        i = i + 1
 
    i = 0
    while i < 7:
         dvoichFin[i] = int(dvoichFin[i])
         i = i + 1
    
    t = t + 1
    
    kol = 0
    i = 0
    while i < 7:
        if dvoichFin[i] == 1:
            kol = kol + 1
        i = i + 1
    
    if kol == 1:
        l1.append(dvoichFin)

    if kol == 2:
        l2.append(dvoichFin)

    if kol == 3:
        l3.append(dvoichFin)

    if kol == 4:
        l4.append(dvoichFin)

    if kol == 5:
        l5.append(dvoichFin)
    
    if kol == 6:
        l6.append(dvoichFin)
    
    if kol == 7:
        l7.append(dvoichFin)

    dvoichFin = ['','','','','','','']
    dvoich = []
    kol = 0


      