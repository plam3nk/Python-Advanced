input_line = input().split("|")

matrix = []

for item in input_line[::-1]:
    matrix.extend(item.split())

print(*matrix)