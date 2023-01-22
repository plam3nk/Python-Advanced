rows, columns = [int(x) for x in input().split()]

matrix = [[col for col in input().split()] for row in range(rows)]

command = input()
while command != "END":
    command = command.split()
    if command[0] == "swap" and len(command) == 5:
        r1, c1, r2, c2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])
        if r1 > len(matrix) or r2 > len(matrix) or c1 > len(matrix[0]) or c2 > len(matrix[0]):
            print("Invalid input!")
            command = input()
            continue
        temp = matrix[r1][c1]
        matrix[r1][c1] = matrix[r2][c2]
        matrix[r2][c2] = temp
        for items in matrix:
            print(" ".join(str(x) for x in items))
    else:
        print("Invalid input!")
    command = input()



