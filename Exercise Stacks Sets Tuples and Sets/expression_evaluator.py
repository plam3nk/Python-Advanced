from functools import reduce

integers_operators = input().split()
index = 0

functions = {
    "*": lambda i: reduce(lambda a, b: int(a) * int(b), integers_operators[:i]),
    "/": lambda i: reduce(lambda a, b: int(a) / int(b), integers_operators[:i]),
    "-": lambda i: reduce(lambda a, b: int(a) - int(b), integers_operators[:i]),
    "+": lambda i: reduce(lambda a, b: int(a) + int(b), integers_operators[:i]),
}

while index < len(integers_operators):
    item = integers_operators[index]
    if item in "*/+-":
        result = functions[item](index)
        [integers_operators.pop(1) for i in range(index)]
        integers_operators[0] = result
        index = 0
    index += 1
print(int(integers_operators[0]))