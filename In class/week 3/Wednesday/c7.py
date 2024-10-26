#from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 #databases using sqlite
#import flask #websites using CSS and HTML and JS

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username =="jsim" and password=="sac123":
        
        messagebox.showinfo("login", "Welcome")

        SecondForm.deiconify() #show this form
        FirstForm.withdraw() #hide this form

    else:
         messagebox.showerror("login","invalid")
         username_entry.delete(0,tk.END)
         password_entry.delete(0,tk.END)
         username_entry.focus_set() #places a cursor

def open_new_form():

    SecondForm = tk.Toplevel(root) #topLevel means that this is another form
    SecondForm.title("Customers Form")

    label = tk.Label(new_window, text = "welcome")
    label.pack()

FirstForm  = tk.Tk()
FirstForm.title("Login Form")

username_label = tk.Label(FirstForm, text = "username")
username_label.pack()

username_entry = tk.Entry(FirstForm)
username_entry.pack()

#password widgets
password_label = tk.Label(FirstForm, text = "password")
password_label.pack()

password_entry = tk.Entry(FirstForm, show="*")
password_entry.pack()

login_button = tk.Button(FirstForm, text ="login", command=login)
login_button.pack()

def display_message():

    name = name_entry.get()
    address = address_entry.get()
    city = city_entry.get()
    state = state_combobox.get()

    message = f"{name}\nAddress: {address}\n City: {city}\n State: {state}"

    messagebox.showinfo("Results", message)

SecondForm = tk.Tk()
SecondForm.title("Customers Form")
SecondForm.withdraw()

states = ['CA','TX']

name_label = tk.Label(SecondForm,text = "Name")
name_label.pack()

name_entry = tk.Entry(SecondForm)
name_entry.pack()

address_label = tk.Label(SecondForm,text = "address")
address_label.pack()

address_entry = tk.Entry(SecondForm)
address_entry.pack()

city_label = tk.Label(SecondForm,text = "city")
city_label.pack()

city_entry = tk.Entry(SecondForm)
city_entry.pack()

state_label = tk.Label(SecondForm, text = "state")
state_label.pack()

state_combobox = ttk.Combobox(SecondForm, values=states)
state_combobox.pack()

button = tk.Button(SecondForm, text="enter", command=display_message)
button.pack()

FirstForm.mainloop()
