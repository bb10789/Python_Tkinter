from tkinter import *
from PIL import ImageTk, Image

root = Tk()
im = Image.open("pictures/buddy.jpg")

im = im.resize((round(im.size[0] * 0.2), round(im.size[1]*0.2)))
my_img = ImageTk.PhotoImage(im, size= 2)
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()