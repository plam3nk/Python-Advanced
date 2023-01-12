from collections import deque

pumps_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

pumps_data_copy = pumps_data.copy()
index = 0
fuel_in_tank = 0

while pumps_data_copy:
    petrol, distance = pumps_data_copy.popleft()

    fuel_in_tank += petrol

    if fuel_in_tank - distance < 0:
        pumps_data.rotate(-1)
        pumps_data_copy = pumps_data.copy()
        index += 1
        fuel_in_tank = 0
    else:
        fuel_in_tank -= distance

print(index)