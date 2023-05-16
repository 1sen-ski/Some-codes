import random

board = ["□", "□", "□",
         "□", "□", "□",
         "□", "□", "□"]

game_on = True
winning_player = None
current_player = "X"


def board_print(board):
    print(board[0] + " | " + board[1] + " | " + board[2])

    print(board[3] + " | " + board[4] + " | " + board[5])

    print(board[6] + " | " + board[7] + " | " + board[8])


def player_input(board):
    inp = int(input("Enter a number 1-9: "))
    if 1 <= inp <= 9 and board[inp - 1] == "□":
        board[inp - 1] = current_player
    else:
        print("Spot taken.")


def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "□":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "□":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "□":
        winner = board[6]
        return True


def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "□":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[0] != "□":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[0] != "□":
        winner = board[2]
        return True


def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "□":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "□":
        winner = board[2]
        return True


def check_tie(board):
    global game_on
    if "□" not in board:
        board_print(board)
        print("Tie!")
        game_on = False


def win_check():
    if check_diagonal(board) or check_horizontal(board) or check_row(board):
        print(f"The winner is {winner}")


def player_switch():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def against_pc(board):
    while current_player == "O":
        position = random.randint(0, 8)
        if board[position] == "□":
            board[position] = "O"
            player_switch()


while game_on:
    board_print(board)
    player_input(board)
    win_check()
    check_tie(board)
    player_switch()
    against_pc(board)
    win_check()
    check_tie(board)

print(board_print(board))
