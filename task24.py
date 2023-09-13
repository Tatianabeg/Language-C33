# Напишите функцию для транспонирования матрицы

def print_matrix(matrix: [[int]]) -> None:
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()
    print()

def transpose_matrix(matrix: [[int]]) -> [[int]]:
    t_matrix = [[0] * len(matrix) for i in range(len(matrix[0]))]
    for i in range(len(t_matrix)):
        for j in range(len(t_matrix[0])):
            t_matrix[i][j] = matrix[j][i]
    return t_matrix

matrix_1 = [[11, 12, 13, 14],
            [15, 16, 17, 18]]
print_matrix(matrix_1)
print_matrix(transpose_matrix(matrix_1))

matrix_2 = [[11, 12, 13],
            [14, 15, 16],
            [17, 18, 19]]
print_matrix(matrix_2)
print_matrix(transpose_matrix(matrix_2))


# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

names = ['str', 'int', 'bool', 'None', 'float', 'list', 'tuple', 'set']
vals = ['abc', 24, True, None, 3.14, [1, 2, 3], (1, 2, 3), {1, 2, 3}]


def form_dict(name_list, val_list):
    res_dict = {}
    for name, val in zip(name_list, val_list):
        try:
            res_dict[val] = name
        except TypeError:
            res_dict[str(val)] = name
    return res_dict


print(form_dict(names, vals))


# Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список

START_BALANCE = 0
DEPOSIT_FACTOR = 50
WITHDRAW_FACTOR = 50
WITHDRAW_RATE = 0.015
WITHDRAW_RATE_MIN = 30
WITHDRAW_RATE_MAX = 600
INTEREST_FREQUENCY = 3
INTEREST_PERCENT = 0.003
TRESHOLD_AMOUNT = 5_000_000
WEALTH_TAX = 0.010

balance = START_BALANCE
count = 0
operations = []


def deposit_account(acc_balance, operation_count, operation_list):
    deposit_amount = int(input(f'Ввести
     сумму пополнения, кратную {DEPOSIT_FACTOR}: '))
    if deposit_amount > 0 and deposit_amount % DEPOSIT_FACTOR == 0:
        acc_balance += deposit_amount
        operation_list.append(deposit_amount)
    else:
        print(f'Данная сумма пополнения не кратна {DEPOSIT_FACTOR}')

    print(f'Баланс вашего счета: {acc_balance:.0f}')
    operation_count += 1

    return acc_balance, operation_count, operation_list


def withdraw_account(acc_balance, operation_count, operation_list):
    withdraw_amount = int(input(f'Ввести сумму снятия, кратную {WITHDRAW_FACTOR}.\n'
                                f'Нельзя снять больше, чем на счете: '))

    if withdraw_amount % WITHDRAW_FACTOR == 0:
        percent = balance * WITHDRAW_RATE
        if percent < WITHDRAW_RATE_MIN:
            percent = WITHDRAW_RATE_MIN
        elif percent > WITHDRAW_RATE_MAX:
            percent = WITHDRAW_RATE_MAX

        if withdraw_amount + percent > acc_balance:
            print('Недостаточно средств на счете')
        else:
            acc_balance -= withdraw_amount + percent
            operation_list.append(int(-withdraw_amount - percent))
    else:
        print(f'Данная сумма снятия не кратна {WITHDRAW_FACTOR}')
    print(f'Баланс счета: {acc_balance:.0f}')
    operation_count += 1
    return acc_balance, operation_count, operation_list


while True:

    if balance > TRESHOLD_AMOUNT:
        tax = balance * WEALTH_TAX
        balance -= tax
        print(f'Баланс счета после удержания налога: {balance:.0f}')
        operations.append(int(-tax))
    if count % INTEREST_FREQUENCY == 0:
        interest = balance * INTEREST_PERCENT
        balance += interest
        print(f'Баланс счета, после налога: {balance:.0f}')
        operations.append(int(interest))
    operation = input(f' Выбрать действие:\n1 - пополнить\n'
                      f'2 - снять\n3 - выйти\n')
match operation:
        case '1':
            balance, count, operations = deposit_account(balance, count, operations)
        case '2':
            balance, count, operations = withdraw_account(balance, count, operations)
        case '3':
            print(f'Баланс счета: {balance:.0f}')
            break
        case _:
            break

print(operations)               
    


