from tkinter import *

top = Tk()

listbox = Listbox(top, height=10,
                  width=15, 
                  bg="grey",
                  activestyle="dotbox", 
                  font="Times", 
                  fg="yellow",
                  selectmode = MULTIPLE)

top.geometry("300x250")

label = Label(top, text = "Food Items")

listbox.insert(1,'sandwiches')
listbox.insert(2,'burger')
listbox.insert(3,'pizza')
listbox.insert(4,'Hotdogs')
listbox.insert(5,'Chicken Sandwiches')
listbox.insert(6,'IN And OUT')


label.pack()

listbox.pack()

top.mainloop()