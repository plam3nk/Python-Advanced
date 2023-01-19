size_of_square_matrix = int(input())
matrix = []
for row in range(size_of_square_matrix):
    current_row = input()
    matrix.append([])
    for letter in current_row:
        matrix[row].append(letter)
symbol = input()
is_found = False
for row in range(len(matrix)):
    for letter in range(len(matrix[row])):
        if matrix[row][letter] == symbol:
            print(f"({row}, {letter})")
            is_found = True
    if is_found:
        break
else:
    print(f"{symbol} does not occur in the matrix")