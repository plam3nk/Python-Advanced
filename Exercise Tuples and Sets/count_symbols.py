input_line = tuple(x for x in input())
input_line = sorted(input_line)
symbols_count = {}
for item in input_line:
    if item not in symbols_count:
        symbols_count[item] = 0
    symbols_count[item] += 1
for key, value in symbols_count.items():
    print(f"{key}: {value} time/s")
