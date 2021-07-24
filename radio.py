from tkinter import *
from PIL import ImageTk, Image

root = Tk()

r = IntVar()
r.set(2)

MODES = [
    ("Pepperoni", "Pepperoni",),
    ("Cheese", "Cheese",),
    ("Mushroom", "Mushroom",),
    ("Onion", "Onion",),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked():
    myLabel = Label(root, text=pizza.get())
    myLabel.pack()

#Radiobutton(root, text="Option 1", variable=r, value=1, command=clicked).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=clicked).pack()

myLabel = Label(root, text=pizza.get())
myLabel.pack()

myButton = Button(root, text="CLick Me", command=clicked)
myButton.pack()
root.mainloop()