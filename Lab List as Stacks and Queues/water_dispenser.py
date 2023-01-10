from collections import deque

water_quantity = int(input())
name = input()
queue = deque()
while name != "Start":
    queue.append(name)

    name = input()

command = input()
while command != "End":
    command = command.split()
    if command[0] == "refill":
        water_quantity += int(command[1])
    else:
        wanted_liters = int(command[0])
        if water_quantity >= wanted_liters:
            person_name = queue.popleft()
            print(f"{person_name} got water")
            water_quantity -= wanted_liters
        else:
            person_name = queue.popleft()
            print(f"{person_name} must wait")
    command = input()

print(f"{water_quantity} liters left")