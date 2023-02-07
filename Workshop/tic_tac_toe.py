from math import ceil


def setup():
    global player_one, player_two
    player_one_name = input("First player name: ")
    player_two_name = input("Second player name: ")

    player_one_character = input(f"{player_one_name} would you like to play with 'X' or 'O'?: ")
    player_two_character = ""
    if player_one_character == "X":
        player_two_character = "O"
    elif player_two_character == "O":
        player_two_character = "X"
    else:
        while player_one_character not in "XO":
            player_one_character = input("Oops.. Invalid character. Try again!")
    player_one = [player_one_name, player_one_character]
    player_two = [player_two_name, player_two_character]
    print("This is the numeration of the board:")
    print("|  1  |  2  |  3  |")
    print("|  4  |  5  |  6  |")
    print("|  7  |  8  |  9  |")
    print(f"{player_one_name} starts first!")


def print_board(board):
    for row in board:
        print("|", end="")
        print('  |  '.join(str(x) for x in row), end='')
        print("  |")


def check_win(current_player, board):
    global not_winner
    first_row = all(x == current_player[1] for x in board[0])
    second_row = all(x == current_player[1] for x in board[1])
    third_row = all(x == current_player[1] for x in board[2])
    first_column = all(x == current_player[1] for x in [board[0][0], board[1][0], board[2][0]])
    second_column = all(x == current_player[1] for x in [board[0][1], board[1][1], board[2][1]])
    third_column = all(x == current_player[1] for x in [board[0][2], board[1][2], board[2][2]])
    first_diagonal = all(x == current_player[1] for x in [board[0][0], board[1][1], board[2][2]])
    second_diagonal = all(x == current_player[1] for x in [board[2][0], board[1][1], board[0][2]])
    if any([first_row, second_row, third_row, first_column, second_column, third_column,
            first_diagonal, second_diagonal]):
        print(f"{current_player[0]} won!")
        not_winner = False


def gameplay(current_player, board):
    current_choice = int(input(f"{current_player[0]} choose free position: "))
    row = ceil(current_choice / 3) - 1
    column = current_choice % 3 - 1
    board[row][column] = current_player[1]
    print_board(board)
    check_win(current_player, board)


player_one = ''
player_two = ''
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

setup()

current_player = player_one
second_player = player_two
not_winner = True

while not_winner:
    gameplay(current_player, board)
    current_player, second_player = second_player, current_player




