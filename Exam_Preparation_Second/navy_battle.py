size_of_matrix = int(input())

matrix = []

for row in range(size_of_matrix):
    columns = input()
    matrix.append(columns)

directions = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0],
}

submarine_pos = []
for row in range(len(matrix)):
    if "S" in matrix[row]:
        col = matrix[row].index("S")
        submarine_pos.append(row)
        submarine_pos.append(col)
        break

matrix[submarine_pos[0]] = matrix[submarine_pos[0]].replace("S", "-")
naval_mines = 0
destroyed_cruisers = 0
while True:

    direction = input()
    submarine_pos[0] += directions[direction][0]
    submarine_pos[1] += directions[direction][1]

    if matrix[submarine_pos[0]][submarine_pos[1]] == "-":
        continue

    elif matrix[submarine_pos[0]][submarine_pos[1]] == "*":
        matrix[submarine_pos[0]] = matrix[submarine_pos[0]][:submarine_pos[1]] + "-" \
                                   + matrix[submarine_pos[0]][submarine_pos[1] + 1:]
        naval_mines += 1
        if naval_mines == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_pos[0]}, {submarine_pos[1]}]!")
            break

    elif matrix[submarine_pos[0]][submarine_pos[1]] == "C":
        matrix[submarine_pos[0]] = matrix[submarine_pos[0]][:submarine_pos[1]] + "-" \
                                   + matrix[submarine_pos[0]][submarine_pos[1] + 1:]
        destroyed_cruisers += 1
        if destroyed_cruisers == 3:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

matrix[submarine_pos[0]] = matrix[submarine_pos[0]][:submarine_pos[1]] + "S" \
                           + matrix[submarine_pos[0]][submarine_pos[1]+1:]
for row in matrix:
    print(row)


