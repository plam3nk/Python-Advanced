string = input()
my_stack = []
for character in string:
    my_stack.append(character)

while my_stack:
    print(my_stack.pop(), end="")