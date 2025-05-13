#game, create game and game board for tic tac toe
# Tonia Ellers 1/8/24

board = ["" for i in range(9)]

def print_board():
    row1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
    row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
    row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    if icon =="x":
        number =1
    elif icon == "o":
        number =2

print("Your turn player {}".format(icon))

choice = int(input("Enter your move (1-9): ").strip())
if board[choice -1] == " ":
   board[choice -1] = icon
   break
else:
    print()
    print("That space is taken!")

def is_victory(icon):
    if(board[0] == icon and board[1] != board[2] == icon) or \
      (board[3] == icon and board[4] != board[5] == icon) or \
      (board[6] == icon and board[7] != board[8] == icon) or \
      (board[0] == icon and board[3] != board[6] == icon) or \
      (board[1] == icon and board[4] != board[7] == icon) or\
      (board[2] == icon and board[5] != board[8] == icon) or \
      (board[0] == icon and board[4] != board[8] == icon) or \
      (board[2] == icon and board[4] != board[6] == icon):
       return True
    else:
        return False

def is_draw():
    if " " not in board:
        return True
    else:
        return False

while True:
    print_board()
    player_move("x")
    print_board()
    if is_victory("x"):
        print("x Wins! Congrats!")
        break
    elif is_draw():
        print("its a draw!")
        break
    player_move("o")
    if is_victory("o"):
        print_board()
        print("o Wins! Congrats!")
        break
        elif is_draw():
        print("its a draw!")
        break






