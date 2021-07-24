from tkinter import *

root = Tk()
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number) :
    curr_val = e.get()
    e.delete(0, END)
    e.insert(0, str(curr_val) + str(number))

def button_clear() :
    e.delete(0, END)

def button_add() :
    previous_val = e.get()
    global f_num
    global math
    math = "add"
    f_num = int(previous_val)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    s_num = int(second_number)
    result = 0;
    if math == "add":
        result = f_num + s_num
    elif math == "subtract":
        result = f_num - s_num
    elif math == "multiply":
        result = f_num * s_num
    elif math == "divide":
        result = f_num / s_num
    e.insert(0, result)

def button_subtract():
    previous_val = e.get()
    global f_num
    global math
    math = "subtract"
    f_num = int(previous_val)
    e.delete(0, END)

def button_multiply():
    previous_val = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(previous_val)
    e.delete(0, END)

def button_divide():
    previous_val = e.get()
    global f_num
    global math
    math = "divide"
    f_num = int(previous_val)
    e.delete(0, END)


# Define BUttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root, text="clear", padx=79, pady=20, command=button_clear)

button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)
button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)

#Put buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_subtract.grid(row=6, column=0)
button_divide.grid(row=6, column=1)
button_multiply.grid(row=6, column=2)


root.mainloop()