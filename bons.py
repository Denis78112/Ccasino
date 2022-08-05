#Кости
from email import message_from_binary_file
from http.client import MOVED_PERMANENTLY


def dice():
    global money
    playGame = True

    while (playGame):

        print()
        colorLine(3, "Добро пожаловать на игру в Кости!")
        color(14)
        print(f"\n У тебя на счету {money} {valuta}\n")

        color(7)
        stavka = getIntInput(0, money, f"    Сделай ставку в пределах {money} {valuta}: ")
        if (stavka == 0):
            return 0
        
        playRound = True
        control = stavka
        oldResult = getDice()
        firstPlay = True

        while (playRound and stavka > 0 and money >0):

            if (stavka > money):
                stavka = money

        color(11)
        print(f"\n    В твоем распоряжении {stavka} {valuta}")
        color(12)
        print(f"\n    Текущая сумма чисел на костях: {oldResult}")
        color(11)
        print("\n    Сумма чисел на гранях будет больше, меньше или равна предедущей?")
        color(7)
        x = getInput("0123", "    Введи 1 - больше, 2 - меньше, 3 - равно, 0 - выход: ")

        if (x != "0"):
            firstPlay = False
            if (stavka > money):
                stavka = money

            money -= stavka
            diceResult = getDice()

            win = False
            if (oldResult > diceResult):
                if (x == "2"):
                    win = True
            elif (oldResult < diceResult):
                if (x == "1"):
                    win = True
            
            if (not x == "3"):
                if (win):
                    money += stavka + stavka // 5
                    pobeda(stavka // 5)
                    stavka += stavka // 5
                else:
                    stavka = control
                    proigr(stavka)
            elif (x == "3"):
                if (oldResult == diceResult):
                    money += stavka * 3
                    pobeda(stavka * 2)
                    stavka *= 3
                else:
                    stavka = control
                    proigr(stavka)
            
            oldResult = diceResult
        else:
            if (firstPlay):
                money -= stavka
            playRound = False


#Анимация Костей
def getDice():
    count = random.randint(3, 8)
    sleep = 0
    while (count > 0):
        color(count + 7)
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        print(" " * 10, "----- -----")
        print(" " * 10, f"| {x} | | {y} |")
        print(" " * 10, "----- -----")
        time.sleep(sleep)
        sleep += 1 / count
        count -= 1
    return x + y

