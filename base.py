from tkinter import *
from PIL import ImageTk, Image

root = Tk()




def open() :
    top = Toplevel()
    lbl = Label(top, text="Hello World").pack()
    global my_img
    my_img = ImageTk.PhotoImage(Image.open("pictures/pic1.jpg"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close Window", command=top.destroy).pack()

btn = Button(root, text ="Open Second Window", command=open).pack()

root.mainloop()