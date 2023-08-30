# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. 
# Функцию hex используйте для проверки своего результата.

HEX_FACTOR = 16
hex_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']


def get_number_from_user() -> int:
    enter = input('Ввести целое число >0: ')
    return int(enter)


def converter(number: int) -> str:
    res: str = ''
    while number > 0:
        res = str(hex_data[number % HEX_FACTOR]) + res
        number //= HEX_FACTOR
    return res


num = get_number_from_user()
if isinstance(num, int):
    print(converter(num))
else:
    print('Что-то не так. Пробуйте снова.')

print(hex(num)[2:])


# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

from fractions import Fraction


class SelfFraction:
    def __init__(self, numerator: int, denominator: int):
        if not isinstance(numerator, int) and not isinstance(denominator, int):
            raise ValueError
        elif denominator == 0:
            raise ZeroDivisionError
        else:
            nod = SelfFraction.check_nod(numerator, denominator)
            self.num = numerator // nod
            self.den = denominator // nod

    def __add__(self, other):
        main_den = self.den * other.den
        main_num = self.num * other.den + other.num * self.den
        return SelfFraction(main_num, main_den)

    def __mul__(self, other):
        main_num = self.num * other.num
        main_den = self.den * other.den
        return SelfFraction(main_num, main_den)

    @staticmethod
    def check_nod(num: int, den: int) -> int:
        nod = 1
        for i in range(1, max(num, den) // 2 + 1):
            if num % i == 0 and den % i == 0:
                nod = i
        return nod

    def __str__(self):
        return f'{self.num}/{self.den}'


first_fract = input('Ввести 1 дробь формата "a/b": ').split('/')
second_fract = input('Ввести 2 дробь формата "a/b": ').split('/')

self_fract_1 = SelfFraction(int(first_fract[0]), int(first_fract[1]))
self_fract_2 = SelfFraction(int(second_fract[0]), int(second_fract[1]))
original_fract_1 = Fraction(int(first_fract[0]), int(first_fract[1]))
original_fract_2 = Fraction(int(second_fract[0]), int(second_fract[1]))

print(f'Свой класс {self_fract_1 + self_fract_2}')
print(f'Проверка {original_fract_1 + original_fract_2}')

print(f'Свой класс {self_fract_1 * self_fract_2}')
print(f'Проверка {original_fract_1 * original_fract_2}')