from tkinter import *
from PIL import ImageTk, Image, ImageEnhance
import glob, os

my_img1 = Image.open("pictures/pic1.jpg")
root = Tk()
root.title("Image Viewer")
# Image size
size = (922, 693)
image_list = []
image_image_list = []
image_name_list =[]
image_image_copy_list = []

def import_image() :
    # image import
    for infile in glob.glob("pictures/*.jpg"):
        curr_image = Image.open(infile)
        curr_image = curr_image.resize(size)
        image_name_list.append(infile)
        image_image_list.append(curr_image)
        image_image_copy_list.append(curr_image)
        image_list.append(ImageTk.PhotoImage(curr_image))



status = Label(root, text ="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

def forward(index):
    global my_label
    global button_forward
    global button_back
    global status
    global button_edit

    save()
    my_label.grid_forget()
    status.grid_forget()
    button_edit.grid_forget()
    my_label = Label(image=image_list[index - 1])
    button_forward = Button(root, text=">>", command=lambda:forward(index+1))
    button_back = Button(root, text="<<", command=lambda:back(index-1))
    my_label.grid(row=1, column=0, columnspan=3)
    button_edit = Button(root, text="edit", command=lambda: edit(index))
    print ("Curr Index: ", index)

    if index == len(image_list):
        button_forward = Button(root, text=">>", state=DISABLED)
    button_forward.grid(row=2, column=2)
    button_back.grid(row=2, column=0)
    status = Label(root, text="Image " + str(index) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=3, column=0, columnspan=3, sticky=W + E)
    button_edit.grid(row=0, column=0, sticky=W)

def back(index):
    print(index)
    global my_label
    global button_forward
    global button_back
    global status
    global button_edit

    save()
    my_label.grid_forget()
    status.grid_forget()
    button_edit.grid_forget()
    my_label = Label(image=image_list[index - 1])
    button_forward = Button(root, text=">>", command=lambda:forward(index+1))
    button_back = Button(root, text="<<", command=lambda :back(index-1))
    button_edit = Button(root, text="edit", command=lambda: edit(index))

    if index <= 1:
        button_back = Button(root, text="<<", state=DISABLED)

    button_forward.grid(row=2, column=2)
    button_back.grid(row=2, column=0)
    my_label.grid(row=1, column=0, columnspan=3)
    status = Label(root, text="Image " + str(index) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=3, column=0, columnspan=3, sticky=W + E)
    button_edit.grid(row=0, column=0, sticky=W)

def update_image():
    # Contrast
    global my_label
    global image_contrast
    global image_saturation
    global image_brightness
    global image_index

    my_label.grid_forget()
    # Get image
    img = image_image_copy_list[image_index - 1]

    level = int(image_contrast)
    factor = (259 * (level + 255)) / (255 * (259 - level))
    def contrast_method(c):
        return 128 + factor * (c - 128)
    contrast_image = img.point(contrast_method)
    # Update image again
    img = contrast_image

    level = image_brightness
    # Brightness
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(level)
    img2 = ImageTk.PhotoImage(img)

    level = image_saturation
    # Contrast
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(level)


    img2 = ImageTk.PhotoImage(img)
    my_label = Label(image=img2)
    my_label.img = img2
    my_label.grid(row=1, column=0, columnspan=3)
    image_image_list[image_index - 1] = img



def change_contrast(value):

    global image_index
    global image_contrast

    image_contrast = int(value)
    update_image()



def change_brightness(value):
    global image_brightness
    level = float(value)
    level = 1 + level / 100
    image_brightness = level

    update_image()




def change_saturation(value) :
    global image_saturation
    level = float(value)
    level = 1 + level / 100

    image_saturation = level
    update_image()

def save():
    global image_index
    global contrast
    global brightness
    global saturation
    global contrast_text
    global brightness_text
    global saturation_text
    global status
    global edit_opened
    global my_label

    if edit_opened:
        my_label.grid_forget();
        contrast.grid_forget();
        brightness.grid_forget();
        saturation.grid_forget();
        contrast_text.grid_forget();
        brightness_text.grid_forget();
        saturation_text.grid_forget();
        save_button.grid_forget();
        status.grid_forget()
        status.grid(row=3, column=0, columnspan=3, sticky=W + E)
        img = image_image_list[image_index - 1]
        img.save(image_name_list[image_index - 1])
        img_Tk = ImageTk.PhotoImage(img)
        image_list[image_index - 1] = img_Tk
        image_list[image_index - 1].img = img_Tk
        my_label = Label(image=img_Tk)
        my_label.img = img_Tk
        my_label.grid(row=1, column=0, columnspan=3)

        print("Image Saved at ", image_name_list[image_index - 1])
    edit_opened = False


def edit(index):
    # Values
    global status
    global image_index
    global my_label
    global  image_contrast
    global image_brightness
    global image_saturation

    # Widgets
    global contrast
    global brightness
    global saturation
    global contrast_text
    global brightness_text
    global saturation_text
    global save_button

    global edit_opened
    edit_opened = True

    image_contrast = 0
    image_brightness = 1
    image_saturation = 1
    image_index = index


    contrast = Scale(root, from_=0, to=100, orient=HORIZONTAL, length=500, command=change_contrast)
    brightness = Scale(root, from_=0, to=100, orient=HORIZONTAL, length=500, command=change_brightness)
    saturation = Scale(root, from_=0, to=100, orient=HORIZONTAL, length=500, command=change_saturation)
    save_button = Button(root, text="save", command=save)
    contrast_text = Label(text="Contrast")
    brightness_text = Label(text="Brightness")
    saturation_text = Label(text="Saturation")
    status.grid_forget()

    contrast.grid(row=3, column=1, columnspan=2)
    brightness.grid(row=4, column=1, columnspan=3)
    saturation.grid(row=5, column=1, columnspan=3)
    contrast_text.grid(row=3, column=0)
    brightness_text.grid(row=4, column=0)
    saturation_text.grid(row=5, column=0)
    save_button.grid(row = 6, column=1)
    status = Label(root, text="Image " + str(index) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=7, column=0, columnspan=3, sticky=W + E)
    return

def open_file():
    return

# for img in image_list:
#     resized_img = img.resize((round(img.size[0] * 0.2), round(img.size[1] * 0.2)))
#     image_resize_list.append(ImageTk.PhotoImage(resized_img))

global edit_opened
edit_opened = False
import_image()
my_label = Label(image=image_list[0])
my_label.grid(row=1, column=0, columnspan=3)

button_back = Button(root, text="<<", state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda:forward(2))
button_edit = Button(root, text="edit", command=lambda:edit(1))
button_open = Button(root, text="open file", command=lambda:open_file())
status = Label(root, text="Image 1" + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

button_back.grid(row=2, column=0)
button_exit.grid(row=2, column=1)
button_forward.grid(row=2, column=2, pady=10)
button_edit.grid(row=0, column=0, sticky=W)
button_open.grid(row=0, column=2, sticky=E)


status.grid(row=3, column=0, columnspan=3, sticky=W+E)

root.mainloop()