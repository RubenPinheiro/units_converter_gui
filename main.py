from tkinter import *
from tkinter import ttk

result = 0
result_unit = ['Cm', 'Kg']
window = Tk()
window.title("US units to Real units converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)


def action():
    if inches_pounds.get() == 'Inches':
        math = round(float(user_input.get()) * 2.54, 2)
        result_unit_label.config(text=f"{result_unit[0]}")
    else:
        math = round(float(user_input.get()) * 0.4535924,2)
        result_unit_label.config(text=f"{result_unit[1]}")
    result_label.config(text=f"{math}")


def update_label(event):
    if inches_pounds.get() == 'Inches':
        result_unit_label.config(text=f"{result_unit[0]}")
    else:
        result_unit_label.config(text=f"{result_unit[1]}")


user_input = Entry()
user_input.insert(END, result)
user_input.grid(column=2, row=1)

n = IntVar()
inches_pounds = ttk.Combobox(window, width=7, textvariable=n)
inches_pounds['values'] = ('Inches', 'Pounds')
inches_pounds.current(0)
inches_pounds.bind('<<ComboboxSelected>>', update_label)
inches_pounds.grid(column=3, row=1)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=2, row=2)
result_label = Label(text=f"{result}")
result_label.grid(column=3, row=2)
result_unit_label = Label(text=f"{result_unit[0]}")
result_unit_label.grid(column=4, row=2)


calculate = Button(text="Calculate", command=action)
calculate.grid(column=3, row=3)



window.mainloop()
