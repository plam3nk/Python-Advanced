size_of_board = int(input())
board = [[column for column in input()] for row in range(size_of_board)]

positions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, -1),
    (2, 1),
    (1, 2),
    (1, -2)
)

removed_knights = 0

while True:
    max_attacks = 0
    most_attacks_knight_pos = []

    for row in range(size_of_board):
        for col in range(size_of_board):
            if board[row][col] == "K":
                attacks = 0

                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < size_of_board and 0 <= pos_col < size_of_board:
                        if board[pos_row][pos_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    most_attacks_knight_pos = [row, col]
                    max_attacks = attacks

    if most_attacks_knight_pos:
        board[most_attacks_knight_pos[0]][most_attacks_knight_pos[1]] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)