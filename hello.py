""" Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным. 
Пример: - 6 -> да - 7 -> да - 1 -> нет  """

day = int(input('Enter day number: '))
# if day > 7 or day < 1:
# print('Repeat the input')
# elif day == 6 or day == 7:
# print("Это выходной!")
# else:
# print("Это не выходной!")

# 2. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

x = int(input('input x: '))
# y = int(input('input y: '))
# if x > 0 and y > 0:
#     print('1')
# if x < 0 and y > 0:
#     print('2')
# if x < 0 and y < 0:
#     print('3')
# if x > 0 and y < 0:
#     print('4')

#3. Напишите программу, которая по заданному номеру четверти, 
#показывает диапазон возможных координат точек в этой четверти (x и y).

# n = int(input('input quarter: '))
# if n < 1 or n > 4:
# print('Repeat the input')
# elif n == 1:
# print('x > 0 and y > 0')
# elif n == 2:
# print('x < 0 and y > 0')
# elif n == 3:
# print('x < 0 and y < 0')
# elif n == 4:
# print('x > 0 and y < 0')

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def input_numbers(x): 
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        reality = False
        while not reality:
            try:
                number = int(input(f"Ввод координаты {xy[i]}: "))
                a.append(number)
                reality = True
            except ValueError:
                print(" Цифра,без запятых")
    return a


def Length(a, b):  
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)  
    return lengthSegment


print("Введите координаты точки А")
pointA = input_numbers(2)
print("Введите координаты точки В")
pointB = input_numbers(2)

print(f"Длина отрезка: {round(Length(pointA, pointB),2)}")

  

    
     