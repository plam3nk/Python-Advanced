from collections import deque

quantity_of_food = int(input())
orders = deque(input().split())
max_order = max([int(x) for x in orders])
while quantity_of_food > 0:
    if not orders:
        break

    current_order = int(orders.popleft())
    if current_order > quantity_of_food:
        orders.insert(0, str(current_order))
        break

    quantity_of_food -= current_order
print(max_order)
if orders:
    print("Orders left: ", end="")
    print(*orders, sep=" ")
else:
    print("Orders complete")
