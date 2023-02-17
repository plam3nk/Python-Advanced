from collections import deque

bowls = [int(x) for x in input().split(', ')]
customers = deque(int(x) for x in input().split(', '))

while bowls and customers:
    current_ramen = bowls.pop()
    current_customer = customers.popleft()

    if current_ramen == current_customer:
        continue
    elif current_ramen > current_customer:
        diff = current_ramen - current_customer
        bowls.append(diff)
    elif current_customer > current_ramen:
        diff = current_customer - current_ramen
        customers.insert(0, diff)

if not customers:
    print("Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join([str(x) for x in bowls])}")
if customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")