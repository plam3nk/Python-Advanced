def forecast(*data):
    print_string = ""
    locations = {}
    for location, weather in data:
        locations[location] = weather
    for location in sorted(locations.keys()):
        if locations[location] == "Sunny":
            print_string += f"{location} - {locations[location]}\n"

    for location in sorted(locations.keys()):
        if locations[location] == "Cloudy":
            print_string += f"{location} - {locations[location]}\n"

    for location in sorted(locations.keys()):
        if locations[location] == "Rainy":
            print_string += f"{location} - {locations[location]}\n"

    return print_string[:len(print_string)-1]


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))



