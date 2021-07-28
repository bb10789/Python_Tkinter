from tkinter import *
from PIL import ImageTk, Image
import glob, os

root = Tk()
size = (922, 693)
image_list = []
image_image_list = []

# image import
for infile in glob.glob("pictures/*.jpg"):
    curr_image = Image.open(infile)
    curr_image = curr_image.resize(size)
    image_image_list.append(curr_image)
    image_list.append(ImageTk.PhotoImage(curr_image))


my_img = ImageTk.PhotoImage(image_image_list[0])
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()