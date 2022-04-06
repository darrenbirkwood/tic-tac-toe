board = [" " for i in range(9)]

def print_board_key():
    row1 = "|{}|{}|{}|".format(1,2,3)
    row2 = "|{}|{}|{}|".format(4,5,6)
    row3 = "|{}|{}|{}|".format(7,8,9)

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def print_board():
    row1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
    row2 = "|{}|{}|{}|".format(board[3],board[4],board[5])
    row3 = "|{}|{}|{}|".format(board[6],board[7],board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    while True:
        try:
            if icon == "X":
                number = 1
            elif icon == "O":
                number = 2
                
            print("Your turn player {}".format(number))

            choice = int(input("Enter your move (1-9): ").strip())

            if choice <=0 or choice >=10:
                print("Please enter a number between 1 and 9.")
                continue
            elif board[choice-1]!=" ":
                print("That space is taken!")
                continue
            elif choice >= 1 or choice <= 9:
                break
        except ValueError:
            print("That's not a number!")

    board[choice-1]==" "
    board[choice-1]=icon

def is_victory(icon):
    if (board[0]==icon and board[1]==icon and board[2]==icon) or \
       (board[3]==icon and board[4]==icon and board[5]==icon) or \
       (board[6]==icon and board[7]==icon and board[8]==icon) or \
       (board[0]==icon and board[3]==icon and board[6]==icon) or \
       (board[1]==icon and board[4]==icon and board[7]==icon) or \
       (board[2]==icon and board[5]==icon and board[8]==icon) or \
       (board[0]==icon and board[4]==icon and board[8]==icon) or \
       (board[2]==icon and board[4]==icon and board[6]==icon):
        return True
    else:
        return False

def is_draw():
    if " " not in board:
        return True
    else:
        return False

print_board_key()
print("-------")
print_board()

while True:
    player_move("X")
    print_board_key()
    print("-------")
    print_board()
    if is_victory("X"):
        print("X Wins! Congratulations!")
        break
    elif is_draw():
        print("it's a draw!")
        break
    player_move("O")
    print_board_key()
    print("-------")
    print_board()
    if is_victory("O"):
        print_board()
        print("O Wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break
