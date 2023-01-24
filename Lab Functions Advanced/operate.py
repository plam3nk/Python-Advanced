from functools import reduce


def operate(operator: str, *args):

    def addition():
        return reduce(lambda a, b: a + b, args)

    def subtract():
        return reduce(lambda a, b: a - b, args)

    def multiply():
        return reduce(lambda a, b: a * b, args)

    def divide():
        return reduce(lambda a, b: a / b, args)

    if operator == "+":
        return addition()
    elif operator == "-":
        return subtract()
    elif operator == "*":
        return multiply()
    elif operator == "/":
        return divide()


print(operate("*", 3, 4))
print(operate("+", 1, 2, 3))
