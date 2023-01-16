number_of_lines = int(input())
parking_lot = set()
for line in range(number_of_lines):
    direction, car_number = input().split(", ")

    if direction == "IN":
        parking_lot.add(car_number)
    elif direction == "OUT":
        parking_lot.remove(car_number)
if parking_lot:
    for car in parking_lot:
        print(car)
else:
    print("Parking Lot is Empty")