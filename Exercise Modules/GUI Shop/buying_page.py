from json import load, dump
from tkinter import Button

from PIL import Image, ImageTk
from helpers import clean_screen
from canvas import frame, root


def display_products():
    clean_screen()
    visualize_elements()


def visualize_elements():
    global info
    with open("db/products_data.json", "r") as stock:
        info = load(stock)

    x, y = 125, 25

    for item_name, item_info in info.items():
        item_img = ImageTk.PhotoImage(Image.open(item_info["image"]))
        images.append(item_img)

        frame.create_text(x, y, text=item_name, font=("Comic Sans MS", 15))
        frame.create_image(x, y + 130, image=item_img)

        if item_info["quantity"]:
            color = "green"
            text = f"In stock: {item_info['quantity']}"

            item_button = Button(
                root,
                text="Buy",
                font=("Comic Sans MS", 12),
                bg="green",
                fg="white",
                width=5,
                command=lambda x=item_name: buy_product(x),
            )

            frame.create_window(x, y + 285, window=item_button)

        else:
            color = "red"
            text = "Out of stock"

        frame.create_text(x, y + 255, text=text, font=("Comic Sans MS", 12), fill=color)

        x += 200

        if x > 550:
            x = 125
            y += 315


def buy_product(product):
    info[product]["quantity"] -= 1

    with open("db/products_data.json", "w") as stock:
        dump(info, stock)

    display_products()


images = []
info = {}
