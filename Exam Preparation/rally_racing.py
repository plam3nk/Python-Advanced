size_of_matrix = int(input())
racing_number = input()

matrix = [[column for column in input().split()] for row in range(size_of_matrix)]

directions = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0],
}

passed_kilometres = 0

command = input()
car_pos = [0, 0]
finished = False

while command != "End":
    current_direction = command

    car_pos[0] += directions[current_direction][0]
    car_pos[1] += directions[current_direction][1]

    if matrix[car_pos[0]][car_pos[1]] == ".":
        passed_kilometres += 10

    elif matrix[car_pos[0]][car_pos[1]] == "T":
        matrix[car_pos[0]][car_pos[1]] = "."
        is_found = False

        for row in range(len(matrix)):
            if "T" in matrix[row]:
                column = matrix[row].index("T")
                matrix[row][column] = "."

                car_pos[0] = row
                car_pos[1] = column
                passed_kilometres += 30
                break

    elif matrix[car_pos[0]][car_pos[1]] == "F":
        passed_kilometres += 10
        print(f"Racing car {racing_number} finished the stage!")
        finished = True
        break

    command = input()

if not finished:
    print(f"Racing car {racing_number} DNF.")

print(f"Distance covered {passed_kilometres} km.")

matrix[car_pos[0]][car_pos[1]] = "C"

for row in matrix:
    print(*row, sep="")
