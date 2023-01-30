def move(direction, steps):
    r = my_pos[0] + (directions[direction][0] * steps)
    c = my_pos[1] + (directions[direction][1] * steps)

    if not (0 <= r < size and 0 <= c < size):
        return my_pos
    if matrix[r][c] == "x":
        return my_pos
    return [r, c]


def shoot(direction):
    r = my_pos[0] + directions[direction][0]
    c = my_pos[1] + directions[direction][1]

    while 0 <= r < size and 0 <= c < size:
        if matrix[r][c] == "x":
            matrix[r][c] = "."
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]


size = 5
matrix = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

shot_targets_pos = []
target_hits = 0
my_pos = []
targets = 0

for row in range(size):
    matrix.append(input().split())
    if "A" in matrix[row]:
        my_pos = [row, matrix[row].index("A")]
    if "x" in matrix[row]:
        targets += matrix[row].count("x")

for _ in range(int(input())):
    command_info = input().split()
    if command_info[0] == "move":
        my_pos = move(command_info[1], int(command_info[2]))
    elif command_info[0] == "shoot":
        shot_target_pos = shoot(command_info[1])

        if shot_target_pos:
            shot_targets_pos.append(shot_target_pos)
            target_hits += 1

        if targets == target_hits:
            print(f"Training completed! All {targets} targets hit.")
            break

else:
    print(f"Training not completed! {targets - target_hits} targets left.")

print(*shot_targets_pos, sep="\n")



