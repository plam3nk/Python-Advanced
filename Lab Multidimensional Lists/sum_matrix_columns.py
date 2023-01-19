def matrix_creator(rows: int, columns):
    matrix_creator = []
    for row in range(rows):
        matrix_creator.append([])
        columns = input().split()
        for column in columns:
            matrix_creator[row].append(int(column))
    return matrix_creator


rows, columns = input().split(", ")
matrix = matrix_creator(int(rows), columns)
for index in range(int(columns)):
    sum_of_each_column = 0
    for row in range(len(matrix)):
        sum_of_each_column += (matrix[row][index])
    print(sum_of_each_column)