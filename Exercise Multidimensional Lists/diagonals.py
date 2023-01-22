rows = int(input())
matrix = [[int(column) for column in input().split(", ")]for row in range(rows)]

primary_diagonal = [matrix[row][row] for row in range(rows)]
secondary_diagonal = [matrix[row][rows - row - 1] for row in range(rows - 1, -1, -1)]

print(f"Primary diagonal: {', '.join(str(n) for n in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(n) for n in secondary_diagonal[::-1])}. Sum: {sum(secondary_diagonal)}")