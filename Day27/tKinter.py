from tkinter import *
from random import choice

tk = Tk()
tk.title("This is my window")
tk.wm_minsize(height=400,width=500)
#label
label =Label(text="Hello I am default Button")
label.grid(column=0,row=0)
input = Entry(width=20)
input.grid(column=3,row=3)



def change_label():
    #lst = ["Red","Green", "Blue","orange"]
    #print(f"I want to change to {choice(lst)}")
    text = input.get()
    label["text"]=text




#Button
button = Button(background="lightGrey",text="I am Button", width=40,wraplength=40,command=change_label)
button.grid(column=2,row=0)




tk.mainloop()