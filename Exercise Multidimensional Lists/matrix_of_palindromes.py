rows, columns = [int(x) for x in input().split()]
matrix = []

for row in range(rows):
    matrix.append([])

    for col in range(columns):

        current_string = f"{chr(97 + row)}{chr(97 + row + col)}{chr(97 + row)}"
        matrix[row].append(current_string)

for items in matrix:
    print(" ".join(str(x) for x in items))
