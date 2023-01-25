from collections import deque

chocolate = [int(x) for x in input().split(", ")]
cups_of_milk = deque(int(x) for x in input().split(", "))
milkshakes = 0
while chocolate and cups_of_milk:

    current_chocolate = chocolate.pop()
    current_cup = cups_of_milk.popleft()
    if current_cup <= 0 and current_chocolate <= 0:
        continue
    if current_cup <= 0:
        chocolate.append(current_chocolate)
        continue
    if current_chocolate <= 0:
        cups_of_milk.insert(0, current_cup)
        continue
    if current_cup == current_chocolate:
        milkshakes += 1
    else:
        chocolate.append(current_chocolate)
        cups_of_milk.append(current_cup)
        chocolate[-1] -= 5
    if milkshakes == 5:
        print("Great! You made all the chocolate milkshakes needed!")
        break

if milkshakes < 5:
    print("Not enough milkshakes.")

if chocolate:
    print("Chocolate:", end=" ")
    print(", ".join(str(x) for x in chocolate))
else:
    print("Chocolate: empty")
if cups_of_milk:
    print("Milk:", end=" ")
    print(", ".join(str(x) for x in cups_of_milk))
else:
    print("Milk: empty")
