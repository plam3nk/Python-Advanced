def arrived_guests_data():
    arrived_guest_lst = []
    while True:
        data = input()
        if data == "END":
            break
        else:
            arrived_guest_lst.append(data)

    return arrived_guest_lst


def print_func(not_arrived_guests_data):
    print(len(not_arrived_guests_data))
    for guest_number in sorted(not_arrived_guests_data):
        print(guest_number)


number_of_guests = int(input())
guests_reservation = [input() for _ in range(number_of_guests)]
arrived_guests = arrived_guests_data()
not_arrived_guests = set(guests_reservation).difference(arrived_guests)
print_func(not_arrived_guests)
