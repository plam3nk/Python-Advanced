from collections import deque


def math(symbol, bee, nectar):

    if symbol == "+":
        return abs(bee + nectar)
    elif symbol == "-":
        return abs(bee - nectar)
    elif symbol == "/":
        if bee == 0 or nectar == 0:
            return 0
        else:
            return abs(bee / nectar)
    elif symbol == "*":
        return abs(bee * nectar)


bees = deque(int(x) for x in input().split())
nectar_values = [int(x) for x in input().split()]
symbols = deque(input().split())
honey = 0
while bees and nectar_values:
    current_bee = bees.popleft()
    current_nectar = nectar_values.pop()

    if current_nectar >= current_bee:
        current_symbol = symbols.popleft()
        honey += math(current_symbol, current_bee, current_nectar)
    else:
        bees.insert(0, current_bee)

print(f"Total honey made: {honey}")

if bees:
    print("Bees left:", end=" ")
    print(", ".join(str(x) for x in bees))

if nectar_values:
    print("Nectar left:", end=" ")
    print(", ".join(str(x) for x in nectar_values))
