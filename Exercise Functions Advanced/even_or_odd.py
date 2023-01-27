def even_odd(*args):
    parameter = args[-1]
    r = len(args) - 1
    numbers = args[:r]
    filtered_numbers = 0
    if parameter == "even":
        filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    elif parameter == "odd":
        filtered_numbers = list(filter(lambda x: x % 2 != 0, numbers))

    return filtered_numbers


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))