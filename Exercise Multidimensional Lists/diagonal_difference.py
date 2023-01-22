rows = int(input())
matrix = [[int(column) for column in input().split(" ")]for row in range(rows)]

primary_diagonal = [matrix[row][row] for row in range(rows)]
secondary_diagonal = [matrix[row][rows - row - 1] for row in range(rows - 1, -1, -1)]

result = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(result)