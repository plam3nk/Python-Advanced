from json import loads, dump
from tkinter import Button, Entry

from canvas import root, frame
from helpers import clean_screen
from buying_page import display_products


def get_user_data():
    info_data = []

    with open("db/user_credentials_db.txt", "r") as users_file:
        for line in users_file:
            info_data.append(loads(line))

    return info_data


def render_entry():
    register_button = Button(
        root,
        text="Register",
        bg="darkgrey",
        fg="white",
        borderwidth=0,
        width=20,
        height=3,
        command=register,
    )

    login_button = Button(
        root,
        text="Login",
        bg="grey",
        fg="white",
        width=20,
        height=3,
        borderwidth=0,
        command=login
    )

    frame.create_window(350, 260, window=register_button)
    frame.create_window(350, 320, window=login_button)


def login():
    clean_screen()

    frame.create_text(100, 50, text="Username:")
    frame.create_text(100, 100, text="Password:")

    frame.create_window(200, 50, window=username_box)
    frame.create_window(200, 100, window=password_box)

    logging_button = Button(
        root,
        text="Login",
        bg="grey",
        fg="white",
        width=15,
        height=3,
        borderwidth=0,
        command=logging
    )

    frame.create_window(250, 150, window=logging_button)


def logging():
    if check_logging():
        display_products()
    else:
        frame.create_text(160,200, text="Invalid credentials!", fill="red")


def check_logging():
    info_data = get_user_data()
    user_username = username_box.get()
    user_password = password_box.get()

    for i in range(len(info_data)):
        username = info_data[i]["username"]
        password = info_data[i]["password"]

        if username == user_username and password == user_password:
            return True

    return False


def register():
    clean_screen()

    frame.create_text(150, 50, text="First name:")
    frame.create_text(150, 100, text="Last name:")
    frame.create_text(150, 150, text="Username:")
    frame.create_text(150, 200, text="Password:")

    frame.create_window(250, 50, window=first_name_box)
    frame.create_window(250, 100, window=last_name_box)
    frame.create_window(250, 150, window=username_box)
    frame.create_window(250, 200, window=password_box)

    registration_button = Button(
        root,
        text="Register",
        bg="darkgrey",
        fg="white",
        command=registration
    )

    frame.create_window(300, 300, window=registration_button)


def registration():
    info_dict = {
        "first_name": first_name_box.get(),
        "last_name": last_name_box.get(),
        "username": username_box.get(),
        "password": password_box.get(),
    }

    if check_registration(info_dict):
        with open("db/user_credentials_db.txt", "a") as users_file:
            dump(info_dict, users_file)
            users_file.write('\n')
            display_products()


def check_registration(info):
    for el in info.values():
        if not el.strip():
            frame.create_text(
                300,
                325,
                text="Some information is missing!",
                fill="red",
                tag="error"
            )

            return False

    frame.delete("error")

    info_data = get_user_data()

    for record in info_data:
        if record["username"] == info["username"]:
            frame.create_text(
                300,
                325,
                text="Username already exists!",
                fill="red",
                tag="error",
            )

            return False

    frame.delete("error")

    return True


first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0)
