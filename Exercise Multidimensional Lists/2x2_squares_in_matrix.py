rows, columns = input().split()
matrix = [[column for column in input().split()] for row in range(int(rows))]

squares_in_matrix = 0

for row in range(int(rows) - 1):
    for column in range(int(columns) - 1):
        symbol = matrix[row][column]

        if matrix[row][column + 1] == symbol \
                and matrix[row + 1][column] == symbol \
                and matrix[row + 1 ][column + 1] == symbol:
            squares_in_matrix += 1

print(squares_in_matrix)