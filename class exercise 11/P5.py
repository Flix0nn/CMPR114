import tkinter as tk
from tkinter import ttk

def submit():
    name = name_entry.get()
    age = age_entry.get()
    address = address_entry.get()
    city = city_entry.get()
    state = state_entry.get()
    zipcode = zipcode_entry.get()
    tree.insert("", tk.END, values=(name,age,address,city,state,zipcode))
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    city_entry.delete(0, tk.END)
    state_entry.delete(0, tk.END)
    zipcode_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Grid View Example")

tree = ttk.Treeview(root, columns=("Name", "Age","Address","City","State","Zipcode"))
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("Address", text="Address")
tree.heading("City", text="City")
tree.heading("State", text="State")
tree.heading("Zipcode", text="Zipcode")
tree.pack()

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

age_label = tk.Label(root, text="Age:")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

city_label = tk.Label(root, text="City:")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

state_label = tk.Label(root, text="State:")
state_label.pack()
state_entry = tk.Entry(root)
state_entry.pack()

zipcode_label = tk.Label(root, text="Zipcode:")
zipcode_label.pack()
zipcode_entry = tk.Entry(root)
zipcode_entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

root.mainloop()