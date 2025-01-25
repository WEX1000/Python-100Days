from tkinter import *


def miles_to_km():
    kilometer_result_label.config(text=float(miles_input.get())*1.609)

window = Tk()
window.title("Miles to Kilometers")
window.config(padx=20, pady=20)

miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_buton = Button(text="Calculate", command=miles_to_km)
calculate_buton.grid(column=1, row=2)





window.mainloop()