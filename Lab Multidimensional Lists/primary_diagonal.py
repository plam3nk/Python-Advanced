size_of_matrix = int(input())
matrix = []
for line in range(size_of_matrix):
    column = [int(x) for x in input().split()]
    matrix.append(column)
primary_diagonal = []
row = 0
for index in range(len(matrix[0])):
    primary_diagonal.append(matrix[row][index])
    row += 1
print(sum(primary_diagonal))

