from tkinter import *


def calculate():
    km_result = int(input.get()) * 1.609
    result.config(text=str(round(km_result, 2)))


window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=100)
window.config(padx=50, pady=30)

# Input Entry
input = Entry(width=10)
input.grid(column=1, row=0)

# Label
miles = Label(text='Miles', font=('Arial', 10, 'bold'))
miles.grid(column=2, row=0)

is_equal_to = Label(text='is equal to', font=('Arial', 10, 'bold'))
is_equal_to.grid(column=0, row=1)

result = Label(text='0', font=('Arial', 10, 'bold'))
result.grid(column=1, row=1)

km = Label(text='km', font=('Arial', 10, 'bold'))
km.grid(column=2, row=1)

button = Button(text='Calculate', command=calculate)
button.grid(column=1, row=2)

window.mainloop()
