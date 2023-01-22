rows, columns = [int(x) for x in input().split()]

snake = [str(x) for x in input()]
counter = 0
for r in range(rows):
    current_string = ""
    for col in range(columns):
        if counter == len(snake):
            counter = 0
        current_string += snake[counter]
        counter += 1
    if r % 2 == 0:
        print(current_string)
    else:
        print(current_string[::-1])
