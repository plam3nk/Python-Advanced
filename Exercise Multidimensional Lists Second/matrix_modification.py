rows = int(input())
matrix = [[int(column) for column in input().split()]for row in range(rows)]

command = input()
while command != "END":
    action, row, col, value = command.split()
    if not 0 <= int(row) <= len(matrix) - 1 or not 0 <= int(col) <= len(matrix[0]) - 1:
        print("Invalid coordinates")
        command = input()
        continue
    else:
        if action == "Add":
            matrix[int(row)][int(col)] += int(value)
        elif action == "Subtract":
            matrix[int(row)][int(col)] -= int(value)
    command = input()
for row in matrix:
    print(" ".join(str(x)for x in row))
