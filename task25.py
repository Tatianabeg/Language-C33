
import data_check.date_check as dch
import data_check.chess_check as chess

_NEED_OK_POSITIONS = 4  # Необходимое кол-во успешных расстановок

def validate_queens(positions):
    for i in range(8):
        for j in range(i+1, 8):
            # проверка на наличие на одной строке или диагонали
            if positions[i] == positions[j] or \
                positions[i] - i == positions[j] - j or \
                positions[i] + i == positions[j] + j:
                return False
    return True


for list_position in queens_positions:
        print(list_position)
        if chess.check_queen_8x8(list_position):
            print("Ферзи друг друга не бьют")
        else:
            print(" Ферзи под ударом")

 
    total_case_generate = 0  
    case_ok = 0  
    list_ok_positions = []  

    while case_ok < _NEED_OK_POSITIONS:
        generated_position = chess.gen_positions()
        total_case_generate += 1
        if chess.check_queen_8x8(generated_position):
            case_ok += 1
            list_ok_positions.append(generated_position)

    print(f" Всего сгенерировано {total_case_generate}, удачные:")
    for pos in list_ok_positions:
        print(pos)
        