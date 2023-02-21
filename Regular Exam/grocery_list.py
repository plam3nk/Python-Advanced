def shop_from_grocery_list(*data):
    budget = data[0]
    grocery_lst = data[1]
    bought_products = []
    for i in range(2, len(data)):
        product = data[i][0]
        price = data[i][1]
        if product in grocery_lst:
            if budget >= price:
                bought_products.append(product)
                budget -= price
                grocery_lst.remove(product)
            elif price > budget:
                break

    if not grocery_lst:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f'You did not buy all the products. Missing products: {", ".join(x for x in grocery_lst)}.'


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))



