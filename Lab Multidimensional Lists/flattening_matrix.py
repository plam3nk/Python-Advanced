matrix_rows = int(input())
matrix = [[int(column) for column in input().split(", ")] for row in range(matrix_rows)]
flattening_matrix = []
for row in range(len(matrix)):
    for column in matrix[row]:
        flattening_matrix.append(column)
print(flattening_matrix)
