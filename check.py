from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.geometry("400x400")


var = StringVar()

def show():
    myLabel = Label(root, text=var.get()).pack()

c = Checkbutton(root, text="Check this box, I dare you!", variable=var, onvalue="on", offvalue="off")
c.select()
c.pack()


my_button = Button(root, text="Show Selection", command=show).pack()
root.mainloop()