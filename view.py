from tkinter import *
from PIL import ImageTk, Image

root = Tk()
my_img1 = Image.open("pictures/buddy.jpg")
my_img2 = Image.open("pictures/pic1.jpg")
my_img3 = Image.open("pictures/pic2.jpg")
my_img4 = Image.open("pictures/pic3.jpg")
my_img5 = Image.open("pictures/pic4.jpg")

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]
image_resize_list = []


def forward(index):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_resize_list[index-1])
    button_forward = Button(root, text=">>", command=lambda:forward(index+1))
    button_back = Button(root, text="<<", command=lambda :back(index-1))
    my_label.grid(row=0, column=0, columnspan=3)

    if index == len(image_resize_list) - 1:
        button_forward = Button(root, text=">>", state=DISABLED)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)


def back(index):
    print(index)
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label.grid_forget()
    my_label = Label(image=image_resize_list[index-1])
    button_forward = Button(root, text=">>", command=lambda:forward(index+1))
    button_back = Button(root, text="<<", command=lambda :back(index-1))

    if index <= 1:
        button_back = Button(root, text="<<", state=DISABLED)

    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    my_label.grid(row=0, column=0, columnspan=3)

for img in image_list:
    resized_img = img.resize((round(img.size[0] * 0.2), round(img.size[1] * 0.2)))
    image_resize_list.append(ImageTk.PhotoImage(resized_img))

my_label = Label(image= image_resize_list[0])
my_label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text="<<", state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda:forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()