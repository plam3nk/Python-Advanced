def sorting_cheeses(**kwargs):
    sorted_data = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    items = []
    for cheese, quantity in sorted_data:
        items.append(cheese)
        items.extend(sorted(quantity,reverse=True))

    return "\n".join(str(x) for x in items)


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
