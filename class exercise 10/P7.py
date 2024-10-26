from cProfile import label
import tkinter as tk

class LoginForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login From")

        self.label_username = tk.Label(self, text="Username:")
        self.label_username.grid(row=0, column=0)
        self.entry_username = tk.Entry(self)
        self.entry_username.grid(row=0, column=1)

        self.label_password = tk.Label(self, text="Password:")
        self.label_password.grid(row=1, column=0)
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.grid(row=1, column=1)

        self.button_login = tk.Button(self, text="Login", command=self.login)
        self.button_login.grid(row=2, columnspan=2, pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "sac" and password == "sac":

            self.withdraw()
            order_form = OrderForm(self)
            order_form.mainloop()
        
        else:

            error_window = tk.Toplevel(self)
            error_window.title("Login Error")

            label_error = tk.Label(error_window, text="Invalid username or password!")
            label_error.pack(pady=10)

class OrderForm(tk.Tk):

    def __init__(self, login_form): 
        super().__init__()
        self.title("Order Form")
        self.login_form = login_form
        
        self.label_item = tk.Label(self, text="Item:")
        self.label_item.grid(row=0, column=0)
        self.entry_item = tk.Entry(self)
        self.entry_item.grid(row=0, column=1)

        self.label_quantity = tk.Label(self, text="Quantity:")
        self.label_quantity.grid(row=1, column=0)
        self.entry_quantity = tk.Entry(self)
        self.entry_quantity.grid(row=1, column=1)
    
        self.button_login = tk.Button(self, text="Submit", command=self.submit)
        self.button_login.grid(row=2, columnspan=2, pady=10)

        self.button_exit = tk.Button(self, text="Exit", command=self.exit_form)
        self.button_exit.grid(row=2, columnspan=1, pady=10)

    def submit(self):
        item = self.entry_item.get()
        quantity = self.entry_quantity.get()
        
        print(f"Order placed: Item={item}, Quantity={quantity}")
    
    def exit_form(self):
        self.withdraw()
        self.login_form.deiconify()
    

if __name__ == "__main__":
    login_form = LoginForm()
    login_form.mainloop()
