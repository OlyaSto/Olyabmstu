delim = []
delit = [1,0,1,1]


def xor(a,b):
    if a == b:
        return 0
    if a != b:
        return 1

def gxor(delim):
    ost= [0,0,0,0]
    i = 3
    while i >= 0:
         ost[i] = xor(delim[i],delit[i])
         i = i - 1
    return(ost)

def dely(delim):
    delim1 = [0,0,0,0]
    otvet = []

    i = 0
    while i < 4:
        delim1[i] = delim[i]
        i = i + 1
    
    k = 0
    i = 3
    c = 0
    while i < 7 and k < 3:
         if delim1[0] == 0:
             i = i + 1
             delim1[0] = delim1[1] 
             delim1[1] = delim1[2] 
             delim1[2] = delim1[3] 

             delim1[3] = delim[i]
             k = k + 1
             c = c + 1
             if c == 2:
                  otvet.append(0)
                  c = 0

             


         if delim1[0] != 0:
             delim1 = gxor(delim1) 
             otvet.append(1)



    if k == 2:
        delim1[0] = delim1[1] 
        delim1[1] = delim1[2] 
        delim1[2] = delim1[3] 

        delim1[3] = delim[6]

    return(delim1)