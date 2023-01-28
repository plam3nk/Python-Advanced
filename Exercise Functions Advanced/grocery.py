def grocery_store(**data):
    sorted_data = sorted(data.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    return '\n'.join([f"{key}: {value}" for key, value in sorted_data])


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
