from tkinter import *

window = Tk()
window.title("Length Converter App")
window.geometry("400x300")

def convert_length():
    inches = entry_2.get()
    inch_to_centimeters = 2.54
    centimeters = float(inches) * inch_to_centimeters

    converting_value = entry_2.get()
    result_label.config(text = f"• {converting_value} inches converted to centimeters is: {centimeters}")

frame_1 = Frame(master = window, width = 360, height = 200, bg = "#9400D3")

label_1 = Label(text = "Name", fg = "#FFFFFF", bg = "#C443D5")
label_2 = Label(text = "Length in inches", fg = "#FFFFFF", bg = "#C443D5")

entry_1 = Entry(frame_1)
entry_2 = Entry(frame_1)

button = Button(text = "Convert", bg = "#77176C", fg = "#FFFFFF", command = convert_length)

frame_1.place(x = 20, y = 0)
label_1.place(x = 20, y = 20)
entry_1.place(x = 150, y = 20)
label_2.place(x = 20, y = 80)
entry_2.place(x = 150, y = 80)
button.place(x = 150, y = 150)

result_label = Label(window, text = "")
result_label.place(x = 10, y = 200)


window.mainloop()