from collections import deque

names = input().split()
step_hot_potato = int(input())

names_deque = deque(names)
counter = 0
while len(names_deque) > 1:
    counter += 1
    current_name = names_deque.popleft()
    if counter == step_hot_potato:
        print(f"Removed {current_name}")
        counter = 0
    else:
        names_deque.append(current_name)

print(f"Last is {names_deque[0]}")
