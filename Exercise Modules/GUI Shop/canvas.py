from tkinter import *


def create_app():
    root = Tk()
    root.geometry("700x600")
    root.title("Gui Product Shop")
    return root


def create_frame():
    frame = Canvas(root, width=700, height= 700)
    frame.grid(row=0, column=0)

    return frame


root = create_app()
frame = create_frame()