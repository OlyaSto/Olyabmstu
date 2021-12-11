from pack.decode import *
from colorama import init
init()
from colorama import Fore, Back, Style
vec = [0,0,0,0,0,0,0]

print(Back.YELLOW + Fore.BLACK + 'КОДИРОВАНИЕ ВЕКТОРА'+ Style.RESET_ALL)
print("Вектор вида x1x2x3x4")

print("Введите x1:")
vec[0] = int(input())

print("Введите x2:")
vec[1] = int(input())

print("Введите x3:")
vec[2] = int(input())

print("Введите x4:")
vec[3] = int(input())

def code(vec):
     vec1 = dely(vec)

     vec[4] = vec1[1]
     vec[5] = vec1[2]
     vec[6] = vec1[3]

     return vec
