from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from colorama import init
init()
from colorama import Fore, Back, Style

def main():
    r = Rectangle("синего", 18, 18)
    c = Circle("зеленого", 18)
    s = Square("красного", 18)
    print(r)
    print(c)
    print(s)


print(Fore.GREEN + 'зеленый текст')
print(Back.YELLOW + 'на желтом фоне' + Style.RESET_ALL)

if __name__ == "__main__":
    main()
