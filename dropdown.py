from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("400x400")


def show():
    myLabel = Label(root, text=clicked.get()).pack()


clicked = StringVar()
clicked.set("Monday")

options = [
    "Monday",
    "Tuesday",
    "Wed",
    "Thurs",
    "Fri"
]

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()
root.mainloop()
