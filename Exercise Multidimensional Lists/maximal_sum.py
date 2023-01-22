rows, columns = [int(x) for x in input().split()]

matrix = [[int(column) for column in input().split()] for row in range(rows)]
maximal_sum = 0
sub_matrix = 0

for row in range(rows - 2):
    for col in range(columns - 2):
        current_sum = 0
        current_matrix = []
        for r in range(3):
            current_matrix.append([])
            for c in range(3):
                current_matrix[r].append(int(matrix[r+row][c+col]))
        for items in current_matrix:
            current_sum += sum(items)
        if current_sum >= maximal_sum:
            maximal_sum = current_sum
            sub_matrix = current_matrix

print(f"Sum = {maximal_sum}")
for row in sub_matrix:
    print(*row)
