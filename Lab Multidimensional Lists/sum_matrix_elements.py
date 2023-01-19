rows, columns = input().split(", ")
matrix = []
for row in range(int(rows)):
    matrix.append([])
    elements = input().split(", ")
    for column in range(int(columns)):
        matrix[row].append(int(elements[column]))
sum_of_matrix = sum([sum(items) for items in matrix])
print(sum_of_matrix)
print(matrix)