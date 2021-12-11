from pack import *
from pack.miscode import *
from pack.decode import *
from pack.codir import *
from colorama import init
init()
from colorama import Fore, Back, Style

mist = []
vect = []

print("Закодированный вектор:")

#НАЛОЖЕНИЕ МАСКИ ОШИБКИ 

def mask(mist, vect):
    vect1 = vect.copy()
    t = 0
    while t < 7:
        if mist[t] == 1:
            vect1[t] = xor(vect[t], 1) 
        
        t += 1
        
    return vect1    

def prov(vect):
    v = dely(vect)

    t = 0
    while t < 4:
        if v[t] == 1:
            t = 20 
        t += 1

    if t == 21:
        return 1
    else:
        return 0

codvec = code(vec)
print(codvec)
#codvec1 = ['','','','','','','']
#i = 0
#while i < 7:
#    codvec1[i] = codvec[i] 
#    i += 1

codvec1 = codvec.copy()

print("i   Кол-во ошибок   Кол-во найденных ошибок   Обнаруж. способность")

l = 0
kol = 0
while l < 7:
     codvec2 = codvec1
     a = mask(l1[l],codvec2)
     prov(a)
     if prov(a) == 1:
         kol += 1
     l += 1

print("1","       ",len(l1),'                  ',kol,'                    ',kol/len(l1))


l = 0
kol = 0
while l < 21:
     codvec2 = codvec1
     a = mask(l2[l],codvec2)
     prov(a)
     if prov(a) == 1:
         kol += 1
     l += 1

print("2","       ",len(l2),'                 ',kol,'                   ',kol/len(l2))

l = 0
kol = 0
while l < 35:
     codvec2 = codvec1
     a = mask(l3[l],codvec2)
     prov(a)
     if prov(a) == 1:
         kol += 1
     l += 1

print("3","       ",len(l3),'                 ',kol,'                   ',kol/len(l3))

l = 0
kol = 0
while l < 35:
     codvec2 = codvec1
     a = mask(l4[l],codvec2)
     prov(a)
     if prov(a) == 1:
         kol += 1
     l += 1

print("4","       ",len(l4),'                 ',kol,'                   ',kol/len(l4))

l = 0
kol = 0
while l < 21:
     codvec2 = codvec1
     a = mask(l5[l],codvec2)
     prov(a)
     if prov(a) == 1:
         kol += 1
     l += 1

print("5","       ",len(l5),'                 ',kol,'                   ',kol/len(l5))

l = 0
kol = 0
while l < 7:
     codvec2 = codvec1
     a = mask(l6[l],codvec2)
     prov(a)
     if prov(a) == 1:
         kol += 1
     l += 1

print("6","       ",len(l6),'                  ',kol,'                    ',kol/len(l6))

l = 0
kol = 0
while l < 1:
     codvec2 = codvec1
     a = mask(l7[l],codvec2)
     prov(a)
     if prov(a) == 1:
         kol += 1
     l += 1

print("7","       ",len(l7),'                  ',kol,'                    ',kol/len(l7))
