from pack import comp
from pack.comp import comp
from pack.orch import orch
from pack.comp_orch import comp_orch
from pack.data import *
from colorama import init
init()
from colorama import Fore, Back, Style

def main():

    one_to_many = [(c.mus, c.long, o.name) 
        for o in orchs 
        for c in comps 
        if c.orch_id==o.id]

    many_to_many_temp = [(o.name, co.comp_id, co.orch_id) 
        for o in orchs 
        for co in comps_orchs 
        if o.id==co.orch_id]
    
    many_to_many = [(c.mus, c.long, orch_name) 
        for orch_name, comp_id, orch_id in many_to_many_temp
        for c in comps if c.id==comp_id]

    print(Back.CYAN + 'Задание А1 - список всех оркестров, в названиии кототорых есть слово "оркестр"'+ Style.RESET_ALL)

    res11 = []

    for i in one_to_many:
        if i[2].find("оркестр") != -1:
            int = [i[2], i[0]]
            res11.append(int)
    
    k = ""

    for i in res11:
       if k == "":
            k = i[0]
            print(i[0])
            for i in res11:
                if k == i[0]:
                   print('     ', i[1])
       elif k != i[0]:
           k = i[0]
           print(i[0])
           for i in res11:
                if k == i[0]:
                   print('     ', i[1])

    print(Fore.BLACK + Back.YELLOW + 'Задание А2 - средняя продолжительность произведений для каждого оркестра'+ Style.RESET_ALL)
    
    k = ""
    s = 0
    dl = 0

    for i in one_to_many:
        if k =="":
            k = i[2]
            for i in one_to_many:
                if k == i[2]:
                    s += 1
                    dl += i[1]
            print (k, "----", round(dl/s, 2))
        elif k != i[2]:
            k = i[2]
            for i in one_to_many:
                if k == i[2]:
                    s += 1
                    dl += i[1]
            print (k, "----", round(dl/s, 2))
        
    print(Back.MAGENTA +'Задание А3 - список всех произведений, начинающихся на "Т"'+ Style.RESET_ALL)

    res13 = []
    kkk = []

    for i in many_to_many:
        if i[0][0] == 'Т':
            res13.append(i)
    
    k = ""

    for i in res13:
       if k == "":
            k = i[0]
            kkk.append(i[0])
            print(i[0])
            for i in res13:
                if k == i[0]:
                   print('     ', i[2])
       elif k != i[0] and i[0] not in kkk:
           k = i[0]
           kkk.append(i[0])
           print(i[0])
           for i in res13:
                if k == i[0]:
                   print('     ', i[2])





if __name__ == '__main__':
    main()
