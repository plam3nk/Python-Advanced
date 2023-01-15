numbers = tuple(map(float, input().split()))

count_values = {}

for n in numbers:
    if n not in count_values:
        count_values[n] = 0
    count_values[n] += 1

for key, value in count_values.items():
    print(f"{key} - {value} times")