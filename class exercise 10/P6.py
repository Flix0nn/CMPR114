import tkinter as tk

class EmployeeForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Employee From")

        self.label_name = tk.Label(self, text="Name:")
        self.label_name.grid(row=0, column=0)
        self.entry_name = tk.Entry(self)
        self.entry_name.grid(row=0, column=1)

        self.label_age = tk.Label(self, text="Age:")
        self.label_age.grid(row=1, column=0)
        self.entry_age = tk.Entry(self)
        self.entry_age.grid(row=1, column=1)

        self.button_submit = tk.Button(self, text="Submit", command=self.submit)
        self.button_submit.grid(row=2, columnspan=2, pady=10)

        self.geometry("300x200")

    def submit(self):
        name = self.entry_name.get()
        age = self.entry_age.get()
        self.display_employee_info(name, age)
    
    def display_employee_info(self, name, age):
        info_window = tk.Toplevel(self)
        info_window.title("Employee Information")
        info_window.geometry("300x100")

        label_info = tk.Label(info_window, text="Employee Information")
        label_info.pack(pady=10)
        label_name = tk.Label(info_window, text=f"Name: {name}")
        label_name.pack()

        label_age = tk.Label(info_window, text=f"Age: {age}")
        label_age.pack()
    
class ManagerForm(EmployeeForm):
    def __init__(self):
        super().__init__()
        self.title("Manager From")

        self.label_department = tk.Label(self, text="Deparment:")
        self.label_department.grid(row=3, column=0)
        self.entry_department = tk.Entry(self)
        self.entry_department.grid(row=3, column=1)

        self.geometry("400x250")

    def submit(self):
        name = self.entry_name.get()
        age = self.entry_age.get()
        department = self.entry_department.get()
        self.display_employee_info(name, age, department)
    
    def display_employee_info(self, name, age, department):
        info_window = tk.Toplevel(self)
        info_window.title("Manager Information")
        info_window.geometry("300x150")

        label_info = tk.Label(info_window, text="Manager Information")
        label_info.pack(pady=10)

        label_name = tk.Label(info_window, text=f"Name: {name}")
        label_name.pack()

        label_age = tk.Label(info_window, text=f"Age: {age}")
        label_age.pack()

        label_department = tk.Label(info_window, text=f"Department: {department}")
        label_department.pack()

if __name__ == "__main__":
    app = ManagerForm()
    app.mainloop()
