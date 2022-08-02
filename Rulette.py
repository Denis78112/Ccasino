from http.client import MOVED_PERMANENTLY


def getRoulette(visible):
    tickTime = random.randint(100, 200 ) / 10000
    mainTime = 0
    number = randon.randint(0, 38)
    increaseTickTime = random.randint(100, 110) / 100
    col = 1

    while (mainTime < 0.7):
        col += 1
        if (col > 15):
            col = 1
        mainTime += tickTime
        tickTime *= increaseTickTime

        color(col)
        number += 1
        if (number > 38):
            number = 0
            print()

        printNumber = number
        if (number == 37):
            printNumber = "00"
        elif (number == 38):
            printNumber = "000"

        print(" Число >", printNumber, "*" * number, " " * (79 - number * 2), "*" * number)

        if (visible):
            time.sleep(mainTime)
    return number

def roulette():
    global money
    playGame = True

    while (playGame and money > 0):
        colorLine(3, "Добро пожаловать на игру в Рутетку!")
        color(14)
        print(f"\n У тебя на счету {money} {valuta}\n")
        color(11)
        print(" Ставлю на...")
        print("   1. Чётное (выигрыш 1:1)")
        print("   2. Нечетное (выигрыш 1:1")
        print("   3. Дюжина (выигрыш 3:1")
        print("   4. Число (выигрыш 36:1")
        print("   0. Возврат в предыдущее меню")

        x = getInput("01234", "    Твой выбор? ")

        playRoulette = True

        if (x == "3"):
            color(2)
            print()
            print(" Выбери числа:...")
            print("   1. От 1 до 12")
            print("   2. От 13 до 24")
            print("   3. От 25 до 36")
            print("   0. Назад")

            duzhina = getInput("0123", "    Твой выбор? ")

            if (duzhina == "1"):
                textDuzhina = "от 1 до 12"
            elif (duzhina == "2"):
                textDuzhina = "от 13 до 24"
            elif (duzhina == "3"):
                textDuzhina = "от 25 до 36"
            elif (duzhina == "0"):
                playRoulette = False
        elif (x == "4"):
            chislo = getIntInput(0, 36, "    На какое число ставишь? (0..36): ")
        
        color(7)
        if (x == "0"):
            return 0

        if (playRoulette):
            stavka = getIntInput(0, money, f"    Сколько поставишь? (не больше {money}): ")
            if (stavka == 0):
                return 0
            
            number = getRoulette(True)

            print()
            color(11)

            if (number < 37):
                print(f"    Выпало число {number}! " + "*" * number)
            else:
                if (number == 37):
                    printNumber = "00"
                elif (number == 38):
                    printNumber = "000"
                print(f"    выпало число {printNumber}! ")
            
            if (x == "1"):
                print("    Ты ставил на ЧЁТНОЕ!")
                if (number <37 and number % 2 == 0):
                    money += stavka
                    pobeda(stavka)
                else:
                    money -= stavka
                    proigr(stavka)
            

