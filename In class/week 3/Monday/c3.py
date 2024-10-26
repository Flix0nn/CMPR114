import tkinter as tk
from tkinter import messagebox

def submit():
    name = name_entry.get() #.get() retrieves the input from the name
    age = age_entry.get()
    hobbies = hobby_entry.get()

    #if all inputs are in the correct format
    if not name.isdigit() and age.isdigit() and not hobbies.isdigit():
        write_to_file(name, age, hobbies)
        messagebox.showinfo("Success", "Data recorded")


    elif name.isdigit() and not age.isdigit():
        messagebox.showerror("error, fix the inputs")

    else:
        messagebox.showerror("error", 'invalid input for name, age, hobbies')

def clear():
    name_entry.delete(0,tk.END)
    age_entry.delete(0,tk.END)
    hobby_entry.delete(0,tk.END)

def write_to_file(name, age, hobbies):
    file_name = "hobbies.txt"
    
                          #a means to append
    with open (file_name, 'a') as file:
        file.write(f"Name: {name} \n")
        file.write(f"Age: {age} \n")
        file.write(f"Your Hobbys are: {hobbies} \n")
    
        print(f"Data written to the {file_name} was transferred")

window = tk.Tk()

name_label = tk.Label(window, text="name")
name_label.pack()#pack function allow the widgets to be placed on the
#window with no spaces in between

name_entry = tk.Entry(window)
name_entry.pack()

age_label = tk.Label(window, text="age")
age_label.pack()

age_entry = tk.Entry(window)
age_entry.pack()

hobbies_label = tk.Label(window, text="enter hobby")
hobbies_label.pack()

hobby_entry = tk.Entry(window)
hobby_entry.pack()

submit_button = tk.Button(window,text = "SUBMIT", command=submit)
submit_button.pack()

clear_button = tk.Button(window,text = "CLEAR", command=clear)
clear_button.pack()

window.mainloop()#window will stay open for us


