def rectangle(length, width):
    if type(length) != int or type(width) != int:
        return "Enter valid values!"
    else:
        def area():
            return length * width

        def perimeter():
            return (length + width) * 2

    return f'''Rectangle area: {area()}
Rectangle perimeter: {perimeter()}'''


print(rectangle(2, 10))
