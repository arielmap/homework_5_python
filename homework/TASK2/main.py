import random

print(
    '"Игра с конфетами: на столе лежит 2021 конфета,\n'
    'играют два игрока делая ход друг после друга.\n'
    'Первый ход определяется жеребьёвкой.\n'
    'За один ход можно забрать не более чем 28 конфет.\n'
    'Все конфеты оппонента достаются сделавшему последний ход.\n'
)

player1 = input('Первый игрок, введите Ваше имя:\n')
player2 = input('Второй игрок, введите Ваше имя: \n')
players = [player1, player2]

total_sweets = 2021
max_number_move = 28


def game_friend_vs_friend_or_smartbot(total_sweets, max_number_move, players):
    count = 0
    first = random.randint(0, 1)
    print (f'\nПервый ход определён жеребьёвкой, начинает игрок № {first + 1}')
    while total_sweets > 0:
        if players[0] == 'бот' and first % 2 == 0:
            if total_sweets > 28:
                move = total_sweets % (max_number_move + 1)
            else:
                move = total_sweets
        elif players[1] == 'бот' and first % 2 == 1:
            if total_sweets > 28:
                move = total_sweets % (max_number_move + 1)
            else:
                move = total_sweets
        else:
            move = int(input(f'{players[first % 2]}: '))
        if move > total_sweets or move > max_number_move:
            print(f'Можно взять не более 28 конфет, у нас всего {total_sweets} конфет(ы)!')
            chance = 2
            while chance > 0:
                if total_sweets >= move <= max_number_move:
                    break
                print(f'Попробуйте ещё раз, у Вас {chance} попытки')
                if players[0] == 'бот' and first % 2 == 0:
                    if total_sweets > 28:
                        move = total_sweets % (max_number_move + 1)
                    else:
                        move = total_sweets
                elif players[1] == 'бот' and first % 2 == 1:
                    if total_sweets > 28:
                        move = total_sweets % (max_number_move + 1)
                    else:
                        move = total_sweets
                else:
                    move = int(input())
                chance -= 1
            else:
                return print(f'Попытки закончились! Вы проиграли!')
        total_sweets = total_sweets - move
        if total_sweets > 0:
            print(f'Осталось {total_sweets} конфет(ы)!')
        else:
            print('Все конфеты разобраны.')
        first += 1
    return players[(first - 1) % 2]

def game_friend_vs_friend_or_fullbot(total_sweets, max_number_move, players):
    count = 0
    first = random.randint(0, 1)
    print (f'\nПервый ход определён жеребьёвкой, начинает игрок № {first + 1}')
    while total_sweets > 0:
        if players[0] == 'бот' and first % 2 == 0:
            move = random.randint(0, 28)
        elif players[1] == 'бот' and first % 2 == 1:
            move = random.randint(0, 28)
        else:
            move = int(input(f'{players[first % 2]}: '))
        if move > total_sweets or move > max_number_move:
            print(f'Можно взять не более 28 конфет, у нас всего {total_sweets} конфет(ы)!')
            chance = 2
            while chance > 0:
                if total_sweets >= move <= max_number_move:
                    break
                print(f'Попробуйте ещё раз, у Вас {chance} попытки')
                if players[0] == 'бот' and first % 2 == 0:
                    move = random.randint(0, 28)
                elif players[1] == 'бот' and first % 2 == 1:
                    move = random.randint(0, 28)
                else:
                    move = int(input())
                chance -= 1
            else:
                return print(f'Попытки закончились! Вы проиграли!')
        total_sweets = total_sweets - move
        if total_sweets > 0:
            print(f'Осталось {total_sweets} конфет(ы)!')
        else:
            print('Все конфеты разобраны.')
        first += 1
    return players[(first - 1) % 2]

winer = game_friend_vs_friend_or_smartbot(total_sweets, max_number_move, players)
if not winer:
    print('Победителя нет.')
else:
    print(f'Поздравляю! Победил {winer}!')