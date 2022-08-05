from http.client import MOVED_PERMANENTLY


def getMaxCount(digit, v1, v2, v3, v4, v5):
    ret = 0
    if (digit == v1):
        ret +=1
    if (digit == v2):
        ret += 1
    if (digit == v3):
        ret += 1
    if (digit == v4):
        ret += 1
    if (digit == v5):
        ret += 1
    return ret

def getOHBRes(stavka):
    res = stavka
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0
    getD1 = True
    getD2 = True
    getD3 = True
    getD4 = True
    getD5 = True
    col = 10

    while (getD1 or getD2 or getD3 or getD4 or getD5):
        if (getD1):
            d1 += 1
        if (getD2):
            d2 -= 1
        if (getD3):
            d3 += 1
        if (getD4):
            d4 -= 1
        if (getD5):
            d5 += 1
        
        if (d1 > 9):
            d1 = 0
        if (d2 < 0):
            d2 = 9
        if (d3 > 9):
            d3 = 0
        if (d4 < 0):
            d4 = 9
        if (d5 > 9):
            d5 = 0

        if (random.randint(0, 20) == 1):
            getD1 = False
        if (random.randint(0, 20) == 1):
            getD2 = False
        if (random.randint(0, 20) == 1):
            getD3 = False
        if (random.randint(0, 20) == 1):
            getD4 = False
        if (random.randint(0, 20) == 1):
            getD5 = False
        
        time.sleep(0.1)
        color(col)
        col += 1
        if (col > 15):
            col = 10
        
        print("    " + "%" * )
        print(f"    {d1} {d2} {d3} {d4} {d5}")

    maxCount = getMaxCount(d1, d2, d3, d4, d5)

    if (maxCount < getMaxCount(d2, d1, d3, d4, d5)):
        maxCount = getMaxCount(d2, d1, d2, d3, d4, d5)
    if (maxCount < getMaxCount(d3, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d3, d1, d2, d3, d4, d5)
    if (maxCount < getMaxCount(d4, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d4, d1, d2, d3, d4, d5)
    if (maxCount < getMaxCount(d5, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d5, d1, d2, d3, d4, d5)

    color(14)
    if (maxCount == 2):
        print(f" Совпадениедвух чисел! Твой выигрыш в размере ставкиЖ {res}")
    elif (maxCount == 3):
        res *= 2
        print(f" Совпадение трех чисел! Твой выигрыш 2:1 {res}")
    elif (maxCount == 4):
        res *= 5
        print(f" Совпадение Четырех чисел! Твй выигрыш  5:1: {res}")
    elif (maxCount == 5):
        res *= 10
        print(f" БИНГО! Совпадение Всех чисел! Твой выигрыш 10:1: {res}")
    else:
        proigr(res)
        res = 0

    color(11)
    print()
    input(" Нажмите ENTER для продолжения...")
    return res

#Однорукий Бандит
def oneHandBandit():
    global money
    playGame = True
    while (playGame):
        colorLine(3, "Добро пожаловать на игру в Однорукий Бандит!")
        color(14)
        print(f"\n У тебя на счету {money} {valuta}\n")
        color(5)
        print(" Правила игры: ")
        print("    1. При совпадении 2-х чисел ставка не списывается.")
        print("    2. При совпадении 3-х чисел выигрыш 2:1.")
        print("    3. При совпадении 4-х чисел выигрыш 5:1.")
        print("    4. При совпадении 5-ти чисел выигрыш 10:1.")
        print("    0. Ставка 0 для завершения игры\n")

        stavka = getIntInput(0, money, f"    Введи ставку от 0 до {money}: ")
        if (stavka == 0):
            return 0
        money -= stavka
        money += getOHBRes(stavka)
        if (money <= 0):
            playGame = False
