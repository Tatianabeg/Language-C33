# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open('incoming_text_021.txt','w', encoding='UTF-8' ) as file:
    file.write(input('initial textт: '))
with open('incoming_text_021.txt','r') as file:
    my_text = file.readline()
    change_text = my_text.split()
print()
print(my_text)
print()

del_text = input('entering a combination of letters to delete :  ')
print(del_text)

result = ' '.join(filter(lambda x: del_text not in x, change_text))
with open('format_text_021.txt','w', encoding='UTF-8') as file:
    file.write(f'{result}')
print(result)

# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# б) Подумайте, как наделить бота "интеллектом"

# вариант человек против бота c "интеллектом":
from random import randint

def input_dat(name):
    x = int(input(f"{name}, entering the number of candies from 1 to 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, entering the requuired number of candies: "))
    return x


def p_print(name, k, counter, value):
    print(f"motion {name}, took {k}, become {counter}. left {value} candy.")


def bot_calc(value):
    k = randint(1,29)
    while value-k <= 28 and value > 29:
        k = randint(1,29)
    return k

player1 = input("enter the name of the first player: ")
player2 = "Bot"
value = int(input("enter the number of candies: "))
flag = randint(0,2) 
if flag:
    print(f"the first move {player1}")
else:
    print(f"the first move {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = bot_calc(value)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"won {player1}")
else:
    print(f"won {player2}")
 
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('text_for_RLE_024.txt', 'w', encoding='UTF-8') as file:
    file.write(input('text to compress: '))
with open('text_for_RLE_024.txt', 'r') as file:
    my_text = file.readline()
    text_compression = my_text.split()


print(my_text)


def rle_encode (text):
    enconding  = ""
    prev_char = ""
    count  = 1
    if not text:
        return ''

    for char in text:
        if char != prev_char:
            if prev_char:
                enconding += str(count) + prev_charprev_char
            count = 1
            prev_char = charchar
        else:
            count += 1
    else:
        enconding += str(count) + prev_charprev_char
        return encondingenconding


text_compression = rle_encode(my_text)

with open('text_compression_RLE_024.txt', 'w', encoding='UTF-8') as filefile:
    filefile.writewrite(f'{text_compressiontext_compression}')
print(text_compression)