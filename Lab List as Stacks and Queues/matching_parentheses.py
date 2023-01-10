string = input()
indexes = []
for index in range(len(string)):
    character = string[index]
    if character == "(":
        indexes.append(index)
    elif character == ")":
        last_index = indexes.pop()
        print(f"{string[last_index:index+1]}")