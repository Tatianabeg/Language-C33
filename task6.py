# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
import random
txt = "абв"
print("word to delete: ", txt)
num_word = (int(input("number of words in the text: ")))
list_word = []
print("random text: ")
for x in range(num_word):
    random_txt = random.sample(txt, 3)
    list_word.append("".join(random_txt))
print(" ".join(list_word))

print("text without абв: ")
list_word2 = list(filter(lambda x: txt not in x, list_word))
print (" ".join(list_word2))
print(" ".join(list_word2))


 #Создайте программу  для игры в ""Крестики-нолики""
board  = list (range (1,10))

def draw_board(board):
    print ("-" * 13)
    for i in range (3):
        print ("|", board [0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-" * 13)

def take_input (player_token):
    valid  = False
    while  notvalid:
        player_answer = input("motion " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("mistake,this is a number?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ("the cage is occupied")
        else:
            print ("mistage,entering a number from 1 to 9")

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "victory")
                win = True
                break
        if counter == 9:
            print ("draw!")
            break
    draw_board(board)

main(board)