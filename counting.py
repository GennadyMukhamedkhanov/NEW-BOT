import random

def count(meaning):
    YOU = 0
    BOT = 0
    sp = {'камень' : 1, 'ножницы' : 2, 'бумага' : 3}
    if meaning in sp.keys():
        bot_zn = random.randint(1, 3)
        if sp[meaning] == bot_zn:
            return 'Ничья'
        elif sp[meaning] == 1 and bot_zn == 2:
            return 'Ты выиграл'
        elif sp[meaning] == 1 and bot_zn == 3:
            return 'Выиграл БОТ'
        elif sp[meaning] == 2 and bot_zn == 1:
            return 'Выиграл БОТ'
        elif sp[meaning] == 2 and bot_zn == 3:
            return 'Ты выиграл'
        elif sp[meaning] == 3 and bot_zn == 1:
            return 'Ты выиграл'
        elif sp[meaning] == 3 and bot_zn == 2:
            return 'Выиграл БОТ'


