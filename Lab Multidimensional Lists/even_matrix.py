rows = int(input())
matrix = [[int(column) for column in input().split(", ") if int(column) % 2 == 0] for row in range(rows)]
print(matrix)