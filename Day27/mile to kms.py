from tkinter import *

window = Tk()
window.wm_minsize(width=200, height=150)
window.config(padx=100, pady=50)

window.title("Miles to Kms Converter")

input = Entry(width=5)


input.grid(column=2, row=0)


l1 = Label(text="miles")
l1.grid(column=4, row=0)
l2 = Label(text="is equal to = ")
l2.grid(column=1, row=1)
l3 = Label(text="kms")
l3.grid(column=4, row=1)
l4 = Label(text="0")
l4.grid(column=2, row=1)

def mile_kms():
    mile = int(input.get())
    kms = mile * 1.609
    l4["text"]=f"{kms}"



button = Button(text="Calculate", command=mile_kms)
button.grid(column=2, row=5)

window.mainloop()
