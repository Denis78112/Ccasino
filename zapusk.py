#Запуск игры
from turtle import color


def main():
    global money, playGame
    money = loadMoney()
    startMoney = money

    while (playGame and money > 0):
        colorLine(10, "Приветствую тебя в нашем казино!")
        color(14)
        print(f' У тебя на счету {money} {valuta}')

        color(6)
        print(' Ты можешь сыграть в:')
        print("    1. Рулетку")
        print("    2. Кости")
        print("    3. Однорукого бандита")
        print("    0. Выход. Ставка 0 в играх - выход.")
        color(7)

        x = getInput("0123", "    Твой выбор? ")

        if (x == "0"):
            playGame = False
        elif (x == '1'):
            roulette()
        elif (x == '2'):
            dice()
        elif (x == '3'):
            oneHandBandit()

    colorLine(12, "Жаль, что ты покидаешь нас! Возвращайся скорее!")
    color(13)
    if (money <= 0):
        print(" Ой, ты остался без денег. Возьми кредит.")

    color(11)
    if (money > startMoney):
        print("Ну что же, поздравляем с прибылью!")
        print(f"На начало игры у тебя было {startMoney} {valuta}")
        print(f"Сейчас уже {money} {valuta}! Играй еще и приумножай!")
    else:
        print(f"К сожалению, ты проиграл {startMoney - money} {valuta}")
        print("В следующий раз все обязательно получиться!")
    saveMoney(money)

    color(7)
    quit(0)
main()