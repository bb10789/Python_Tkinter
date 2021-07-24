from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look I clicked a button!!")
    myLabel.pack()


myButton = Button(root, text="CLick ME!", padx=50, command=myClick, fg="blue", bg="#ffffff")
myButton.pack()

root.mainloop()