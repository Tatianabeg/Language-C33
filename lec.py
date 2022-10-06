# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции. Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list = [2, 3, 5, 9, 3]
print(list)

sum = 0
for i in range(len(list)):
    if i %  2 != 0:
        sum = sum + list[i]
print(f'Sum of elements in odd position {list} is', sum)

# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [2,3,4,5,6]
print(list,'==>')

def mult(list):
    mult = []
    for i in range((len(list)+1)//2):
        mult.append(list[i]*list[len(list)-1-i])
    return mult
print(mult(list))


# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
print(list)

def dif(list):
    dif_max_min =[]
    for i in range(len(list)):
        dif_max_min.append(list[i]%1)
    return max(dif_max_min) - min(dif_max_min)
print(round(dif(list),2))


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

a = int(input('Enter the number: '))
b = ''
while a > 0:
    b = str(a % 2)+b
    a = a//2
print(b)
