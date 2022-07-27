# Казино 678
from ctypes import *
valuta = "руб."
money = 0
defaultMoney = 10000
windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))

#Вывод сообщения о выигрышеэ
def pobeda(result):
    color(14)
    print(f"    Победа за тобой! Выигрыш составил: {result} {valuta}")
    print(f"    У тебя на счету: {money}")

#Вывод сообщения о проигреше
def proigr(result):
    color(12)
    print(f"    К сожалению проигрыш: {result} {valuta}")
    print(f"    У тебя на счету: {money}")
    print(f"    Обязательно нужно отыграться!")

#Чтение из файла оставшейся суммы
def loadMoney():
    try:
        f = open("money.dat", "r")
        m = int(f.readline())
        f.close
    except FileNotFoundError:
        print(f'Файла не сущетвует, задано значение {defaultMoney} {valuta}')
        m = defaultMoney
    return m

#Запись суммы в файл
def saveMoney(moneyToSave):
    try:
        f = open('money.dat', 'w')
        f.write(str(moneyToSave))
        f.close()
    except:
        print(f"Ошибка сщздания файла, наше казино закрывается!")
        quit(0)

#Установка цвета текста
def color(c):
    windll.Kernel32.SetConsoleTextAttribute(h, c)

#Вывод на экран цветного, обрамленного звездочками текста
def colorLine(c, s):
    for i in range(30):
        print()
    color(c)
    print("*" * (len(s) + 2))
    print(' ' + s)
    print("*" * (len(s) + 2))

#Функция ввода целого числа
def getIntInput(minimum, maximum, message):
    color(7)
    ret = -1
    while (ret < minimum or ret > maximum):
        st = input(message)
        if (st.isdigit()):
            ret = int(st)
        else:
            print('    Введи целое число!')
    return ret

#Функция ввода значения
def getInput(digit, message):
    color(7)
    ret = ""
    while (ret == "" or not ret in digit):
        ret = input(message)
    return ret

