# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

my_list = [ 1, 2, 3, 2, 1, 5, 5, 8, 11, 13]
new_list = []
my_set = set(my_list)

for item in my_set:
    if my_list.count(item) > 1:
        new_list.append(item)

print(new_list)

# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.

import string

text = "Интерпретатор Python — встроенная программа, которая выполняет исходный код. "\
         "Интерпретатор выступает в роли дешифровщика. Написанный код переводится в байт-код и выполняется."\
         "Создавать код можно даже в блокноте, главное — поставить расширение .py."\
         " Как выбрать версию. Python — это интерфейс. " \
         "У него есть несколько реализаций: Jython, PyPy, IronPython."\
         "Но самая распространенная — CPython. Она считается версией «по умолчанию»."
        
MOST_FREQ = 10
punct = f'—{string.punctuation}'
print(punct)
for item in punct:
    text = text.replace(item, ' ')
words_list = text.lower().split()

qty_dict = {}
for item in words_list:
    key = qty_dict.setdefault(words_list.count(item), set([]))
    key.add(item)
print(qty_dict)

qty_set = sorted(qty_dict.keys(), reverse=True)

the_most_freq = []
for i in range(MOST_FREQ):
    the_most_freq.append(qty_dict.get(qty_set[i]))
print(the_most_freq) 

# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. 

MAX_WEIGTH = 5_000
things = ['Ложка', 'Чашка', 'Тарелка', 'Палатка', 'Футболка',
          'Спортивки', 'Боксеры', 'Зубная щетка', 'Одеяло']
weights = [50, 250, 380, 3_550, 300, 280, 180, 70, 1_670]

my_dict = {}
for num, thing in enumerate(things):
    my_dict[thing] = weights[num]

weight = 0
things_in = []
for key, value in my_dict.items():
    weight += value
    if weight <= MAX_WEIGTH:
        things_in.append(key)
    else:
        weight -= value
print(things_in)