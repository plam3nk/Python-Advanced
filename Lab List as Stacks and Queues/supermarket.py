from collections import  deque

queue = deque()

command = input()
while command != "End":
    if command == "Paid":
        while queue:
            print(queue.popleft())
    else:
        name = command
        queue.append(name)

    command = input()

print(f"{len(queue)} people remaining.")